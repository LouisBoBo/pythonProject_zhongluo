# MES 自然语言 → SQL 工作流优化说明

本文档总结 MES Dify 工作流本轮优化策略、架构分工、实测效果与维护方式。

---

## 0. 优化成果摘要（2026-06）

| 节点 | 优化前 | 优化后 | 状态 |
|------|--------|--------|------|
| 表名清单（代码预排序） | 全量 177 张 ~57k token | Top-N 候选 ~2.5k~4.7k token | ✅ 已上线 |
| 分析业务表（LLM 选表） | ~8s，completion ~1300 | 明显下降，completion ~40~100 | ✅ 已上线 |
| 表结构（代码拼 schema） | 知识库逐表检索 | 毫秒级 | ✅ 已上线 |
| 维表映射（代码） | 完整规则 ~11k 字/表 | 精简规则 ~4.7k（SFC/EAM） | ✅ 已配置 |
| **SQL 生成（LLM）** | prompt ~29k，~10~11s | **仍约 ~12s** | ⚠️ 可接受，仍有空间 |

**结论**

- **选表链路**已从主要瓶颈中移除（代码预筛 + LLM 终选 + 精简 JSON）。
- **SQL 生成**仍是整条链路最慢环节（大 SYSTEM + 维表规则 + 长 SQL 输出）；已做 schema 瘦身、精简维表、列表默认少 JOIN，实测仍约 **12s**，与优化前同量级，**整体 workflow 体感已可接受**。
- 架构定为：**代码加速 + LLM 保准确度**，不采用纯代码选表。

---

## 1. 背景与目标

**原问题**

- 「分析业务表」LLM 节点 prompt 过大（全量 177 张表 + 关联说明），单次 prompt 约 **57k token**，节点耗时约 **8s**。
- LLM 输出冗长 JSON（`scene`、`reason`、`excluded_tables` 等），completion 约 **1300 token**，进一步拖慢选表。
- 知识库逐表检索表结构慢，SQL 生成 prompt 冗余。

**优化目标**

- 降低选表与 SQL 生成延迟，同时 **保留 LLM 最终选表**（语义消歧，如维修工单 vs 生产工单）。
- 用 **代码节点** 替代慢路径（知识库检索、全量表清单），不引入按业务硬编码选表。

---

## 2. 总体架构

采用 **「代码预筛 + LLM 终选 + 代码拼 schema」** 分层：

```
用户问题 sys.query
    │
    ▼
┌──────────────────────────────┐
│ 代码：输出表名清单 (v4)         │  177 张 → 约 12~40 张候选
│ dify_mes_table_catalog.py     │  输出 table_catalog
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ LLM：分析业务表                 │  从候选清单终选
│ dify_mes_table_select_system_prompt.md │
│ 输出精简 JSON tables           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 代码：按表拼 schema             │  毫秒级；入参 tables_json（**当前线上**）
│ dify_mes_schema_by_tables.py  │  或 fact_table+join_tables（**调序后**）
└──────────────┬───────────────┘
               │
               ▼
    dimension / sql_rules / datetime          ← 循环外：读 DB rule_list
               │
               ▼
         SQL LLM → fix_sql → db_validate → text2data
               │
               └── 报错（循环内）→ tiqu_error_rule → conversation.add_rules
                                    └→ dify_mes_sql_rules_db_write.py → mes_sql_rules
```

**分工原则**

| 层级 | 职责 | 不做 |
|------|------|------|
| 代码预排序 | 缩小候选范围、意图加权、补全主从表 | 替代 LLM 做最终业务判断 |
| LLM 选表 | 语义消歧、主/明细/基础表角色划分 | 读全量 177 张表 |
| 代码 schema | 按选中表嵌入字段说明 | — |
| SQL LLM | 生成 SQL | 选表 |

---

## 3. 选表阶段优化

### 3.1 精简表清单（Catalog Slim）

- **来源**：`中络项目MES 系统表名清单V1.2.md`
- **格式**：每表一行 `TBL_XXX | 中文表名 | 业务含义`，去掉章节说明与关联关系。
- **规模**：177 张表，约 **9928 字符**（原完整清单约 **67434 字符**，约减 **86%**）。
- **实现**：`mes_table_catalog.py` → `build_mes_catalog_bundle.py` → 嵌入 `dify_mes_table_catalog.py`（Dify 沙箱不读磁盘）。

### 3.2 通用预排序（Rank）

- **实现**：`mes_table_catalog_rank.py`
- **方法**：从用户问题提取中文 n-gram（2~6 字）及英文 token，对 catalog 每行打分；取得分 Top-N（默认 35）作为 LLM 候选。
- **无业务硬编码**：不维护「维修工单 → 固定表列表」类规则。

**意图加权（`_apply_intent_boosts`）**

| 问题特征 | 处理方式 |
|----------|----------|
| 含「生产记录 / 报工 / 过站」 | 优先 `TBL_SFC_WS_LOG`、`TBL_SFC_WS_LOG_ITEM`；EAP/PATTERN 设备日志降权 |
| 含「工序」 | `TBL_BD_PROCESS` 适度加分 |

**关联表补全（`_expand_related_tables`）**

- 主表选中后自动补常见子表（如 `TBL_FA_YHYJ_MAIN` → `TBL_FA_YHYJ_MI`，`TBL_SFC_WS_LOG` → `TBL_SFC_WS_LOG_ITEM`）。
- 子表紧跟主表之后注入，不抬高到清单顶部。

### 3.3 LLM SYSTEM 提示词

- **文件**：`dify_mes_table_select_system_prompt.md`（**仅**粘贴到 LLM SYSTEM，不含 Dify 接线说明）。
- **候选清单**：`{{#输出表名清单.table_catalog#}}` 动态注入，不再在 SYSTEM 内贴 336 行全表。
- **业务消歧**（提示词约束，非代码硬编码）：
  - 设备维修工单 → `TBL_EAM_REPAIR`，非 `TBL_MO`
  - 工序生产记录 → 主表 `TBL_SFC_WS_LOG`；`TBL_FA_*` 为 FA 补充，不可替代 SFC 主表
  - 采购收货 → SRM 模块；IPQC → QM 模块
- **输出 JSON**（精简，便于下游解析、降低 completion）：

```json
{"tables":[{"table_name":"TBL_XXX","score":95,"table_role":"主业务表"}]}
```

### 3.4 Dify 配置要点

| 节点 | 配置 |
|------|------|
| 输出表名清单（代码） | 脚本 `dify_mes_table_catalog.py`；入参 `user_question` = `{{#sys.query#}}` |
| 分析业务表（LLM） | SYSTEM = `dify_mes_table_select_system_prompt.md` 全文；USER = 仅一条 `{{#sys.query#}}` |
| 表结构（代码） | **推荐**：`fact_table` + `join_tables` = 维表节点；兼容旧：`tables_json` = LLM text |

**常见错误**

- SYSTEM 写死示例问题（如「维修工单」）。
- USER 重复两条相同内容。
- 把运维/接线说明贴进 SYSTEM。

---

## 4. Schema 与 SQL 阶段优化（同期完成）

### 4.1 按表拼 schema（替代知识库）

- **文件**：`dify_mes_schema_by_tables.py`（由 `build_mes_schema_bundle.py` 生成）。
- **推荐 workflow 顺序**（ERP 文档 §3.1 同样标注为「推荐」，**ERP/MES 线上多为旧顺序**）：

```
【当前线上 · ERP/MES 常见】
选表 LLM → schema（tables_json）→ 维表 → SQL LLM

【启用 fact_table/join_tables 减 prompt 时】
选表 LLM → 维表 → schema（fact_table + join_tables）→ SQL LLM
```

维表节点**只需** `user_question`，不依赖选表 JSON；但 schema 要接 `fact_table`/`join_tables` 时，**维表必须在 schema 之前**（旧顺序下无法把维表出参接回 schema）。

- **入参**：
  - **推荐**：`fact_table={{#维表节点.fact_table#}}`，`join_tables={{#维表节点.join_tables#}}`（可不传 `tables_json`）
  - **兼容旧版**：仍只接 `tables_json` / `tables` 时行为与改前一致（全量表、不截断）
  - `max_tables`：仅维表路径生效，默认 8
- **出参**：`context`（参考表结构文本）、`found_tables`、`missing_tables`。
- **效果**：选表后毫秒级出 schema；接维表后只拼事实表 + JOIN 维表，显著减少 SQL LLM token。

### 4.2 Schema 瘦身

- `mes_schema_by_tables.py` 中 `slim_schema_section()`：去掉关联关系段，减少 SQL LLM prompt。

### 4.3 SQL 规则与维度

**约束规则两层（与 ERP 同构）**：

| 变量 | 位置 | 来源 | 接到 SQL LLM |
|------|------|------|--------------|
| `rule_list` | **循环外** | `dify_mes_sql_rules_db_read.py` | 【规则约束】 |
| `add_rules` | **循环内** | 报错提取 → `conversation.add_rules` | 【新增约束规则】 |

- **Learned 持久化**：循环内 `dify_mes_sql_rules_db_write.py` 写入 `mes_sql_rules`；循环外读节点只返回 learned，**不含 base**
- **基础约束**：`中络项目MES SQL约束规则提示词.md` 或 SQL LLM SYSTEM 正文
- **维度映射**：`dify_mes_dimension_node.py` → `dimension_rules`
- **维护脚本**：`seed_mes_sql_rules.py`、`seed_mes_sql_learned_rules.py`、`build_mes_sql_rules_db_bundle.py`

### 4.4 多表主从明细 · TOP (1000)（2026-06）

**Dify 约束**：明细查询**必须** `SELECT TOP (1000)`，超过 1000 行出参 token 超限会报错，**禁止省略 TOP**。

**主表 + 明细 JOIN**：TOP 限制 JOIN 后最多 1000 行；须 `ORDER BY` 主表时间 DESC + 明细 CSEQ ASC，优先返回最新主记录及有序模板项。用户问「全部/每一项」时，在【相关表】说明单次上限。

**代码**：`mes_sql_multijoin.py`（维表节点注入排序提示；fix 节点仅在缺 TOP 时补 `TOP (1000)`，**不再删除 TOP**）。

---

## 5. 效果对比（实测 trace）

### 5.1 选表阶段（已达标）

| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| 分析业务表 prompt | ~56,937 token | ~2,500~4,700 token |
| 分析业务表 completion | ~1,301 token | ~38~100 token |
| 分析业务表 latency | ~8s | **明显下降**（用户确认） |
| 表清单来源 | SYSTEM 贴全表 / 知识库 | 代码节点 `table_catalog` 动态注入 |

### 5.2 SQL 生成阶段（当前瓶颈，约 12s）

| 指标 | 优化前（样例：客户 A36 生产记录） | 优化后（同场景） |
|------|----------------------------------|------------------|
| prompt_tokens | ~28,677 | 仍偏大（SYSTEM 全业务段 + 维表 + schema + learned） |
| completion_tokens | ~2,595 | 视模型是否遵守「列表默认少 JOIN」而定 |
| latency | ~11.5s | **~12s 量级**（用户确认：差不多，可接受） |
| 表结构获取 | 知识库循环 | 代码节点毫秒级 |

### 5.3 端到端

- 选表从 ~8s 降下来后，**总耗时主要由 SQL LLM 决定**（约 12s）。
- 模型：Qwen3-4B-Instruct-2507-FP8；大 prompt + 长 T-SQL（多列 CASE + 中文别名）是主要耗时来源。

---

## 6. 关键文件清单

| 文件 | 用途 |
|------|------|
| `中络项目MES 系统表名清单V1.2.md` | 表清单源数据（维护入口） |
| `中络项目MES 查找业务关联表.md` | 选表参考文档（历史全量清单版，查阅用） |
| `mes_table_catalog.py` | 精简 catalog 生成 |
| `mes_table_catalog_rank.py` | 通用预排序 + 意图加权 |
| `build_mes_catalog_bundle.py` | 打包 → `dify_mes_table_catalog.py` |
| `dify_mes_table_catalog.py` | Dify 代码节点 v4 |
| `dify_mes_table_select_system_prompt.md` | Dify LLM SYSTEM 提示词 |
| `build_mes_schema_bundle.py` | 打包 → `dify_mes_schema_by_tables.py` |
| `dify_mes_schema_by_tables.py` | Dify 按表拼 schema |
| `dify_mes_dimension_node.py` | 维度规则节点 |
| `mes_dimension_joins.map` | 维表映射维护入口 |
| `中络项目MES MES生成SQL提示词.md` | SQL 生成 LLM SYSTEM |
| `dify_mes_sql_rules_db_read.py` | DB learned 规则读取 |
| `fix_mes_sql_nolock.py` | SQL 修复（NOLOCK / 截断 / 多表 TOP） |
| `mes_sql_multijoin.py` | 多表主从 TOP 策略检测与修复 |

---

## 7. 维护流程

### 7.1 表清单变更

1. 修改 `中络项目MES 系统表名清单V1.2.md`
2. 执行：

```bash
cd 读取MES配置维表
python3 build_mes_catalog_bundle.py
```

3. 将生成的 `dify_mes_table_catalog.py` 复制到 Dify「输出表名清单」代码节点并发布。

### 7.2 表结构变更

1. 修改 `中络项目MES 系统数据库表结构V1.2.md`
2. 执行 `python3 build_mes_schema_bundle.py`
3. 更新 Dify schema 代码节点。

### 7.3 预排序逻辑变更

1. 修改 `mes_table_catalog_rank.py`
2. 执行 `python3 build_mes_catalog_bundle.py`
3. 本地抽样验证：

```bash
python3 -c "
from mes_table_catalog import load_catalog_text, slim_catalog_text
from mes_table_catalog_rank import rank_catalog_lines
slim = slim_catalog_text(load_catalog_text())
for q in ['查询近一个月维修工单', '压合工序生产记录', 'IPQC检验记录']:
    _, n, mode = rank_catalog_lines(q, slim)
    print(q, mode, n)
"
```

### 7.4 LLM 选表提示词变更

- 编辑 `dify_mes_table_select_system_prompt.md`，同步到 Dify「分析业务表」LLM SYSTEM。
- 勿将 Dify 接线说明写入该文件。

### 7.5 维表 / SQL 规则变更

1. 修改 `mes_dimension_joins.map`（`精简规则=是` 须写在 `[映射 …]` **之前**）
2. 执行 `python3 build_dify_bundle.py`
3. 复制 `dify_mes_dimension_node.py` 到 Dify 并发布
4. 同步 `中络项目MES MES生成SQL提示词.md` 到 SQL LLM SYSTEM

---

## 8. 设计约束（后续扩展请遵守）

1. **LLM 保留终选权**：代码只做预筛与加速，不整体替换 LLM 选表（除非明确要求）。
2. **预排序保持通用**：优先 token 匹配 + 意图加权；避免「一问一表」硬编码映射。
3. **提示词与运维文档分离**：LLM SYSTEM 仅含角色、规则、变量占位符。
4. **JSON 输出最小化**：下游 `dify_mes_schema_by_tables` 只需 `table_name` 列表，不必让 LLM 生成解释性字段。
5. **消歧写进 SYSTEM**：MO/EAM、SFC/FA/EAP 等易混场景在提示词中明确，而非仅靠排序分数。

---

## 9. SQL 生成阶段优化

### 9.1 已落地改动

| 改动 | 文件 | 效果 |
|------|------|------|
| schema 去掉关联关系 | `build_mes_schema_bundle.py` → `dify_mes_schema_by_tables.py` | 单表 schema ~1.6k 字，无「关联关系」块 |
| 生产记录精简维表 | `mes_dimension_joins.map` → `TBL_SFC_WS_LOG` | 维表规则 ~11k → ~4.7k 字；列表默认不 JOIN |
| 维修工单精简维表 | 同上 → `TBL_EAM_REPAIR` | 同上（此前已配） |
| SYSTEM 列表默认策略 | `中络项目MES MES生成SQL提示词.md` | 「列表默认不 JOIN 维表」，与维表规则一致 |
| learned 规则分离 | `dify_mes_sql_rules_db_read.py` | DB 只读增量；基础规则在 SYSTEM |

### 9.2 实测结果

- 样例：「查询客户编码 A36 的生产记录」
- SQL LLM latency：**约 12s**（与优化前 ~11.5s 同量级，用户评估可接受）
- 原因：SYSTEM 仍含全业务段落（采购/化验/用户等）；completion 仍可能输出长 SQL（多列 CASE + 中文别名）

### 9.3 Dify 部署清单（SQL 相关）

1. `python3 build_dify_bundle.py` → 更新 **维表** 代码节点
2. `python3 build_mes_schema_bundle.py` → 更新 **表结构** 代码节点
3. **（可选）调整 workflow 顺序以启用最小 schema** — ERP 文档同样写为「推荐」，**并非 ERP 已上线的新顺序**：
   - **当前线上（ERP/MES 常见）**：选表 → **schema** → **维表** → SQL LLM（schema 仍用 `tables_json`，**与改代码前一致**）
   - **启用优化时**：选表 → **维表** → **schema** → SQL LLM，schema 接 `fact_table` / `join_tables`
4. **schema 节点入参**（推荐）：
   - `fact_table` = `{{#维表节点.fact_table#}}`
   - `join_tables` = `{{#维表节点.join_tables#}}`
   - 可移除 `tables_json`（未改接线前仍兼容全量表）
5. 复制 **`中络项目MES MES生成SQL提示词.md`** → SQL LLM SYSTEM
6. 确认 **fix_mes_sql_nolock.py** 在 SQL LLM 与 text2data 之间
7. **`dify_mes_sql_db_validate_node.py`**（fix 与 text2data 之间，**推荐**）
8. 每次修改后 **发布** workflow

### 9.4 其它表启用精简维表

在 `[表 TBL_XXX]` 内、`[映射 …]` **之前**：

```
精简规则=是
列表默认=主表
默认排序=别名.时间列 DESC, 别名.CID DESC
```

### 9.5 若需继续压 SQL 耗时（可选）

- 清理 PostgreSQL `mes_sql_rules` 中无效 learned 条目，避免 207 约束叠加
- SYSTEM 只保留通用 T-SQL 规范；按表业务段下沉到维表节点输出
- 换更大/faster 推理模型或降低 `SELECT` 默认列数（需业务确认）

---

## 10. 后续可选优化

- SQL SYSTEM 按事实表拆分，只注入当前业务相关段落（预期可再降 prompt）
- 定期清理 learned 规则，避免重试叠加
- 选表 JSON 解析节点（若 LLM 偶发非纯 JSON 输出）
- 预排序参数微调（`top_n`、意图加权）

---

## 11. 维护检查清单（日常照着做）

### 11.1 两条维护线

| 类型 | 维护入口 | 要跑脚本？ | Dify 里改什么 |
|------|----------|------------|---------------|
| **提示词** | 仓库根目录 `中络项目MES *.md` | 否 | 对应 LLM 节点 SYSTEM |
| **代码节点** | `读取MES配置维表/` 源文件 | **是** rebuild | 复制 `dify_*.py` 全文 |

改 `.map` / 表结构 / 表清单 → 本地 rebuild → 复制到 Dify → **发布 workflow**。  
只改 `.md` → 粘贴 SYSTEM → **发布**。

### 11.2 场景 → 改什么 → 命令 → Dify 节点

| 你要改… | 维护文件 | 打包命令 | Dify 节点 |
|---------|----------|----------|-----------|
| 维表 JOIN / 枚举 / 列表默认列 | `mes_dimension_joins.map` | `python3 build_dify_bundle.py` | 维表代码（`dify_mes_dimension_node.py`） |
| 表结构 / schema 最小表集 | `mes_schema_by_tables.py` | `python3 build_mes_schema_bundle.py` | 表结构代码；**维表在 schema 前**，接 `fact_table`+`join_tables` |
| 表字段 / 新表 | `../中络项目MES 系统数据库表结构V1.2.md` | 同上 `build_mes_schema_bundle.py` | 表结构代码 |
| 选表清单 / 预排序 | `../中络项目MES 系统表名清单V1.2.md`、`mes_table_catalog_rank.py` | `python3 build_mes_catalog_bundle.py` | 输出表名清单（`dify_mes_table_catalog.py`） |
| 选表 LLM 消歧 | `dify_mes_table_select_system_prompt.md` | 无 | 分析业务表 LLM SYSTEM |
| SQL 生成规则 | `../中络项目MES MES生成SQL提示词.md` | 无 | SQL LLM SYSTEM（连线 `dimension_rules`） |
| SQL 修复 NOLOCK / TOP | `fix_mes_sql_nolock.py`、`mes_sql_multijoin.py` | 无（维表改 multijoin 时跑 `build_dify_bundle.py`） | fix 节点；入参 `user_question`=`{{#sys.query#}}` |
| **SQL 库表列校验（207 兜底）** | `../读取ERP配置维表/sql_db_validate_core.py`（共用） | `python3 build_mes_sql_db_validate_bundle.py` | `dify_mes_sql_db_validate_node.py`（fix 与 text2data 之间） |
| Learned 报错规则 | PostgreSQL / `seed_mes_sql_rules.py` | `python3 build_mes_sql_rules_db_bundle.py` | 读取 SQL 约束规则节点 |
| 问题分类 查询/追问 | `../中络项目MES 问题分类器.md` | 无 | 分类器 LLM SYSTEM |
| 历史能否复用 | `../中络项目MES 历史数据回复用户问题.md` | 无 | 充分性判定 LLM SYSTEM |

### 11.3 标准发布流程（改代码后）

```bash
cd 读取MES配置维表
python3 build_all.py
```

等价于依次执行 `build_mes_catalog_bundle.py`、`build_mes_schema_bundle.py`、`build_dify_bundle.py`、`build_mes_sql_db_validate_bundle.py`，并自动 `py_compile` 检查 4 个 `dify_*.py`。

单独打包（仅改其中一项时可选）：

```bash
python3 build_mes_catalog_bundle.py   # 仅表清单
python3 build_mes_schema_bundle.py    # 仅表结构
python3 build_dify_bundle.py          # 仅维表 .map
python3 build_mes_sql_rules_db_bundle.py  # 仅 learned 规则节点（少改）
python3 build_mes_sql_db_validate_bundle.py  # 仅 SQL 列校验节点
```

Dify：**替换 4 个 dify 代码节点全文 → 核对连线 → 发布 workflow**。

### 11.4 工作流连线速查

```text
sys.query
  → dify_mes_table_catalog.py          user_question
  → 分析业务表 LLM                     dify_mes_table_select_system_prompt.md
  → dify_mes_schema_by_tables.py       tables_json = LLM text（**当前线上**）
  → dify_mes_dimension_node.py         user_question → dimension_rules, fact_table, join_tables
  → dify_current_datetime.py           current_datetime
  → dify_mes_sql_rules_db_read.py       rule_list（循环外）
  → SQL LLM                            中络项目MES MES生成SQL提示词.md
  → fix_mes_sql_nolock.py              sql + user_question → fixed_sql
  → dify_mes_sql_db_validate_node.py   fixed_sql + DB 连接 → fixed_sql（推荐）
  → text2data
       └─ 报错（循环内）→ tiqu_error_rule → conversation.add_rules
                         → dify_mes_sql_rules_db_write.py → mes_sql_rules
       └─ 重试 → SQL LLM（带 add_rules + 上一次SQL/报错）
```

会话前置（若启用）：`问题分类器.md` → `历史数据回复用户问题.md`。

### 11.5 常见坑

1. **`精简规则=是` 必须在 `[映射]` 之前**，否则解析忽略  
2. **`dify_*.py` 禁止手改**，只改源文件再 rebuild  
3. **`build_dify_bundle.py` 后必须整段复制**，避免 `from __future__` 不在文件头  
4. **TOP (1000) 不能删**（Dify token 上限）；多表 JOIN 靠 ORDER BY 控制优先返回哪 1000 行  
5. **维修工单 ≠ 生产工单**：选表见 `dify_mes_table_select_system_prompt.md`；历史判定见 `历史数据回复用户问题.md`  
6. **LLM SYSTEM 与运维文档分离**；接线说明只写在本目录 `readme.md` / 本文档

### 11.6 改完回归样例（Dify 上跑 3 条）

| 样例问题 | 检查点 |
|----------|--------|
| 查询近一个月维修工单 | 选表含 `TBL_EAM_REPAIR`；历史判定为 `不可以` |
| 查询客户编码 A36 的生产记录 | SFC 精简规则；列表默认少 JOIN |
| 按工单批次 WOA… 查报工+模板项 | `TOP (1000)` 保留；`mo.CUST_CODE` 与 `l.CUSTOMER_CODE` 分列 |

### 11.7 本地快速验证

```bash
cd 读取MES配置维表
python3 mes_dimension_rules.py --question "查询近一个月维修工单"
python3 -c "from mes_schema_by_tables import _normalize_table_names; print(_normalize_table_names('{\"tables\":[{\"table_name\":\"TBL_MO\"}]}'))"
python3 -c "from mes_sql_multijoin import build_multijoin_query_hints; print(build_multijoin_query_hints('按批次查报工模板每一项')[:200])"
```

---

*文档版本：2026-06 · 选表 v4 + SQL 精简维表 + 多表 TOP 策略 + 维护清单 §11。*
