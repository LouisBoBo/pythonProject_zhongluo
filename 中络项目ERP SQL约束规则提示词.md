## 约束

**【硬约束·245·P_MO.status 与 P_WO.status 不可混用】**  
- **`P_MO.status`** 为 **string**（如 `Active`、`Order`、`WOWX` 等），列名 **`[单据状态]`**；**禁止** `CASE pmo.status WHEN 1 THEN N'外协' …` 数字分支（遇 `'Order'` 等字符串必 **error 245**）。  
- **`P_WO.status`** 为 **int?**（1 外协、2 未发放…），列名 **`[工单状态]`**；**禁止**把 `P_MO` 的 string CASE 套到 `P_WO`。  
- **`P_MO.synchro` / `P_MO.dev`** 为 **string** 存 `'0'`/`'1'` 等，译码须 string CASE 或 `CAST` 后再比较，**禁止**裸 `WHEN 0`/`WHEN 1`。

**【硬约束·102·中文列别名】**  
凡 `AS` 后中文别名含 **`/`**、**`(`** **`)`**、**`（`** **`）`**、空格、**`-`**：**必须** `AS [全文]`。  
**反例**：`AS 审核/驳回人`、`AS 参数值（板厚）`。  
**正例**：`AS [审核/驳回人]`、`AS [参数值（板厚）]`。

**【硬约束·WITH (NOLOCK) 同行】**  
每张表须 **`dbo.表名 别名 WITH (NOLOCK)` 同一行**；**禁止** `FROM dbo.P_MO pmo` 换行再写 `WITH (NOLOCK)`。定稿前全文搜索 `WITH`，若前一字符为换行则重写。

---

## 核心原则（优先级最高）

1. **列名白名单 = 本次【参考表结构】对应表小节中明确出现的字段名**，须逐字复制（含大小写）。  
2. **表名白名单 = 本次【参考表结构】中出现的 ERP 表名**（`P_`/`M_`/`S_`/`FGI_`/`T_`/`E_` 等）；**禁止** MES 的 `TBL_*` 表。  
3. **主键/外键**：ERP 主键一般为 **`recId`**；外键关联写 `xxx.recId = yyy.xxxId`，**禁止** MES 风格 `CID`/`CXXX_ID`。  
4. **人员维表**：**`T_User`**（`ON tu.recId = 主表.creatorId`）；**禁止** `TBL_SYS_USER`。  
5. **`modifiedBy` 为字符串用户名**的表：**禁止** `JOIN T_User ON recId = 事实表.modifiedBy`；直接 **`事实表.modifiedBy AS [修改人]`**。  
6. 用户要的列在片段中不存在：**禁止编造**；说明无法查询或改用片段已有列。

---

## 行数与 TOP

- 明细/列表查询默认 **`SELECT TOP (1000)`**；用户指定 n 时取 `min(n, 1000)`。  
- 纯 `COUNT(*)` / 无 `GROUP BY` 聚合：**禁止** `ORDER BY`（**8127**）。  
- 主表 + 明细 JOIN：**必须**保留 `TOP (1000)`；**ORDER BY** 主表时间 **DESC** + **`recId DESC`** + 明细 **`recId ASC`**。

---

## 绝对禁止

1. 编造未在【参考表结构】中出现的表名、字段名。  
2. **禁止**在 ERP SQL 中使用 **MES 表/字段**（`TBL_*`、`CID`、`CWC_ID`、`CCUSTOMER_CODE` 等）。  
3. **`P_WO` 上禁止**无文档依据写 **`pwo.partnum`/`pwo.partNum`**（**207**）；制造部件编码经 **`P_MORoute` → `E_JobMfgParts.partNum`**。  
4. **`P_WO` 禁止**写 **`moroute`** 列；工艺路线用 **`P_MORoute`**。  
5. 枚举/状态列：**禁止**裸输出 `pmo.status`、`wo.status`；须按【维表映射规则】CASE 译码。  
6. **`ORDER BY` 末尾禁止追加 `TOP`**（**156**）；`TOP` 只能紧接第一个 `SELECT`。  
7. 人员外键 **禁止只输出 ID**；须 JOIN **`T_User`** 输出姓名/账号（以维表规则为准）。  
8. **`JOIN` 必须带完整 `ON`**；禁止半截 `JOIN dbo.某表` 无 `ON`（**102**）。

---

## 定稿自检（输出 SQL 前必做）

- 每个 `别名.列名` 在【参考表结构】该表小节中逐字存在。  
- `P_MO.status` / `P_WO.status` 是否用错 CASE 类型。  
- 中文别名是否均已 `[ ]` 包裹（含 `/`、括号）。  
- 每张表 `WITH (NOLOCK)` 是否与表别名同行。  
- 明细列表是否有 `TOP (1000)` 与合理 `ORDER BY DESC`。  
- 是否误用 `TBL_*` 或 MES 字段名。

---

## 通用 boilerplate（learned 合并时保留）

【硬约束】所有字段必须来自参考表结构，禁止臆造字段。  
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。  
【硬约束】禁止在 ERP SQL 中使用 MES 表名/字段（TBL_*、CID、CWC_ID 等）。
