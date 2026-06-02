# 数据库结构参考说明文档（关联关系版）


## 二、核心数据表结构及关联关系

### 2.1 基础模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 1 系统设定 (T_AppSeting)

- **业务含义**：系统设定
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 2 区域 (T_Area)

- **业务含义**：区域
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Area.areaId = T_Area.recId
- T_Area.cityId = T_Area.recId
- T_Area.continentId = T_Area.recId
- T_Area.countryId = T_Area.recId
- T_Area.parentId = T_Area.recId
- T_Area.provinceId = T_Area.recId

---

#### 3 系统日志 (T_AtomLog)

- **业务含义**：系统日志
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 4 业务表 (T_Business)

- **业务含义**：业务表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 5 流程设计--流程分类 (T_BusinessItem)

- **业务含义**：流程设计--流程分类
- **所属数据库**：思方云2 ERP
-关联关系：
- T_BusinessItem.businessId = T_Business.recId

---

#### 6 等级管理表 (T_Cate)

- **业务含义**：等级管理表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 7 物料类别表（物料分组 (T_Category)

- **业务含义**：物料类别表（物料分组
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Category.companyId = T_Company.recId
- T_Category.inspectGroupId = T_InspectGroup.recId
- T_Category.inspectPostId = T_PostRole.recId
- T_Category.parentId = T_Category.recId
- T_Category.postRoleId = T_PostRole.recId
- T_Category.receiptPostId = T_PostRole.recId

---

#### 8 物料类别明细表（储区） (T_CategoryItem)

- **业务含义**：物料类别明细表（储区）
- **所属数据库**：思方云2 ERP
-关联关系：
- T_CategoryItem.categoryId = T_Category.recId
- T_CategoryItem.companyId = T_Company.recId

---

#### 9 附加费用 (T_ChargeItem)

- **业务含义**：附加费用
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ChargeItem.saleProjectId = S_SaleProject.recId

---

#### 10 公司管理 (T_Company)

- **业务含义**：公司管理
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Company.currencyId = T_Currency.recId
- T_Company.plantBusinessId = F_PlantBusiness.recId

---

#### 11 币种 (T_Currency)

- **业务含义**：币种
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 12 币种兑换明细 (T_CurrencyItem)

- **业务含义**：币种兑换明细
- **所属数据库**：思方云2 ERP
-关联关系：
- T_CurrencyItem.baseCurrId = T_Currency.recId
- T_CurrencyItem.currencyId = T_Currency.recId

---

#### 13 自定义脚本 (T_CustomScript)

- **业务含义**：自定义脚本
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 14 自定义表 (T_CustTable)

- **业务含义**：自定义表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 15 自定义表明细 (T_CustTableValue)

- **业务含义**：自定义表明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 16 缺陷表 (T_Defect)

- **业务含义**：缺陷表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 17 部门表 (T_Department)

- **业务含义**：部门表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Department.companyId = T_Company.recId
- T_Department.parentId = T_Department.recId

---

#### 18 部门--用户表 (T_DepartmentUser)

- **业务含义**：部门--用户表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_DepartmentUser.departmentId = T_Department.recId
- T_DepartmentUser.userId = T_User.recId

---

#### 19 文件上传记录 (T_Document)

- **业务含义**：文件上传记录
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 20 导出设置 (T_ExportSetting)

- **业务含义**：导出设置
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 21 导出设置明细 (T_ExportSettingItem)

- **业务含义**：导出设置明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 22 导出设置URL (T_ExportSettingUrl)

- **业务含义**：导出设置URL
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 23 会计期间 (T_FiscalPeriod)

- **业务含义**：会计期间
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 24 流程设计主表 (T_Flow)

- **业务含义**：流程设计主表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Flow.flowTypeId = T_FlowType.recId

---

#### 25 流程设计 (T_FlowType)

- **业务含义**：流程设计
- **所属数据库**：思方云2 ERP
-关联关系：
- T_FlowType.businessId = T_Business.recId
- T_FlowType.companyId = T_Company.recId
- T_FlowType.parentId = T_FlowType.recId
- T_FlowType.userId = T_User.recId

---

#### 26 贸易方式 (T_FOB)

- **业务含义**：贸易方式
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 27 系统模块功能表 (T_FunctionRight)

- **业务含义**：系统模块功能表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_FunctionRight.moduleId = T_Module.recId

---

#### 28 用户组管理 (T_Group)

- **业务含义**：用户组管理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 29 用户组--用户 (T_GroupUser)

- **业务含义**：用户组--用户
- **所属数据库**：思方云2 ERP
-关联关系：
- T_GroupUser.groupId = T_Group.recId
- T_GroupUser.userId = T_User.recId

---

#### 30 检验分组--检验项目 (T_Inspect)

- **业务含义**：检验分组--检验项目
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Inspect.inspectGroupId = T_InspectGroup.recId
- T_Inspect.inspectItemsId = T_InspectItems.recId

---

#### 31 检验分组 (T_InspectGroup)

- **业务含义**：检验分组
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 32 检验项目 (T_InspectItems)

- **业务含义**：检验项目
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 33 盘点原因 (T_InventoryCheckReason)

- **业务含义**：盘点原因
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 34 JSON接口日志 (T_JSONHistory)

- **业务含义**：JSON接口日志
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 35 联系人 (T_Linkman)

- **业务含义**：联系人
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Linkman.typeId = M_Suppliers.recId

---

#### 36 储区表 (T_Location)

- **业务含义**：储区表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Location.companyId = T_Company.recId
- T_Location.parentId = T_Location.recId
- T_Location.stepsId = T_Steps.recId
- T_Location.warehouseId = T_Warehouse.recId

---

#### 37 模块表 (T_Module)

- **业务含义**：模块表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Module.parentId = T_Module.recId

---

#### 38 模组类型 (T_ModuleType)

- **业务含义**：模组类型
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 39 用户模块权限表 (T_MyModule)

- **业务含义**：用户模块权限表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_MyModule.userId = T_User.recId

---

#### 40 记事本 (T_Notepad)

- **业务含义**：记事本
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Notepad.notepadGroupId = T_NotepadGroup.recId

---

#### 41 记事分组表 (T_NotepadGroup)

- **业务含义**：记事分组表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_NotepadGroup.companyId = T_Company.recId

---

#### 42 单据号码表 (T_NumberControl)

- **业务含义**：单据号码表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_NumberControl.companyId = T_Company.recId

---

#### 43 付款方式 (T_PaymentMethod)

- **业务含义**：付款方式
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 44 付款周期 (T_PaymentTerm)

- **业务含义**：付款周期
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 45 工厂 (T_Plants)

- **业务含义**：工厂
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Plants.shippingWarehouseId = T_Warehouse.recId
- T_Plants.stockingWarehouseId = T_Warehouse.recId
- T_Plants.wipWarehouseId = T_Warehouse.recId
- T_Plants.AP_CASH_DISCOUNT_ACCID = F_Accounts.recId
- T_Plants.AP_Exhange_Gain_ACCID = F_Accounts.recId
- T_Plants.AP_Exhange_Loss_ACCID = F_Accounts.recId
- T_Plants.AP_Misc_ACCID = F_Accounts.recId
- T_Plants.AP_Tax_IN_ACCID = F_Accounts.recId
- T_Plants.AR_CASH_DISCOUNT_ACCID = F_Accounts.recId
- T_Plants.AR_CostSold_ACCID = F_Accounts.recId
- T_Plants.AR_Exhange_Gain_ACCID = F_Accounts.recId
- T_Plants.AR_Exhange_Loss_ACCID = F_Accounts.recId
- T_Plants.AR_Misc_ACCID = F_Accounts.recId
- T_Plants.AR_Others_Revenue_AccID = F_Accounts.recId
- T_Plants.AR_Product_Revenue_AccID = F_Accounts.recId
- T_Plants.AR_Tax_OUT_ACCID = F_Accounts.recId
- T_Plants.bankAccountId = F_Accounts.recId
- T_Plants.companyId = T_Company.recId
- T_Plants.currentProfitId = F_Accounts.recId
- T_Plants.FG_Inventory_ACCID = F_Accounts.recId
- T_Plants.FG_PC_ACCID = F_Accounts.recId
- T_Plants.FG_Reject_ACCID = F_Accounts.recId
- T_Plants.incomeTaxId = F_Accounts.recId
- T_Plants.investmentIncomeId = F_Accounts.recId
- T_Plants.OutSource_ACCID = F_Accounts.recId
- T_Plants.profitAllotId = F_Accounts.recId
- T_Plants.RM_DM_ISSUE_ACCID = F_Accounts.recId
- T_Plants.RM_IDM_ISSUE_ACCID = F_Accounts.recId
- T_Plants.RM_INVENTORY_ACCID = F_Accounts.recId
- T_Plants.RM_PC_ACCID = F_Accounts.recId
- T_Plants.RM_PM_ISSUE_ACCID = F_Accounts.recId
- T_Plants.RM_REJECT_ACCID = F_Accounts.recId

---

#### 46 岗位 (T_PostRole)

- **业务含义**：岗位
- **所属数据库**：思方云2 ERP
-关联关系：
- T_PostRole.companyId = T_Company.recId

---

#### 47 岗位模块 (T_PostRoleModule)

- **业务含义**：岗位模块
- **所属数据库**：思方云2 ERP
-关联关系：
- T_PostRoleModule.moduleId = T_Cate.recId
- T_PostRoleModule.postRoleId = T_PostRole.recId

---

#### 48 工艺表 (T_Process)

- **业务含义**：工艺表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 49 工艺缺陷报废 (T_ProcessDefect)

- **业务含义**：工艺缺陷报废
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ProcessDefect.defectId = T_Defect.recId
- T_ProcessDefect.processId = T_Process.recId

---

#### 50 工艺--雇员权限(工程设计流程权限) (T_ProcessEmployee)

- **业务含义**：工艺--雇员权限(工程设计流程权限)
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 51 工艺流程参数表 (T_ProcessParameter)

- **业务含义**：工艺流程参数表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ProcessParameter.parametersId = S_Parameters.recId
- T_ProcessParameter.processId = T_Process.recId

---

#### 52 工艺管理--工厂 (T_ProcessPlant)

- **业务含义**：工艺管理--工厂
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ProcessPlant.plantsId = T_Plants.recId
- T_ProcessPlant.processId = T_Process.recId

---

#### 53 销售数据--产品分类--工厂 (T_ProductCategoryPlant)

- **业务含义**：销售数据--产品分类--工厂
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ProductCategoryPlant.plantsId = T_Plants.recId
- T_ProductCategoryPlant.productCategoryId = S_ProductCategory.recId

---

#### 54 货架表 (T_Racks)

- **业务含义**：货架表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Racks.locationId = T_Location.recId

---

#### 55 表单设定 (T_ReportSeting)

- **业务含义**：表单设定
- **所属数据库**：思方云2 ERP
-关联关系：
- T_ReportSeting.companyId = T_Company.recId
- T_ReportSeting.customerId = S_Customer.recId
- T_ReportSeting.fgiPackingListId = T_FunctionRight.recId
- T_ReportSeting.fgiSOInvoiceId = T_FunctionRight.recId
- T_ReportSeting.matPackingListId = T_FunctionRight.recId
- T_ReportSeting.matSOInvoiceId = T_FunctionRight.recId
- T_ReportSeting.supplierId = M_Suppliers.recId

---

#### 56 运输方式 (T_Shipping)

- **业务含义**：运输方式
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 57 工序--雇员权限(过数权限) (T_StepEmployee)

- **业务含义**：工序--雇员权限(过数权限)
- **所属数据库**：思方云2 ERP
-关联关系：
- T_StepEmployee.employeeId = S_BusinessMan.recId
- T_StepEmployee.stepsId = T_Steps.recId

---

#### 58 工序--间接材料 (T_StepIndiectMatLink)

- **业务含义**：工序--间接材料
- **所属数据库**：思方云2 ERP
-关联关系：
- T_StepIndiectMatLink.altMaterialsId = M_Materials.recId
- T_StepIndiectMatLink.altUnitId = T_Unit.recId
- T_StepIndiectMatLink.materialsId = M_Materials.recId
- T_StepIndiectMatLink.stepsId = T_Steps.recId
- T_StepIndiectMatLink.unitId = T_Unit.recId

---

#### 59 工序表 (T_Steps)

- **业务含义**：工序表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Steps.companyId = T_Company.recId
- T_Steps.departmentId = T_Department.recId
- T_Steps.plantsId = T_Plants.recId
- T_Steps.unitId = T_Unit.recId

---

#### 60 工序关联工艺 (T_StepsProcess)

- **业务含义**：工序关联工艺
- **所属数据库**：思方云2 ERP
-关联关系：
- T_StepsProcess.postRoleId = T_PostRole.recId
- T_StepsProcess.processId = T_Process.recId
- T_StepsProcess.stepsId = T_Steps.recId

---

#### 61 工艺定量、定性检验项表 (T_StepsProcessInspectItem)

- **业务含义**：工艺定量、定性检验项表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 62 外协类型 (T_SubcontractType)

- **业务含义**：外协类型
- **所属数据库**：思方云2 ERP
-关联关系：
- T_SubcontractType.endProcessId = T_Process.recId
- T_SubcontractType.inspectGroupId = T_InspectGroup.recId
- T_SubcontractType.startProcessId = T_Process.recId
- T_SubcontractType.unitId = T_Unit.recId

---

#### 63 外协类型明细表 (T_SubcontractTypeItem)

- **业务含义**：外协类型明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_SubcontractTypeItem.currencyId = T_Currency.recId
- T_SubcontractTypeItem.subcontractTypeId = T_SubcontractType.recId
- T_SubcontractTypeItem.suppliersId = M_Suppliers.recId

---

#### 64 外协类型-参数表 (T_SubcontractTypeParams)

- **业务含义**：外协类型-参数表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 65 系统配置表 (T_SystemConfig)

- **业务含义**：系统配置表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_SystemConfig.companyId = T_Company.recId

---

#### 66 系统日志 (T_SystemLog)

- **业务含义**：系统日志
- **所属数据库**：思方云2 ERP
-关联关系：
- T_SystemLog.userId = T_User.recId

---

#### 67 税率表 (T_Tax)

- **业务含义**：税率表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Tax.textId = T_Text.recId

---

#### 68 记事本 (T_Text)

- **业务含义**：记事本
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 69 单位 (T_Unit)

- **业务含义**：单位
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 70 T_UseProcess (T_UseProcess)

- **业务含义**：ERP 系统 T_UseProcess 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_UseProcess.formRecId = T_Category.recId
- T_UseProcess.materialsId = M_Materials.recId
- T_UseProcess.processRecId = T_Process.recId
- T_UseProcess.creatorId = T_User.recId
- T_UseProcess.companyId = T_Company.recId
- T_UseProcess.productGroupId = S_ProductGroup.recId
- T_UseProcess.locationId = T_Location.recId

---

#### 71 用户表 (T_User)

- **业务含义**：用户表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_User.businessManId = S_BusinessMan.recId
- T_User.setDepId = T_Department.recId

---

#### 72 用户功能表 (T_UserFunctionRight)

- **业务含义**：用户功能表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_UserFunctionRight.functionRightId = T_FunctionRight.recId
- T_UserFunctionRight.groupId = T_Group.recId
- T_UserFunctionRight.userId = T_User.recId

---

#### 73 用户模块 (T_UserModule)

- **业务含义**：用户模块
- **所属数据库**：思方云2 ERP
-关联关系：
- T_UserModule.groupId = T_Group.recId
- T_UserModule.moduleId = T_Module.recId
- T_UserModule.userId = T_User.recId

---

#### 74 用户所在工厂权限 (T_UserPlant)

- **业务含义**：用户所在工厂权限
- **所属数据库**：思方云2 ERP
-关联关系：
- T_UserPlant.plantsId = T_Plants.recId
- T_UserPlant.userId = T_User.recId

---

#### 75 用户--岗位 (T_UserPostRole)

- **业务含义**：用户--岗位
- **所属数据库**：思方云2 ERP
-关联关系：
- T_UserPostRole.postRoleId = T_PostRole.recId
- T_UserPostRole.userId = T_User.recId

---

#### 76 仓库 (T_Warehouse)

- **业务含义**：仓库
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Warehouse.companyId = T_Company.recId
- T_Warehouse.plantsId = T_Plants.recId
- T_Warehouse.postRoleId = T_PostRole.recId

---

#### 77 仓库人员明细 (T_WarehouseKeepers)

- **业务含义**：仓库人员明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 78 T_Workshop (T_Workshop)

- **业务含义**：ERP 系统 T_Workshop 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- T_Workshop.plantsId = T_Plants.recId

---

### 2.2 物料模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 79 BOM发料 (M_BOMIssue)

- **业务含义**：BOM发料
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMIssue.bomPicklistId = M_BOMPicklist.recId
- M_BOMIssue.creatorId = T_User.recId
- M_BOMIssue.departmentId = T_Department.recId
- M_BOMIssue.warehouseId = T_Warehouse.recId

---

#### 80 BOM发料明细表 (M_BOMIssueItem)

- **业务含义**：BOM发料明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMIssueItem.inventoryBatchId = 物料批次库存.recId
- M_BOMIssueItem.bomIssueId = M_BOMIssue.recId
- M_BOMIssueItem.materialsId = M_Materials.recId
- M_BOMIssueItem.stockUnitId = T_Unit.recId
- M_BOMIssueItem.mfgPartId = E_JobMfgParts.recId

---

#### 81 BOM领料单 (M_BOMPicklist)

- **业务含义**：BOM领料单
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMPicklist.companyId = T_Company.recId
- M_BOMPicklist.creatorId = T_User.recId
- M_BOMPicklist.departmentId = T_Department.recId
- M_BOMPicklist.flowTypeId = T_FlowType.recId
- M_BOMPicklist.plantsId = T_Plants.recId
- M_BOMPicklist.postRoleId = T_PostRole.recId
- M_BOMPicklist.stepsId = T_Steps.recId
- M_BOMPicklist.warehouseId = T_Warehouse.recId
- M_BOMPicklist.bomIssueId = M_BOMIssue.recId

---

#### 82 BOM领料单审批记录 (M_BOMPicklistHistory)

- **业务含义**：BOM领料单审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMPicklistHistory.bomPicklistId = M_BOMPicklist.recId
- M_BOMPicklistHistory.myId = T_User.recId

---

#### 83 BOM领料单明细 (M_BOMPicklistItem)

- **业务含义**：BOM领料单明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMPicklistItem.bomBatchingId = P_BOMBatching.recId
- M_BOMPicklistItem.bomPicklistId = M_BOMPicklist.recId
- M_BOMPicklistItem.mfgPartId = E_JobMfgParts.recId
- M_BOMPicklistItem.materialsId = M_Materials.recId
- M_BOMPicklistItem.moId = P_MO.recId
- M_BOMPicklistItem.stockUnitId = T_Unit.recId
- M_BOMPicklistItem.bomIssueItemId = M_BOMIssueItem.recId

---

#### 84 BOM领料批次 (M_BOMPicklistItemBatch)

- **业务含义**：BOM领料批次
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMPicklistItemBatch.bomIssueItemId = M_BOMIssueItem.recId
- M_BOMPicklistItemBatch.bomPicklistItemId = M_BOMPicklistItem.qtyRemaining
- M_BOMPicklistItemBatch.inventoryBatchId = M_InventoryBatch.recId

---

#### 85 BOM领料外发 (M_BOMPicklistWF)

- **业务含义**：BOM领料外发
- **所属数据库**：思方云2 ERP
-关联关系：
- M_BOMPicklistWF.bomPicklistId = M_BOMPicklist.recId
- M_BOMPicklistWF.myId = T_User.recId

---

#### 86 寄送表 (M_Consignment)

- **业务含义**：寄送表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Consignment.warehousingId = T_Warehousing.recId
- M_Consignment.purchaseOrderId = M_PurchaseOrder.recId

---

#### 87 物料数据--包线管理 (M_Envelope)

- **业务含义**：物料数据--包线管理
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Envelope.companyId = T_Company.recId
- M_Envelope.creatorId = T_User.recId
- M_Envelope.currencyId = T_Currency.recId
- M_Envelope.flowTypeId = T_FlowType.recId
- M_Envelope.postRoleId = T_PostRole.recId
- M_Envelope.processId = T_Process.recId
- M_Envelope.stepsIds = T_Steps.recId
- M_Envelope.suppliersId = M_Suppliers.recId
- M_Envelope.taxId = T_Tax.recId
- M_Envelope.unitId = T_Unit.recId

---

#### 88 M_EnvelopeHistory (M_EnvelopeHistory)

- **业务含义**：ERP 系统 M_EnvelopeHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 89 物料数据--包线管理明细 (M_EnvelopeItem)

- **业务含义**：物料数据--包线管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_EnvelopeItem.envelopeId = M_Envelope.recId

---

#### 90 M_EnvelopeWF (M_EnvelopeWF)

- **业务含义**：ERP 系统 M_EnvelopeWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 91 物料库存 (M_Inventory)

- **业务含义**：物料库存
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Inventory.locationId = T_Location.recId
- M_Inventory.materialsId = M_Materials.recId
- M_Inventory.stockUnitId = T_Unit.recId
- M_Inventory.warehouseId = T_Warehouse.recId

---

#### 92 物料批次库存 (M_InventoryBatch)

- **业务含义**：物料批次库存
- **所属数据库**：思方云2 ERP
-关联关系：
- M_InventoryBatch.poItemId = M_PurchaseOrderItem.recId
- M_InventoryBatch.receiptItemId = M_ReceiptItem.recId
- M_InventoryBatch.locationId = T_Location.recId
- M_InventoryBatch.materialsId = M_Materials.recId
- M_InventoryBatch.stockUnitId = T_Unit.recId
- M_InventoryBatch.suppliersId = M_Suppliers.recId
- M_InventoryBatch.warehouseId = T_Warehouse.recId

---

#### 93 M_InventoryBatch_bak0413 (M_InventoryBatch_bak0413)

- **业务含义**：ERP 系统 M_InventoryBatch_bak0413 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 94 碎料管理 (M_InventorybatchRemaining)

- **业务含义**：碎料管理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 95 库存检验 (M_InventoryCheck)

- **业务含义**：库存检验
- **所属数据库**：思方云2 ERP
-关联关系：
- M_InventoryCheck.creatorId = T_User.recId
- M_InventoryCheck.fiscalPeriodId = T_FiscalPeriod.recId
- M_InventoryCheck.postRoleId = T_PostRole.recId
- M_InventoryCheck.warehouseId = T_Warehouse.recId

---

#### 96 库存检验明细 (M_InventoryCheckItem)

- **业务含义**：库存检验明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_InventoryCheckItem.inventoryBatchId = M_InventoryBatch.recId
- M_InventoryCheckItem.inventoryId = M_Inventory.recId
- M_InventoryCheckItem.inventoryCheckId = M_InventoryCheck.recId
- M_InventoryCheckItem.inventoryCheckReasonId = T_InventoryCheckReason.recId
- M_InventoryCheckItem.locationId = T_Location.recId
- M_InventoryCheckItem.materialsId = M_Materials.recId
- M_InventoryCheckItem.stockUnitId = T_Unit.recId

---

#### 97 杂项领料中的物料 (M_InventoryMiscBatch)

- **业务含义**：杂项领料中的物料
- **所属数据库**：思方云2 ERP
-关联关系：
- M_InventoryMiscBatch.poItemId = M_PurchaseOrderItem.recId
- M_InventoryMiscBatch.stockUnitId = T_Unit.recId
- M_InventoryMiscBatch.suppliersId = M_Suppliers.recId
- M_InventoryMiscBatch.warehouseId = T_Warehouse.recId

---

#### 98 模组 (M_InventoryOut)

- **业务含义**：模组
- **所属数据库**：思方云2 ERP
-关联关系：
- M_InventoryOut.inventoryId = M_Inventory.recId
- M_InventoryOut.inventoryBatchId = M_InventoryBatch.currencyId

---

#### 99 物料IQC报废 (M_IQC)

- **业务含义**：物料IQC报废
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQC.buyUnitId = T_Unit.recId
- M_IQC.checkorId = T_User.recId
- M_IQC.companyId = T_Company.recId
- M_IQC.creatorId = T_User.recId
- M_IQC.flowTypeId = T_FlowType.recId
- M_IQC.materialsId = M_Materials.recId
- M_IQC.plantsId = T_Plants.recId
- M_IQC.postRoleId = T_PostRole.recId
- M_IQC.suppliersId = M_Suppliers.recId

---

#### 100 M_IQCHistory (M_IQCHistory)

- **业务含义**：ERP 系统 M_IQCHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQCHistory.iqcTestId = M_IQC.recId
- M_IQCHistory.myId = T_User.recId

---

#### 101 物料IQC报废明细表 (M_IQCItem)

- **业务含义**：物料IQC报废明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQCItem.inspectItemsId = T_InspectItems.recId
- M_IQCItem.iqcTestId = M_IQC.recId

---

#### 102 物料送检单管理 (M_IQCRecheck)

- **业务含义**：物料送检单管理
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQCRecheck.inventoryId = M_Inventory.recId
- M_IQCRecheck.creatorId = T_User.recId
- M_IQCRecheck.inspectPostId = T_PostRole.recId
- M_IQCRecheck.inventoryBatchId = M_InventoryBatch.recId
- M_IQCRecheck.postRoleId = T_PostRole.recId
- M_IQCRecheck.warehouseId = T_Warehouse.recId

---

#### 103 物料检验 报废原因 (M_IQCResult)

- **业务含义**：物料检验 报废原因
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQCResult.defectId = T_Defect.recId
- M_IQCResult.iqcTestId = M_IQC.recId

---

#### 104 M_IQCWF (M_IQCWF)

- **业务含义**：ERP 系统 M_IQCWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_IQCWF.iqcTestId = M_IQC.recId
- M_IQCWF.myId = T_User.recId

---

#### 105 领料和退料表 (M_MaterialIssueRequest)

- **业务含义**：领料和退料表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialIssueRequest.companyId = T_Company.recId
- M_MaterialIssueRequest.creatorId = T_User.recId
- M_MaterialIssueRequest.departmentId = T_Department.recId
- M_MaterialIssueRequest.flowTypeId = T_FlowType.recId
- M_MaterialIssueRequest.plantsId = T_Plants.recId
- M_MaterialIssueRequest.postRoleId = T_PostRole.recId
- M_MaterialIssueRequest.warehouseId = T_Warehouse.recId
- M_MaterialIssueRequest.rdProjectId = M_RDProject.recId

---

#### 106 领料和退料审批历史 (M_MaterialIssueRequestHistory)

- **业务含义**：领料和退料审批历史
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialIssueRequestHistory.myId = T_User.recId
- M_MaterialIssueRequestHistory.materialIssueRequestId = M_MaterialIssueRequest.recId

---

#### 107 领料和退料明细表 (M_MaterialIssueRequestItem)

- **业务含义**：领料和退料明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialIssueRequestItem.inventoryMiscBatchId = inventoryMiscBatch.recId
- M_MaterialIssueRequestItem.materialsIssueNoteItemId = M_MaterialsIssueNoteItem.recId
- M_MaterialIssueRequestItem.materialsId = M_Materials.recId
- M_MaterialIssueRequestItem.materialIssueRequestId = M_MaterialIssueRequest.recId
- M_MaterialIssueRequestItem.stepsId = T_Steps.recId
- M_MaterialIssueRequestItem.stockUnitId = T_Unit.recId
- M_MaterialIssueRequestItem.processId = T_Process.recId
- M_MaterialIssueRequestItem.bomPicklistItemId = M_BOMPicklistItem.qtyRemaining

---

#### 108 领料和退料审批流程 (M_MaterialIssueRequestWF)

- **业务含义**：领料和退料审批流程
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialIssueRequestWF.myId = T_User.recId
- M_MaterialIssueRequestWF.materialIssueRequestId = M_MaterialIssueRequest.recId

---

#### 109 材料装运明细表 (M_MaterialPackingSlipItem)

- **业务含义**：材料装运明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialPackingSlipItem.contractMaterialsId = S_ContractMaterials.recId
- M_MaterialPackingSlipItem.creatorId = T_User.recId
- M_MaterialPackingSlipItem.customerId = S_Customer.recId
- M_MaterialPackingSlipItem.packingSlipId = FGI_PackingSlip.recId
- M_MaterialPackingSlipItem.plantsId = T_Plants.recId
- M_MaterialPackingSlipItem.postRoleId = T_PostRole.recId

---

#### 110 采购报价明细表 (M_MaterialPriceChangedItem)

- **业务含义**：采购报价明细表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 111 物料表 (M_Materials)

- **业务含义**：物料表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Materials.botCuId = S_Conductor.recId
- M_Materials.topCuId = S_Conductor.recId
- M_Materials.buyUnitId = T_Unit.recId
- M_Materials.companyId = T_Company.recId
- M_Materials.customsUnitId = T_Unit.recId
- M_Materials.locationId = T_Location.recId
- M_Materials.postRoleId = T_PostRole.recId
- M_Materials.productGroupId = T_Category.recId
- M_Materials.stockUnitId = T_Unit.recId
- M_Materials.suppliersId = M_Suppliers.recId
- M_Materials.pdId = S_MaterialType.recId
- M_Materials.creatorId = T_User.recId

---

#### 112 物料所属公司 (M_MaterialsCompany)

- **业务含义**：物料所属公司
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialsCompany.companyId = T_Company.recId
- M_MaterialsCompany.materialsId = M_Materials.recId

---

#### 113 物料可分配数量表(占用) (M_MaterialsCostByPlant)

- **业务含义**：物料可分配数量表(占用)
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 114 发料和退回表 (M_MaterialsIssueNote)

- **业务含义**：发料和退回表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialsIssueNote.companyId = T_Company.recId
- M_MaterialsIssueNote.creatorId = T_User.recId
- M_MaterialsIssueNote.departmentId = T_Department.recId
- M_MaterialsIssueNote.postRoleId = T_PostRole.recId
- M_MaterialsIssueNote.userId = T_User.recId
- M_MaterialsIssueNote.warehouseId = T_Warehouse.recId

---

#### 115 发料和退回明细 (M_MaterialsIssueNoteItem)

- **业务含义**：发料和退回明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 116 物料发料和退回批次 (M_MaterialsIssueNoteItemBatch)

- **业务含义**：物料发料和退回批次
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialsIssueNoteItemBatch.bomPicklistItemBatchId = M_BomPicklistItemBatch.recId
- M_MaterialsIssueNoteItemBatch.inventoryId = M_Inventory.recId
- M_MaterialsIssueNoteItemBatch.materialInventoryOutId = M_MaterialInventoryOut.recId
- M_MaterialsIssueNoteItemBatch.inventoryBatchId = M_InventoryBatch.currencyId
- M_MaterialsIssueNoteItemBatch.materialsIssueNoteItemId = M_MaterialsIssueNoteItem.recId

---

#### 117 物料所在仓库 (M_MaterialsWarehouse)

- **业务含义**：物料所在仓库
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MaterialsWarehouse.locationId = T_Location.recId
- M_MaterialsWarehouse.materialsId = M_Materials.recId
- M_MaterialsWarehouse.warehouseId = T_Warehouse.recId

---

#### 118 月结记账表 (M_MonthlyClosing)

- **业务含义**：月结记账表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MonthlyClosing.fiscalPeriodId = T_FiscalPeriod.recId
- M_MonthlyClosing.plantsId = T_Plants.recId
- M_MonthlyClosing.companyId = T_Company.recId
- M_MonthlyClosing.warehouseId = T_Warehouse.recId

---

#### 119 物料月结部门表 (M_MonthlyClosingDepartment)

- **业务含义**：物料月结部门表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 120 月结记账明细表 (M_MonthlyClosingItem)

- **业务含义**：月结记账明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_MonthlyClosingItem.materialsId = M_Materials.recId
- M_MonthlyClosingItem.monthlyClosingId = M_MonthlyClosing.recId

---

#### 121 采购单 (M_PurchaseOrder)

- **业务含义**：采购单
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 122 采购审批表 (M_PurchaseOrderHistory)

- **业务含义**：采购审批表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_PurchaseOrderHistory.myId = T_User.recId
- M_PurchaseOrderHistory.purchaseOrderId = M_PurchaseOrder.recId

---

#### 123 采购明细单 (M_PurchaseOrderItem)

- **业务含义**：采购明细单
- **所属数据库**：思方云2 ERP
-关联关系：
- M_PurchaseOrderItem.contractMaterialsId = S_ContractMaterials.recId
- M_PurchaseOrderItem.prLinkId = M_RequisitionsItemAccepted.recId
- M_PurchaseOrderItem.buyUnitId = T_Unit.recId
- M_PurchaseOrderItem.customsUnitId = T_Unit.recId
- M_PurchaseOrderItem.departmentId = T_Department.recId
- M_PurchaseOrderItem.materialsId = M_Materials.recId
- M_PurchaseOrderItem.postRoleId = T_PostRole.recId
- M_PurchaseOrderItem.purchaseOrderId = M_PurchaseOrder.recId
- M_PurchaseOrderItem.stockUnitId = T_Unit.recId
- M_PurchaseOrderItem.warehouseId = T_Warehouse.recId

---

#### 124 采购待审批 (M_PurchaseOrderWF)

- **业务含义**：采购待审批
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 125 采购预算 (M_PurchasingBudget)

- **业务含义**：采购预算
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 126 预算明细（用户） (M_PurchasingBudgetItem)

- **业务含义**：预算明细（用户）
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 127 项目管理 (M_RDProject)

- **业务含义**：项目管理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 128 物料接收 (M_Receipt)

- **业务含义**：物料接收
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Receipt.companyId = T_Company.recId
- M_Receipt.creatorId = T_User.recId
- M_Receipt.plantsId = T_Plants.recId
- M_Receipt.postRoleId = T_PostRole.recId
- M_Receipt.suppliersId = M_Suppliers.recId

---

#### 129 物料接收明细 (M_ReceiptItem)

- **业务含义**：物料接收明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_ReceiptItem.inventoryMiscBatchId = M_InventoryMiscBatch.recId
- M_ReceiptItem.poItemId = M_PurchaseOrderItem.FGI_Inventory
- M_ReceiptItem.buyUnitId = T_Unit.recId
- M_ReceiptItem.customsUnitId = T_Unit.recId
- M_ReceiptItem.departmentId = T_Department.recId
- M_ReceiptItem.locationId = T_Location.recId
- M_ReceiptItem.materialsId = M_Materials.recId
- M_ReceiptItem.postRoleId = T_PostRole.recId
- M_ReceiptItem.receiptId = M_Receipt.recId
- M_ReceiptItem.stockUnitId = T_Unit.recId
- M_ReceiptItem.warehouseId = T_Warehouse.recId

---

#### 130 M_ReplaceMaterials (M_ReplaceMaterials)

- **业务含义**：ERP 系统 M_ReplaceMaterials 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_ReplaceMaterials.materialsId = M_Materials.recId
- M_ReplaceMaterials.replaceMaterialsId = M_ReplaceMaterials.recId

---

#### 131 请购单 (M_Requisitions)

- **业务含义**：请购单
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Requisitions.companyId = T_Company.recId
- M_Requisitions.creatorId = T_User.recId
- M_Requisitions.departmentId = T_Department.recId
- M_Requisitions.flowTypeId = T_FlowType.recId
- M_Requisitions.plantsId = T_Plants.recId
- M_Requisitions.postRoleId = T_PostRole.recId

---

#### 132 请购审批表 (M_RequisitionsHistory)

- **业务含义**：请购审批表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_RequisitionsHistory.myId = T_User.recId
- M_RequisitionsHistory.requisitionsId = M_Requisitions.recId

---

#### 133 请购明细单 (M_RequisitionsItem)

- **业务含义**：请购明细单
- **所属数据库**：思方云2 ERP
-关联关系：
- M_RequisitionsItem.materialsId = M_Materials.recId
- M_RequisitionsItem.postRoleId = T_PostRole.recId
- M_RequisitionsItem.requisitionsId = M_Requisitions.recId
- M_RequisitionsItem.stockUnitId = T_Unit.recId
- M_RequisitionsItem.suppliersId = M_Suppliers.recId

---

#### 134 请购受理表 (M_RequisitionsItemAccepted)

- **业务含义**：请购受理表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_RequisitionsItemAccepted.ifSpecifySuppId = M_Suppliers.recId
- M_RequisitionsItemAccepted.poLinkId = M_PurchaseOrderItem.FGI_Inventory
- M_RequisitionsItemAccepted.requisitionsItemId = M_RequisitionsItem.recId
- M_RequisitionsItemAccepted.acceptorId = T_User.recId
- M_RequisitionsItemAccepted.buyUnitId = T_Unit.recId
- M_RequisitionsItemAccepted.creatorId = T_User.recId
- M_RequisitionsItemAccepted.currencyId = T_Currency.recId
- M_RequisitionsItemAccepted.departmentId = T_Department.recId
- M_RequisitionsItemAccepted.materialsId = M_Materials.recId
- M_RequisitionsItemAccepted.plantsId = T_Plants.recId
- M_RequisitionsItemAccepted.postRoleId = T_PostRole.recId
- M_RequisitionsItemAccepted.stockUnitId = T_Unit.recId
- M_RequisitionsItemAccepted.suppliersId = M_Suppliers.recId

---

#### 135 M_RequisitionsWF (M_RequisitionsWF)

- **业务含义**：ERP 系统 M_RequisitionsWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_RequisitionsWF.myId = T_User.recId
- M_RequisitionsWF.requisitionsId = M_Requisitions.recId

---

#### 136 退货表 (M_ReturnOrder)

- **业务含义**：退货表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_ReturnOrder.companyId = T_Company.recId
- M_ReturnOrder.creatorId = T_User.recId
- M_ReturnOrder.plantsId = T_Plants.recId
- M_ReturnOrder.postRoleId = T_PostRole.recId
- M_ReturnOrder.suppliersId = M_Suppliers.recId

---

#### 137 退货明细表 (M_ReturnOrderItem)

- **业务含义**：退货明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_ReturnOrderItem.debitMemoItemId = F_AP_DebitMemoItem.recId
- M_ReturnOrderItem.iqcId = M_IQC.recId
- M_ReturnOrderItem.returnOrderId = M_ReturnOrder.recId

---

#### 138 SPDS管理 (M_SPDS)

- **业务含义**：SPDS管理
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SPDS.buyUnitId = T_Unit.recId
- M_SPDS.companyId = T_Company.recId
- M_SPDS.creatorId = T_User.recId
- M_SPDS.currencyId = T_Currency.recId
- M_SPDS.customsUnitId = T_Unit.recId
- M_SPDS.flowTypeId = T_FlowType.recId
- M_SPDS.materialsId = M_Materials.recId
- M_SPDS.postRoleId = T_PostRole.recId
- M_SPDS.stockUnitId = T_Unit.recId
- M_SPDS.suppliersId = M_Suppliers.recId
- M_SPDS.taxId = T_Tax.recId
- M_SPDS.warehouseId = T_Warehouse.recId

---

#### 139 M_SPDSHistory (M_SPDSHistory)

- **业务含义**：ERP 系统 M_SPDSHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 140 SPDS管理明细 (M_SPDSItem)

- **业务含义**：SPDS管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SPDSItem.spdsId = M_SPDS.recId

---

#### 141 M_SPDSWF (M_SPDSWF)

- **业务含义**：ERP 系统 M_SPDSWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SPDSWF.myId = T_User.recId
- M_SPDSWF.spdsId = M_SPDS.recId

---

#### 142 M_StepCheck (M_StepCheck)

- **业务含义**：ERP 系统 M_StepCheck 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_StepCheck.fiscalPeriodId = T_FiscalPeriod.recId
- M_StepCheck.postRoleId = T_PostRole.recId
- M_StepCheck.stepsId = T_Steps.recId

---

#### 143 M_StepCheckItem (M_StepCheckItem)

- **业务含义**：ERP 系统 M_StepCheckItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_StepCheckItem.stepMaterialStandardId = T_StepIndiectMatLink.recId
- M_StepCheckItem.materialsId = M_Materials.recId
- M_StepCheckItem.stepCheckId = M_StepCheck.stepsId

---

#### 144 供应商资料 (M_Suppliers)

- **业务含义**：供应商资料
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Suppliers.textId = T_Text.recId
- M_Suppliers.areaId = T_Area.recId
- M_Suppliers.companyId = T_Company.recId
- M_Suppliers.creatorId = T_User.recId
- M_Suppliers.reditId = T_Cate.recId
- M_Suppliers.currencyId = T_Currency.recId
- M_Suppliers.flowTypeId = T_FlowType.recId
- M_Suppliers.fobId = T_FOB.recId
- M_Suppliers.paymentMethodId = T_PaymentMethod.recId
- M_Suppliers.paymentTermId = T_PaymentTerm.recId
- M_Suppliers.postRoleId = T_PostRole.recId
- M_Suppliers.taxId = T_Tax.recId

---

#### 145 供应商所属公司 (M_SuppliersCompany)

- **业务含义**：供应商所属公司
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SuppliersCompany.companyId = T_Company.recId
- M_SuppliersCompany.suppliersId = M_Suppliers.recId

---

#### 146 供应商审批记录 (M_SuppliersHistory)

- **业务含义**：供应商审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SuppliersHistory.myId = T_User.recId
- M_SuppliersHistory.suppliersId = M_Suppliers.recId

---

#### 147 M_SuppliersWF (M_SuppliersWF)

- **业务含义**：ERP 系统 M_SuppliersWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- M_SuppliersWF.myId = T_User.recId
- M_SuppliersWF.suppliersId = M_Suppliers.recId

---

#### 148 调拨管理 (M_Transfer)

- **业务含义**：调拨管理
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Transfer.creatorId = T_User.recId
- M_Transfer.destWarehouseId = T_Warehouse.recId
- M_Transfer.origWarehouseId = T_Warehouse.recId
- M_Transfer.postRoleId = T_PostRole.recId
- M_Transfer.receiveId = T_User.recId
- M_Transfer.receiveCompanyId = T_Company.recId

---

#### 149 调拨管理明细 (M_TransferItem)

- **业务含义**：调拨管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_TransferItem.inventoryId = M_Inventory.recId
- M_TransferItem.inventoryBatchId = M_InventoryBatch.currencyId
- M_TransferItem.locationId = T_Location.recId
- M_TransferItem.transferId = M_Transfer.recId
- M_TransferItem.transferItemId = M_TransferItem.recId

---

#### 150 物料入库 (M_Warehousing)

- **业务含义**：物料入库
- **所属数据库**：思方云2 ERP
-关联关系：
- M_Warehousing.companyId = T_Company.recId
- M_Warehousing.creatorId = T_User.recId
- M_Warehousing.postRoleId = T_PostRole.recId
- M_Warehousing.warehouseId = T_Warehouse.recId

---

#### 151 物料入库明细 (M_WarehousingItem)

- **业务含义**：物料入库明细
- **所属数据库**：思方云2 ERP
-关联关系：
- M_WarehousingItem.inventoryBatchId = M_InventoryBatch.currencyId
- M_WarehousingItem.inventoryId = M_Inventory.recId
- M_WarehousingItem.receiptItemId = M_ReceiptItem.recId
- M_WarehousingItem.buyUnitId = T_Unit.recId
- M_WarehousingItem.customsUnitId = T_Unit.recId
- M_WarehousingItem.locationId = T_Location.recId
- M_WarehousingItem.materialsId = M_Materials.recId
- M_WarehousingItem.stockUnitId = T_Unit.recId
- M_WarehousingItem.suppliersId = M_Suppliers.recId
- M_WarehousingItem.warehousingId = M_Warehousing.recId

---

### 2.3 成品模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 152 装箱单编号表（箱包表） (FGI_CartonsNumber)

- **业务含义**：装箱单编号表（箱包表）
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_CartonsNumber.cartonsNumberService = FGI_StockForm.recId
- FGI_CartonsNumber.stockFormJobId = FGI_StockFormJob.recId
- FGI_CartonsNumber.jobId = s_job.recId
- FGI_CartonsNumber.salesPartId = S_SalesParts.recId

---

#### 153 成品库存 (FGI_Inventory)

- **业务含义**：成品库存
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_Inventory.batchNumber = FGI_StockFormItem.batchNumber
- FGI_Inventory.customerId = S_Customer.recId
- FGI_Inventory.poItemId = S_OS_POItem.recId
- FGI_Inventory.stockFormItemId = FGI_stockFormItem.recId
- FGI_Inventory.jobId = S_Job.recId
- FGI_Inventory.locationId = T_Location.recId
- FGI_Inventory.plantsId = T_Plants.recId
- FGI_Inventory.salesPartId = S_SalesParts.recId
- FGI_Inventory.suppliersId = M_Suppliers.recId
- FGI_Inventory.warehouseId = T_Warehouse.recId
- FGI_Inventory.contractItemId = S_ContractItem（不包括外协订单入库）.recId
- FGI_Inventory.fgiScrapSheetItemId = FGI_ScrapSheetItem.recId
- FGI_Inventory.fgiPropertyId = 分类.recId
- FGI_Inventory.woId = P_WO.recId
- FGI_Inventory.moId = P_MO.recId

---

#### 154 成品出库批次号表 (FGI_InventoryOut)

- **业务含义**：成品出库批次号表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_InventoryOut.contractItemId = S_ContractItem.recId
- FGI_InventoryOut.fgiInventoryId = FGI_Inventory.recId
- FGI_InventoryOut.jobId = S_Job.recId
- FGI_InventoryOut.packingSlipItemId = FGI_PackingSlipItem.recId

---

#### 155 制成品检验单 (FGI_IQC)

- **业务含义**：制成品检验单
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_IQC.moId = P_MO.recId
- FGI_IQC.poItemId = S_OS_POItem.recId
- FGI_IQC.checkorId = T_User.recId
- FGI_IQC.creatorId = T_User.recId
- FGI_IQC.flowTypeId = T_FlowType.recId
- FGI_IQC.jobId = S_Job.recId
- FGI_IQC.plantsId = T_Plants.recId
- FGI_IQC.postRoleId = T_PostRole.recId
- FGI_IQC.salesPartId = S_SalesParts.recId
- FGI_IQC.unitId = T_Unit.recId

---

#### 156 FGI_IQCHistory (FGI_IQCHistory)

- **业务含义**：ERP 系统 FGI_IQCHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_IQCHistory.fgiiqcId = FGI_IQC.recId

---

#### 157 检验项目 (FGI_IQCItem)

- **业务含义**：检验项目
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_IQCItem.fgiiqcId = FGI_IQC.recId
- FGI_IQCItem.inspectItemsId = T_InspectItems.recId

---

#### 158 检验结果表 (FGI_IQCResult)

- **业务含义**：检验结果表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_IQCResult.defectId = T_Defect.recId
- FGI_IQCResult.fgiiqcId = FGI_IQC.recId
- FGI_IQCResult.processId = T_Process.recId
- FGI_IQCResult.stepsId = T_Steps.recId
- FGI_IQCResult.unitId = T_Unit.recId

---

#### 159 FGI_IQCWF (FGI_IQCWF)

- **业务含义**：ERP 系统 FGI_IQCWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_IQCWF.fgiiqcId = FGI_IQC.recId
- FGI_IQCWF.myId = T_User.recId

---

#### 160 FGI_JobIssueNote (FGI_JobIssueNote)

- **业务含义**：ERP 系统 FGI_JobIssueNote 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueNote.companyId = T_Company.recId
- FGI_JobIssueNote.creatorId = T_User.recId
- FGI_JobIssueNote.departmentId = T_Department.recId
- FGI_JobIssueNote.postRoleId = T_PostRole.recId
- FGI_JobIssueNote.userId = T_User.recId
- FGI_JobIssueNote.warehouseId = T_Warehouse.recId

---

#### 161 FGI_JobIssueNoteItem (FGI_JobIssueNoteItem)

- **业务含义**：ERP 系统 FGI_JobIssueNoteItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueNoteItem.jobIssueRequestItemId = FGI_JobIssueRequestItem.recId
- FGI_JobIssueNoteItem.jobIssueNoteId = FGI_JobIssueNote.recId

---

#### 162 FGI_JobIssueNoteItemBatch (FGI_JobIssueNoteItemBatch)

- **业务含义**：ERP 系统 FGI_JobIssueNoteItemBatch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueNoteItemBatch.fgiInventoryId = FGI_Inventory.recId
- FGI_JobIssueNoteItemBatch.jobIssueNoteItemId = FGI_JobIssueNoteItem.recId

---

#### 163 FGI_JobIssueRequest (FGI_JobIssueRequest)

- **业务含义**：ERP 系统 FGI_JobIssueRequest 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueRequest.companyId = T_Company.recId
- FGI_JobIssueRequest.creatorId = T_User.recId
- FGI_JobIssueRequest.departmentId = T_Department.recId
- FGI_JobIssueRequest.flowTypeId = T_FlowType.recId
- FGI_JobIssueRequest.plantsId = T_Plants.recId
- FGI_JobIssueRequest.postRoleId = T_PostRole.recId
- FGI_JobIssueRequest.warehouseId = T_Warehouse.recId

---

#### 164 FGI_JobIssueRequestHistory (FGI_JobIssueRequestHistory)

- **业务含义**：ERP 系统 FGI_JobIssueRequestHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueRequestHistory.myId = T_User.recId
- FGI_JobIssueRequestHistory.jobIssueRequestId = FGI_JobIssueRequest.recId

---

#### 165 FGI_JobIssueRequestItem (FGI_JobIssueRequestItem)

- **业务含义**：ERP 系统 FGI_JobIssueRequestItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_JobIssueRequestItem.jobId = S_Job.recId
- FGI_JobIssueRequestItem.fgiIssueRequestId = FGI_JobIssueRequest.recId
- FGI_JobIssueRequestItem.stepsId = T_Steps.recId

---

#### 166 FGI_JobIssueRequestWF (FGI_JobIssueRequestWF)

- **业务含义**：ERP 系统 FGI_JobIssueRequestWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 167 成品月结 (FGI_MonthlyClosing)

- **业务含义**：成品月结
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_MonthlyClosing.creatorId = T_User.recId
- FGI_MonthlyClosing.fiscalPeriodId = T_FiscalPeriod.recId
- FGI_MonthlyClosing.plantsId = T_Plants.recId
- FGI_MonthlyClosing.companyId = T_Company.recId
- FGI_MonthlyClosing.warehouseId = T_WareHouse.recId

---

#### 168 成品月结明细 (FGI_MonthlyClosingItem)

- **业务含义**：成品月结明细
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_MonthlyClosingItem.jobId = S_Job.recId
- FGI_MonthlyClosingItem.monthlyClosingId = FGI_MonthlyClosing.recId
- FGI_MonthlyClosingItem.fgiMonthlyClosingId = FGI_MonthlyClosing.recId

---

#### 169 成品装箱单 (FGI_PackingItem)

- **业务含义**：成品装箱单
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackingItem.packingSlipItemId = FGI_PackingSlipItem.recId
- FGI_PackingItem.packingSlipId = FGI_PackingSlip.recId
- FGI_PackingItem.cartonsId = S_Cartons.recId

---

#### 170 成品出货 (FGI_PackingSlip)

- **业务含义**：成品出货
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackingSlip.assignUserId = T_User.recId
- FGI_PackingSlip.salesRepId = S_BusinessMan.recId
- FGI_PackingSlip.companyId = T_Company.recId
- FGI_PackingSlip.confirmedUserId = T_User.recId
- FGI_PackingSlip.creatorId = T_User.recId
- FGI_PackingSlip.currencyId = T_Currency.recId
- FGI_PackingSlip.customerId = S_Customer.recId
- FGI_PackingSlip.shippingAddressId = S_CustomerAddress.recId
- FGI_PackingSlip.flowTypeId = T_FlowType.recId
- FGI_PackingSlip.fobId = T_FOB.recId
- FGI_PackingSlip.shipUserId = T_User.recId
- FGI_PackingSlip.shippingMethodId = T_Shipping.recId

---

#### 171 箱包关联表 (FGI_PackingSlipCartonsNumber)

- **业务含义**：箱包关联表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackingSlipCartonsNumber.packingSlipId = FGI_PackingSlip.recId
- FGI_PackingSlipCartonsNumber.cartonsNumberId = FGI_CartonsNumber.recId
- FGI_PackingSlipCartonsNumber.salesPartId = S_SalesParts.recId

---

#### 172 FGI_PackingSlipHistory (FGI_PackingSlipHistory)

- **业务含义**：ERP 系统 FGI_PackingSlipHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackingSlipHistory.myId = T_User.recId
- FGI_PackingSlipHistory.packingSlipId = FGI_PackingSlip.recId

---

#### 173 成品出货明细表 (FGI_PackingSlipItem)

- **业务含义**：成品出货明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackingSlipItem.jobId = S_Job.recId
- FGI_PackingSlipItem.packingSlipItemId = FGI_PackingSlipItem.recId
- FGI_PackingSlipItem.contractItemId = S_ContractItem.recId
- FGI_PackingSlipItem.contractSOId = S_ContractSO.recId
- FGI_PackingSlipItem.creatorId = T_User.recId
- FGI_PackingSlipItem.customerId = S_Customer.recId
- FGI_PackingSlipItem.orderUnitId = T_Unit.recId
- FGI_PackingSlipItem.packingSlipId = FGI_PackingSlip.recId
- FGI_PackingSlipItem.plantsId = T_Plants.recId
- FGI_PackingSlipItem.postRoleId = T_PostRole.recId

---

#### 174 FGI_PackingSlipWF (FGI_PackingSlipWF)

- **业务含义**：ERP 系统 FGI_PackingSlipWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 175 箱包，包明细表 (FGI_PackNumber)

- **业务含义**：箱包，包明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PackNumber.fgiInventoryId = FGI_Inventory.recId
- FGI_PackNumber.cartonsNumberId = FGI_CartonsNumber.recId
- FGI_PackNumber.stockFormItemId = FGI_StockFormItem.recId

---

#### 176 卡板表 (FGI_PalletNumber)

- **业务含义**：卡板表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_PalletNumber.plantsId = T_Plants.recId
- FGI_PalletNumber.jobId = S_Job.recId
- FGI_PalletNumber.creatorId = T_User.recId
- FGI_PalletNumber.modifiedById = T_User.recId

---

#### 177 制成品接收单 (FGI_Receipt)

- **业务含义**：制成品接收单
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_Receipt.sourceId = M_Suppliers/S_Customer.recId
- FGI_Receipt.creatorId = T_User.recId
- FGI_Receipt.plantsId = T_Plants.recId
- FGI_Receipt.postRoleId = T_PostRole.recId

---

#### 178 制成品接收单明细 (FGI_ReceiptItem)

- **业务含义**：制成品接收单明细
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_ReceiptItem.orderId = S_OS_POItem.recId
- FGI_ReceiptItem.fgiReceiptId = FGI_Receipt.recId
- FGI_ReceiptItem.jobId = S_Job.recId
- FGI_ReceiptItem.postRoleId = T_PostRole.recId
- FGI_ReceiptItem.salesPartId = S_SalesParts.recId
- FGI_ReceiptItem.unitId = T_Unit.recId

---

#### 179 成品退货表 (FGI_ReturnOrder)

- **业务含义**：成品退货表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_ReturnOrder.creatorId = T_User.recId
- FGI_ReturnOrder.plantsId = T_Plants.recId
- FGI_ReturnOrder.postRoleId = T_PostRole.recId
- FGI_ReturnOrder.suppliersId = M_Suppliers.recId

---

#### 180 成品退货明细表 (FGI_ReturnOrderItem)

- **业务含义**：成品退货明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_ReturnOrderItem.fgiReturnOrderId = FGI_ReturnOrder.recId
- FGI_ReturnOrderItem.fgiiqcId = FGI_IQC.recId
- FGI_ReturnOrderItem.jobId = S_Job.recId
- FGI_ReturnOrderItem.salesPartId = S_SalesParts.recId
- FGI_ReturnOrderItem.unitId = T_Unit.recId

---

#### 181 成品报废 (FGI_ScrapSheet)

- **业务含义**：成品报废
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_ScrapSheet.checkorId = T_User.recId
- FGI_ScrapSheet.creatorId = T_User.recId
- FGI_ScrapSheet.warehouseId = T_Warehouse.recId

---

#### 182 成品报废明细 (FGI_ScrapSheetItem)

- **业务含义**：成品报废明细
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_ScrapSheetItem.fgiInventoryId = FGI_Inventory.recId
- FGI_ScrapSheetItem.fgiScrapSheetId = FGI_ScrapSheet.recId

---

#### 183 成品入库 (FGI_StockForm)

- **业务含义**：成品入库
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 184 成品入库明细 (FGI_StockFormItem)

- **业务含义**：成品入库明细
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_StockFormItem.orderId = FGI_ReceiptItem.recId
- FGI_StockFormItem.cartonsId = S_Cartons.recId
- FGI_StockFormItem.jobId = S_Job.recId
- FGI_StockFormItem.locationId = T_Location.recId
- FGI_StockFormItem.salesPartId = S_SalesParts.recId
- FGI_StockFormItem.stockFormId = FGI_StockForm.recId
- FGI_StockFormItem.contractSOId = S_ContractSO.recId
- FGI_StockFormItem.moId = P_MO.recId

---

#### 185 生产入库 (FGI_StockFormItemWO)

- **业务含义**：生产入库
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_StockFormItemWO.stockFormItemId = FGI_StockFormItem.recId
- FGI_StockFormItemWO.woId = P_WO.recId
- FGI_StockFormItemWO.outPutId = P_OutPut.recId

---

#### 186 生产入库型号关联表 (FGI_StockFormJob)

- **业务含义**：生产入库型号关联表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_StockFormJob.stockFormId = FGI_StockForm.recId

---

#### 187 成品转仓表 (FGI_Transfer)

- **业务含义**：成品转仓表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_Transfer.creatorId = T_User.recId
- FGI_Transfer.destWarehouseId = T_Warehouse.recId
- FGI_Transfer.origWarehouseId = T_Warehouse.recId
- FGI_Transfer.receiveId = T_User.recId

---

#### 188 成品转仓明细表 (FGI_TransferItem)

- **业务含义**：成品转仓明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- FGI_TransferItem.desInventoryId = FGI_Inventory.recId
- FGI_TransferItem.locationId = T_Location.recId
- FGI_TransferItem.oriInventoryId = FGI_Inventory.recId
- FGI_TransferItem.transferId = FGI_Transfer.recId

---

### 2.4 工程模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 189 成德区分参数展示主表 (E_BoardTypeParameterSettings)

- **业务含义**：成德区分参数展示主表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 190 部件成本参数 (E_CostJobMfgPartsParams)

- **业务含义**：部件成本参数
- **所属数据库**：思方云2 ERP
-关联关系：
- E_CostJobMfgPartsParams.jobId = S_job.recId
- E_CostJobMfgPartsParams.mfgpartId = E_JobMfgParts.recId
- E_CostJobMfgPartsParams.parameterVal = E_JobMfgParts.recId
- E_CostJobMfgPartsParams.seq = E_JobMfgParts.recId
- E_CostJobMfgPartsParams.version = E_JobMfgParts.recId
- E_CostJobMfgPartsParams.parameterId = S_Parameters.recId

---

#### 191 工程流程那里添加的自定义脚本表 (E_CustomScriptSetting)

- **业务含义**：工程流程那里添加的自定义脚本表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 192 钻孔设计 (E_DrillDetails)

- **业务含义**：钻孔设计
- **所属数据库**：思方云2 ERP
-关联关系：
- E_DrillDetails.drl_Id = E_DrillTitle.recId
- E_DrillDetails.jobId = S_Job.recId

---

#### 193 钻带表 (E_DrillTitle)

- **业务含义**：钻带表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_DrillTitle.jobId = S_Job.recId
- E_DrillTitle.mfgpartId = E_JobMfgParts.recId

---

#### 194 工具表 (E_FPCToolTable)

- **业务含义**：工具表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_FPCToolTable.jobId = S_JOB.recId

---

#### 195 阻抗表 (E_Impedance)

- **业务含义**：阻抗表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 196 JOB关联合拼表 (E_JobChildren)

- **业务含义**：JOB关联合拼表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 197 生产型号图片 (E_JobImages)

- **业务含义**：生产型号图片
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobImages.jobId = S_Job.recId

---

#### 198 工作层  层信息 (E_JobLayers)

- **业务含义**：工作层  层信息
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobLayers.jobId = S_Job.recId
- E_JobLayers.baseCopperId = S_Conductor.recId
- E_JobLayers.finishCopperId = S_Conductor.recId

---

#### 199 工程制作——流程——部件参数表 (E_JobMfgPartParams)

- **业务含义**：工程制作——流程——部件参数表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobMfgPartParams.jobId = S_Job.recId
- E_JobMfgPartParams.mfgpartId = E_JobMfgParts.recId
- E_JobMfgPartParams.parametersId = S_Parameters.recId

---

#### 200 制造部件编号(本厂型号BOM表) (E_JobMfgParts)

- **业务含义**：制造部件编号(本厂型号BOM表)
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobMfgParts.jobId = S_Job.recId
- E_JobMfgParts.unitIdOfBom = T_Unit.recId
- E_JobMfgParts.jobRoutesId = E_JobRoutes.recId
- E_JobMfgParts.materialTypeId = S_MaterialType.recId
- E_JobMfgParts.materialsId = M_Materials.recId
- E_JobMfgParts.parentId = E_JobMfgParts.recId
- E_JobMfgParts.unitIdOfStock = T_Unit.recId
- E_JobMfgParts.subMaterialsId = M_Materials.recId

---

#### 201 工程制作——基本信息——销售部件的参数值对应job这里的 (E_JobParams)

- **业务含义**：工程制作——基本信息——销售部件的参数值对应job这里的
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobParams.jobId = S_Job.recId
- E_JobParams.parametersId = S_Parameters.recId

---

#### 202 流程参数值 (E_JobRouteParams)

- **业务含义**：流程参数值
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobRouteParams.jobId = S_Job.recId
- E_JobRouteParams.jobRoutesId = E_JobRoutes.recId
- E_JobRouteParams.mfgpartId = E_JobMfgParts.recId
- E_JobRouteParams.parametersId = S_Parameters.recId

---

#### 203 制造部件流程表 (E_JobRoutes)

- **业务含义**：制造部件流程表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobRoutes.jobId = S_Job.recId
- E_JobRoutes.mfgpartId = E_JobMfgParts.recId
- E_JobRoutes.processId = T_Process.recId

---

#### 204 E_JobSMTBOM (E_JobSMTBOM)

- **业务含义**：ERP 系统 E_JobSMTBOM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_JobSMTBOM.materialsId = M_Materials.recId
- E_JobSMTBOM.processId = T_Process.recId
- E_JobSMTBOM.jobId = S_Job.recId
- E_JobSMTBOM.suppliersId = M_Suppliers.recId

---

#### 205 E_JobTargetHole (E_JobTargetHole)

- **业务含义**：ERP 系统 E_JobTargetHole 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 206 产品分组（流程模版主表 (E_ProcessLibrary)

- **业务含义**：产品分组（流程模版主表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 207 风险警示表 (E_RiskWarning)

- **业务含义**：风险警示表
- **所属数据库**：思方云2 ERP
-关联关系：
- E_RiskWarning.customerId = S_Customer.recId
- E_RiskWarning.salesPartsId = S_SalesParts.recId
- E_RiskWarning.plantsId = T_Plants.recId

---

#### 208 大料信息表 (E_SheetInfo)

- **业务含义**：大料信息表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 209 工程制作——叠构 (E_StackUpInfo)

- **业务含义**：工程制作——叠构
- **所属数据库**：思方云2 ERP
-关联关系：
- E_StackUpInfo.jobId = S_Job.grossWeight
- E_StackUpInfo.baseCopperId = S_Conductor.recId
- E_StackUpInfo.botCuId = S_Conductor.recId
- E_StackUpInfo.finishCopperId = S_Conductor.recId
- E_StackUpInfo.materialFamilyId = S_MaterialFamily.recId
- E_StackUpInfo.materialTypeId = S_MaterialType.recId
- E_StackUpInfo.materialId = M_Materials.recId
- E_StackUpInfo.topCuId = S_Conductor.recId

---

#### 210 工具表 (E_ToolName)

- **业务含义**：工具表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.5 销售模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 211 雇员信息 (S_BusinessMan)

- **业务含义**：雇员信息
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 212 S_CAR (S_CAR)

- **业务含义**：ERP 系统 S_CAR 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_CAR.companyId = T_Company.recId
- S_CAR.complainmentId = S_Complainment.recId
- S_CAR.customerId = S_Customer.recId
- S_CAR.jobId = S_Job.recId
- S_CAR.plantId = T_Plants.recId
- S_CAR.salesPartId = S_SalesParts.recId

---

#### 213 纸箱定义 (S_Cartons)

- **业务含义**：纸箱定义
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 214 客诉管理 (S_Complainment)

- **业务含义**：客诉管理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 215 客诉管理审批记录 (S_ComplainmentHistory)

- **业务含义**：客诉管理审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ComplainmentHistory.complainmentId = S_Complainment.recId
- S_ComplainmentHistory.myId = T_User.recId

---

#### 216 S_ComplainmentWF (S_ComplainmentWF)

- **业务含义**：ERP 系统 S_ComplainmentWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 217 铜厚表 (S_Conductor)

- **业务含义**：铜厚表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 218 销售订单合同 (S_Contract)

- **业务含义**：销售订单合同
- **所属数据库**：思方云2 ERP
-关联关系：
- S_Contract.companyId = T_Company.recId
- S_Contract.contractTypeId = S_OrderType.recId
- S_Contract.creatorId = T_User.recId
- S_Contract.currencyId = T_Currency.recId
- S_Contract.customerId = S_Customer.recId
- S_Contract.fobId = T_FOB.recId
- S_Contract.paymentMethodId = T_PaymentMethod.recId
- S_Contract.paymentTermId = T_PaymentTerm.recId
- S_Contract.postRoleId = T_PostRole.recId
- S_Contract.shippingId = T_Shipping.recId

---

#### 219 合同明细 (S_ContractItem)

- **业务含义**：合同明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 220 货币 (S_ContractItem scti)

- **业务含义**：货币
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 221 合同制造明细---额外费用表 (S_ContractItemAddCharge)

- **业务含义**：合同制造明细---额外费用表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemAddCharge.addtionalChargeId = T_ChargeItem.recId
- S_ContractItemAddCharge.contractItemId = S_ContractItem.recId

---

#### 222 合同审核表 (S_ContractItemHistory)

- **业务含义**：合同审核表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemHistory.contractItemId = S_ContractItem.recId
- S_ContractItemHistory.myId = T_User.recId

---

#### 223 销售订单合同明细--修改记录 (S_ContractItemLog)

- **业务含义**：销售订单合同明细--修改记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemLog.contractItemId = S_ContractItem.recId
- S_ContractItemLog.creatorId = T_User.recId
- S_ContractItemLog.destJobId = S_Job.recId
- S_ContractItemLog.destSalePartId = S_SalePart.recId
- S_ContractItemLog.srcJobId = S_Job.recId
- S_ContractItemLog.srcSalePartId = S_SalePart.recId

---

#### 224 订单明细参数 (S_ContractItemParameter)

- **业务含义**：订单明细参数
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemParameter.parametersId = S_Parameters.recId
- S_ContractItemParameter.contractItemId = S_ContractItem.recId

---

#### 225 S_ContractItemProject (S_ContractItemProject)

- **业务含义**：ERP 系统 S_ContractItemProject 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemProject.contractItemId = S_ContractItem.recId
- S_ContractItemProject.plantsId = T_Plants.recId

---

#### 226 S_ContractItemWF (S_ContractItemWF)

- **业务含义**：ERP 系统 S_ContractItemWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractItemWF.contractItemId = S_ContractItem.recId
- S_ContractItemWF.myId = T_User.recId

---

#### 227 材料销售订单（贸易） (S_ContractMaterials)

- **业务含义**：材料销售订单（贸易）
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractMaterials.contractId = S_Contract.recId
- S_ContractMaterials.contractItemId = S_ContractItem.recId
- S_ContractMaterials.materialsId = M_Materials.recId
- S_ContractMaterials.processId = T_Process.recId

---

#### 228 销售订单表 (S_ContractSO)

- **业务含义**：销售订单表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ContractSO.customerId = S_Customer.recId
- S_ContractSO.plantBusinessItemId = F_PlantBusinessItem.recId
- S_ContractSO.supplierId = M_Suppliers.recId

---

#### 229 合同明细 (S_ContractSO scts)

- **业务含义**：合同明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 230 客户管理 (S_Customer)

- **业务含义**：客户管理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 231 客户管理--客户地址 (S_CustomerAddress)

- **业务含义**：客户管理--客户地址
- **所属数据库**：思方云2 ERP
-关联关系：
- S_CustomerAddress.cartonsId = S_Cartons.recId
- S_CustomerAddress.customerId = S_Customer.recId
- S_CustomerAddress.fobId = T_FOB.recId
- S_CustomerAddress.shippingId = T_Shipping.recId

---

#### 232 客户绑定公司 (S_CustomerCompany)

- **业务含义**：客户绑定公司
- **所属数据库**：思方云2 ERP
-关联关系：
- S_CustomerCompany.companyId = T_Company.recId
- S_CustomerCompany.customerId = S_Customer.recId

---

#### 233 客户管理审批记录 (S_CustomerHistory)

- **业务含义**：客户管理审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_CustomerHistory.customerId = S_Customer.recId
- S_CustomerHistory.myId = T_User.recId

---

#### 234 客户审批 (S_CustomerWF)

- **业务含义**：客户审批
- **所属数据库**：思方云2 ERP
-关联关系：
- S_CustomerWF.customerId = S_Customer.recId
- S_CustomerWF.myId = T_User.recId

---

#### 235 费用管理 (S_ExpenseForm)

- **业务含义**：费用管理
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ExpenseForm.companyId = T_Company.recId
- S_ExpenseForm.creatorId = T_User.recId
- S_ExpenseForm.flowTypeId = T_FlowType.recId

---

#### 236 费用管理审批记录 (S_ExpenseFormHistory)

- **业务含义**：费用管理审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ExpenseFormHistory.expenseFormId = S_ExpenseForm.recId
- S_ExpenseFormHistory.myId = T_User.recId

---

#### 237 费用管理明细 (S_ExpenseFormItem)

- **业务含义**：费用管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ExpenseFormItem.currencyId = T_Currency.recId
- S_ExpenseFormItem.customerId = S_Customer.recId
- S_ExpenseFormItem.expenseFormId = S_ExpenseForm.recId
- S_ExpenseFormItem.expenseItemId = S_ExpenseItem.recId

---

#### 238 S_ExpenseFormWF (S_ExpenseFormWF)

- **业务含义**：ERP 系统 S_ExpenseFormWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ExpenseFormWF.expenseFormId = S_ExpenseForm.recId
- S_ExpenseFormWF.myId = T_User.recId

---

#### 239 费用定义 (S_ExpenseItem)

- **业务含义**：费用定义
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 240 成品送检单 (S_FGIIQCRecheck)

- **业务含义**：成品送检单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_FGIIQCRecheck.creatorId = T_User.recId
- S_FGIIQCRecheck.fgiInventoryId = FGI_Inventory.recId
- S_FGIIQCRecheck.inspectPostId = T_PostRole.recId
- S_FGIIQCRecheck.postRoleId = T_PostRole.recId
- S_FGIIQCRecheck.warehouseId = T_Warehouse.recId

---

#### 241 成品送检单明细 (S_FGIIQCRecheckItem)

- **业务含义**：成品送检单明细
- **所属数据库**：思方云2 ERP
-关联关系：
- S_FGIIQCRecheckItem.fgiInventoryId = FGI_Inventory.recId
- S_FGIIQCRecheckItem.fgiSubmissionId = S_FGIIQCRecheck.recId

---

#### 242 产品型号  生产部件 (S_Job)

- **业务含义**：产品型号  生产部件
- **所属数据库**：思方云2 ERP
-关联关系：
- S_Job.assignedUserId = T_User.recId
- S_Job.companyId = T_Company.recId
- S_Job.creatorId = T_User.recId
- S_Job.deliveryUnitId = T_Unit.recId
- S_Job.flowTypeId = T_FlowType.recId
- S_Job.postRoleId = T_PostRole.recId
- S_Job.productGroupId = S_ProductGroup.recId
- S_Job.partId = S_SalesParts.recId
- S_Job.scenaroId = S_MaterialTypeCombination.recId
- S_Job.customerId = S_Customer.recId
- S_Job.saleProjectId = S_SaleProject.recId
- S_Job.productGradeId = T_Cate.recId
- S_Job.appCategoryId = S_ProductCategory.recId
- S_Job.plantId = T_Plants.recId
- S_Job.endCustomerId = S_Customer.recId
- S_Job.fromprejobid = S_Job.grossWeight

---

#### 243 生产型号审批记录 (S_JobHistory)

- **业务含义**：生产型号审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_JobHistory.myId = T_User.recId
- S_JobHistory.partNumberId = S_Job.grossWeight

---

#### 244 型号连接销售部件 (S_JobLink)

- **业务含义**：型号连接销售部件
- **所属数据库**：思方云2 ERP
-关联关系：
- S_JobLink.jobId = S_Job.grossWeight
- S_JobLink.salesPartsId = S_SalesParts.recId

---

#### 245 S_JobPrjLink (S_JobPrjLink)

- **业务含义**：ERP 系统 S_JobPrjLink 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_JobPrjLink.jobId = S_Job.grossWeight
- S_JobPrjLink.projectCombinationId = S_ProjectCombination.recId

---

#### 246 生产编号审批 (S_JobWF)

- **业务含义**：生产编号审批
- **所属数据库**：思方云2 ERP
-关联关系：
- S_JobWF.myId = T_User.recId
- S_JobWF.partNumberId = S_Job.grossWeight

---

#### 247 层信息 (S_LayerType)

- **业务含义**：层信息
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 248 厂商型号 (S_MaterialFamily)

- **业务含义**：厂商型号
- **所属数据库**：思方云2 ERP
-关联关系：
- S_MaterialFamily.materialTypeId = S_MaterialType.recId
- S_MaterialFamily.suppliersId = M_Suppliers.recId

---

#### 249 物料类型 (S_MaterialType)

- **业务含义**：物料类型
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 250 材料类型组合 (S_MaterialTypeCombination)

- **业务含义**：材料类型组合
- **所属数据库**：思方云2 ERP
-关联关系：
- S_MaterialTypeCombination.coreId = S_MaterialFamily.recId
- S_MaterialTypeCombination.prePregid = S_MaterialFamily.recId

---

#### 251 订单类型 (S_OrderType)

- **业务含义**：订单类型
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 252 外协采购单 (S_OS_PO)

- **业务含义**：外协采购单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PO.creatorId = T_User.recId
- S_OS_PO.currencyId = T_Currency.recId
- S_OS_PO.flowTypeId = T_FlowType.recId
- S_OS_PO.os_PlantId = T_Plants.recId
- S_OS_PO.paymentMethodId = T_PaymentMethod.recId
- S_OS_PO.paymentTermId = T_PaymentTerm.recId
- S_OS_PO.plantsId = T_Plants.recId
- S_OS_PO.postRoleId = T_PostRole.recId
- S_OS_PO.suppliersId = M_Suppliers.recId

---

#### 253 外协采购单审批记录 (S_OS_POHistory)

- **业务含义**：外协采购单审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_POHistory.myId = T_User.recId
- S_OS_POHistory.os_PO_Id = S_OS_PO.recId

---

#### 254 外协采购明细单 (S_OS_POItem)

- **业务含义**：外协采购明细单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_POItem.os_PRItemId = S_OS_PRItem.recId
- S_OS_POItem.contractItemId = S_ContractItem.recId
- S_OS_POItem.currencyId = T_Currency.recId
- S_OS_POItem.jobId = S_Job.grossWeight
- S_OS_POItem.mfgPartId = E_JobMfgParts.recId
- S_OS_POItem.os_PO_Id = S_OS_PO.recId
- S_OS_POItem.salesPartId = S_SalesParts.recId
- S_OS_POItem.subcontractTypeId = T_SubcontractType.recId
- S_OS_POItem.unitId = T_Unit.recId

---

#### 255 外发采购明细更改表 (S_OS_POItemAddCharge)

- **业务含义**：外发采购明细更改表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_POItemAddCharge.chargeItemId = T_ChargeItem.recId
- S_OS_POItemAddCharge.os_POItemId = S_OS_POItem.recId

---

#### 256 外协采购单审批 (S_OS_POWF)

- **业务含义**：外协采购单审批
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_POWF.myId = T_User.recId
- S_OS_POWF.os_PO_Id = S_OS_PO.recId

---

#### 257 外协请购单 (S_OS_PR)

- **业务含义**：外协请购单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PR.creatorId = T_User.recId
- S_OS_PR.currencyId = T_Currency.recId
- S_OS_PR.flowTypeId = T_FlowType.recId
- S_OS_PR.os_PlantId = T_Plants.recId
- S_OS_PR.plantsId = T_Plants.recId
- S_OS_PR.postRoleId = T_PostRole.recId
- S_OS_PR.suppliersId = M_Suppliers.recId

---

#### 258 外协请购单审批记录 (S_OS_PRHistory)

- **业务含义**：外协请购单审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PRHistory.myId = T_User.recId
- S_OS_PRHistory.os_PR_Id = S_OS_PR.recId

---

#### 259 外协请购明细单 (S_OS_PRItem)

- **业务含义**：外协请购明细单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PRItem.contractSOId = S_ContractSO.recId
- S_OS_PRItem.contractItemId = S_ContractItem.recId
- S_OS_PRItem.currencyId = T_Currency.recId
- S_OS_PRItem.jobId = S_Job.grossWeight
- S_OS_PRItem.mfgPartId = E_JobMfgParts.recId
- S_OS_PRItem.os_PR_Id = S_OS_PR.recId
- S_OS_PRItem.salesPartId = S_SalesParts.recId
- S_OS_PRItem.subcontractTypeId = T_SubcontractType.recId
- S_OS_PRItem.unitId = T_Unit.recId

---

#### 260 外协请购明细单修改记录 (S_OS_PRItemAddCharge)

- **业务含义**：外协请购明细单修改记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PRItemAddCharge.chargeItemId = T_ChargeItem.recId
- S_OS_PRItemAddCharge.os_PRItemId = S_OS_PRItem.recId

---

#### 261 S_OS_PRWF (S_OS_PRWF)

- **业务含义**：ERP 系统 S_OS_PRWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_PRWF.myId = T_User.recId
- S_OS_PRWF.os_PR_Id = S_OS_PR.recId

---

#### 262 外协装运 (S_OS_Shipment)

- **业务含义**：外协装运
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_Shipment.plantsId = T_Plants.recId
- S_OS_Shipment.postRoleId = T_PostRole.recId
- S_OS_Shipment.suppliersId = M_Suppliers.recId
- S_OS_Shipment.userId = T_User.recId

---

#### 263 外协装运明细 (S_OS_ShipmentItem)

- **业务含义**：外协装运明细
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OS_ShipmentItem.os_poItemId = S_OS_POItem.recId
- S_OS_ShipmentItem.jobId = S_Job.grossWeight
- S_OS_ShipmentItem.mfgPartId = E_JobMfgParts.recId
- S_OS_ShipmentItem.os_ShipmentId = S_OS_Shipment.recId

---

#### 264 外协采购工单表 (S_OSWO)

- **业务含义**：外协采购工单表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OSWO.poItemId = S_OS_POItem.recId
- S_OSWO.prItemId = S_OS_PRItem.recId
- S_OSWO.moRouteId = P_MORoute.recId
- S_OSWO.woId = P_WO.recId

---

#### 265 外协接收 (S_OSWOReceipt)

- **业务含义**：外协接收
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OSWOReceipt.fgiReceiptId = FGI_Receipt.recId
- S_OSWOReceipt.os_poItemId = S_OS_POItem.recId
- S_OSWOReceipt.oswoId = S_OSWO.recId

---

#### 266 外协采购分配工单表 (S_OSWOSend)

- **业务含义**：外协采购分配工单表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OSWOSend.iqcId = FGI_IQC.recId
- S_OSWOSend.oswoId = S_OSWO.recId

---

#### 267 外协采购工单装运表 (S_OSWOShipment)

- **业务含义**：外协采购工单装运表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_OSWOShipment.shipmentItemId = S_OS_ShipmentItem.recId
- S_OSWOShipment.oswoId = S_OSWO.recId

---

#### 268 销售数据--参数管理 (S_Parameters)

- **业务含义**：销售数据--参数管理
- **所属数据库**：思方云2 ERP
-关联关系：
- S_Parameters.parametersGroupId = S_ParametersGroup.recId

---

#### 269 销售数据--参数分组 (S_ParametersGroup)

- **业务含义**：销售数据--参数分组
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 270 客户信息-评审-右侧的参数 (S_ParameterValue)

- **业务含义**：客户信息-评审-右侧的参数
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 271 销售数据--产品分类 (S_ProductCategory)

- **业务含义**：销售数据--产品分类
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 272 销售数据--产品分类--公司 (S_ProductCategoryCompany)

- **业务含义**：销售数据--产品分类--公司
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 273 销售数据--产品分组 (S_ProductGroup)

- **业务含义**：销售数据--产品分组
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ProductGroup.inspectGroupId = T_InspectGroup.recId
- S_ProductGroup.productCategoryId = S_ProductCategory.recId
- S_ProductGroup.saleProjectId = S_SaleProject.recId

---

#### 274 销售数据--产品分组--公司 (S_ProductGroupCompany)

- **业务含义**：销售数据--产品分组--公司
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 275 销售数据--产品分组-参数管理 (S_ProductGroupSpec)

- **业务含义**：销售数据--产品分组-参数管理
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ProductGroupSpec.parametersId = S_Parameters.recId
- S_ProductGroupSpec.productGroupId = S_ProductGroup.recId

---

#### 276 销售数据--项目组合 (S_ProjectCombination)

- **业务含义**：销售数据--项目组合
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ProjectCombination.parentId = S_ProjectCombination.recId
- S_ProjectCombination.plantsId = T_Plants.recId
- S_ProjectCombination.postRoleId = T_PostRole.recId
- S_ProjectCombination.saleProjectId = S_SaleProject.recId

---

#### 277 报价单快速报价结果 (S_QuickQuoteResult)

- **业务含义**：报价单快速报价结果
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 278 报价类别 (S_QuoteCategory)

- **业务含义**：报价类别
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 279 报价分组 (S_QuoteGroup)

- **业务含义**：报价分组
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 280 报价参数 (S_QuoteParameter)

- **业务含义**：报价参数
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 281 客诉管理--扣款明细 (S_ReturnSO)

- **业务含义**：客诉管理--扣款明细
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ReturnSO.contractId = S_Contract.recId
- S_ReturnSO.contractItemId = S_ContractItem.recId
- S_ReturnSO.contractSOId = S_ContractSO.recId
- S_ReturnSO.creditMemoId = F_AR_CreditMemo.recId
- S_ReturnSO.customerId = S_Customer.recId
- S_ReturnSO.supplierId = M_Suppliers.recId
- S_ReturnSO.complainmentId = S_Complainment.recId
- S_ReturnSO.currencyId = T_Currency.recId
- S_ReturnSO.fromId = T_Plants.recId
- S_ReturnSO.providerId = T_Plants.recId
- S_ReturnSO.toId = T_Plants.recId
- S_ReturnSO.soReconcileId = F_AR_SOReconcile.recId
- S_ReturnSO.invoiceId = F_AR_Invoice.recId

---

#### 282 报价单 (S_Rfq)

- **业务含义**：报价单
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 283 报价单额外费用 (S_RfqAddCharge)

- **业务含义**：报价单额外费用
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 284 报价单审批历史 (S_RfqHistory)

- **业务含义**：报价单审批历史
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 285 报价单参数 (S_RfqParameter)

- **业务含义**：报价单参数
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 286 报价单审批 (S_RfqWF)

- **业务含义**：报价单审批
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 287 S_Rpt_Member (S_Rpt_Member)

- **业务含义**：ERP 系统 S_Rpt_Member 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_Rpt_Member.parentId = S_Rpt_SalesRepresentative.recId
- S_Rpt_Member.userId = S_BusinessMan.recId

---

#### 288 S_Rpt_SalesRepresentative (S_Rpt_SalesRepresentative)

- **业务含义**：ERP 系统 S_Rpt_SalesRepresentative 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_Rpt_SalesRepresentative.plantId = T_Plants.recId
- S_Rpt_SalesRepresentative.userId = S_BusinessMan.recId

---

#### 289 销售项目 (S_SaleProject)

- **业务含义**：销售项目
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 290 销售预测 (S_SalesForecast)

- **业务含义**：销售预测
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesForecast.companyId = T_Company.recId
- S_SalesForecast.creatorId = T_User.recId
- S_SalesForecast.currencyId = T_Currency.recId
- S_SalesForecast.customerId = S_Customer.recId
- S_SalesForecast.fobId = T_FOB.recId
- S_SalesForecast.jobId = S_Job.grossWeight
- S_SalesForecast.paymentMethodId = T_PaymentMethod.recId
- S_SalesForecast.paymentTermId = T_PaymentTerm.recId
- S_SalesForecast.postRoleId = T_PostRole.recId
- S_SalesForecast.salesPartId = S_SalesParts.recId
- S_SalesForecast.shippingId = T_Shipping.recId
- S_SalesForecast.unitId = T_Unit.recId

---

#### 291 销售预测审批历史 (S_SalesForecastHistory)

- **业务含义**：销售预测审批历史
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 292 销售预测明细 (S_SalesForecastItem)

- **业务含义**：销售预测明细
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesForecastItem.salesForecastId = S_SalesForecast.recId

---

#### 293 销售预测分单 (S_SalesForecastSplitting)

- **业务含义**：销售预测分单
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 294 销售预测审批 (S_SalesForecastWF)

- **业务含义**：销售预测审批
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 295 销售部件 (S_SalesParts)

- **业务含义**：销售部件
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesParts.salesPartBOMId = S_SalesPartsAdditionalBOM.recId
- S_SalesParts.status = 作废.recId
- S_SalesParts.customerId = S_Customer.recId
- S_SalesParts.productGroupId = S_ProductGroup.recId
- S_SalesParts.projectCombinationId = S_ProjectCombination.recId
- S_SalesParts.appCategoryId = S_ProductCategory.recId
- S_SalesParts.salesUnitId = T_Unit.recId
- S_SalesParts.productGradeId = T_Cate.recId
- S_SalesParts.creatorId = T_User.recId
- S_SalesParts.jobId = S_Job.grossWeight
- S_SalesParts.endCustomerId = S_Customer.recId

---

#### 296 销售部件--AdditionalBOM (S_SalesPartsAdditionalBOM)

- **业务含义**：销售部件--AdditionalBOM
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPartsAdditionalBOM.bomUnitId = T_Unit.recId
- S_SalesPartsAdditionalBOM.materialsId = M_Materials.recId
- S_SalesPartsAdditionalBOM.salesPartsId = S_SalesParts.recId
- S_SalesPartsAdditionalBOM.stockUnitId = T_Unit.recId

---

#### 297 销售部件层信息表 (S_SalesPartsLayers)

- **业务含义**：销售部件层信息表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPartsLayers.materialTyepId = S_MaterialType.recId
- S_SalesPartsLayers.baseCopperId = S_Conductor.recId
- S_SalesPartsLayers.finishCopperId = S_Conductor.recId
- S_SalesPartsLayers.salesPartsId = S_SalesParts.recId

---

#### 298 销售部件对应产品分组参数值 (S_SalesPartsParameter)

- **业务含义**：销售部件对应产品分组参数值
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPartsParameter.parametersId = S_Parameters.recId
- S_SalesPartsParameter.salesPartsId = S_SalesParts.recId

---

#### 299 销售部件对应套板信息 (S_SalesPartsSets)

- **业务含义**：销售部件对应套板信息
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPartsSets.salesPartsId = S_SalesParts.recId

---

#### 300 销售部件对应PCBA材料单 (S_SalesPartsSMTBOM)

- **业务含义**：销售部件对应PCBA材料单
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPartsSMTBOM.custUnitId = T_Unit.recId
- S_SalesPartsSMTBOM.materialsId = M_Materials.recId
- S_SalesPartsSMTBOM.processId = T_Process.recId
- S_SalesPartsSMTBOM.salesPartsId = S_SalesParts.recId
- S_SalesPartsSMTBOM.suppliersId = M_Suppliers.recId

---

#### 301 销售订单更改记录 (S_SalesPlanReview)

- **业务含义**：销售订单更改记录
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SalesPlanReview.contractItemId = S_ContractItem.recId

---

#### 302 撤销出货表 (S_ShipmentRevoke)

- **业务含义**：撤销出货表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_ShipmentRevoke.creatorId = T_User.recId
- S_ShipmentRevoke.packingSlipItemId = FGI_PackingSlipItem.recId
- S_ShipmentRevoke.checkorId = T_User.recId
- S_ShipmentRevoke.customerId = S_Customer.recId

---

#### 303 订单装运表 (S_SODayShipment)

- **业务含义**：订单装运表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_SODayShipment.plantsId = T_Plants.recId

---

#### 304 备货冲销记录 (S_SOMatWriteOff)

- **业务含义**：备货冲销记录
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 305 成品盘点表 (S_StockCheck)

- **业务含义**：成品盘点表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_StockCheck.creatorId = T_User.recId
- S_StockCheck.fiscalPeriodId = T_FiscalPeriod.recId
- S_StockCheck.postRoleId = T_PostRole.recId
- S_StockCheck.warehouseId = T_Warehouse.recId

---

#### 306 成品盘点明细表 (S_StockCheckItem)

- **业务含义**：成品盘点明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_StockCheckItem.fgiInventoryId = FGI_Inventory.recId
- S_StockCheckItem.inventoryCheckReasonId = T_InventoryCheckReason.recId
- S_StockCheckItem.stockCheckId = S_StockCheck.recId

---

#### 307 工作计划表 (S_WorkPlan)

- **业务含义**：工作计划表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_WorkPlan.businessManId = S_BusinessMan.recId
- S_WorkPlan.companyId = T_Company.recId
- S_WorkPlan.creatorId = T_User.recId
- S_WorkPlan.flowTypeId = T_FlowType.recId

---

#### 308 工作计划明细表 (S_WorkPlanItem)

- **业务含义**：工作计划明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_WorkPlanItem.customerId = S_Customer.recId
- S_WorkPlanItem.workPlanId = S_WorkPlan.recId

---

#### 309 工作计划审批记录表 (S_WorkPlantHistory)

- **业务含义**：工作计划审批记录表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_WorkPlantHistory.myId = T_User.recId
- S_WorkPlantHistory.workPlanId = S_WorkPlan.recId

---

#### 310 S_WorkPlantWF (S_WorkPlantWF)

- **业务含义**：ERP 系统 S_WorkPlantWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- S_WorkPlantWF.myId = T_User.recId
- S_WorkPlantWF.workPlanId = S_WorkPlan.recId

---

### 2.6 生产模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 311 BOM领料批次 (P_BOMBatching)

- **业务含义**：BOM领料批次
- **所属数据库**：思方云2 ERP
-关联关系：
- P_BOMBatching.bomPicklistItemId = M_BOMPicklistItem.qtyRemaining
- P_BOMBatching.mfgPartId = E_JobMfgParts.recId
- P_BOMBatching.materialsId = M_Materials.recId
- P_BOMBatching.moId = P_MO.recId
- P_BOMBatching.processId = T_Process.recId
- P_BOMBatching.stockUnitId = T_Unit.recId
- P_BOMBatching.warehouseId = T_Warehouse.recId
- P_BOMBatching.stepsId = T_Steps.recId
- P_BOMBatching.contractItemId = S_ContractItem.recId
- P_BOMBatching.materialsCostByPlantId = M_MaterialsCostByPlant.recId

---

#### 312 OCN\ECN管理 (P_ECN)

- **业务含义**：OCN\ECN管理
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ECN.companyId = T_Company.recId
- P_ECN.contractSOId = S_ContractSO.recId
- P_ECN.creatorId = T_User.recId
- P_ECN.customerId = S_Customer.recId
- P_ECN.departmentId = T_Department.recId
- P_ECN.flowTypeId = T_FlowType.recId
- P_ECN.jobId = S_Job.recId
- P_ECN.miUserId = T_User.recId
- P_ECN.ocnUserId = T_User.recId
- P_ECN.onlineUserId = T_User.recId
- P_ECN.payforUserId = T_User.recId
- P_ECN.postRoleId = T_PostRole.recId
- P_ECN.salesPartsId = S_SalesParts.recId
- P_ECN.stockUserId = T_User.recId
- P_ECN.toolUserId = T_User.recId

---

#### 313 OCN\ECN管理-审批记录 (P_ECNHistory)

- **业务含义**：OCN\ECN管理-审批记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ECNHistory.ecnId = P_ECN.recId
- P_ECNHistory.myId = T_User.recId

---

#### 314 OCN\ECN管理-工具-工具类型 (P_ECNLog)

- **业务含义**：OCN\ECN管理-工具-工具类型
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ECNLog.ecnId = P_ECN.recId
- P_ECNLog.creatorId = T_User.recId

---

#### 315 OCN\ECN审核 (P_ECNTool)

- **业务含义**：OCN\ECN审核
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 316 OCN/ECN审批流程 (P_ECNWF)

- **业务含义**：OCN/ECN审批流程
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ECNWF.ecnId = P_ECN.recId
- P_ECNWF.myId = T_User.recId

---

#### 317 MRB检查 (P_Inspection)

- **业务含义**：MRB检查
- **所属数据库**：思方云2 ERP
-关联关系：
- P_Inspection.mrbRequisitionId = P_MRBRequisition.recId
- P_Inspection.prd_MO_RoutesId = P_MORoute.recId
- P_Inspection.creatorId = T_User.recId
- P_Inspection.defectId = T_Defect.recId
- P_Inspection.inspectItemsId = T_InspectItems.recId
- P_Inspection.processId = T_Process.recId
- P_Inspection.unitId = T_Unit.recId
- P_Inspection.woId = P_WO.recId
- P_Inspection.suppliersId = M_Suppliers.recId

---

#### 318 P_IPQC (P_IPQC)

- **业务含义**：ERP 系统 P_IPQC 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 319 P_IPQCItem (P_IPQCItem)

- **业务含义**：ERP 系统 P_IPQCItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 320 合拼单 (P_MergeOrder)

- **业务含义**：合拼单
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 321 合拼明细表 (P_MergeOrderSO)

- **业务含义**：合拼明细表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 322 部件表 (P_MfgPartsInv)

- **业务含义**：部件表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MfgPartsInv.woId = P_WO.recId
- P_MfgPartsInv.userId = T_User.recId
- P_MfgPartsInv.wipWarehouseId = T_Warehouse.recId
- P_MfgPartsInv.stepId = T_Step.recId
- P_MfgPartsInv.pwoId = P_WO.recId

---

#### 323 部件使用情况表 (P_MfgPartsIssue)

- **业务含义**：部件使用情况表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MfgPartsIssue.woId = P_WO.recId
- P_MfgPartsIssue.mfgPartsInvId = P_MfgPartsInv.recId
- P_MfgPartsIssue.userId = T_User.recId

---

#### 324 部件升级记录 (P_MfgUpRevLog)

- **业务含义**：部件升级记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MfgUpRevLog.creatorId = T_User.recId
- P_MfgUpRevLog.desJobId = S_Job.recId
- P_MfgUpRevLog.desJobMfgPartId = E_JobMfgParts.recId
- P_MfgUpRevLog.oriJobId = S_Job.recId
- P_MfgUpRevLog.oriJobMfgPartId = E_JobMfgParts.recId
- P_MfgUpRevLog.processId = T_Process.recId

---

#### 325 制造订单表 (P_MO)

- **业务含义**：制造订单表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MO.parentId = P_MO.recId
- P_MO.pcsOfPanel_A = 制造部件.recId
- P_MO.creatorId = T_User.recId
- P_MO.jobId = S_Job.recId
- P_MO.mfgPartId = E_JobMfgParts.recId
- P_MO.plantsId = T_Plants.recId
- P_MO.postRoleId = T_PostRole.recId
- P_MO.customerId = S_Customer.recId
- P_MO.contractItemId = S_ContractItem.recId
- P_MO.rdProjectId = M_RDProject.recId

---

#### 326 制造订单表中的BOM (P_MOBOM)

- **业务含义**：制造订单表中的BOM
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MOBOM.bomPicklistItemId = M_BOMPicklistItem.qtyRemaining
- P_MOBOM.jobId = S_Job.recId
- P_MOBOM.bomUnitId = T_Unit.recId
- P_MOBOM.mfgPartId = E_JobMfgParts.recId
- P_MOBOM.materialsId = M_Materials.recId
- P_MOBOM.moId = P_MO.recId
- P_MOBOM.processId = T_Process.recId
- P_MOBOM.contractItemId = S_ContractItem.recId

---

#### 327 OCN/ECN工单变更 (P_ModRoute)

- **业务含义**：OCN/ECN工单变更
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 328 OCN/ECN工单变更流程 (P_ModRouteItem)

- **业务含义**：OCN/ECN工单变更流程
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 329 MO修改记录 (P_ModRouteLog)

- **业务含义**：MO修改记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ModRouteLog.creatorId = T_User.recId
- P_ModRouteLog.processId = T_Process.recId
- P_ModRouteLog.stepsId = T_Steps.recId
- P_ModRouteLog.woId = P_WO.recId

---

#### 330 OCN/ECN工单变更参数 (P_ModRouteParams)

- **业务含义**：OCN/ECN工单变更参数
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 331 OCN/ECN工单变更工单列表 (P_ModRouteWO)

- **业务含义**：OCN/ECN工单变更工单列表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 332 制造订单中的制造部件 (P_MOMfgPart)

- **业务含义**：制造订单中的制造部件
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MOMfgPart.mfgPartId = E_JobMfgParts.recId
- P_MOMfgPart.moId = P_MO.recId

---

#### 333 制造订单中的制造部件参数 (P_MOMfgPartParams)

- **业务含义**：制造订单中的制造部件参数
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MOMfgPartParams.mfgPartId = E_JobMfgParts.recId
- P_MOMfgPartParams.parametersId = S_Parameters.recId

---

#### 334 制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表 (P_MORoute)

- **业务含义**：制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MORoute.moId = P_MO.recId
- P_MORoute.qty_Array_INTRANSIT = 测试为转出数量.recId
- P_MORoute.qty_PCS_INTRANSIT = 测试为转出数量.recId
- P_MORoute.qty_PNL_INTRANSIT = 测试为转出数量.recId
- P_MORoute.reworkId = P_ReWork.recId
- P_MORoute.reworkRouteId = P_ReworkRoute.recId
- P_MORoute.stepId = T_Steps.recId
- P_MORoute.mfgPartId = E_JobMfgParts.recId
- P_MORoute.plantsId = T_Plants.recId
- P_MORoute.processId = T_Process.recId
- P_MORoute.unitId = T_Unit.recId
- P_MORoute.woId = P_WO.recId

---

#### 335 工单流程参数 (P_MORouteParams)

- **业务含义**：工单流程参数
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MORouteParams.moId = P_MO.recId
- P_MORouteParams.routeId = P_MORoute.recId
- P_MORouteParams.parametersId = S_Parameters.recId

---

#### 336 制造订单\销售订单 (P_MOSO)

- **业务含义**：制造订单\销售订单
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MOSO.contractSOId = S_ContractSO.recId
- P_MOSO.jobId = S_Job.recId
- P_MOSO.moId = P_MO.recId

---

#### 337 MRB送检申请 (P_MRBRequisition)

- **业务含义**：MRB送检申请
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MRBRequisition.fixedById = T_User.recId
- P_MRBRequisition.prd_MO_RoutesId = P_MORoute.recId
- P_MRBRequisition.sendById = T_User.recId
- P_MRBRequisition.unitId = T_Unit.recId
- P_MRBRequisition.woId = P_WO.recId

---

#### 338 MRP物资需求计划 (P_MRP)

- **业务含义**：MRP物资需求计划
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MRP.companyId = T_Company.recId
- P_MRP.creatorId = T_User.recId
- P_MRP.plantsId = T_Plants.recId
- P_MRP.postRoleId = T_PostRole.recId

---

#### 339 P_MRPREQ (P_MRPREQ)

- **业务含义**：ERP 系统 P_MRPREQ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MRPREQ.materialsId = M_Materials.recId
- P_MRPREQ.mrpId = P_MRP.recId

---

#### 340 P_MRPREQItem (P_MRPREQItem)

- **业务含义**：ERP 系统 P_MRPREQItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_MRPREQItem.bomUnitId = T_Unit.recId
- P_MRPREQItem.materialsId = M_Materials.recId
- P_MRPREQItem.mrpreqId = P_MRPREQ.recId
- P_MRPREQItem.stepsId = T_Steps.recId

---

#### 341 工单过数记录表 (P_OutPut)

- **业务含义**：工单过数记录表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_OutPut.moId = P_MO.recId
- P_OutPut.nextOutPutRouteId = P_OutPutRoute(无效).recId
- P_OutPut.nextPlantId = T_Plants.recId
- P_OutPut.nextProcessId = T_Process.recId
- P_OutPut.prd_MO_RoutesId = P_MORoute.recId
- P_OutPut.reworkId = P_ReWork  返工表.recId
- P_OutPut.stepId = T_Step.recId
- P_OutPut.creatorId = T_User.recId
- P_OutPut.equipmentId = EQ_Equipments.recId
- P_OutPut.outputManId = S_BusinessMan.recId

---

#### 342 P_PQE (P_PQE)

- **业务含义**：ERP 系统 P_PQE 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 343 P_RetrospectTool (P_RetrospectTool)

- **业务含义**：ERP 系统 P_RetrospectTool 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_RetrospectTool.moRouteId = P_MORoute.recId
- P_RetrospectTool.toolId = P_Tools.recId

---

#### 344 返工表 (P_ReWork)

- **业务含义**：返工表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ReWork.prd_MO_RoutesId = P_MORoute.recId
- P_ReWork.creatorId = T_User.recId
- P_ReWork.unitId = T_Unit.recId
- P_ReWork.woId = P_WO.recId
- P_ReWork.employeeId = T_User.recId
- P_ReWork.tempProcessId = T_Process.recId
- P_ReWork.tempStepId = T_Step.recId

---

#### 345 P_ReWorkApplication (P_ReWorkApplication)

- **业务含义**：ERP 系统 P_ReWorkApplication 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ReWorkApplication.plantsId = T_Plants.recId
- P_ReWorkApplication.prd_MO_RoutesId = P_MORoute.recId
- P_ReWorkApplication.woid = P_WO.recId
- P_ReWorkApplication.stepId = T_Steps.recId
- P_ReWorkApplication.processId = T_Process.recId

---

#### 346 P_ReWorkApplicationProcess (P_ReWorkApplicationProcess)

- **业务含义**：ERP 系统 P_ReWorkApplicationProcess 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 347 订单BOM表 (P_SOBOM)

- **业务含义**：订单BOM表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_SOBOM.jobId = S_Job.recId
- P_SOBOM.bomUnitId = T_Unit.recId
- P_SOBOM.contractItemId = S_ContractItem.recId
- P_SOBOM.mfgPartId = E_JobMfgParts.recId
- P_SOBOM.materialsId = M_Materials.recId
- P_SOBOM.processId = T_Process.recId

---

#### 348 工单拆分记录 (P_SplitWOLog)

- **业务含义**：工单拆分记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_SplitWOLog.stepId = T_Step.recId
- P_SplitWOLog.creatorId = T_User.recId
- P_SplitWOLog.processId = T_Process.recId
- P_SplitWOLog.woId = P_WO.recId

---

#### 349 工具申请单 (P_ToolApply)

- **业务含义**：工具申请单
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolApply.contractSOId = S_ContractSO.recId
- P_ToolApply.creatorId = T_User.recId
- P_ToolApply.flowTypeId = T_FlowType.recId
- P_ToolApply.mfgPartId = E_JobMfgParts.recId
- P_ToolApply.locationId = T_Location.recId
- P_ToolApply.plantsId = T_Plants.recId
- P_ToolApply.postRoleId = T_PostRole.recId
- P_ToolApply.toolTypeId = P_ToolTypes.recId

---

#### 350 工具申请审批流程记录 (P_ToolApplyHistory)

- **业务含义**：工具申请审批流程记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolApplyHistory.myId = T_User.recId
- P_ToolApplyHistory.toolApplyId = P_ToolApply.recId

---

#### 351 P_ToolApplyWF (P_ToolApplyWF)

- **业务含义**：ERP 系统 P_ToolApplyWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolApplyWF.myId = T_User.recId
- P_ToolApplyWF.toolApplyId = P_ToolApply.recId

---

#### 352 工具发放 (P_ToolIssued)

- **业务含义**：工具发放
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolIssued.creatorId = T_User.recId
- P_ToolIssued.issuedById = T_User.recId
- P_ToolIssued.pickedById = T_User.recId
- P_ToolIssued.plantsId = T_Plants.recId
- P_ToolIssued.postRoleId = T_PostRole.recId
- P_ToolIssued.stepsId = T_Steps.recId
- P_ToolIssued.toolId = P_Tools.recId

---

#### 353 工具退回 (P_ToolReturned)

- **业务含义**：工具退回
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolReturned.creatorId = T_User.recId
- P_ToolReturned.plantsId = T_Plants.recId
- P_ToolReturned.postRoleId = T_PostRole.recId
- P_ToolReturned.receivedById = T_User.recId
- P_ToolReturned.returnById = T_User.recId
- P_ToolReturned.stepsId = T_Steps.recId
- P_ToolReturned.toolId = P_Tools.recId
- P_ToolReturned.toolIssuedId = P_ToolIssued.recId

---

#### 354 工具登记表 (P_Tools)

- **业务含义**：工具登记表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_Tools.creatorId = T_User.recId
- P_Tools.mfgPartId = E_JobMfgParts.recId
- P_Tools.lifeUnitId = T_Unit.recId
- P_Tools.locationId = T_Location.recId
- P_Tools.onholdById = T_User.recId
- P_Tools.plantsId = T_Plants.recId
- P_Tools.postRoleId = T_PostRole.recId
- P_Tools.scrappedById = T_User.recId
- P_Tools.stockUnitId = T_Unit.recId
- P_Tools.toolApplyId = P_ToolApply.recId
- P_Tools.toolTypeId = P_ToolTypes.recId

---

#### 355 工具类型 (P_ToolTypes)

- **业务含义**：工具类型
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolTypes.inspectGroupId = T_InspectGroup.recId
- P_ToolTypes.lifeUnitId = T_Unit.recId
- P_ToolTypes.purchasePostId = T_PostRole.recId
- P_ToolTypes.stockUnitId = T_Unit.recId

---

#### 356 工具类型所在仓库 (P_ToolTypeWarehouse)

- **业务含义**：工具类型所在仓库
- **所属数据库**：思方云2 ERP
-关联关系：
- P_ToolTypeWarehouse.locationId = locationId.recId
- P_ToolTypeWarehouse.toolTypeId = toolTypeId.recId
- P_ToolTypeWarehouse.warehouseId = warehouseId.recId

---

#### 357 P_UpdateLog (P_UpdateLog)

- **业务含义**：ERP 系统 P_UpdateLog 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_UpdateLog.modifyTableRecId = M_Materials.recId

---

#### 358 工作单号 (P_WO)

- **业务含义**：工作单号
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WO.splitRootId = P_SplitWOLog.woId

---

#### 359 工单IQC (P_WOIQC)

- **业务含义**：工单IQC
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOIQC.fgiiqcTestId = FGI_IQC.recId
- P_WOIQC.jobId = S_Job.recId
- P_WOIQC.woId = P_WO.recId

---

#### 360 P_WOProcessBack (P_WOProcessBack)

- **业务含义**：ERP 系统 P_WOProcessBack 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 361 P_WOProcessSend (P_WOProcessSend)

- **业务含义**：ERP 系统 P_WOProcessSend 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOProcessSend.employeeId = S_BusinessMan.recId
- P_WOProcessSend.equipmentId = EQ_Equipments.recId
- P_WOProcessSend.moRouteId = P_MORoute.recId
- P_WOProcessSend.userId = T_User.recId

---

#### 362 P_WOProcessStock (P_WOProcessStock)

- **业务含义**：ERP 系统 P_WOProcessStock 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOProcessStock.employeeId = S_BusinessMan.recId
- P_WOProcessStock.equipmentId = EQ_Equipments.recId
- P_WOProcessStock.moRouteId = P_MORoute.recId

---

#### 363 工单对应销售单 (P_WOSO)

- **业务含义**：工单对应销售单
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOSO.contractSOId = S_ContractSO.recId
- P_WOSO.jobId = S_Job.recId
- P_WOSO.woId = P_WO.recId

---

#### 364 P_WOSplitBatchApplication (P_WOSplitBatchApplication)

- **业务含义**：ERP 系统 P_WOSplitBatchApplication 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOSplitBatchApplication.plantsId = T_Plants.recId
- P_WOSplitBatchApplication.prd_MO_RoutesId = P_MORoute.recId
- P_WOSplitBatchApplication.woid = P_WO.recId
- P_WOSplitBatchApplication.stepId = T_Steps.recId
- P_WOSplitBatchApplication.processId = T_Process.recId

---

#### 365 工单转出记录 (P_WOTransfer)

- **业务含义**：工单转出记录
- **所属数据库**：思方云2 ERP
-关联关系：
- P_WOTransfer.prd_MO_RoutesId = P_MORoute.recId

---

### 2.8 财务模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 366 财务应用-成本核算-成本明细 (F_AccCostWOByPeriod)

- **业务含义**：财务应用-成本核算-成本明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 367 工单成本明细 (F_AccCostWOBySteps)

- **业务含义**：工单成本明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AccCostWOBySteps.periodId = T_FiscalPeriod.recId
- F_AccCostWOBySteps.stepId = T_Steps.recId
- F_AccCostWOBySteps.woId = P_WO.recId
- F_AccCostWOBySteps.processId = T_Process.recId
- F_AccCostWOBySteps.processNumber = 序号.recId

---

#### 368 财务管理-财务数据-科目分组 (F_AccountGroups)

- **业务含义**：财务管理-财务数据-科目分组
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 369 F_AccountProjects (F_AccountProjects)

- **业务含义**：ERP 系统 F_AccountProjects 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 370 科目管理 (F_Accounts)

- **业务含义**：科目管理
- **所属数据库**：思方云2 ERP
-关联关系：
- F_Accounts.periodId = T_FiscalPeriod.recId
- F_Accounts.voucherProjctId = F_VoucherProject.recId
- F_Accounts.accountGroupId = F_AccountGroups.recId
- F_Accounts.companyId = T_Company.recId
- F_Accounts.currencyId = T_Currency.recId
- F_Accounts.parentId = F_Accounts.recId
- F_Accounts.projectCatagoryId = F_ProjectCatagory.recId

---

#### 371 F_AllScrapWOCost (F_AllScrapWOCost)

- **业务含义**：ERP 系统 F_AllScrapWOCost 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 372 供应商扣款 (F_AP_DebitMemo)

- **业务含义**：供应商扣款
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_DebitMemo.returnOrderId = M_ReturnOrder.recId
- F_AP_DebitMemo.companyId = T_Company.recId
- F_AP_DebitMemo.creatorId = T_User.recId
- F_AP_DebitMemo.currencyId = T_Currency.recId
- F_AP_DebitMemo.fiscalPeriodId = T_FiscalPeriod.recId
- F_AP_DebitMemo.plantBusinessId = F_PlantBusiness.recId
- F_AP_DebitMemo.plantBusinessItemId = F_PlantBusinessItem.recId
- F_AP_DebitMemo.plantsId = T_Plants.recId
- F_AP_DebitMemo.postRoleId = T_PostRole.recId
- F_AP_DebitMemo.suppliersId = M_Suppliers.recId
- F_AP_DebitMemo.targetId = T_Plants.recId

---

#### 373 供应商扣款明细 (F_AP_DebitMemoItem)

- **业务含义**：供应商扣款明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_DebitMemoItem.jobId = S_Job.recId
- F_AP_DebitMemoItem.poItemId = M_PurchaseOrderItem.recId
- F_AP_DebitMemoItem.returnOrderItemId = M_ReturnOrderItem.recId
- F_AP_DebitMemoItem.returnSOId = S_ReturnSO.recId
- F_AP_DebitMemoItem.debitMemoId = F_AP_DebitMemo.recId
- F_AP_DebitMemoItem.taxId = T_Tax.recId

---

#### 374 应付账款/付款管理 (F_AP_Disburse)

- **业务含义**：应付账款/付款管理
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_Disburse.sourceId = M_Suppliers.recId
- F_AP_Disburse.accountId = F_Accounts.recId
- F_AP_Disburse.bankAccountsId = F_BankAccounts.recId
- F_AP_Disburse.companyId = T_Company.recId
- F_AP_Disburse.creatorId = T_User.recId
- F_AP_Disburse.currencyId = T_Currency.recId
- F_AP_Disburse.modifyId = T_User.recId
- F_AP_Disburse.postRoleId = T_PostRole.recId
- F_AP_Disburse.flowTypeId = T_FlowType.recId

---

#### 375 应付账款/付款管理明细 (F_AP_DisburseItem)

- **业务含义**：应付账款/付款管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_DisburseItem.disburseId = F_AP_Disburse.recId
- F_AP_DisburseItem.invoiceId = F_AP_Invoice.recId
- F_AP_DisburseItem.soInvoiceId = F_AR_Invoice.recId

---

#### 376 采购发票 (F_AP_Invoice)

- **业务含义**：采购发票
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_Invoice.companyId = T_Company.recId
- F_AP_Invoice.creatorId = T_User.recId
- F_AP_Invoice.currencyId = T_Currency.recId
- F_AP_Invoice.paymentTermId = T_PaymentTerm.recId
- F_AP_Invoice.plantsId = T_Plants.recId
- F_AP_Invoice.postRoleId = T_PostRole.recId
- F_AP_Invoice.suppliersId = M_Suppliers.recId
- F_AP_Invoice.targetId = T_Plants.recId
- F_AP_Invoice.flowTypeId = T_FlowType.recId
- F_AP_Invoice.taxId = T_tax.recId

---

#### 377 采购发票明细 (F_AP_InvoiceItem)

- **业务含义**：采购发票明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_InvoiceItem.contractSOId = S_ContractSo.recId
- F_AP_InvoiceItem.packingSlipItemContractSOId = F_PackingSlipItemContractSO.recId
- F_AP_InvoiceItem.packingSlipItemId = M_MaterialPackingSlipItem.recId
- F_AP_InvoiceItem.poItemId = M_PurchaseOrderItem.recId
- F_AP_InvoiceItem.receiptItemId = M_ReceiptItem.recId
- F_AP_InvoiceItem.reconcileItemId = F_AP_ReconcileItems.recId
- F_AP_InvoiceItem.apInvoiceId = F_AP_Invoice.recId
- F_AP_InvoiceItem.taxId = T_Tax.recId

---

#### 378 采购对账 (F_AP_Reconcile)

- **业务含义**：采购对账
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_Reconcile.companyId = T_Company.recId
- F_AP_Reconcile.creatorId = T_User.recId
- F_AP_Reconcile.currencyId = T_Currency.recId
- F_AP_Reconcile.fiscalPeriodId = T_FiscalPeriod.recId
- F_AP_Reconcile.plantsId = T_Plants.recId
- F_AP_Reconcile.postRoleId = T_PostRole.recId
- F_AP_Reconcile.suppliersId = M_Suppliers.recId
- F_AP_Reconcile.flowTypeId = T_flowType.recId

---

#### 379 采购对账明细 (F_AP_ReconcileItems)

- **业务含义**：采购对账明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AP_ReconcileItems.contractSOId = S_ContractSO.recId
- F_AP_ReconcileItems.packingSlipItemContractSOId = F_PackingSlipItemContractSO.recId
- F_AP_ReconcileItems.packingSlipItemId = FGI_PackingSlipItem.recId
- F_AP_ReconcileItems.receiptItemId = M_ReceiptItem.recId
- F_AP_ReconcileItems.reconcileId = F_AP_Reconcile.recId
- F_AP_ReconcileItems.taxId = T_Tax.recId

---

#### 380 客户扣款（对账和发票） (F_AR_CreditMemo)

- **业务含义**：客户扣款（对账和发票）
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_CreditMemo.invoiceId = F_AP_Invoice.recId
- F_AR_CreditMemo.reconcileId = F_AR_SOReconcile.recId
- F_AR_CreditMemo.anlysisUserId = T_User.recId
- F_AR_CreditMemo.companyId = T_Company.recId
- F_AR_CreditMemo.creatorId = T_User.recId
- F_AR_CreditMemo.currencyId = T_Currency.recId
- F_AR_CreditMemo.customerId = S_Customer.recId
- F_AR_CreditMemo.fiscalPeriodId = T_FiscalPeriod.recId
- F_AR_CreditMemo.plantBusinessId = F_PlantBusiness.recId
- F_AR_CreditMemo.plantBusinessItemId = F_PlantBusinessItem.recId
- F_AR_CreditMemo.plantsId = T_Plants.recId
- F_AR_CreditMemo.postRoleId = T_PostRole.recId
- F_AR_CreditMemo.targetId = T_Plants.recId
- F_AR_CreditMemo.flowTypeId = T_FlowType.recId
- F_AR_CreditMemo.taxId = T_Tax.recId
- F_AR_CreditMemo.deductionId = T_ModuleType.recId

---

#### 381 客户扣款明细 (F_AR_CreditMemoItem)

- **业务含义**：客户扣款明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_CreditMemoItem.returnSOId = S_ReturnSO.recId
- F_AR_CreditMemoItem.creditMemoId = F_AR_CreditMemo.recId

---

#### 382 财务管理-财务应用-应收账款-销售发票 (F_AR_Invoice)

- **业务含义**：财务管理-财务应用-应收账款-销售发票
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_Invoice.companyId = T_Company.recId
- F_AR_Invoice.creatorId = T_User.recId
- F_AR_Invoice.currencyId = T_Currency.recId
- F_AR_Invoice.customerId = S_Customer.recId
- F_AR_Invoice.paymentTermId = T_PaymentTerm.recId
- F_AR_Invoice.plantsId = T_Plants.recId
- F_AR_Invoice.postRoleId = T_PostRole.recId
- F_AR_Invoice.targetId = T_Plants.recId
- F_AR_Invoice.flowTypeId = T_FlowType.recId
- F_AR_Invoice.taxId = T_Tax.recId

---

#### 383 销售发票明细 (F_AR_InvoiceItem)

- **业务含义**：销售发票明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_InvoiceItem.jobId = S_JOB.recId
- F_AR_InvoiceItem.soReconcileItemId = F_AR_SOReconcileItems.recId
- F_AR_InvoiceItem.contractSOId = S_ContractSO.recId
- F_AR_InvoiceItem.invoiceId = F_AR_Invoice.recId
- F_AR_InvoiceItem.packingSlipItemId = FGI_PackingSlipItem.recId
- F_AR_InvoiceItem.taxId = T_Tax.recId

---

#### 384 收款管理 (F_AR_Receivable)

- **业务含义**：收款管理
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_Receivable.sourceType = S_Customer.recId
- F_AR_Receivable.accountId = F_Accounts.recId
- F_AR_Receivable.bankAccountsId = F_BankAccounts.recId
- F_AR_Receivable.companyId = T_Company.recId
- F_AR_Receivable.creatorId = T_User.recId
- F_AR_Receivable.currencyId = T_Currency.recId
- F_AR_Receivable.modifyId = T_User.recId
- F_AR_Receivable.postRoleId = T_PostRole.recId
- F_AR_Receivable.flowTypeId = T_FlowType.recId

---

#### 385 收款管理明细 (F_AR_ReceivableItem)

- **业务含义**：收款管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_ReceivableItem.invoiceId = F_AR_Invoice.recId
- F_AR_ReceivableItem.receivableId = F_AR_Receivable.recId
- F_AR_ReceivableItem.poInvoiceId = F_AP_Invoice.recId

---

#### 386 财务管理-财务应用-应收账款-销售对账 (F_AR_SOReconcile)

- **业务含义**：财务管理-财务应用-应收账款-销售对账
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_SOReconcile.companyId = T_Company.recId
- F_AR_SOReconcile.creatorId = T_User.recId
- F_AR_SOReconcile.currencyId = T_Currency.recId
- F_AR_SOReconcile.customerId = S_Customer.recId
- F_AR_SOReconcile.fiscalPeriodId = T_FiscalPeriod.recId
- F_AR_SOReconcile.plantsId = T_Plants.recId
- F_AR_SOReconcile.postRoleId = T_PostRole.recId
- F_AR_SOReconcile.flowTypeId = T_flowType.recId

---

#### 387 销售对账明细 (F_AR_SOReconcileItems)

- **业务含义**：销售对账明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AR_SOReconcileItems.contractSOId = S_ContractSO.recId
- F_AR_SOReconcileItems.packingSlipItemId = FGI_PackingSlipItem.recId
- F_AR_SOReconcileItems.soReconcileId = F_AR_SOReconcile.recId
- F_AR_SOReconcileItems.taxId = T_Tax.recId

---

#### 388 财务管理-资产管理-资产类别明细表 (F_AssetCategoryItem)

- **业务含义**：财务管理-资产管理-资产类别明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AssetCategoryItem.assetAccountId = F_Accounts.recId
- F_AssetCategoryItem.assetCategoryId = F_AssetCategorys.recId
- F_AssetCategoryItem.depAddAcountId = F_Accounts.recId
- F_AssetCategoryItem.depDisposalAccountId = F_Accounts.recId
- F_AssetCategoryItem.depExpenseAccountId = F_Accounts.recId
- F_AssetCategoryItem.plantsId = T_Plants.recId

---

#### 389 财务管理-资产管理-资产类别 (F_AssetCategorys)

- **业务含义**：财务管理-资产管理-资产类别
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AssetCategorys.assetAccountId = F_Accounts.recId
- F_AssetCategorys.depAddAcountId = F_Accounts.recId
- F_AssetCategorys.depExpenseAccountId = F_Accounts.recId

---

#### 390 资产变动管理 (F_AssetChange)

- **业务含义**：资产变动管理
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AssetChange.assetChangeWayId = F_AssetChangeWays.recId
- F_AssetChange.companyId = T_Company.recId
- F_AssetChange.creatorId = T_User.recId
- F_AssetChange.fixedAssetId = F_FixedAssets.recId
- F_AssetChange.flowTypeId = T_FlowType.recId
- F_AssetChange.postRoleId = T_PostRole.recId

---

#### 391 F_AssetChangeHistory (F_AssetChangeHistory)

- **业务含义**：ERP 系统 F_AssetChangeHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 392 资产变动管理明细 (F_AssetChangeItem)

- **业务含义**：资产变动管理明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AssetChangeItem.assetChangeId = F_AssetChange.recId

---

#### 393 资产变动方式 (F_AssetChangeWays)

- **业务含义**：资产变动方式
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 394 F_AssetChangeWF (F_AssetChangeWF)

- **业务含义**：ERP 系统 F_AssetChangeWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 395 资产清理 (F_AssetDisposal)

- **业务含义**：资产清理
- **所属数据库**：思方云2 ERP
-关联关系：
- F_AssetDisposal.assetChangeWayId = F_AssetChangeWays.recId
- F_AssetDisposal.companyId = T_Company.recId
- F_AssetDisposal.creatorId = T_User.recId
- F_AssetDisposal.currencyId = T_Currency.recId
- F_AssetDisposal.fixedAssetId = F_FixedAssets.recId
- F_AssetDisposal.postRoleId = T_PostRole.recId

---

#### 396 资产状态 (F_AssetStatus)

- **业务含义**：资产状态
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 397 现金账户 (F_BankAccounts)

- **业务含义**：现金账户
- **所属数据库**：思方云2 ERP
-关联关系：
- F_BankAccounts.ba_accountId = F_Accounts.recId
- F_BankAccounts.bankReconcileSetingId = F_BankReconcileSeting.recId
- F_BankAccounts.companyId = T_Company.recId
- F_BankAccounts.currencyId = T_Currency.recId
- F_BankAccounts.loss_accountId = F_Accounts.recId

---

#### 398 银行对账 (F_BankReconcile)

- **业务含义**：银行对账
- **所属数据库**：思方云2 ERP
-关联关系：
- F_BankReconcile.bankReconcileSetingId = F_BankReconcileSeting.recId
- F_BankReconcile.bankAccountsId = F_BankAccounts.recId
- F_BankReconcile.companyId = T_Company.recId
- F_BankReconcile.creatorId = T_User.recId
- F_BankReconcile.fiscalPeriodId = T_FiscalPeriod.recId
- F_BankReconcile.postRoleId = T_PostRole.recId

---

#### 399 银行对账明细 (F_BankReconcileItem)

- **业务含义**：银行对账明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_BankReconcileItem.bankReconcileId = F_BankReconcile.recId

---

#### 400 银行对账配置 (F_BankReconcileSeting)

- **业务含义**：银行对账配置
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 401 银行对账配置明细 (F_BankReconcileSetingItem)

- **业务含义**：银行对账配置明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_BankReconcileSetingItem.bankReconcileSetingId = F_BankReconcileSeting.recId

---

#### 402 现金账流水 (F_CashAccount)

- **业务含义**：现金账流水
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CashAccount.accountId = F_Accounts.recId
- F_CashAccount.bankAccountsId = F_BankAccounts.recId
- F_CashAccount.companyId = T_Company.recId
- F_CashAccount.creatorId = T_User.recId
- F_CashAccount.currencyId = T_Currency.recId
- F_CashAccount.fiscalPeriodId = T_FiscalPeriod.recId
- F_CashAccount.postRoleId = T_PostRole.recId
- F_CashAccount.projectCatagoryItemId = F_ProjectCatagoryItem.recId

---

#### 403 现金账流水明细 (F_CashAccountItem)

- **业务含义**：现金账流水明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CashAccountItem.accountId = F_Accounts.recId
- F_CashAccountItem.cashAccountId = F_CashAccount.recId
- F_CashAccountItem.currencyId = T_Currency.recId
- F_CashAccountItem.projectCatagoryItemId = F_ProjectCatagoryItem.recId

---

#### 404 出纳管理/现金账 (F_CloseCashAccount)

- **业务含义**：出纳管理/现金账
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CloseCashAccount.companyId = T_Company.recId
- F_CloseCashAccount.creatorId = T_User.recId
- F_CloseCashAccount.currencyId = T_Currency.recId
- F_CloseCashAccount.postRoleId = T_PostRole.recId

---

#### 405 出纳管理/现金账明细 (F_CloseCashAccountItem)

- **业务含义**：出纳管理/现金账明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CloseCashAccountItem.cashAccountId = F_CashAccount.recId
- F_CloseCashAccountItem.closeCashAccountId = F_CloseCashAccount.recId
- F_CloseCashAccountItem.cashAccountItemId = F_CashAccountItem.recId

---

#### 406 期末调汇 (F_CurrExchAdj)

- **业务含义**：期末调汇
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CurrExchAdj.creatorId = T_User.recId
- F_CurrExchAdj.currencyId = T_Currency.recId
- F_CurrExchAdj.fiscalPeriodId = T_FiscalPeriod.recId
- F_CurrExchAdj.companyId = T_Company.recId

---

#### 407 期末调汇明细 (F_CurrExchAdjItem)

- **业务含义**：期末调汇明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_CurrExchAdjItem.currencyItemId = F_CurrExchAdjItem.currencyItemId
- F_CurrExchAdjItem.currExchAdjId = F_CurrExchAdj.recId
- F_CurrExchAdjItem.currencyId = T_Currency.recId
- F_CurrExchAdjItem.voucherId = F_Voucher.recId

---

#### 408 折旧计提 (F_Depreciation)

- **业务含义**：折旧计提
- **所属数据库**：思方云2 ERP
-关联关系：
- F_Depreciation.companyId = T_Company.recId
- F_Depreciation.creatorId = T_User.recId
- F_Depreciation.fiscalPeriodId = T_FiscalPeriod.recId
- F_Depreciation.postRoleId = T_PostRole.recId

---

#### 409 折旧计提明细表 (F_DepreciationItem)

- **业务含义**：折旧计提明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_DepreciationItem.depAddAcountId = F_Accounts.recId
- F_DepreciationItem.depExpenseAccountId = F_Accounts.recId
- F_DepreciationItem.depreciationId = F_Depreciation.recId
- F_DepreciationItem.fixedAssetsId = F_FixedAssets.recId

---

#### 410 凭证登记 (F_DiaryAccount)

- **业务含义**：凭证登记
- **所属数据库**：思方云2 ERP
-关联关系：
- F_DiaryAccount.approvedId = T_User.recId
- F_DiaryAccount.companyId = T_Company.recId
- F_DiaryAccount.creatorId = T_User.recId
- F_DiaryAccount.fiscalPeriodId = T_FiscalPeriod.recId
- F_DiaryAccount.flowTypeId = T_FlowType.recId
- F_DiaryAccount.postRoleId = T_PostRole.recId
- F_DiaryAccount.postedId = T_User.recId

---

#### 411 F_DiaryAccountHistory (F_DiaryAccountHistory)

- **业务含义**：ERP 系统 F_DiaryAccountHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 412 凭证登记明细表 (F_DiaryAccountItem)

- **业务含义**：凭证登记明细表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_DiaryAccountItem.accountId = F_Accounts.recId
- F_DiaryAccountItem.currencyId = T_Currency.recId
- F_DiaryAccountItem.diaryAccountId = F_DiaryAccount.recId
- F_DiaryAccountItem.voucherItemId = F_VoucherItem.recId

---

#### 413 F_DiaryAccountWF (F_DiaryAccountWF)

- **业务含义**：ERP 系统 F_DiaryAccountWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 414 固定资产 (F_FixedAssets)

- **业务含义**：固定资产
- **所属数据库**：思方云2 ERP
-关联关系：
- F_FixedAssets.assetCategoryId = F_AssetCategorys.recId
- F_FixedAssets.assetChangeWayId = F_AssetChangeWays.recId
- F_FixedAssets.assetStatusId = F_AssetStatus.recId
- F_FixedAssets.assetUseId = T_Cate.recId
- F_FixedAssets.companyId = T_Company.recId
- F_FixedAssets.creatorId = T_User.recId
- F_FixedAssets.currencyId = T_Currency.recId
- F_FixedAssets.plantsId = T_Plants.recId
- F_FixedAssets.postRoleId = T_PostRole.recId
- F_FixedAssets.storageLocationId = T_Cate.recId
- F_FixedAssets.suppliersId = M_Suppliers.recId
- F_FixedAssets.unitId = T_Unit.recId
- F_FixedAssets.equipmentId = EQ_Equipments.recId

---

#### 415 固定资产明细 (F_FixedAssetsItem)

- **业务含义**：固定资产明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_FixedAssetsItem.accountId = F_Accounts.recId
- F_FixedAssetsItem.departmentId = T_Department.recId
- F_FixedAssetsItem.fixedAssetsId = F_FixedAssets.recId

---

#### 416 科目设定 (F_GL_Setting)

- **业务含义**：科目设定
- **所属数据库**：思方云2 ERP
-关联关系：
- F_GL_Setting.companyId = T_Company.recId

---

#### 417 科目设定明细 (F_GL_SettingItem)

- **业务含义**：科目设定明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_GL_SettingItem.accountId = F_Accounts.recId
- F_GL_SettingItem.desAccountId = F_Accounts.recId
- F_GL_SettingItem.gl_SettingId = F_GL_Setting.recId

---

#### 418 结存表 (F_LastPeriodWoBalanceCost)

- **业务含义**：结存表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_LastPeriodWoBalanceCost.periodId = T_FiscalPeriod.recId
- F_LastPeriodWoBalanceCost.woId = P_WO.recId
- F_LastPeriodWoBalanceCost.stepId = T_Steps.recId
- F_LastPeriodWoBalanceCost.processId = T_Process.recId
- F_LastPeriodWoBalanceCost.companyId = T_Company.recId

---

#### 419 F_PackingSlipItemContractSO (F_PackingSlipItemContractSO)

- **业务含义**：ERP 系统 F_PackingSlipItemContractSO 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_PackingSlipItemContractSO.contractSOId = S_ContractSO.recId
- F_PackingSlipItemContractSO.packingSlipItemId = FGI_PackingSlipItem.recId

---

#### 420 请款单 (F_PaymentRequest)

- **业务含义**：请款单
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 421 销售单位、财务设置里面的业务类型 (F_PlantBusiness)

- **业务含义**：销售单位、财务设置里面的业务类型
- **所属数据库**：思方云2 ERP
-关联关系：
- F_PlantBusiness.plantId = T_Plants.recId
- F_PlantBusiness.targetId = T_Plants.recId

---

#### 422 工厂业务明细 (F_PlantBusinessItem)

- **业务含义**：工厂业务明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_PlantBusinessItem.currencyId = T_Currency.recId
- F_PlantBusinessItem.plantBusinessId = F_PlantBusiness.recId
- F_PlantBusinessItem.providerId = T_Plants.recId
- F_PlantBusinessItem.tradingBusinessId = F_TradingBusiness.recId

---

#### 423 出纳扎账&财务过账 (F_Post)

- **业务含义**：出纳扎账&财务过账
- **所属数据库**：思方云2 ERP
-关联关系：
- F_Post.companyId = T_Company.recId
- F_Post.creatorId = T_User.recId
- F_Post.fiscalPeriodId = T_FiscalPeriod.recId
- F_Post.postRoleId = T_PostRole.recId

---

#### 424 出纳扎账明细 (F_PostItem)

- **业务含义**：出纳扎账明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_PostItem.accountId = F_Accounts.recId
- F_PostItem.postId = F_Post.recId

---

#### 425 核算项目 (F_ProjectCatagory)

- **业务含义**：核算项目
- **所属数据库**：思方云2 ERP
-关联关系：
- F_ProjectCatagory.companyId = T_Company.recId
- F_ProjectCatagory.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 426 核算项目明细 (F_ProjectCatagoryItem)

- **业务含义**：核算项目明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_ProjectCatagoryItem.projectCatagoryId = F_ProjectCatagory.recId
- F_ProjectCatagoryItem.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 427 应付暂估 (F_ProvisionalEstimate)

- **业务含义**：应付暂估
- **所属数据库**：思方云2 ERP
-关联关系：
- F_ProvisionalEstimate.companyId = T_Company.recId
- F_ProvisionalEstimate.creatorId = T_User.recId
- F_ProvisionalEstimate.fiscalPeriodId = T_FiscalPeriod.recId
- F_ProvisionalEstimate.postRoleId = T_PostRole.recId

---

#### 428 应付暂估明细 (F_ProvisionalEstimateItem)

- **业务含义**：应付暂估明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_ProvisionalEstimateItem.poItemId = M_PurchaseOrderItem.recId
- F_ProvisionalEstimateItem.currencyId = T_Currency.recId
- F_ProvisionalEstimateItem.customerId = S_Customer.recId
- F_ProvisionalEstimateItem.jobId = S_Job.recId
- F_ProvisionalEstimateItem.materialsId = M_Materials.recId
- F_ProvisionalEstimateItem.provisionalEstimateId = F_ProvisionalEstimate.recId
- F_ProvisionalEstimateItem.salesPartId = S_SalesParts.recId
- F_ProvisionalEstimateItem.suppliersId = M_Suppliers.recId
- F_ProvisionalEstimateItem.unitId = T_Unit.recId

---

#### 429 凭证摘要 (F_RefLib)

- **业务含义**：凭证摘要
- **所属数据库**：思方云2 ERP
-关联关系：
- F_RefLib.parentId = F_RefLib.recId

---

#### 430 交易业务 (F_TradingBusiness)

- **业务含义**：交易业务
- **所属数据库**：思方云2 ERP
-关联关系：
- F_TradingBusiness.fromId = T_Plants.recId
- F_TradingBusiness.toId = T_Plants.recId

---

#### 431 凭证 (F_Voucher)

- **业务含义**：凭证
- **所属数据库**：思方云2 ERP
-关联关系：
- F_Voucher.approvedId = T_User.recId
- F_Voucher.companyId = T_Company.recId
- F_Voucher.creatorId = T_User.recId
- F_Voucher.fiscalPeriodId = T_FiscalPeriod.recId
- F_Voucher.flowTypeId = T_FlowType.recId
- F_Voucher.postRoleId = T_PostRole.recId
- F_Voucher.postedId = T_User.recId
- F_Voucher.postedRoleId = T_PostRole.recId

---

#### 432 凭证描述 (F_VoucherDesc)

- **业务含义**：凭证描述
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 433 凭证审批历史记录 (F_VoucherHistory)

- **业务含义**：凭证审批历史记录
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 434 凭证明细 (F_VoucherItem)

- **业务含义**：凭证明细
- **所属数据库**：思方云2 ERP
-关联关系：
- F_VoucherItem.accountId = F_Accounts.recId
- F_VoucherItem.currencyId = T_Currency.recId
- F_VoucherItem.voucherId = F_Voucher.recId
- F_VoucherItem.cashProjectId = F_ProjectCatagoryItem.recId

---

#### 435 F_VoucherProject (F_VoucherProject)

- **业务含义**：ERP 系统 F_VoucherProject 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- F_VoucherProject.voucherId = F_Voucher.recId
- F_VoucherProject.voucherItemId = F_VoucherItem.recId

---

#### 436 凭证审批记录 (F_VoucherWF)

- **业务含义**：凭证审批记录
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.9 成本模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 437 产品项目 (C_CostSetting)

- **业务含义**：产品项目
- **所属数据库**：思方云2 ERP
-关联关系：
- C_CostSetting.accountId = F_Accounts.recId
- C_CostSetting.company = T_Company.recId
- C_CostSetting.costTypeId = C_CostType.recId
- C_CostSetting.parametersId = S_Parameters.recId

---

#### 438 成本设置对应工艺和工序 (C_CostSettingItem)

- **业务含义**：成本设置对应工艺和工序
- **所属数据库**：思方云2 ERP
-关联关系：
- C_CostSettingItem.costSettingId = C_CostSetting.recId
- C_CostSettingItem.parametersId = S_Parameters.recId
- C_CostSettingItem.stepsProcessId = T_StepsProcess.recId

---

#### 439 费用分组（费用管理） (C_CostSharing)

- **业务含义**：费用分组（费用管理）
- **所属数据库**：思方云2 ERP
-关联关系：
- C_CostSharing.companyId = T_Company.recId
- C_CostSharing.creatorId = T_User.recId
- C_CostSharing.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 440 费用分组明细（费用管理明细） (C_CostSharingItem)

- **业务含义**：费用分组明细（费用管理明细）
- **所属数据库**：思方云2 ERP
-关联关系：
- C_CostSharingItem.costSettingId = C_CostSetting.recId
- C_CostSharingItem.costSharingId = C_CostSharing.recId
- C_CostSharingItem.userId = T_User.recId

---

#### 441 费用管理--项目明细 (C_CostSharingItemCount)

- **业务含义**：费用管理--项目明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 442 C_CostSharingOutputDetail (C_CostSharingOutputDetail)

- **业务含义**：ERP 系统 C_CostSharingOutputDetail 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 443 项目类型 (C_CostType)

- **业务含义**：项目类型
- **所属数据库**：思方云2 ERP
-关联关系：
- C_CostType.systemId = T_SystemConfig.recId

---

#### 444 直接成本 (C_DirectBomCost)

- **业务含义**：直接成本
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 445 C_FinancialReport (C_FinancialReport)

- **业务含义**：ERP 系统 C_FinancialReport 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 446 C_FinancialReportItem (C_FinancialReportItem)

- **业务含义**：ERP 系统 C_FinancialReportItem 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 447 C_JobCostPeriods (C_JobCostPeriods)

- **业务含义**：ERP 系统 C_JobCostPeriods 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 448 工单明细成本 (C_JobWoDetailsCalStatus)

- **业务含义**：工单明细成本
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 449 C_StepIndirecMatCost (C_StepIndirecMatCost)

- **业务含义**：ERP 系统 C_StepIndirecMatCost 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.11 设备管理

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 450 设备管理表 (EQ_Equipments)

- **业务含义**：设备管理表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_Equipments.creatorId = T_User.recId
- EQ_Equipments.fixedAssetsId = F_FixedAssets.recId
- EQ_Equipments.plantsId = T_Plants.recId
- EQ_Equipments.pmGroupId = PM_Group.recId
- EQ_Equipments.processId = T_Process.recId
- EQ_Equipments.stepsId = T_Steps.recId
- EQ_Equipments.suppliersId = M_Suppliers.recId
- EQ_Equipments.postRoleId = T_PostRole.recId
- EQ_Equipments.departmentId = T_Department.recId

---

#### 451 设备保养管理 (EQ_MLO)

- **业务含义**：设备保养管理
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_MLO.closedById = T_User.recId
- EQ_MLO.confirmedById = T_User.recId
- EQ_MLO.creatorId = T_User.recId
- EQ_MLO.departmentId = T_Department.recId
- EQ_MLO.flowTypeId = T_FlowType.recId
- EQ_MLO.lastEditedById = T_User.recId
- EQ_MLO.plantsId = T_Plants.recId
- EQ_MLO.pmTypeId = PM_Types.recId
- EQ_MLO.preventiveId = EQ_Preventives.recId
- EQ_MLO.processId = T_Process.recId

---

#### 452 EQ_MLOEmployees (EQ_MLOEmployees)

- **业务含义**：ERP 系统 EQ_MLOEmployees 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 453 EQ_MLOEQ (EQ_MLOEQ)

- **业务含义**：ERP 系统 EQ_MLOEQ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 454 EQ_MLOHistory (EQ_MLOHistory)

- **业务含义**：ERP 系统 EQ_MLOHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_MLOHistory.mloId = EQ_MLO.recId
- EQ_MLOHistory.myId = T_User.recId

---

#### 455 设备保养明细 (EQ_MLOMaterials)

- **业务含义**：设备保养明细
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_MLOMaterials.materialsId = M_Materials.recId
- EQ_MLOMaterials.mloId = EQ_MLO.recId
- EQ_MLOMaterials.unitId = T_Unit.recId

---

#### 456 EQ_MLOTasks (EQ_MLOTasks)

- **业务含义**：ERP 系统 EQ_MLOTasks 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 457 设备保养审批 (EQ_MLOWF)

- **业务含义**：设备保养审批
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 458 P_MORouteParams (EQ_PMO)

- **业务含义**：P_MORouteParams
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PMO.departmentId = T_Department.recId
- EQ_PMO.equipmentId = EQ_Equipments.recId

---

#### 459 设备维修管理关联雇员表 (EQ_PMOEmployees)

- **业务含义**：设备维修管理关联雇员表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PMOEmployees.pmoId = EQ_PMO.recId

---

#### 460 设备维修管理--审核记录 (EQ_PMOHistory)

- **业务含义**：设备维修管理--审核记录
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 461 设备维修管理--物料 (EQ_PMOMaterials)

- **业务含义**：设备维修管理--物料
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PMOMaterials.materialsId = M_Materials.recId
- EQ_PMOMaterials.pmoId = EQ_PMO.recId
- EQ_PMOMaterials.unitId = T_Unit.recId

---

#### 462 设备维修管理--任务 (EQ_PMOTasks)

- **业务含义**：设备维修管理--任务
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 463 EQ_PMOWF (EQ_PMOWF)

- **业务含义**：ERP 系统 EQ_PMOWF 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 464 设备保养定义关联设备表 (EQ_PreventiveEQ)

- **业务含义**：设备保养定义关联设备表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PreventiveEQ.equipmentId = EQ_Equipments.recId
- EQ_PreventiveEQ.preventiveId = EQ_Preventives.recId

---

#### 465 保养类型和物料关联表 (EQ_PreventiveMaterials)

- **业务含义**：保养类型和物料关联表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PreventiveMaterials.materialsId = M_Materials.recId
- EQ_PreventiveMaterials.preventiveId = EQ_Preventives.recId

---

#### 466 设备保养定义 (EQ_Preventives)

- **业务含义**：设备保养定义
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_Preventives.pmGroupId = PM_Group.recId
- EQ_Preventives.pmTypeId = PM_Types.recId
- EQ_Preventives.departmentId = T_Department.recId

---

#### 467 设备保养定义管理任务表 (EQ_PreventiveTasks)

- **业务含义**：设备保养定义管理任务表
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_PreventiveTasks.preventiveId = EQ_Preventives.recId
- EQ_PreventiveTasks.taskId = PM_tasks.recId

---

#### 468 设备管理--物料 (EQ_Spareparts)

- **业务含义**：设备管理--物料
- **所属数据库**：思方云2 ERP
-关联关系：
- EQ_Spareparts.materialsId = M_Materials.recId
- EQ_Spareparts.equipmentId = EQ_Equipments.recId

---

#### 469 故障现象 (PM_Faults)

- **业务含义**：故障现象
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 470 维修分组 (PM_Group)

- **业务含义**：维修分组
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_Group.companyId = T_Company.recId
- PM_Group.userId = T_User.recId

---

#### 471 维修分组--用户 (PM_GroupEmployees)

- **业务含义**：维修分组--用户
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_GroupEmployees.groupID = PM_Group.recId
- PM_GroupEmployees.employeeID = S_BusinessMan.recId

---

#### 472 维修发料 (PM_IssueForm)

- **业务含义**：维修发料
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_IssueForm.creatorId = T_User.recId
- PM_IssueForm.pickedById = T_User.recId
- PM_IssueForm.plantsId = T_Plants.recId

---

#### 473 维修发料-维修单和保养单 (PM_IssueFormItem)

- **业务含义**：维修发料-维修单和保养单
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_IssueFormItem.issueFormId = PM_IssueForm.recId
- PM_IssueFormItem.mloMaterialId = EQ_MLOMaterials.recId
- PM_IssueFormItem.pmoMaterialId = EQ_PMOMaterials.recId

---

#### 474 维修退料批次 (PM_IssueReturnBatch)

- **业务含义**：维修退料批次
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_IssueReturnBatch.issueReturnBatchId = PM_IssueFormItem.recId
- PM_IssueReturnBatch.issuereturnItemId = PM_IssueFormItem.recId
- PM_IssueReturnBatch.inventoryBatchId = M_InventoryBatch.currencyId

---

#### 475 故障原因 (PM_Reasons)

- **业务含义**：故障原因
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 476 维修退料 (PM_ReturnForm)

- **业务含义**：维修退料
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_ReturnForm.creatorId = T_User.recId
- PM_ReturnForm.plantsId = T_Plants.recId
- PM_ReturnForm.returnById = T_User.recId

---

#### 477 维修退料明细 (PM_ReturnFormItem)

- **业务含义**：维修退料明细
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_ReturnFormItem.issueFormItemId = PM_IssueFormItem.recId
- PM_ReturnFormItem.returnFormId = PM_ReturnForm.recId

---

#### 478 标准任务 (PM_Tasks)

- **业务含义**：标准任务
- **所属数据库**：思方云2 ERP
-关联关系：
- PM_Tasks.userId = T_User.recId

---

#### 479 业务员 (PM_Types)

- **业务含义**：业务员
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.12 APS排程

> 本章节数据来源于 Excel 工作表：`APS数据库`

#### 480 设备 (EQUIPMENT)

- **业务含义**：设备
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 481 EQUIPMENT_GROUP (EQUIPMENT_GROUP)

- **业务含义**：ERP 系统 EQUIPMENT_GROUP 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 482 工序表 (STEP)

- **业务含义**：工序表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.13 工作流引擎

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 483 JBPM4_DEPLOYMENT (JBPM4_DEPLOYMENT)

- **业务含义**：ERP 系统 JBPM4_DEPLOYMENT 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 484 JBPM4_DEPLOYPROP (JBPM4_DEPLOYPROP)

- **业务含义**：ERP 系统 JBPM4_DEPLOYPROP 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 485 JBPM4_EXECUTION (JBPM4_EXECUTION)

- **业务含义**：ERP 系统 JBPM4_EXECUTION 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 486 JBPM4_HIST_ACTINST (JBPM4_HIST_ACTINST)

- **业务含义**：ERP 系统 JBPM4_HIST_ACTINST 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 487 JBPM4_HIST_DETAIL (JBPM4_HIST_DETAIL)

- **业务含义**：ERP 系统 JBPM4_HIST_DETAIL 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 488 JBPM4_HIST_PROCINST (JBPM4_HIST_PROCINST)

- **业务含义**：ERP 系统 JBPM4_HIST_PROCINST 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 489 JBPM4_HIST_TASK (JBPM4_HIST_TASK)

- **业务含义**：ERP 系统 JBPM4_HIST_TASK 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 490 JBPM4_HIST_VAR (JBPM4_HIST_VAR)

- **业务含义**：ERP 系统 JBPM4_HIST_VAR 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 491 JBPM4_ID_GROUP (JBPM4_ID_GROUP)

- **业务含义**：ERP 系统 JBPM4_ID_GROUP 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 492 JBPM4_ID_MEMBERSHIP (JBPM4_ID_MEMBERSHIP)

- **业务含义**：ERP 系统 JBPM4_ID_MEMBERSHIP 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 493 JBPM4_ID_USER (JBPM4_ID_USER)

- **业务含义**：ERP 系统 JBPM4_ID_USER 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 494 JBPM4_JOB (JBPM4_JOB)

- **业务含义**：ERP 系统 JBPM4_JOB 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 495 JBPM4_LOB (JBPM4_LOB)

- **业务含义**：ERP 系统 JBPM4_LOB 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 496 JBPM4_PARTICIPATION (JBPM4_PARTICIPATION)

- **业务含义**：ERP 系统 JBPM4_PARTICIPATION 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 497 JBPM4_PROPERTY (JBPM4_PROPERTY)

- **业务含义**：ERP 系统 JBPM4_PROPERTY 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 498 JBPM4_SWIMLANE (JBPM4_SWIMLANE)

- **业务含义**：ERP 系统 JBPM4_SWIMLANE 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 499 JBPM4_TASK (JBPM4_TASK)

- **业务含义**：ERP 系统 JBPM4_TASK 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 500 JBPM4_VARIABLE (JBPM4_VARIABLE)

- **业务含义**：ERP 系统 JBPM4_VARIABLE 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.14 自定义表

> 本章节数据来源于 Excel 工作表：`自定义表、表名`

#### 501 A_AAA (A_AAA)

- **业务含义**：ERP 系统 A_AAA 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 502 a_allMaterialsFromZB20170221 (a_allMaterialsFromZB20170221)

- **业务含义**：ERP 系统 a_allMaterialsFromZB20170221 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 503 a_backup_deletedMatrlList_20170325 (a_backup_deletedMatrlList_20170325)

- **业务含义**：ERP 系统 a_backup_deletedMatrlList_20170325 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 504 a_CustomerfromZB20170221 (a_CustomerfromZB20170221)

- **业务含义**：ERP 系统 a_CustomerfromZB20170221 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 505 a_CustomerfromZB20170221-1 (a_CustomerfromZB20170221-1)

- **业务含义**：ERP 系统 a_CustomerfromZB20170221-1 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 506 a_DeletedMtrlList_20170325 (a_DeletedMtrlList_20170325)

- **业务含义**：ERP 系统 a_DeletedMtrlList_20170325 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 507 a_FGI_Inevneotyr_20170506 (a_FGI_Inevneotyr_20170506)

- **业务含义**：ERP 系统 a_FGI_Inevneotyr_20170506 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 508 a_fgibal_20170401 (a_fgibal_20170401)

- **业务含义**：ERP 系统 a_fgibal_20170401 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 509 a_FGIStock0401 (a_FGIStock0401)

- **业务含义**：ERP 系统 a_FGIStock0401 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 510 a_import_fgi-0301 (a_import_fgi-0301)

- **业务含义**：ERP 系统 a_import_fgi-0301 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 511 a_import_Materials-0301 (a_import_Materials-0301)

- **业务含义**：ERP 系统 a_import_Materials-0301 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 512 a_log1_02262017922PM (a_log1_02262017922PM)

- **业务含义**：ERP 系统 a_log1_02262017922PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 513 a_log1_02262017923PM (a_log1_02262017923PM)

- **业务含义**：ERP 系统 a_log1_02262017923PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 514 a_log1_022720171031PM (a_log1_022720171031PM)

- **业务含义**：ERP 系统 a_log1_022720171031PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 515 a_log1_02282017943PM (a_log1_02282017943PM)

- **业务含义**：ERP 系统 a_log1_02282017943PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 516 a_log1_03162017933PM (a_log1_03162017933PM)

- **业务含义**：ERP 系统 a_log1_03162017933PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 517 a_log1_03312017615PM (a_log1_03312017615PM)

- **业务含义**：ERP 系统 a_log1_03312017615PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 518 a_log1_03312017617PM (a_log1_03312017617PM)

- **业务含义**：ERP 系统 a_log1_03312017617PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 519 a_log1_03312017657PM (a_log1_03312017657PM)

- **业务含义**：ERP 系统 a_log1_03312017657PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 520 a_log2_02262017922PM (a_log2_02262017922PM)

- **业务含义**：ERP 系统 a_log2_02262017922PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 521 a_log2_02262017923PM (a_log2_02262017923PM)

- **业务含义**：ERP 系统 a_log2_02262017923PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 522 a_log2_02282017943PM (a_log2_02282017943PM)

- **业务含义**：ERP 系统 a_log2_02282017943PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 523 a_log2_03312017615PM (a_log2_03312017615PM)

- **业务含义**：ERP 系统 a_log2_03312017615PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 524 a_log2_03312017617PM (a_log2_03312017617PM)

- **业务含义**：ERP 系统 a_log2_03312017617PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 525 a_log2_03312017657PM (a_log2_03312017657PM)

- **业务含义**：ERP 系统 a_log2_03312017657PM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 526 a_log2_041012017657AM (a_log2_041012017657AM)

- **业务含义**：ERP 系统 a_log2_041012017657AM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 527 a_log2_041112017657AM (a_log2_041112017657AM)

- **业务含义**：ERP 系统 a_log2_041112017657AM 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 528 a_log2_20170403 (a_log2_20170403)

- **业务含义**：ERP 系统 a_log2_20170403 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 529 a_mtrlBal_20170401 (a_mtrlBal_20170401)

- **业务含义**：ERP 系统 a_mtrlBal_20170401 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 530 a_mtrlbal_20170401_1 (a_mtrlbal_20170401_1)

- **业务含义**：ERP 系统 a_mtrlbal_20170401_1 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 531 a_oldErp_So$ (a_oldErp_So$)

- **业务含义**：ERP 系统 a_oldErp_So$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 532 a_olderp_so2$ (a_olderp_so2$)

- **业务含义**：ERP 系统 a_olderp_so2$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 533 a_P_MOROUTE_20170506 (a_P_MOROUTE_20170506)

- **业务含义**：ERP 系统 a_P_MOROUTE_20170506 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 534 a_SM_FromZB20170220 (a_SM_FromZB20170220)

- **业务含义**：ERP 系统 a_SM_FromZB20170220 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 535 a_UpdatePanelSize_20170302 (a_UpdatePanelSize_20170302)

- **业务含义**：ERP 系统 a_UpdatePanelSize_20170302 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 536 a_UpdatePanelSize_20170302_1 (a_UpdatePanelSize_20170302_1)

- **业务含义**：ERP 系统 a_UpdatePanelSize_20170302_1 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 537 a_旧成品库存$ (a_旧成品库存$)

- **业务含义**：ERP 系统 a_旧成品库存$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 538 a_物料批次货位$ (a_物料批次货位$)

- **业务含义**：ERP 系统 a_物料批次货位$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 539 a_物料批次货位2$ (a_物料批次货位2$)

- **业务含义**：ERP 系统 a_物料批次货位2$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 540 a_物料批次货位3$ (a_物料批次货位3$)

- **业务含义**：ERP 系统 a_物料批次货位3$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 541 alan_materails_20170211 (alan_materails_20170211)

- **业务含义**：ERP 系统 alan_materails_20170211 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 542 alan_parameter_mapping (alan_parameter_mapping)

- **业务含义**：ERP 系统 alan_parameter_mapping 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 543 工厂管理-应收应付 (F_AccountSetting1)

- **业务含义**：工厂管理-应收应付
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 544 F_AccountSetting2 (F_AccountSetting2)

- **业务含义**：ERP 系统 F_AccountSetting2 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 545 F_AccountSetting3 (F_AccountSetting3)

- **业务含义**：ERP 系统 F_AccountSetting3 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 546 F_AccountSetting4 (F_AccountSetting4)

- **业务含义**：ERP 系统 F_AccountSetting4 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 547 fgi_inventory_0427_2200 (fgi_inventory_0427_2200)

- **业务含义**：ERP 系统 fgi_inventory_0427_2200 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 548 FGI_Inventory_backup_0420 (FGI_Inventory_backup_0420)

- **业务含义**：ERP 系统 FGI_Inventory_backup_0420 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 549 FGI_Inventory_BAK20170407 (FGI_Inventory_BAK20170407)

- **业务含义**：ERP 系统 FGI_Inventory_BAK20170407 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 550 fgi_inventory_bak_0429 (fgi_inventory_bak_0429)

- **业务含义**：ERP 系统 fgi_inventory_bak_0429 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 551 FGI_StockFormItem_bak0407 (FGI_StockFormItem_bak0407)

- **业务含义**：ERP 系统 FGI_StockFormItem_bak0407 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 552 FGI_StockFormItem_moid_bak (FGI_StockFormItem_moid_bak)

- **业务含义**：ERP 系统 FGI_StockFormItem_moid_bak 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 553 M_MaterialsWarehouse_bak (M_MaterialsWarehouse_bak)

- **业务含义**：ERP 系统 M_MaterialsWarehouse_bak 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 554 M_MaterialsWarehouse_bak0413 (M_MaterialsWarehouse_bak0413)

- **业务含义**：ERP 系统 M_MaterialsWarehouse_bak0413 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 555 p_bombatching_0413 (p_bombatching_0413)

- **业务含义**：ERP 系统 p_bombatching_0413 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 556 xnh_ChangedToConsigment_411 (xnh_ChangedToConsigment_411)

- **业务含义**：ERP 系统 xnh_ChangedToConsigment_411 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 557 xnh_ChangedToConsigment_412 (xnh_ChangedToConsigment_412)

- **业务含义**：ERP 系统 xnh_ChangedToConsigment_412 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 558 xnh_reworkChangeLog-返工工序记录 (xnh_reworkChangeLog-返工工序记录)

- **业务含义**：ERP 系统 xnh_reworkChangeLog-返工工序记录 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 559 xnh_奇立04010405_1724_item (xnh_奇立04010405_1724_item)

- **业务含义**：ERP 系统 xnh_奇立04010405_1724_item 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 560 xnh_底油线路 (xnh_底油线路)

- **业务含义**：ERP 系统 xnh_底油线路 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 561 xnh_贵阳海信_item (xnh_贵阳海信_item)

- **业务含义**：ERP 系统 xnh_贵阳海信_item 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 562 xnh_达信20170405001_item (xnh_达信20170405001_item)

- **业务含义**：ERP 系统 xnh_达信20170405001_item 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 563 xnh_高效170331_item (xnh_高效170331_item)

- **业务含义**：ERP 系统 xnh_高效170331_item 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 564 操作员$ (操作员$)

- **业务含义**：ERP 系统 操作员$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 565 转序员$ (转序员$)

- **业务含义**：ERP 系统 转序员$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

### 2.15 其它

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 566 物料 (-MO已分配数量-SO已分配数量)

- **业务含义**：物料
- **所属数据库**：思方云2 ERP
-关联关系：
- -MO已分配数量-SO已分配数量.plantsId = T_Plants.recId

---

#### 567 财务管理-财务数据-科目管理上级 (A_account)

- **业务含义**：财务管理-财务数据-科目管理上级
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 568 a_addlPHPart (a_addlPHPart)

- **业务含义**：ERP 系统 a_addlPHPart 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 569 a_AllInfo (a_AllInfo)

- **业务含义**：ERP 系统 a_AllInfo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 570 a_atom (a_atom)

- **业务含义**：ERP 系统 a_atom 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 571 a_CoreToBeFixed (a_CoreToBeFixed)

- **业务含义**：ERP 系统 a_CoreToBeFixed 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 572 a_DeletedJob (a_DeletedJob)

- **业务含义**：ERP 系统 a_DeletedJob 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 573 a_deletespds (a_deletespds)

- **业务含义**：ERP 系统 a_deletespds 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 574 a_drill (a_drill)

- **业务含义**：ERP 系统 a_drill 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 575 a_drill_adjustbase (a_drill_adjustbase)

- **业务含义**：ERP 系统 a_drill_adjustbase 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 576 a_fgi_batch (a_fgi_batch)

- **业务含义**：ERP 系统 a_fgi_batch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 577 a_FGI_Inventory (a_FGI_Inventory)

- **业务含义**：ERP 系统 a_FGI_Inventory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 578 a_importSO_AE (a_importSO_AE)

- **业务含义**：ERP 系统 a_importSO_AE 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 579 a_ImportSO_Flex (a_ImportSO_Flex)

- **业务含义**：ERP 系统 a_ImportSO_Flex 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 580 a_importSO_PPC (a_importSO_PPC)

- **业务含义**：ERP 系统 a_importSO_PPC 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 581 a_JobRouteParam (a_JobRouteParam)

- **业务含义**：ERP 系统 a_JobRouteParam 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 582 a_JobRoutes (a_JobRoutes)

- **业务含义**：ERP 系统 a_JobRoutes 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 583 a_laminate (a_laminate)

- **业务含义**：ERP 系统 a_laminate 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 584 a_Materials (a_Materials)

- **业务含义**：ERP 系统 a_Materials 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 585 a_MaterialsFromWH (a_MaterialsFromWH)

- **业务含义**：ERP 系统 a_MaterialsFromWH 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 586 a_materialwithoutwh (a_materialwithoutwh)

- **业务含义**：ERP 系统 a_materialwithoutwh 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 587 A_MET2 (A_MET2)

- **业务含义**：ERP 系统 A_MET2 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 588 a_OdrBatch (a_OdrBatch)

- **业务含义**：ERP 系统 a_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 589 a_old_erp_so (a_old_erp_so)

- **业务含义**：ERP 系统 a_old_erp_so 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 590 a_osScrapHistory (a_osScrapHistory)

- **业务含义**：ERP 系统 a_osScrapHistory 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 591 A_PARTTODOLIST (A_PARTTODOLIST)

- **业务含义**：ERP 系统 A_PARTTODOLIST 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 592 a_poList (a_poList)

- **业务含义**：ERP 系统 a_poList 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 593 a_PP_FromZB20170220 (a_PP_FromZB20170220)

- **业务含义**：ERP 系统 a_PP_FromZB20170220 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 594 a_ReWo_Status (a_ReWo_Status)

- **业务含义**：ERP 系统 a_ReWo_Status 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 595 a_reworkhistory-返工单 (a_reworkhistory-返工单)

- **业务含义**：ERP 系统 a_reworkhistory-返工单 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 596 a_Route (a_Route)

- **业务含义**：ERP 系统 a_Route 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 597 a_ScrapHistory-外发报废 (a_ScrapHistory-外发报废)

- **业务含义**：ERP 系统 a_ScrapHistory-外发报废 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 598 a_stepInfo (a_stepInfo)

- **业务含义**：ERP 系统 a_stepInfo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 599 A_Title (A_Title)

- **业务含义**：ERP 系统 A_Title 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 600 a_wo_Rework (a_wo_Rework)

- **业务含义**：ERP 系统 a_wo_Rework 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 601 a_yd (a_yd)

- **业务含义**：ERP 系统 a_yd 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 602 ab_OdrBatch (ab_OdrBatch)

- **业务含义**：ERP 系统 ab_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 603 供应商 (AND scts.fromId=scti.plantsId)

- **业务含义**：供应商
- **所属数据库**：思方云2 ERP
-关联关系：
- AND scts.fromId=scti.plantsId.toId = T_Plants.recId

---

#### 604 发放人 (and 主工单.Id=子工单.parentId)

- **业务含义**：发放人
- **所属数据库**：思方云2 ERP
-关联关系：
- and 主工单.Id=子工单.parentId.splitBatchId = P_WOSplitBatchApplication.recId

---

#### 605 物料批次库存 (b_matrl)

- **业务含义**：物料批次库存
- **所属数据库**：思方云2 ERP
-关联关系：
- b_matrl.whptr = T_Warehouse.recId
- b_matrl.locptr = T_Location.recId
- b_matrl.matrlPtr = M_Materials.recId

---

#### 606 b_Update_JobCustomer (b_Update_JobCustomer)

- **业务含义**：ERP 系统 b_Update_JobCustomer 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 607 b_Update_SalesPartCustomer (b_Update_SalesPartCustomer)

- **业务含义**：ERP 系统 b_Update_SalesPartCustomer 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 608 B_USER_WIP01 (B_USER_WIP01)

- **业务含义**：ERP 系统 B_USER_WIP01 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 609 ba (ba)

- **业务含义**：ERP 系统 ba 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 610 e2 (e2)

- **业务含义**：ERP 系统 e2 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 611 fgi_cartonsnumber (fgi_cartonsnumber)

- **业务含义**：ERP 系统 fgi_cartonsnumber 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 612 寄售 (fgi_sotransfer)

- **业务含义**：寄售
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 613 客户备份信息 (IMP_CustInfo)

- **业务含义**：客户备份信息
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 614 IMP_CustMapping (IMP_CustMapping)

- **业务含义**：ERP 系统 IMP_CustMapping 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 615 IMP_OdrBatch (IMP_OdrBatch)

- **业务含义**：ERP 系统 IMP_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 616 IMP_OdrProdNo (IMP_OdrProdNo)

- **业务含义**：ERP 系统 IMP_OdrProdNo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 617 imp_OrderList (imp_OrderList)

- **业务含义**：ERP 系统 imp_OrderList 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 618 IMP_PnInfo (IMP_PnInfo)

- **业务含义**：ERP 系统 IMP_PnInfo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 619 IMP_User (IMP_User)

- **业务含义**：ERP 系统 IMP_User 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 620 钻孔历史记录表 (org_DrillDetails)

- **业务含义**：钻孔历史记录表
- **所属数据库**：思方云2 ERP
-关联关系：
- org_DrillDetails.JobId = S_Job.recId

---

#### 621 qty_Order (qty_Order)

- **业务含义**：ERP 系统 qty_Order 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：
- qty_Order.creatorId = T_User.recId
- qty_Order.jobId = S_Job.recId

---

#### 622 rpt_moRoute_snap (rpt_moRoute_snap)

- **业务含义**：ERP 系统 rpt_moRoute_snap 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 623 rpt_ShopFloorInfo (rpt_ShopFloorInfo)

- **业务含义**：ERP 系统 rpt_ShopFloorInfo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 624 rpt_ShopFloorSummary (rpt_ShopFloorSummary)

- **业务含义**：ERP 系统 rpt_ShopFloorSummary 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 625 rpt_StepMapping (rpt_StepMapping)

- **业务含义**：ERP 系统 rpt_StepMapping 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 626 rpt_targetInfo (rpt_targetInfo)

- **业务含义**：ERP 系统 rpt_targetInfo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 627 来自工厂默认等于1，筛掉海外数据 (scts.contractItemId=scti.recId)

- **业务含义**：来自工厂默认等于1，筛掉海外数据
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 628 面积表 (VPartArea)

- **业务含义**：面积表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 629 W_DailyStepWipOutPut (W_DailyStepWipOutPut)

- **业务含义**：ERP 系统 W_DailyStepWipOutPut 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 630 W_WIP (W_WIP)

- **业务含义**：ERP 系统 W_WIP 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 631 W_WIPFieldDisplay (W_WIPFieldDisplay)

- **业务含义**：ERP 系统 W_WIPFieldDisplay 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 632 W_WIPQueryExecute (W_WIPQueryExecute)

- **业务含义**：ERP 系统 W_WIPQueryExecute 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 633 W_WIPStepDetails (W_WIPStepDetails)

- **业务含义**：ERP 系统 W_WIPStepDetails 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 634 月结主表 (WIP_Backlog)

- **业务含义**：月结主表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 635 WIP_PC (WIP_PC)

- **业务含义**：ERP 系统 WIP_PC 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 636 WIP_PCSteps (WIP_PCSteps)

- **业务含义**：ERP 系统 WIP_PCSteps 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 637 WIP_PCWO (WIP_PCWO)

- **业务含义**：ERP 系统 WIP_PCWO 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 638 wo_Rework$ (wo_Rework$)

- **业务含义**：ERP 系统 wo_Rework$ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 639 xnh_BOMBatch (xnh_BOMBatch)

- **业务含义**：ERP 系统 xnh_BOMBatch 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 640 xnh_BOMBatch2 (xnh_BOMBatch2)

- **业务含义**：ERP 系统 xnh_BOMBatch2 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 641 xnh_ChangedtobePlaned (xnh_ChangedtobePlaned)

- **业务含义**：ERP 系统 xnh_ChangedtobePlaned 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 642 xnh_DeletedLock (xnh_DeletedLock)

- **业务含义**：ERP 系统 xnh_DeletedLock 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 643 成品入库 (xnh_fgi_stockForm)

- **业务含义**：成品入库
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 644 成品入库明细 (xnh_fgi_stockFormItem)

- **业务含义**：成品入库明细
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 645 xnh_fgi_stockformitemwo (xnh_fgi_stockformitemwo)

- **业务含义**：ERP 系统 xnh_fgi_stockformitemwo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 646 xnh_last3setp (xnh_last3setp)

- **业务含义**：ERP 系统 xnh_last3setp 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 647 xnh_OrderDateChanged (xnh_OrderDateChanged)

- **业务含义**：ERP 系统 xnh_OrderDateChanged 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 648 xnh_orphanPart (xnh_orphanPart)

- **业务含义**：ERP 系统 xnh_orphanPart 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 649 xnh_OSMORoute (xnh_OSMORoute)

- **业务含义**：ERP 系统 xnh_OSMORoute 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 650 xnh_qtyshipped (xnh_qtyshipped)

- **业务含义**：ERP 系统 xnh_qtyshipped 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 651 xnh_resetPlanningedQty (xnh_resetPlanningedQty)

- **业务含义**：ERP 系统 xnh_resetPlanningedQty 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 652 xnh_stockedIn (xnh_stockedIn)

- **业务含义**：ERP 系统 xnh_stockedIn 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 653 xnh_wipBalance (xnh_wipBalance)

- **业务含义**：ERP 系统 xnh_wipBalance 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 654 xnh_wo (xnh_wo)

- **业务含义**：ERP 系统 xnh_wo 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 655 xnh_wotemp (xnh_wotemp)

- **业务含义**：ERP 系统 xnh_wotemp 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 656 xnh_woTempQty (xnh_woTempQty)

- **业务含义**：ERP 系统 xnh_woTempQty 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 657 zb_materials (zb_materials)

- **业务含义**：ERP 系统 zb_materials 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 658 set数量 (·)

- **业务含义**：set数量
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 659 不需要接收 (不需要接收)

- **业务含义**：ERP 系统 不需要接收 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 660 工厂 (主工单.moId=子工单.moId)

- **业务含义**：工厂
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 661 采购受理 (供应商)

- **业务含义**：采购受理
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 662 化验 (化验)

- **业务含义**：ERP 系统 化验 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 663 MO已分配数量 (可入库数量-MO需求数量)

- **业务含义**：MO已分配数量
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 664 可分配数量=库存数量+可入库数量 (可分配数量=库存数量+可入库数量)

- **业务含义**：ERP 系统 可分配数量=库存数量+可入库数量 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 665 可用数量=库存数量+ (可用数量=库存数量+)

- **业务含义**：ERP 系统 可用数量=库存数量+ 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 666 请购数量 (在途可分配数=请购数+采购数)

- **业务含义**：请购数量
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 667 制造部件 (工单对应的制造部件号)

- **业务含义**：制造部件
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 668 制造单表 (工单有主卡和子卡)

- **业务含义**：制造单表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 669 下一个工序 (空数据)

- **业务含义**：下一个工序
- **所属数据库**：思方云2 ERP
-关联关系：
- 空数据.nextOutputMORouteId = P_MORoute.recId
- 空数据.iqcId = FGI_IQC.recId
- 空数据.backlogUnitId = T_Unit.recId
- 空数据.pendingStatus = 1进站,2上机,3下机,4出站,5转出.recId
- 空数据.operateInformation = 工具,物料,参数.recId
- 空数据.isLock = 0正常1锁定2预警3超时锁定4超时预警.recId

---

#### 670 补货，投诉， (补货，投诉，)

- **业务含义**：ERP 系统 补货，投诉， 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 671 退货，换货，返修（新出单） (退货，换货，返修（新出单）)

- **业务含义**：ERP 系统 退货，换货，返修（新出单） 业务数据表
- **所属数据库**：思方云2 ERP
-关联关系：无

---

#### 672 审批通过时间 (需要接收（成品接收客户类型）)

- **业务含义**：审批通过时间
- **所属数据库**：思方云2 ERP
-关联关系：无

---

## 三、核心关联关系汇总

### 3.1 基础模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | T_Area.areaId = T_Area.recId |
| 2 | T_Area.cityId = T_Area.recId |
| 3 | T_Area.continentId = T_Area.recId |
| 4 | T_Area.countryId = T_Area.recId |
| 5 | T_Area.parentId = T_Area.recId |
| 6 | T_Area.provinceId = T_Area.recId |
| 7 | T_BusinessItem.businessId = T_Business.recId |
| 8 | T_Category.companyId = T_Company.recId |

### 3.2 物料模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | M_BOMIssue.bomPicklistId = M_BOMPicklist.recId |
| 2 | M_BOMIssue.creatorId = T_User.recId |
| 3 | M_BOMIssue.departmentId = T_Department.recId |
| 4 | M_BOMIssue.warehouseId = T_Warehouse.recId |
| 5 | M_BOMIssueItem.inventoryBatchId = 物料批次库存.recId |
| 6 | M_BOMIssueItem.bomIssueId = M_BOMIssue.recId |
| 7 | M_BOMIssueItem.materialsId = M_Materials.recId |
| 8 | M_BOMIssueItem.stockUnitId = T_Unit.recId |

### 3.3 成品模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | FGI_CartonsNumber.cartonsNumberService = FGI_StockForm.recId |
| 2 | FGI_CartonsNumber.stockFormJobId = FGI_StockFormJob.recId |
| 3 | FGI_CartonsNumber.jobId = s_job.recId |
| 4 | FGI_CartonsNumber.salesPartId = S_SalesParts.recId |
| 5 | FGI_IQC.moId = P_MO.recId |
| 6 | FGI_IQC.poItemId = S_OS_POItem.recId |
| 7 | FGI_IQC.checkorId = T_User.recId |
| 8 | FGI_IQC.creatorId = T_User.recId |

### 3.4 工程模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | E_CostJobMfgPartsParams.jobId = S_job.recId |
| 2 | E_CostJobMfgPartsParams.mfgpartId = E_JobMfgParts.recId |
| 3 | E_CostJobMfgPartsParams.parameterVal = E_JobMfgParts.recId |
| 4 | E_CostJobMfgPartsParams.seq = E_JobMfgParts.recId |
| 5 | E_CostJobMfgPartsParams.version = E_JobMfgParts.recId |
| 6 | E_CostJobMfgPartsParams.parameterId = S_Parameters.recId |
| 7 | E_DrillDetails.drl_Id = E_DrillTitle.recId |
| 8 | E_DrillDetails.jobId = S_Job.recId |

### 3.5 销售模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | S_CAR.companyId = T_Company.recId |
| 2 | S_CAR.complainmentId = S_Complainment.recId |
| 3 | S_CAR.customerId = S_Customer.recId |
| 4 | S_CAR.jobId = S_Job.recId |
| 5 | S_CAR.plantId = T_Plants.recId |
| 6 | S_CAR.salesPartId = S_SalesParts.recId |
| 7 | S_ComplainmentHistory.complainmentId = S_Complainment.recId |
| 8 | S_ComplainmentHistory.myId = T_User.recId |

### 3.6 生产模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | P_BOMBatching.bomPicklistItemId = M_BOMPicklistItem.qtyRemaining |
| 2 | P_BOMBatching.mfgPartId = E_JobMfgParts.recId |
| 3 | P_BOMBatching.materialsId = M_Materials.recId |
| 4 | P_BOMBatching.moId = P_MO.recId |
| 5 | P_BOMBatching.processId = T_Process.recId |
| 6 | P_BOMBatching.stockUnitId = T_Unit.recId |
| 7 | P_BOMBatching.warehouseId = T_Warehouse.recId |
| 8 | P_BOMBatching.stepsId = T_Steps.recId |

### 3.7 财务模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | F_AP_DebitMemo.returnOrderId = M_ReturnOrder.recId |
| 2 | F_AP_DebitMemo.companyId = T_Company.recId |
| 3 | F_AP_DebitMemo.creatorId = T_User.recId |
| 4 | F_AP_DebitMemo.currencyId = T_Currency.recId |
| 5 | F_AP_DebitMemo.fiscalPeriodId = T_FiscalPeriod.recId |
| 6 | F_AP_DebitMemo.plantBusinessId = F_PlantBusiness.recId |
| 7 | F_AP_DebitMemo.plantBusinessItemId = F_PlantBusinessItem.recId |
| 8 | F_AP_DebitMemo.plantsId = T_Plants.recId |

### 3.8 成本模块核心关联

| 序号 | 关联关系 |
|------|----------|
| 1 | C_CostSetting.accountId = F_Accounts.recId |
| 2 | C_CostSetting.company = T_Company.recId |
| 3 | C_CostSetting.costTypeId = C_CostType.recId |
| 4 | C_CostSetting.parametersId = S_Parameters.recId |
| 5 | C_CostSettingItem.costSettingId = C_CostSetting.recId |
| 6 | C_CostSettingItem.parametersId = S_Parameters.recId |
| 7 | C_CostSettingItem.stepsProcessId = T_StepsProcess.recId |
| 8 | C_CostSharing.companyId = T_Company.recId |


---
