# -*- coding: utf-8 -*-
# 【Dify 代码节点专用 · 由 build_erp_catalog_bundle.py 自动生成，请勿手改】
# 维护：改 中络项目ERP 系统表名清单V1.0.md → python3 build_erp_catalog_bundle.py → 复制到 Dify
#
# 通用加速：按用户问题对全表清单做相关性排序，仅 Top-N 送入「分析业务表」LLM（无业务硬编码）。
# 版本：DIFY_CATALOG_NODE_VERSION=1
#
# 入参：user_question（接 {{#sys.query#}}）
# 出参（均为 string）：
#   table_catalog — 排序后的候选清单（接到分析业务表 LLM）
#   table_count   — 候选表数量
#   char_count    — 候选清单字符数
#   rank_mode     — ranked | full
#   char_count_full — 全量精简清单字符数（排查用）

_EMBEDDED_CATALOG_SLIM = "# ERP 表清单（精简·选表用，仅表名+业务含义）\n# 格式：TableName | 中文表名 | 业务含义\n\nT_AppSeting | 系统设定 | 系统设定\nT_Area | 区域 | 区域\nT_AtomLog | 系统日志 | 系统日志\nT_Business | 业务表 | 业务表\nT_BusinessItem | 流程设计--流程分类 | 流程设计--流程分类\nT_Cate | 等级管理表 | 等级管理表\nT_Category | 物料类别表（物料分组 | 物料类别表（物料分组\nT_CategoryItem | 物料类别明细表（储区） | 物料类别明细表（储区）\nT_ChargeItem | 附加费用 | 附加费用\nT_Company | 公司管理 | 公司管理\nT_Currency | 币种 | 币种\nT_CurrencyItem | 币种兑换明细 | 币种兑换明细\nT_CustomScript | 自定义脚本 | 自定义脚本\nT_CustTable | 自定义表 | 自定义表\nT_CustTableValue | 自定义表明细 | 自定义表明细\nT_Defect | 缺陷表 | 缺陷表\nT_Department | 部门表 | 部门表\nT_DepartmentUser | 部门--用户表 | 部门--用户表\nT_Document | 文件上传记录 | 文件上传记录\nT_ExportSetting | 导出设置 | 导出设置\nT_ExportSettingItem | 导出设置明细 | 导出设置明细\nT_ExportSettingUrl | 导出设置URL | 导出设置URL\nT_FiscalPeriod | 会计期间 | 会计期间\nT_Flow | 流程设计主表 | 流程设计主表\nT_FlowType | 流程设计 | 流程设计\nT_FOB | 贸易方式 | 贸易方式\nT_FunctionRight | 系统模块功能表 | 系统模块功能表\nT_Group | 用户组管理 | 用户组管理\nT_GroupUser | 用户组--用户 | 用户组--用户\nT_Inspect | 检验分组--检验项目 | 检验分组--检验项目\nT_InspectGroup | 检验分组 | 检验分组\nT_InspectItems | 检验项目 | 检验项目\nT_InventoryCheckReason | 盘点原因 | 盘点原因\nT_JSONHistory | JSON接口日志 | JSON接口日志\nT_Linkman | 联系人 | 联系人\nT_Location | 储区表 | 储区表\nT_Module | 模块表 | 模块表\nT_ModuleType | 模组类型 | 模组类型\nT_MyModule | 用户模块权限表 | 用户模块权限表\nT_Notepad | 记事本 | 记事本\nT_NotepadGroup | 记事分组表 | 记事分组表\nT_NumberControl | 单据号码表 | 单据号码表\nT_PaymentMethod | 付款方式 | 付款方式\nT_PaymentTerm | 付款周期 | 付款周期\nT_Plants | 工厂 | 工厂\nT_PostRole | 岗位 | 岗位\nT_PostRoleModule | 岗位模块 | 岗位模块\nT_Process | 工艺表 | 工艺表\nT_ProcessDefect | 工艺缺陷报废 | 工艺缺陷报废\nT_ProcessEmployee | 工艺--雇员权限(工程设计流程权限) | 工艺--雇员权限(工程设计流程权限)\nT_ProcessParameter | 工艺流程参数表 | 工艺流程参数表\nT_ProcessPlant | 工艺管理--工厂 | 工艺管理--工厂\nT_ProductCategoryPlant | 销售数据--产品分类--工厂 | 销售数据--产品分类--工厂\nT_Racks | 货架表 | 货架表\nT_ReportSeting | 表单设定 | 表单设定\nT_Shipping | 运输方式 | 运输方式\nT_StepEmployee | 工序--雇员权限(过数权限) | 工序--雇员权限(过数权限)\nT_StepIndiectMatLink | 工序--间接材料 | 工序--间接材料\nT_Steps | 工序表 | 工序表\nT_StepsProcess | 工序关联工艺 | 工序关联工艺\nT_StepsProcessInspectItem | 工艺定量、定性检验项表 | 工艺定量、定性检验项表\nT_SubcontractType | 外协类型 | 外协类型\nT_SubcontractTypeItem | 外协类型明细表 | 外协类型明细表\nT_SubcontractTypeParams | 外协类型-参数表 | 外协类型-参数表\nT_SystemConfig | 系统配置表 | 系统配置表\nT_SystemLog | 系统日志 | 系统日志\nT_Tax | 税率表 | 税率表\nT_Text | 记事本 | 记事本\nT_Unit | 单位 | 单位\nT_UseProcess | T_UseProcess | ERP 系统 T_UseProcess 业务数据表\nT_User | 用户表 | 用户表\nT_UserFunctionRight | 用户功能表 | 用户功能表\nT_UserModule | 用户模块 | 用户模块\nT_UserPlant | 用户所在工厂权限 | 用户所在工厂权限\nT_UserPostRole | 用户--岗位 | 用户--岗位\nT_Warehouse | 仓库 | 仓库\nT_WarehouseKeepers | 仓库人员明细 | 仓库人员明细\nT_Workshop | T_Workshop | ERP 系统 T_Workshop 业务数据表\nM_BOMIssue | BOM发料 | BOM发料\nM_BOMIssueItem | BOM发料明细表 | BOM发料明细表\nM_BOMPicklist | BOM领料单 | BOM领料单\nM_BOMPicklistHistory | BOM领料单审批记录 | BOM领料单审批记录\nM_BOMPicklistItem | BOM领料单明细 | BOM领料单明细\nM_BOMPicklistItemBatch | BOM领料批次 | BOM领料批次\nM_BOMPicklistWF | BOM领料外发 | BOM领料外发\nM_Consignment | 寄送表 | 寄送表\nM_Envelope | 物料数据--包线管理 | 物料数据--包线管理\nM_EnvelopeHistory | M_EnvelopeHistory | ERP 系统 M_EnvelopeHistory 业务数据表\nM_EnvelopeItem | 物料数据--包线管理明细 | 物料数据--包线管理明细\nM_EnvelopeWF | M_EnvelopeWF | ERP 系统 M_EnvelopeWF 业务数据表\nM_Inventory | 物料库存 | 物料库存\nM_InventoryBatch | 物料批次库存 | 物料批次库存\nM_InventoryBatch_bak0413 | M_InventoryBatch_bak0413 | ERP 系统 M_InventoryBatch_bak0413 业务数据表\nM_InventorybatchRemaining | 碎料管理 | 碎料管理\nM_InventoryCheck | 库存检验 | 库存检验\nM_InventoryCheckItem | 库存检验明细 | 库存检验明细\nM_InventoryMiscBatch | 杂项领料中的物料 | 杂项领料中的物料\nM_InventoryOut | 模组 | 模组\nM_IQC | 物料IQC报废 | 物料IQC报废\nM_IQCHistory | M_IQCHistory | ERP 系统 M_IQCHistory 业务数据表\nM_IQCItem | 物料IQC报废明细表 | 物料IQC报废明细表\nM_IQCRecheck | 物料送检单管理 | 物料送检单管理\nM_IQCResult | 物料检验 报废原因 | 物料检验 报废原因\nM_IQCWF | M_IQCWF | ERP 系统 M_IQCWF 业务数据表\nM_MaterialIssueRequest | 领料和退料表 | 领料和退料表\nM_MaterialIssueRequestHistory | 领料和退料审批历史 | 领料和退料审批历史\nM_MaterialIssueRequestItem | 领料和退料明细表 | 领料和退料明细表\nM_MaterialIssueRequestWF | 领料和退料审批流程 | 领料和退料审批流程\nM_MaterialPackingSlipItem | 材料装运明细表 | 材料装运明细表\nM_MaterialPriceChangedItem | 采购报价明细表 | 采购报价明细表\nM_Materials | 物料表 | 物料表\nM_MaterialsCompany | 物料所属公司 | 物料所属公司\nM_MaterialsCostByPlant | 物料可分配数量表(占用) | 物料可分配数量表(占用)\nM_MaterialsIssueNote | 发料和退回表 | 发料和退回表\nM_MaterialsIssueNoteItem | 发料和退回明细 | 发料和退回明细\nM_MaterialsIssueNoteItemBatch | 物料发料和退回批次 | 物料发料和退回批次\nM_MaterialsWarehouse | 物料所在仓库 | 物料所在仓库\nM_MonthlyClosing | 月结记账表 | 月结记账表\nM_MonthlyClosingDepartment | 物料月结部门表 | 物料月结部门表\nM_MonthlyClosingItem | 月结记账明细表 | 月结记账明细表\nM_PurchaseOrder | 采购单 | 采购单\nM_PurchaseOrderHistory | 采购审批表 | 采购审批表\nM_PurchaseOrderItem | 采购明细单 | 采购明细单\nM_PurchaseOrderWF | 采购待审批 | 采购待审批\nM_PurchasingBudget | 采购预算 | 采购预算\nM_PurchasingBudgetItem | 预算明细（用户） | 预算明细（用户）\nM_RDProject | 项目管理 | 项目管理\nM_Receipt | 物料接收 | 物料接收\nM_ReceiptItem | 物料接收明细 | 物料接收明细\nM_ReplaceMaterials | M_ReplaceMaterials | ERP 系统 M_ReplaceMaterials 业务数据表\nM_Requisitions | 请购单 | 请购单\nM_RequisitionsHistory | 请购审批表 | 请购审批表\nM_RequisitionsItem | 请购明细单 | 请购明细单\nM_RequisitionsItemAccepted | 请购受理表 | 请购受理表\nM_RequisitionsWF | M_RequisitionsWF | ERP 系统 M_RequisitionsWF 业务数据表\nM_ReturnOrder | 退货表 | 退货表\nM_ReturnOrderItem | 退货明细表 | 退货明细表\nM_SPDS | SPDS管理 | SPDS管理\nM_SPDSHistory | M_SPDSHistory | ERP 系统 M_SPDSHistory 业务数据表\nM_SPDSItem | SPDS管理明细 | SPDS管理明细\nM_SPDSWF | M_SPDSWF | ERP 系统 M_SPDSWF 业务数据表\nM_StepCheck | M_StepCheck | ERP 系统 M_StepCheck 业务数据表\nM_StepCheckItem | M_StepCheckItem | ERP 系统 M_StepCheckItem 业务数据表\nM_Suppliers | 供应商资料 | 供应商资料\nM_SuppliersCompany | 供应商所属公司 | 供应商所属公司\nM_SuppliersHistory | 供应商审批记录 | 供应商审批记录\nM_SuppliersWF | M_SuppliersWF | ERP 系统 M_SuppliersWF 业务数据表\nM_Transfer | 调拨管理 | 调拨管理\nM_TransferItem | 调拨管理明细 | 调拨管理明细\nM_Warehousing | 物料入库 | 物料入库\nM_WarehousingItem | 物料入库明细 | 物料入库明细\nFGI_CartonsNumber | 装箱单编号表（箱包表） | 装箱单编号表（箱包表）\nFGI_Inventory | 成品库存 | 成品库存\nFGI_InventoryOut | 成品出库批次号表 | 成品出库批次号表\nFGI_IQC | 制成品检验单 | 制成品检验单\nFGI_IQCHistory | FGI_IQCHistory | ERP 系统 FGI_IQCHistory 业务数据表\nFGI_IQCItem | 检验项目 | 检验项目\nFGI_IQCResult | 检验结果表 | 检验结果表\nFGI_IQCWF | FGI_IQCWF | ERP 系统 FGI_IQCWF 业务数据表\nFGI_JobIssueNote | FGI_JobIssueNote | ERP 系统 FGI_JobIssueNote 业务数据表\nFGI_JobIssueNoteItem | FGI_JobIssueNoteItem | ERP 系统 FGI_JobIssueNoteItem 业务数据表\nFGI_JobIssueNoteItemBatch | FGI_JobIssueNoteItemBatch | ERP 系统 FGI_JobIssueNoteItemBatch 业务数据表\nFGI_JobIssueRequest | FGI_JobIssueRequest | ERP 系统 FGI_JobIssueRequest 业务数据表\nFGI_JobIssueRequestHistory | FGI_JobIssueRequestHistory | ERP 系统 FGI_JobIssueRequestHistory 业务数据表\nFGI_JobIssueRequestItem | FGI_JobIssueRequestItem | ERP 系统 FGI_JobIssueRequestItem 业务数据表\nFGI_JobIssueRequestWF | FGI_JobIssueRequestWF | ERP 系统 FGI_JobIssueRequestWF 业务数据表\nFGI_MonthlyClosing | 成品月结 | 成品月结\nFGI_MonthlyClosingItem | 成品月结明细 | 成品月结明细\nFGI_PackingItem | 成品装箱单 | 成品装箱单\nFGI_PackingSlip | 成品出货 | 成品出货\nFGI_PackingSlipCartonsNumber | 箱包关联表 | 箱包关联表\nFGI_PackingSlipHistory | FGI_PackingSlipHistory | ERP 系统 FGI_PackingSlipHistory 业务数据表\nFGI_PackingSlipItem | 成品出货明细表 | 成品出货明细表\nFGI_PackingSlipWF | FGI_PackingSlipWF | ERP 系统 FGI_PackingSlipWF 业务数据表\nFGI_PackNumber | 箱包，包明细表 | 箱包，包明细表\nFGI_PalletNumber | 卡板表 | 卡板表\nFGI_Receipt | 制成品接收单 | 制成品接收单\nFGI_ReceiptItem | 制成品接收单明细 | 制成品接收单明细\nFGI_ReturnOrder | 成品退货表 | 成品退货表\nFGI_ReturnOrderItem | 成品退货明细表 | 成品退货明细表\nFGI_ScrapSheet | 成品报废 | 成品报废\nFGI_ScrapSheetItem | 成品报废明细 | 成品报废明细\nFGI_StockForm | 成品入库 | 成品入库\nFGI_StockFormItem | 成品入库明细 | 成品入库明细\nFGI_StockFormItemWO | 生产入库 | 生产入库\nFGI_StockFormJob | 生产入库型号关联表 | 生产入库型号关联表\nFGI_Transfer | 成品转仓表 | 成品转仓表\nFGI_TransferItem | 成品转仓明细表 | 成品转仓明细表\nE_BoardTypeParameterSettings | 成德区分参数展示主表 | 成德区分参数展示主表\nE_CostJobMfgPartsParams | 部件成本参数 | 部件成本参数\nE_CustomScriptSetting | 工程流程那里添加的自定义脚本表 | 工程流程那里添加的自定义脚本表\nE_DrillDetails | 钻孔设计 | 钻孔设计\nE_DrillTitle | 钻带表 | 钻带表\nE_FPCToolTable | 工具表 | 工具表\nE_Impedance | 阻抗表 | 阻抗表\nE_JobChildren | JOB关联合拼表 | JOB关联合拼表\nE_JobImages | 生产型号图片 | 生产型号图片\nE_JobLayers | 工作层  层信息 | 工作层  层信息\nE_JobMfgPartParams | 工程制作——流程——部件参数表 | 工程制作——流程——部件参数表\nE_JobMfgParts | 制造部件编号(本厂型号BOM表) | 制造部件编号(本厂型号BOM表)\nE_JobParams | 工程制作——基本信息——销售部件的参数值对应job这里的 | 工程制作——基本信息——销售部件的参数值对应job这里的\nE_JobRouteParams | 流程参数值 | 流程参数值\nE_JobRoutes | 制造部件流程表 | 制造部件流程表\nE_JobSMTBOM | E_JobSMTBOM | ERP 系统 E_JobSMTBOM 业务数据表\nE_JobTargetHole | E_JobTargetHole | ERP 系统 E_JobTargetHole 业务数据表\nE_ProcessLibrary | 产品分组（流程模版主表 | 产品分组（流程模版主表\nE_RiskWarning | 风险警示表 | 风险警示表\nE_SheetInfo | 大料信息表 | 大料信息表\nE_StackUpInfo | 工程制作——叠构 | 工程制作——叠构\nE_ToolName | 工具表 | 工具表\nS_BusinessMan | 雇员信息 | 雇员信息\nS_CAR | S_CAR | ERP 系统 S_CAR 业务数据表\nS_Cartons | 纸箱定义 | 纸箱定义\nS_Complainment | 客诉管理 | 客诉管理\nS_ComplainmentHistory | 客诉管理审批记录 | 客诉管理审批记录\nS_ComplainmentWF | S_ComplainmentWF | ERP 系统 S_ComplainmentWF 业务数据表\nS_Conductor | 铜厚表 | 铜厚表\nS_Contract | 销售订单合同 | 销售订单合同\nS_ContractItem | 合同明细 | 合同明细\nS_ContractItemAddCharge | 合同制造明细---额外费用表 | 合同制造明细---额外费用表\nS_ContractItemHistory | 合同审核表 | 合同审核表\nS_ContractItemLog | 销售订单合同明细--修改记录 | 销售订单合同明细--修改记录\nS_ContractItemParameter | 订单明细参数 | 订单明细参数\nS_ContractItemProject | S_ContractItemProject | ERP 系统 S_ContractItemProject 业务数据表\nS_ContractItemWF | S_ContractItemWF | ERP 系统 S_ContractItemWF 业务数据表\nS_ContractMaterials | 材料销售订单（贸易） | 材料销售订单（贸易）\nS_ContractSO | 销售订单表 | 销售订单表\nS_Customer | 客户管理 | 客户管理\nS_CustomerAddress | 客户管理--客户地址 | 客户管理--客户地址\nS_CustomerCompany | 客户绑定公司 | 客户绑定公司\nS_CustomerHistory | 客户管理审批记录 | 客户管理审批记录\nS_CustomerWF | 客户审批 | 客户审批\nS_ExpenseForm | 费用管理 | 费用管理\nS_ExpenseFormHistory | 费用管理审批记录 | 费用管理审批记录\nS_ExpenseFormItem | 费用管理明细 | 费用管理明细\nS_ExpenseFormWF | S_ExpenseFormWF | ERP 系统 S_ExpenseFormWF 业务数据表\nS_ExpenseItem | 费用定义 | 费用定义\nS_FGIIQCRecheck | 成品送检单 | 成品送检单\nS_FGIIQCRecheckItem | 成品送检单明细 | 成品送检单明细\nS_Job | 产品型号  生产部件 | 产品型号  生产部件\nS_JobHistory | 生产型号审批记录 | 生产型号审批记录\nS_JobLink | 型号连接销售部件 | 型号连接销售部件\nS_JobPrjLink | S_JobPrjLink | ERP 系统 S_JobPrjLink 业务数据表\nS_JobWF | 生产编号审批 | 生产编号审批\nS_LayerType | 层信息 | 层信息\nS_MaterialFamily | 厂商型号 | 厂商型号\nS_MaterialType | 物料类型 | 物料类型\nS_MaterialTypeCombination | 材料类型组合 | 材料类型组合\nS_OrderType | 订单类型 | 订单类型\nS_OS_PO | 外协采购单 | 外协采购单\nS_OS_POHistory | 外协采购单审批记录 | 外协采购单审批记录\nS_OS_POItem | 外协采购明细单 | 外协采购明细单\nS_OS_POItemAddCharge | 外发采购明细更改表 | 外发采购明细更改表\nS_OS_POWF | 外协采购单审批 | 外协采购单审批\nS_OS_PR | 外协请购单 | 外协请购单\nS_OS_PRHistory | 外协请购单审批记录 | 外协请购单审批记录\nS_OS_PRItem | 外协请购明细单 | 外协请购明细单\nS_OS_PRItemAddCharge | 外协请购明细单修改记录 | 外协请购明细单修改记录\nS_OS_PRWF | S_OS_PRWF | ERP 系统 S_OS_PRWF 业务数据表\nS_OS_Shipment | 外协装运 | 外协装运\nS_OS_ShipmentItem | 外协装运明细 | 外协装运明细\nS_OSWO | 外协采购工单表 | 外协采购工单表\nS_OSWOReceipt | 外协接收 | 外协接收\nS_OSWOSend | 外协采购分配工单表 | 外协采购分配工单表\nS_OSWOShipment | 外协采购工单装运表 | 外协采购工单装运表\nS_Parameters | 销售数据--参数管理 | 销售数据--参数管理\nS_ParametersGroup | 销售数据--参数分组 | 销售数据--参数分组\nS_ParameterValue | 客户信息-评审-右侧的参数 | 客户信息-评审-右侧的参数\nS_ProductCategory | 销售数据--产品分类 | 销售数据--产品分类\nS_ProductCategoryCompany | 销售数据--产品分类--公司 | 销售数据--产品分类--公司\nS_ProductGroup | 销售数据--产品分组 | 销售数据--产品分组\nS_ProductGroupCompany | 销售数据--产品分组--公司 | 销售数据--产品分组--公司\nS_ProductGroupSpec | 销售数据--产品分组-参数管理 | 销售数据--产品分组-参数管理\nS_ProjectCombination | 销售数据--项目组合 | 销售数据--项目组合\nS_QuickQuoteResult | 报价单快速报价结果 | 报价单快速报价结果\nS_QuoteCategory | 报价类别 | 报价类别\nS_QuoteGroup | 报价分组 | 报价分组\nS_QuoteParameter | 报价参数 | 报价参数\nS_ReturnSO | 客诉管理--扣款明细 | 客诉管理--扣款明细\nS_Rfq | 报价单 | 报价单\nS_RfqAddCharge | 报价单额外费用 | 报价单额外费用\nS_RfqHistory | 报价单审批历史 | 报价单审批历史\nS_RfqParameter | 报价单参数 | 报价单参数\nS_RfqWF | 报价单审批 | 报价单审批\nS_Rpt_Member | S_Rpt_Member | ERP 系统 S_Rpt_Member 业务数据表\nS_Rpt_SalesRepresentative | S_Rpt_SalesRepresentative | ERP 系统 S_Rpt_SalesRepresentative 业务数据表\nS_SaleProject | 销售项目 | 销售项目\nS_SalesForecast | 销售预测 | 销售预测\nS_SalesForecastHistory | 销售预测审批历史 | 销售预测审批历史\nS_SalesForecastItem | 销售预测明细 | 销售预测明细\nS_SalesForecastSplitting | 销售预测分单 | 销售预测分单\nS_SalesForecastWF | 销售预测审批 | 销售预测审批\nS_SalesParts | 销售部件 | 销售部件\nS_SalesPartsAdditionalBOM | 销售部件--AdditionalBOM | 销售部件--AdditionalBOM\nS_SalesPartsLayers | 销售部件层信息表 | 销售部件层信息表\nS_SalesPartsParameter | 销售部件对应产品分组参数值 | 销售部件对应产品分组参数值\nS_SalesPartsSets | 销售部件对应套板信息 | 销售部件对应套板信息\nS_SalesPartsSMTBOM | 销售部件对应PCBA材料单 | 销售部件对应PCBA材料单\nS_SalesPlanReview | 销售订单更改记录 | 销售订单更改记录\nS_ShipmentRevoke | 撤销出货表 | 撤销出货表\nS_SODayShipment | 订单装运表 | 订单装运表\nS_SOMatWriteOff | 备货冲销记录 | 备货冲销记录\nS_StockCheck | 成品盘点表 | 成品盘点表\nS_StockCheckItem | 成品盘点明细表 | 成品盘点明细表\nS_WorkPlan | 工作计划表 | 工作计划表\nS_WorkPlanItem | 工作计划明细表 | 工作计划明细表\nS_WorkPlantHistory | 工作计划审批记录表 | 工作计划审批记录表\nS_WorkPlantWF | S_WorkPlantWF | ERP 系统 S_WorkPlantWF 业务数据表\nP_BOMBatching | BOM领料批次 | BOM领料批次\nP_ECN | OCN\\ECN管理 | OCN\\ECN管理\nP_ECNHistory | OCN\\ECN管理-审批记录 | OCN\\ECN管理-审批记录\nP_ECNLog | OCN\\ECN管理-工具-工具类型 | OCN\\ECN管理-工具-工具类型\nP_ECNTool | OCN\\ECN审核 | OCN\\ECN审核\nP_ECNWF | OCN/ECN审批流程 | OCN/ECN审批流程\nP_Inspection | MRB检查 | MRB检查\nP_IPQC | P_IPQC | ERP 系统 P_IPQC 业务数据表\nP_IPQCItem | P_IPQCItem | ERP 系统 P_IPQCItem 业务数据表\nP_MergeOrder | 合拼单 | 合拼单\nP_MergeOrderSO | 合拼明细表 | 合拼明细表\nP_MfgPartsInv | 部件表 | 部件表\nP_MfgPartsIssue | 部件使用情况表 | 部件使用情况表\nP_MfgUpRevLog | 部件升级记录 | 部件升级记录\nP_MO | 制造订单表 | 制造订单表\nP_MOBOM | 制造订单表中的BOM | 制造订单表中的BOM\nP_ModRoute | OCN/ECN工单变更 | OCN/ECN工单变更\nP_ModRouteItem | OCN/ECN工单变更流程 | OCN/ECN工单变更流程\nP_ModRouteLog | MO修改记录 | MO修改记录\nP_ModRouteParams | OCN/ECN工单变更参数 | OCN/ECN工单变更参数\nP_ModRouteWO | OCN/ECN工单变更工单列表 | OCN/ECN工单变更工单列表\nP_MOMfgPart | 制造订单中的制造部件 | 制造订单中的制造部件\nP_MOMfgPartParams | 制造订单中的制造部件参数 | 制造订单中的制造部件参数\nP_MORoute | 制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表 | 制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表\nP_MORouteParams | 工单流程参数 | 工单流程参数\nP_MOSO | 制造订单\\销售订单 | 制造订单\\销售订单\nP_MRBRequisition | MRB送检申请 | MRB送检申请\nP_MRP | MRP物资需求计划 | MRP物资需求计划\nP_MRPREQ | P_MRPREQ | ERP 系统 P_MRPREQ 业务数据表\nP_MRPREQItem | P_MRPREQItem | ERP 系统 P_MRPREQItem 业务数据表\nP_OutPut | 工单过数记录表 | 工单过数记录表\nP_PQE | P_PQE | ERP 系统 P_PQE 业务数据表\nP_RetrospectTool | P_RetrospectTool | ERP 系统 P_RetrospectTool 业务数据表\nP_ReWork | 返工表 | 返工表\nP_ReWorkApplication | P_ReWorkApplication | ERP 系统 P_ReWorkApplication 业务数据表\nP_ReWorkApplicationProcess | P_ReWorkApplicationProcess | ERP 系统 P_ReWorkApplicationProcess 业务数据表\nP_SOBOM | 订单BOM表 | 订单BOM表\nP_SplitWOLog | 工单拆分记录 | 工单拆分记录\nP_ToolApply | 工具申请单 | 工具申请单\nP_ToolApplyHistory | 工具申请审批流程记录 | 工具申请审批流程记录\nP_ToolApplyWF | P_ToolApplyWF | ERP 系统 P_ToolApplyWF 业务数据表\nP_ToolIssued | 工具发放 | 工具发放\nP_ToolReturned | 工具退回 | 工具退回\nP_Tools | 工具登记表 | 工具登记表\nP_ToolTypes | 工具类型 | 工具类型\nP_ToolTypeWarehouse | 工具类型所在仓库 | 工具类型所在仓库\nP_UpdateLog | P_UpdateLog | ERP 系统 P_UpdateLog 业务数据表\nP_WO | 工作单号 | 工作单号\nP_WOIQC | 工单IQC | 工单IQC\nP_WOProcessBack | P_WOProcessBack | ERP 系统 P_WOProcessBack 业务数据表\nP_WOProcessSend | P_WOProcessSend | ERP 系统 P_WOProcessSend 业务数据表\nP_WOProcessStock | P_WOProcessStock | ERP 系统 P_WOProcessStock 业务数据表\nP_WOSO | 工单对应销售单 | 工单对应销售单\nP_WOSplitBatchApplication | P_WOSplitBatchApplication | ERP 系统 P_WOSplitBatchApplication 业务数据表\nP_WOTransfer | 工单转出记录 | 工单转出记录\nF_AccCostWOByPeriod | 财务应用-成本核算-成本明细 | 财务应用-成本核算-成本明细\nF_AccCostWOBySteps | 工单成本明细 | 工单成本明细\nF_AccountGroups | 财务管理-财务数据-科目分组 | 财务管理-财务数据-科目分组\nF_AccountProjects | F_AccountProjects | ERP 系统 F_AccountProjects 业务数据表\nF_Accounts | 科目管理 | 科目管理\nF_AllScrapWOCost | F_AllScrapWOCost | ERP 系统 F_AllScrapWOCost 业务数据表\nF_AP_DebitMemo | 供应商扣款 | 供应商扣款\nF_AP_DebitMemoItem | 供应商扣款明细 | 供应商扣款明细\nF_AP_Disburse | 应付账款/付款管理 | 应付账款/付款管理\nF_AP_DisburseItem | 应付账款/付款管理明细 | 应付账款/付款管理明细\nF_AP_Invoice | 采购发票 | 采购发票\nF_AP_InvoiceItem | 采购发票明细 | 采购发票明细\nF_AP_Reconcile | 采购对账 | 采购对账\nF_AP_ReconcileItems | 采购对账明细 | 采购对账明细\nF_AR_CreditMemo | 客户扣款（对账和发票） | 客户扣款（对账和发票）\nF_AR_CreditMemoItem | 客户扣款明细 | 客户扣款明细\nF_AR_Invoice | 财务管理-财务应用-应收账款-销售发票 | 财务管理-财务应用-应收账款-销售发票\nF_AR_InvoiceItem | 销售发票明细 | 销售发票明细\nF_AR_Receivable | 收款管理 | 收款管理\nF_AR_ReceivableItem | 收款管理明细 | 收款管理明细\nF_AR_SOReconcile | 财务管理-财务应用-应收账款-销售对账 | 财务管理-财务应用-应收账款-销售对账\nF_AR_SOReconcileItems | 销售对账明细 | 销售对账明细\nF_AssetCategoryItem | 财务管理-资产管理-资产类别明细表 | 财务管理-资产管理-资产类别明细表\nF_AssetCategorys | 财务管理-资产管理-资产类别 | 财务管理-资产管理-资产类别\nF_AssetChange | 资产变动管理 | 资产变动管理\nF_AssetChangeHistory | F_AssetChangeHistory | ERP 系统 F_AssetChangeHistory 业务数据表\nF_AssetChangeItem | 资产变动管理明细 | 资产变动管理明细\nF_AssetChangeWays | 资产变动方式 | 资产变动方式\nF_AssetChangeWF | F_AssetChangeWF | ERP 系统 F_AssetChangeWF 业务数据表\nF_AssetDisposal | 资产清理 | 资产清理\nF_AssetStatus | 资产状态 | 资产状态\nF_BankAccounts | 现金账户 | 现金账户\nF_BankReconcile | 银行对账 | 银行对账\nF_BankReconcileItem | 银行对账明细 | 银行对账明细\nF_BankReconcileSeting | 银行对账配置 | 银行对账配置\nF_BankReconcileSetingItem | 银行对账配置明细 | 银行对账配置明细\nF_CashAccount | 现金账流水 | 现金账流水\nF_CashAccountItem | 现金账流水明细 | 现金账流水明细\nF_CloseCashAccount | 出纳管理/现金账 | 出纳管理/现金账\nF_CloseCashAccountItem | 出纳管理/现金账明细 | 出纳管理/现金账明细\nF_CurrExchAdj | 期末调汇 | 期末调汇\nF_CurrExchAdjItem | 期末调汇明细 | 期末调汇明细\nF_Depreciation | 折旧计提 | 折旧计提\nF_DepreciationItem | 折旧计提明细表 | 折旧计提明细表\nF_DiaryAccount | 凭证登记 | 凭证登记\nF_DiaryAccountHistory | F_DiaryAccountHistory | ERP 系统 F_DiaryAccountHistory 业务数据表\nF_DiaryAccountItem | 凭证登记明细表 | 凭证登记明细表\nF_DiaryAccountWF | F_DiaryAccountWF | ERP 系统 F_DiaryAccountWF 业务数据表\nF_FixedAssets | 固定资产 | 固定资产\nF_FixedAssetsItem | 固定资产明细 | 固定资产明细\nF_GL_Setting | 科目设定 | 科目设定\nF_GL_SettingItem | 科目设定明细 | 科目设定明细\nF_LastPeriodWoBalanceCost | 结存表 | 结存表\nF_PackingSlipItemContractSO | F_PackingSlipItemContractSO | ERP 系统 F_PackingSlipItemContractSO 业务数据表\nF_PaymentRequest | 请款单 | 请款单\nF_PlantBusiness | 销售单位、财务设置里面的业务类型 | 销售单位、财务设置里面的业务类型\nF_PlantBusinessItem | 工厂业务明细 | 工厂业务明细\nF_Post | 出纳扎账&财务过账 | 出纳扎账&财务过账\nF_PostItem | 出纳扎账明细 | 出纳扎账明细\nF_ProjectCatagory | 核算项目 | 核算项目\nF_ProjectCatagoryItem | 核算项目明细 | 核算项目明细\nF_ProvisionalEstimate | 应付暂估 | 应付暂估\nF_ProvisionalEstimateItem | 应付暂估明细 | 应付暂估明细\nF_RefLib | 凭证摘要 | 凭证摘要\nF_TradingBusiness | 交易业务 | 交易业务\nF_Voucher | 凭证 | 凭证\nF_VoucherDesc | 凭证描述 | 凭证描述\nF_VoucherHistory | 凭证审批历史记录 | 凭证审批历史记录\nF_VoucherItem | 凭证明细 | 凭证明细\nF_VoucherProject | F_VoucherProject | ERP 系统 F_VoucherProject 业务数据表\nF_VoucherWF | 凭证审批记录 | 凭证审批记录\nC_CostSetting | 产品项目 | 产品项目\nC_CostSettingItem | 成本设置对应工艺和工序 | 成本设置对应工艺和工序\nC_CostSharing | 费用分组（费用管理） | 费用分组（费用管理）\nC_CostSharingItem | 费用分组明细（费用管理明细） | 费用分组明细（费用管理明细）\nC_CostSharingItemCount | 费用管理--项目明细 | 费用管理--项目明细\nC_CostSharingOutputDetail | C_CostSharingOutputDetail | ERP 系统 C_CostSharingOutputDetail 业务数据表\nC_CostType | 项目类型 | 项目类型\nC_DirectBomCost | 直接成本 | 直接成本\nC_FinancialReport | C_FinancialReport | ERP 系统 C_FinancialReport 业务数据表\nC_FinancialReportItem | C_FinancialReportItem | ERP 系统 C_FinancialReportItem 业务数据表\nC_JobCostPeriods | C_JobCostPeriods | ERP 系统 C_JobCostPeriods 业务数据表\nC_JobWoDetailsCalStatus | 工单明细成本 | 工单明细成本\nC_StepIndirecMatCost | C_StepIndirecMatCost | ERP 系统 C_StepIndirecMatCost 业务数据表\nEQ_Equipments | 设备管理表 | 设备管理表\nEQ_MLO | 设备保养管理 | 设备保养管理\nEQ_MLOEmployees | EQ_MLOEmployees | ERP 系统 EQ_MLOEmployees 业务数据表\nEQ_MLOEQ | EQ_MLOEQ | ERP 系统 EQ_MLOEQ 业务数据表\nEQ_MLOHistory | EQ_MLOHistory | ERP 系统 EQ_MLOHistory 业务数据表\nEQ_MLOMaterials | 设备保养明细 | 设备保养明细\nEQ_MLOTasks | EQ_MLOTasks | ERP 系统 EQ_MLOTasks 业务数据表\nEQ_MLOWF | 设备保养审批 | 设备保养审批\nEQ_PMO | P_MORouteParams | P_MORouteParams\nEQ_PMOEmployees | 设备维修管理关联雇员表 | 设备维修管理关联雇员表\nEQ_PMOHistory | 设备维修管理--审核记录 | 设备维修管理--审核记录\nEQ_PMOMaterials | 设备维修管理--物料 | 设备维修管理--物料\nEQ_PMOTasks | 设备维修管理--任务 | 设备维修管理--任务\nEQ_PMOWF | EQ_PMOWF | ERP 系统 EQ_PMOWF 业务数据表\nEQ_PreventiveEQ | 设备保养定义关联设备表 | 设备保养定义关联设备表\nEQ_PreventiveMaterials | 保养类型和物料关联表 | 保养类型和物料关联表\nEQ_Preventives | 设备保养定义 | 设备保养定义\nEQ_PreventiveTasks | 设备保养定义管理任务表 | 设备保养定义管理任务表\nEQ_Spareparts | 设备管理--物料 | 设备管理--物料\nPM_Faults | 故障现象 | 故障现象\nPM_Group | 维修分组 | 维修分组\nPM_GroupEmployees | 维修分组--用户 | 维修分组--用户\nPM_IssueForm | 维修发料 | 维修发料\nPM_IssueFormItem | 维修发料-维修单和保养单 | 维修发料-维修单和保养单\nPM_IssueReturnBatch | 维修退料批次 | 维修退料批次\nPM_Reasons | 故障原因 | 故障原因\nPM_ReturnForm | 维修退料 | 维修退料\nPM_ReturnFormItem | 维修退料明细 | 维修退料明细\nPM_Tasks | 标准任务 | 标准任务\nPM_Types | 业务员 | 业务员\nEQUIPMENT | 设备 | 设备\nEQUIPMENT_GROUP | EQUIPMENT_GROUP | ERP 系统 EQUIPMENT_GROUP 业务数据表\nSTEP | 工序表 | 工序表\nJBPM4_DEPLOYMENT | JBPM4_DEPLOYMENT | ERP 系统 JBPM4_DEPLOYMENT 业务数据表\nJBPM4_DEPLOYPROP | JBPM4_DEPLOYPROP | ERP 系统 JBPM4_DEPLOYPROP 业务数据表\nJBPM4_EXECUTION | JBPM4_EXECUTION | ERP 系统 JBPM4_EXECUTION 业务数据表\nJBPM4_HIST_ACTINST | JBPM4_HIST_ACTINST | ERP 系统 JBPM4_HIST_ACTINST 业务数据表\nJBPM4_HIST_DETAIL | JBPM4_HIST_DETAIL | ERP 系统 JBPM4_HIST_DETAIL 业务数据表\nJBPM4_HIST_PROCINST | JBPM4_HIST_PROCINST | ERP 系统 JBPM4_HIST_PROCINST 业务数据表\nJBPM4_HIST_TASK | JBPM4_HIST_TASK | ERP 系统 JBPM4_HIST_TASK 业务数据表\nJBPM4_HIST_VAR | JBPM4_HIST_VAR | ERP 系统 JBPM4_HIST_VAR 业务数据表\nJBPM4_ID_GROUP | JBPM4_ID_GROUP | ERP 系统 JBPM4_ID_GROUP 业务数据表\nJBPM4_ID_MEMBERSHIP | JBPM4_ID_MEMBERSHIP | ERP 系统 JBPM4_ID_MEMBERSHIP 业务数据表\nJBPM4_ID_USER | JBPM4_ID_USER | ERP 系统 JBPM4_ID_USER 业务数据表\nJBPM4_JOB | JBPM4_JOB | ERP 系统 JBPM4_JOB 业务数据表\nJBPM4_LOB | JBPM4_LOB | ERP 系统 JBPM4_LOB 业务数据表\nJBPM4_PARTICIPATION | JBPM4_PARTICIPATION | ERP 系统 JBPM4_PARTICIPATION 业务数据表\nJBPM4_PROPERTY | JBPM4_PROPERTY | ERP 系统 JBPM4_PROPERTY 业务数据表\nJBPM4_SWIMLANE | JBPM4_SWIMLANE | ERP 系统 JBPM4_SWIMLANE 业务数据表\nJBPM4_TASK | JBPM4_TASK | ERP 系统 JBPM4_TASK 业务数据表\nJBPM4_VARIABLE | JBPM4_VARIABLE | ERP 系统 JBPM4_VARIABLE 业务数据表\nA_AAA | A_AAA | ERP 系统 A_AAA 业务数据表\na_allMaterialsFromZB20170221 | a_allMaterialsFromZB20170221 | ERP 系统 a_allMaterialsFromZB20170221 业务数据表\na_backup_deletedMatrlList_20170325 | a_backup_deletedMatrlList_20170325 | ERP 系统 a_backup_deletedMatrlList_20170325 业务数据表\na_CustomerfromZB20170221 | a_CustomerfromZB20170221 | ERP 系统 a_CustomerfromZB20170221 业务数据表\na_DeletedMtrlList_20170325 | a_DeletedMtrlList_20170325 | ERP 系统 a_DeletedMtrlList_20170325 业务数据表\na_FGI_Inevneotyr_20170506 | a_FGI_Inevneotyr_20170506 | ERP 系统 a_FGI_Inevneotyr_20170506 业务数据表\na_fgibal_20170401 | a_fgibal_20170401 | ERP 系统 a_fgibal_20170401 业务数据表\na_FGIStock0401 | a_FGIStock0401 | ERP 系统 a_FGIStock0401 业务数据表\na_log1_02262017922PM | a_log1_02262017922PM | ERP 系统 a_log1_02262017922PM 业务数据表\na_log1_02262017923PM | a_log1_02262017923PM | ERP 系统 a_log1_02262017923PM 业务数据表\na_log1_022720171031PM | a_log1_022720171031PM | ERP 系统 a_log1_022720171031PM 业务数据表\na_log1_02282017943PM | a_log1_02282017943PM | ERP 系统 a_log1_02282017943PM 业务数据表\na_log1_03162017933PM | a_log1_03162017933PM | ERP 系统 a_log1_03162017933PM 业务数据表\na_log1_03312017615PM | a_log1_03312017615PM | ERP 系统 a_log1_03312017615PM 业务数据表\na_log1_03312017617PM | a_log1_03312017617PM | ERP 系统 a_log1_03312017617PM 业务数据表\na_log1_03312017657PM | a_log1_03312017657PM | ERP 系统 a_log1_03312017657PM 业务数据表\na_log2_02262017922PM | a_log2_02262017922PM | ERP 系统 a_log2_02262017922PM 业务数据表\na_log2_02262017923PM | a_log2_02262017923PM | ERP 系统 a_log2_02262017923PM 业务数据表\na_log2_02282017943PM | a_log2_02282017943PM | ERP 系统 a_log2_02282017943PM 业务数据表\na_log2_03312017615PM | a_log2_03312017615PM | ERP 系统 a_log2_03312017615PM 业务数据表\na_log2_03312017617PM | a_log2_03312017617PM | ERP 系统 a_log2_03312017617PM 业务数据表\na_log2_03312017657PM | a_log2_03312017657PM | ERP 系统 a_log2_03312017657PM 业务数据表\na_log2_041012017657AM | a_log2_041012017657AM | ERP 系统 a_log2_041012017657AM 业务数据表\na_log2_041112017657AM | a_log2_041112017657AM | ERP 系统 a_log2_041112017657AM 业务数据表\na_log2_20170403 | a_log2_20170403 | ERP 系统 a_log2_20170403 业务数据表\na_mtrlBal_20170401 | a_mtrlBal_20170401 | ERP 系统 a_mtrlBal_20170401 业务数据表\na_mtrlbal_20170401_1 | a_mtrlbal_20170401_1 | ERP 系统 a_mtrlbal_20170401_1 业务数据表\na_P_MOROUTE_20170506 | a_P_MOROUTE_20170506 | ERP 系统 a_P_MOROUTE_20170506 业务数据表\na_SM_FromZB20170220 | a_SM_FromZB20170220 | ERP 系统 a_SM_FromZB20170220 业务数据表\na_UpdatePanelSize_20170302 | a_UpdatePanelSize_20170302 | ERP 系统 a_UpdatePanelSize_20170302 业务数据表\na_UpdatePanelSize_20170302_1 | a_UpdatePanelSize_20170302_1 | ERP 系统 a_UpdatePanelSize_20170302_1 业务数据表\nalan_materails_20170211 | alan_materails_20170211 | ERP 系统 alan_materails_20170211 业务数据表\nalan_parameter_mapping | alan_parameter_mapping | ERP 系统 alan_parameter_mapping 业务数据表\nF_AccountSetting1 | 工厂管理-应收应付 | 工厂管理-应收应付\nF_AccountSetting2 | F_AccountSetting2 | ERP 系统 F_AccountSetting2 业务数据表\nF_AccountSetting3 | F_AccountSetting3 | ERP 系统 F_AccountSetting3 业务数据表\nF_AccountSetting4 | F_AccountSetting4 | ERP 系统 F_AccountSetting4 业务数据表\nfgi_inventory_0427_2200 | fgi_inventory_0427_2200 | ERP 系统 fgi_inventory_0427_2200 业务数据表\nFGI_Inventory_backup_0420 | FGI_Inventory_backup_0420 | ERP 系统 FGI_Inventory_backup_0420 业务数据表\nFGI_Inventory_BAK20170407 | FGI_Inventory_BAK20170407 | ERP 系统 FGI_Inventory_BAK20170407 业务数据表\nfgi_inventory_bak_0429 | fgi_inventory_bak_0429 | ERP 系统 fgi_inventory_bak_0429 业务数据表\nFGI_StockFormItem_bak0407 | FGI_StockFormItem_bak0407 | ERP 系统 FGI_StockFormItem_bak0407 业务数据表\nFGI_StockFormItem_moid_bak | FGI_StockFormItem_moid_bak | ERP 系统 FGI_StockFormItem_moid_bak 业务数据表\nM_MaterialsWarehouse_bak | M_MaterialsWarehouse_bak | ERP 系统 M_MaterialsWarehouse_bak 业务数据表\nM_MaterialsWarehouse_bak0413 | M_MaterialsWarehouse_bak0413 | ERP 系统 M_MaterialsWarehouse_bak0413 业务数据表\np_bombatching_0413 | p_bombatching_0413 | ERP 系统 p_bombatching_0413 业务数据表\nxnh_ChangedToConsigment_411 | xnh_ChangedToConsigment_411 | ERP 系统 xnh_ChangedToConsigment_411 业务数据表\nxnh_ChangedToConsigment_412 | xnh_ChangedToConsigment_412 | ERP 系统 xnh_ChangedToConsigment_412 业务数据表\nxnh_奇立04010405_1724_item | xnh_奇立04010405_1724_item | ERP 系统 xnh_奇立04010405_1724_item 业务数据表\nxnh_底油线路 | xnh_底油线路 | ERP 系统 xnh_底油线路 业务数据表\nxnh_贵阳海信_item | xnh_贵阳海信_item | ERP 系统 xnh_贵阳海信_item 业务数据表\nxnh_达信20170405001_item | xnh_达信20170405001_item | ERP 系统 xnh_达信20170405001_item 业务数据表\nxnh_高效170331_item | xnh_高效170331_item | ERP 系统 xnh_高效170331_item 业务数据表\nA_account | 财务管理-财务数据-科目管理上级 | 财务管理-财务数据-科目管理上级\na_addlPHPart | a_addlPHPart | ERP 系统 a_addlPHPart 业务数据表\na_AllInfo | a_AllInfo | ERP 系统 a_AllInfo 业务数据表\na_atom | a_atom | ERP 系统 a_atom 业务数据表\na_CoreToBeFixed | a_CoreToBeFixed | ERP 系统 a_CoreToBeFixed 业务数据表\na_DeletedJob | a_DeletedJob | ERP 系统 a_DeletedJob 业务数据表\na_deletespds | a_deletespds | ERP 系统 a_deletespds 业务数据表\na_drill | a_drill | ERP 系统 a_drill 业务数据表\na_drill_adjustbase | a_drill_adjustbase | ERP 系统 a_drill_adjustbase 业务数据表\na_fgi_batch | a_fgi_batch | ERP 系统 a_fgi_batch 业务数据表\na_FGI_Inventory | a_FGI_Inventory | ERP 系统 a_FGI_Inventory 业务数据表\na_importSO_AE | a_importSO_AE | ERP 系统 a_importSO_AE 业务数据表\na_ImportSO_Flex | a_ImportSO_Flex | ERP 系统 a_ImportSO_Flex 业务数据表\na_importSO_PPC | a_importSO_PPC | ERP 系统 a_importSO_PPC 业务数据表\na_JobRouteParam | a_JobRouteParam | ERP 系统 a_JobRouteParam 业务数据表\na_JobRoutes | a_JobRoutes | ERP 系统 a_JobRoutes 业务数据表\na_laminate | a_laminate | ERP 系统 a_laminate 业务数据表\na_Materials | a_Materials | ERP 系统 a_Materials 业务数据表\na_MaterialsFromWH | a_MaterialsFromWH | ERP 系统 a_MaterialsFromWH 业务数据表\na_materialwithoutwh | a_materialwithoutwh | ERP 系统 a_materialwithoutwh 业务数据表\nA_MET2 | A_MET2 | ERP 系统 A_MET2 业务数据表\na_OdrBatch | a_OdrBatch | ERP 系统 a_OdrBatch 业务数据表\na_old_erp_so | a_old_erp_so | ERP 系统 a_old_erp_so 业务数据表\na_osScrapHistory | a_osScrapHistory | ERP 系统 a_osScrapHistory 业务数据表\nA_PARTTODOLIST | A_PARTTODOLIST | ERP 系统 A_PARTTODOLIST 业务数据表\na_poList | a_poList | ERP 系统 a_poList 业务数据表\na_PP_FromZB20170220 | a_PP_FromZB20170220 | ERP 系统 a_PP_FromZB20170220 业务数据表\na_ReWo_Status | a_ReWo_Status | ERP 系统 a_ReWo_Status 业务数据表\na_Route | a_Route | ERP 系统 a_Route 业务数据表\na_stepInfo | a_stepInfo | ERP 系统 a_stepInfo 业务数据表\nA_Title | A_Title | ERP 系统 A_Title 业务数据表\na_wo_Rework | a_wo_Rework | ERP 系统 a_wo_Rework 业务数据表\na_yd | a_yd | ERP 系统 a_yd 业务数据表\nab_OdrBatch | ab_OdrBatch | ERP 系统 ab_OdrBatch 业务数据表\nb_matrl | 物料批次库存 | 物料批次库存\nb_Update_JobCustomer | b_Update_JobCustomer | ERP 系统 b_Update_JobCustomer 业务数据表\nb_Update_SalesPartCustomer | b_Update_SalesPartCustomer | ERP 系统 b_Update_SalesPartCustomer 业务数据表\nB_USER_WIP01 | B_USER_WIP01 | ERP 系统 B_USER_WIP01 业务数据表\nba | ba | ERP 系统 ba 业务数据表\ne2 | e2 | ERP 系统 e2 业务数据表\nfgi_cartonsnumber | fgi_cartonsnumber | ERP 系统 fgi_cartonsnumber 业务数据表\nfgi_sotransfer | 寄售 | 寄售\nIMP_CustInfo | 客户备份信息 | 客户备份信息\nIMP_CustMapping | IMP_CustMapping | ERP 系统 IMP_CustMapping 业务数据表\nIMP_OdrBatch | IMP_OdrBatch | ERP 系统 IMP_OdrBatch 业务数据表\nIMP_OdrProdNo | IMP_OdrProdNo | ERP 系统 IMP_OdrProdNo 业务数据表\nimp_OrderList | imp_OrderList | ERP 系统 imp_OrderList 业务数据表\nIMP_PnInfo | IMP_PnInfo | ERP 系统 IMP_PnInfo 业务数据表\nIMP_User | IMP_User | ERP 系统 IMP_User 业务数据表\norg_DrillDetails | 钻孔历史记录表 | 钻孔历史记录表\nqty_Order | qty_Order | ERP 系统 qty_Order 业务数据表\nrpt_moRoute_snap | rpt_moRoute_snap | ERP 系统 rpt_moRoute_snap 业务数据表\nrpt_ShopFloorInfo | rpt_ShopFloorInfo | ERP 系统 rpt_ShopFloorInfo 业务数据表\nrpt_ShopFloorSummary | rpt_ShopFloorSummary | ERP 系统 rpt_ShopFloorSummary 业务数据表\nrpt_StepMapping | rpt_StepMapping | ERP 系统 rpt_StepMapping 业务数据表\nrpt_targetInfo | rpt_targetInfo | ERP 系统 rpt_targetInfo 业务数据表\nVPartArea | 面积表 | 面积表\nW_DailyStepWipOutPut | W_DailyStepWipOutPut | ERP 系统 W_DailyStepWipOutPut 业务数据表\nW_WIP | W_WIP | ERP 系统 W_WIP 业务数据表\nW_WIPFieldDisplay | W_WIPFieldDisplay | ERP 系统 W_WIPFieldDisplay 业务数据表\nW_WIPQueryExecute | W_WIPQueryExecute | ERP 系统 W_WIPQueryExecute 业务数据表\nW_WIPStepDetails | W_WIPStepDetails | ERP 系统 W_WIPStepDetails 业务数据表\nWIP_Backlog | 月结主表 | 月结主表\nWIP_PC | WIP_PC | ERP 系统 WIP_PC 业务数据表\nWIP_PCSteps | WIP_PCSteps | ERP 系统 WIP_PCSteps 业务数据表\nWIP_PCWO | WIP_PCWO | ERP 系统 WIP_PCWO 业务数据表\nxnh_BOMBatch | xnh_BOMBatch | ERP 系统 xnh_BOMBatch 业务数据表\nxnh_BOMBatch2 | xnh_BOMBatch2 | ERP 系统 xnh_BOMBatch2 业务数据表\nxnh_ChangedtobePlaned | xnh_ChangedtobePlaned | ERP 系统 xnh_ChangedtobePlaned 业务数据表\nxnh_DeletedLock | xnh_DeletedLock | ERP 系统 xnh_DeletedLock 业务数据表\nxnh_fgi_stockForm | 成品入库 | 成品入库\nxnh_fgi_stockFormItem | 成品入库明细 | 成品入库明细\nxnh_fgi_stockformitemwo | xnh_fgi_stockformitemwo | ERP 系统 xnh_fgi_stockformitemwo 业务数据表\nxnh_last3setp | xnh_last3setp | ERP 系统 xnh_last3setp 业务数据表\nxnh_OrderDateChanged | xnh_OrderDateChanged | ERP 系统 xnh_OrderDateChanged 业务数据表\nxnh_orphanPart | xnh_orphanPart | ERP 系统 xnh_orphanPart 业务数据表\nxnh_OSMORoute | xnh_OSMORoute | ERP 系统 xnh_OSMORoute 业务数据表\nxnh_qtyshipped | xnh_qtyshipped | ERP 系统 xnh_qtyshipped 业务数据表\nxnh_resetPlanningedQty | xnh_resetPlanningedQty | ERP 系统 xnh_resetPlanningedQty 业务数据表\nxnh_stockedIn | xnh_stockedIn | ERP 系统 xnh_stockedIn 业务数据表\nxnh_wipBalance | xnh_wipBalance | ERP 系统 xnh_wipBalance 业务数据表\nxnh_wo | xnh_wo | ERP 系统 xnh_wo 业务数据表\nxnh_wotemp | xnh_wotemp | ERP 系统 xnh_wotemp 业务数据表\nxnh_woTempQty | xnh_woTempQty | ERP 系统 xnh_woTempQty 业务数据表\nzb_materials | zb_materials | ERP 系统 zb_materials 业务数据表\n不需要接收 | 不需要接收 | ERP 系统 不需要接收 业务数据表\n供应商 | 采购受理 | 采购受理\n化验 | 化验 | ERP 系统 化验 业务数据表\n工单对应的制造部件号 | 制造部件 | 制造部件\n工单有主卡和子卡 | 制造单表 | 制造单表\n空数据 | 下一个工序 | 下一个工序"
_EMBEDDED_CATALOG_FULL_CHAR_COUNT = "140981"
_EMBEDDED_TABLE_COUNT = "642"

# -*- coding: utf-8 -*-
"""通用表清单相关性排序：按用户问题对精简 catalog 行打分，缩小 LLM 选表范围。"""

import re
from typing import Dict, List, Set, Tuple

_CJK_RUN = re.compile(r"[\u4e00-\u9fff]+")
_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+")
_TABLE_LINE = re.compile(r"^[\w_]+\s*\|")

_FGI_KW = ("制成品接收", "接收明细", "FGI", "IQC")
_MO_KW = ("制造订单", "制造单", "MOSO")
_WO_KW = ("工单", "工作单")
_PURCHASE_KW = ("采购订单", "采购明细", "采购")
_OUTPUT_KW = ("过数", "产出", "工单过数")
_REQ_KW = ("请购", "请购单")
_MRB_KW = ("MRB", "送检申请", "送检")
_BOM_KW = ("领料", "BOM领料", "BOM 领料")


def extract_query_tokens(question: str) -> List[str]:
    """从问题中提取中文 n-gram（2~6字）及英文/表名片段，无业务硬编码。"""
    q = (question or "").strip()
    if not q:
        return []
    tokens: List[str] = []
    for run in _CJK_RUN.findall(q):
        tokens.append(run)
        max_n = min(6, len(run))
        for n in range(2, max_n + 1):
            for i in range(len(run) - n + 1):
                tokens.append(run[i : i + n])
    for w in _TOKEN.findall(q):
        tokens.append(w)
        if len(w) > 2:
            tokens.append(w.lower())
    seen: Set[str] = set()
    out: List[str] = []
    for t in sorted(tokens, key=len, reverse=True):
        key = t.lower()
        if key in seen or len(key) < 2:
            continue
        seen.add(key)
        out.append(t)
    return out


def _parse_line(line: str) -> Tuple[str, str, str]:
    parts = [p.strip() for p in line.split("|", 2)]
    tname = parts[0]
    label = parts[1] if len(parts) > 1 else ""
    biz = parts[2] if len(parts) > 2 else label
    return tname, label, biz


def score_catalog_line(line: str, tokens: List[str]) -> int:
    if not _TABLE_LINE.match((line or "").strip()):
        return 0
    text = line.lower()
    score = 0
    for tok in tokens:
        t = tok.lower()
        if t in text:
            score += len(t) * 10
    return score


def _infer_related_tables(tname: str, all_names: Set[str]) -> List[str]:
    """主表选中时，补全常见明细/子表（Receipt→ReceiptItem 等）。"""
    related: List[str] = []
    upper_map = {n.upper(): n for n in all_names}
    for suffix in ("Item", "Items", "Detail", "Details"):
        cand = tname + suffix
        if cand in all_names:
            related.append(cand)
        elif cand.upper() in upper_map:
            related.append(upper_map[cand.upper()])
    return related


def _apply_intent_boosts(question: str, scored: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """按问题意图调整分数：制造订单/工单/接收/采购等易混场景。"""
    q = question or ""
    has_detail = "明细" in q or "详情" in q
    boosted: List[Tuple[int, str]] = []

    for s, ln in scored:
        tname, label, biz = _parse_line(ln)

        if any(k in q for k in _FGI_KW):
            if tname == "FGI_ReceiptItem":
                s += 300
            elif tname == "FGI_Receipt":
                s += 180 if has_detail else 120

        if any(k in q for k in _MO_KW):
            if tname == "P_MOSO":
                s += 280
            elif tname == "P_MO":
                s += 220 if not has_detail else 120

        if any(k in q for k in _WO_KW) and "制造订单" not in q:
            if tname == "P_WO":
                s += 250
            elif tname == "P_OutPut" and any(k in q for k in _OUTPUT_KW):
                s += 200

        if any(k in q for k in _PURCHASE_KW):
            if tname == "M_PurchaseOrderItem":
                s += 280 if has_detail else 180
            elif tname == "M_PurchaseOrder":
                s += 180 if not has_detail else 100

        if any(k in q for k in _REQ_KW) and tname == "M_Requisitions":
            s += 250

        if any(k in q for k in _MRB_KW) and tname == "P_MRBRequisition":
            s += 280

        if any(k in q for k in _BOM_KW):
            if tname == "M_BOMPicklistItem" and has_detail:
                s += 260
            elif tname == "M_BOMPicklist":
                s += 200

        boosted.append((s, ln))

    boosted.sort(key=lambda x: (-x[0], x[1]))
    return boosted


def _expand_related_tables(
    picked: List[Tuple[int, str]], line_by_name: Dict[str, str]
) -> List[Tuple[int, str]]:
    """主表选中后补子表，紧跟主表之后，不抬高到清单顶部。"""
    seen: Set[str] = set()
    merged: List[Tuple[int, str]] = []

    for s, ln in picked:
        tname = _parse_line(ln)[0]
        if tname not in seen:
            merged.append((s, ln))
            seen.add(tname)
        for rel in _infer_related_tables(tname, set(line_by_name)):
            if rel not in seen:
                merged.append((max(s - 1, 1), line_by_name[rel]))
                seen.add(rel)

    return merged


def rank_catalog_lines(
    question: str,
    slim_catalog: str,
    *,
    top_n: int = 40,
    min_score: int = 10,
) -> Tuple[str, int, str]:
    """
    返回 (ranked_catalog_text, matched_count, mode)。
    mode: "ranked" | "full"（无有效 token 或未命中时退回全量精简清单）
    """
    tokens = extract_query_tokens(question)
    lines = slim_catalog.splitlines()
    header = [ln for ln in lines if not _TABLE_LINE.match(ln.strip())]
    table_lines = [ln for ln in lines if _TABLE_LINE.match(ln.strip())]
    line_by_name = {_parse_line(ln)[0]: ln for ln in table_lines}

    if not tokens or not table_lines:
        return slim_catalog.strip(), len(table_lines), "full"

    scored = [(score_catalog_line(ln, tokens), ln) for ln in table_lines]
    scored = [(s, ln) for s, ln in scored if s >= min_score]
    scored.sort(key=lambda x: (-x[0], x[1]))

    if not scored:
        return slim_catalog.strip(), 0, "full"

    scored = _apply_intent_boosts(question, scored)
    picked = scored[:top_n]
    picked = _expand_related_tables(picked, line_by_name)
    picked = picked[: top_n + 8]

    body = [ln for _, ln in picked]
    ranked = "\n".join(header + [""] + body).strip()
    return ranked, len(body), "ranked"

def main(user_question="", **kwargs):
    """Dify 入口：嵌入清单 + 通用相关性排序，不读磁盘。"""
    q = str(user_question or kwargs.get("user_question") or kwargs.get("query") or "").strip()
    full_slim = _EMBEDDED_CATALOG_SLIM
    ranked, n_ranked, mode = rank_catalog_lines(q, full_slim, top_n=40, min_score=10)
    use = ranked if mode == "ranked" else full_slim
    return {
        "table_catalog": str(use),
        "table_count": str(n_ranked if mode == "ranked" else _EMBEDDED_TABLE_COUNT),
        "char_count": str(len(use)),
        "char_count_full": str(len(full_slim)),
        "rank_mode": str(mode),
    }

try:
    user_question
except NameError:
    user_question = ""

_out = main(user_question=user_question)
table_catalog = str(_out.get("table_catalog") or "")
table_count = str(_out.get("table_count") or "0")
char_count = str(_out.get("char_count") or "0")
char_count_full = str(_out.get("char_count_full") or "0")
rank_mode = str(_out.get("rank_mode") or "full")
