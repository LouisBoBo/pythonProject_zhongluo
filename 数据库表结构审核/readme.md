# 数据库表结构审核

## 文件说明

| 文件 | 说明 |
|------|------|
| `mes_db_schema_audit_rules.yaml` | **审核规则**（SQL Server 通用 + 中络 MES 命名/公共字段习惯） |
| `dify_get_db_scheme.py` | Dify 节点①：采集库表结构 |
| `dify_audit_db_scheme.py` | Dify 节点②：按规则审核 |
| `get_db_scheme.md` | 采集节点说明 |
| `审核报告提示词.md` | Dify 节点③ LLM：生成 Markdown 审核报告 |

## 审核规则概览

规则文件 `mes_db_schema_audit_rules.yaml`（v1.2）审核维度：

**主审（四类）**

1. **命名规范**：表/字段/索引/外键命名，`TBL_`、`C` 前缀等 MES 习惯  
2. **字段类型**：长度、MAX 滥用、`DATETIME2`、主外键禁用浮点、金额用 `DECIMAL`  
3. **主外键约束**：主键存在且非空、外键字段有效、命名规范  
4. **索引设计**：外键列覆盖索引、重复索引、索引过多、索引命名  

**辅审（专业性补充）**

5. **文档与注释**：表/字段 `MS_Description`  
6. **MES 企业标准**：`CID`、审计字段、`CSTATE` 等  
7. **对象治理**：测试/备份/临时表识别  
8. **表结构设计**：字段数过少、重复列名  

采集节点需开启 `include_indexes=true`（默认已开）方可做索引审核。

**评分**：error 扣 10 分、warning 扣 3 分；存在 error 即「不通过」。

关联表（`_MAP` / `_LINK` / `_ITEM` 等）不强制 `CID` 与完整审计字段。

> 已移除 V1.2 固定基准 JSON 对比：换库/换项目可直接审，不再绑定 `mes_baseline_v12.json`。

## 本地一键：采集 + 审核

```bash
cd 数据库表结构审核
python3 -m pip install sqlalchemy pymssql

# 指定表审核
python3 run_audit_local.py '{"table_names":"TBL_SYS_DICTIONARY,TBL_MO"}'

# 全库审核（耗时长，CIMOM_TEST 约 726 表）
python3 run_audit_local.py '{}'
```

仅审核、不重新连库时，可将 `schema_data` 传给 `dify_audit_db_scheme.main(schema_data=...)`。

## Dify 手把手配置

### 整体流程（3 个节点）

```mermaid
flowchart LR
  A[开始] --> B[代码① 采集表结构]
  B --> C[代码② 规则审核]
  C --> D[LLM 生成报告]
  D --> E[结束]
```

| 步骤 | 节点类型 | 做什么 |
|------|----------|--------|
| 1 | **开始** | 传入数据库连接、要审的表名（可选） |
| 2 | **代码** | 连 SQL Server，输出 `schema_data` |
| 3 | **代码** | 按规则审核，输出 `violations_json` |
| 4 | **LLM** | 根据 `violations_json` 生成 Markdown 报告 |

---

### 第 0 步：安装 Python 依赖

在 Dify **设置 → 代码执行 / 沙箱** 里添加（两个代码节点都要能 import）：

```text
sqlalchemy
pymssql
```

---

### 第 1 步：「开始」节点 — 定义输入变量

| 变量名 | 必填 | 示例值 | 说明 |
|--------|------|--------|------|
| `server` | 是 | `192.168.49.10` | 数据库地址 |
| `port` | 否 | `1433` | 端口 |
| `username` | 是 | `sa` | 用户名 |
| `password` | 是 | `***` | 密码 |
| `database` | 是 | `CIMOM_TEST` | 库名（可换任意 SQL Server 库） |
| `table_names` | 否 | `TBL_MO,TBL_SYS_DICTIONARY` | 建议首次填写；留空=读全库 |
| `max_tables` | 否 | `0` | 最多读几张表，`0`=不限制 |
| `rules_yaml` | 否 | （见下） | 规则全文；留空则用脚本同目录默认规则 |

\* Dify 沙箱读不到本机 YAML 时，将 `mes_db_schema_audit_rules.yaml` **全文**粘贴到 `rules_yaml`。

---

### 第 2 步：代码节点①「采集表结构」

复制 `dify_get_db_scheme.py` 全文到代码节点，绑定开始节点连接参数。

输出：`result`、`message`、`schema_data`、`table_count`、`schema_text`

---

### 第 3 步：代码节点②「规则审核」

复制 `dify_audit_db_scheme.py` 全文到代码节点（约 500 行，**无需**再内嵌基准 JSON）。

| 代码入参 | 绑定到 |
|----------|--------|
| `schema_data` | 采集表结构 / schema_data |
| `rules_yaml` | 开始 / rules_yaml（可选） |

输出：`audit_result`、`audit_score`、`violations_json`

---

### 第 4 步：LLM 生成审核报告

1. **系统提示词**：`审核报告提示词.md` 全文  
2. **用户消息**：

```text
请根据以下审核结果生成报告：

{{#规则审核.violations_json#}}
```

3. 温度 **0.2–0.4**

---

### 常见问题

| 现象 | 处理 |
|------|------|
| `error: timeout` / `signal: killed` | ① 必须传 `table_names`（勿留空全库）② 更新最新 `dify_get_db_scheme.py`（指定表不再枚举 726 张表）③ Dify 云版往往访问不了 `192.168.x.x` 内网，需自建 Dify 或 VPN ④ 代码节点超时调到 120s+ ⑤ 可设 `include_schema_text=false` 减负 |
| `No module named 'pymssql'` | 沙箱安装 `sqlalchemy`、`pymssql` |
| 全库超时 | 用 `table_names` 或 `max_tables` 分批审 |
| 密码含 `@` | 代码已 URL 编码，传原始密码即可 |

---

## Dify 工作流（简图）

```
[代码] dify_get_db_scheme → schema_data
        ↓
[代码] dify_audit_db_scheme → audit_result, audit_score, violations_json
        ↓
[LLM] 审核报告提示词.md → Markdown 报告
```

## 更新规则

直接编辑 `mes_db_schema_audit_rules.yaml`，保存后重新复制到 Dify 或更新 `rules_yaml` 即可。
