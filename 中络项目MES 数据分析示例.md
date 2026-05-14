数据库表结构模板
工单 + 工位生产报工（5 表）
表名： TBL_BD_ITEM（产品和物料信息表）
业务含义： 维护本厂料号、规格、客户料号及物料类型等主数据。
字段列表（节选）：
- CID long 主键（文档中外键统一写为对应 [TBL_BD_ITEM].[CID]）
- CITEM_NO string 产品编号
- CITEM_NAME string 产品名称
- CITEM_DESC string 产品描述
- CITEM_TYPE_ID long? 产品类型 ID（可再扩链到 TBL_BD_ITEM_TYPE）
- CUSTOMER_CODE string 客户代码
关联关系：
（本表为物料维度的根；下游表通过 CITEM_ID 引用 CID。）

表名： TBL_MO（工单信息表）
业务含义： 按批次/层级描述生产工单的计划、状态及当前工序、工作中心等。
字段列表（节选）：
- CMO_LOT string 工单批次（与报工、检验等多表对齐）
- CORDER_NO string 工单编号
- CITEM_ID long? 物料 ID，对应 TBL_BD_ITEM.CID
- CPROCESS_ID long? 工序 ID
- CWC_ID long? 工作中心 ID
- CPLAN_QTY decimal? 计划数量
- CCOMPLETED_QTY decimal? 完工数量
- CUST_CODE string 客户代码
关联关系：
- TBL_MO.CITEM_ID = TBL_BD_ITEM.CID

表名： TBL_BD_PROCESS（工序工艺信息表）
业务含义： 工序主数据（编码、名称、顺序、路径等）。
字段列表（节选）：
- CID long 主键（文档强调：TBL_MO.CPROCESS_ID、TBL_SFC_WS_LOG.CPROCESS_ID 等指向 TBL_BD_PROCESS.CID，不能误用 p.CPROCESS_ID 作工序主键列）
- CPROCESS_NO string 工序编码
- CPROCESS_NAME string 工序名称
- CPROCESS_SEQ int? 工序顺序
关联关系：
- TBL_MO.CPROCESS_ID = TBL_BD_PROCESS.CID（与工单当前工序一致时）
- TBL_SFC_WS_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID

表名： TBL_SFC_WS_LOG（生产记录表）
业务含义： 工位报工/检验类生产记录主表（数量、班次、条码、模板等）。
字段列表（节选）：
- CID long 主键；与子表关联为 l.CID = i.CWS_LOG_ID（主表无 CWS_LOG_ID）
- CMO_LOT string 工单批次
- CITEM_ID long? 物料 ID，对应 TBL_BD_ITEM.CID
- CPROCESS_ID long 工序 ID
- CWC_ID long 工作中心 ID
- CWORK_NUMBER decimal 工作数量
- CNG_NUMBER decimal? 不良数量
- CSCRAP_NUMBER decimal? 报废数量
- CUSTOMER_CODE string 客户编码（文档强调：勿写成 CCUSTOMER_CODE）
- CSCAN_BARCODE string 扫描条码
- CTEMPLATE_ID long 模板 ID
关联关系：
- TBL_SFC_WS_LOG.CMO_LOT = TBL_MO.CMO_LOT（工单与报工的主业务键，多行工单时注意与 CITEM_ID/CPROCESS_ID 联合约束）
- TBL_SFC_WS_LOG.CITEM_ID = TBL_BD_ITEM.CID
- TBL_SFC_WS_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID

表名： TBL_SFC_WS_LOG_ITEM（生产记录项目明细表）
业务含义： 生产记录主表按检验/报工模板的逐项录入结果。
字段列表（节选）：
- CWS_LOG_ID long 生产记录主表 ID
- CTEMPLATE_ITEM_CODE string 模板项编码
- CTEMPLATE_ITEM_NAME string 模板项名称
- CINPUT_VALUE string 输入值
- CRESULT int 结果
- CSTANDARD_VALUE string 标准值
- CUNIT string 单位
关联关系：
- TBL_SFC_WS_LOG_ITEM.CWS_LOG_ID = TBL_SFC_WS_LOG.CID

五表串联关系小结（推荐 JOIN 顺序）
TBL_BD_ITEM → TBL_MO（CITEM_ID）→ TBL_BD_PROCESS（CPROCESS_ID）→ TBL_SFC_WS_LOG（CMO_LOT + 可选 CITEM_ID/CPROCESS_ID 收紧）→ TBL_SFC_WS_LOG_ITEM（CID = CWS_LOG_ID）。

数据库查询示例
输入问题
请按工单批次 WOA012604292842-00-001-001 查询：料号、品名及客户编码；工单的计划数量、完工数量、当前状态；该批次下每一笔工位报工的开工/完工时间、工作中心、工序名称与工序编码、工作数量、不良、报废、报工上的客户编码；以及每笔报工在模板中的每一项：项目名称、标准值、录入值、判定结果。
生成SQL
{
  "sql": "SELECT TOP (1000)\n  i.CITEM_NO AS [料号], i.CITEM_NAME AS [品名], l.CUSTOMER_CODE AS [客户编码], m.CPLAN_QTY AS [计划数量], m.CCOMPLETED_QTY AS [完工数量], m.CSTATUS AS [当前状态], l.CSTART_TIME AS [开工时间], l.CEND_TIME AS [完工时间], wc.CWC_NAME AS [工作中心], p.CPROCESS_NAME AS [工序名称], p.CPROCESS_NO AS [工序编码], l.CWORK_NUMBER AS [工作数量], l.CNG_NUMBER AS [不良], l.CSCRAP_NUMBER AS [报废], log_item.CTEMPLATE_ITEM_NAME AS [项目名称], log_item.CSTANDARD_VALUE AS [标准值], log_item.CINPUT_VALUE AS [录入值], log_item.CRESULT AS [判定结果]\nFROM dbo.TBL_MO m\nINNER JOIN dbo.TBL_BD_ITEM i ON m.CITEM_ID = i.CID\nINNER JOIN dbo.TBL_SFC_WS_LOG l ON m.CMO_LOT = l.CMO_LOT\nINNER JOIN dbo.TBL_BD_PROCESS p ON l.CPROCESS_ID = p.CID\nINNER JOIN dbo.TBL_BD_WC wc ON l.CWC_ID = wc.CID\nLEFT JOIN dbo.TBL_SFC_WS_LOG_ITEM log_item ON l.CID = log_item.CWS_LOG_ID\nWHERE m.CMO_LOT = N'WOA012604292842-00-001-001'\nORDER BY l.CSTART_TIME DESC"
}
查询结果


暂时无法在飞书文档外展示此内容
SQL业务表
这条 SQL 一共查了 6 张表
TBL_MO、TBL_BD_ITEM、TBL_SFC_WS_LOG、TBL_BD_PROCESS、TBL_BD_WC、TBL_SFC_WS_LOG_ITEM
关联关系（业务语义）：
- 工单 → 物料：TBL_MO 通过 CITEM_ID 指向 TBL_BD_ITEM 主键 CID，取料号、品名。
- 工单 → 工位报工：TBL_MO 与 TBL_SFC_WS_LOG 用 CMO_LOT（工单批次） 对齐。
- 报工 → 工序：TBL_SFC_WS_LOG 的 CPROCESS_ID 指向 TBL_BD_PROCESS 主键 CID（文档要求用 p.CID，不能误用 p.CPROCESS_ID）。
- 报工 → 工作中心：TBL_SFC_WS_LOG 的 CWC_ID 指向 TBL_BD_WC 主键 CID，取工作中心名称。
- 报工主表 → 报工明细：TBL_SFC_WS_LOG 主键 CID 对应 TBL_SFC_WS_LOG_ITEM 的 CWS_LOG_ID（主表没有 CWS_LOG_ID 列）；用 LEFT JOIN 表示没有明细行时主表报工仍会出现。
过滤条件： m.CMO_LOT = N'WOA012604292842-00-001-001'。


---
备注：以上数据来自中络MES CIMOM_TEST数据库
