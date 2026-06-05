# 维表映射配置维护说明

本目录用于配置 ERP 自然语言查数时的**外键 → 维表 JOIN → 中文列名**规则，供 Dify 工作流注入【维表映射规则】，避免列表里只显示 ID、账号。

---

## 日常只需关心 2 个文件

| 文件 | 是否手改 | 作用 |
|------|----------|------|
| `../中络项目ERP 系统数据库表结构V1.0.md` | **要** | 表结构、字段中文名、**关联关系**（权威来源） |
| `erp_dimension_joins.map` | **要** | 维表 JOIN / SELECT 中文别名（表格式，推荐维护入口） |
| `erp_dimension_joins.json` | 不要手改 | 由 `build_dify_bundle.py` 从 `.map` 解析生成 |
| `dify_erp_dimension_node.py` | 不要手改 | 维表规则，复制到 Dify **SQL 生成前** |
| **`dify_erp_sql_fix_node.py`** | 不要手改 | **SQL 修复，复制到 LLM 与 text2data 之间（必加）** |

其余为工具脚本，一般不用改：

| 文件 | 作用 |
|------|------|
| `parse_dimension_map.py` | `.map` → JSON 解析器 |
| `erp_dimension_rules.py` | 根据配置生成 Markdown 规则文本 |
| `build_dify_bundle.py` | 同步 JSON + 打包 Dify 单文件节点 |
| `generate_dimension_map_from_schema.py` | 从表结构文档**批量重生成**整个 `.map` |

---

## 加一张新表

### 第 1 步：更新表结构文档

在 `中络项目ERP 系统数据库表结构V1.0.md` 中补充新表小节，**关联关系**写全，例如：

```markdown
#### 200 新业务表 ( T_XXX_New )

- **业务含义**：……
- **所属数据库**：思方云2 ERP

| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
- **关联关系**：
  - T_XXX_New.creatorId = T_User.recId
  - T_XXX_New.plantsId = T_Plants.recId

---
```

说明：创建人 `creatorId`、修改人 `modifiedBy` 等字段，脚本会按关联或字段名自动补 `T_User` 映射。

### 第 2 步：更新映射配置（二选一）

#### 方式 A — 只加一张表（推荐日常）

在 `erp_dimension_joins.map` 末尾**复制**已有类似表（如 `FGI_ReceiptItem`），改表名、别名、ON 条件：

```text
[表 T_XXX_New]
标签=新业务表
关键词=新业务, XXX
别名=x

[映射 creator]
字段=creatorId
关联=u | T_User | u.recId = x.creatorId
列=u.employeeName | 建单人
列=u.loginName | 登录账号

[映射 plants]
字段=plantsId
关联=pl | T_Plants | pl.recId = x.plantsId
列=pl.name | 工厂名称
```

`关键词=` 用于用户问题里出现这些词时，自动选中该事实表。

#### 方式 B — 从文档批量生成（表多或大改文档时）

```bash
cd 读取ERP配置维表
python3 generate_dimension_map_from_schema.py
```

**注意**：会**覆盖**整个 `erp_dimension_joins.map`，手改内容请先 git 提交或备份。

### 第 3 步：同步到 Dify

```bash
cd 读取ERP配置维表
python3 build_dify_bundle.py
```

将生成的 `dify_erp_dimension_node.py` **全文复制**到 Dify「代码」节点（入参：`user_question`；出参：`query_rules` 接到【维表映射规则】）。

---

## `.map` 写法速查

文件头部有完整注释，核心格式如下：

```text
[全局]
默认别名=l
禁止=……

[表 表名]
标签=中文表名
关键词=词1, 词2
别名=SQL别名

[映射 英文id]
字段=事实表外键列
类型=账号          # 仅人员账号字段
可选=是            # 非必出映射
说明=备注
关联=别名 | 维表名 | ON条件 [| 依赖=上一别名]
列=SQL表达式 | 中文列名
禁止=错误写法示例
```

---

## 常见字段 → 抄哪段映射

| 事实表字段 | 映射写法 |
|-----------|----------|
| `creatorId` | `[映射 creator]` → `T_User`（`u.recId = 事实表.creatorId`） |
| `plantsId` | `[映射 plants]` → `T_Plants` |
| `companyId` | `[映射 company]` → `T_Company` |
| `sourceId` | 供应商/客户 → `M_Suppliers` 或 `S_Customer`（见文档关联） |
| `fgiReceiptId` | 主表 → `FGI_Receipt` |

制成品接收相关表见 `.map` 中 `FGI_Receipt` / `FGI_ReceiptItem` 示例。

---

## 维护流程一览

```text
新表 / 新关联上线
  │
  ├─ 写入 中络项目ERP 系统数据库表结构V1.0.md
  │
  ├─ 只加 1 张表 ──► 手改 erp_dimension_joins.map
  │
  └─ 表很多 / 文档大改 ──► generate_dimension_map_from_schema.py
  │
  └─► python3 build_dify_bundle.py ──► 复制 dify_erp_dimension_node.py 到 Dify
```

---

## 本地验证（可选）

```bash
# 查看某张表生成的规则文本
python3 erp_dimension_rules.py FGI_ReceiptItem

# 按用户问题推断事实表
python3 erp_dimension_rules.py --question "查制成品接收明细"
```

---

## 相关文档

- SQL 生成总规则：`../中络项目ERP 最新生成SQL提示词.md`
- 表结构全文：`../中络项目ERP 系统数据库表结构V1.0.md`
- 示例规则输出：`规则.txt`（仅供参考，以 `.map` / 代码节点为准）
