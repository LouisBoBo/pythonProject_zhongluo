# MES 查数配置 · 同事一页纸

> 详细架构见 [`MES_Dify工作流优化说明.md`](./MES_Dify工作流优化说明.md) §11。

---

## 只需记住 3 个「手改入口」

| # | 改什么 | 文件 |
|---|--------|------|
| ① | 维表 JOIN、中文列名、列表默认少 JOIN | **`mes_dimension_joins.map`** |
| ② | 表字段、关联关系 | **`../中络项目MES 系统数据库表结构V1.2.md`** |
| ③ | 选表清单（表名+业务含义） | **`../中络项目MES 系统表名清单V1.2.md`** |

**不要手改**：`dify_*.py`、`mes_dimension_joins.json`（都是脚本生成的）。

改 LLM 话术 → 仓库根目录 `中络项目MES *.md`，复制到 Dify 对应 LLM 的 SYSTEM，**不用跑脚本**。

---

## 改完代码配置：一条命令

```bash
cd 读取MES配置维表
python3 build_all.py
```

然后到 Dify **全文替换** 这 3 个代码节点，并 **发布** workflow：

| 生成文件 | Dify 节点 |
|----------|-----------|
| `dify_mes_table_catalog.py` | 输出表名清单 |
| `dify_mes_schema_by_tables.py` | 表结构（**当前**：`tables_json`；**调序后**可接维表 `fact_table`+`join_tables`） |
| `dify_mes_dimension_node.py` | 维表映射 |

**Dify 接线 · 当前线上（不改 workflow 顺序）**：

| 入参 | 来源 |
|------|------|
| `tables_json` | 选表 LLM 的 `text` |

**可选 · 调序后启用最小 schema**（维表移到 schema 前）：

| 入参 | 来源 |
|------|------|
| `fact_table` | `{{#维表节点.fact_table#}}` |
| `join_tables` | `{{#维表节点.join_tables#}}` |

仅更新代码、不改 Dify 顺序时行为与旧版完全一致。

另 2 个代码节点**很少改**，不用每次 build：

| 文件 | Dify 节点 |
|------|-----------|
| `fix_mes_sql_nolock.py` | SQL 修复（入参 `sql` + `user_question`） |
| `dify_mes_sql_db_validate_node.py` | **SQL 列校验**（fix 之后、text2data 之前，**推荐**） |
| `dify_current_datetime.py` | 当前时间 |
| `dify_mes_sql_rules_db_read.py` | 读取约束规则（**循环外** → `rule_list`） |
| `dify_mes_sql_rules_db_write.py` | 写入学习规则（**循环内**报错后） |

---

## SQL 约束规则（PostgreSQL · 表 `mes_sql_rules`）

| 层级 | 时机 | 接到 SQL LLM |
|------|------|--------------|
| 持久 learned | **循环外** | 【规则约束】`{{#读取SQL约束规则.rule_list#}}` |
| 当轮报错规则 | **循环内** | 【新增约束规则】`{{#conversation.add_rules#}}` |

```bash
python3 build_mes_sql_rules_db_bundle.py   # 打包读/写节点
python3 build_mes_sql_db_validate_bundle.py  # 打包 SQL 列校验节点（与 ERP 共用核心）
python3 seed_mes_sql_rules.py              # 改 base 约束 md 后
python3 seed_mes_sql_learned_rules.py      # 可选：预置 learned
```

## 提示词文件（改完直接粘 Dify SYSTEM）

| 文件 | Dify 节点 |
|------|-----------|
| `dify_mes_table_select_system_prompt.md` | 分析业务表 |
| `../中络项目MES MES生成SQL提示词.md` | SQL 生成（连线 `dimension_rules`） |
| `../中络项目MES 问题分类器.md` | 查询 / 追问 分类（若启用） |
| `../中络项目MES 历史数据回复用户问题.md` | 历史能否回答（若启用） |

---

## `.map` 最常改的两行（写在 `[映射]` 前面）

```text
精简规则=是
列表默认=主表
```

表示：列表查询只出本表列 + 枚举，默认不 JOIN 维表（用户点名「姓名/机台/明细」再 JOIN）。

---

## 发布前检查（30 秒）

- [ ] 跑了 `python3 build_all.py` 且无报错  
- [ ] 3 个 `dify_*.py` 已全文复制到 Dify  
- [ ] 若改了 `.md` 提示词，已同步到 LLM SYSTEM  
- [ ] 点击 **发布** workflow（不发布不生效）

**回归 3 问**（可选）：近一个月维修工单 / A36 生产记录 / 按批次查报工模板项。

---

## 本地试规则（可选）

```bash
python3 mes_dimension_rules.py --question "查询近一个月维修工单"
```

---

## 换项目 / 新库（以后）

复制本目录结构，替换 ①②③ 三个 md/map，再跑 `build_all.py`；workflow 骨架不变。  
批量生成 `.map`：`python3 generate_dimension_map_from_schema.py`（**会覆盖**，先备份）。
