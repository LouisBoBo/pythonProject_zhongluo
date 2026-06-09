# ERP 查数配置 · 同事一页纸

> 详细架构见 [`ERP_Dify工作流优化说明.md`](./ERP_Dify工作流优化说明.md) §11。

---

## 只需记住 3 个「手改入口」

| # | 改什么 | 文件 |
|---|--------|------|
| ① | 维表 JOIN、中文列名、列表默认少 JOIN | **`erp_dimension_joins.map`** |
| ② | 表字段、关联关系 | **`../中络项目ERP 系统数据库表结构V1.0.md`** |
| ③ | 选表清单（表名+业务含义） | **`../中络项目ERP 系统表名清单V1.0.md`** |

**不要手改**：`dify_*.py`、`erp_dimension_joins.json`、`erp_table_schemas.json`（都是脚本生成的）。

改 LLM 话术 → 仓库根目录 `中络项目MES ERP生成SQL提示词.md` 等，复制到 Dify 对应 LLM 的 SYSTEM，**不用跑脚本**。

---

## 改完代码配置：一条命令

```bash
cd 读取ERP配置维表
python3 build_all.py
```

然后到 Dify **全文替换** 这 3 个代码节点，并 **发布** workflow：

| 生成文件 | Dify 节点 |
|----------|-----------|
| `dify_erp_table_catalog.py` | 输出表名清单 |
| `dify_erp_schema_by_tables.py` | 表结构 |
| `dify_erp_dimension_node.py` | 维表映射 |
| `dify_erp_sql_fix_node.py` | **SQL 修复**（LLM 之后，**必加**） |
| `dify_erp_sql_db_validate_node.py` | **SQL 列校验**（fix 之后、text2data 之前，**推荐**） |

另 1 个代码节点**很少改**，不用每次 build：

| 文件 | Dify 节点 |
|------|-----------|
| `dify_current_datetime.py` | 当前时间 |

**SQL 修复节点入参**：`query_sql`（或 `sql`）← LLM 输出；`user_question` ← `{{#sys.query#}}`  
**SQL 列校验节点入参**：`fixed_sql` ← fix 节点；`server/port/username/password/database` ← 与 text2data **同一 ERP 库**  
**出参**：`fixed_sql`（接到 text2data）；可选调试 `was_changed`、`removed_columns`、`tables_checked`、`table_column_counts`、`validate_error`

核心逻辑在 **`sql_db_validate_core.py`**（MES 侧 `dify_mes_sql_db_validate_node.py` 共用，环境变量前缀分别为 `ERP_DB_*` / `MES_DB_*`）。

Dify 沙箱需安装：`pip install sqlalchemy pymssql`

---

## 提示词文件（改完直接粘 Dify SYSTEM）

| 文件 | Dify 节点 |
|------|-----------|
| `dify_erp_table_select_system_prompt.md` | 分析业务表 |
| `../中络项目MES ERP生成SQL提示词.md` | SQL 生成（连线 `dimension_rules` + `rule_list`） |
| `../中络项目ERP SQL约束规则提示词.md` | base 约束（入库 `erp_sql_rules`，非直接粘 LLM） |

---

## SQL 约束规则（PostgreSQL · 表 `erp_sql_rules`）

与 MES 的 `mes_sql_rules` **完全独立**。

| 层级 | 时机 | 文件 / 变量 | 接到 SQL LLM |
|------|------|-------------|--------------|
| 持久 learned | **循环外** | `dify_erp_sql_rules_db_read.py` → `rule_list` | 【规则约束】 |
| 当轮报错规则 | **循环内** | `tiqu_error_rule` → `conversation.add_rules` | 【新增约束规则】 |
| 持久化写入 | **循环内**报错后 | `dify_erp_sql_rules_db_write.py` | （写 DB，供下次 rule_list） |

```bash
python3 seed_erp_sql_rules.py              # 首次 / 改 base 约束 md 后
python3 seed_erp_sql_learned_rules.py      # 可选：预置 learned
```

---

## `.map` 最常改的两行（写在 `[映射]` 前面）

```text
精简规则=是
列表默认=主表
```

表示：列表查询只出本表列 + 枚举，默认不 JOIN 维表（用户点名「姓名/工厂/明细」再 JOIN）。

---

## 发布前检查（30 秒）

- [ ] 跑了 `python3 build_all.py` 且无报错
- [ ] 3 个 `dify_*.py` 已全文复制到 Dify
- [ ] 若改了 `.md` 提示词，已同步到 LLM SYSTEM
- [ ] 点击 **发布** workflow（不发布不生效）

**回归 3 问**（可选）：制成品接收明细 / 制造订单列表 / 采购订单明细。

---

## 本地试规则（可选）

```bash
python3 erp_dimension_rules.py --question "查制成品接收明细"
```

---

## 与 MES 的边界

- ERP 配置**全部**在 `读取ERP配置维表/`；MES 在 `读取MES配置维表/`，**互不影响**。
- ERP 表前缀 `P_`/`M_`/`S_`/`FGI_`/`T_` 等；**禁止**在 ERP workflow 中使用 MES 的 `TBL_*` 表。

---

## 换项目 / 新库（以后）

复制本目录结构，替换 ①②③ 三个 md/map，再跑 `build_all.py`；workflow 骨架不变。
批量生成 `.map`：`python3 generate_dimension_map_from_schema.py`（**会覆盖**，先备份）。
