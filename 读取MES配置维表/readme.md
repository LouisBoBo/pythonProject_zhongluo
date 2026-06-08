# MES Dify 工作流 · 维护入口

本目录是 **自然语言 → SQL** 链路的代码与维表配置根目录。  
**完整维护清单（场景表、发布流程、连线、回归样例）** → [`MES_Dify工作流优化说明.md` §11](./MES_Dify工作流优化说明.md#11-维护检查清单日常照着做)。

---

## 日常只需关心什么

| 你要改… | 手改文件 | 打包命令 | Dify |
|---------|----------|----------|------|
| 维表 JOIN / 中文列 / 列表默认 | `mes_dimension_joins.map` | `python3 build_dify_bundle.py` | `dify_mes_dimension_node.py` |
| 表结构字段 | `../中络项目MES 系统数据库表结构V1.2.md` | `python3 build_mes_schema_bundle.py` | `dify_mes_schema_by_tables.py` |
| 选表清单 | `../中络项目MES 系统表名清单V1.2.md` | `python3 build_mes_catalog_bundle.py` | `dify_mes_table_catalog.py` |
| SQL / 选表 / 分类 / 历史判定 规则 | `../中络项目MES *.md` | 无 | 对应 LLM SYSTEM |

**不要手改**：`dify_*.py`、`mes_dimension_joins.json`（均由 build 脚本生成）。

---

## 维表 `.map` 快速维护

### 文件关系

| 文件 | 作用 |
|------|------|
| `mes_dimension_joins.map` | **维护入口**（表格式） |
| `mes_dimension_joins.json` | build 自动生成 |
| `dify_mes_dimension_node.py` | 复制到 Dify 维表代码节点 |
| `mes_dimension_rules.py` | 规则文本生成逻辑 |
| `parse_dimension_map.py` | `.map` 解析器 |
| `build_dify_bundle.py` | 打包（含 `mes_sql_multijoin.py`） |
| `generate_dimension_map_from_schema.py` | 从表结构**批量重生成**整个 `.map`（会覆盖，先备份） |

### 加一张新表（3 步）

1. 更新 `../中络项目MES 系统数据库表结构V1.2.md`（含关联关系）
2. 在 `mes_dimension_joins.map` 末尾复制类似表块，改表名/别名/映射  
   - `精简规则=是`、`列表默认=主表` 写在 **`[映射]` 之前**
3. `python3 build_dify_bundle.py` → 复制 `dify_mes_dimension_node.py` → Dify **发布**

### `.map` 写法速查

```text
[全局]
默认别名=l
禁止=……

[表 TBL_表名]
标签=中文表名
关键词=词1, 词2
别名=SQL别名
精简规则=是          # 可选，须在 [映射] 前
列表默认=主表        # 可选
默认排序=l.CSTART_TIME DESC, l.CID DESC

[映射 item]
字段=CITEM_ID
关联=i | TBL_BD_ITEM | i.CID = l.CITEM_ID
列=i.CITEM_NO | 料号
列=i.CITEM_NAME | 品名
禁止=错误写法
```

### 常见字段 → 抄哪段

| 事实表字段 | 映射 |
|-----------|------|
| `CWC_ID` | `[映射 work_center]`，`wc` + `wc_p` |
| `CPROCESS_ID` | `[映射 process]` |
| `CITEM_ID` | `[映射 item]` |
| `CSTART_USER_NAME` / `CEND_USER_NAME` | `类型=账号` → `TBL_SYS_USER` |
| `CMO_LOT` | 参考 `TBL_SFC_WS_LOG` 的 `[映射 mo_lot]` |

`TBL_SFC_WS_LOG`：`CUSTOMER_CODE`（非 `CCUSTOMER_CODE`）、`CSCAN_BARCODE`、明细 JOIN 用 `l.CID = i.CWS_LOG_ID`。

---

## 改完必做

```bash
cd 读取MES配置维表
python3 build_dify_bundle.py          # 改了 .map 或 mes_sql_multijoin
python3 build_mes_schema_bundle.py    # 改了表结构 md
python3 build_mes_catalog_bundle.py   # 改了表名清单 md
python3 -m py_compile dify_mes_dimension_node.py   # 推荐
```

Dify：**替换节点 → 发布 workflow**。

---

## 本地验证

```bash
python3 mes_dimension_rules.py --question "查询近一个月维修工单"
python3 mes_dimension_rules.py TBL_SFC_WS_LOG
```

---

## 相关文档（仓库根目录）

| 文档 | 用途 |
|------|------|
| [`MES_Dify工作流优化说明.md`](./MES_Dify工作流优化说明.md) | 架构、效果、**§11 维护清单** |
| `../中络项目MES MES生成SQL提示词.md` | SQL LLM SYSTEM |
| `dify_mes_table_select_system_prompt.md` | 选表 LLM SYSTEM |
| `../中络项目MES 问题分类器.md` | 查询 / 追问 路由 |
| `../中络项目MES 历史数据回复用户问题.md` | 历史数据 可以/不可以 |
| `../中络项目MES SQL约束规则提示词.md` | 约束规则（seed / 参考） |
| `fix_mes_sql_nolock.py` | SQL 修复节点（NOLOCK + TOP 兜底） |
