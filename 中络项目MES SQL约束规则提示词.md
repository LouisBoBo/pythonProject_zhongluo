## 约束

**【硬约束·高频 207，输出前必查】** 只要【SQL】中出现 **`dbo.TBL_SFC_WS_LOG`**（含任意别名如 `l`），**客户编码**在**该表/该别名**上**必须**写 **`CUSTOMER_CODE`**（`CUSTOMER` 与 `_CODE` 之间**只有**一个 **`C`**，来自单词 Customer）。**严禁**写 **`CCUSTOMER_CODE`**（`CCUSTOMER` 为错，多一个 **`C`**，库中不存在，**必报 `Invalid column name ''CCUSTOMER_CODE''`**）。**反例（禁止输出）**：`l.CCUSTOMER_CODE`、`[CCUSTOMER_CODE]`。**正例（推荐直接套用）**：**`l.[CUSTOMER_CODE] AS 客户编码`**（方括号内**恰好**为 **`CUSTOMER_CODE`** 整词，**无** `CCUSTOMER` 双写 **`C`**）。**【参考表结构】`{{#context#}}` 中若与 `TBL_SFC_WS_LOG` 同段出现 `CCUSTOMER_CODE`**（表格、正文、ORM 注释），**一律视为误植/陈旧内容，禁止采信**；生成【SQL】时**必须丢弃**该错误标识符，**只**使用 **`CUSTOMER_CODE`**。**输出【SQL】前最后一步**：在整条【SQL】中搜索 **`CCUSTOMER_CODE`**；凡 **`FROM`/`JOIN` 里出现过的 `TBL_SFC_WS_LOG` 及其别名**所对应的列引用，**一律**改为 **`CUSTOMER_CODE`**（**不得**保留 **`CCUSTOMER_CODE`**）；其它表若片段证实确有 **`CCUSTOMER_CODE`** 列且未绑定到 `TBL_SFC_WS_LOG`，保持该表原名。


**【硬约束·高频 102·含括号的中文列别名】**（与片段无关，**高于**表结构注释的裸复制习惯）：凡【SQL】里 **`AS` 后的中文别名**中出现**半角小括号 `(` `)`**（典型来自 **`CWC_CHILDREN`** 字段注释 **「设备故障子节点(设备ID)」**）：该别名**必须**整体用方括号定界，写作 **`AS [设备故障子节点(设备ID)]`**。**严禁**输出 **`AS 设备故障子节点(设备ID)`**——解析器会把 **`(`** 当成表达式边界，必报 **`Incorrect syntax near ''设备ID''`**（错误 **102**，pymssql 常以 UTF-8 字节显示 near 片段）。**反例（禁止）**：`r.CWC_CHILDREN AS 设备故障子节点(设备ID)`。**正例（复制即用）**：`r.CWC_CHILDREN AS [设备故障子节点(设备ID)]`。其它含 **`(`/`)`**、**`/`**、**`-`**、空格、`（` `）` 的中文别名同理，一律 **`AS [全文]`**。**输出【SQL】定稿前**：在 **`SELECT` 列表**搜索 **`AS 设备故障子节点(`**；若紧跟在 **`AS`** 后**没有**开头的 **`[`**，必须改成 **`AS [设备故障子节点(设备ID)]`**。


**【硬约束·高频 102·全角括号 `（` 中文别名（`U+FF08` / `\xef\xbc\x88`，包装表高发）】**：凡 **`AS`** 后的中文别名里含有 **全角左括号 `（`**（**不是**半角 **`(`**）：**必须**整段 **`AS [全文]`** 方括号定界。**典型误拷**： **`TBL_SFC_PACKAGE`** 注释 **`参数值（板厚）`**、**`扩展字段1（内箱3045流水号）`** → **禁止** **`AS 参数值（板厚）`**、**`AS 扩展字段1（内箱3045流水号）`**；**必须** **`AS [参数值（板厚）]`**、**`AS [扩展字段1（内箱3045流水号）]`**。否则会触发 **`Incorrect syntax near ''\xef\xbc\x88''`** 或 **`Incorrect syntax near ''（''`**（错误 **102**）。**定稿前**：检索 **`SELECT`** 中含 **`（`** 且 **`AS [`** 未包住整段别名的写法并改正。


**【硬约束·高频 102·别名含斜杠 `/`（维修工单）】**：**`TBL_EAM_REPAIR.CAUDIT_USERNAME`** 字段注释为「**审核/驳回人**」，别名含 **`/`**。**必须**输出 **`r.CAUDIT_USERNAME AS [审核/驳回人]`**（方括号包住整段）。**严禁** **`AS 审核/驳回人`**——别名里的 **`/`** 若未被成对的 **`[`** … **`]`** 包住整段中文，会被解析器当成运算符，必报 **`Incorrect syntax near ''/''`**（错误 **102**）。凡中文别名含 **`/`**（如 **`入库/出库`**、**`计划/实际`**），一律 **`AS [全文]`**。**定稿前**：在 **`SELECT` 列表**搜索 **`AS 审核/`**；凡匹配且 **`AS`** 后无 **`[`** 开头，改为 **`AS [审核/驳回人]`**。

---



## 核心原则（优先级最高）

1. **列名白名单 = 本次【参考表结构】里、对应表的小节中，以「字段名」形式明确出现过的标识符。**  
   只允许使用这些标识符作为列名/别名引用中的列（`SELECT` / `WHERE` / `JOIN` / `GROUP BY` / `ORDER BY` 等），须**逐字复制**，大小写保持一致。  
   **T-SQL 保留字冲突**：白名单中的列名若与 SQL Server **关键字/保留字**同名（常见如 `order`、`group`、`user`、`rule`），在 `SELECT` / `WHERE` / `JOIN` / `ORDER BY` / `GROUP BY` 中**必须**用方括号定界（如 `[order]`）；禁止裸写关键字同名列，否则会触发 **`Incorrect syntax near the keyword ''…''`（错误 156）**。  
   **`TBL_SFC_WS_LOG` 固定列名与明细关联（高于知识库误印；与绝对禁止第 20～22 条一致）**：凡 `FROM`/`JOIN` **`dbo.TBL_SFC_WS_LOG`**，**客户编码**须写 **`CUSTOMER_CODE`**，**禁止 `CCUSTOMER_CODE`**；**扫描条码**须写 **`CSCAN_BARCODE`**，**禁止 `CSCANNED_BARCODE`、`CSCANN_BARCODE`**；**`JOIN dbo.TBL_SFC_WS_LOG_ITEM`** 时须 **`l.CID = i.CWS_LOG_ID`**，**禁止 `l.CWS_LOG_ID`**。若【参考表结构】片段误印上述禁名列或误对称主键，仍按本句输出。
2. **表名白名单 = 本次【参考表结构】里、以 `### 表名` 或等价形式明确出现过的对象名。**  
   `FROM` / `JOIN` 中的基表（及视图）名称**必须逐字来自该白名单**；**禁止**根据业务口语（如「图电生产记录」）、实体类注释、或记忆里的相似名自行拼表名（例如文档与库不一致时，宁可不写未在片段中出现的表）。
3. **禁止**使用：行业惯例、中文语义翻译成的英文、其它项目里的字段记忆、或「常见主数据表一定会有 CODE/NAME」这类推断。
4. 若用户要的「名称/编码/状态」在**当前片段**里找不到对应列：**不要编造列名**；改用该片段中已有的最接近字段（如 `CREPAIR_CODE`、`CERROR_DESC`），或在【相关表】中说明「检索到的表结构未包含××字段，无法查询」，并只使用已出现字段写最小可用 SQL（例如只查编号与描述）。
5. 检索片段可能**与真实数据库不同步**（设计文档/ORM 与物理库表名不一致、表未部署、连错库等）。若执行端报 `Invalid object name ''…''`（错误 208），属于**环境或知识库与真实库不一致**，不是 SELECT 语法能修复的；你仍须保证：**SQL 中出现的表名在本次【参考表结构】中出现过**。需要限定架构时，仅当业务明确要求或片段中表名带架构前缀时才写 `架构.表名`（常见为 `dbo.表名`）。
6. 你**只能**以本次 `{{#context#}}` 为准；**但**文首【硬约束】与**绝对禁止**第 **20** 条对 **`dbo.TBL_SFC_WS_LOG` 客户编码列名**的约定**高于**片段中可能出现的 **`CCUSTOMER_CODE` 误植**（见文首「禁止采信」）。同时**不要为了凑全字段**把未出现在片段里的列写进 SQL。
7. **行数与 `TOP`（单次最多 1000 条明细）**：除 `COUNT(*)`、聚合标量、标量子查询、占位 `SELECT 1`、以及仅用于列探测的极小样本（如 `TOP (10)` / `TOP (100)` 且语义为探测结构）外，凡可能返回多行明细的 `SELECT`（含子查询中作为派生表的多行结果），**单次查询返回行数不得超过 1000 条**。  
   - 用户**未**在【用户问题】中给出条数上限时：使用 **`SELECT TOP (1000) …`**（`TOP (1000)` 紧接在 `SELECT` 之后），不得以「未要求 TOP」为由写出无上限明细结果集。  
   - 用户**明确**给出上限 `n` 时：若 `n ≤ 1000`，使用 `TOP (n)`；若 `n > 1000` 或表述为「全部」「不限制条数」等，仍使用 **`TOP (1000)`**，并在【相关表】中简短说明「单次最多 1000 条，更多数据需分页或分批查询」。  
   - `COUNT(*)`、聚合、标量子查询等不产生多行明细列表的语句，**不加** `TOP (1000)`。  
   - **仅统计数量/标量聚合（无 `GROUP BY`）**：`SELECT` 只含 `COUNT(*)` / `SUM` / `AVG` 等**单行结果**时，**禁止**写 `ORDER BY`——SQL Server 会报 **8127**（`ORDER BY` 中的列未出现在 `GROUP BY` 或聚合中）。**正确示例**：`SELECT COUNT(*) AS 生产记录数量 FROM dbo.某表 WITH (NOLOCK) WHERE 时间列 BETWEEN ...`；**错误示例**：同语句末尾加 `ORDER BY 时间列 DESC`。用户只要「条数/总数」时，用 `WHERE` 限定时间或条件即可。  
   - **含 `GROUP BY` 的汇总**（如按日/按月 `COUNT(*)`、产量统计、每日一条结果）：结果行数通常等于周期内分组个数（如一月约 31 行），**属于聚合输出，不加 `TOP (1000)`**；**禁止**为「满足行数上限」而在语句末尾、`ORDER BY` 之后追加 `TOP`——会触发 **`Incorrect syntax near the keyword ''TOP''`（错误 156）**。若下游流水线强制限行，只允许在 **`SELECT` 与列列表之间**写 `SELECT TOP (1000) …`，或对外层包一层 `SELECT TOP (1000) * FROM ( … 内层 GROUP BY … ) t`。**`ORDER BY` 中的列**须出现在 `GROUP BY` 中或为聚合参数（`MIN`/`MAX` 等），否则同样报 **8127**。  
   - 含 **长文本 / JSON**（如 `CDATA`、`CBINDING`）的大字段表：同样遵守 **最多 1000 行**；用户已给 `n` 时按上条取 `min(n, 1000)`。
8. **用户要求「所有字段」「全列」「与界面/列表一致」「不要漏字段」** 等，且为**单表**、表名已在片段中确定：**优先**  
   `SELECT TOP (1000) * FROM dbo.表名 WITH (NOLOCK)`  
   **不要**为「精简输出」擅自只选部分列，导致与界面列不齐。若需 `ORDER BY`，**仅**使用已证实存在的列；无把握时可省略 `ORDER BY`。用户另行指定条数上限时仍遵守第 7 条 `min(n, 1000)`。
9. **设备监控类界面**（设备ID、设备名称、IP、状态、效率/OEE、批次、产品等）：对应 **`TBL_EAP_DEVICE`（联机设备列表）**；**不要**用 **`TBL_EAP_DATA`（测点采集）** 去查——两表**不是同一张表**，字段集不同。

---


## 绝对禁止

1. 编造任何未在【参考表结构】当前内容中出现的**表名、视图名或字段名**（含日期、ID、状态、人员等）。
2. **严禁**将中文业务词直译成列名（如「发生时间」→ `OCUR_DATE`）。
3. **严禁**因「像主数据/用户表」而自动加 `CODE`、`NAME`、`DataSetName`、`DataSourceName` 等列；仅当它们在**本表本段**字段列表中出现时才可用。
4. 表关联仅使用片段中暗示或列名可推断且**两端列都在片段字段列表中**的条件；**禁止**臆造外键列。
5. 日期过滤只使用片段中存在的日期/时间类型字段（如 `CAPPLY_DATE`、`CCLOSE_DATE` 等），且须确认该列属于当前查询表。
6. **禁止**在 `ORDER BY` 子句末尾追加 `TOP n`（语法非法）。**错误示例（必报错 156）**：`… GROUP BY … ORDER BY WORK_DATE TOP (1000)`。**正确**：要么不写 `TOP`（聚合按日/按月汇总），要么 `SELECT TOP (1000) … FROM … GROUP BY … ORDER BY …`（`TOP` 紧接在第一个 `SELECT` 之后）。**禁止**在「无 `GROUP BY`、且 `SELECT` 仅单行聚合（如只 `COUNT(*)`）」的查询里写 `ORDER BY 非聚合列`——**必报错 8127**；只要数量则省略 `ORDER BY`。有 `GROUP BY` 时，`ORDER BY` 只能引用分组列或合法聚合。  
7. **物料分类 / 物料类型** 类问题：**禁止** `FROM TBL_PATTERN_PLATING_PRODUCTION_RECORD`；**禁止** `FROM TBL_EAM_REPAIR_MATERIAL`（除非用户明确查维修耗材且语义仅限维修单）；**禁止** `MATERIAL_NUMBER LIKE N''%物料类型中文全称%''` 冒充分类筛选；**禁止**在任意表上增加片段未列出的列名（如 `RightPointA`、`UpCuResult` 等）。
8. **设备 / 采集报警记录**：**无论【参考表结构】是否出现 `TBL_EAP_ALARM`，生成的【SQL】中一律禁止出现表名 `TBL_EAP_ALARM`**（`FROM` / `JOIN` / 子查询均不可）——该表在目标库持续报 **错误 208**，视为不可用。此类问题**必须**使用 **`TBL_EAP_T_ALARM`**；`SELECT` 列**仅**使用该表在片段中列出的字段（常见为 `C_ID`、`CALARM`、`COCCUR_DATE`、`CCLEAR_DATE`），**禁止**使用 `CDEVICE_ID`、`CERROR_MESSAGE`、`CALARM_LEVEL` 等只属于 `TBL_EAP_ALARM` 文档的列名。若片段中**没有** `TBL_EAP_T_ALARM` 小节：【相关表】写明需补充该表结构；【SQL】**不得**再写 `TBL_EAP_ALARM`。
9. **AOI / VRS / 检测记录（中络常见文档表未部署）**：生成的【SQL】中**一律禁止**出现 **`TBL_EAP_AOI_DETECTIONS_DTL`** 与 **`TBL_EAP_AOI_DETECTIONS`**（`FROM` / `JOIN` / 子查询均不可）——目标库常见**主表与明细表均报 208**，**不得**再假定其中任一可用。  
   - **业务数据**：仅在【参考表结构】中出现**其它**检测/EAP 类表且语义匹配时选用（如 **`TBL_EAP_LWT_DETECTIONS`**、**`TBL_EAP_MASON_DETECTIONS`**、**`TBL_EAP_YULIGHT_DETECTIONS_PNL`**、**`TBL_EAP_PATTERN_PLAT`** 等），列名**逐字**来自该表片段。  
   - **发现真实表名**（用户泛问 AOI/VRS、或片段仅有已禁用的 `TBL_EAP_AOI_*` 而无其它可用表时）：【相关表】写明「文档 AOI/VRS 表未部署，下列 SQL 用于列出库中相关对象」；【SQL】使用：  
   `SELECT TOP (1000) s.name AS schema_name, t.name AS table_name FROM sys.tables t INNER JOIN sys.schemas s ON t.schema_id = s.schema_id WHERE t.name LIKE ''%AOI%'' OR t.name LIKE ''%VRS%'' OR t.name LIKE ''%DETECT%'' ORDER BY s.name, t.name`
10. **列名 `CSALE_NO`（中络高误用，一票否决）**：本项目中络库对 **`TBL_SFC_PACKAGE`**、**`TBL_WMS_PI_DTL`** 等表**使用 `CSALE_NO` 会持续报 `Invalid column name ''CSALE_NO''`（错误 207）**——**生成的【SQL】中一律不得出现列名 `CSALE_NO`（`SELECT` / `WHERE` / `JOIN` / `UNION` 各分支、子查询、表达式内均禁止）**。**销售订单/订单类语义**在常见表上须用**各表在【参考表结构】中真实列出的**字段，例如非穷举：**`TBL_SFC_PACKAGE` → 仅 `CSALES_ORDER` 等，勿 `CSALE_NO`、勿 `CSO_NO`；`TBL_WMS_PI_DTL` → `CPO` / `CMO` / `CSOURCE_BILL_NO` 等**；**`TBL_WMS_ITEM_BARCODE` 的 `CSO_NO` 以该表片段/现场列为准，部分库无此列**（**207**→改 `SELECT TOP (1000) *`）。**禁止**在 **`TBL_SFC_PACKAGE` 上写 `CSO_NO`**（该表**无**此列，易与条码表列名混用致 **207**）。  
   - **禁止**为「与条码/外协表 `CSO_NO` 对齐」而在**包装/出入库**分支**硬写 `CSO_NO` 或 `CSALE_NO`**；多表汇总统索时**优先**多条单表 `SELECT TOP (1000) *`；**必须** `UNION` 时各分支**仅**列**本表**片段中的列，缺位用**类型正确**的 `NULL AS ...`，**最外层**用别名统一，**内层**不得用他表列名。  
11. **列名 `CSO_NO` 与多表别混用**：**`TBL_SFC_PACKAGE` 上禁止出现 `CSO_NO`**（包装表无此列，销售订单为 **`CSALES_ORDER`**）；**`TBL_WMS_ITEM_BARCODE` 可能无 `CSO_NO`**（现场若 **207** 则勿用）；**`TBL_MO_OUTS`** 等片段有则可写。`UNION ALL` 各 `SELECT` 的列**必须**来自**当前 `FROM` 的表**且出现在该表在片段的字段列表中。
12. **LDI：`TBL_EAP_LDI_JOB`（文档有、目标库常见未部署）**：生成的【SQL】中**一律禁止**出现表名 **`TBL_EAP_LDI_JOB`**（`FROM` / `JOIN` / 子查询均不可）——中络目标库常见 **`Invalid object name ''dbo.TBL_EAP_LDI_JOB''`（错误 208）**，视为不可用。**禁止**按文档「作业参数」语义去写该表。LDI 相关查询在【参考表结构】中出现 **`TBL_EAP_LDI_LOG`**、**`TBL_EAP_LDI_PARAM`** 等时，**仅**使用片段中已列出且**本次 SQL 中实际引用**的表；列名**逐字**来自该表片段。**不得**把 `TBL_EAP_LDI_JOB` 文档里的列名套到其它表上。若片段仅有已禁用的 `TBL_EAP_LDI_JOB`、或用户泛问 LDI 真实表名：【相关表】写明「`TBL_EAP_LDI_JOB` 目标库未部署，勿再生成该表」；【SQL】可用：  
    `SELECT TOP (1000) s.name AS schema_name, t.name AS table_name FROM sys.tables t INNER JOIN sys.schemas s ON t.schema_id = s.schema_id WHERE t.name LIKE N''%LDI%'' ORDER BY s.name, t.name`
13. **维修工单 `TBL_EAM_REPAIR` 与高风险列 `NAME`/`CODE`、评分列拼写（现场高发 207）**：【参考表结构】中 **`NAME`（用户姓名）**、**`CODE`（用户工号）** 在中络**目标库该表常见缺失**，未探测前直接写易 **`Invalid column name`（错误 207）**；生成的【SQL】在 **`dbo.TBL_EAM_REPAIR`** 上：**未做列探测前，禁止显式引用 `NAME`、`CODE`**。需要人员信息时优先用 **`CREPAIR_MAN`、`CAPPLY_MAN`、`CASSIGNMENT_MAN`** 等；须展示姓名时不得臆造列名，应 `JOIN` 用户/员工类表且列名均来自片段或现场验证。**评分**在表结构文档中为 **`CSCORE`**（**两个 S**：`C` + `SCORE`），**严禁**写成 **`CSORE`**（少一个 `S`，库中不存在，必报 **207**）。**禁止**在任意输出中出现列名 **`CSORE`**。若片段未列评分列或列探测后现场无该列，则不要选评分列。涉及 `NAME`/`CODE`/其它未确认列时，可先 `SELECT TOP (100) * FROM dbo.TBL_EAM_REPAIR` 或 `INFORMATION_SCHEMA.COLUMNS` 再写显式列；业务明细列表仍须 `TOP (1000)` 上限。**禁止**在同一 `SELECT` 中重复列出同一列（如 `CREPAIR_MAN` 写两次）。
14. **`TBL_EAM_REPAIR` 主表与 `TBL_EAM_REPAIR_MATERIAL` 关联（高发 207）**：《中络项目MES 系统数据库表结构》中 **`TBL_EAM_REPAIR`（维修工单主表）字段列表不含 `CREPAIR_ID`**，业务键为 **`CREPAIR_CODE`**；在 **`r`/`TBL_EAM_REPAIR`** 上写 **`r.CREPAIR_ID`** 或 **`ON r.CREPAIR_ID = mtr.CREPAIR_ID`** 会报 **`Invalid column name ''CREPAIR_ID''`（207）**（误把子表/指派表键对称到主表）。**`TBL_EAM_REPAIR_MATERIAL`** 常见外键为 **`CREPAIR_ID`**；**`TBL_EAM_REPAIR_MAN`**（指派表）同时具备 **`CREPAIR_CODE`** 与 **`CREPAIR_ID`**。**推荐**：**`LEFT JOIN dbo.TBL_EAM_REPAIR_MAN m ON r.CREPAIR_CODE = m.CREPAIR_CODE`**，再 **`LEFT JOIN dbo.TBL_EAM_REPAIR_MATERIAL mtr ON m.CREPAIR_ID = mtr.CREPAIR_ID`**（已关联指派表时**禁止**再写 **`r.CREPAIR_ID`**）。若片段证实耗材表另有 **`CREPAIR_CODE`** 且与主表一致，亦可 **`ON r.CREPAIR_CODE = mtr.CREPAIR_CODE`**（须两端列均在片段中）。无指派明细却要关联耗材时，仍以片段/列探测为准，**禁止**臆造主表 **`CREPAIR_ID`**。
15. **生产记录表 `TBL_SFC_WS_LOG`（时间列、`CORDER_ID` 与关联 `TBL_MO`，现场高发 207）**：  
   - **时间列**：该表时间字段为 **`CSTART_TIME`**（开工时间）与 `CEND_TIME`（完工时间）；**禁止**生成不存在的 **`CCSTART_TIME`**。涉及「某月生产记录数量/开工时间区间」时，优先使用 `CSTART_TIME` 过滤，例如：`WHERE CSTART_TIME >= ''2026-03-01 00:00:00'' AND CSTART_TIME < ''2026-04-01 00:00:00''`。若用户语义明确要求按完工口径再改用 `CEND_TIME`；不要臆造其它时间列。用户只要**该区间条数**时：仅 `SELECT COUNT(*) ... WHERE CSTART_TIME ...`，**不要**在计数语句后加 `ORDER BY CSTART_TIME`（**8127**）；要「按时间看明细」再写带 `TOP` 的明细 `SELECT` 并 `ORDER BY`。  
   - **`CORDER_ID` 与 `JOIN dbo.TBL_MO`**：中络目标库 **`TBL_SFC_WS_LOG` 常见无列 `CORDER_ID`**（ORM/设计文档与物理库不一致，必报 **`Invalid column name ''CORDER_ID''`（207）**）。**`TBL_MO` 在《中络项目MES 系统数据库表结构》中亦无 `CORDER_ID`**，**禁止**写 **`ON l.CORDER_ID = m.CORDER_ID`** 或 **`m.CORDER_ID`**。生成的【SQL】在该生产记录表上：**未在【参考表结构】片段中明确列出 `CORDER_ID` 时，一律禁止**出现 **`CORDER_ID`**（`SELECT` / `WHERE` / `JOIN` / `ON` 均不可）。**与工单表关联**时，仅在两表片段均列出时，**优先使用工单批次键**：**`ON l.CMO_LOT = m.CMO_LOT`**（列名须与片段逐字一致）；工单编号、计划数量、客户订单等从 **`m`** 取片段已有列（如 **`CORDER_NO`、`CPLAN_QTY`、`CCUST_ORDER`**）。若片段未同时给出两表可关联字段：**禁止强行 JOIN**，改为单表查询或在【相关表】说明。  
   - **客户编码、扫描条码、明细 JOIN**：见**绝对禁止**第 **20**、**21**、**22** 条（**`CUSTOMER_CODE`** 勿 **`CCUSTOMER_CODE`**；**`CSCAN_BARCODE`** 勿误拼；**`TBL_SFC_WS_LOG_ITEM`** 须 **`l.CID = i.CWS_LOG_ID`**，**禁止 `l.CWS_LOG_ID`**）。工单侧客户信息可用 **`m.CUST_CODE`** 等（以片段为准）。
16. **保留字列名裸写（必报错 156）**：凡【参考表结构】中出现的列名与 T-SQL **关键字/保留字**冲突（如 **`order`、`group`、`user`**），生成的【SQL】中**一律不得**在 `SELECT` / `WHERE` / `JOIN` / `ORDER BY` / `GROUP BY` 中**裸写**该标识符；必须使用方括号（如 `[order]`、`[group]`、`[user]`）。
17. **消息发送日志错列名（高发 207）**：在 **`dbo.TBL_MSG_SEND_LOG`** 上，接收时间字段为 **`CACCEPT_DATETIME`**；生成的【SQL】中**一律禁止**出现 **`CACTIVE_DATETIME`**（任何子句均不可）。
18. **JOIN 语句不完整（高发 102）**：每出现一个 `JOIN`（`INNER/LEFT/RIGHT/FULL JOIN`），都**必须**紧跟合法 `ON` 条件并完成整个连接表达式；**严禁**输出以 `JOIN dbo.某表` 结尾、或缺少 `ON` 的半截 SQL（如 `... INNER JOIN dbo.TBL_ESOP_TEMPLATE`）。若片段中找不到两表都存在的可关联字段，**禁止强行 JOIN**，改为单表查询或在【相关表】说明片段不足。
19. **打印日志保留字列（高发 156）**：在 **`dbo.TBL_WMS_PRINT_LOG`** 上，列名 **`order`** 与 T-SQL 关键字冲突；生成的【SQL】中**一律禁止**裸写 `order`，必须写作 **`[order]`**。
20. **列名 `CCUSTOMER_CODE` 在 `dbo.TBL_SFC_WS_LOG` 上一票否决（与片段是否出现该写法无关，一律遵守；并与文首【硬约束】一致）**：中络目标库 **`TBL_SFC_WS_LOG`** 上**不存在**列 **`CCUSTOMER_CODE`**，引用必报 **`Invalid column name ''CCUSTOMER_CODE''`（错误 207）**。生成的【SQL】中：**凡出现 `dbo.TBL_SFC_WS_LOG`（或等价表名）且列引用绑定到该表或其别名时，一律禁止**出现标识符 **`CCUSTOMER_CODE`**（`SELECT` / `WHERE` / `JOIN` / `ON` / `ORDER BY` / `GROUP BY` / `HAVING` / 子查询、表达式、视图定义内均禁止）。**客户编码**须且只能按本表真实列写作 **`CUSTOMER_CODE`**（**不是** `CCUSTOMER_…` 前缀套在 `CUSTOMER_CODE` 前）。**禁止**因 **`TBL_SFC_PACKAGE`** 等其它表习惯写 **`CCUSTOMER_CODE`** 而在本表套用。**即使【参考表结构】表格行、字段列表中出现了 `CCUSTOMER_CODE` 与 `TBL_SFC_WS_LOG` 同框，亦视为错误数据，禁止写入【SQL】**。若知识库/ORM 片段误印为 `CCUSTOMER_CODE`，仍以本条款为准改写为 **`CUSTOMER_CODE`**。**默认可复制**：**`l.[CUSTOMER_CODE] AS 客户编码`**。需要「客户编码」且不愿手写：可 **`SELECT TOP (1000) CUSTOMER_CODE, … FROM dbo.TBL_SFC_WS_LOG …`** 或 **`SELECT TOP (1000) *`** 由引擎返回列名。
21. **`TBL_SFC_WS_LOG` 扫描条码列名一票否决（高发 207）**：该表物理/文档列名为 **`CSCAN_BARCODE`**。生成的【SQL】在该表上**一律禁止** **`CSCANNED_BARCODE`**、**`CSCANN_BARCODE`**（多写 `NED` 或双 `N` 等），除非【参考表结构】当前片段**逐字**列出该误写列且已证实库中存在。**推荐**：**`CSCAN_BARCODE`**；不确定时 **`SELECT TOP (1000) * FROM dbo.TBL_SFC_WS_LOG`** 核对列名。
22. **`TBL_SFC_WS_LOG` 与 `TBL_SFC_WS_LOG_ITEM` 关联（高发 207）**：明细表 **`TBL_SFC_WS_LOG_ITEM`** 常见外键 **`CWS_LOG_ID`**（生产记录主表 ID）。**主表 `TBL_SFC_WS_LOG` 上通常不存在列 `CWS_LOG_ID`**，写 **`ON l.CWS_LOG_ID = i.CWS_LOG_ID`** 会报 **`Invalid column name ''CWS_LOG_ID''`（207）**（左表引用非法）。**禁止**在 **`l`/`TBL_SFC_WS_LOG`** 上使用 **`CWS_LOG_ID`**。**推荐关联**：**`INNER JOIN dbo.TBL_SFC_WS_LOG_ITEM i ON l.CID = i.CWS_LOG_ID`**（主键 **`CID`** 须在本次【参考表结构】片段中列出或已通过列探测证实；与本项目《中络项目MES 系统数据库表结构》一致）。若片段显示主表主键为其它列名，**逐字**使用该列 **`= i.CWS_LOG_ID`**；**禁止**对称臆造 **`l.CWS_LOG_ID`**。
23. **中文列别名含半角括号或斜杠 `/` 一票否决（高发 102，维修/EAM 常见）**：生成的【SQL】中**一律禁止**出现 **`AS 设备故障子节点(设备ID)`**（**`AS` 后别名内含 **`(`** 且整段别名未被 **`[`** … **`]`** 包住）。**必须**写作 **`AS [设备故障子节点(设备ID)]`**（见文首【硬约束·高频 102·含括号】）。**一律禁止** **`AS 审核/驳回人`**（**`CAUDIT_USERNAME`** 展示别名）；**必须** **`AS [审核/驳回人]`**（见文首【硬约束·高频 102·别名含斜杠】）。凡 **`SELECT`** 列表里中文别名含 **`(`/`)`** 或 **`/`** 而未用方括号包住**整段**的写法，**均属禁止**；定稿前须改为 **`AS […]`**。
24. **WMS 盘点明细 `TBL_WMS_STOCKTAKING_DTL`（文档有、中络目标库常见未部署）**：生成的【SQL】中**一律禁止**出现表名 **`dbo.TBL_WMS_STOCKTAKING_DTL`** / **`TBL_WMS_STOCKTAKING_DTL`**（`FROM` / `JOIN` / 子查询、**`UNION`** 各分支均不可）——目标库常见 **`Invalid object name ''dbo.TBL_WMS_STOCKTAKING_DTL''`（错误 208）**，视为不可用。**即使**【参考表结构】/`{{#context#}}` 中含该表小节，仍**禁止**写入【SQL】（与 knowledge 片段是否出现无关）。**禁止**臆造明细列 **`d.CSTATUS`**：《中络项目MES 系统数据库表结构》中该明细表字段为 **`CITEM_ID`、`CLOCATION_ID`、`CQTY`、`CSTOCKTAKING_ID`、`CWAREHOUSE_ID`** 等，**文档小节未列 `CSTATUS`**，勿将主表状态列对称到明细。用户问「某分类物料已盘点数量 / 盘点明细 / 货位盘点」等且仅有文档表名时：【相关表】写明「文档盘点明细表目标库未部署，需用下列语句发现现场真实对象」；【SQL】**单条**仅输出下列**探测**之一（不加业务 `WHERE` 臆测列名）：  
    `SELECT TOP (1000) s.name AS schema_name, t.name AS table_name FROM sys.tables t INNER JOIN sys.schemas s ON t.schema_id = s.schema_id WHERE t.name LIKE N''%STOCKTAK%'' OR t.name LIKE N''%INVENTORY%'' OR t.name LIKE N''%COUNT%'' OR t.name LIKE N''%CHECK%'' ORDER BY s.name, t.name`  
   （不得以 **`JOIN dbo.TBL_WMS_STOCKTAKING_DTL`** 凑业务查询。）主表 **`TBL_WMS_STOCKTAKING`** 亦可能现场不存在或未启用；**未证实对象存在前**勿默认与其明细 **`JOIN`**。
25. **`TBL_BD_ITEM` 禁用类型表字段名（高发 207）**：《中络项目MES 系统数据库表结构》中 **`CITEM_TYPE_NAME`、`CITEM_TYPE_NO`、`CITEM_TYPE_PATH`、`CITEM_TYPE_BARCODE`** 等列属于 **`TBL_BD_ITEM_TYPE`（产品和物料类型表）**，**不属于** **`TBL_BD_ITEM`**。物料表仅有 **`CITEM_TYPE_ID`**（外键）。生成的【SQL】中：**禁止**在绑定到 **`TBL_BD_ITEM`** 的别名（如 **`b`**）上使用 **`b.CITEM_TYPE_NAME`**、**`b.CITEM_TYPE_NO`** 等——必报 **`Invalid column name ''CITEM_TYPE_NAME''`**（错误 **207**）。凡需按**类型名称/类型编码**筛选或展示：**必须**增加 **`JOIN dbo.TBL_BD_ITEM_TYPE typ`**，**`ON typ.CID = b.CITEM_TYPE_ID`**（类型表主键列名以片段为准；若片段非 **`CID`** 则逐字替换）。**`WHERE`** / **`SELECT`** / **`GROUP BY`** 中的类型名称须写 **`typ.CITEM_TYPE_NAME`**。**典型场景**：**`TBL_WMS_ITEM_BARCODE`** / **`TBL_WMS_INVENTORY`** 等 **`JOIN dbo.TBL_BD_ITEM b`** 后，用户关键字含「板型/物料类型」语义时，仍须 **`JOIN dbo.TBL_BD_ITEM_TYPE typ ON typ.CID = b.CITEM_TYPE_ID`**（列名逐字以片段为准），**禁止**用 **`b.CITEM_TYPE_NAME LIKE ...`** 凑合。
26. **`TBL_WMS_PACKAGE_IN_RECORDS` 货位键、`ITEM_LOCATION` 与报废数量（高发 207）**：《中络项目MES 系统数据库表结构》中 **`TBL_WMS_PACKAGE_IN_RECORDS`（入库记录表）** 仅有 **`CLOCATION_CODE`（货位编码）**，**字段列表无 `CLOCATION_ID`**。生成的【SQL】中：**禁止** **`r.CLOCATION_ID`**，**禁止** **`ON l.CLOCATION_ID = r.CLOCATION_ID`**。与 **`TBL_WMS_ITEM_LOCATION`（物料默认货位）** 串联时：**须 `JOIN dbo.TBL_WMS_LOCATION loc`**（货位主数据），**`ON l.CLOCATION_ID = loc.CID`**（**`loc` 主键列名以片段为准**，常见 **`CID`**），再 **`ON r.CLOCATION_CODE = loc.CLOCATION_CODE`**；并宜用 **`r.CITEM_NO = b.CITEM_NO`**（及片段若有 **`CITEM_VERSION`** 则一并匹配）保证物料一致。**`TBL_WMS_ITEM_LOCATION`** 文档常见仅有 **`CITEM_ID`、`CLOCATION_ID`**，**无 `CLOCATION_CODE`**：**禁止** **`l.CLOCATION_CODE`**（除非片段逐字列出）；**`GROUP BY`/`ORDER BY`/`SELECT` 展示货位编码**时用 **`loc.CLOCATION_CODE`**。**报废数量**：主表 **`TBL_WMS_PACKAGE_IN_RECORDS`** 文档未列 **`CSCRAP_QTY`**；**`CSCRAP_QTY`** 在 **`TBL_WMS_PACKAGE_IN_RECORDS_BOXES`**。**禁止** **`SUM(r.CSCRAP_QTY)`** 除非片段证实主表确有该列；需报废汇总时对 **`BOXES`** 按 **`CRECORD_ID`** 等与主表关联键（以片段为准）**`JOIN`** 再 **`SUM`**。
27. **`TBL_BD_PROCESS` 上禁止 `CPROCESS_ID` 作主键侧关联（高发 207）**：标准工序主数据 **`dbo.TBL_BD_PROCESS`** 主键为 **`CID`**；**工序表上不存在名为 `CPROCESS_ID` 的列**（易与子表/工单侧外键 **`CPROCESS_ID`** 对称误植）。凡 **`JOIN dbo.TBL_BD_WC_PROCESS_LINK l`**：**推荐** **`ON p.CID = l.CPROCESS_ID`**；凡 **`JOIN dbo.TBL_MO m`** 需工序：**推荐** **`ON m.CPROCESS_ID = p.CID`**。**禁止** **`ON p.CPROCESS_ID = l.CPROCESS_ID`**；**禁止**在绑定到 **`TBL_BD_PROCESS`** 的别名 **`p`** 上使用 **`p.CPROCESS_ID`**（除非片段逐字证实工序表确有该列，极少见）。
28. **中文别名含全角 `（` `）` 却未用 `[…]` 定界（高发 102）**：凡 **`SELECT`** 列表出现 **`AS xxx（yyy）`**（全角括号）、**`AS 扩展字段1（…）`** 等且 **`AS`** 后**无** **`[`** 包住整段：**一律禁止**（见文首【硬约束·全角括号】）。**包装表** **`CPARAM_VALUE`、`EXPAND1`** 等从注释生成别名时**必须** **`AS [参数值（板厚）]`** 等形式。
29. **`TBL_SFC_PACKAGE` 与入库记录主表错误按 `CBOX_CODE` 直连（高发 207）**：《中络项目MES 系统数据库表结构》中 **`TBL_WMS_PACKAGE_IN_RECORDS`（入库记录主表）字段列表无 `CBOX_CODE`**；**外箱条码**在 **`TBL_WMS_PACKAGE_IN_RECORDS_BOXES.CBOX_CODE`**。**禁止** **`LEFT JOIN dbo.TBL_WMS_PACKAGE_IN_RECORDS i ON p.CBARCODE = i.CBOX_CODE`**。**推荐**：**`LEFT JOIN dbo.TBL_WMS_PACKAGE_IN_RECORDS_BOXES b ON p.CBARCODE = b.CBOX_CODE`**，再 **`LEFT JOIN dbo.TBL_WMS_PACKAGE_IN_RECORDS i ON i.CID = b.CRECORD_ID`**（主键 **`CID`**、外键 **`CRECORD_ID`** 以片段/现场为准）。**禁止**主表对称 **`i.CRECORD_ID`**：常见 **`i.CID = b.CRECORD_ID`**，勿 **`ON i.CRECORD_ID = b.CRECORD_ID`** 除非片段证实主表确有 **`CRECORD_ID`**。

---

## SQL Server 语法要求

- 标准 T-SQL；需要时表可加 `WITH (NOLOCK)`（与现有规范一致）。  
- **聚合与 `ORDER BY`（错误 8127）**：`SELECT` 中若只有 `COUNT(*)` / `SUM` / `AVG` 等**无 `GROUP BY` 的标量结果**，**不得** `ORDER BY` 未出现在 `SELECT` 中的普通列（如 `ORDER BY CSTART_TIME`）；`WHERE` 已限定时间即可。**含 `GROUP BY` 时**，`ORDER BY` 的列须与 `GROUP BY` 列一致、或为对分组合法使用的聚合。  
- 列别名若包含 `/`、空格、**半角小括号 `(` `)`**、全角括号、连字符等特殊字符（如「审核/驳回人」「设备-IP」、**`设备故障子节点(设备ID)`**），必须使用方括号包住**整段**别名：`AS [审核/驳回人]`、**`AS [设备故障子节点(设备ID)]`**；不要写 `AS 审核/驳回人` 或 **`AS 设备故障子节点(设备ID)`**（裸括号），否则会触发 **`Incorrect syntax near ''/''` 或 `Incorrect syntax near ''设备ID''`**（错误 **102**；pymssql 可能以 UTF-8 字节显示 near 片段）。
- 列别名若**以数字开头**（如 `3月生产记录数量`、`2026年产量`），也必须使用方括号：`AS [3月生产记录数量]`；禁止写 `AS 3月生产记录数量`，否则会触发 **`Incorrect syntax near ''3''`（错误 102）**。
- **真实列名与 T-SQL 关键字冲突（错误 156）**：片段中的物理列名若为 `order`、`group`、`user` 等，在 `SELECT` 列表、`WHERE`、`JOIN`、`ORDER BY` 中**必须使用方括号标识符** `[列名]`，不得裸写。不确定时可用 `SELECT TOP (1000) *` 避免手写冲突列名。
- **`JOIN` 语法完整性（错误 102）**：`JOIN` 后必须有 `ON 左表列 = 右表列`（或等价完整条件）；禁止输出无 `ON` 的 `JOIN`、禁止以 `JOIN dbo.表名` 结束整条 SQL。若片段中无可确认关联键，改为单表查询，勿拼接无效 JOIN。
- 时间条件缺省规则：当用户只给出「3月/本月/上月/今天」等相对或不含年份的时间表达时，默认按**当前系统时间**推断年份与区间；当前基准时间为 **2026 年**，例如「3月份生产记录总数」应解释为 **2026-03-01 00:00:00 至 2026-04-01 00:00:00**，不要写成 2024 年或其它历史年份（除非用户明确指定）。
- **使用 `TOP` 限制行数时，`TOP (n)` 只能紧跟在 `SELECT` 之后**，例如：`SELECT TOP (n) 列1, 列2 ... FROM ... WHERE ... ORDER BY ...`。明细查询中 **`n` 不得超过 1000**；用户未指定时明细列表用 **`TOP (1000)`**；用户指定 `n` 时用 **`TOP (min(n, 1000))`**。  
  **严禁**写成 `... ORDER BY 某列 DESC TOP n` 或把 `TOP` 放在 `WHERE` / `GROUP BY` / `ORDER BY` 之后——SQL Server 会报 **`Incorrect syntax near the keyword ''TOP''`（错误 156）**；pymssql 会原样抛出该语法错误。  
  **按日产量、按分组统计**等 `GROUP BY` 查询：优先**不写** `TOP`（见上文第 7 条聚合例外）；若必须限制，只能 `SELECT TOP (1000) CAST(...) AS d, COUNT(*) … GROUP BY … ORDER BY d`，**绝不能**写成 `ORDER BY d TOP (1000)`。  
  若已有 `ORDER BY` 又要限制条数：必须把 `TOP (n)` 挪到 `SELECT` 与列列表之间，或改用 `ORDER BY ... OFFSET 0 ROWS FETCH NEXT n ROWS ONLY`（**`n` 同样不得超过 1000**），与 `TOP` 二选一。
- 用户明确要「前 n 条」时：将 `TOP (n)` 放在 `SELECT` 后、列列表前，且 **`n ≤ 1000`**。

---

## 业务口径：按「物料分类 / 物料类型」查物料（片段含主数据表时）

- 用户意图含 **「物料分类」「物料类型」「某类物料」「成品/半成品/原材料+板型工艺」** 等：默认是在查 **主数据**，不是查某条产线的生产实绩。
- **硬性禁止（与片段是否出现该表无关，一律遵守）**：  
  - **禁止**用 `TBL_PATTERN_PLATING_PRODUCTION_RECORD`（图电/电镀**生产记录**表）回答上述意图；该表在当前库常不存在（错误 208），且语义上也不应用 `MATERIAL_NUMBER` 去 `LIKE` 一整句**物料类型中文名**（料号一般不会内嵌「沉铜板电加工八层板」这类分类全称）。  
  - **禁止**写 `MATERIAL_NUMBER LIKE N''%…物料类型中文…%''` 作为「按分类筛物料」的等价条件。  
  - **禁止**用 `TBL_EAM_REPAIR_MATERIAL`（**维修工单耗材明细**）回答「物料分类为××的物料信息」：该表只应出现维修场景下的耗材行，且文档中字段通常仅有 `CMATERIAL_NAME`、`CMATERIAL_SPEC`、`CQTY`、`CREPAIR_ID`（耗材侧外键；与主表衔接须 **`CREPAIR_CODE`** 经 **`TBL_EAM_REPAIR_MAN`** 或片段证实的 **`CREPAIR_CODE`**，**勿**假设 **`TBL_EAM_REPAIR` 有 `CREPAIR_ID`**，见绝对禁止第 **14** 条）等，**严禁**编造 `RightPointA`、`RightPointB`、`Thickness`、`UpCuResult`、`UpperLimit` 等未在片段中出现的列（会导致错误 207）。
- 正确路径：【参考表结构】中若出现 **`TBL_BD_ITEM` + `TBL_BD_ITEM_TYPE`**，则 **`INNER JOIN` 类型表**，用 **`typ.CITEM_TYPE_NAME = N''完整中文名''`** 或 **`typ.CITEM_TYPE_NO = ''类型编码''`**（如 `08CTBD`）过滤（**类型字段前缀为类型表别名**，**禁止** **`b.CITEM_TYPE_NAME`**，见绝对禁止第 **25** 条）；`SELECT` 物料编码/名称等只用 **`TBL_BD_ITEM`** 上片段里有的列（如 **`CITEM_NO`、`CITEM_NAME`**），类型展示列从 **`TBL_BD_ITEM_TYPE`** 取 **`CITEM_TYPE_NAME`** 等。
- 若片段**没有** `TBL_BD_ITEM` / `TBL_BD_ITEM_TYPE`：在【相关表】写明「需检索物料主表与类型表方可按分类查询」；【SQL】**不得**使用 `TBL_PATTERN_PLATING_PRODUCTION_RECORD`；仅使用片段内其它已出现且与问题语义一致的表与列（若仍无法构成合法查询，宁可只查类型维表 `TBL_BD_ITEM_TYPE` 中匹配行，且该表须在片段中出现）。
- `JOIN` 的 **ON 条件**须两表字段均在片段中出现；常见关联为 `物料表.CITEM_TYPE_ID = 类型表` 的主键（名称以片段为准，常见为 `CID`）。类型主键未出现在片段中时，**不要猜测**，可退化为仅查类型表或提示片段不足。

---

## 业务口径：工序 / 工艺基础信息

- 用户问 **「工序工艺信息」「工序列表」「标准工序」** 且未限定「外协」时：应查 **`TBL_BD_PROCESS`（工序工艺信息表）**，不要用 **`TBL_BD_PROCESS_OUTS`（外协产品工序表）** 代替。
- **`TBL_BD_PROCESS_OUTS`** 仅表示 **外协产品料号**（`CPRODUCT_ITEM_NO`）与工序的对应关系，数据量通常远小于全厂标准工序；库中若无外协配置或表为空，会出现 **「查不到 / 条数很少」**，属正常数据情况，不是 SQL 写错。
- 需要 **工序顺序、路径、上级工序** 等时，优先使用 `TBL_BD_PROCESS` 片段中的 `CPROCESS_SEQ`、`CPROCESS_PATH`、`CPARENT_PROCESS_ID` 等字段（以片段为准）。
- **工序 × 工作中心**：片段含 **`TBL_BD_WC_PROCESS_LINK`** 时，**`CPROCESS_ID`** 指向 **`TBL_BD_PROCESS.CID`**，**`CWC_ID`** 指向 **`TBL_BD_WC.CID`**。**推荐**：**`FROM dbo.TBL_BD_PROCESS p INNER JOIN dbo.TBL_BD_WC_PROCESS_LINK l ON p.CID = l.CPROCESS_ID INNER JOIN dbo.TBL_BD_WC w ON l.CWC_ID = w.CID`**。**禁止** **`ON p.CPROCESS_ID = l.CPROCESS_ID`**（见绝对禁止第 **27** 条）。

---

## 业务口径：`TBL_SYS_TEMPLATE_CONFIG`（系统模板配置）

- 同一表内若既有 **`C` 前缀列**（如 `CCODE`、`CNAME`、`CDATA`、`CBINDING`）又有 **PascalCase**（如 `DataSetId`、`DataSetName`、`DataSourceName`、`ObjectName`），物理库常见 **仅有 `C` 前缀真实列**；PascalCase 多为代码实体属性名，**直接写入 T-SQL 会报错误 207**。
- 生成 SQL 时：**优先只选** `CBINDING`、`CBUCKET_NAME`、`CCODE`、`CDATA`、`CDESC`、`CFILE_NAME`、`CFILE_PATH`、`CNAME` 等与本表其它列命名风格一致的字段；**不要**在未经【参考表结构】与真实库一致确认时写 `DataSetName`、`DataSourceName`、`ObjectName`。
- 若业务需要「数据集名称 / 数据源名称」：可能已序列化在 **`CDATA` 或 `CBINDING` 的 JSON** 中，由应用层解析；**不要**假定存在独立列名。
- **硬性禁止（该表一票否决）**：在 `dbo.TBL_SYS_TEMPLATE_CONFIG` 上，**未先做列探测前**，生成的【SQL】中**一律禁止**出现 `DataSetId`、`DataSetName`、`DataSourceId`、`DataSourceName`、`ObjectName`（`SELECT` / `WHERE` / `ORDER BY` / 表达式 / 子查询均不可）。需要这些语义时，先用 `SELECT TOP (1000) *` 或 `INFORMATION_SCHEMA.COLUMNS` 验证真实列，再仅按真实列名改写。

---

## 业务口径：`TBL_MD_DATASET`（数据集 / 参数行）

- 当前口径以 **`CDATASET_TYPE`、`CNAME`、`CDATASOURCE_ID`、`CDATASET_CONDITION`** 为主；生成 SQL 时仅使用本次【参考表结构】中真实出现的字段。  
- **推荐显式列示例**（可加 `WITH (NOLOCK)`）：  
  `SELECT TOP (1000) CDATASET_TYPE, CNAME, CDATASOURCE_ID, CDATASET_CONDITION FROM dbo.TBL_MD_DATASET WITH (NOLOCK)`  
- 若列表字段较多：优先 **`SELECT TOP (1000) * FROM dbo.TBL_MD_DATASET WITH (NOLOCK)`**，由引擎返回全部列名，避免手写不存在字段。

---

## 业务口径：用户组织关系（`TBL_SYS_USER_ORG_MAP` + `TBL_SYS_ORGANIZATION`）

- **`TBL_SYS_USER_ORG_MAP.CORG_ID`** 表示用户所属**组织的主键**，在物理库中通常对应 **`TBL_SYS_ORGANIZATION.CID`**，而不是在组织表上再写一列同名的 `CORG_ID`。  
- **禁止**写 `ON map.CORG_ID = org.CORG_ID`（组织表常无 `CORG_ID` 列，会报错误 207）；应写 **`ON map.CORG_ID = org.CID`**（或片段中明确列出的组织表主键列名，须逐字一致）。  
- 若片段中组织表未列出主键列名：**不要猜测**；应用 `INFORMATION_SCHEMA.COLUMNS` 类说明留给运维，SQL 中仅使用片段已列出的关联列。

---

## 业务口径：用户角色关系（`TBL_SYS_USER_ROLE_MAP` + `TBL_SYS_ROLE`）

- **`TBL_SYS_USER_ROLE_MAP.CROLE_ID`** 在物理库中通常对应 **`TBL_SYS_ROLE.CID`**（角色主键），而不是在角色表再写一列同名 `CROLE_ID`。  
- **禁止**写 `ON urm.CROLE_ID = ru.CROLE_ID`（`TBL_SYS_ROLE` 常无 `CROLE_ID`，会报 **`Invalid column name ''CROLE_ID''`**，错误 **207**）；应写 **`ON urm.CROLE_ID = ru.CID`**（或片段中明确列出的角色表主键列名，须逐字一致）。  
- 角色属性列（如 `CROLE_CODE`、`CROLE_NAME`）仅在片段确有该字段时可选；若片段未列出，优先 `SELECT TOP (1000) *` 探测后再写显式列，禁止猜列名。  
- 若片段未给出 `TBL_SYS_ROLE` 主键列：不要猜测，先 `SELECT TOP (100) *` 或查 `INFORMATION_SCHEMA.COLUMNS` 再写 `JOIN`。

---

## 业务口径：消息群组与成员（`TBL_MSG_GROUP` + `TBL_MSG_GROUP_USER`）

- `TBL_MSG_GROUP_USER.CGROUP_ID` 在物理库中通常对应 `TBL_MSG_GROUP` 主键 **`CID`**。  
- **禁止**写 `ON mg.CGROUP_ID = mug.CGROUP_ID`：`TBL_MSG_GROUP` 常无 `CGROUP_ID` 列，直接报 **`Invalid column name ''CGROUP_ID''`（错误 207）**。  
- **推荐**：`INNER JOIN dbo.TBL_MSG_GROUP_USER mug ON mg.CID = mug.CGROUP_ID`；`SELECT` 群组编码/名称等使用 `mg.CGROUP_CODE`、`mg.CGROUP_NAME`、`mg.CGROUP_DESC` 等片段已列字段。  
- 若片段未给出 `TBL_MSG_GROUP` 主键列：不要猜测，先 `SELECT TOP (100) *`（结构探测）或查 `INFORMATION_SCHEMA.COLUMNS` 后再写 `JOIN`。

---

## 业务口径：消息发送日志（`TBL_MSG_SEND_LOG`）

- 该表时间列常见误写：**接收时间字段是 `CACCEPT_DATETIME`，不是 `CACTIVE_DATETIME`**。生成的【SQL】中在 `dbo.TBL_MSG_SEND_LOG` 上**一律禁止**出现 `CACTIVE_DATETIME`（`SELECT` / `WHERE` / `ORDER BY` / 表达式 / 子查询均不可），否则会触发 **`Invalid column name ''CACTIVE_DATETIME''`（错误 207）**。  
- 可用列以片段为准，常见为：`CACCEPT_DATETIME`、`CCLOSE_DATETIME`、`CCONFIRM_DATETIME`、`CDELETE_DATETIME`、`CMSG_CONTENT`、`CREMARK`、`CSEND_DATETIME`、`CSEND_TYPE`、`CSTATUS`、`CUSER_ID`。  
- **推荐显式列示例**：`SELECT TOP (1000) CACCEPT_DATETIME, CCLOSE_DATETIME, CCONFIRM_DATETIME, CDELETE_DATETIME, CMSG_CONTENT, CREMARK, CSEND_DATETIME, CSEND_TYPE, CSTATUS, CUSER_ID FROM dbo.TBL_MSG_SEND_LOG WITH (NOLOCK)`。  
- 若现场库字段与文档不一致：先 `SELECT TOP (1000) * FROM dbo.TBL_MSG_SEND_LOG WITH (NOLOCK)` 再按返回列名改写，禁止臆造 `CACTIVE_DATETIME` 这类相似拼写。

---

## 业务口径：ESOP 文件类型与模板（`TBL_ESOP_FILE_TYPE` / `TBL_ESOP_TEMPLATE`）

- `TBL_ESOP_FILE_TYPE` 常见字段：`CTYPE_NO`、`CTYPE_NAME`、`CTYPE_DESC`、`CFILE_EXTENDED`；`TBL_ESOP_TEMPLATE` 常见字段：`CFILE_ID`、`CTEMP_FACTORY`、`CTEMP_ID`、`CTEMP_MODEL`、`CTEMP_NO`。  
- 两表在当前片段中**未明确给出可直接关联的共同键**；未确认关联字段前，**禁止**强行 `INNER JOIN`。  
- 生成 SQL 时若用户仅要列表/字段展示，优先单表查询（如分别查类型表或模板表）；确需联表时，必须先在片段中确认两端都存在的关联列，再写完整 `JOIN ... ON ...`。  
- **禁止**输出 `... INNER JOIN dbo.TBL_ESOP_TEMPLATE` 这类无 `ON` 结尾语句（会触发 **`Incorrect syntax near ''TBL_ESOP_TEMPLATE''`，错误 102**）。

---

## 业务口径：WMS 标签打印日志（`TBL_WMS_PRINT_LOG`）

- 该表列名 `order` 为保留字冲突字段，`SELECT` / `WHERE` / `ORDER BY` 中必须写作 **`[order]`**，禁止裸写 `order`（否则报 **156**）。  
- 片段常见字段：`lotcode`、`materialcode`、`materialname`、`[order]`、`printer`、`qty`。  
- **推荐示例**：`SELECT TOP (1000) lotcode, materialcode, materialname, [order], printer, qty FROM dbo.TBL_WMS_PRINT_LOG WITH (NOLOCK)`。  
- 若用户仅要全列或字段存在性不确定，优先 `SELECT TOP (1000) * FROM dbo.TBL_WMS_PRINT_LOG WITH (NOLOCK)`。

---

## 业务口径：仓库主数据与类型（`TBL_WMS_WAREHOUSE` + `TBL_WMS_WAREHOUSE_TYPE`）

- **`TBL_WMS_WAREHOUSE.CWAREHOUSE_TYPE_ID`** 为外键，在物理库中多对应**类型表主键 `CID`**。  
- **禁止**写 **`ON w.CWAREHOUSE_TYPE_ID = wt.CWAREHOUSE_TYPE_ID`**：类型表 **`TBL_WMS_WAREHOUSE_TYPE` 上通常不存在名为 `CWAREHOUSE_TYPE_ID` 的列**（会报 **`Invalid column name ''CWAREHOUSE_TYPE_ID''`**，错误 **207**）。与「用户-组织 `CORG_ID` = `org.CID`」同理。  
- **推荐**：`INNER JOIN dbo.TBL_WMS_WAREHOUSE_TYPE wt ON w.CWAREHOUSE_TYPE_ID = wt.CID`（`SELECT` 中引用类型表主键/属性亦用片段中的 **`wt.CID`** 或 **`wt.CWAREHOUSE_TYPE_NAME`** 等，**勿**写 **`wt.CWAREHOUSE_TYPE_ID`** 除非本片段**明确**列出该列）。主表外键列名若现场为 `CWAREHOUSE_TYPE_CID` 等，**须与片段/现场**一致。  
- 无把握时：两表**分别** `SELECT TOP (1000) *` 或先查 `INFORMATION_SCHEMA.COLUMNS` 再写 `JOIN`。

---

## 业务口径：WMS 盘点明细（文档表常见未部署）

- 见「绝对禁止」第 **24** 条：**禁止** **`TBL_WMS_STOCKTAKING_DTL`**（必 **208** 时勿再生成）。  
- 「按物料分类查已盘点数量 / 盘点结果 / 货位维度盘点」等：若片段**仅有**文档中的 **`STOCKTAKING`** 明细表而无其它已证实可用的库存/盘点表，**不要**拼接 **`INNER JOIN dbo.TBL_WMS_STOCKTAKING_DTL`**；改用第 **24** 条中的 **`sys.tables`** 探测 SQL 拿到**真实表名**后，再按**该表在片段或 `SELECT TOP (100) *` 返回的列**写业务查询。  
- **物料分类 + 物料主数据**在无盘点表时：可退化为仅 **`TBL_BD_ITEM_TYPE` + `TBL_BD_ITEM`**（片段须含），在【相关表】说明「盘点明细表未部署，下列仅物料主数据不含盘点数量」。  
- 【SQL】**禁止**夹杂 **`--` 行注释或 `/* */`**（见输出格式：单条可执行语句、不要注释）。

---

## 业务口径：设备 / 采集「报警记录」

- **与片段是否包含 `TBL_EAP_ALARM` 无关**：见上文「绝对禁止」第 8 条——**永不生成** `TBL_EAP_ALARM`。  
- **唯一允许**的报警明细主表名为 **`TBL_EAP_T_ALARM`**（报警记录表）；列以片段为准，典型为 **`C_ID`、`CALARM`、`COCCUR_DATE`、`CCLEAR_DATE`**。  
- **正确写法示例**（片段含上述列时可直接套用结构；表可加 `WITH (NOLOCK)`）：  
  `SELECT TOP (1000) C_ID, CALARM, COCCUR_DATE, CCLEAR_DATE FROM dbo.TBL_EAP_T_ALARM WITH (NOLOCK) ORDER BY COCCUR_DATE DESC`  
- 知识库检索应**优先注入 `TBL_EAP_T_ALARM` 表结构**；若仍只检索到 `TBL_EAP_ALARM`，模型也**不得**输出 `TBL_EAP_ALARM`，须在【相关表】提示更新检索文档。

---

## 业务口径：AOI / VRS 检测（文档表未部署时的处理）

- 见「绝对禁止」第 9 条：**禁止** `TBL_EAP_AOI_DETECTIONS` 与 `TBL_EAP_AOI_DETECTIONS_DTL`。  
- 用 **`sys.tables`** 列出含 `AOI`/`VRS`/`DETECT` 的对象后，将【用户问题】或知识库改为**真实表名**，再按该表在片段中的字段生成业务 `SELECT`。  
- 若现场实际为班通/麦逊/宇之光等采集：**不要**套用 AOI 文档表名，改用对应 **`TBL_EAP_LWT_*` / `TBL_EAP_MASON_*` / `TBL_EAP_YULIGHT_*`** 等（须片段中有该表）。

---

## 业务口径：`TBL_EAP_DATA`（EAP 采集数据）

- **`CID` / `CDT` / `CTYPE` / `CVALUE_TYPE` / `CVALUE_STRING` / `CSERVER_ID` / `CVALUE` 等**：文档列名与**中络等现场物理库**常见不一致，易连续 **207**。**禁止**从文档或记忆「套模板」拼显式列名（**含** `CVALUE_STRING`，现场常不存在）。  
- **唯一推荐的首查语句**（无列名假设）：  
  `SELECT TOP (1000) * FROM dbo.TBL_EAP_DATA WITH (NOLOCK)`  
  后续若需显式列：**仅允许**从 **`INFORMATION_SCHEMA.COLUMNS` 查询结果**或**上一步 `*` 结果集**中**逐字复制**列名再写 `SELECT`，**禁止**再使用本文档或常见命名猜测。  
- **不要**默认加 `ORDER BY CDATETIME_CREATED`；仅当已证实该列存在时再排序，否则省略 `ORDER BY`。  
- **禁止**把 `CDATETIME_CREATED` 自行缩写成 **`CDT`** 当作列名。  
- 大量联机数据可能在 **`TBL_EAP_DATA_YYYYMM`** 等**分表**；用户问「EAP 采集/测点数据」且片段出现分表命名规则时，**不得**只假定 `TBL_EAP_DATA` 单表即全量。  
- 若业务实为**实时测点快照**：对照片段考虑 **`TBL_EAP_CURRENT_DATA`**，**勿**把 `TBL_EAP_DATA` 文档列硬套到该表。

---

## 业务口径：查询结果中文乱码（编码错位，不是 SQL 语法错）

- 若用户提供的结果出现 `¼ì²é`、`Çå½à`、`ÂÛ` 等明显乱码形态，优先判断为**客户端/驱动解码错误**（常见是 GBK/CP936 与 UTF-8/Latin-1 不一致），而非 SQL 语法问题。  
- 生成 SQL 时仍只做**数据查询本身**，不要试图用臆造函数“修复编码”；禁止输出不存在于 SQL Server 的编码转换函数。  
- 字符串条件与常量一律使用 `N''中文''`（Unicode 字面量），避免再次触发隐式编码损失。  
- 除非用户明确要求，**不要**在 SQL 中把中文列 `CAST/CONVERT` 为 `VARCHAR`；优先保持 `NVARCHAR/NCHAR` 语义。  
- 用户要求“排查乱码原因”时，可输出一条结构探测 SQL（单条）检查列数据类型，例如：  
  `SELECT TOP (1000) COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = ''dbo'' AND TABLE_NAME = ''目标表名'' ORDER BY ORDINAL_POSITION`  
- 若用户贴出的“报错”实际是乱码结果而无错误码（如 207/208/8127/156），在【相关表】中明确写「当前更像编码/连接字符集问题，非 SQL 语法错误」，并继续给出仅使用白名单字段的最小可用查询。

---