<h1 align="center">数据库结构参考说明文档</h1>

> 本文档根据数据字典生成，为使用人员提供数据库表结构参考，帮助快速熟悉表定义及字段含义

## 变更记录

| 序号 | 变更内容 | 变更时间 | 变更人 | 备注 |
|------|----------|----------|--------|------|
| 1 | V1.0 | 待填写 | 自动生成脚本 | 初始版本 |
|  |  |  |  |  |

## 一、文档概述

### 1.1 文档目的

本文档旨在为使用人员提供数据库结构的全面参考，使使用人员能够：
- 快速理解各数据表的用途及字段含义
- 掌握各表所属业务域与数据库来源
- 准确编写查询语句进行数据提取
- 快速完成系统数据字典查阅

---

## 二、核心数据表结构

### 2.1 基础模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 1 系统设定 ( T_AppSeting )
- **业务含义**：系统设定
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| attach | string | 是 | - | - |
| email | string | 是 | - | 邮箱 |
| host | string | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| lg | string | 是 | - | - |
| modifiedBy | string | 是 | - | 更新人员 |
| password | string | 是 | - | 登录密码 |
| poVoucher | bool? | 是 | - | 生成采购凭证 |
| port | string | 是 | - | - |
| reportURI | string | 是 | - | - |
| sendEmail | bool? | 是 | - | 流程邮件提醒 |
| smtp | string | 是 | - | - |
| soVoucher | bool? | 是 | - | 生成销售凭证 |
| timeout | string | 是 | - | 访问期限 |
| upload_odbplusplus_path | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| matQtyDigit | int? | 是 | - | 物料采购数量位数 |
| matStockQtyDigit | int? | 是 | - | 物料库存数量位数 |
| mi_MfgPartUseSamePanelData | bool? | 是 | - | 制造部件用相同拼版 |
| mi_attachedFilePath_usedPartNum | bool? | 是 | - | MI编号存储附加文件 |
| mi_import_path | string | 是 | - | MI数据导入目录 |
| mi_fileupload_path | string | 是 | - | MI文件上载目录 |
| mi_partArea_factor | string | 是 | - | 交货板面积转换系数 |
| searchStartWithPercent | bool? | 是 | - | 工序结存查询过滤前面加% |
| recompileSPWhenOpenWipPage | bool? | 是 | - | 打开纵向WIP查询时重编译SP |
| importMiFileFormat | string | 是 | - | 导入MI文件格式 |
| soPriceDigit | int? | 是 | - | 销售价格位数 |
| miRouteMustReviseBeforeEdit | bool? | 是 | - | - |
| stackupUsedGeneralBom | bool? | 是 | - | 叠构采用通用物料 |
| noArrayOutput | bool? | 是 | - | Array不参与过数 |
| issueWay | string | 是 | - | 发料方式 |
| ifTaxPrice | bool? | 是 | - | - |
| notAssignerCanEditMI | bool? | 是 | - | 非分配者可编辑工程资料 |
| miCanReleaseWithPartialApproval | bool? | 是 | - | 工程资料流程可部分审批投产 |
| miShowSlotSize | bool? | 是 | - | - |
| miShowMfgpartParams | bool? | 是 | - | 工程设计显示子部件参数 |
| miShowMatStandard | bool? | 是 | - | 工程设计显示物料规格 |
| sheetImgShowVerHorMark | bool? | 是 | - | 开料图上显示横直料 |
| showStackupWithChar | bool? | 是 | - | 用不同字符表示层压图物料 |
| ifMulMICoding | bool? | 是 | - | 多工厂MI编码 |
| partNumOriRev | string | 是 | - | MI原始版本初始值 |
| custOrderControl | bool? | 是 | - | 业务员助理权限控制 |
| importTxtDrillCountDefine | string | 是 | - | 导入TXT钻嘴数据孔数定义 |
| isCheckSalesPartPcsOfArray | bool? | 是 | - | 检查MI与销售部件交货板单元数 |
| ifOsSelfDo | bool? | 是 | - | - |
| monthlyClosingByCompany | bool? | 是 | - | 按公司进行月结 |
| standard | bool? | 是 | - | 标准采购 |
| overTransferSO | bool? | 是 | - | 允许超额转仓 |
| defaultPlantId | int? | 是 | - | MI默认工厂ID |
| ifPODiscount | bool? | 是 | - | - |
| runCostScirptBeforeSubmit | bool? | 是 | - | MI提交前运行成本参数脚本 |
| voucherNoEqOrder | bool? | 是 | - | 凭证号等于单据号 |
| moAutoWOProcess | bool? | 是 | - | 在MO创建工单流程 |
| cannotMiAssignNoPlant | bool? | 是 | - | 未分单MI不能分配 |
| reworkRecPost | bool? | 是 | - | 返工接收过数管控 |
| partNum_RevCoding | bool? | 是 | - | MI编码+版本唯一 |
| miCodingUnRev | bool? | 是 | - | 订单分单时MI编码不变 |
| mfgpartLayerchar | string | 是 | - | 制造部件层连接符 |
| plantIdfLast | bool? | 是 | - | MI编码工厂标识放版本号最后一位 |
| bomPriceFromMonthlyClosing | bool? | 是 | - | 成本计算物料价格取月结成本价 |
| scrapCostAllocatedToWO | bool? | 是 | - | 报废成本分摊至工单入仓成本 |
| stackupShowLegendSolderMask | bool? | 是 | - | 叠构图显示文字油墨 |
| soConfirmViewUnApproval | bool? | 是 | - | 订单确认显示未审批的订单 |
| drillmustselectmfgpart | bool? | 是 | - | 钻带需选制造部件 |
| complainmentType | string | 是 | - | - |
| monthConsignmentPrice | bool? | 是 | - | 月结寄售入库单价来源寄售处理 |
| importMiCanRefreshBom | bool? | 是 | - | - |
| ifMatStandard | bool? | 是 | - | 物料&规格唯一 |
| outlineTypeNotNull | bool? | 是 | - | 锣带类型不能为空 |
| usedVCutPic | bool? | 是 | - | - |
| copyMfgParams | bool? | 是 | - | - |
| pausedJobNotReadFiles | bool? | 是 | - | - |
| importMiFileWay | string | 是 | - | 导入MI数据文件方法 |
| pickingSameMat | bool? | 是 | - | 领相同的物料 |
| checkMinMfgDate | bool? | 是 | - | - |
| miCanImportStackupImage | bool? | 是 | - | - |
| checkFGIStockExpiry | bool? | 是 | - | - |
| checkFGIProperty | bool? | 是 | - | - |
| checkVMiStock | bool? | 是 | - | 寄售和标准材料分开仓库入仓 |
| tecMfgQcPmc | bool? | 是 | - | 技研制造品保生管 |
| autoCreateBomPicking | bool? | 是 | - | - |
| overMatPicking | bool? | 是 | - | 领料可超出可用数 |
| mrbReasonScrap | bool? | 是 | - | MRB基于原因报废 |
| moAllocStockByCompany | bool? | 是 | - | MO按公司预分配库存 |
| bomMatQueryFromName | bool? | 是 | - | BOM物料查询按名称 |
| unCountNatGrossWeight | bool? | 是 | - | 送货单不自动计算净重与毛重 |
| stockByTheSameMO | bool? | 是 | - | 生产入库区分MO |
| customerOnlyHaveOneSpec | bool? | 是 | - | - |
| mobileVUnDo | bool? | 是 | - | 移动端箱包处理只显示待办列表 |
| stockBySalesPart | bool? | 是 | - | 按销售部件控制生产入库 |
| matMulPlantStock | bool? | 是 | - | 多工厂的物料入同一仓库 |
| ifOsMixStock | bool? | 是 | - | - |
| stockMatPriceChanged | bool? | 是 | - | 采购入库差异调整 |
| monthlyClosingByCompanyAndWarahouse | bool? | 是 | - | - |
| moReplaceMatCheck | bool? | 是 | - | MO替换物料属性检查提示 |
| moBomFromSOBom | bool? | 是 | - | MOBom来源于销售订单 |
| warehousingBySupplier | bool? | 是 | - | 物料按供应商入仓 |
| viewSoDisPrice | bool? | 是 | - | 显示订单折扣价 |
| noSuppMatVim | bool? | 是 | - | - |
| wipExportArea | string | 是 | - | WIP查询导出面积 |
| ifScp | bool? | 是 | - | - |
| scpUrl | string | 是 | - | 供应商协同平台网址 |
| partNumIsCustAndSerial | bool? | 是 | - | 生产编号查询须客户代码+流水号 |
| accountVoucherCoding | bool? | 是 | - | 会计凭证统一编号 |
| saleProvisionalEstimate | string | 是 | - | 销售暂估 |
| bomTypeCodeBeforeSubmit | bool? | 是 | - | - |
| checkSuppMax | bool? | 是 | - | 采购供应商限额控制 |
| poStockMax | string | 是 | - | 采购库存限额控制 |
| osCheckList | bool? | 是 | - | 工单外协料号加工检查 |
| onlineWarePZ | bool? | 是 | - | 线边仓凭证 |
| historySOPrice | bool? | 是 | - | 下单显示历史订单 |
| stepCheckInStock | bool? | 是 | - | 工序盘点计入期末库存 |
| voucherOriVal | bool? | 是 | - | 凭证负数原值记账 |
| cartonPackCheck | bool? | 是 | - | 箱包校验 |
| checkCustomerToBoxing | bool? | 是 | - | 检查客户箱包出入库 |
| sameMiPartNumBitNum | int? | 是 | - | - |
| jobPriceEffDays | int? | 是 | - | 产品定价有效天数 |
| expiredMatUnIssue | int? | 是 | - | 过期物料禁止发放 |
| mrpLockedInventory | bool? | 是 | - | 物料分配锁定库存批次 |
| importedMiNotEdit | bool? | 是 | - | 导入MI不能修改 |
| shipUnModPrice | bool? | 是 | - | 出货的订单不允许改价格 |
| ksInfoCheck | bool? | 是 | - | 客诉信息检查 |
| pcsOfPanelFromPart | bool? | 是 | - | - |
| bomCounting | bool? | 是 | - | Bom计算用量 |
| integrateSQ | bool? | 是 | - | 集成报价系统 |
| sqDbType | string | 是 | - | 报价数据库类型 |
| sqUser | string | 是 | - | 报价数据库用户 |
| sqPassword | string | 是 | - | 报价数据库密码 |
| sqDriverClass | string | 是 | - | 报价数据库驱动 |
| sqJdbcUrl | string | 是 | - | 报价数据库连接串 |
| custPoStock | bool? | 是 | - | 客户PO箱包入库 |
| xchangeUrl | string | 是 | - | 交换平台地址 |
| showTextLineInPanelPic | bool? | 是 | - | 拼版图下面显示文字行 |
| miBomShowSubstitute | bool? | 是 | - | 工程设计BOM显示替换物料 |
| salePartOrderPrice | bool? | 是 | - | 成品定价单取价 |
| hadSimpleScheduling | bool? | 是 | - | - |
| daysAheadSchedule | int? | 是 | - | - |
| calDaysWithProcessTime | bool? | 是 | - | 用工艺加工时间计算制造周期 |
| stockBySalesPartXout | bool? | 是 | - | 按销售部件控制叉板入库 |
| forbidManualPaymentPZ | bool? | 是 | - | 禁止手工凭证做收付款 |
| poLastPriceByMat | bool? | 是 | - | PO最后一次价格按照物料 |
| jsonSeCode | string | 是 | - | Json调用安全码 |
| woSetPrint | bool? | 是 | - | 工单套打 |
| mergeControl | bool? | 是 | - | 合拼最大面积限制 |
| costCalPromptSaveLog | bool? | 是 | - | 成本计算提示写入日志文件 |
| packBagStockByJob | bool? | 是 | - | 箱包按料号扫描入库 |
| packBagShipRepCartonNum | bool? | 是 | - | 箱包扫描出货标准箱可替换 |
| squareStr | string | 是 | - | 面积单位 |
| customLicVal | int? | 是 | - | - |
| copyRfqPriceToSP | bool? | 是 | - | - |
| stockUploadUrl | string | 是 | - | 库存上传地址 |
| stockUploadCore | string | 是 | - | 上传定时表达式 |
| stockUploadVendor | string | 是 | - | 库存上传供应商 |
| stockUploadToken | string | 是 | - | 库存上传密钥 |
| stockUploadMail | string | 是 | - | 库存上传失败接收邮件 |
| miWithSMT | bool? | 是 | - | - |
| thirdErpDbType | string | 是 | - | 第三方ERP数据库类型 |
| thirdErpUser | string | 是 | - | 第三方ERP数据库用户 |
| thirdErpPassword | string | 是 | - | 第三方ERP数据库密码 |
| thirdErpDriverClass | string | 是 | - | 第三方ERP数据库驱动 |
| thirdErpJdbcUrl | string | 是 | - | 第三方ERP数据库连接串 |
| infactWasteByStep | bool? | 是 | - | 按工序录入废弃物实际回收量 |
| sqIncludingNotApproved | bool? | 是 | - | - |
| smtBomProcessCode | string | 是 | - | SMT元器件默认使用工艺 |
| mfgpartLayerNumPrefix | string | 是 | - | 部件代码层数前缀 |
| poPriceDigit | int? | 是 | - | 采购价格位数 |
| inputMiNoCheck | bool? | 是 | - | 导入MI不需检查 |
| noShowCustomerSpec | bool? | 是 | - | 不显示客户技术标准 |
| jsonTimeout | int? | 是 | - | JSON接口超时设置 |
| birtURI | string | 是 | - | - |
| dbversion | string | 是 | - | - |
| sapUserName | string | 是 | - | SAP接口用户名 |
| sapPassword | string | 是 | - | SAP接口密码 |
| identificationCode | string | 是 | - | 设备识别码 |
| hisenseUploadId | string | 是 | - | 库存上传ID |
| hisenseUploadKey | string | 是 | - | 库存上传Key |
| hisenseUploadUrl | string | 是 | - | - |
| hisenseUploadCore | string | 是 | - | - |
| salePartRev | string | 是 | - | 销售部件版本 |
| defaultJobPriceEffectDate | bool? | 是 | - | 默认产品定价生效日期 |
| defaultPOCommittedDate | bool? | 是 | - | 默认采购单明细承诺交期 |
| markRemainingMat | bool? | 是 | - | 标记余料尺寸 |
| dcParamCode | string | 是 | - | 周期码参数代码 |
| paramShowUnit | bool? | 是 | - | - |
| expiredMonthNum | int? | 是 | - | 保持期默认添加月数 |
| miImageBlackWhite | bool? | 是 | - | - |
| stackupDrawMatOption | int? | 是 | - | - |
| btwFilePath | string | 是 | - | 标签模板文件路径 |
| labelSamplePath | string | 是 | - | 标签效果样例文件路径 |
| labelPrintTxtPath | string | 是 | - | 标签打印数据TXT文件目录 |
| labelQuerySp | string | 是 | - | 标签数据存储过程 |
| finAccountSetNumber | string | 是 | - | 财务账套代码 |
| impTypeTranfered | bool? | 是 | - | 旧阻抗数据已转换处理 |
| impCalAddr | string | 是 | - | 阻抗计算服务地址 |
| c1 | decimal? | 是 | - | - |
| c2 | decimal? | 是 | - | - |
| cer | decimal? | 是 | - | - |
| er1 | decimal? | 是 | - | - |
| w1SubW2 | decimal? | 是 | - | (W1-W2) |
| priceExchRate | bool? | 是 | - | 订单取报价时汇率 |
| pricingRate | bool? | 是 | - | 内部公司加价率来自存储过程 |
| suppDocType | string | 是 | - | 供应商文档类型 |
| prelecUser | string | 是 | - | 生产记录库用户 |
| prelecPassword | string | 是 | - | 生产记录库密码 |
| prelecDriverClass | string | 是 | - | 生产记录库驱动 |
| prelecJdbcUrl | string | 是 | - | 生产记录库地址 |
| smtProcessRelStep | bool? | 是 | - | - |
| defaultCartonWeight | decimal? | 是 | - | 默认箱重(单元重量相同单位) |
| miUpdateSalespart | bool? | 是 | - | MI保存时更新销售部件 |
| multiPanelize | bool? | 是 | - | 多拼版方案 |
| enableTaxesFlag | bool? | 是 | - | 产成品保税标识 |
| orderWarn | string | 是 | - | 下单风险控制 |
| shipmentWarn | string | 是 | - | 出货风险控制 |
| inOutLabelSameData | bool? | 是 | - | 内外标签统一数据文件 |
| matnoauditnotmatpricechanged | bool? | 是 | - | 物料未审核不允许创建报价单 |
| matnoauditnotspds | bool? | 是 | - | 物料未审核不允许创建SPDS |
| salesForcastControl | bool? | 是 | - | - |
| xxVal | int? | 是 | - | - |
| yyVal | int? | 是 | - | - |
| showPBSHeadAndDetail | bool? | 是 | - | 包装入库单启用表头+明细展示 |
| showFGIStockHeadAndDetail | bool? | 是 | - | 成品入库单启用表头+明细展示 |
| showCaseBoxingHeadAndDetail | bool? | 是 | - | 箱包入库单启用表头+明细展示 |
| allowDuplicateParameterName | bool? | 是 | - | 允许参数名称重复 |
| showwostockheadanddetail | bool? | 是 | - | 生产入库单启用表头+明细展示 |
| spdsRequiredType | string | 是 | - | 强制SPDS控制 |
| showunloadingheadanddetail | bool? | 是 | - | 退料管理启用表头+明细展示 |
| isSuppluersEditPostRole | bool? | 是 | - | 供应商管理可修改岗位角色 |
| uniontransUid | string | 是 | - | 协同平台企业UID |
| uniontransApiUrl | string | 是 | - | 协同平台API地址 |
| uniontransLoginJson | string | 是 | - | 协同平台登录Json |
| isOpenKeyPolicy | bool? | 是 | - | 是否启用密钥策略 |
| passwordValidityDays | int? | 是 | - | 密码有效期天数 |
| layoutDirectUseF | bool? | 是 | - | 拼版图方向用“F” |
| defaultAllPositiveDirect | bool? | 是 | - | 拼版图默认全部加正方向 |
| minMarginLenWidCanSwap | bool? | 是 | - | - |
| sheetLenWeftwise | bool? | 是 | - | - |
| ifSalesForecastSplitting | bool? | 是 | - | 销售预测分单 |
| defaultEndShippingAddress | bool? | 是 | - | 终端客户地址自动默认 |
| sheetSizeUnit | string | 是 | - | 工程大料尺寸单位 |
| stackupImageDispThickTol | bool? | 是 | - | 叠构图显示厚度公差 |
| ozDecimalPlaces | int? | 是 | - | 计算阻抗理论值保留小数位 |
| spControlByArchiveStatus | bool? | 是 | - | 销售部件建档状态控制 |
| filterBySupplierPosition | bool? | 是 | - | 请购受理按供应商岗位过滤 |
| allowNoSelectProcess | bool? | 是 | - | 过数管理允许不选择工序 |
| orderReviewEnable | bool? | 是 | - | 订单审核启用销售组织架构 |
| costCarrier | bool? | 是 | - | 成本载体 |
| unShipmentClearPackNum | bool? | 是 | - | 取消装运同步清除送货单号 |
| otherDbType | string | 是 | - | 其它数据源类型 |
| otherDbUser | string | 是 | - | 其它数据源用户 |
| otherDbPassword | string | 是 | - | 其它数据源密码 |
| otherDbDriverClass | string | 是 | - | 其它数据源驱动 |
| otherDbJdbcUrl | string | 是 | - | 其它数据源连接串 |
| spcInspectSpWithWo | string | 是 | - | SPC数据采集工单存储过程 |
| autoGenReviewReport | bool? | 是 | - | 自动产生评审报告 |
| timeExpression | string | 是 | - | 时间表达式 |
| spcDefaultTimeStr | string | 是 | - | SPC报告默认时间 |
| miCodingBySP | bool? | 是 | - | 订单分单MI编码来自存储过程 |
| useSFStartDateAsPeriod | bool? | 是 | - | 开始期间默认为预测期间 |
| miCopyNoFilterByLayerNum | bool? | 是 | - | 从...拷贝不按层数过滤 |
| autoCreateToolApplyForm | bool? | 是 | - | MI审核后自动产生工具申请单 |
| engineeringInterfaceSwitchAddress | string | 是 | - | - |
| requisitionNotAllowedToModifyDepartment | bool? | 是 | - | 请购部门默认带出用户所属部门且不允许修改 |
| purchaseAcceptedOnlySelectSPDS | bool? | 是 | - | 未做SPDS的物料不能进行采购请购 |
| isEquipmnetMaintenanceTimeByOperationTime | bool? | 是 | - | 设备稼动依操作时间为主 |
| isEquipmnetOrderSubmitNoNGTasks | bool? | 是 | - | 设备单据提交时不能有NG任务 |
| inECNShowSalesPartOnly | bool? | 是 | - | 外部ECN仅显示销售部件类型 |
| isEnterExpenses | bool? | 是 | - | 是否录入费用 |
| priceNotAllowedSPDSPrice | bool? | 是 | - | 采购单单价不允许大于SPDS单价 |
| luodaiCalculationServiceAddress | string | 是 | - | 锣带计算服务地址 |
| integerBit | int? | 是 | - | 整数位 |
| decimalPlaces | int? | 是 | - | 小数位 |
| exceptionReportEightDMode | bool? | 是 | - | 异常报告8D模式 |
| theMethodOfCreateMergeOrder | string | 是 | - | 合拼单生成方式 |
| copyTechSpec | bool? | 是 | - | - |
| stackupCopyOutLayerMfgParams | bool? | 是 | - | 重新重构时拷贝外层部件参数 |
| verifyTaxRate | bool? | 是 | - | - |
| reportPriceDecimalPlace | int? | 是 | - | - |
| reportAmountDecimalPlace | int? | 是 | - | - |
| updateWhichJobBySP | bool? | 是 | - | - |
| panelSizeDecimalDigits | int? | 是 | - | - |
| defaultPpMinTol | decimal? | 是 | - | - |
| paramsGroupDisp | bool? | 是 | - | - |
| isHalogenFreeHidden | bool? | 是 | - | - |
| requiredRack | bool? | 是 | - | - |
| miSortBy | string | 是 | - | - |
| showLastContractItem | bool? | 是 | - | - |
| ifEditFactoryName | bool? | 是 | - | - |
| ifeditassetsnumber | bool? | 是 | - | - |
| isOCNCodingRules | bool? | 是 | - | - |
| isSuttle | bool? | 是 | - | 净重是否必录 |
| requiredDepartment | bool? | 是 | - | - |
| ifCodeSort | bool? | 是 | - | - |
| ifGenerateInternalModel | bool? | 是 | - | - |
| proVoteNewCoding | bool? | 是 | - | - |
| divideNewMI | bool? | 是 | - | - |
| endCustomerDisplayType | bool? | 是 | - | - |
| invoiceGenerationNumberInPickingApproval | bool? | 是 | - | - |
| ContractManageCutName | string | 是 | - | - |
| ContractManageCutName2 | string | 是 | - | - |
| ContractManageCutName3 | string | 是 | - | - |
| ContractManageCutName4 | string | 是 | - | - |
| workOrderDistributionWithoutFilteringStatusLoadingAll | bool? | 是 | - | - |
| isNecessaryEquipmentType | bool? | 是 | - | - |
| packIsSelected | bool? | 是 | - | - |
| isReceiptBatchAuto | bool? | 是 | - | - |
| isSalesPartsLimitType | bool? | 是 | - | - |
| isContractItemCustomTypeNotNull | bool? | 是 | - | - |
| isUpdateWOFromBacklogStep | bool? | 是 | - | 工单升级从结存工艺开始升级 |
| isModifyECNWithoutUpdateingPart | bool? | 是 | - | 编辑ECN不更新新销售部件和生产编号 |
- **关联关系**：无

---

#### 2 区域 ( T_Area )
- **业务含义**：区域
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 修改人呢 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| type | string | 是 | - | Root 根 Continent 洲  Country 国 Area 区 Province 省 City 市 |
| version | int? | 是 | - | - |
| areaId | int? | 是 | - | 本记录的ID，对应T_Area.recId |
| cityId | int? | 是 | - | 城市ID，对应T_Area.recId |
| continentId | int? | 是 | - | 洲ID，对应T_Area.recId |
| countryId | int? | 是 | - | 国ID，对应T_Area.recId |
| parentId | int? | 是 | - | 上一级ID，对应T_Area.recId |
| provinceId | int? | 是 | - | 省ID，对应T_Area.recId |
- **关联关系**：
  - T_Area.areaId = T_Area.recId
  - T_Area.cityId = T_Area.recId
  - T_Area.continentId = T_Area.recId
  - T_Area.countryId = T_Area.recId
  - T_Area.parentId = T_Area.recId
  - T_Area.provinceId = T_Area.recId

---

#### 3 系统日志 ( T_AtomLog )
- **业务含义**：系统日志
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| fileName | string | 是 | - | 文件名 |
| msgs | string | 是 | - | 异常标识码 |
| content | string | 是 | - | 详情 |
| note | string | 是 | - | 备注 |
| createTime | DateTime? | 是 | - | 操作时间 |
| userId | int? | 是 | - | 用户 |
| ttype | string | 是 | - | 类型；Error: 异常 |
- **关联关系**：无

---

#### 4 业务表 ( T_Business )
- **业务含义**：业务表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| businessSeting | string | 是 | - | 业务设置 |
| code | string | 是 | - | 代码 |
| enable | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 5 流程设计--流程分类 ( T_BusinessItem )
- **业务含义**：流程设计--流程分类
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| enable | bool? | 是 | - | 是否激活 |
| forms | string | 是 | - | 业务表单 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
| businessId | int? | 是 | - | 业务配置，对应T_Business.recId |
- **关联关系**：
  - T_BusinessItem.businessId = T_Business.recId

---

#### 6 等级管理表 ( T_Cate )
- **业务含义**：等级管理表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| type | string | 是 | - | 类型；SuppliersGrade 供应商等级
ClientGrade 客户等级
MaterialsGrade 物料等级
ProductGrade 成品等级
WIPGrade 半成品等级
ToolGrade 工具等级
EquipmentGrade 设备等级 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司 |
| shelfLife | int? | 是 | - | 保质期 |
| subCateId | int? | 是 | - | 子等级 |
| creditLimited | decimal? | 是 | - | 授权额度 |
| currencyId | int? | 是 | - | 币种 |
- **关联关系**：无

---

#### 7 物料类别表（物料分组 ( T_Category )
- **业务含义**：物料类别表（物料分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| bom | bool? | 是 | - | 是否用于BOM |
| classLevel | int? | 是 | - | 节点 |
| code | string | 是 | - | 代码 |
| customUnitEntry | bool? | 是 | - | 是否海关单位控制 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifSale | bool? | 是 | - | 是否销售 |
| indirectBOM | bool? | 是 | - | 是否间接BOM |
| inspection | bool? | 是 | - | 是否检查 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| materialTypeId | int? | 是 | - | 物料类型 |
| mfgDateEntry | bool? | 是 | - | 是否制造日期控制 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| reclaiming | bool? | 是 | - | 是否余料控制 |
| sort | string | 是 | - | 排序 |
| type | string | 是 | - | 类别，，材料还是配件等 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| inspectGroupId | int? | 是 | - | 检验分组，对应T_InspectGroup.recId |
| inspectPostId | int? | 是 | - | 检验岗位，对应T_PostRole.recId |
| parentId | int? | 是 | - | 上级物料类别，对应T_Category.recId |
| postRoleId | int? | 是 | - | 采购岗位，对应T_PostRole.recId |
| receiptPostId | int? | 是 | - | 接收岗位，对应T_PostRole.recId |
| shelfLife | int? | 是 | - | 保质期 |
| idfCode | string | 是 | - | 标识符 |
| serialNumber | int? | 是 | - | 当前编号 |
| rules | string | 是 | - | 生成规则 |
| ifLen | int? | 是 | - | 长 |
| ifWide | int? | 是 | - | 宽 |
| ifHigh | int? | 是 | - | 高 |
| ifSuppliers | int? | 是 | - | 供应商 |
| ifproductGroup | int? | 是 | - | 物料类型 |
| iftopCu | int? | 是 | - | 上铜 |
| ifbotCu | int? | 是 | - | 下铜 |
| ifdk | int? | 是 | - | 介电系数 |
| ifcolour | int? | 是 | - | 颜色 |
| iftg | int? | 是 | - | TG |
| ifhaligonfree | int? | 是 | - | 无卤素 |
| ifresin | int? | 是 | - | 含胶量 |
| iforgType | int? | 是 | - | 材料类型 |
| ifmaterialFamily | int? | 是 | - | 厂商型号 |
| qa | bool? | 是 | - | 保质期 |
| ifSupp | bool? | 是 | - | 供应商 |
| watermark | bool? | 是 | - | 水印 |
| expiryWay | string | 是 | - | 过期类型 |
| matIDStr | string | 是 | - | 物料标识符表达式 |
| ifcti | int? | 是 | - | 是否CTI |
| ifheatRate | int? | 是 | - | 导热系数 |
| ifMacLayerHigh | int? | 是 | - | 介质层厚度 |
| revMustSuppNo | bool? | 是 | - | 接收强制输入批号 |
| userDef01 | int? | 是 | - | 自定义属性01 |
| userDef02 | int? | 是 | - | 自定义属性02 |
| userDef03 | int? | 是 | - | 自定义属性03 |
| userDef04 | int? | 是 | - | 自定义属性04 |
| userDef05 | int? | 是 | - | 自定义属性05 |
| userDef06 | int? | 是 | - | 自定义属性06 |
| userDef07 | int? | 是 | - | 自定义属性07 |
| userDef08 | int? | 是 | - | 自定义属性08 |
| userDef09 | int? | 是 | - | 自定义属性09 |
| userDef10 | int? | 是 | - | 自定义属性10 |
| scrapRate | decimal? | 是 | - | 报废率 |
| ifThickCu | int? | 是 | - | 铜厚 |
| ifWatermark | int? | 是 | - | 水印 |
| ifAddTolerance | int? | 是 | - | 正公差 |
| ifSubTolerance | int? | 是 | - | 负公差 |
| userDef11 | int? | 是 | - | 自定义属性11 |
| userDef12 | int? | 是 | - | 自定义属性12 |
| userDef13 | int? | 是 | - | 自定义属性13 |
| userDef14 | int? | 是 | - | 自定义属性14 |
| userDef15 | int? | 是 | - | 自定义属性15 |
| userDef16 | int? | 是 | - | 自定义属性16 |
| userDef17 | int? | 是 | - | 自定义属性17 |
| userDef18 | int? | 是 | - | 自定义属性18 |
| userDef19 | int? | 是 | - | 自定义属性19 |
| userDef20 | int? | 是 | - | 自定义属性20 |
| ifBonded | bool? | 是 | - | 保税 |
| ifProcessSpecialMaterials | bool? | 是 | - | 是否工艺专用料；0: 否
1: 是 |
| spdsRequired | bool? | 是 | - | 强制SPDS |
| uniontransIndate | DateTime? | 是 | - | - |
| ifDepartmentSpecialMaterials | bool? | 是 | - | 是否部门专用料；0: 否
1: 是 |
- **关联关系**：
  - T_Category.companyId = T_Company.recId
  - T_Category.inspectGroupId = T_InspectGroup.recId
  - T_Category.inspectPostId = T_PostRole.recId
  - T_Category.parentId = T_Category.recId
  - T_Category.postRoleId = T_PostRole.recId
  - T_Category.receiptPostId = T_PostRole.recId

---

#### 8 物料类别明细表（储区） ( T_CategoryItem )
- **业务含义**：物料类别明细表（储区）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| version | int? | 是 | - | 记录版本 |
| categoryId | int? | 是 | - | 物料分组，对应T_Category.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| locationId | int? | 是 | - | 储区 |
| sobomPR | bool? | 是 | - | - |
- **关联关系**：
  - T_CategoryItem.categoryId = T_Category.recId
  - T_CategoryItem.companyId = T_Company.recId

---

#### 9 附加费用 ( T_ChargeItem )
- **业务含义**：附加费用
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| taxRate | decimal? | 是 | - | - |
| type | string | 是 | - | 类型：EndProductCharge 成品附加费  PurchaseCharge 采购附加费 |
| version | int? | 是 | - | - |
| saleProjectId | int? | 是 | - | 销售项目，对应S_SaleProject.recId |
- **关联关系**：
  - T_ChargeItem.saleProjectId = S_SaleProject.recId

---

#### 10 公司管理 ( T_Company )
- **业务含义**：公司管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| address | string | 是 | - | 地址 |
| code | string | 是 | - | 代码 |
| email | string | 是 | - | 邮箱 |
| fax | string | 是 | - | 传真 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifCreateSaleContract | bool? | 是 | - | 生成销售合同 |
| ifPR | bool? | 是 | - | 外协请购 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| linkman | string | 是 | - | 联系人 |
| mobilePhone | string | 是 | - | 手机 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| nickName | string | 是 | - | 简称 |
| note | string | 是 | - | 备注 |
| postType | string | 是 | - | 结账方式： M 月度 Y 年度 |
| prodType | string | 是 | - | 加工方式：Self 自制 Internal 内部外发 Outsourcing 外部外发 |
| sort | string | 是 | - | 排序 |
| telephone | string | 是 | - | 固话 |
| version | int? | 是 | - | 记录版本 |
| webSite | string | 是 | - | 网址 |
| zip | string | 是 | - | 邮编 |
| currencyId | int? | 是 | - | 币种，对应T_Currency.recId |
| plantBusinessId | int? | 是 | - | 工厂业务，对应F_PlantBusiness.recId |
| soPrice | string | 是 | - | - |
| forecastPrice | string | 是 | - | - |
| enableFinance | bool? | 是 | - | 启用财务 |
| custDateShipment | bool? | 是 | - | 按客户交期出货 |
| shipmentWay | int? | 是 | - | 出货方式 |
| costCountWay | int? | 是 | - | 成本核算方式 |
| soPackingList | bool? | 是 | - | 订单装箱 |
| spdsPriceConsignMat | bool? | 是 | - | 寄售PO从SPDS取价 |
| costCount | bool? | 是 | - | 月结前成本核算 |
| stockCheckWay | int? | 是 | - | 活动盘点 |
| eaddress | string | 是 | - | 英文地址 |
| ename | string | 是 | - | 英文名称 |
| autoXChange | bool? | 是 | - | NC单据审核后自动执行 |
| ospoRecBySubmit | bool? | 是 | - | 外协订单提交可接收 |
| packingFromMI | bool? | 是 | - | 包装信息来自MI |
| custReconcileXml | string | 是 | - | 销售对账导出配置 |
| purchReconcilexML | string | 是 | - | 采购对账导出配置 |
| shelfLifeDef | string | 是 | - | 保质期 |
| shipmentByReplenishment | bool? | 是 | - | 补货单独出货 |
| pzViewParent | bool? | 是 | - | 凭证显示上级科目名称 |
| assetAddPz | bool? | 是 | - | 固定资产创建产生凭证 |
| toolAutoRev | bool? | 是 | - | 工具接收自动登记 |
| ifCustoms | bool? | 是 | - | 报关单 |
| invPzAloneDo | bool? | 是 | - | 发票和凭证分开处理 |
| ifEstimate | bool? | 是 | - | 暂估流程 |
| packDirScaStock | bool? | 是 | - | 箱包直接扫描出货 |
| dueFromInvDate | bool? | 是 | - | 到期日基于发票日 |
| ifCloseReq | bool? | 是 | - | 关闭请款单 |
| ifEnableSQ | bool? | 是 | - | - |
| poType | bool? | 是 | - | 采购类型 |
| prodInst | bool? | 是 | - | - |
| lineWare | bool? | 是 | - | 线边仓 |
| pzFDFromInvDate | int? | 是 | - | 采购发票凭证期间来源 |
| notAssignerCanEditMI | bool? | 是 | - | 非分配者可编辑工程资料 |
| ifCompanyIQCGroup | bool? | 是 | - | 按公司制订物料检验分组 |
| processFilterByPanelType | bool? | 是 | - | 按板件类型过滤工艺 |
| ifCompanyShipment | bool? | 是 | - | 按公司出货 |
| defaultPlantId | int? | 是 | - | MI默认工厂 |
| miCopyRePlaceInnerLay | bool? | 是 | - | MI拷贝替换内层部件代码 |
| miFilePathWithPnAndVer | bool? | 是 | - | 用编号+版本号做MI附件路径 |
| soOwe | bool? | 是 | - | 订单欠数入库 |
| poPriceDigit | int? | 是 | - | 采购价格位数 |
| mirevFromSelf | bool? | 是 | - | MI版本检查来源于自身编号 |
| revMatByCompany | bool? | 是 | - | 按公司接收工厂物料 |
| giftDz | bool? | 是 | - | 赠品对账 |
| ifMulMICoding | bool? | 是 | - | 多工厂MI编码 |
| bagsBatch | bool? | 是 | - | 批次箱数管理 |
| matAutoSysBat | bool? | 是 | - | 物料入仓使用系统批次 |
| matMonthlyByConsign | bool? | 是 | - | 物料月结来自寄售处理 |
| defRackByLast | bool? | 是 | - | 入仓默认上次货位 |
| accountTile | bool? | 是 | - | 结转平铺 |
| mesInitControl | bool? | 是 | - | MES初始化控制 |
| currExchAdjTile | bool? | 是 | - | 调汇凭证平铺 |
| customerSupply | bool? | 是 | - | 客供料 |
| dullWareActive | bool? | 是 | - | 呆滞仓可用 |
| mrpDateType | string | 是 | - | Mrp订单统计 |
| sameScraprateAllMfg | bool? | 是 | - | 强制Job与外层报废率一致 |
| poReceiveCheck | bool? | 是 | - | 采购接收控制 |
| woOSAdvance | bool? | 是 | - | 允许预先工单外协请购/采购 |
| dgRevOutPutData | bool? | 是 | - | 转厂回收产生过数记录 |
| allowShortAssignment | bool? | 是 | - | 允许短装出库 |
| autoAssignShipJob | bool? | 是 | - | 客诉来自出货料号 |
| sheetUsedRateDispPercent | bool? | 是 | - | 大料利用率显示百分比 |
| excludeUnavailableStockQty | bool? | 是 | - | 物料呆滞仓线边仓不可用 |
| fgiUnitPriceIncludeAllScrap | bool? | 是 | - | 成品入库单价包含全报废 |
| viaHoleAttr | bool? | 是 | - | Via孔属性 |
| limitMonthly | int? | 是 | - | 锁账月份 |
| saleDzMonUp | int? | 是 | - | 销售对账推后月数 |
| complainmentWithoutInvoiced | bool? | 是 | - | 客诉不校验开票数 |
| mrpPRFromReqDate | int? | 是 | - | MRP生成请购方式 |
| mrpLastMORepSOBom | bool? | 是 | - | MRP最近投产替换SOBom |
| saleItemAmountDeg | int? | 是 | - | 销售明细金额精度 |
| miShowMfgpartParams | bool? | 是 | - | 工程设计显示子部件参数 |
| daysAheadSampleProd | int? | 是 | - | 样板投产提前天数 |
| useCustPriority | bool? | 是 | - | 设置客户排产级别 |
| osRepairSeparateBatch | bool? | 是 | - | 外协成品返修分批次入库 |
| isCalCostDetails | bool? | 是 | - | 计算成本明细项 |
| ignoreRPModule | string | 是 | - | 忽略外协请购 |
| identificationCode | string | 是 | - | 财务 |
| salesDataIsolation | bool? | 是 | - | 销售循环岗位隔离 |
| carrierPlate | bool? | 是 | - | 载板特性 |
| poItemSortOrder | string | 是 | - | 采购明细显示顺序 |
| notAllowDuplicateSteps | int? | 是 | - | MO不允许重复工艺 |
| newAccStd | bool? | 是 | - | 新会计准则 |
| boxShipWay | int? | 是 | - | 箱包出货方式 |
| brokenMatNotInWoCost | bool? | 是 | - | 碎料不计入工单成本 |
| requiredParamCheckNull | bool? | 是 | - | 工程设计必填流程参数空值检查 |
| bagShipUnCheckDateCode | bool? | 是 | - | 箱包出货不检查周期码 |
| addChargeReconcile | bool? | 是 | - | 额外费明细项对账 |
| miBomDispStandard | bool? | 是 | - | 工程设计BOM显示材料规格 |
| boxInBatOutStock | bool? | 是 | - | 箱包入库按批次出库 |
| enablePurchaseBudget | bool? | 是 | - | 启用采购预算 |
| spdsPriceWay | string | 是 | - | 采购受理取价方式 |
| isAssignmentConfirm | bool? | 是 | - | 订单出库需要确认 |
| selectOrdersByCustomer | bool? | 是 | - | 出货计划按客户选择订单 |
| packbagInventoryNoFinishedTransfer | bool? | 是 | - | 箱包库存不能进行成品转仓 |
| pzFDFromInvDate2 | int? | 是 | - | 销售发票凭证期间来源 |
- **关联关系**：
  - T_Company.currencyId = T_Currency.recId
  - T_Company.plantBusinessId = F_PlantBusiness.recId

---

#### 11 币种 ( T_Currency )
- **业务含义**：币种
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| baseFlag | bool? | 是 | - | 是否是本币 |
| code | string | 是 | - | 代码 |
| createDate | DateTime? | 是 | - | 建单日期 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 12 币种兑换明细 ( T_CurrencyItem )
- **业务含义**：币种兑换明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| exchRate | decimal? | 是 | - | 汇率 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| transDate | DateTime? | 是 | - | 建单日期 |
| version | int? | 是 | - | - |
| baseCurrId | int? | 是 | - | 本币货币，对应T_Currency.recId |
| currencyId | int? | 是 | - | 货币名称，对应T_Currency.recId |
- **关联关系**：
  - T_CurrencyItem.baseCurrId = T_Currency.recId
  - T_CurrencyItem.currencyId = T_Currency.recId

---

#### 13 自定义脚本 ( T_CustomScript )
- **业务含义**：自定义脚本
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| isActive | bool? | 是 | - | 是否激活 |
| notes | string | 是 | - | 备注 |
| runMode | bool? | 是 | - | 是否运行模式 |
| scriptCode | string | 是 | - | 代码 |
| scriptName | string | 是 | - | 名称 |
| scripts | string | 是 | - | 脚本 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| version | int? | 是 | - | 记录版本 |
| plantsId | int? | 是 | - | 工厂 |
| isWasteScript | bool? | 是 | - | - |
- **关联关系**：无

---

#### 14 自定义表 ( T_CustTable )
- **业务含义**：自定义表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 15 自定义表明细 ( T_CustTableValue )
- **业务含义**：自定义表明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 16 缺陷表 ( T_Defect )
- **业务含义**：缺陷表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 缺陷代码 |
| ifActive | bool? | 是 | - | 是否激活 0否  1是 |
| ifMaterials | bool? | 是 | - | 是否用于物料 0否  1是 |
| ifProduct | bool? | 是 | - | 是否用于成品 0否  1是 |
| ifWIP | bool? | 是 | - | 是否用于WIP 0否  1是 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 缺陷名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| type | string | 是 | - | 类型： Repair返修 Return退货 Defect特采 Scrapped 报废 |
| version | int? | 是 | - | - |
| ifSpecial | bool? | 是 | ((0)) | 是否用于特定 0否  1是 |
- **关联关系**：无

---

#### 17 部门表 ( T_Department )
- **业务含义**：部门表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| type | string | 是 | - | 部门:D,部门主管领导:CL,部门经理:L,部门主管:DL,部门接收人:RP |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| parentId | int? | 是 | - | 上一级部门ID，对应T_Department.recId |
- **关联关系**：
  - T_Department.companyId = T_Company.recId
  - T_Department.parentId = T_Department.recId

---

#### 18 部门--用户表 ( T_DepartmentUser )
- **业务含义**：部门--用户表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人呢 |
| version | int? | 是 | - | - |
| departmentId | int? | 是 | - | 部门表，对应T_Department.recId |
| userId | int? | 是 | - | 用户表，对应T_User.recId |
- **关联关系**：
  - T_DepartmentUser.departmentId = T_Department.recId
  - T_DepartmentUser.userId = T_User.recId

---

#### 19 文件上传记录 ( T_Document )
- **业务含义**：文件上传记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| attachId | string | 是 | - | - |
| contentType | string | 是 | - | 文件类型 |
| createDate | DateTime? | 是 | - | 创建时间 |
| creator | string | 是 | - | 创建人 |
| dayPath | string | 是 | - | - |
| fileSize | int? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | - |
| miPrint | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| monthPath | string | 是 | - | - |
| name | string | 是 | - | - |
| note | string | 是 | - | - |
| type | string | 是 | - | 对应模块类型 |
| typeId | string | 是 | - | 对应模块RECID |
| url | string | 是 | - | - |
| version | int? | 是 | - | - |
| woPrint | bool? | 是 | - | - |
| yearPath | string | 是 | - | - |
| fileType | string | 是 | - | 文件类型(1:采购订单回签) |
- **关联关系**：无

---

#### 20 导出设置 ( T_ExportSetting )
- **业务含义**：导出设置
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| ifActive | bool? | 是 | - | 是否激活 |
| version | int? | 是 | - | 记录版本 |
| modifiedBy | string | 是 | - | 更新人员 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| retryTimes | int? | 是 | - | 重试次数 |
- **关联关系**：无

---

#### 21 导出设置明细 ( T_ExportSettingItem )
- **业务含义**：导出设置明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| settingId | int? | 是 | - | 导出设置 |
| plantId | int? | 是 | - | 工厂 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 22 导出设置URL ( T_ExportSettingUrl )
- **业务含义**：导出设置URL
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| settingId | int? | 是 | - | 导出设置 |
| url | string | 是 | - | URL |
| version | int? | 是 | - | 记录版本 |
| sort | string | 是 | - | 排序 |
| type | string | 是 | - | 类型 |
| authorizationId | string | 是 | - | - |
- **关联关系**：无

---

#### 23 会计期间 ( T_FiscalPeriod )
- **业务含义**：会计期间
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ending | DateTime? | 是 | - | 结束日期 |
| ifClose | bool? | 是 | - | 是否关闭 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| period | int? | 是 | - | 期间 |
| starting | DateTime? | 是 | - | 开始日期 |
| type | string | 是 | - | Month 月 Year 年 |
| version | int? | 是 | - | - |
| year | int? | 是 | - | 年度 |
- **关联关系**：无

---

#### 24 流程设计主表 ( T_Flow )
- **业务含义**：流程设计主表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| content | string | 是 | - | - |
| deploymentId | string | 是 | - | - |
| flowVersion | int? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| modifiedBy | string | 是 | - | 更新人员 |
| note | string | 是 | - | - |
| pdId | string | 是 | - | 流程定义标示 |
| publish | bool? | 是 | - | - |
| publishTime | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| flowTypeId | int? | 是 | - | 审批流程设置，对应T_FlowType.recId |
- **关联关系**：
  - T_Flow.flowTypeId = T_FlowType.recId

---

#### 25 流程设计 ( T_FlowType )
- **业务含义**：流程设计
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| enable | bool? | 是 | - | 是否禁用 |
| flow | bool? | 是 | - | 是否用于流程 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| uniqueid | string | 是 | - | - |
| version | int? | 是 | - | - |
| businessId | int? | 是 | - | 业务表，对应T_Business.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| parentId | int? | 是 | - | 上一级流程设计，对应T_FlowType.recId |
| userId | int? | 是 | - | 用户，对应T_User.recId |
- **关联关系**：
  - T_FlowType.businessId = T_Business.recId
  - T_FlowType.companyId = T_Company.recId
  - T_FlowType.parentId = T_FlowType.recId
  - T_FlowType.userId = T_User.recId

---

#### 26 贸易方式 ( T_FOB )
- **业务含义**：贸易方式
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 27 系统模块功能表 ( T_FunctionRight )
- **业务含义**：系统模块功能表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| extParameters | string | 是 | - | - |
| functionCode | string | 是 | - | 模块代码 |
| functionEName | string | 是 | - | 模块简称名 |
| functionName | string | 是 | - | 模块简称名称 |
| ifActive | bool? | 是 | - | 是否禁用 |
| ifDefault | bool? | 是 | - | 是否默认 |
| ifOrderId | bool? | 是 | - | - |
| ifUser | bool? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
| moduleId | int? | 是 | - | 模块表，对应T_Module.recId |
- **关联关系**：
  - T_FunctionRight.moduleId = T_Module.recId

---

#### 28 用户组管理 ( T_Group )
- **业务含义**：用户组管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 29 用户组--用户 ( T_GroupUser )
- **业务含义**：用户组--用户
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
| groupId | int? | 是 | - | 用户组管理，对应T_Group.recId |
| userId | int? | 是 | - | 用户，对应T_User.recId |
- **关联关系**：
  - T_GroupUser.groupId = T_Group.recId
  - T_GroupUser.userId = T_User.recId

---

#### 30 检验分组--检验项目 ( T_Inspect )
- **业务含义**：检验分组--检验项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| version | int? | 是 | - | - |
| inspectGroupId | int? | 是 | - | 检验分组，对应T_InspectGroup.recId |
| inspectItemsId | int? | 是 | - | 检验项目，对应T_InspectItems.recId |
- **关联关系**：
  - T_Inspect.inspectGroupId = T_InspectGroup.recId
  - T_Inspect.inspectItemsId = T_InspectItems.recId

---

#### 31 检验分组 ( T_InspectGroup )
- **业务含义**：检验分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifFGI | bool? | 是 | - | 是否用于制成品分组 |
| ifRM | bool? | 是 | - | 是否用于RM |
| ifWIP | bool? | 是 | - | 是否用于WIP |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 32 检验项目 ( T_InspectItems )
- **业务含义**：检验项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifFGI | bool? | 是 | - | 是否用于制成品分组 |
| ifRM | bool? | 是 | - | 是否用于RM |
| ifWIP | bool? | 是 | - | 是否用于WIP |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| method | string | 是 | - | 检验方法 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sample | string | 是 | - | 检验样本 |
| sort | string | 是 | - | - |
| standard | string | 是 | - | 检验标准 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 33 盘点原因 ( T_InventoryCheckReason )
- **业务含义**：盘点原因
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifMaterials | bool? | 是 | - | 是否用于物料盘点 |
| ifProduct | bool? | 是 | - | 是否用于成品 |
| ifWIP | bool? | 是 | - | 是否用于WIP |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 34 JSON接口日志 ( T_JSONHistory )
- **业务含义**：JSON接口日志
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| action | bool? | 是 | - | 动作；0: 导出
1: 导入 |
| type | string | 是 | - | 类型；Supplier: 供应商
prImport: 请购单
MaterialStock: 物料入库
NormIssue: 部门领料
NormReturn: 部门退料
BOMIssue: BOM发料
BOMReturn: BOM退料
SuppReturn:供应商退货
NoPoReturn: 客供料退货
M_PHCount: 物料盘点
AllocateOut: 物料公司内调出
AllocateIn: 物料公司内调入
TransferOut: 物料公司间调出
TransferResult: 物料公司间调出结果
LockStock: 物料锁定
MaterialOut:物料报废
Customer: 客户
soChange: 订单变更
osPRonHold: 外协请购
osPOonHold: 外协采购
osPOout: 外协装运
osPOreturn: 外协发放
FGIReturnOrder: 外协退货
MI: 工程设计
MO: 制造订单
operationInst: 投产指示
WOStatus:工单状态变更
woHold: 暂缓工单
woCancel: 取消工单
reactive: 激活工单
stepHold: 暂缓工序
undo:撤销工序暂缓
splitLot:拆分工单
reworkRaise: 工单返工
shopFloorInOut: 工单过数
plantTFSent: 转厂接收
plantTFBack: 代工回收
WorkOrderUpgrade: 工单升级
WIPCount: 工序盘点
FGIInspRequest: 成品检验单
FGIInspection: 成品检验结果
mrbImport: MRB报废
FGIRecheck:成品送检
OutCP: 成品报废
FGI_Production:成品入库
FGI_Outsource: 外协入库
FGI_Direct: 成品直接入仓
FGI_Return: 销售退货
FGI_PartedIn: 半成品入仓
MaterialSale: 原材料销售出库
OutSo: 销售出库
FGI_PHCount: 成品盘点
toCustomer: 客户
toSupplier: 供应商
toInventory: 存货档案
toBomMaterialOut: 材料出库
toPurchaseOrder: 采购单
toReceive: 收货单
toDispatchReturn: 退货单
MoRoutingBill: 订单工序报工
RequisitOrder: 请购单
Operation: 工序
Routing: 工艺路线
ProductIn: 成品入库
BOM: 物料清单
OMOrder: 物料清单
ProductionOrder: 生产订单
ProductIn: 产成品入库
SaleInvoice: 销售发票
PurchaseInvoice: 采购发票
UniontransInterface: 协同平台接口 |
| code | string | 是 | - | 代码 |
| uniqueTag | string | 是 | - | 唯一标识 |
| status | int? | 是 | - | 状态；0: 成功
1: 失败 |
| content | string | 是 | - | 报文 |
| result | string | 是 | - | 结果 |
| retryTimes | int? | 是 | - | 重试次数 |
| url | string | 是 | - | URL |
| apitime | DateTime? | 是 | - | 接口调用时间 |
- **关联关系**：无

---

#### 35 联系人 ( T_Linkman )
- **业务含义**：联系人
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| email | string | 是 | - | 邮箱 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| loginName | string | 是 | - | 代码 |
| mobilePhone | string | 是 | - | 固话 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| password | string | 是 | - | 密码 |
| telephone | string | 是 | - | 联系电话 |
| type | string | 是 | - | Customer 客户  Suppliers 供应商 |
| typeId | int? | 是 | - | 供应商ID，对应M_Suppliers.recId |
| version | int? | 是 | - | - |
- **关联关系**：
  - T_Linkman.typeId = M_Suppliers.recId

---

#### 36 储区表 ( T_Location )
- **业务含义**：储区表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| classLevel | int? | 是 | - | 节点 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sceneWare | bool? | 是 | - | 是否用于现场仓(WIP) |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| parentId | int? | 是 | - | 上一级仓位，对应T_Location.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - T_Location.companyId = T_Company.recId
  - T_Location.parentId = T_Location.recId
  - T_Location.stepsId = T_Steps.recId
  - T_Location.warehouseId = T_Warehouse.recId

---

#### 37 模块表 ( T_Module )
- **业务含义**：模块表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifUser | bool? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| moduleCode | string | 是 | - | 模块代码 |
| moduleEName | string | 是 | - | 模块简称 |
| moduleName | string | 是 | - | 名称名称 |
| sort | string | 是 | - | - |
| type | string | 是 | - | Function 模块  Report 报表 |
| version | int? | 是 | - | - |
| parentId | int? | 是 | - | 上一级模块ID，对应T_Module.recId |
- **关联关系**：
  - T_Module.parentId = T_Module.recId

---

#### 38 模组类型 ( T_ModuleType )
- **业务含义**：模组类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 39 用户模块权限表 ( T_MyModule )
- **业务含义**：用户模块权限表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| createTime | DateTime? | 是 | - | 制单时间 |
| userId | int? | 是 | - | 用户表，对应T_User.recId |
- **关联关系**：
  - T_MyModule.userId = T_User.recId

---

#### 40 记事本 ( T_Notepad )
- **业务含义**：记事本
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| notepad | string | 是 | - | 记事本 |
| version | int? | 是 | - | 记录版本 |
| notepadGroupId | int? | 是 | - | 记事分组，对应T_NotepadGroup.recId |
| sort | string | 是 | - | 排序 |
- **关联关系**：
  - T_Notepad.notepadGroupId = T_NotepadGroup.recId

---

#### 41 记事分组表 ( T_NotepadGroup )
- **业务含义**：记事分组表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| ttype | string | 是 | - | 类型 |
- **关联关系**：
  - T_NotepadGroup.companyId = T_Company.recId

---

#### 42 单据号码表 ( T_NumberControl )
- **业务含义**：单据号码表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| numberMedian | int? | 是 | - | 流水号位 |
| plantId | int? | 是 | - | - |
| prefix | string | 是 | - | 单据前缀 |
| rules | string | 是 | - | 生成规则 |
| serialNumber | int? | 是 | - | 序号 |
| tmonth | int? | 是 | - | - |
| type | string | 是 | - | 类型 |
| version | int? | 是 | - | - |
| way | string | 是 | - | 编码级别：Group 集团级别编号 Company 公司级别编号 Plant 工厂级别编号 |
- **关联关系**：
  - T_NumberControl.companyId = T_Company.recId

---

#### 43 付款方式 ( T_PaymentMethod )
- **业务含义**：付款方式
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 44 付款周期 ( T_PaymentTerm )
- **业务含义**：付款周期
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| ptDate | int? | 是 | - | 付款周期 |
| ptDays | int? | 是 | - | 付款日期 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
| way | string | 是 | - | 付款到期计算方法：Monthly 月结天数法 Open 开票天数法 |
- **关联关系**：无

---

#### 45 工厂 ( T_Plants )
- **业务含义**：工厂
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| address | string | 是 | - | 地址 |
| code | string | 是 | - | 代码 |
| DEFAULT_FLG | bool? | 是 | - | 是否默认工厂 |
| email | string | 是 | - | 邮箱 |
| fax | string | 是 | - | 传真 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| mfgPartsIssueWay | string | 是 | - | 部件发放方式 |
| mobilePhone | string | 是 | - | 固话 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| shippingWarehouseId | int? | 是 | - | 出货仓，对应T_Warehouse.recId |
| stockingWarehouseId | int? | 是 | - | 备件仓，对应T_Warehouse.recId |
| telephone | string | 是 | - | 联系电话 |
| version | int? | 是 | - | 记录版本 |
| wipWarehouseId | int? | 是 | - | WIP仓库，对应T_Warehouse.recId |
| AP_CASH_DISCOUNT_ACCID | int? | 是 | - | 科目管理，对应F_Accounts.recId |
| AP_Exhange_Gain_ACCID | int? | 是 | - | 汇兑收益，对应F_Accounts.recId |
| AP_Exhange_Loss_ACCID | int? | 是 | - | 汇兑损失，对应F_Accounts.recId |
| AP_Misc_ACCID | int? | 是 | - | 应付杂项，对应F_Accounts.recId |
| AP_Tax_IN_ACCID | int? | 是 | - | 进项税，对应F_Accounts.recId |
| AR_CASH_DISCOUNT_ACCID | int? | 是 | - | 销售折扣，对应F_Accounts.recId |
| AR_CostSold_ACCID | int? | 是 | - | 销售成本，对应F_Accounts.recId |
| AR_Exhange_Gain_ACCID | int? | 是 | - | 汇兑收益，对应F_Accounts.recId |
| AR_Exhange_Loss_ACCID | int? | 是 | - | 汇兑损失，对应F_Accounts.recId |
| AR_Misc_ACCID | int? | 是 | - | 应收杂项，对应F_Accounts.recId |
| AR_Others_Revenue_AccID | int? | 是 | - | 非主营业务收入，对应F_Accounts.recId |
| AR_Product_Revenue_AccID | int? | 是 | - | 主营业务收入，对应F_Accounts.recId |
| AR_Tax_OUT_ACCID | int? | 是 | - | 销项税，对应F_Accounts.recId |
| bankAccountId | int? | 是 | - | 银行存款，对应F_Accounts.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| currentProfitId | int? | 是 | - | 本年利润，对应F_Accounts.recId |
| FG_Inventory_ACCID | int? | 是 | - | 成品存货科目，对应F_Accounts.recId |
| FG_PC_ACCID | int? | 是 | - | 成品盘亏科目，对应F_Accounts.recId |
| FG_Reject_ACCID | int? | 是 | - | 成品报废科目，对应F_Accounts.recId |
| incomeTaxId | int? | 是 | - | 所得税，对应F_Accounts.recId |
| investmentIncomeId | int? | 是 | - | 投资收益，对应F_Accounts.recId |
| OutSource_ACCID | int? | 是 | - | 外发加工费，对应F_Accounts.recId |
| profitAllotId | int? | 是 | - | 利润分配，对应F_Accounts.recId |
| RM_DM_ISSUE_ACCID | int? | 是 | - | 对应F_Accounts.recId |
| RM_IDM_ISSUE_ACCID | int? | 是 | - | 辅料发放科目，对应F_Accounts.recId |
| RM_INVENTORY_ACCID | int? | 是 | - | 物料存货，对应F_Accounts.recId |
| RM_PC_ACCID | int? | 是 | - | 盘亏调整科目，对应F_Accounts.recId |
| RM_PM_ISSUE_ACCID | int? | 是 | - | 维修发放科目，对应F_Accounts.recId |
| RM_REJECT_ACCID | int? | 是 | - | 物料报废科目，对应F_Accounts.recId |
| orderPut | bool? | 是 | ((1)) | 按订单投产 |
| throughputPCS | int? | 是 | ((0)) | 日产出PCS数 |
| throughputArea | int? | 是 | ((0)) | 日产出面积数 |
| days | int? | 是 | ((7)) | 天数 |
| deliveryCheck | string | 是 | ('OrderDelivery') | 检查方式 |
| soLoadingCheck | string | 是 | ('PCS') | 订单检查 |
| outputWay | string | 是 | ('IN') | 过数方式 |
| autoPrintWO | bool? | 是 | ((0)) | 工单发放自动打印 |
| conversionFactor | decimal? | 是 | ((0)) | - |
| osIqcPostId | int? | 是 | - | 外协检验岗位 |
| repairIqcPostId | int? | 是 | - | 返修检验岗位 |
| mulSOVote | bool? | 是 | - | - |
| blendIssue | bool? | 是 | - | - |
| wipStock | bool? | 是 | - | - |
| ifForecast | bool? | 是 | ((0)) | - |
| return_os_receiptWIP | bool? | 是 | - | - |
| return_receiptWIP | bool? | 是 | - | - |
| fgiMarginCount | string | 是 | - | 余量统计 |
| ifLotOutputSeq | bool? | 是 | - | - |
| ifAutoWipBacklog | bool? | 是 | - | 自动工序月结 |
| wipBacklogTime | string | 是 | - | 工序月结时间 |
| osPrice | int? | 是 | - | 外协单价位数 |
| fgiStockWay | string | 是 | - | 成品出库方式 |
| ifOSWOAutoIqc | bool? | 是 | - | 工单外协自动生成检验单 |
| stepStayWay | string | 是 | - | 工序滞留时间 |
| poPlantId | int? | 是 | - | - |
| idfCode | string | 是 | - | 标识符 |
| qtyPanelOfWO | int? | 是 | - | MO工单最小板数 |
| unMOLackMat | bool? | 是 | - | 材料不足禁止开MO |
| xoutWarehouseId | int? | 是 | - | 叉品仓 |
| shipCheckPrepaid | bool? | 是 | - | 出货检查预收款 |
| checkIssueOfWOSend | bool? | 是 | - | 未发料禁止工单发放 |
| shippingLocationId | int? | 是 | - | 出货区 |
| RM_PCAdd_ACCID | int? | 是 | - | 盘赢调整科目 |
| FG_WorkValue_ACCID | int? | 是 | - | 在制品价值 |
| FG_Rework_ACCID | int? | 是 | - | 成品返修 |
| Cost_Product_ACCID | int? | 是 | - | 主营业务成本 |
| FG_PCADD_ACCID | int? | 是 | - | 成品盘赢科目 |
| ifWareHouseStock | bool? | 是 | - | 按仓库出货 |
| ifPanelBOtherMI | bool? | 是 | - | AB板允许B板换料号 |
| ifFreeShipCheck | bool? | 是 | - | 禁止赠品超出 |
| pickMatUseDay | int? | 是 | - | 领料没提交占用天数 |
| stepStockCodeRevNum | int? | 是 | - | 工序结存本厂编号版本唯一位数 |
| splitQtys | int? | 是 | - | 拆单次数 |
| creditMemoAccountId | int? | 是 | - | 客户扣款 |
| issueGoodsAccountId | int? | 是 | - | 发出商品 |
| issueGoodsVmiAccountId | int? | 是 | - | 发出商品-寄售 |
| AR_Product_Revenue_fo_AccID | int? | 是 | - | - |
| Cost_Product_fo_ACCID | int? | 是 | - | 外销主营业务成本 |
| issueGoodsFoAccountId | int? | 是 | - | 外销发出商品 |
| issueGoodsVmiFoAccountId | int? | 是 | - | 外销发出商品-寄售 |
| lineWareAccountId | int? | 是 | - | 线边仓 |
| bomWarehouseId | int? | 是 | - | BOM仓 |
| matIssueGoodsAccountId | int? | 是 | - | 物料发出商品 |
| matSaleCostAccountId | int? | 是 | - | 物料销售成本 |
| matSaleInAccountId | int? | 是 | - | 物料销售收入 |
| scrapRateDays | int? | 是 | - | 报废率天数 |
| bFKsProcessId | string | 是 | - | 报废扣数工艺 |
| auto_MOBOM | bool? | 是 | - | 自动产生配料单 |
| bFKsRbProcessId | string | 是 | - | - |
| workingProjectAccId | int? | 是 | - | - |
| altColor | string | 是 | - | 预警颜色时间 |
| preScrapOfPartNumer | bool? | 是 | - | 预报废扣数来自生产编号 |
| partNumerCutForward | bool? | 是 | - | 预扣数生产编号向前截取 |
| steelPlantId | int? | 是 | - | - |
| postIssueControl | string | 是 | - | 工单过数发料控制 |
| bomCounting | bool? | 是 | - | Bom计算用量 |
| mfgStepId | int? | 是 | - | - |
| unCheckXou | bool? | 是 | - | 成品入库不检查叉板配对 |
| autoCreateBomPicking | bool? | 是 | - | MO下单自动创建领料单 |
| unOrderPicking | bool? | 是 | - | 非开单Bom领料 |
| stockByTheSameMO | bool? | 是 | - | 生产入库区分MO |
| processId | int? | 是 | - | 包装工艺 |
| fgiPickAccId | int? | 是 | - | - |
| outPutCheckDc | bool? | 是 | - | 过数检查周期码 |
| dcFormat | string | 是 | - | 内置周期码格式 |
| maxSampleOutput | int? | 是 | - | 样品最大投产量 |
| packingWay | string | 是 | - | 包装形式 |
| stockUnit | string | 是 | - | 入库最小单位 |
| packingBat | string | 是 | - | 批次入库方式 |
| mrbExcReportMaxPnl | int? | 是 | - | MRB报废自动异常报告阀值 |
| mrbStopWOMaxPnl | int? | 是 | - | MRB报废自动暂停工单阀值 |
| outputQualityWarning | bool? | 是 | - | 过数显示品质警示 |
| outPutPassCheck | bool? | 是 | - | 过数密码验证 |
| batchWO | bool? | 是 | - | 多批次开工单 |
| saveEquipmentForRetrospect | bool? | 是 | - | 接收登记追溯加工设备 |
| checkIssueOfWOPrint | bool? | 是 | - | 未发料禁止列印工单 |
| mfgWarehouseId | int? | 是 | - | 半成品仓 |
| devCostAccId | int? | 是 | - | - |
| wipTransferAccId | int? | 是 | - | - |
| scrapWoCostAccId | int? | 是 | - | - |
| deadCostAccId | int? | 是 | - | - |
| checkCostAccId | int? | 是 | - | - |
| defaultFilmMode | string | 是 | - | 叠构默认干膜方式 |
| fileSite | string | 是 | - | 共享文件站点 |
| stackupImageDispThickTol | bool? | 是 | - | 叠构图显示厚度公差 |
| stackupThickUnit | string | 是 | - | 叠构图厚度单位 |
| mrbUseSteps | bool? | 是 | - | MRB检查按工序处理 |
| drillSizeDecimalPoint | int? | 是 | - | 钻孔尺寸小数点 |
| finishSizeUsedChar | bool? | 是 | - | 要求尺寸可输入字符 |
| stackupCanEditThick | bool? | 是 | - | 叠构能否修改厚度 |
| flexRigidUsedSameDrillFormat | bool? | 是 | - | 软硬板统一钻嘴表样式 |
| overProductPcs1 | int? | 是 | - | 超投PCS数量 |
| overProductPcs2 | int? | 是 | - | 超投PCS数量 |
| overProductPcs3 | int? | 是 | - | 超投PCS数量 |
| overProductPcs4 | int? | 是 | - | 超投PCS数量 |
| overProductPcs5 | int? | 是 | - | 超投PCS数量 |
| overProductRatio1 | decimal? | 是 | - | 超投比例限制 |
| overProductRatio2 | decimal? | 是 | - | 超投比例限制 |
| overProductRatio3 | decimal? | 是 | - | 超投比例限制 |
| overProductRatio4 | decimal? | 是 | - | 超投比例限制 |
| overProductRatio5 | decimal? | 是 | - | 超投比例限制 |
| overProductArea | decimal? | 是 | - | 超投面积限制 |
| woSendActiveUnFirstMatUse | bool? | 是 | - | 非首道用料工艺自动激活工单发放 |
| innerMfgStockWay | string | 是 | - | 内层入仓组件处理方式 |
| osPRRequiredSupplier | bool? | 是 | - | - |
| autoCreateMatIssueForm | bool? | 是 | - | - |
| stackupNoShowThickness | bool? | 是 | - | - |
| moAllocationFromSpareStock | bool? | 是 | - | - |
| unAltMatsMustFlowing | bool? | 是 | - | 非指定替代料MO走流程审批 |
| allowMRBScrapInUnit | bool? | 是 | - | - |
| onlyAllowToDeletePersonalDocuments | bool? | 是 | - | 只允许删除本人单据 |
| measurementResultsFile | string | 是 | - | 仪器测量结果文件夹 |
| finAccountSetNumber | string | 是 | - | 财务账套代码 |
| throughputMultiPCS | int? | 是 | - | 日产出多层板PCS数 |
| throughputMultiArea | int? | 是 | - | 日产出多层板面积数 |
| throughputLines | int? | 是 | - | 日产出款数 |
| throughputMultiLines | int? | 是 | - | 日产出多层板款数 |
- **关联关系**：
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

#### 46 岗位 ( T_PostRole )
- **业务含义**：岗位
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| type | string | 是 | - | 岗位类型：General 一般类型 MI 工程设计 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
- **关联关系**：
  - T_PostRole.companyId = T_Company.recId

---

#### 47 岗位模块 ( T_PostRoleModule )
- **业务含义**：岗位模块
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| version | int? | 是 | - | - |
| moduleId | int? | 是 | - | 等级管理表，对应T_Cate.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
- **关联关系**：
  - T_PostRoleModule.moduleId = T_Cate.recId
  - T_PostRoleModule.postRoleId = T_PostRole.recId

---

#### 48 工艺表 ( T_Process )
- **业务含义**：工艺表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifWorkStation | bool? | 是 | - | 是否工作站 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| modifiedBy | string | 是 | - | 更新人员 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| pcbABom | bool? | 是 | - | 是否PCBABBOM |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
| ifDateCode | bool? | 是 | ((0)) | 是否周期码 |
| vcut | bool? | 是 | - | 是否V-CUT |
| toolsType | string | 是 | - | 工具类型 |
| toolsNote | string | 是 | - | 工具备注 |
| isFlex | bool? | 是 | - | 是否软板 |
| isRigid | bool? | 是 | - | 是否硬板 |
| isSmt | bool? | 是 | - | 是否贴片 |
| isTooling | bool? | 是 | - | 是否工具 |
| mrb | bool? | 是 | - | MRB |
| iqcCheck | bool? | 是 | - | 是否品质检验 |
| ipqc | bool? | 是 | - | 是否IPQC |
| isTearing | bool? | 是 | - | 是否分板 |
| mfgIssueFlg | bool? | 是 | - | 是否内层组件发料工艺 |
- **关联关系**：无

---

#### 49 工艺缺陷报废 ( T_ProcessDefect )
- **业务含义**：工艺缺陷报废
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| seq | int? | 是 | - | 序号 |
| version | int? | 是 | - | 记录版本 |
| defectId | int? | 是 | - | 缺陷报废，对应T_Defect.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
- **关联关系**：
  - T_ProcessDefect.defectId = T_Defect.recId
  - T_ProcessDefect.processId = T_Process.recId

---

#### 50 工艺--雇员权限(工程设计流程权限) ( T_ProcessEmployee )
- **业务含义**：工艺--雇员权限(工程设计流程权限)
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| version | string | 是 | - | - |
| employeeId | string | 是 | - | 雇员信息 |
| processId | string | 是 | - | 工艺 |
| ifupload | string | 是 | - | 上传 |
| ifdownload | string | 是 | - | 下载 |
| ifview | string | 是 | - | 查看 |
- **关联关系**：无

---

#### 51 工艺流程参数表 ( T_ProcessParameter )
- **业务含义**：工艺流程参数表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
| parametersId | int? | 是 | - | 参数，对应S_Parameters.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
- **关联关系**：
  - T_ProcessParameter.parametersId = S_Parameters.recId
  - T_ProcessParameter.processId = T_Process.recId

---

#### 52 工艺管理--工厂 ( T_ProcessPlant )
- **业务含义**：工艺管理--工厂
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| version | int? | 是 | - | 记录版本 |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
- **关联关系**：
  - T_ProcessPlant.plantsId = T_Plants.recId
  - T_ProcessPlant.processId = T_Process.recId

---

#### 53 销售数据--产品分类--工厂 ( T_ProductCategoryPlant )
- **业务含义**：销售数据--产品分类--工厂
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| version | int? | 是 | - | - |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| productCategoryId | int? | 是 | - | 销售数据--产品分类，对应S_ProductCategory.recId |
- **关联关系**：
  - T_ProductCategoryPlant.plantsId = T_Plants.recId
  - T_ProductCategoryPlant.productCategoryId = S_ProductCategory.recId

---

#### 54 货架表 ( T_Racks )
- **业务含义**：货架表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| locationId | int? | 是 | - | 储区表，对应T_Location.recId |
- **关联关系**：
  - T_Racks.locationId = T_Location.recId

---

#### 55 表单设定 ( T_ReportSeting )
- **业务含义**：表单设定
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| deliveryAddress | string | 是 | - | - |
| fgiPackingListUrl | string | 是 | - | 成品装箱地址 |
| fgiSOInvoiceUrl | string | 是 | - | 成品发票地址 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| matPackingListUrl | string | 是 | - | 原材料发票地址 |
| matSOInvoiceUrl | string | 是 | - | - |
| miInnerLayerUrl | string | 是 | - | - |
| miOuterLayerUrl | string | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| woUrl | string | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| fgiPackingListId | int? | 是 | - | 对应T_FunctionRight.recId |
| fgiSOInvoiceId | int? | 是 | - | 对应T_FunctionRight.recId |
| matPackingListId | int? | 是 | - | 对应T_FunctionRight.recId |
| matSOInvoiceId | int? | 是 | - | 对应T_FunctionRight.recId |
| supplierId | int? | 是 | - | 对应M_Suppliers.recId |
| productionQueryUrl | string | 是 | - | - |
- **关联关系**：
  - T_ReportSeting.companyId = T_Company.recId
  - T_ReportSeting.customerId = S_Customer.recId
  - T_ReportSeting.fgiPackingListId = T_FunctionRight.recId
  - T_ReportSeting.fgiSOInvoiceId = T_FunctionRight.recId
  - T_ReportSeting.matPackingListId = T_FunctionRight.recId
  - T_ReportSeting.matSOInvoiceId = T_FunctionRight.recId
  - T_ReportSeting.supplierId = M_Suppliers.recId

---

#### 56 运输方式 ( T_Shipping )
- **业务含义**：运输方式
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| scac | string | 是 | - | - |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 57 工序--雇员权限(过数权限) ( T_StepEmployee )
- **业务含义**：工序--雇员权限(过数权限)
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| version | int? | 是 | - | - |
| employeeId | int? | 是 | - | 雇员信息，对应S_BusinessMan.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| ifupload | string | 是 | - | 上传 |
| ifdownload | string | 是 | - | 下载 |
| ifview | string | 是 | - | 查看 |
- **关联关系**：
  - T_StepEmployee.employeeId = S_BusinessMan.recId
  - T_StepEmployee.stepsId = T_Steps.recId

---

#### 58 工序--间接材料 ( T_StepIndiectMatLink )
- **业务含义**：工序--间接材料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| altQuantity | double? | 是 | - | 替换数量 |
| ifAutoCal | bool? | 是 | - | - |
| note | string | 是 | - | 备注 |
| quantity | double? | 是 | - | 原数量 |
| version | int? | 是 | - | - |
| altMaterialsId | int? | 是 | - | 替换物料，对应M_Materials.recId |
| altUnitId | int? | 是 | - | 替换单位，对应T_Unit.recId |
| materialsId | int? | 是 | - | 原物料，对应M_Materials.recId |
| stepsId | int? | 是 | - | 工艺表，对应T_Steps.recId |
| unitId | int? | 是 | - | 原单位，对应T_Unit.recId |
- **关联关系**：
  - T_StepIndiectMatLink.altMaterialsId = M_Materials.recId
  - T_StepIndiectMatLink.altUnitId = T_Unit.recId
  - T_StepIndiectMatLink.materialsId = M_Materials.recId
  - T_StepIndiectMatLink.stepsId = T_Steps.recId
  - T_StepIndiectMatLink.unitId = T_Unit.recId

---

#### 59 工序表 ( T_Steps )
- **业务含义**：工序表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| partOutPut | bool? | 是 | - | 是否用于部分过账 |
| sort | string | 是 | - | - |
| stdLeadTime | int? | 是 | - | 设定时间 |
| stdTPArea | int? | 是 | - | - |
| stdTPJobQty | int? | 是 | - | - |
| stdTPPanles | int? | 是 | - | - |
| stdtransferTime | int? | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| unitId | int? | 是 | - | 单位（过数单位），对应T_Unit.recId |
| ifOutWork | bool? | 是 | ((0)) | - |
| ifOS | bool? | 是 | ((0)) | 是否用于外协过数 |
| ifLast | bool? | 是 | ((0)) | 是否用于最后工序 |
| wipDispUnitId | int? | 是 | - | 横向WIP结存单位 |
| tooling | string | 是 | - | - |
| ifSeqOutput | string | 是 | - | 是否按顺序过数 |
| costCenter | string | 是 | - | - |
| physicalCount | string | 是 | - | - |
| maxHoldTime | string | 是 | - | - |
| stepOutputWay | string | 是 | - | Must提示并不允许过数，Warn提示并允许过数 |
| sampleHoldTime | string | 是 | - | - |
| dgOutputNext | string | 是 | - | - |
| bcodeOutput | string | 是 | - | - |
| unIndirectMat | string | 是 | - | - |
| checkConsume | string | 是 | - | - |
| ifEqument | string | 是 | - | - |
| ifSplit | string | 是 | - | - |
| costStepId | string | 是 | - | - |
| balancePicking | string | 是 | - | - |
| ifScheduling | string | 是 | - | - |
| eqNums | string | 是 | - | - |
| mixedProcessing | string | 是 | - | - |
| modifyUserId | string | 是 | - | - |
| modifyTime | string | 是 | - | - |
| lineWareId | string | 是 | - | - |
- **关联关系**：
  - T_Steps.companyId = T_Company.recId
  - T_Steps.departmentId = T_Department.recId
  - T_Steps.plantsId = T_Plants.recId
  - T_Steps.unitId = T_Unit.recId

---

#### 60 工序关联工艺 ( T_StepsProcess )
- **业务含义**：工序关联工艺
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifBarcodEntry | bool? | 是 | - | 是否是过数工作站 |
| nissanCan | int? | 是 | - | 日产能 |
| postOPTime | int? | 是 | - | 后置时间 |
| processTime | int? | 是 | - | 加工时间 |
| queueTime | int? | 是 | - | 排队时间 |
| scrapeRate | decimal? | 是 | - | 报废 |
| setupTime | int? | 是 | - | 设置时间 |
| transferTime | int? | 是 | - | 转序时间 |
| version | int? | 是 | - | - |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| ifDefault | bool? | 是 | ((1)) | 是否默认工序 |
| ifCost | string | 是 | - | 成本 |
| unStopProcess | string | 是 | - | - |
| mulSuppOSTip | string | 是 | - | - |
| modifyUserId | string | 是 | - | - |
| modifyTime | string | 是 | - | - |
| arrival | bool? | 是 | - | 进站 |
| onDuty | bool? | 是 | - | 上机 |
| offDuty | bool? | 是 | - | 下机 |
| departure | bool? | 是 | - | 出站 |
- **关联关系**：
  - T_StepsProcess.postRoleId = T_PostRole.recId
  - T_StepsProcess.processId = T_Process.recId
  - T_StepsProcess.stepsId = T_Steps.recId

---

#### 61 工艺定量、定性检验项表 ( T_StepsProcessInspectItem )
- **业务含义**：工艺定量、定性检验项表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 记录ID |
| stepsProcessId | string | 是 | - | 工序工艺表ID |
| inspectItemId | string | 是 | - | 检验项目表ID |
| seq | string | 是 | - | 序号 |
| ifActive | string | 是 | - | 是否激活 |
| ifRequired | string | 是 | - | 必填项 |
| sourceType | string | 是 | - | 单据类型（1:IPQC, 2:FA, 3:MRB） |
| type | string | 是 | - | 检验项目类型（1:定量检验, 2:定性检验） |
| version | string | 是 | - | 版本号 |
| modifyUserId | string | 是 | - | 修改人 |
| modifyTime | string | 是 | - | 修改时间 |
- **关联关系**：无

---

#### 62 外协类型 ( T_SubcontractType )
- **业务含义**：外协类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| allMfg | bool? | 是 | - | 是否ALLMfg |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| innerLayer | bool? | 是 | - | 是否用于子层外协 |
| name | string | 是 | - | 名称 |
| version | int? | 是 | - | - |
| endProcessId | int? | 是 | - | 结束工艺，对应T_Process.recId |
| inspectGroupId | int? | 是 | - | 检验分组，对应T_InspectGroup.recId |
| startProcessId | int? | 是 | - | 开始工艺，对应T_Process.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - T_SubcontractType.endProcessId = T_Process.recId
  - T_SubcontractType.inspectGroupId = T_InspectGroup.recId
  - T_SubcontractType.startProcessId = T_Process.recId
  - T_SubcontractType.unitId = T_Unit.recId

---

#### 63 外协类型明细表 ( T_SubcontractTypeItem )
- **业务含义**：外协类型明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| leadTime | int? | 是 | - | 制造周期 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| subcontractTypeId | int? | 是 | - | 外协类型主表，对应T_SubcontractType.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - T_SubcontractTypeItem.currencyId = T_Currency.recId
  - T_SubcontractTypeItem.subcontractTypeId = T_SubcontractType.recId
  - T_SubcontractTypeItem.suppliersId = M_Suppliers.recId

---

#### 64 外协类型-参数表 ( T_SubcontractTypeParams )
- **业务含义**：外协类型-参数表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| subcontractTypeId | string | 是 | - | 外协类型id |
| parametersId | string | 是 | - | 参数id |
| dataType | string | 是 | - | 参数类型 |
| listVal | string | 是 | - | 下拉值 |
| seq | string | 是 | - | 序号 |
| defaultValue | string | 是 | - | 默认值 |
- **关联关系**：无

---

#### 65 系统配置表 ( T_SystemConfig )
- **业务含义**：系统配置表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| itemCode | string | 是 | - | 功能代码 |
| itemDesc | string | 是 | - | 功能说明 |
| itemValue | string | 是 | - | 功能值 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| modifiedBy | string | 是 | - | 更新人员 |
| moduleCode | string | 是 | - | 模组代码 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
- **关联关系**：
  - T_SystemConfig.companyId = T_Company.recId

---

#### 66 系统日志 ( T_SystemLog )
- **业务含义**：系统日志
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | - |
| operating | string | 是 | - | 操作方式：Delete 删除 Edit 编辑 AgainApproval 激活 |
| operatingTime | DateTime? | 是 | - | 操作时间 |
| tableName | string | 是 | - | 操作表名 |
| tableRecId | int? | 是 | - | - |
| userName | string | 是 | - | 操作人 |
| version | int? | 是 | - | - |
| userId | int? | 是 | - | 用户，对应T_User.recId |
- **关联关系**：
  - T_SystemLog.userId = T_User.recId

---

#### 67 税率表 ( T_Tax )
- **业务含义**：税率表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifVat | bool? | 是 | - | 是否用于增值税 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| content | string | 是 | - | 备注 |
| textId | string | 是 | - | 记事本，对应T_Text.recId |
- **关联关系**：
  - T_Tax.textId = T_Text.recId

---

#### 68 记事本 ( T_Text )
- **业务含义**：记事本
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 69 单位 ( T_Unit )
- **业务含义**：单位
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| enable | bool? | 是 | - | 是否激活 |
| ifCustomsUnit | bool? | 是 | - | 用于海关单位 |
| ifProduce | bool? | 是 | - | 用户生产单位 |
| ifPurchase | bool? | 是 | - | 用户采购单位 |
| ifQuality | bool? | 是 | - | 用于品质单位 |
| ifStock | bool? | 是 | - | 用于库存单位 |
| ifSystemUnit | bool? | 是 | - | 用于系统单位 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 70 T_UseProcess ( T_UseProcess )
- **业务含义**：ERP 系统 T_UseProcess 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 表主键 |
| type | string | 是 | - | 1:材料类别,2:材料项目,3产品分组 |
| formRecId | string | 是 | - | 材料类别ID，对应T_Category.recId |
| materialsId | string | 是 | - | 材料项目ID，对应M_Materials.recId |
| processRecId | string | 是 | - | 工艺ID，对应T_Process.recId |
| creatorId | string | 是 | - | 创建人ID，对应T_User.recId |
| createDate | string | 是 | - | 创建日期 |
| version | string | 是 | - | - |
| companyId | string | 是 | - | 公司ID，对应T_Company.recId |
| productGroupId | string | 是 | - | 产品分组ID，对应S_ProductGroup.recId |
| locationId | string | 是 | - | 储区ID，对应T_Location.recId |
- **关联关系**：
  - T_UseProcess.formRecId = T_Category.recId
  - T_UseProcess.materialsId = M_Materials.recId
  - T_UseProcess.processRecId = T_Process.recId
  - T_UseProcess.creatorId = T_User.recId
  - T_UseProcess.companyId = T_Company.recId
  - T_UseProcess.productGroupId = S_ProductGroup.recId
  - T_UseProcess.locationId = T_Location.recId

---

#### 71 用户表 ( T_User )
- **业务含义**：用户表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| emailPassword | string | 是 | - | 邮箱密码 |
| employeeEmail | string | 是 | - | 邮箱地址 |
| employeeEngName | string | 是 | - | 用户简称 |
| employeeMobile | string | 是 | - | 固话 |
| employeeName | string | 是 | - | 用户名称 |
| employeePhone | string | 是 | - | 联系电话 |
| ifActive | bool? | 是 | - | 是否激活 |
| imapPort | int? | 是 | - | IMAP端口 |
| imapServer | string | 是 | - | IMAP服务器地址 |
| language | string | 是 | - | 语言： zh_CN |
| lastModifyDate | DateTime? | 是 | - | - |
| loginName | string | 是 | - | 登录账号 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| password | string | 是 | - | 密码 |
| securityCode | string | 是 | - | - |
| smtpPort | int? | 是 | - | SMTP端口 |
| smtpServer | string | 是 | - | SMTP服务地址 |
| sort | string | 是 | - | - |
| userCode | string | 是 | - | 用户代码 |
| version | int? | 是 | - | - |
| businessManId | int? | 是 | - | 雇员表，对应S_BusinessMan.recId |
| setDepId | int? | 是 | - | 部门表，对应T_Department.recId |
- **关联关系**：
  - T_User.businessManId = S_BusinessMan.recId
  - T_User.setDepId = T_Department.recId

---

#### 72 用户功能表 ( T_UserFunctionRight )
- **业务含义**：用户功能表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| version | int? | 是 | - | - |
| functionRightId | int? | 是 | - | 系统模块功能表，对应T_FunctionRight.recId |
| groupId | int? | 是 | - | 用户组管理，对应T_Group.recId |
| userId | int? | 是 | - | 用户表，对应T_User.recId |
- **关联关系**：
  - T_UserFunctionRight.functionRightId = T_FunctionRight.recId
  - T_UserFunctionRight.groupId = T_Group.recId
  - T_UserFunctionRight.userId = T_User.recId

---

#### 73 用户模块 ( T_UserModule )
- **业务含义**：用户模块
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
| groupId | int? | 是 | - | 用户组管理，对应T_Group.recId |
| moduleId | int? | 是 | - | 模块表，对应T_Module.recId |
| userId | int? | 是 | - | 用户，对应T_User.recId |
- **关联关系**：
  - T_UserModule.groupId = T_Group.recId
  - T_UserModule.moduleId = T_Module.recId
  - T_UserModule.userId = T_User.recId

---

#### 74 用户所在工厂权限 ( T_UserPlant )
- **业务含义**：用户所在工厂权限
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| userId | int? | 是 | - | 用户ID，对应T_User.recId |
- **关联关系**：
  - T_UserPlant.plantsId = T_Plants.recId
  - T_UserPlant.userId = T_User.recId

---

#### 75 用户--岗位 ( T_UserPostRole )
- **业务含义**：用户--岗位
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| userId | int? | 是 | - | 用户，对应T_User.recId |
- **关联关系**：
  - T_UserPostRole.postRoleId = T_PostRole.recId
  - T_UserPostRole.userId = T_User.recId

---

#### 76 仓库 ( T_Warehouse )
- **业务含义**：仓库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| address | string | 是 | - | 地址 |
| code | string | 是 | - | 代码 |
| email | string | 是 | - | 邮箱 |
| endProduct | bool? | 是 | - | 是否用于成品 |
| fax | string | 是 | - | 传真 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| material | bool? | 是 | - | 是否用于物料 |
| mobilePhone | string | 是 | - | 固话 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| nickName | string | 是 | - | 简称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| telephone | string | 是 | - | 联系电话 |
| version | int? | 是 | - | - |
| wip | bool? | 是 | - | 是否用于WIP |
| zip | string | 是 | - | 邮编 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| productShipment | string | 是 | - | 1成品出货 |
| ifConsigment | string | 是 | - | 寄售 |
| mantissaWarehouse | string | 是 | - | 尾数仓 |
- **关联关系**：
  - T_Warehouse.companyId = T_Company.recId
  - T_Warehouse.plantsId = T_Plants.recId
  - T_Warehouse.postRoleId = T_PostRole.recId

---

#### 77 仓库人员明细 ( T_WarehouseKeepers )
- **业务含义**：仓库人员明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 78 T_Workshop ( T_Workshop )
- **业务含义**：ERP 系统 T_Workshop 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 唯一id |
| plantsId | string | 是 | - | 工厂id，对应T_Plants.recId |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| ifActive | string | 是 | - | 是否激活 |
| creatorId | string | 是 | - | 创建人 |
| creatorTime | string | 是 | - | 创建时间 |
| modifiedById | string | 是 | - | 修改人 |
| modifiedTime | string | 是 | - | 修改时间 |
- **关联关系**：
  - T_Workshop.plantsId = T_Plants.recId

---

### 2.2 物料模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 79 BOM发料 ( M_BOMIssue )
- **业务含义**：BOM发料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 发料单号 |
| issueDate | DateTime? | 是 | - | 发料日期 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| bomPicklistId | int? | 是 | - | BOM领料明细，对应M_BOMPicklist.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_BOMIssue.bomPicklistId = M_BOMPicklist.recId
  - M_BOMIssue.creatorId = T_User.recId
  - M_BOMIssue.departmentId = T_Department.recId
  - M_BOMIssue.warehouseId = T_Warehouse.recId

---

#### 80 BOM发料明细表 ( M_BOMIssueItem )
- **业务含义**：BOM发料明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| inventoryBatchId | int? | 是 | - | M_InventoryBatch，对应物料批次库存.recId |
| inventoryId | int? | 是 | - | M_Inventory |
| note | string | 是 | - | - |
| qtyIssued | decimal? | 是 | - | 已发数量 |
| qtyOut | decimal? | 是 | - | 超发数量 |
| quantity | decimal? | 是 | - | 领料数量 |
| saleType | string | 是 | - | 销售类型：Bonded 保税 ForDomestic 内销  ForExport 外销 |
| version | int? | 是 | - | - |
| bomIssueId | int? | 是 | - | 主表，对应M_BOMIssue.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| stockUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| mfgPartId | string | 是 | - | 制造部件，对应E_JobMfgParts.recId |
- **关联关系**：
  - M_BOMIssueItem.inventoryBatchId = 物料批次库存.recId
  - M_BOMIssueItem.bomIssueId = M_BOMIssue.recId
  - M_BOMIssueItem.materialsId = M_Materials.recId
  - M_BOMIssueItem.stockUnitId = T_Unit.recId
  - M_BOMIssueItem.mfgPartId = E_JobMfgParts.recId

---

#### 81 BOM领料单 ( M_BOMPicklist )
- **业务含义**：BOM领料单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | Pending:制作中   Approved：审批通过 |
| approveVersion | int? | 是 | - | - |
| code | string | 是 | - | 领料单号 |
| enableApproval | bool? | 是 | - | - |
| note | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | 请领日期 |
| requestedDate | DateTime? | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门表，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| bomIssueCode | string | 是 | - | 发料单号 |
| bomIssueId | int? | 是 | - | BOM发料，对应M_BOMIssue.recId |
| EnterDate | DateTime? | 是 | (getdate()) | 领料日期 |
| rpMat | string | 是 | - | 是否补料 |
- **关联关系**：
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

#### 82 BOM领料单审批记录 ( M_BOMPicklistHistory )
- **业务含义**：BOM领料单审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | 开始审批时间 |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | 结束审批日期 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| bomPicklistId | int? | 是 | - | 对应M_BOMPicklist.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - M_BOMPicklistHistory.bomPicklistId = M_BOMPicklist.recId
  - M_BOMPicklistHistory.myId = T_User.recId

---

#### 83 BOM领料单明细 ( M_BOMPicklistItem )
- **业务含义**：BOM领料单明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | Pending:制作中   Approved：审批通过 |
| bomBatchingId | int? | 是 | - | BOM配料单表，对应P_BOMBatching.recId |
| ideas | string | 是 | - | - |
| locked | bool? | 是 | - | - |
| note | string | 是 | - | - |
| orderArea | decimal? | 是 | - | 订单面积 |
| qtyIssued | decimal? | 是 | - | 已发数量PCS |
| qtyOut | decimal? | 是 | - | - |
| quantity | decimal? | 是 | - | 领料数量 |
| requestedDate | DateTime? | 是 | - | 需求日期 |
| version | int? | 是 | - | - |
| voteArea | decimal? | 是 | - | 投料面积 |
| bomPicklistId | int? | 是 | - | 主表，对应M_BOMPicklist.recId |
| mfgPartId | int? | 是 | - | 制造部件号，对应E_JobMfgParts.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| moId | int? | 是 | - | 制造单号，对应P_MO.recId |
| stockUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| bomIssueItemId | int? | 是 | - | 发料明细单，对应M_BOMIssueItem.recId |
| qtyHairBack | decimal? | 是 | - | - |
| onhold | bool? | 是 | ((0)) | 关闭   1：关闭  0：激活 |
| remaining | string | 是 | - | 回收碎料   1：回收   ，0：不回收 |
| qtyRemaining | string | 是 | - | 碎料数量 |
- **关联关系**：
  - M_BOMPicklistItem.bomBatchingId = P_BOMBatching.recId
  - M_BOMPicklistItem.bomPicklistId = M_BOMPicklist.recId
  - M_BOMPicklistItem.mfgPartId = E_JobMfgParts.recId
  - M_BOMPicklistItem.materialsId = M_Materials.recId
  - M_BOMPicklistItem.moId = P_MO.recId
  - M_BOMPicklistItem.stockUnitId = T_Unit.recId
  - M_BOMPicklistItem.bomIssueItemId = M_BOMIssueItem.recId

---

#### 84 BOM领料批次 ( M_BOMPicklistItemBatch )
- **业务含义**：BOM领料批次
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| averageUnitCost | decimal? | 是 | - | - |
| bomIssueItemId | int? | 是 | - | BOM发料明细表，对应M_BOMIssueItem.recId |
| ma_Cost | decimal? | 是 | - | - |
| note | string | 是 | - | 备注 |
| poItemId | int? | 是 | - | - |
| quantity | decimal? | 是 | - | 发料数量PCS |
| version | int? | 是 | - | - |
| bomPicklistItemId | int? | 是 | - | BOM领料明细单，对应M_BOMPicklistItem.recId |
| inventoryBatchId | int? | 是 | - | 库存批次，对应M_InventoryBatch.recId |
| EnterDate | DateTime? | 是 | (getdate()) | 实际发放日期 |
| qtyRemaining | string | 是 | - | 碎料数量 |
| inventorybatchRemainingAssignId | string | 是 | - | - |
- **关联关系**：
  - M_BOMPicklistItemBatch.bomIssueItemId = M_BOMIssueItem.recId
  - M_BOMPicklistItemBatch.bomPicklistItemId = M_BOMPicklistItem.recId
  - M_BOMPicklistItemBatch.inventoryBatchId = M_InventoryBatch.recId

---

#### 85 BOM领料外发 ( M_BOMPicklistWF )
- **业务含义**：BOM领料外发
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| bomPicklistId | int? | 是 | - | BOM领料单，对应M_BOMPicklist.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - M_BOMPicklistWF.bomPicklistId = M_BOMPicklist.recId
  - M_BOMPicklistWF.myId = T_User.recId

---

#### 86 寄送表 ( M_Consignment )
- **业务含义**：寄送表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| receiptId | int? | 是 | - | - |
| transactionDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| warehousingId | int? | 是 | - | 仓库，对应T_Warehousing.recId |
| purchaseOrderId | int? | 是 | - | 采购，对应M_PurchaseOrder.recId |
- **关联关系**：
  - M_Consignment.warehousingId = T_Warehousing.recId
  - M_Consignment.purchaseOrderId = M_PurchaseOrder.recId

---

#### 87 物料数据--包线管理 ( M_Envelope )
- **业务含义**：物料数据--包线管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | NA直接通过 |
| approveVersion | int? | 是 | - | - |
| createDate | DateTime? | 是 | - | 建单时间 |
| enableApproval | bool? | 是 | - | - |
| envelopeNumber | string | 是 | - | - |
| notes | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| status | string | 是 | - | 单据状态： 生效 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| stepsIds | int? | 是 | - | 工序，对应T_Steps.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| taxId | int? | 是 | - | 税率，对应T_Tax.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
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

#### 88 M_EnvelopeHistory ( M_EnvelopeHistory )
- **业务含义**：ERP 系统 M_EnvelopeHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 89 物料数据--包线管理明细 ( M_EnvelopeItem )
- **业务含义**：物料数据--包线管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| activateDate | DateTime? | 是 | - | 生效时间 |
| discount | decimal? | 是 | - | 折扣率 |
| note | string | 是 | - | 备注 |
| priceInTax | decimal? | 是 | - | 含税单价 |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| qtyOfTo | decimal? | 是 | - | - |
| qtyofFrom | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| envelopeId | int? | 是 | - | 主表，对应M_Envelope.recId |
- **关联关系**：
  - M_EnvelopeItem.envelopeId = M_Envelope.recId

---

#### 90 M_EnvelopeWF ( M_EnvelopeWF )
- **业务含义**：ERP 系统 M_EnvelopeWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 91 物料库存 ( M_Inventory )
- **业务含义**：物料库存
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| avgCost | decimal? | 是 | - | 平均成本 |
| qtyAllocated | decimal? | 是 | - | 指派数量 |
| qtyConsignment | decimal? | 是 | - | 寄售数量 |
| qtyOnHand | decimal? | 是 | - | 库存数量 |
| version | int? | 是 | - | 记录版本 |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_Inventory.locationId = T_Location.recId
  - M_Inventory.materialsId = M_Materials.recId
  - M_Inventory.stockUnitId = T_Unit.recId
  - M_Inventory.warehouseId = T_Warehouse.recId

---

#### 92 物料批次库存 ( M_InventoryBatch )
- **业务含义**：物料批次库存
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| actualCost | decimal? | 是 | - | 库存单价；本币不含税单价 |
| suppBatchNo | string | 是 | - | 供应商批号 |
| consignmentFlg | bool? | 是 | - | 是否寄售；0.否   1是 |
| deliveryCode | string | 是 | - | - |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| fifoCost | decimal? | 是 | - | - |
| internalBatchNo | string | 是 | - | 内部批号；物料批次 |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| note | string | 是 | - | 备注 |
| poItemId | int? | 是 | - | 采购明细单，对应M_PurchaseOrderItem.FGI_Inventory |
| purchasePrice | decimal? | 是 | - | 成本价格；原币不含税单价 |
| qtyAllocated | decimal? | 是 | - | 已分配已指派数量；在途数量 |
| qtyCustoms | decimal? | 是 | - | 海关关税 |
| qtyInspection | decimal? | 是 | - | 检查数量PCS；PCS |
| qtyOnHand | decimal? | 是 | - | 库存数量 |
| receiptItemId | int? | 是 | - | 接收表，对应M_ReceiptItem.recId |
| stockDate | DateTime? | 是 | - | 入库日期 |
| taxFree | bool? | 是 | - | 是否外购库存；0.否  1.是 |
| version | int? | 是 | - | 记录版本 |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| rack | string | 是 | - | 货位 |
| weightOfUnit | decimal? | 是 | - | 单重 |
| prnote | string | 是 | - | 请购备注 |
| remaining | bool? | 是 | - | 碎料；0.否  1.是 |
| orgbatchId | int? | 是 | - | 原批次 |
| fiscalPeriodId | int? | 是 | - | 财务期间 |
| currencyId | int? | 是 | - | 币种 |
| qtyLocked | decimal? | 是 | - | 锁定数量 |
| customerId | int? | 是 | - | 客户 |
| ttype | string | 是 | - | - |
| qtyTransit | decimal? | 是 | - | 调拨数量 |
| osSuppliersId | int? | 是 | - | 外协供应商 |
| frozen | bool? | 是 | - | - |
| saleType | string | 是 | - | 贸易类型 |
| taxesFlag | string | 是 | - | 保税类型 |
- **关联关系**：
  - M_InventoryBatch.poItemId = M_PurchaseOrderItem.recId
  - M_InventoryBatch.receiptItemId = M_ReceiptItem.recId
  - M_InventoryBatch.locationId = T_Location.recId
  - M_InventoryBatch.materialsId = M_Materials.recId
  - M_InventoryBatch.stockUnitId = T_Unit.recId
  - M_InventoryBatch.suppliersId = M_Suppliers.recId
  - M_InventoryBatch.warehouseId = T_Warehouse.recId

---

#### 93 M_InventoryBatch_bak0413 ( M_InventoryBatch_bak0413 )
- **业务含义**：ERP 系统 M_InventoryBatch_bak0413 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 94 碎料管理 ( M_InventorybatchRemaining )
- **业务含义**：碎料管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| bomPicklistItemBatchId | int? | 是 | - | 物料领用批次 |
| createDate | DateTime? | 是 | - | 创建日期 |
| inventoryId | int? | 是 | - | 物料库存 |
| invtRate | decimal? | 是 | - | 库存比 |
| length | decimal? | 是 | - | 长 |
| note | string | 是 | - | 备注 |
| orgLength | decimal? | 是 | - | 原长 |
| orgWidth | decimal? | 是 | - | 原宽 |
| qty | int? | 是 | - | 数量 |
| qtyAssigned | int? | 是 | - | 订单出数 |
| qtyAvailable | int? | 是 | - | 可用数量 |
| qtyStock | decimal? | 是 | - | 库存数量 |
| status | string | 是 | - | 状态 |
| version | int? | 是 | - | 记录版本 |
| width | decimal? | 是 | - | 宽 |
| inventoryBatchId | int? | 是 | - | 物料批次 |
| locationId | int? | 是 | - | 储区 |
| materialsId | int? | 是 | - | 物料 |
| orgInventoryBatchId | int? | 是 | - | 原物料批次 |
| plantsId | int? | 是 | - | 工厂 |
| userId | int? | 是 | - | 用户 |
| actualCost | decimal? | 是 | - | 实际成本 |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| suppliersId | int? | 是 | - | 供应商 |
| suppBatchNo | string | 是 | - | 供应商批次 |
| materialsIssueNoteItemBatchId | int? | 是 | - | 物料发放批次 |
| rack | string | 是 | - | 货位 |
| departmentId | int? | 是 | - | 部门 |
- **关联关系**：无

---

#### 95 库存检验 ( M_InventoryCheck )
- **业务含义**：库存检验
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checkDate | DateTime? | 是 | - | 检验日期 |
| code | string | 是 | - | 代码 |
| ifCheck0 | bool? | 是 | - | - |
| locked | bool? | 是 | - | - |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | Close：关闭 Open：打开 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_InventoryCheck.creatorId = T_User.recId
  - M_InventoryCheck.fiscalPeriodId = T_FiscalPeriod.recId
  - M_InventoryCheck.postRoleId = T_PostRole.recId
  - M_InventoryCheck.warehouseId = T_Warehouse.recId

---

#### 96 库存检验明细 ( M_InventoryCheckItem )
- **业务含义**：库存检验明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checkQuantity | decimal? | 是 | - | 检查数量 |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| internalBatchNo | string | 是 | - | 内部批号 |
| inventoryBatchId | int? | 是 | - | 物料批次库存，对应M_InventoryBatch.recId |
| inventoryId | int? | 是 | - | 物料库存，对应M_Inventory.recId |
| sysQuantity | decimal? | 是 | - | 系统检验数量 |
| version | int? | 是 | - | - |
| inventoryCheckId | int? | 是 | - | 主表，对应M_InventoryCheck.recId |
| inventoryCheckReasonId | int? | 是 | - | 对应T_InventoryCheckReason.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| stockUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - M_InventoryCheckItem.inventoryBatchId = M_InventoryBatch.recId
  - M_InventoryCheckItem.inventoryId = M_Inventory.recId
  - M_InventoryCheckItem.inventoryCheckId = M_InventoryCheck.recId
  - M_InventoryCheckItem.inventoryCheckReasonId = T_InventoryCheckReason.recId
  - M_InventoryCheckItem.locationId = T_Location.recId
  - M_InventoryCheckItem.materialsId = M_Materials.recId
  - M_InventoryCheckItem.stockUnitId = T_Unit.recId

---

#### 97 杂项领料中的物料 ( M_InventoryMiscBatch )
- **业务含义**：杂项领料中的物料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| actualCost | string | 是 | - | 成本 |
| suppBatchNo | string | 是 | - | - |
| customsUnitVal | string | 是 | - | - |
| expiryDate | string | 是 | - | - |
| fifoCost | string | 是 | - | - |
| internalBatchNo | string | 是 | - | 批次号 |
| purchasePrice | string | 是 | - | - |
| qtyAllocated | string | 是 | - | - |
| qtyOnHand | string | 是 | - | 库存数 |
| stockDate | string | 是 | - | 入库时间 |
| version | string | 是 | - | - |
| locationId | string | 是 | - | - |
| poItemId | string | 是 | - | 采购明细，对应M_PurchaseOrderItem.FGI_Inventory |
| stockUnitId | string | 是 | - | 单位，对应T_Unit.recId |
| suppliersId | string | 是 | - | 供应商，对应M_Suppliers.recId |
| warehouseId | string | 是 | - | 仓库，对应T_Warehouse.recId |
| miscPartId | string | 是 | - | - |
- **关联关系**：
  - M_InventoryMiscBatch.poItemId = M_PurchaseOrderItem.recId
  - M_InventoryMiscBatch.stockUnitId = T_Unit.recId
  - M_InventoryMiscBatch.suppliersId = M_Suppliers.recId
  - M_InventoryMiscBatch.warehouseId = T_Warehouse.recId

---

#### 98 模组 ( M_InventoryOut )
- **业务含义**：模组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| averageUnitCost | decimal? | 是 | - | 平均成本 |
| inventoryId | int? | 是 | - | 物料库存，对应M_Inventory.recId |
| ma_Cost | decimal? | 是 | - | 物料成本 |
| materialPackingSlipItemId | int? | 是 | - | 原材料装运指派明细 |
| note | string | 是 | - | 备注 |
| quantity | decimal? | 是 | - | 装运数量PCS |
| version | int? | 是 | - | 记录版本 |
| inventoryBatchId | int? | 是 | - | 物料库存批次，对应M_InventoryBatch.recId |
| locked | bool? | 是 | - | - |
| shipDate | DateTime? | 是 | - | 装运日期 |
| qtyReturned | decimal? | 是 | - | 退回数量 |
- **关联关系**：
  - M_InventoryOut.inventoryId = M_Inventory.recId
  - M_InventoryOut.inventoryBatchId = M_InventoryBatch.recId

---

#### 99 物料IQC报废 ( M_IQC )
- **业务含义**：物料IQC报废
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | NA 审批通过 |
| approveVersion | int? | 是 | - | - |
| batchCode | string | 是 | - | 供应商批号 |
| checkDate | DateTime? | 是 | - | 检验日期 |
| code | string | 是 | - | 检验单号 |
| deliveryCode | string | 是 | - | 送货单号 |
| enableApproval | bool? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| locked | bool? | 是 | - | 是否审批通过 0否  1是 |
| modifiedBy | string | 是 | - | 最后修改人 |
| note | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| qtyDefected | decimal? | 是 | - | 特采数量 |
| qtyInspected | decimal? | 是 | - | 检验总数（接收数量） |
| qtyQualified | decimal? | 是 | - | 合格数量 |
| qtyReturn | decimal? | 是 | - | 退货数量 |
| qtyReturned | decimal? | 是 | - | - |
| qtySample | decimal? | 是 | - | 抽样检测 |
| qtyScrapped | decimal? | 是 | - | 报废数量 |
| qtyStocked | decimal? | 是 | - | 入库数量 |
| qtyToStock | decimal? | 是 | - | 可以再入库数 |
| receiveDate | DateTime? | 是 | - | 收货日期 |
| sourceId | int? | 是 | - | 仓库接收检验   从接收检验 |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | 单据状态：Valid 有效的 |
| testDate | DateTime? | 是 | - | 测试日期 |
| type | string | 是 | - | Receipt 接收检验  Stock仓库检验 |
| version | int? | 是 | - | - |
| buyUnitId | int? | 是 | - | 送检单位，对应T_Unit.recId |
| checkorId | int? | 是 | - | 检验员，对应T_User.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人（检验员），对应T_User.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
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

#### 100 M_IQCHistory ( M_IQCHistory )
- **业务含义**：ERP 系统 M_IQCHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| iqcTestId | int? | 是 | - | 对应M_IQC.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - M_IQCHistory.iqcTestId = M_IQC.recId
  - M_IQCHistory.myId = T_User.recId

---

#### 101 物料IQC报废明细表 ( M_IQCItem )
- **业务含义**：物料IQC报废明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| inspectResult | string | 是 | - | 检验结果 |
| judgementResult | string | 是 | - | 判断结果 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| inspectItemsId | int? | 是 | - | 报废明细表，对应T_InspectItems.recId |
| iqcTestId | int? | 是 | - | 对应M_IQC.recId |
- **关联关系**：
  - M_IQCItem.inspectItemsId = T_InspectItems.recId
  - M_IQCItem.iqcTestId = M_IQC.recId

---

#### 102 物料送检单管理 ( M_IQCRecheck )
- **业务含义**：物料送检单管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 送检单号 |
| inventoryId | int? | 是 | - | 物料库存，对应M_Inventory.recId |
| ma_Cost | decimal? | 是 | - | 成本（不含税） |
| note | string | 是 | - | 备注 |
| qtyInspection | decimal? | 是 | - | 送检数量 |
| qtyReStock | decimal? | 是 | - | 入仓数量 |
| qtyReturn | decimal? | 是 | - | 退货数量 |
| qtyScrapped | decimal? | 是 | - | 报废数量 |
| status | string | 是 | - | 单据状态：Active 活动  IQC 已检视 Submit 提交 |
| submissionDate | DateTime? | 是 | - | 送检日期 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| inspectPostId | int? | 是 | - | 检验岗位，对应T_PostRole.recId |
| inventoryBatchId | int? | 是 | - | 物料批次库存，对应M_InventoryBatch.recId |
| postRoleId | int? | 是 | - | 建单岗位，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| ReStockDate | DateTime? | 是 | - | 返仓日期 |
- **关联关系**：
  - M_IQCRecheck.inventoryId = M_Inventory.recId
  - M_IQCRecheck.creatorId = T_User.recId
  - M_IQCRecheck.inspectPostId = T_PostRole.recId
  - M_IQCRecheck.inventoryBatchId = M_InventoryBatch.recId
  - M_IQCRecheck.postRoleId = T_PostRole.recId
  - M_IQCRecheck.warehouseId = T_Warehouse.recId

---

#### 103 物料检验 报废原因 ( M_IQCResult )
- **业务含义**：物料检验 报废原因
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| quantity | decimal? | 是 | - | 报废数 |
| result | string | 是 | - | - |
| version | int? | 是 | - | - |
| defectId | int? | 是 | - | 缺陷表，对应T_Defect.recId |
| iqcTestId | int? | 是 | - | 物料IQC报废，对应M_IQC.recId |
- **关联关系**：
  - M_IQCResult.defectId = T_Defect.recId
  - M_IQCResult.iqcTestId = M_IQC.recId

---

#### 104 M_IQCWF ( M_IQCWF )
- **业务含义**：ERP 系统 M_IQCWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| iqcTestId | int? | 是 | - | 对应M_IQC.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - M_IQCWF.iqcTestId = M_IQC.recId
  - M_IQCWF.myId = T_User.recId

---

#### 105 领料和退料表 ( M_MaterialIssueRequest )
- **业务含义**：领料和退料表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | 审批状态 |
| approveVersion | int? | 是 | - | 审批版本 |
| code | string | 是 | - | 代码 |
| enableApproval | bool? | 是 | - | 是否启用审批 |
| note | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | 原始状态 |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| requestedDate | DateTime? | 是 | - | 日期 |
| sourceType | string | 是 | - | 单据类型；DepartmentPicking 部门领料
ProductionPicking 生产领料 |
| startTaskName | string | 是 | - | 开始任务 |
| status | string | 是 | - | 状态 |
| type | string | 是 | - | 类型；Spicking 标准领料
Mpicking 杂项领料
Sunloading 标准退料
Bunlo塔顶雪天樰 ading BOM领料 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 审批类型，对应T_FlowType.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 角色，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| moduleTypeId | int? | 是 | - | 模组类型 |
| overtake | bool? | 是 | - | - |
| ifPrint | bool? | 是 | - | 是否打印 |
| printUserId | int? | 是 | - | 打印用户 |
| printTime | DateTime? | 是 | - | 打印时间 |
| lineWareId | int? | 是 | - | 线边仓 |
| toolApplyId | int? | 是 | - | 工具申请单 |
| mobomBatchingId | int? | 是 | - | - |
| rdProjectId | int? | 是 | - | 项目，对应M_RDProject.recId |
- **关联关系**：
  - M_MaterialIssueRequest.companyId = T_Company.recId
  - M_MaterialIssueRequest.creatorId = T_User.recId
  - M_MaterialIssueRequest.departmentId = T_Department.recId
  - M_MaterialIssueRequest.flowTypeId = T_FlowType.recId
  - M_MaterialIssueRequest.plantsId = T_Plants.recId
  - M_MaterialIssueRequest.postRoleId = T_PostRole.recId
  - M_MaterialIssueRequest.warehouseId = T_Warehouse.recId
  - M_MaterialIssueRequest.rdProjectId = M_RDProject.recId

---

#### 106 领料和退料审批历史 ( M_MaterialIssueRequestHistory )
- **业务含义**：领料和退料审批历史
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 审批版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 流程说明 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 建议 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务表单 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| materialIssueRequestId | int? | 是 | - | 领料和退料，对应M_MaterialIssueRequest.recId |
- **关联关系**：
  - M_MaterialIssueRequestHistory.myId = T_User.recId
  - M_MaterialIssueRequestHistory.materialIssueRequestId = M_MaterialIssueRequest.recId

---

#### 107 领料和退料明细表 ( M_MaterialIssueRequestItem )
- **业务含义**：领料和退料明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveStatus | string | 是 | - | 审批状态 |
| ideas | string | 是 | - | - |
| internalMiscBatch | string | 是 | - | - |
| inventoryMiscBatchId | int? | 是 | - | 对应inventoryMiscBatch.recId |
| misMaterialsDesc | string | 是 | - | - |
| misMaterialsSpec | string | 是 | - | - |
| note | string | 是 | - | 备注 |
| materialsIssueNoteCode | string | 是 | - | 发料单号 |
| materialsIssueNoteItemId | int? | 是 | - | 发料明细，对应M_MaterialsIssueNoteItem.recId |
| qtyHairBack | decimal? | 是 | - | 可领/可退数量 |
| qtyIssued | decimal? | 是 | - | 已发/已退数量 |
| quantity | decimal? | 是 | - | 请领/请退数量 |
| requestedDate | DateTime? | 是 | - | 领料/退料时间 |
| version | int? | 是 | - | 记录版本 |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| materialIssueRequestId | int? | 是 | - | 领料和退料，对应M_MaterialIssueRequest.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| bomPicklistItemId | int? | 是 | - | BOM领料明细，对应M_BOMPicklistItem.recId |
| qtyRemaining | decimal? | 是 | - | - |
| qtyPcsRemaining | int? | 是 | - | - |
| qtyReturnRemaining | decimal? | 是 | - | - |
| checkConsume | bool? | 是 | - | - |
| stdConsume | decimal? | 是 | - | - |
| actualConsume | decimal? | 是 | - | - |
| lineWarePick | bool? | 是 | - | - |
- **关联关系**：
  - M_MaterialIssueRequestItem.inventoryMiscBatchId = inventoryMiscBatch.recId
  - M_MaterialIssueRequestItem.materialsIssueNoteItemId = M_MaterialsIssueNoteItem.recId
  - M_MaterialIssueRequestItem.materialsId = M_Materials.recId
  - M_MaterialIssueRequestItem.materialIssueRequestId = M_MaterialIssueRequest.recId
  - M_MaterialIssueRequestItem.stepsId = T_Steps.recId
  - M_MaterialIssueRequestItem.stockUnitId = T_Unit.recId
  - M_MaterialIssueRequestItem.processId = T_Process.recId
  - M_MaterialIssueRequestItem.bomPicklistItemId = M_BOMPicklistItem.recId

---

#### 108 领料和退料审批流程 ( M_MaterialIssueRequestWF )
- **业务含义**：领料和退料审批流程
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 审批版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 流程说明 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 建议 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务表单 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| materialIssueRequestId | int? | 是 | - | 领料和退料，对应M_MaterialIssueRequest.recId |
- **关联关系**：
  - M_MaterialIssueRequestWF.myId = T_User.recId
  - M_MaterialIssueRequestWF.materialIssueRequestId = M_MaterialIssueRequest.recId

---

#### 109 材料装运明细表 ( M_MaterialPackingSlipItem )
- **业务含义**：材料装运明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| amount_Invoiced | decimal? | 是 | - | 开票金额 |
| amount_Invoiced2 | decimal? | 是 | - | - |
| amount_Receivables | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | 对账金额 |
| amount_Reconciled2 | decimal? | 是 | - | - |
| enterDate | DateTime? | 是 | - | 创建日期 |
| note | string | 是 | - | 备注 |
| qty_Invoiced | decimal? | 是 | - | 开票数量 |
| qty_Invoiced2 | decimal? | 是 | - | - |
| qty_Receivables | decimal? | 是 | - | - |
| qty_Reconciled | decimal? | 是 | - | 对账数量 |
| qty_Reconciled2 | decimal? | 是 | - | - |
| qty_Stock | decimal? | 是 | - | 数量 |
| version | int? | 是 | - | 记录版本 |
| contractMaterialsId | int? | 是 | - | 物料销售，对应S_ContractMaterials.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| packingSlipId | int? | 是 | - | 送货单，对应FGI_PackingSlip.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| qty_estimate | string | 是 | - | - |
| qtyReturned | string | 是 | - | 退回数量 |
- **关联关系**：
  - M_MaterialPackingSlipItem.contractMaterialsId = S_ContractMaterials.recId
  - M_MaterialPackingSlipItem.creatorId = T_User.recId
  - M_MaterialPackingSlipItem.customerId = S_Customer.recId
  - M_MaterialPackingSlipItem.packingSlipId = FGI_PackingSlip.recId
  - M_MaterialPackingSlipItem.plantsId = T_Plants.recId
  - M_MaterialPackingSlipItem.postRoleId = T_PostRole.recId

---

#### 110 采购报价明细表 ( M_MaterialPriceChangedItem )
- **业务含义**：采购报价明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| effectDate | string | 是 | - | 有效期 |
| ifTaxPrice | string | 是 | - | 是否含税 |
| newPrice | string | 是 | - | 新价格 |
| newPrice2 | string | 是 | - | - |
| orgPrice | string | 是 | - | 原始价格 |
| orgPriceNoTax | string | 是 | - | 原始无税单价 |
| percents | string | 是 | - | - |
| qtyOfTo | string | 是 | - | 开始订量 |
| qtyofFrom | string | 是 | - | 结束订量 |
| rate | string | 是 | - | - |
| taxRate | string | 是 | - | 税率 |
| materialsId | string | 是 | - | 物料id |
| newCurrencyId | string | 是 | - | 新币种id |
| orgCurrencyId | string | 是 | - | 原始币种id |
| discount | string | 是 | - | 折扣率 |
| oriPriceInTax | string | 是 | - | 原始含税单价 |
| taxId | string | 是 | - | 税率id |
| vmi | string | 是 | - | 寄售 |
| deliveryCycle | string | 是 | - | 交货周期 |
- **关联关系**：无

---

#### 111 物料表 ( M_Materials )
- **业务含义**：物料表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| alertDays | int? | 是 | - | 预警天数 |
| batchNo | int? | 是 | - | 批次号 |
| bom | bool? | 是 | - | BOM |
| botCuId | int? | 是 | - | 下铜，对应S_Conductor.recId |
| code | string | 是 | - | 代码 |
| consignmentInventory | decimal? | 是 | - | 寄售库存量 |
| customUnitEntry | bool? | 是 | - | 海关单位控制 |
| customsBuyRate | decimal? | 是 | - | 海关/采购比 |
| customsStockRate | decimal? | 是 | - | 海关/库存比 |
| high | decimal? | 是 | - | 高 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifConsignment | bool? | 是 | - | 是否寄售 |
| indirectBOM | bool? | 是 | - | 间接BOM |
| inspection | bool? | 是 | - | 物料检验 |
| inventory | decimal? | 是 | - | 库存量 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| length | decimal? | 是 | - | 长 |
| manufacturers | string | 是 | - | 制造商 |
| materialFamilyId | int? | 是 | - | 物料分组 |
| materialTypeId | int? | 是 | - | 物料类型 |
| maxStockQty | decimal? | 是 | - | 最大库存 |
| mfgDateEntry | bool? | 是 | - | 制造日期控制 |
| minStockQty | decimal? | 是 | - | 安全库存 |
| mobileCost | decimal? | 是 | - | 移动成本 |
| modelCode | string | 是 | - | 型号 |
| modifiedBy | string | 是 | - | 更新用户 |
| name | string | 是 | - | 名称 |
| passRate | decimal? | 是 | - | 及格率 |
| reclaiming | bool? | 是 | - | 余料控制 |
| reorderQty | decimal? | 是 | - | 经济订购量 |
| shelfLife | int? | 是 | - | 保质期 |
| sort | string | 是 | - | 排序 |
| spare1 | string | 是 | - | 备用字段1 |
| spare2 | string | 是 | - | 备用字段2 |
| spare3 | string | 是 | - | 备用字段3 |
| spare4 | string | 是 | - | 备用字段4 |
| spare5 | string | 是 | - | 备用字段5 |
| spds | bool? | 是 | - | SPDS |
| standard | string | 是 | - | 规格 |
| standardCost | decimal? | 是 | - | 标准成本 |
| statementCost | decimal? | 是 | - | 月结成本 |
| stockBuyRate | decimal? | 是 | - | 库存/采购比 |
| textId | string | 是 | - | 备注 |
| thickCu | bool? | 是 | - | 含铜厚度 |
| topCuId | int? | 是 | - | 上铜，对应S_Conductor.recId |
| type | string | 是 | - | 类型；Materials 材料
Spare 备件 
Service 服务
Tool 工具
Equipment 设备 |
| version | int? | 是 | - | 记录版本 |
| vmi | bool? | 是 | - | 是否寄售 |
| wide | decimal? | 是 | - | 宽 |
| buyUnitId | int? | 是 | - | 采购单位，对应T_Unit.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| customsUnitId | int? | 是 | - | 海关单位，对应T_Unit.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| postRoleId | int? | 是 | - | 角色，对应T_PostRole.recId |
| productGroupId | int? | 是 | - | 物料分组，对应T_Category.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId，对应S_MaterialType.recId |
| status | string | 是 | - | 状态 |
| originalStatus | string | 是 | - | 原始状态 |
| enableApproval | bool? | 是 | - | 是否启用审批 |
| approveStatus | string | 是 | - | 审批状态 |
| approveVersion | int? | 是 | - | 审批版本 |
| flowTypeId | int? | 是 | - | 审批类型 |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| colour | string | 是 | - | 颜色 |
| orgType | string | 是 | - | 材料类型 |
| tg | string | 是 | - | TG |
| haligonfree | bool? | 是 | - | 无卤素 |
| resin | decimal? | 是 | - | 含胶量 |
| dk | decimal? | 是 | - | 介电系数 |
| lockIssue | bool? | 是 | - | 锁定发料 |
| qa | int? | 是 | - | 中检阻抗及公差(质保期) |
| watermark | bool? | 是 | - | 水印 |
| cti | int? | 是 | - | CTI |
| addTolerance | decimal? | 是 | - | 正公差 |
| subTolerance | decimal? | 是 | - | 负公差 |
| matIDStr | string | 是 | - | 物料标识符 |
| issueRate | decimal? | 是 | - | 最小包装单位值 |
| heatRate | decimal? | 是 | - | 导热系数 |
| ifheatRate | bool? | 是 | - | 是否导热系数 |
| macLayerHigh | int? | 是 | - | 介质层厚度 |
| stackup | string | 是 | - | 叠构 |
| ifOnTrial | bool? | 是 | - | 试用物料 |
| scrapRate | decimal? | 是 | - | 报废率 |
| userDef01 | string | 是 | - | 自定义属性01 |
| userDef02 | string | 是 | - | 自定义属性02 |
| userDef03 | string | 是 | - | 自定义属性03 |
| userDef04 | string | 是 | - | 自定义属性04 |
| userDef05 | string | 是 | - | 自定义属性05 |
| userDef06 | string | 是 | - | 自定义属性06 |
| userDef07 | string | 是 | - | 自定义属性07 |
| userDef08 | string | 是 | - | 自定义属性08 |
| userDef09 | string | 是 | - | 自定义属性08 |
| userDef10 | string | 是 | - | 自定义属性10 |
| userDef11 | string | 是 | - | 自定义属性11 |
| userDef12 | string | 是 | - | 自定义属性12 |
| userDef13 | string | 是 | - | 自定义属性13 |
| userDef14 | string | 是 | - | 自定义属性14 |
| userDef15 | string | 是 | - | 自定义属性15 |
| userDef16 | string | 是 | - | 自定义属性16 |
| userDef17 | string | 是 | - | 自定义属性17 |
| userDef18 | string | 是 | - | 自定义属性18 |
| userDef19 | string | 是 | - | 自定义属性19 |
| userDef20 | string | 是 | - | 自定义属性20 |
| ifBonded | bool? | 是 | - | 保税 |
| ifProcessSpecialMaterials | bool? | 是 | - | 是否工艺专用料 |
| ifSale | bool? | 是 | - | 允许销售 |
| spdsRequired | bool? | 是 | - | 强制SPDS |
| uniontransIndate | DateTime? | 是 | - | - |
| ifDepartmentSpecialMaterials | bool? | 是 | - | 是否部门专用料 |
| validityAlertDays | int? | 是 | - | 有效期预警天数 |
| copyMaterialsId | string | 是 | - | 被复制物料ID；M_Materials.recId |
| inventoryCategoryId | string | 是 | - | 存货类别；M_InventoryCategory |
| mustPleaseBuy | string | 是 | - | 必须走请购 |
- **关联关系**：
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

#### 112 物料所属公司 ( M_MaterialsCompany )
- **业务含义**：物料所属公司
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | T_Category |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
- **关联关系**：
  - M_MaterialsCompany.companyId = T_Company.recId
  - M_MaterialsCompany.materialsId = M_Materials.recId

---

#### 113 物料可分配数量表(占用) ( M_MaterialsCostByPlant )
- **业务含义**：物料可分配数量表(占用)
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| averageCostByMonth | decimal? | 是 | - | - |
| averageCostByMonth_Current | decimal? | 是 | - | - |
| averageUnitCost | decimal? | 是 | - | - |
| note | string | 是 | - | - |
| qtyInStock | decimal? | 是 | - | 库存数量 |
| qtyInVStock | decimal? | 是 | - | 寄售库存 |
| qtyOfMO | decimal? | 是 | - | MO需求数量 |
- **关联关系**：无

---

#### 114 发料和退回表 ( M_MaterialsIssueNote )
- **业务含义**：发料和退回表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| entDate | DateTime? | 是 | - | 创建日期 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| locked | bool? | 是 | - | 是否锁定0否  1是 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| stockDate | DateTime? | 是 | - | 发料/退料日期 |
| type | string | 是 | - | SPicking 标准领料  SUnloading 物料退回 BUnloading BOM物料退回 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| userId | int? | 是 | - | 领料人，对应T_User.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_MaterialsIssueNote.companyId = T_Company.recId
  - M_MaterialsIssueNote.creatorId = T_User.recId
  - M_MaterialsIssueNote.departmentId = T_Department.recId
  - M_MaterialsIssueNote.postRoleId = T_PostRole.recId
  - M_MaterialsIssueNote.userId = T_User.recId
  - M_MaterialsIssueNote.warehouseId = T_Warehouse.recId

---

#### 115 发料和退回明细 ( M_MaterialsIssueNoteItem )
- **业务含义**：发料和退回明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 116 物料发料和退回批次 ( M_MaterialsIssueNoteItemBatch )
- **业务含义**：物料发料和退回批次
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| averageUnitCost | decimal? | 是 | - | 不含税单价 |
| bomPicklistItemBatchId | int? | 是 | - | BOM领料批次，对应M_BomPicklistItemBatch.recId |
| createDate | DateTime? | 是 | - | 实际发料时间 |
| inventoryId | int? | 是 | - | 对应M_Inventory.recId |
| ma_Cost | decimal? | 是 | - | 本币不含税单价 |
| materialInventoryOutId | int? | 是 | - | 对应M_MaterialInventoryOut.recId |
| note | string | 是 | - | 备注 |
| materialsIssueNoteCode | string | 是 | - | 发料和退料单号 |
| poItemId | int? | 是 | - | - |
| quantity | decimal? | 是 | - | 发料数量（库存批次发料） |
| type | string | 是 | - | SPicking 标准领料  SUnloading 物料退回 BUnloading BOM物料退回 |
| version | int? | 是 | - | - |
| inventoryBatchId | int? | 是 | - | 物料库存批次，对应M_InventoryBatch.recId |
| materialsIssueNoteItemId | int? | 是 | - | 发料和退回明细，对应M_MaterialsIssueNoteItem.recId |
- **关联关系**：
  - M_MaterialsIssueNoteItemBatch.bomPicklistItemBatchId = M_BomPicklistItemBatch.recId
  - M_MaterialsIssueNoteItemBatch.inventoryId = M_Inventory.recId
  - M_MaterialsIssueNoteItemBatch.materialInventoryOutId = M_MaterialInventoryOut.recId
  - M_MaterialsIssueNoteItemBatch.inventoryBatchId = M_InventoryBatch.recId
  - M_MaterialsIssueNoteItemBatch.materialsIssueNoteItemId = M_MaterialsIssueNoteItem.recId

---

#### 117 物料所在仓库 ( M_MaterialsWarehouse )
- **业务含义**：物料所在仓库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| inventory | decimal? | 是 | - | 库存量 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| maxStockQty | decimal? | 是 | - | 最大库存 |
| minStockQty | decimal? | 是 | - | 安全库存 |
| modifiedBy | string | 是 | - | 修改人 |
| reorderQty | decimal? | 是 | - | 经济订量 |
| version | int? | 是 | - | - |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_MaterialsWarehouse.locationId = T_Location.recId
  - M_MaterialsWarehouse.materialsId = M_Materials.recId
  - M_MaterialsWarehouse.warehouseId = T_Warehouse.recId

---

#### 118 月结记账表 ( M_MonthlyClosing )
- **业务含义**：月结记账表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cost_Issued | decimal? | 是 | - | 发料总金额 |
| cost_Issued_back | decimal? | 是 | - | 退料总金额 |
| cost_On_hand | decimal? | 是 | - | 当前总金额 |
| cost_Physical_Count | decimal? | 是 | - | 盘点总金额 |
| cost_Received | decimal? | 是 | - | 转入总金额 |
| cost_Returned | decimal? | 是 | - | 转出总金额 |
| cost_Scrapped | decimal? | 是 | - | 报废总金额 |
| cost_Stocked | decimal? | 是 | - | 入仓总金额 |
| cost_begin | decimal? | 是 | - | 期初总金额 |
| cost_end | decimal? | 是 | - | 期末总金额 |
| monthlyClosingDate | DateTime? | 是 | - | 月结时间 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | Active 开启  Close 结束 |
| version | int? | 是 | - | - |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| uuid | string | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| cost_TransferIn | decimal? | 是 | ((0)) | 转入总金额 |
| cost_TransferOut | decimal? | 是 | ((0)) | 转出总金额 |
- **关联关系**：
  - M_MonthlyClosing.fiscalPeriodId = T_FiscalPeriod.recId
  - M_MonthlyClosing.plantsId = T_Plants.recId
  - M_MonthlyClosing.companyId = T_Company.recId
  - M_MonthlyClosing.warehouseId = T_Warehouse.recId

---

#### 119 物料月结部门表 ( M_MonthlyClosingDepartment )
- **业务含义**：物料月结部门表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| averageCostByMonth_Current | string | 是 | - | - |
| companyId | string | 是 | - | - |
| cost_Issued | string | 是 | - | - |
| cost_Issued_back | string | 是 | - | - |
| cost_RepairIssued | string | 是 | - | - |
| cost_RepairIssued_back | string | 是 | - | - |
| cost_consignment | string | 是 | - | - |
| departmentId | string | 是 | - | - |
| fiscalPeriodId | string | 是 | - | - |
| materialGroupId | string | 是 | - | - |
| materialId | string | 是 | - | - |
| qty_Issued | string | 是 | - | - |
| qty_Issued_back | string | 是 | - | - |
| qty_RepairIssued | string | 是 | - | - |
| qty_RepairIssued_back | string | 是 | - | - |
| qty_consignment | string | 是 | - | - |
| warehouseId | string | 是 | - | - |
| qty_Issued_back2 | string | 是 | - | - |
| cost_Issued_back2 | string | 是 | - | - |
| qty_RepairIssued_back2 | string | 是 | - | - |
| cost_RepairIssued_back2 | string | 是 | - | - |
- **关联关系**：无

---

#### 120 月结记账明细表 ( M_MonthlyClosingItem )
- **业务含义**：月结记账明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cost_Issued | decimal? | 是 | - | 发料金额 |
| cost_Issued_back | decimal? | 是 | - | 退料金额 |
| cost_Issued_back2 | string | 是 | - | - |
| cost_On_hand | decimal? | 是 | - | 当前金额 |
| cost_Physical_Count | decimal? | 是 | - | 盘点金额 |
| cost_Received | decimal? | 是 | - | 接收金额（未使用） |
| cost_Returned | decimal? | 是 | - | 退货金额 |
| cost_Scrapped | decimal? | 是 | - | 报废金额 |
| cost_Stocked | decimal? | 是 | - | 入仓金额 |
| cost_begin | decimal? | 是 | - | 期初金额 |
| cost_end | decimal? | 是 | - | 期末金额 |
| qty_Issued | decimal? | 是 | - | 发料数量 |
| qty_Issued_back | decimal? | 是 | - | 退料数量 |
| qty_Issued_back2 | string | 是 | - | - |
| qty_On_hand | decimal? | 是 | - | 当前数量 |
| qty_Physical_Count | decimal? | 是 | - | 盘点数量 |
| qty_Received | decimal? | 是 | - | 接收数量(未使用) |
| qty_Returned | decimal? | 是 | - | 退货数量 |
| qty_Scrapped | decimal? | 是 | - | 报废数量 |
| qty_Stocked | decimal? | 是 | - | 入仓数量 |
| qty_begin | decimal? | 是 | - | 期初数量 |
| qty_end | decimal? | 是 | - | 期末数量 |
| version | int? | 是 | - | - |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| monthlyClosingId | int? | 是 | - | 月结记账表，对应M_MonthlyClosing.recId |
| cost_TransferIn | decimal? | 是 | ((0)) | - |
| cost_TransferOut | decimal? | 是 | ((0)) | - |
| qty_TransferIn | decimal? | 是 | ((0)) | - |
| qty_TransferOut | decimal? | 是 | ((0)) | - |
| cost_RepairIssued | string | 是 | - | 维修发料 |
| cost_RepairIssued_back | string | 是 | - | 维修发料退回 |
| diff_Amount | string | 是 | - | 调整金额 |
| cost_sale | string | 是 | - | 物料出售金额 |
| qty_sale | string | 是 | - | 物料出售数 |
| qty_RepairIssued | string | 是 | - | 维修发料 |
| qty_RepairIssued_back | string | 是 | - | 维修退料 |
| qty_RepairIssued_back2 | string | 是 | - | - |
- **关联关系**：
  - M_MonthlyClosingItem.materialsId = M_Materials.recId
  - M_MonthlyClosingItem.monthlyClosingId = M_MonthlyClosing.recId

---

#### 121 采购单 ( M_PurchaseOrder )
- **业务含义**：采购单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 122 采购审批表 ( M_PurchaseOrderHistory )
- **业务含义**：采购审批表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| purchaseOrderId | int? | 是 | - | 对应M_PurchaseOrder.recId |
- **关联关系**：
  - M_PurchaseOrderHistory.myId = T_User.recId
  - M_PurchaseOrderHistory.purchaseOrderId = M_PurchaseOrder.recId

---

#### 123 采购明细单 ( M_PurchaseOrderItem )
- **业务含义**：采购明细单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| FGI_Inventory | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | 发票金额 |
| amount_Reconciled | decimal? | 是 | - | - |
| approveStatus | string | 是 | - | - |
| committedDate | DateTime? | 是 | - | 承若日期 |
| contractMaterialsId | int? | 是 | - | 原材料出售合同明细，对应S_ContractMaterials.recId |
| deliveryDate | DateTime? | 是 | - | 交付日期 |
| discount | decimal? | 是 | - | 折扣率 |
| ideas | string | 是 | - | - |
| itemNotes | string | 是 | - | 备注 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| lineNumber | int? | 是 | - | - |
| misMaterialDesc | string | 是 | - | 杂料描述 |
| misMaterialSpec | string | 是 | - | - |
| miscType | string | 是 | - | - |
| moId | int? | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| prLinkId | int? | 是 | - | 请购受理，对应M_RequisitionsItemAccepted.recId |
| priceInTax | decimal? | 是 | - | 含税单价 |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| qtyDefected | decimal? | 是 | - | 缺陷数量 |
| qtyInspection | decimal? | 是 | - | 检验数量 |
| qtyInvoiced | decimal? | 是 | - | 发票数量 |
| qtyOrdered | decimal? | 是 | - | 采购数量 |
| qtyRecieved | decimal? | 是 | - | 接收数量 |
| qtyReturned | decimal? | 是 | - | 退回数量 |
| qtyScrapped | decimal? | 是 | - | 报废数量 |
| qtyStocked | decimal? | 是 | - | 入库数量 |
| qtyToReturn | decimal? | 是 | - | 退货数量 |
| qtyToStock | decimal? | 是 | - | 将要入库数量 |
| qty_Invoiced | decimal? | 是 | - | 将要写发票数量 |
| qty_Reconciled | decimal? | 是 | - | 将接收数量 |
| requestDate | DateTime? | 是 | - | 需求日期 |
| salesOrderId | int? | 是 | - | - |
| sbRate | decimal? | 是 | - | 库存/采购 |
| scRate | decimal? | 是 | - | - |
| status | string | 是 | - | - |
| tax1Rate | decimal? | 是 | - | - |
| tax1Val | decimal? | 是 | - | - |
| tax2Rate | decimal? | 是 | - | - |
| tax2Val | decimal? | 是 | - | - |
| tax3Rate | decimal? | 是 | - | - |
| tax3Val | decimal? | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| taxVal | decimal? | 是 | - | - |
| totalInTax | decimal? | 是 | - | 含税金额 |
| totalNoTax | decimal? | 是 | - | 不含税金额 |
| version | int? | 是 | - | - |
| buyUnitId | int? | 是 | - | 采购单位，对应T_Unit.recId |
| customsUnitId | int? | 是 | - | 海关单位，对应T_Unit.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| purchaseOrderId | int? | 是 | - | 主表，对应M_PurchaseOrder.recId |
| stockUnitId | int? | 是 | - | 入库单位，对应T_Unit.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
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

#### 124 采购待审批 ( M_PurchaseOrderWF )
- **业务含义**：采购待审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | - |
| purchaseOrderId | int? | 是 | - | - |
- **关联关系**：无

---

#### 125 采购预算 ( M_PurchasingBudget )
- **业务含义**：采购预算
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 126 预算明细（用户） ( M_PurchasingBudgetItem )
- **业务含义**：预算明细（用户）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 127 项目管理 ( M_RDProject )
- **业务含义**：项目管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 128 物料接收 ( M_Receipt )
- **业务含义**：物料接收
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 接收单号 |
| customsCode | string | 是 | - | 海关单号 |
| deliveryCode | string | 是 | - | 送货单号 |
| entDate | DateTime? | 是 | - | 收货日期 |
| lastModifyDate | DateTime? | 是 | - | 最后修改 |
| locked | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| note | string | 是 | - | - |
| receiveDate | DateTime? | 是 | - | - |
| type | string | 是 | - | PO 有采购接收 NPO无采购接收 MiscPO 杂项采购接收 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - M_Receipt.companyId = T_Company.recId
  - M_Receipt.creatorId = T_User.recId
  - M_Receipt.plantsId = T_Plants.recId
  - M_Receipt.postRoleId = T_PostRole.recId
  - M_Receipt.suppliersId = M_Suppliers.recId

---

#### 129 物料接收明细 ( M_ReceiptItem )
- **业务含义**：物料接收明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | 寄售总数 |
| amount_Receivables | decimal? | 是 | - | 应收数量 |
| amount_Reconciled | decimal? | 是 | - | - |
| avgCost | decimal? | 是 | - | 平均成本 |
| suppBatchNo | string | 是 | - | 供应商批号 |
| customUnitEntry | bool? | 是 | - | - |
| dateDiffVal | int? | 是 | - | 迟交天数 |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| fifoCost | decimal? | 是 | - | - |
| ifInspection | bool? | 是 | - | 是否要检查 0 否  1 是 |
| internalBatchNo | string | 是 | - | 物料批次（内部批次） |
| inventoryMiscBatchId | int? | 是 | - | 对应M_InventoryMiscBatch.recId |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| mfgDateEntry | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| poCode | string | 是 | - | - |
| poDate | DateTime? | 是 | - | - |
| poItemId | int? | 是 | - | 采购明细表，对应M_PurchaseOrderItem.FGI_Inventory |
| poType | string | 是 | - | S 采购，免检，M杂项 |
| priceInTax | decimal? | 是 | - | 含税单价 |
| qtyCustoms | decimal? | 是 | - | 海关接收数量 |
| qtyDefected | decimal? | 是 | - | 缺陷数量 |
| qtyInInspection | decimal? | 是 | - | 检查数量 |
| qtyInspected | decimal? | 是 | - | 已检查数量 |
| qtyRecieved | decimal? | 是 | - | 接收数量 |
| qtyReturned | decimal? | 是 | - | 退货数量 |
| EQ_PIO | decimal? | 是 | - | 报废数量 |
| qtyStocked | decimal? | 是 | - | 入库数量 |
| qtyToReturn | decimal? | 是 | - | 将要退货数量 |
| qtyToStock | decimal? | 是 | - | 将要入库数 |
| qty_Invoiced | decimal? | 是 | - | 已开票数量 |
| qty_Receivables | decimal? | 是 | - | - |
| qty_Reconciled | decimal? | 是 | - | 已对账数量（采购对账） |
| requestDate | DateTime? | 是 | - | 订购日期 |
| sbRate | decimal? | 是 | - | 库存/采购比 |
| status | string | 是 | - | - |
| supplierPartCode | string | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| buyUnitId | int? | 是 | - | 采购单位，对应T_Unit.recId |
| customsUnitId | int? | 是 | - | 海关单位，对应T_Unit.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| receiptId | int? | 是 | - | 主表，对应M_Receipt.recId |
| stockUnitId | int? | 是 | - | 入库单位，对应T_Unit.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| currencyId | string | 是 | - | 币种 |
- **关联关系**：
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

#### 130 M_ReplaceMaterials ( M_ReplaceMaterials )
- **业务含义**：ERP 系统 M_ReplaceMaterials 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amountRate | decimal? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| replaceMaterialsId | int? | 是 | - | 对应M_ReplaceMaterials.recId |
- **关联关系**：
  - M_ReplaceMaterials.materialsId = M_Materials.recId
  - M_ReplaceMaterials.replaceMaterialsId = M_ReplaceMaterials.recId

---

#### 131 请购单 ( M_Requisitions )
- **业务含义**：请购单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| code | string | 是 | - | 请购单号 |
| enableApproval | bool? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| mrpId | int? | 是 | - | - |
| note | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| requestedDate | DateTime? | 是 | - | 请购日期 |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | Valid：已审核  Active：审核中 |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
- **关联关系**：
  - M_Requisitions.companyId = T_Company.recId
  - M_Requisitions.creatorId = T_User.recId
  - M_Requisitions.departmentId = T_Department.recId
  - M_Requisitions.flowTypeId = T_FlowType.recId
  - M_Requisitions.plantsId = T_Plants.recId
  - M_Requisitions.postRoleId = T_PostRole.recId

---

#### 132 请购审批表 ( M_RequisitionsHistory )
- **业务含义**：请购审批表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| requisitionsId | int? | 是 | - | 对应M_Requisitions.recId |
- **关联关系**：
  - M_RequisitionsHistory.myId = T_User.recId
  - M_RequisitionsHistory.requisitionsId = M_Requisitions.recId

---

#### 133 请购明细单 ( M_RequisitionsItem )
- **业务含义**：请购明细单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| acceptedQuantity | decimal? | 是 | - | 已受理数量 |
| approveStatus | string | 是 | - | 受理状态  Ordered：已下单  Close：已关闭 |
| ideas | string | 是 | - | - |
| ifSpecifySuppId | bool? | 是 | - | 是否定制供应商0 否  1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| misMaterialsDesc | string | 是 | - | - |
| misMaterialsSpec | string | 是 | - | - |
| miscType | string | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| orderQuantity | decimal? | 是 | - | 已下单数量 |
| poLinkId | int? | 是 | - | 没有值 |
| quantity | decimal? | 是 | - | 请购数量 |
| requestedDate | DateTime? | 是 | - | 需求日期 |
| version | int? | 是 | - | - |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| requisitionsId | int? | 是 | - | 接收表，对应M_Requisitions.recId |
| stockUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - M_RequisitionsItem.materialsId = M_Materials.recId
  - M_RequisitionsItem.postRoleId = T_PostRole.recId
  - M_RequisitionsItem.requisitionsId = M_Requisitions.recId
  - M_RequisitionsItem.stockUnitId = T_Unit.recId
  - M_RequisitionsItem.suppliersId = M_Suppliers.recId

---

#### 134 请购受理表 ( M_RequisitionsItemAccepted )
- **业务含义**：请购受理表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| acceptedDate | DateTime? | 是 | - | 受理日期 |
| buyQuantity | decimal? | 是 | - | 采购数量（准备采购数量） |
| createDate | DateTime? | 是 | - | 建单日期 |
| ifSpecifySuppId | bool? | 是 | - | 指定供应商，对应M_Suppliers.recId |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| misMaterialsDesc | string | 是 | - | - |
| misMaterialsSpec | string | 是 | - | - |
| miscType | string | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| poLinkId | int? | 是 | - | 采购订单明细表，对应M_PurchaseOrderItem.FGI_Inventory |
| priceInTax | decimal? | 是 | - | 含税单价 |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| requestedDate | DateTime? | 是 | - | 需求日期 |
| requisitionsCode | string | 是 | - | 请购单号 |
| requisitionsItemId | int? | 是 | - | 请购明细单，对应M_RequisitionsItem.recId |
| requisitionsType | string | 是 | - | S:标准请购 M 杂项请购 |
| sbRate | decimal? | 是 | - | 库存/采购比 |
| status | string | 是 | - | 状态 |
| stockQuantity | decimal? | 是 | - | 受理数量 |
| taxRate | decimal? | 是 | - | 税率 |
| transDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| acceptorId | int? | 是 | - | 对应T_User.recId |
| buyUnitId | int? | 是 | - | 对应T_Unit.recId |
| creatorId | int? | 是 | - | 对应T_User.recId |
| currencyId | int? | 是 | - | 对应T_Currency.recId |
| departmentId | int? | 是 | - | 对应T_Department.recId |
| materialsId | int? | 是 | - | 对应M_Materials.recId |
| plantsId | int? | 是 | - | 对应T_Plants.recId |
| postRoleId | int? | 是 | - | 对应T_PostRole.recId |
| stockUnitId | int? | 是 | - | 对应T_Unit.recId |
| suppliersId | int? | 是 | - | 对应M_Suppliers.recId |
| vmi | string | 是 | - | 是否寄售 0 否 1 是 |
- **关联关系**：
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

#### 135 M_RequisitionsWF ( M_RequisitionsWF )
- **业务含义**：ERP 系统 M_RequisitionsWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| requisitionsId | int? | 是 | - | 请购单，对应M_Requisitions.recId |
- **关联关系**：
  - M_RequisitionsWF.myId = T_User.recId
  - M_RequisitionsWF.requisitionsId = M_Requisitions.recId

---

#### 136 退货表 ( M_ReturnOrder )
- **业务含义**：退货表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 退货单号 |
| entDate | DateTime? | 是 | - | 建单日期 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| locked | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| returnDate | DateTime? | 是 | - | 退货日期 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - M_ReturnOrder.companyId = T_Company.recId
  - M_ReturnOrder.creatorId = T_User.recId
  - M_ReturnOrder.plantsId = T_Plants.recId
  - M_ReturnOrder.postRoleId = T_PostRole.recId
  - M_ReturnOrder.suppliersId = M_Suppliers.recId

---

#### 137 退货明细表 ( M_ReturnOrderItem )
- **业务含义**：退货明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| debitMemoDate | DateTime? | 是 | - | 登记日期 |
| debitMemoItemId | int? | 是 | - | 供应商扣款明细，对应F_AP_DebitMemoItem.recId |
| ifCheck | bool? | 是 | - | - |
| note | string | 是 | - | 备注 |
| qtyMemo | decimal? | 是 | - | - |
| quantity | decimal? | 是 | - | 数量 |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| iqcId | int? | 是 | - | 物料检验，对应M_IQC.recId |
| returnOrderId | int? | 是 | - | 退货表，对应M_ReturnOrder.recId |
- **关联关系**：
  - M_ReturnOrderItem.debitMemoItemId = F_AP_DebitMemoItem.recId
  - M_ReturnOrderItem.iqcId = M_IQC.recId
  - M_ReturnOrderItem.returnOrderId = M_ReturnOrder.recId

---

#### 138 SPDS管理 ( M_SPDS )
- **业务含义**：SPDS管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| customsStockRate | decimal? | 是 | - | 海关/库存比 |
| deliveryCycle | int? | 是 | - | 交货周期 |
| enableApproval | bool? | 是 | - | 是否提交审核 0 否 1 是 |
| exchRate | decimal? | 是 | - | 兑换率 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| minQty | decimal? | 是 | - | 最小订量 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| reOrderQty | decimal? | 是 | - | 经济订量 |
| status | string | 是 | - | - |
| stockBuyRate | decimal? | 是 | - | 库存/采购比 |
| supplierPartCode | string | 是 | - | 供应商物料代码 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| vmi | bool? | 是 | - | - |
| buyUnitId | int? | 是 | - | 采购单位，对应T_Unit.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 币种，对应T_Currency.recId |
| customsUnitId | int? | 是 | - | 海关单位，对应T_Unit.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| stockUnitId | int? | 是 | - | 入库单位，对应T_Unit.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| ifTrial | string | 是 | - | 试用 |
| expirationDate | string | 是 | - | 有效期 |
- **关联关系**：
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

#### 139 M_SPDSHistory ( M_SPDSHistory )
- **业务含义**：ERP 系统 M_SPDSHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | - |
| spdsId | int? | 是 | - | - |
- **关联关系**：无

---

#### 140 SPDS管理明细 ( M_SPDSItem )
- **业务含义**：SPDS管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| activateDate | DateTime? | 是 | - | 生效时间 |
| discount | decimal? | 是 | - | 折扣% |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| priceInTax | decimal? | 是 | - | 含税单价 |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| qtyOfTo | decimal? | 是 | - | 结束订购数量 |
| qtyofFrom | decimal? | 是 | - | 开始订购数量 |
| version | int? | 是 | - | - |
| spdsId | int? | 是 | - | 主表，对应M_SPDS.recId |
- **关联关系**：
  - M_SPDSItem.spdsId = M_SPDS.recId

---

#### 141 M_SPDSWF ( M_SPDSWF )
- **业务含义**：ERP 系统 M_SPDSWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| spdsId | int? | 是 | - | 对应M_SPDS.recId |
- **关联关系**：
  - M_SPDSWF.myId = T_User.recId
  - M_SPDSWF.spdsId = M_SPDS.recId

---

#### 142 M_StepCheck ( M_StepCheck )
- **业务含义**：ERP 系统 M_StepCheck 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| checkDate | string | 是 | - | - |
| code | string | 是 | - | - |
| note | string | 是 | - | - |
| status | string | 是 | - | - |
| version | string | 是 | - | - |
| creatorId | string | 是 | - | - |
| fiscalPeriodId | string | 是 | - | 期间表id，对应T_FiscalPeriod.recId |
| postRoleId | string | 是 | - | 岗位表，对应T_PostRole.recId |
| stepsId | string | 是 | - | 工序id，对应T_Steps.recId |
- **关联关系**：
  - M_StepCheck.fiscalPeriodId = T_FiscalPeriod.recId
  - M_StepCheck.postRoleId = T_PostRole.recId
  - M_StepCheck.stepsId = T_Steps.recId

---

#### 143 M_StepCheckItem ( M_StepCheckItem )
- **业务含义**：ERP 系统 M_StepCheckItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| lastFiscalPeriodId | string | 是 | - | - |
| note | string | 是 | - | - |
| qtyBegin | string | 是 | - | 上月结存 |
| qtyCheck | string | 是 | - | 本月结存（盘点数） |
| qtyPicking | string | 是 | - | 本月领料 |
| stepMaterialStandardId | string | 是 | - | 工序间接物料，对应T_StepIndiectMatLink.recId |
| version | string | 是 | - | - |
| materialsId | string | 是 | - | 物料表id，对应M_Materials.recId |
| stepCheckId | string | 是 | - | 主表id，对应M_StepCheck.recId |
| stockUnitId | string | 是 | - | - |
| price | string | 是 | - | 价格 |
| qtyBack | string | 是 | - | 本月退料 |
| qtyConsume | string | 是 | - | 本月消耗 |
| consumeAmount | string | 是 | - | 消耗金额 |
| balanceAmount | string | 是 | - | 结存金额 |
- **关联关系**：
  - M_StepCheckItem.stepMaterialStandardId = T_StepIndiectMatLink.recId
  - M_StepCheckItem.materialsId = M_Materials.recId
  - M_StepCheckItem.stepCheckId = M_StepCheck.recId

---

#### 144 供应商资料 ( M_Suppliers )
- **业务含义**：供应商资料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| account | string | 是 | - | 银行账户 |
| accreditationReviews | string | 是 | - | 评语 |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| bank | string | 是 | - | 开户银行 |
| code | string | 是 | - | 供应商代码 |
| deliveryAdd | string | 是 | - | 送货地址 |
| email | string | 是 | - | 邮件 |
| employees | string | 是 | - | 员工数目 |
| enableApproval | bool? | 是 | - | - |
| ename | string | 是 | - | 英文名称 |
| fax | string | 是 | - | 传真 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| ifConsignment | bool? | 是 | - | 是否寄售 0 否 1 是 |
| ifForeign | bool? | 是 | - | 是否国外采购商 0 否 1 是 |
| ifReactionary | bool? | 是 | - | 是否外协 0 否 1 是     是否反动 0 否 1 是 |
| ifReconcile | bool? | 是 | - | 是否对账 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| ledgerId | int? | 是 | - | - |
| legal | string | 是 | - | 法人代表 |
| majorCustomers | string | 是 | - | 主要客户 |
| majorSuppliers | string | 是 | - | 主要供应商 |
| mobilePhone | string | 是 | - | 联系电话 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 供应商名称 |
| nature | string | 是 | - | 公司性质 |
| nickName | string | 是 | - | 简称 |
| officeAdd | string | 是 | - | 办公地址 |
| operatingItems | string | 是 | - | 经营项目 |
| originalStatus | string | 是 | - | - |
| outsoucing | bool? | 是 | - | 是否外协 0 否 1 是 |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| qualitySystem | string | 是 | - | 质量体系 |
| reconcileDate | int? | 是 | - | 对账日期 |
| reconciliationDate | DateTime? | 是 | - | - |
| reconciliationType | string | 是 | - | - |
| regAdd | string | 是 | - | 注册地址 |
| regCapital | string | 是 | - | 注册资本 |
| regNo | string | 是 | - | 工商注册号 |
| selfCompanyId | int? | 是 | - | 评审等级 |
| setupDate | DateTime? | 是 | - | 成立日期 |
| shareholder | string | 是 | - | 股东信息 |
| sort | string | 是 | - | 排序 |
| spare1 | string | 是 | - | 备注1 |
| spare2 | string | 是 | - | 备注2 |
| spare3 | string | 是 | - | 备注3 |
| spare4 | string | 是 | - | 备注4 |
| spare5 | string | 是 | - | 备注5 |
| status | string | 是 | - | Valid 审批通过 |
| taxRate | decimal? | 是 | - | 税率 |
| taxRegNo | string | 是 | - | 税务登记号 |
| telephone | string | 是 | - | 固话 |
| textId | string | 是 | - | 记事本，对应T_Text.recId |
| totalAssets | string | 是 | - | 总资产 |
| vat | string | 是 | - | - |
| version | int? | 是 | - | - |
| webSite | string | 是 | - | 网址 |
| zip | string | 是 | - | 邮编 |
| areaId | int? | 是 | - | 区域，对应T_Area.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| reditId | int? | 是 | - | 对应T_Cate.recId |
| currencyId | int? | 是 | - | 币种，对应T_Currency.recId |
| flowTypeId | int? | 是 | - | 审批；流程，对应T_FlowType.recId |
| fobId | int? | 是 | - | 贸易方式，对应T_FOB.recId |
| paymentMethodId | int? | 是 | - | 付款方式，对应T_PaymentMethod.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
- **关联关系**：
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

#### 145 供应商所属公司 ( M_SuppliersCompany )
- **业务含义**：供应商所属公司
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - M_SuppliersCompany.companyId = T_Company.recId
  - M_SuppliersCompany.suppliersId = M_Suppliers.recId

---

#### 146 供应商审批记录 ( M_SuppliersHistory )
- **业务含义**：供应商审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| suppliersId | int? | 是 | - | 对应M_Suppliers.recId |
- **关联关系**：
  - M_SuppliersHistory.myId = T_User.recId
  - M_SuppliersHistory.suppliersId = M_Suppliers.recId

---

#### 147 M_SuppliersWF ( M_SuppliersWF )
- **业务含义**：ERP 系统 M_SuppliersWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| suppliersId | int? | 是 | - | 对应M_Suppliers.recId |
- **关联关系**：
  - M_SuppliersWF.myId = T_User.recId
  - M_SuppliersWF.suppliersId = M_Suppliers.recId

---

#### 148 调拨管理 ( M_Transfer )
- **业务含义**：调拨管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 调拨单号 |
| entDate | DateTime? | 是 | - | 建单时间 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 单据状态：Pending:制作中  Received：已接收 Transferred:已调拨 |
| transferDate | DateTime? | 是 | - | 调拨时间 |
| type | string | 是 | - | MyCompanyOut：调出   MyCompanyIn ：调入 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| destWarehouseId | int? | 是 | - | 目标仓库，对应T_Warehouse.recId |
| origWarehouseId | int? | 是 | - | 原仓库，对应T_Warehouse.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| receiveId | int? | 是 | - | 接收人，对应T_User.recId |
| receiveCompanyId | int? | 是 | - | 接收公司，对应T_Company.recId |
- **关联关系**：
  - M_Transfer.creatorId = T_User.recId
  - M_Transfer.destWarehouseId = T_Warehouse.recId
  - M_Transfer.origWarehouseId = T_Warehouse.recId
  - M_Transfer.postRoleId = T_PostRole.recId
  - M_Transfer.receiveId = T_User.recId
  - M_Transfer.receiveCompanyId = T_Company.recId

---

#### 149 调拨管理明细 ( M_TransferItem )
- **业务含义**：调拨管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| actualCost | decimal? | 是 | - | 成本价 |
| inventoryId | int? | 是 | - | 物料库存（暂时没用），对应M_Inventory.recId |
| note | string | 是 | - | 备注 |
| purchasePrice | decimal? | 是 | - | 采购单价（不含税库存单位价格） |
| quantity | decimal? | 是 | - | 调拨数量 |
| transferPrice | decimal? | 是 | - | 调拨时的单价 |
| version | int? | 是 | - | - |
| inventoryBatchId | int? | 是 | - | 物料库存批次，对应M_InventoryBatch.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| transferId | int? | 是 | - | 主表，对应M_Transfer.recId |
| transferItemId | int? | 是 | - | 自身表；调入和调出的行对应，对应M_TransferItem.recId |
- **关联关系**：
  - M_TransferItem.inventoryId = M_Inventory.recId
  - M_TransferItem.inventoryBatchId = M_InventoryBatch.recId
  - M_TransferItem.locationId = T_Location.recId
  - M_TransferItem.transferId = M_Transfer.recId
  - M_TransferItem.transferItemId = M_TransferItem.recId

---

#### 150 物料入库 ( M_Warehousing )
- **业务含义**：物料入库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 入库单号 |
| entDate | DateTime? | 是 | - | 创建日期 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| locked | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| stockDate | DateTime? | 是 | - | 入库时间 |
| type | string | 是 | - | 类型：S 标准入库     V:寄售补给入库  C:寄售处理订单 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - M_Warehousing.companyId = T_Company.recId
  - M_Warehousing.creatorId = T_User.recId
  - M_Warehousing.postRoleId = T_PostRole.recId
  - M_Warehousing.warehouseId = T_Warehouse.recId

---

#### 151 物料入库明细 ( M_WarehousingItem )
- **业务含义**：物料入库明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| suppBatchNo | string | 是 | - | 供应商批号 |
| customsCode | string | 是 | - | 客户代码 |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| ifCheck | bool? | 是 | - | 是否检验0否  1 是 |
| internalBatchNo | string | 是 | - | 内部批号(物料批号) |
| inventoryBatchId | int? | 是 | - | 物料库存批次，对应M_InventoryBatch.recId |
| inventoryId | int? | 是 | - | 物料库存，对应M_Inventory.recId |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| note | string | 是 | - | 备注 |
| priceInTax | decimal? | 是 | - | 含税单价（采购单价） |
| qtyCustoms | decimal? | 是 | - | 海关接收数量 |
| quantity | decimal? | 是 | - | 库存入库数量（采购入仓数量*库存采购比） |
| receiptCode | string | 是 | - | 接收单号 |
| receiptDate | DateTime? | 是 | - | 接收日期 |
| receiptItemId | int? | 是 | - | 物料接收明细表，对应M_ReceiptItem.recId |
| sbRate | decimal? | 是 | - | 汇率 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| buyUnitId | int? | 是 | - | 采购单位，对应T_Unit.recId |
| customsUnitId | int? | 是 | - | 海关单位，对应T_Unit.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| stockUnitId | int? | 是 | - | 入库单位，对应T_Unit.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| warehousingId | int? | 是 | - | 主表，对应M_Warehousing.recId |
- **关联关系**：
  - M_WarehousingItem.inventoryBatchId = M_InventoryBatch.recId
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

#### 152 装箱单编号表（箱包表） ( FGI_CartonsNumber )
- **业务含义**：装箱单编号表（箱包表）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| code | string | 是 | - | 箱子编号 |
| note | string | 是 | - | 备注 |
| qtyQualified | int? | 是 | - | 数量 |
| qtyScrapped | int? | 是 | - | 叉板数pcs |
| status | string | 是 | - | 入仓状态 |
| cartonsNumberService | int? | 是 | - | 生产入库，对应FGI_StockForm.recId |
| stockFormId | string | 是 | - | 入仓明细id |
| stockFormJobId | int? | 是 | - | 生产入库生产型号关联表，对应FGI_StockFormJob.recId |
| ttype | string | 是 | - | CS 标准箱，CM尾箱 |
| version | int? | 是 | - | - |
| cartonsId | int? | 是 | - | 多级包装id |
| jobId | int? | 是 | - | 生产型号表，对应s_job.recId |
| plantsId | int? | 是 | - | 工厂 |
| rack | string | 是 | - | 储区 |
| dateCode | string | 是 | - | 周期码 |
| xout | string | 是 | - | xout数量 |
| ifUnbox | bool? | 是 | - | 是否拆箱 |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| serialNumber | int? | 是 | - | 箱序号 |
| printNum | int? | 是 | - | 打印次数 |
| ifPrint | bool? | 是 | - | 是否打印 |
| ifCheck | bool? | 是 | - | 是否盘点中 |
| checkUserId | int? | 是 | - | 盘点人 |
| checkTime | DateTime? | 是 | - | 盘点时间 |
| warehouseId | int? | 是 | - | 仓库id |
| printNum2 | int? | 是 | - | 多级包装打印次数 |
| custPO | string | 是 | - | 客户合同号 |
| cartonGrossWeight | decimal? | 是 | - | 毛总 |
| cartonNetWeight | decimal? | 是 | - | 净重 |
| woId | string | 是 | - | 工单id |
| caseId | string | 是 | - | 关联FGI_CaseBox表cartonsNumberId |
- **关联关系**：
  - FGI_CartonsNumber.cartonsNumberService = FGI_StockForm.recId
  - FGI_CartonsNumber.stockFormJobId = FGI_StockFormJob.recId
  - FGI_CartonsNumber.jobId = s_job.recId
  - FGI_CartonsNumber.salesPartId = S_SalesParts.recId

---

#### 153 成品库存 ( FGI_Inventory )
- **业务含义**：成品库存
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| actualCost | decimal? | 是 | - | 成本；本币单价 |
| batchNumber | string | 是 | - | 批次号，对应FGI_StockFormItem.batchNumber |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| dateCode | string | 是 | - | 周期码 |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| poItemId | int? | 是 | - | 外协采购明细，对应S_OS_POItem.recId |
| qtyOfArray | int? | 是 | - | 交货板数 |
| qtyOfBag | int? | 是 | - | 包数 |
| qtyOfBagPerCarton | int? | 是 | - | 每箱包数 |
| qtyOfCarton | int? | 是 | - | 箱数 |
| qtyOfPerBag | int? | 是 | - | 每包数量 |
| qtyOfSet | int? | 是 | - | 单元/交货板数 |
| qtyOfUnit | int? | 是 | - | 库存数 |
| qtyOfXOUT | int? | 是 | - | 交叉板数 |
| qtyofArray_Alloc | int? | 是 | - | 已分配交货板数 |
| qtyofUnit_Alloc | int? | 是 | - | 已分配单元数 |
| stdCost | decimal? | 是 | - | 标准成本 |
| stockDate | DateTime? | 是 | - | 入库日期 |
| stockFormItemId | int? | 是 | - | 入库明细，对应FGI_stockFormItem.recId |
| stockType | string | 是 | - | 入库类型；Direct: 直接入库
Production: 生产入库
Return: 退货入库
Outsource: 外包入库 |
| version | int? | 是 | - | 记录版本 |
| jobId | int? | 是 | - | 生产编号，对应S_Job.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| contractItemId | int? | 是 | - | 销售订单，对应S_ContractItem（不包括外协订单入库）.recId |
| fgiScrapSheetItemId | int? | 是 | - | 报废明细，对应FGI_ScrapSheetItem.recId |
| soNumber | string | 是 | - | 销售订单号 |
| qtyTransit | int? | 是 | - | - |
| qtyIqcTransit | int? | 是 | - | - |
| fiscalPeriodId | int? | 是 | - | - |
| currencyId | int? | 是 | - | 币种 |
| calCost | decimal? | 是 | - | - |
| ifPackBag | bool? | 是 | - | - |
| qtyOfStockUnit | int? | 是 | - | 入库单元数 |
| qtyOfStockBag | int? | 是 | - | - |
| qtyOfStockArray | int? | 是 | - | 入库交货板数 |
| priceInTax | decimal? | 是 | - | 含税价格 |
| rack | string | 是 | - | - |
| fgiPropertyId | int? | 是 | - | 对应分类.recId |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| xnh_ifTransfer | int? | 是 | - | - |
| mfgPartsId | int? | 是 | - | 制造部件 |
| qtyOfPanel | int? | 是 | - | - |
| qtyOfPerCarton | int? | 是 | - | - |
| qtyStockedCarton | int? | 是 | - | - |
| actionUserId | int? | 是 | - | - |
| actionTime | DateTime? | 是 | - | - |
| actionNote | string | 是 | - | - |
| actionSourceId | string | 是 | - | - |
| lclNotes | string | 是 | - | - |
| atomonly | int? | 是 | - | - |
| frozen | bool? | 是 | - | 是否冻结 |
| taxesFlag | string | 是 | - | 保税方式 |
| taxesCode | string | 是 | - | 保税代码 |
| mfgCategory | string | 是 | - | - |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| lockFlg | int? | 是 | - | - |
| costCarrierId | int? | 是 | - | - |
| moId | int? | 是 | - | 制造订单，对应P_MO.recId |
- **关联关系**：
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

#### 154 成品出库批次号表 ( FGI_InventoryOut )
- **业务含义**：成品出库批次号表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| contractItemId | int? | 是 | - | 对应S_ContractItem.recId |
| mosoAllocId | int? | 是 | - | - |
| note | string | 是 | - | 备注 |
| qtyofArray | int? | 是 | - | 交货板数set |
| qtyofBags | int? | 是 | - | 叉板数 |
| qtyofCartons | int? | 是 | - | - |
| qtyofPCS | int? | 是 | - | PCS数 |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| fgiInventoryId | int? | 是 | - | 库存表，对应FGI_Inventory.recId |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| packingSlipItemId | int? | 是 | - | 装运明细表，对应FGI_PackingSlipItem.recId |
| fgiOutTime | DateTime? | 是 | - | - |
| EnterDate | DateTime? | 是 | (getdate()) | 建单时间 |
- **关联关系**：
  - FGI_InventoryOut.contractItemId = S_ContractItem.recId
  - FGI_InventoryOut.fgiInventoryId = FGI_Inventory.recId
  - FGI_InventoryOut.jobId = S_Job.recId
  - FGI_InventoryOut.packingSlipItemId = FGI_PackingSlipItem.recId

---

#### 155 制成品检验单 ( FGI_IQC )
- **业务含义**：制成品检验单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| batchCode | string | 是 | - | - |
| checkDate | DateTime? | 是 | - | - |
| code | string | 是 | - | 检验单号 |
| deliveryCode | string | 是 | - | 送货/送检单号 |
| enableApproval | bool? | 是 | - | - |
| ifOutPut | bool? | 是 | - | 合格入库状态 0.禁用 1.启用 |
| ifStock | bool? | 是 | - | 入库状态0.未入库   1.已入库 |
| locked | bool? | 是 | - | - |
| moId | int? | 是 | - | 制造单号，对应P_MO.recId |
| note | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| poItemId | int? | 是 | - | 外协采购单，对应S_OS_POItem.recId |
| qtyArrayDefected | int? | 是 | - | 缺陷数SET |
| qtyArrayQualified | int? | 是 | - | 交货板数SET |
| qtyArrayRecieved | int? | 是 | - | 接收数SET |
| qtyArrayReturn | int? | 是 | - | 返工数SET |
| qtyArrayReturned | int? | 是 | - | 退货数SET |
| qtyArrayScrapped | int? | 是 | - | 报废数SET |
| qtyPanelDefected | int? | 是 | - | 缺陷数PNL；返修 |
| qtyPanelQualified | int? | 是 | - | 交货板数PNL |
| qtyPanelRecieved | int? | 是 | - | 接收数PNL |
| qtyPanelReturn | int? | 是 | - | 返工数PNL |
| qtyPanelReturned | int? | 是 | - | 退货数PNL |
| qtyPanelScrapped | int? | 是 | - | 报废数PNL |
| qtyPcsDefected | int? | 是 | - | 缺陷数PCS；返修 |
| qtyPcsQualified | int? | 是 | - | 交货板数PCS |
| qtyPcsRecieved | int? | 是 | - | 接收数PCS |
| qtyPcsReturn | int? | 是 | - | 返工数PCS |
| qtyPcsReturned | int? | 是 | - | 退货数PCS |
| qtyPcsScrapped | int? | 是 | - | 报废数PCS |
| qtySample | int? | 是 | - | 抽样数PCS |
| receiveDate | DateTime? | 是 | - | 接收时间 |
| scrappedMOId | int? | 是 | - | - |
| sourceCode | string | 是 | - | 外协采购单号 |
| sourceId | int? | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | 单据状态;Valid 生效 |
| suppCustId | int? | 是 | - | - |
| testDate | DateTime? | 是 | - | 测试时间 |
| type | string | 是 | - | 类型：Outsource外协 Stock：仓库 Receipt：客诉 |
| version | int? | 是 | - | - |
| woType | string | 是 | - | 工单状态：UnWorking未加工  Working  已加工 |
| checkorId | int? | 是 | - | 检验员，对应T_User.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| soId | int? | 是 | - | - |
| orderType | string | 是 | - | - |
| soNumber | string | 是 | - | - |
| completeDate | DateTime? | 是 | - | - |
| contractItemId | int? | 是 | - | - |
| contractItemNumber | string | 是 | - | - |
- **关联关系**：
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

#### 156 FGI_IQCHistory ( FGI_IQCHistory )
- **业务含义**：ERP 系统 FGI_IQCHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| fgiiqcId | int? | 是 | - | 对应FGI_IQC.recId |
| myId | int? | 是 | - | - |
- **关联关系**：
  - FGI_IQCHistory.fgiiqcId = FGI_IQC.recId

---

#### 157 检验项目 ( FGI_IQCItem )
- **业务含义**：检验项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| inspectResult | string | 是 | - | 检验结果 |
| judgementResult | string | 是 | - | 判断结果 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| fgiiqcId | int? | 是 | - | 制成品检验单，对应FGI_IQC.recId |
| inspectItemsId | int? | 是 | - | 检验名称，对应T_InspectItems.recId |
- **关联关系**：
  - FGI_IQCItem.fgiiqcId = FGI_IQC.recId
  - FGI_IQCItem.inspectItemsId = T_InspectItems.recId

---

#### 158 检验结果表 ( FGI_IQCResult )
- **业务含义**：检验结果表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | 备注 |
| qtyofArray | int? | 是 | - | SET数 |
| qtyofPanel | int? | 是 | - | PNL数 |
| qtyofPcs | int? | 是 | - | PCS数 |
| result | string | 是 | - | 检验结果 Repair-返修 Scrapped-报废 Return-退货 Defect-缺陷 |
| version | int? | 是 | - | - |
| defectId | int? | 是 | - | 缺陷表，对应T_Defect.recId |
| fgiiqcId | int? | 是 | - | 制成品检验单，对应FGI_IQC.recId |
| processId | int? | 是 | - | 工艺表，对应T_Process.recId |
| stepsId | int? | 是 | - | 工序表，对应T_Steps.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - FGI_IQCResult.defectId = T_Defect.recId
  - FGI_IQCResult.fgiiqcId = FGI_IQC.recId
  - FGI_IQCResult.processId = T_Process.recId
  - FGI_IQCResult.stepsId = T_Steps.recId
  - FGI_IQCResult.unitId = T_Unit.recId

---

#### 159 FGI_IQCWF ( FGI_IQCWF )
- **业务含义**：ERP 系统 FGI_IQCWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| fgiiqcId | int? | 是 | - | 制成品检验单，对应FGI_IQC.recId |
| myId | int? | 是 | - | 建单人，对应T_User.recId |
- **关联关系**：
  - FGI_IQCWF.fgiiqcId = FGI_IQC.recId
  - FGI_IQCWF.myId = T_User.recId

---

#### 160 FGI_JobIssueNote ( FGI_JobIssueNote )
- **业务含义**：ERP 系统 FGI_JobIssueNote 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | - |
| entDate | DateTime? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| note | string | 是 | - | - |
| stockDate | DateTime? | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| userId | int? | 是 | - | 使用人，对应T_User.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - FGI_JobIssueNote.companyId = T_Company.recId
  - FGI_JobIssueNote.creatorId = T_User.recId
  - FGI_JobIssueNote.departmentId = T_Department.recId
  - FGI_JobIssueNote.postRoleId = T_PostRole.recId
  - FGI_JobIssueNote.userId = T_User.recId
  - FGI_JobIssueNote.warehouseId = T_Warehouse.recId

---

#### 161 FGI_JobIssueNoteItem ( FGI_JobIssueNoteItem )
- **业务含义**：ERP 系统 FGI_JobIssueNoteItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifCheck | bool? | 是 | - | - |
| note | string | 是 | - | - |
| qtyOrder | int? | 是 | - | - |
| quantity | int? | 是 | - | - |
| quantityArray | int? | 是 | - | - |
| version | int? | 是 | - | - |
| jobIssueRequestItemId | int? | 是 | - | 对应FGI_JobIssueRequestItem.recId |
| jobIssueNoteId | int? | 是 | - | 对应FGI_JobIssueNote.recId |
- **关联关系**：
  - FGI_JobIssueNoteItem.jobIssueRequestItemId = FGI_JobIssueRequestItem.recId
  - FGI_JobIssueNoteItem.jobIssueNoteId = FGI_JobIssueNote.recId

---

#### 162 FGI_JobIssueNoteItemBatch ( FGI_JobIssueNoteItemBatch )
- **业务含义**：ERP 系统 FGI_JobIssueNoteItemBatch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| contractItemId | int? | 是 | - | - |
| note | string | 是 | - | - |
| jobIssueNoteCode | string | 是 | - | - |
| quantity | int? | 是 | - | - |
| quantityArray | int? | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| fgiInventoryId | int? | 是 | - | 对应FGI_Inventory.recId |
| jobIssueNoteItemId | int? | 是 | - | 对应FGI_JobIssueNoteItem.recId |
- **关联关系**：
  - FGI_JobIssueNoteItemBatch.fgiInventoryId = FGI_Inventory.recId
  - FGI_JobIssueNoteItemBatch.jobIssueNoteItemId = FGI_JobIssueNoteItem.recId

---

#### 163 FGI_JobIssueRequest ( FGI_JobIssueRequest )
- **业务含义**：ERP 系统 FGI_JobIssueRequest 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| code | string | 是 | - | - |
| enableApproval | bool? | 是 | - | - |
| note | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| requestedDate | DateTime? | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 流程表，对应T_FlowType.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - FGI_JobIssueRequest.companyId = T_Company.recId
  - FGI_JobIssueRequest.creatorId = T_User.recId
  - FGI_JobIssueRequest.departmentId = T_Department.recId
  - FGI_JobIssueRequest.flowTypeId = T_FlowType.recId
  - FGI_JobIssueRequest.plantsId = T_Plants.recId
  - FGI_JobIssueRequest.postRoleId = T_PostRole.recId
  - FGI_JobIssueRequest.warehouseId = T_Warehouse.recId

---

#### 164 FGI_JobIssueRequestHistory ( FGI_JobIssueRequestHistory )
- **业务含义**：ERP 系统 FGI_JobIssueRequestHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| jobIssueRequestId | int? | 是 | - | 对应FGI_JobIssueRequest.recId |
- **关联关系**：
  - FGI_JobIssueRequestHistory.myId = T_User.recId
  - FGI_JobIssueRequestHistory.jobIssueRequestId = FGI_JobIssueRequest.recId

---

#### 165 FGI_JobIssueRequestItem ( FGI_JobIssueRequestItem )
- **业务含义**：ERP 系统 FGI_JobIssueRequestItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| ideas | string | 是 | - | - |
| note | string | 是 | - | - |
| jobIssueNoteCode | string | 是 | - | - |
| jobIssueNoteItemId | int? | 是 | - | - |
| qtyHairBack | int? | 是 | - | - |
| qtyIssued | int? | 是 | - | - |
| quantity | int? | 是 | - | - |
| requestedDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | 对应S_Job.recId |
| fgiIssueRequestId | int? | 是 | - | 对应FGI_JobIssueRequest.recId |
| stepsId | int? | 是 | - | 对应T_Steps.recId |
- **关联关系**：
  - FGI_JobIssueRequestItem.jobId = S_Job.recId
  - FGI_JobIssueRequestItem.fgiIssueRequestId = FGI_JobIssueRequest.recId
  - FGI_JobIssueRequestItem.stepsId = T_Steps.recId

---

#### 166 FGI_JobIssueRequestWF ( FGI_JobIssueRequestWF )
- **业务含义**：ERP 系统 FGI_JobIssueRequestWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | - |
| jobIssueRequestId | int? | 是 | - | - |
- **关联关系**：无

---

#### 167 成品月结 ( FGI_MonthlyClosing )
- **业务含义**：成品月结
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| monthlyClosingDate | DateTime? | 是 | - | 月结日期 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 状态;Close  关闭  Active  活动 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_WareHouse.recId |
- **关联关系**：
  - FGI_MonthlyClosing.creatorId = T_User.recId
  - FGI_MonthlyClosing.fiscalPeriodId = T_FiscalPeriod.recId
  - FGI_MonthlyClosing.plantsId = T_Plants.recId
  - FGI_MonthlyClosing.companyId = T_Company.recId
  - FGI_MonthlyClosing.warehouseId = T_WareHouse.recId

---

#### 168 成品月结明细 ( FGI_MonthlyClosingItem )
- **业务含义**：成品月结明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qty_CheckIn | int? | 是 | - | 盘盈 |
| qty_CheckOut | int? | 是 | - | 盘亏 |
| qty_On_hand | int? | 是 | - | 当前数量 |
| qty_Returned | int? | 是 | - | 退货数量 |
| qty_Scrapped | int? | 是 | - | 报废数 |
| qty_Shipment | int? | 是 | - | 出货数量 |
| qty_Stocked | int? | 是 | - | 入库数量 |
| qty_begin | int? | 是 | - | 期初数 |
| qty_end | int? | 是 | - | 期末数 |
| qty_picking | int? | 是 | - | 领料数量 |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | 对应S_Job.recId |
| monthlyClosingId | int? | 是 | - | 不使用该字段，对应FGI_MonthlyClosing.recId |
| fgiMonthlyClosingId | int? | 是 | - | 主表，对应FGI_MonthlyClosing.recId |
| qty_TransferIn | int? | 是 | ((0)) | 转入数量 |
| qty_TransferOut | int? | 是 | ((0)) | 转出数量 |
| qty_IQCOut | int? | 是 | ((0)) | 仓检出库数量 |
| qty_TransferSOIn | string | 是 | - | 订单代管转入 |
| qty_TransferSOOut | string | 是 | - | 订单代管转出 |
| cost_On_hand | string | 是 | - | 在库成本 |
| cost_Stocked | string | 是 | - | 入库金额(批次单价) |
| cost_Shipment | string | 是 | - | 出库金额(批次单价) |
| cost_Returned | string | 是 | - | 客户退货接收金额 |
| cost_CheckIn | string | 是 | - | 盘盈金额 |
| cost_CheckOut | string | 是 | - | 盘亏金额 |
| cost_picking | string | 是 | - | 成品领料金额 |
| cost_Scrapped | string | 是 | - | 检验报废金额 |
| cost_TransferIn | string | 是 | - | 仓库转入金额 |
| cost_TransferOut | string | 是 | - | 仓库转出金额 |
| cost_IQCOut | string | 是 | - | IQC送检金额 |
| cost_TransferSOIn | string | 是 | - | 订单代管转入金额 |
| cost_TransferSOOut | string | 是 | - | 订单代管转出金额 |
| cost_begin | string | 是 | - | 期初金额 |
| cost_end | string | 是 | - | 期末金额 |
| cost_On_hand2 | string | 是 | - | 当前金额 |
| cost_Stocked2 | string | 是 | - | 入库金额 |
| cost_Shipment2 | string | 是 | - | 出货金额 |
| cost_Returned2 | string | 是 | - | 客诉退货金额 |
| cost_CheckIn2 | string | 是 | - | 盘盈金额 |
| cost_CheckOut2 | string | 是 | - | 盘亏金额 |
| cost_picking2 | string | 是 | - | 领用金额 |
| cost_Scrapped2 | string | 是 | - | 报废金额 |
| cost_TransferIn2 | string | 是 | - | 转入金额 |
| cost_TransferOut2 | string | 是 | - | 转出金额 |
| cost_IQCOut2 | string | 是 | - | 仓检出库金额 |
| cost_TransferSOIn2 | string | 是 | - | 销售转入金额 |
| cost_TransferSOOut2 | string | 是 | - | 销售转出金额 |
| cost_begin2 | string | 是 | - | 期初金额 |
| cost_end2 | string | 是 | - | 期末金额 |
| averageCostByMonth_Current | string | 是 | - | 期末单位成本 |
| qty_returnIn | string | 是 | - | 退货入库数量 |
| qty_returnReworked | string | 是 | - | 退货返工数量 |
| qty_returnScrapped | string | 是 | - | 退货报废数量 |
| cost_returnIn2 | string | 是 | - | 退货入库金额 |
| cost_returnReworked2 | string | 是 | - | 退货返工金额 |
| cost_returnScrapped2 | string | 是 | - | 退货报废金额 |
| qty_stockReworked | string | 是 | - | 仓库返修 发放数 |
| cost_stockReworked | string | 是 | - | 仓库返修 发放金额 |
| qtyJsInit | string | 是 | - | 寄售出货期初 |
| qtyJsShipment | string | 是 | - | 寄售出货 |
| qtyJsDz | string | 是 | - | 寄售对账 |
| qtyJsBack | string | 是 | - | 寄售转回 |
| qtyJsReturn | string | 是 | - | 寄售退货 |
| costJsShipment | string | 是 | - | 寄售出货金额 |
| costJsDz | string | 是 | - | 寄售对账金额 |
| costJsBack | string | 是 | - | 寄售转回金额 |
| costJsReturn | string | 是 | - | 寄售退货金额 |
| qty_OsStocked | string | 是 | - | 外协入库数量 |
| cost_OsStocked | string | 是 | - | 外协入库金额 |
| cost_OsStocked2 | string | 是 | - | 外协入库金额不含税 |
| qtyJsEnd | string | 是 | - | 寄售期末 |
- **关联关系**：
  - FGI_MonthlyClosingItem.jobId = S_Job.recId
  - FGI_MonthlyClosingItem.monthlyClosingId = FGI_MonthlyClosing.recId
  - FGI_MonthlyClosingItem.fgiMonthlyClosingId = FGI_MonthlyClosing.recId

---

#### 169 成品装箱单 ( FGI_PackingItem )
- **业务含义**：成品装箱单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cycleNumber | string | 是 | - | 周期 |
| endBoxes | int? | 是 | - | - |
| grossWeight | decimal? | 是 | - | - |
| netWeight | decimal? | 是 | - | - |
| note | string | 是 | - | - |
| packingCartonSize | string | 是 | - | - |
| packingSlipItemId | int? | 是 | - | 空值null，对应FGI_PackingSlipItem.recId |
| panelNumber | string | 是 | - | - |
| qty | int? | 是 | - | 总数量 |
| qtyBoxes | int? | 是 | - | 箱包数 |
| qtyDefective | int? | 是 | - | 叉板数 |
| qtyPerBoxes | int? | 是 | - | 每箱数量 |
| qtyQuality | int? | 是 | - | 正品数 |
| startBoxes | int? | 是 | - | 起始箱 |
| unitWeight | decimal? | 是 | - | 重量（单块板重） |
| version | int? | 是 | - | - |
| salesPartId | string | 是 | - | 销售部件表 |
| packingSlipId | string | 是 | - | 成品出货，对应FGI_PackingSlip.recId |
| cartonsId | string | 是 | - | 纸箱定义，对应S_Cartons.recId |
- **关联关系**：
  - FGI_PackingItem.packingSlipItemId = FGI_PackingSlipItem.recId
  - FGI_PackingItem.packingSlipId = FGI_PackingSlip.recId
  - FGI_PackingItem.cartonsId = S_Cartons.recId

---

#### 170 成品出货 ( FGI_PackingSlip )
- **业务含义**：成品出货
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| confirmedDate | DateTime? | 是 | - | 出库日期 |
| consignmentFlag | int? | 是 | - | - |
| contact | string | 是 | - | 联系人 |
| contactEmail | string | 是 | - | 联系邮件 |
| contactPhone | string | 是 | - | 联系电话 |
| cust_Confirmed | bool? | 是 | - | 箱数 |
| cust_Ref | string | 是 | - | 外部参考号 |
| enableApproval | bool? | 是 | - | - |
| enterDate | DateTime? | 是 | - | - |
| exchangeRate | decimal? | 是 | - | 汇率 |
| freight | decimal? | 是 | - | - |
| grossWeight | decimal? | 是 | - | 毛重 |
| ifassign | bool? | 是 | - | 是否已做库存分配：0未做 1已做 |
| internal_Ref | string | 是 | - | 内部参考号 |
| netWeight | decimal? | 是 | - | 净重 |
| note | string | 是 | - | 备注（运单号） |
| originalStatus | string | 是 | - | - |
| packingCartonSize | string | 是 | - | - |
| packingSlip_Numer | string | 是 | - | 送货单号 |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| printedDate | DateTime? | 是 | - | - |
| printedFlg | bool? | 是 | - | - |
| qtyOfCartons | int? | 是 | - | - |
| shipFlg | int? | 是 | - | 出库状态 0：待出库   1：待装运   2：已装运 |
| shipPlanDate | DateTime? | 是 | - | 计划出货日期 |
| shipType | int? | 是 | - | - |
| shipingNotes_Numer | string | 是 | - | 出库单号 |
| shippedDate | DateTime? | 是 | - | 出货日期（装运日期） |
| shippingAddress | string | 是 | - | 送货地址 |
| shippingCharge | string | 是 | - | 参考运费 |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | Action :有效   Cancel :取消         Valid：生效 |
| type | string | 是 | - | 类型:PackingList 装箱单  DeliveryPlan:出货计划 CTransferWarehouse：寄售转仓 |
| version | int? | 是 | - | - |
| assignUserId | int? | 是 | - | 库存指派员，对应T_User.recId |
| salesRepId | int? | 是 | - | 业务员，对应S_BusinessMan.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| confirmedUserId | int? | 是 | - | 出库人，对应T_User.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 币别，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| shippingAddressId | int? | 是 | - | 客户地址，对应S_CustomerAddress.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| fobId | int? | 是 | - | 对应T_FOB.recId |
| shipUserId | int? | 是 | - | 装运员，对应T_User.recId |
| shippingMethodId | int? | 是 | - | 运输方式，对应T_Shipping.recId |
| saleType | string | 是 | - | ForExport :一般贸易，ForDomestic：内销，Bonded：保税 |
- **关联关系**：
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

#### 171 箱包关联表 ( FGI_PackingSlipCartonsNumber )
- **业务含义**：箱包关联表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| note | string | 是 | - | - |
| packingSlipId | int? | 是 | - | 成本出货表，对应FGI_PackingSlip.recId |
| version | int? | 是 | - | - |
| cartonsNumberId | int? | 是 | - | 主表，对应FGI_CartonsNumber.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
- **关联关系**：
  - FGI_PackingSlipCartonsNumber.packingSlipId = FGI_PackingSlip.recId
  - FGI_PackingSlipCartonsNumber.cartonsNumberId = FGI_CartonsNumber.recId
  - FGI_PackingSlipCartonsNumber.salesPartId = S_SalesParts.recId

---

#### 172 FGI_PackingSlipHistory ( FGI_PackingSlipHistory )
- **业务含义**：ERP 系统 FGI_PackingSlipHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| packingSlipId | int? | 是 | - | 对应FGI_PackingSlip.recId |
- **关联关系**：
  - FGI_PackingSlipHistory.myId = T_User.recId
  - FGI_PackingSlipHistory.packingSlipId = FGI_PackingSlip.recId

---

#### 173 成品出货明细表 ( FGI_PackingSlipItem )
- **业务含义**：成品出货明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | - |
| amount_Receivables | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | - |
| approveStatus | string | 是 | - | Approved:已分配 |
| deliveryInstructionsId | int? | 是 | - | - |
| enterDate | DateTime? | 是 | - | - |
| freight | decimal? | 是 | - | 运费 |
| grossWeight | decimal? | 是 | - | 毛重 |
| ideas | string | 是 | - | - |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| netWeight | decimal? | 是 | - | 净重 |
| note | string | 是 | - | 备注 |
| packingSlipItemId | int? | 是 | - | 对应FGI_PackingSlipItem.recId |
| qtyBoxes | int? | 是 | - | - |
| qtyDefective | int? | 是 | - | 缺陷数量 |
| qtyFreeAssigned | int? | 是 | - | 赠品出数 |
| qtyQuality | int? | 是 | - | - |
| qty_Invoiced | int? | 是 | - | 发票数量 |
| qty_Receivables | int? | 是 | - | - |
| qty_Reconciled | int? | 是 | - | - |
| qtyofArrayAssigned | int? | 是 | - | 出板set数 |
| qtyofBags | int? | 是 | - | 箱数 |
| qtyofCartons | int? | 是 | - | - |
| qtyofConsumed | int? | 是 | - | - |
| qtyofFree | int? | 是 | - | - |
| qtyofOrdered | int? | 是 | - | - |
| qtyofPCSAssigned | int? | 是 | - | 出货数 |
| qtyofShipFree | int? | 是 | - | 赠品计划出数 |
| qtyofShipOrdered | int? | 是 | - | 订单计划出数 |
| qtyofTotal | int? | 是 | - | - |
| recievedFlg | int? | 是 | - | - |
| rootId | int? | 是 | - | - |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 销售订单合同明细，对应S_ContractItem.recId |
| contractSOId | int? | 是 | - | 销售单，对应S_ContractSO.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| orderUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| packingSlipId | int? | 是 | - | 主表，对应FGI_PackingSlip.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| qtyPCSReturn | int? | 是 | ((0)) | 退回数量 |
| qtyArrayReturn | int? | 是 | ((0)) | - |
| qtyPCSReturnReceipt | int? | 是 | - | - |
| ifReturn | bool? | 是 | - | - |
| qty_undo | int? | 是 | - | 撤销出货数量 |
| shipmentRevokeId | int? | 是 | - | - |
- **关联关系**：
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

#### 174 FGI_PackingSlipWF ( FGI_PackingSlipWF )
- **业务含义**：ERP 系统 FGI_PackingSlipWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | - |
| packingSlipId | int? | 是 | - | - |
- **关联关系**：无

---

#### 175 箱包，包明细表 ( FGI_PackNumber )
- **业务含义**：箱包，包明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| code | string | 是 | - | 包号 |
| fgiInventoryId | int? | 是 | - | 成品库存，对应FGI_Inventory.recId |
| note | string | 是 | - | 备注 |
| qtyQualified | int? | 是 | - | 包PCS数 |
| qtyScrapped | int? | 是 | - | 报废数 |
| status | string | 是 | - | 入库状态 |
| version | int? | 是 | - | - |
| cartonsNumberId | int? | 是 | - | 装箱单编号表，对应FGI_CartonsNumber.recId |
| stockFormItemId | int? | 是 | - | 生产入库明细表，对应FGI_StockFormItem.recId |
| dateCode | string | 是 | - | 周期码 |
| xout | string | 是 | - | xout数量 |
| ifUnbox | bool? | 是 | - | - |
| ttype | string | 是 | - | 入仓类型 |
| qtyOfArrayPerBag | int? | 是 | - | 每包SET数 |
| serialNumber | int? | 是 | - | 按工单小包序号 |
| printNum | int? | 是 | - | 打印次数 |
| ifPrint | bool? | 是 | - | 是否打印 |
| ifCheck | bool? | 是 | - | 是否盘点中 |
| checkUserId | int? | 是 | - | 盘点人 |
| checkTime | DateTime? | 是 | - | 盘点状态 |
| printNum2 | int? | 是 | - | 外包打印次数 |
| createUserId | string | 是 | - | 创建人 |
| createTime | string | 是 | - | 创建时间 |
| custPO | string | 是 | - | 客户PO |
| woId | string | 是 | - | 工单id |
| jobId | string | 是 | - | 生产部件id |
| plantsId | string | 是 | - | 工厂 |
| splitPackage | string | 是 | - | 是否拆包 |
| itemNO | string | 是 | - | 序号 |
| mfgDate | string | 是 | - | 生产日期 |
| expiryDate | string | 是 | - | 过期日期 |
| note2 | string | 是 | - | 备注2 |
| note3 | string | 是 | - | 备注3 |
| note4 | string | 是 | - | 备注4 |
| packGrossWeight | string | 是 | - | 毛总 |
| packNetWeight | string | 是 | - | 净重 |
| xPositio | string | 是 | - | x板位置 |
| customerNote1 | string | 是 | - | 客户备注1 |
| customerNote2 | string | 是 | - | 客户备注2 |
| customerNote3 | string | 是 | - | 客户备注3 |
| customerNote4 | string | 是 | - | 客户备注4 |
| customerNote5 | string | 是 | - | 客户备注5 |
| customerNote6 | string | 是 | - | 客户备注6 |
| contractSOId | string | 是 | - | 销售订单id(注意是关联contractItemId) |
| outsideNumber | string | 是 | - | 外箱单号 |
| stockFormJobId | string | 是 | - | 入仓明细id |
- **关联关系**：
  - FGI_PackNumber.fgiInventoryId = FGI_Inventory.recId
  - FGI_PackNumber.cartonsNumberId = FGI_CartonsNumber.recId
  - FGI_PackNumber.stockFormItemId = FGI_StockFormItem.recId

---

#### 176 卡板表 ( FGI_PalletNumber )
- **业务含义**：卡板表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 主键 |
| code | string | 是 | - | 卡板号 |
| status | string | 是 | - | 状态；OutStock：未出库，OutStocked：已出库，Scrap：作废 |
| plantsId | string | 是 | - | 工厂，对应T_Plants.recId |
| jobId | string | 是 | - | 生产编号，对应S_Job.recId |
| qtyQualified | string | 是 | - | 卡数量(PCS) |
| netWeight | string | 是 | - | 卡净重 |
| grossWeight | string | 是 | - | 卡毛重 |
| totalNetWeight | string | 是 | - | 整卡净重 |
| totalGrossWeight | string | 是 | - | 整卡毛重 |
| printNum | string | 是 | - | 打印次数 |
| note | string | 是 | - | 备注 |
| noteOne | string | 是 | - | 备注1 |
| noteTwo | string | 是 | - | 备注2 |
| noteThree | string | 是 | - | 备注3 |
| noteFour | string | 是 | - | 备注4 |
| noteFive | string | 是 | - | 备注5 |
| noteSix | string | 是 | - | 备注6 |
| creatorId | string | 是 | - | 创建人，对应T_User.recId |
| creatorTime | string | 是 | - | 创建时间 |
| modifiedById | string | 是 | - | 修改人，对应T_User.recId |
| modifiedTime | string | 是 | - | 修改时间 |
| version | string | 是 | - | 版本 |
| qtyArray | string | 是 | - | 卡数量（SET） |
- **关联关系**：
  - FGI_PalletNumber.plantsId = T_Plants.recId
  - FGI_PalletNumber.jobId = S_Job.recId
  - FGI_PalletNumber.creatorId = T_User.recId
  - FGI_PalletNumber.modifiedById = T_User.recId

---

#### 177 制成品接收单 ( FGI_Receipt )
- **业务含义**：制成品接收单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 接收单号 |
| customsCode | string | 是 | - | 海关单号 |
| deliveryCode | string | 是 | - | 送货单号 |
| entDate | DateTime? | 是 | - | 创建日期 |
| locked | bool? | 是 | - | - |
| note | string | 是 | - | - |
| receiveDate | DateTime? | 是 | - | 收货日期 |
| sourceCode | string | 是 | - | 供应商/客户  代码 |
| sourceId | int? | 是 | - | 供应商/客户表，对应M_Suppliers/S_Customer.recId |
| type | string | 是 | - | Customer：客户 Outsourcing：供应商 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| EnterDate | DateTime? | 是 | (getdate()) | 接收时间 |
- **关联关系**：
  - FGI_Receipt.sourceId = M_Suppliers/S_Customer.recId
  - FGI_Receipt.creatorId = T_User.recId
  - FGI_Receipt.plantsId = T_Plants.recId
  - FGI_Receipt.postRoleId = T_PostRole.recId

---

#### 178 制成品接收单明细 ( FGI_ReceiptItem )
- **业务含义**：制成品接收单明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | 发票金额 |
| amount_Reconciled | decimal? | 是 | - | - |
| contractItemNumber | string | 是 | - | 合同号 |
| dateDiffVal | int? | 是 | - | - |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| ifInspection | bool? | 是 | - | 是否要检查 0否 1是 |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| note | string | 是 | - | 备注 |
| orderCode | string | 是 | - | 接收单号（客诉号，外协采购单号） |
| orderDate | DateTime? | 是 | - | 外协采购时间 |
| orderId | int? | 是 | - | 外协采购ID，对应S_OS_POItem.recId |
| orderType | string | 是 | - | Outsourcing：供应商，Exchange客户 |
| priceInTax | decimal? | 是 | - | 含税单价 |
| qtyArrayDefected | int? | 是 | - | - |
| qtyArrayInInspection | int? | 是 | - | 检查SET数 |
| qtyArrayInspected | int? | 是 | - | 已检查SET数 |
| qtyArrayQualified | int? | 是 | - | - |
| qtyArrayRecieved | int? | 是 | - | - |
| qtyArrayReturn | int? | 是 | - | - |
| qtyArrayReturned | int? | 是 | - | - |
| qtyArrayReworked | int? | 是 | - | - |
| qtyArrayScrapped | int? | 是 | - | - |
| qtyArrayStocked | int? | 是 | - | 接收交货板SET |
| qtyArrayToStock | int? | 是 | - | 接收交货板SET |
| qtyPanelDefected | int? | 是 | - | - |
| qtyPanelInInspection | int? | 是 | - | 检查PNL数 |
| qtyPanelInspected | int? | 是 | - | - |
| qtyPanelQualified | int? | 是 | - | - |
| qtyPanelRecieved | int? | 是 | - | 接收生产板PNL |
| qtyPanelReturn | int? | 是 | - | 退货数量pnl |
| qtyPanelReturned | int? | 是 | - | 已经退货了的数量pnl |
| qtyPanelReworked | int? | 是 | - | - |
| qtyPanelScrapped | int? | 是 | - | - |
| qtyPanelStocked | int? | 是 | - | 已入库 |
| qtyPanelToStock | int? | 是 | - | 待入库pnl数 |
| qtyPcsDefected | int? | 是 | - | - |
| qtyPcsInInspection | int? | 是 | - | - |
| qtyPcsInspected | int? | 是 | - | 已检验PCS数量 |
| qtyPcsQualified | int? | 是 | - | - |
| qtyPcsRecieved | int? | 是 | - | 接受PCS数量 |
| qtyPcsReturn | int? | 是 | - | - |
| qtyPcsReturned | int? | 是 | - | - |
| qtyPcsReworked | int? | 是 | - | - |
| qtyPcsScrapped | int? | 是 | - | 已报废PCS数量 |
| qtyPcsStocked | int? | 是 | - | 已入库PCS数量 |
| qtyPcsToStock | int? | 是 | - | 合格可以入库PCS数量 |
| qty_Invoiced | int? | 是 | - | - |
| qty_Reconciled | int? | 是 | - | 接收数 |
| status | string | 是 | - | 状态:Active:活动（未执行IQC检验步骤）;
Received：FGI_Receipt.type='Customer'时生产线已接收
IQC:已检验;
Storage:已入库 |
| suppBatchNumber | string | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| woType | string | 是 | - | 加工状态：Working：已加工  UnWorking：未加工 |
| fgiReceiptId | int? | 是 | - | 主表，对应FGI_Receipt.recId |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - FGI_ReceiptItem.orderId = S_OS_POItem.recId
  - FGI_ReceiptItem.fgiReceiptId = FGI_Receipt.recId
  - FGI_ReceiptItem.jobId = S_Job.recId
  - FGI_ReceiptItem.postRoleId = T_PostRole.recId
  - FGI_ReceiptItem.salesPartId = S_SalesParts.recId
  - FGI_ReceiptItem.unitId = T_Unit.recId

---

#### 179 成品退货表 ( FGI_ReturnOrder )
- **业务含义**：成品退货表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 退货单号 |
| entDate | DateTime? | 是 | - | 退货时间 |
| lastModifyDate | DateTime? | 是 | - | 最后修改时间 |
| locked | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| note | string | 是 | - | 备注 |
| returnDate | DateTime? | 是 | - | 退货时间 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - FGI_ReturnOrder.creatorId = T_User.recId
  - FGI_ReturnOrder.plantsId = T_Plants.recId
  - FGI_ReturnOrder.postRoleId = T_PostRole.recId
  - FGI_ReturnOrder.suppliersId = M_Suppliers.recId

---

#### 180 成品退货明细表 ( FGI_ReturnOrderItem )
- **业务含义**：成品退货明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| debitMemoItemId | int? | 是 | - | - |
| note | string | 是 | - | - |
| qtyArray | int? | 是 | - | SET |
| qtyPanel | int? | 是 | - | PNL |
| qtyPcs | int? | 是 | - | PCS |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| fgiReturnOrderId | int? | 是 | - | 主表，对应FGI_ReturnOrder.recId |
| fgiiqcId | int? | 是 | - | 成品检验表，对应FGI_IQC.recId |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - FGI_ReturnOrderItem.fgiReturnOrderId = FGI_ReturnOrder.recId
  - FGI_ReturnOrderItem.fgiiqcId = FGI_IQC.recId
  - FGI_ReturnOrderItem.jobId = S_Job.recId
  - FGI_ReturnOrderItem.salesPartId = S_SalesParts.recId
  - FGI_ReturnOrderItem.unitId = T_Unit.recId

---

#### 181 成品报废 ( FGI_ScrapSheet )
- **业务含义**：成品报废
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checkDate | DateTime? | 是 | - | 审核日期 |
| checkNote | string | 是 | - | 审核备注 |
| code | string | 是 | - | 调拨单号 |
| createDate | DateTime? | 是 | - | 建单日期 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 状态：Checked 核准 TOChecked 待核准 |
| version | int? | 是 | - | - |
| checkorId | int? | 是 | - | 审核人员，对应T_User.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - FGI_ScrapSheet.checkorId = T_User.recId
  - FGI_ScrapSheet.creatorId = T_User.recId
  - FGI_ScrapSheet.warehouseId = T_Warehouse.recId

---

#### 182 成品报废明细 ( FGI_ScrapSheetItem )
- **业务含义**：成品报废明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | - |
| qtyOfArray | int? | 是 | - | 报废SET |
| qtyOfUnit | int? | 是 | - | 报废PCS |
| version | int? | 是 | - | - |
| fgiInventoryId | int? | 是 | - | 成品库存，对应FGI_Inventory.recId |
| fgiScrapSheetId | int? | 是 | - | 主表，对应FGI_ScrapSheet.recId |
| qtyOfUnit_Alloc | int? | 是 | - | 叉板数 |
| qtyOfArray_Alloc | int? | 是 | - | 交货板数 |
- **关联关系**：
  - FGI_ScrapSheetItem.fgiInventoryId = FGI_Inventory.recId
  - FGI_ScrapSheetItem.fgiScrapSheetId = FGI_ScrapSheet.recId

---

#### 183 成品入库 ( FGI_StockForm )
- **业务含义**：成品入库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 184 成品入库明细 ( FGI_StockFormItem )
- **业务含义**：成品入库明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| batchNumber | string | 是 | - | 批次号 |
| dateCode | string | 是 | - | 周期码 |
| ifCartonsStock | bool? | 是 | - | 是否按箱数入库 |
| itemId | string | 是 | - | - |
| mfgDate | DateTime? | 是 | - | 制造日期 |
| note | string | 是 | - | 备注 |
| orderId | int? | 是 | - | 成品接收明细，对应FGI_ReceiptItem.recId |
| orderType | string | 是 | - | 成品接收类型；Outsourcing: 外协
Return: 退货 |
| positionXOUT | string | 是 | - | 叉板位置 |
| qtyOfArray | int? | 是 | - | 交货板数 |
| qtyOfBag | int? | 是 | - | 包数 |
| qtyOfBagPerCarton | int? | 是 | - | 每箱包数 |
| qtyOfCarton | int? | 是 | - | 箱数 |
| qtyOfPerBag | int? | 是 | - | 每包数量 |
| qtyOfSet | int? | 是 | - | SET数 |
| qtyOfUnit | int? | 是 | - | 单元数 |
| qtyOfXOUT | int? | 是 | - | 叉板数 |
| qtyStockedBag | int? | 是 | - | 包数 |
| qtyStockedCarton | int? | 是 | - | 箱数 |
| qtyStockedOfArray | int? | 是 | - | 入库交货板数 |
| qtyStockedOfUnit | int? | 是 | - | 入库单元数 |
| stockDate | DateTime? | 是 | - | 入库日期 |
| version | int? | 是 | - | 记录版本 |
| cartonsId | int? | 是 | - | 纸箱，对应S_Cartons.recId |
| jobId | int? | 是 | - | 生产编号，对应S_Job.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| stockFormId | int? | 是 | - | 成品入库，对应FGI_StockForm.recId |
| contractSOId | int? | 是 | - | 销售订单，对应S_ContractSO.recId |
| ref_recId | int? | 是 | - | - |
| moId | int? | 是 | - | 制造订单，对应P_MO.recId |
| actualCost | decimal? | 是 | - | - |
| ab | string | 是 | - | AB板 |
| qtyOfPanel | int? | 是 | - | - |
| stockFormJobId | int? | 是 | - | - |
| ttype | string | 是 | - | 类型 |
| qtytotal | int? | 是 | - | 实际板数；单元数 - 叉板数 |
| qtyDefective | int? | 是 | - | 叉板数 |
| fgiInventoryId | int? | 是 | - | 成品库存 |
| ifMixXOutPack | bool? | 是 | - | - |
| rack | string | 是 | - | - |
| fgiPropertyId | int? | 是 | - | - |
| mfgPartsId | int? | 是 | - | 制造部件 |
| qtyOfPerCarton | int? | 是 | - | - |
| hasDeduction | bool? | 是 | - | - |
| woId | int? | 是 | - | 工单 |
| iqcInTime | DateTime? | 是 | - | - |
| iqcPanels | int? | 是 | - | - |
| expiryDate | DateTime? | 是 | - | 过期日期 |
| fgiIqcId | int? | 是 | - | 成品检验单 |
| note2 | string | 是 | - | - |
| note3 | string | 是 | - | - |
| note4 | string | 是 | - | - |
| packGrossWeight | decimal? | 是 | - | 包毛重 |
| packNetWeight | decimal? | 是 | - | 包净重 |
| cartonGrossWeight | decimal? | 是 | - | 箱毛重 |
| cartonNetWeight | decimal? | 是 | - | 箱净重 |
- **关联关系**：
  - FGI_StockFormItem.orderId = FGI_ReceiptItem.recId
  - FGI_StockFormItem.cartonsId = S_Cartons.recId
  - FGI_StockFormItem.jobId = S_Job.recId
  - FGI_StockFormItem.locationId = T_Location.recId
  - FGI_StockFormItem.salesPartId = S_SalesParts.recId
  - FGI_StockFormItem.stockFormId = FGI_StockForm.recId
  - FGI_StockFormItem.contractSOId = S_ContractSO.recId
  - FGI_StockFormItem.moId = P_MO.recId

---

#### 185 生产入库 ( FGI_StockFormItemWO )
- **业务含义**：生产入库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| note | string | 是 | - | 备注 |
| qtyOfArray | int? | 是 | - | 交货板数 |
| qtyOfPCS | int? | 是 | - | 单元数 |
| stockFormItemId | int? | 是 | - | 成品入库，对应FGI_StockFormItem.recId |
| version | int? | 是 | - | 记录版本 |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| outPutId | int? | 是 | - | 过数流转，对应P_OutPut.recId |
| qtyOfPanel | int? | 是 | - | 生产板数 |
- **关联关系**：
  - FGI_StockFormItemWO.stockFormItemId = FGI_StockFormItem.recId
  - FGI_StockFormItemWO.woId = P_WO.recId
  - FGI_StockFormItemWO.outPutId = P_OutPut.recId

---

#### 186 生产入库型号关联表 ( FGI_StockFormJob )
- **业务含义**：生产入库型号关联表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| note | string | 是 | - | 备注 |
| qtyBag | int? | 是 | - | 包数 |
| qtyDefective | int? | 是 | - | 缺陷数量 |
| qtyOfArrayPerBag | int? | 是 | - | 每包set数 |
| qtyOfBagPerCarton | int? | 是 | - | 每箱包数 |
| qtyPcs | int? | 是 | - | - |
| qtyQuality | int? | 是 | - | - |
| qtyStockBag | int? | 是 | - | 入仓包数量 |
| qtyStockCarton | int? | 是 | - | 入仓箱数量 |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | 生产编号id |
| stockFormId | int? | 是 | - | 生产入库，对应FGI_StockForm.recId |
| qtyCarton | int? | 是 | - | - |
| printNum | int? | 是 | - | 打印次数 |
| ifPrint | bool? | 是 | - | 是否打印 |
| printNum2 | int? | 是 | - | - |
| custPO | string | 是 | - | 客户PO |
- **关联关系**：
  - FGI_StockFormJob.stockFormId = FGI_StockForm.recId

---

#### 187 成品转仓表 ( FGI_Transfer )
- **业务含义**：成品转仓表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 调拨单号 |
| createDate | DateTime? | 是 | - | 建单时间 |
| note | string | 是 | - | 备注 |
| receiveDate | DateTime? | 是 | - | 转仓时间 |
| status | string | 是 | - | Received：已接收   TOReceive：待接收 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| destWarehouseId | int? | 是 | - | 目的仓库，对应T_Warehouse.recId |
| origWarehouseId | int? | 是 | - | 原仓库，对应T_Warehouse.recId |
| receiveId | int? | 是 | - | 接收人，对应T_User.recId |
- **关联关系**：
  - FGI_Transfer.creatorId = T_User.recId
  - FGI_Transfer.destWarehouseId = T_Warehouse.recId
  - FGI_Transfer.origWarehouseId = T_Warehouse.recId
  - FGI_Transfer.receiveId = T_User.recId

---

#### 188 成品转仓明细表 ( FGI_TransferItem )
- **业务含义**：成品转仓明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| desInventoryId | int? | 是 | - | 目的库存表，对应FGI_Inventory.recId |
| note | string | 是 | - | 备注 |
| qtyOfArray | int? | 是 | - | SET |
| qtyOfUnit | int? | 是 | - | PCS |
| version | int? | 是 | - | - |
| locationId | int? | 是 | - | 储区表，对应T_Location.recId |
| oriInventoryId | int? | 是 | - | 原库存表，对应FGI_Inventory.recId |
| transferId | int? | 是 | - | 主表，对应FGI_Transfer.recId |
| qtyOfUnit_Alloc | int? | 是 | - | 叉板数PCS |
| qtyOfArray_Alloc | int? | 是 | - | 叉板数SET |
- **关联关系**：
  - FGI_TransferItem.desInventoryId = FGI_Inventory.recId
  - FGI_TransferItem.locationId = T_Location.recId
  - FGI_TransferItem.oriInventoryId = FGI_Inventory.recId
  - FGI_TransferItem.transferId = FGI_Transfer.recId

---

### 2.4 工程模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 189 成德区分参数展示主表 ( E_BoardTypeParameterSettings )
- **业务含义**：成德区分参数展示主表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 190 部件成本参数 ( E_CostJobMfgPartsParams )
- **业务含义**：部件成本参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobId | int? | 是 | - | 产品型号，对应S_job.recId |
| mfgpartId | int? | 是 | - | 制造部件编号(本厂型号BOM表)，对应E_JobMfgParts.recId |
| parameterVal | decimal? | 是 | - | pcs面积（乘以系数），对应E_JobMfgParts.recId |
| seq | int? | 是 | - | 对应E_JobMfgParts.recId |
| version | int? | 是 | - | 对应E_JobMfgParts.recId |
| parameterId | int? | 是 | - | 参数表，对应S_Parameters.recId |
- **关联关系**：
  - E_CostJobMfgPartsParams.jobId = S_job.recId
  - E_CostJobMfgPartsParams.mfgpartId = E_JobMfgParts.recId
  - E_CostJobMfgPartsParams.parameterVal = E_JobMfgParts.recId
  - E_CostJobMfgPartsParams.seq = E_JobMfgParts.recId
  - E_CostJobMfgPartsParams.version = E_JobMfgParts.recId
  - E_CostJobMfgPartsParams.parameterId = S_Parameters.recId

---

#### 191 工程流程那里添加的自定义脚本表 ( E_CustomScriptSetting )
- **业务含义**：工程流程那里添加的自定义脚本表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 192 钻孔设计 ( E_DrillDetails )
- **业务含义**：钻孔设计
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| arrayHolesNum | int? | 是 | - | 出货单元数 |
| drillMarker | string | 是 | - | 标记 |
| drillSizeForOrder | decimal? | 是 | - | 钻大小顺序 |
| drill_Size | decimal? | 是 | - | 钻孔大小，成品孔径 |
| drill_Size_MM | decimal? | 是 | - | 钻孔尺寸、钻咀尺寸 |
| drlName | string | 是 | - | 钻带名称 |
| drl_Id | int? | 是 | - | 钻带表，对应E_DrillTitle.recId |
| finish_Size | decimal? | 是 | - | 加工大小（要求大小） |
| E_JobRoutes | decimal? | 是 | - | 加工尺寸（要求大小） |
| holeTypeIsPalted | bool? | 是 | - | PTH |
| isCalculate | bool? | 是 | - | - |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| max_Tol | decimal? | 是 | - | 正公差 |
| min_Tol | decimal? | 是 | - | 负公差 |
| notes | string | 是 | - | - |
| partHolesNum | int? | 是 | - | 拼版孔数 |
| partPanel | int? | 是 | - | - |
| slotLength | decimal? | 是 | - | - |
| slotLength_MM | decimal? | 是 | - | - |
| slotReqd | decimal? | 是 | - | - |
| slotReqd_MM | decimal? | 是 | - | 长孔要求尺寸 |
| slot_MaxTol | decimal? | 是 | - | 长孔要求公差+ |
| slot_MinTol | decimal? | 是 | - | 长孔要求公差- |
| toolSeq | int? | 是 | - | - |
| toolStepName | string | 是 | - | 刀序 |
| unitHolesNum | int? | 是 | - | 小孔单元数 |
| unitPart | int? | 是 | - | - |
| version | int? | 是 | - | - |
| isLock | bool? | 是 | - | 是否锁定 |
| boadSideHoleNums | int? | 是 | - | - |
| pthAttr | string | 是 | - | 孔属性 |
- **关联关系**：
  - E_DrillDetails.drl_Id = E_DrillTitle.recId
  - E_DrillDetails.jobId = S_Job.recId

---

#### 193 钻带表 ( E_DrillTitle )
- **业务含义**：钻带表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| drillName | string | 是 | - | - |
| drillNotes | string | 是 | - | - |
| drillType | string | 是 | - | - |
| endLayer | int? | 是 | - | - |
| jobId | int? | 是 | - | 生产型号表，对应S_Job.recId |
| lastMark | string | 是 | - | - |
| mfgpartCode | string | 是 | - | 部件代码 |
| mfgpartId | int? | 是 | - | 制造部件编号，对应E_JobMfgParts.recId |
| mfgpartThickness | decimal? | 是 | - | - |
| platingCu1 | decimal? | 是 | - | - |
| seq | int? | 是 | - | - |
| startLayer | int? | 是 | - | - |
| uuid | string | 是 | - | - |
| version | int? | 是 | - | - |
| holeVolume | decimal? | 是 | - | - |
| panelName | string | 是 | - | - |
- **关联关系**：
  - E_DrillTitle.jobId = S_Job.recId
  - E_DrillTitle.mfgpartId = E_JobMfgParts.recId

---

#### 194 工具表 ( E_FPCToolTable )
- **业务含义**：工具表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| seq | int? | 是 | - | - |
| toolName | string | 是 | - | - |
| toolVersion | string | 是 | - | - |
| notes | string | 是 | - | 备注 |
| jobId | int? | 是 | - | 对应S_JOB.recId |
| version | int? | 是 | - | - |
| modifiedBy | string | 是 | - | 修改人 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
- **关联关系**：
  - E_FPCToolTable.jobId = S_JOB.recId

---

#### 195 阻抗表 ( E_Impedance )
- **业务含义**：阻抗表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 196 JOB关联合拼表 ( E_JobChildren )
- **业务含义**：JOB关联合拼表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 197 生产型号图片 ( E_JobImages )
- **业务含义**：生产型号图片
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobId | int? | 是 | - | 对应S_Job.recId |
| seq | int? | 是 | - | - |
| imageType | string | 是 | - | 图片格式 |
| imageName | string | 是 | - | 图片名称（PanelImage：A拼版，Panel_Bimage：B拼版，SheetImage：开料图，StackupImage：叠构图） |
| inputName | string | 是 | - | - |
| photo | byte[] | 是 | - | 图片 |
| modifiedBy | string | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：
  - E_JobImages.jobId = S_Job.recId

---

#### 198 工作层  层信息 ( E_JobLayers )
- **业务含义**：工作层  层信息
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| copperDesity | decimal? | 是 | - | 残铜率 |
| cuArea | decimal? | 是 | - | 铜面积 |
| cuLayerNum | int? | 是 | - | - |
| endLayer | int? | 是 | - | 结束层 |
| hoesCuSpec | string | 是 | - | 孔铜要求 |
| holesQty | decimal? | 是 | - | 孔数 |
| impedanceFlag | bool? | 是 | - | - |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| layerName | string | 是 | - | 层名 |
| layerType | string | 是 | - | 层类型 |
| materialTypeId | int? | 是 | - | - |
| minDribit | decimal? | 是 | - | 最小钻嘴 |
| minLine | decimal? | 是 | - | 最小线宽 |
| minLinetoPad | decimal? | 是 | - | 最小线到盘 |
| minPadtoPad | decimal? | 是 | - | 最小孔距 |
| minSpec | decimal? | 是 | - | 最小线距 |
| openQty | decimal? | 是 | - | 开窗数 |
| seq | int? | 是 | - | - |
| startLayer | int? | 是 | - | 开始层 |
| surfaceArea | decimal? | 是 | - | 暴露面积 |
| version | int? | 是 | - | - |
| baseCopperId | int? | 是 | - | 铜基（铜尺寸表），对应S_Conductor.recId |
| finishCopperId | int? | 是 | - | 完成铜厚，对应S_Conductor.recId |
- **关联关系**：
  - E_JobLayers.jobId = S_Job.recId
  - E_JobLayers.baseCopperId = S_Conductor.recId
  - E_JobLayers.finishCopperId = S_Conductor.recId

---

#### 199 工程制作——流程——部件参数表 ( E_JobMfgPartParams )
- **业务含义**：工程制作——流程——部件参数表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | - |
| dataType | string | 是 | - | - |
| dateValue | DateTime? | 是 | - | - |
| floatValue | decimal | 否 | - | - |
| intValue | int? | 是 | - | - |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| listVal | string | 是 | - | 参数值 |
| mfgpartId | int? | 是 | - | 制造部件编号，对应E_JobMfgParts.recId |
| parameterValue | string | 是 | - | - |
| seq | int? | 是 | - | - |
| sort | string | 是 | - | - |
| textValue | string | 是 | - | 参数值 |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 销售部件参数表，对应S_Parameters.recId |
- **关联关系**：
  - E_JobMfgPartParams.jobId = S_Job.recId
  - E_JobMfgPartParams.mfgpartId = E_JobMfgParts.recId
  - E_JobMfgPartParams.parametersId = S_Parameters.recId

---

#### 200 制造部件编号(本厂型号BOM表) ( E_JobMfgParts )
- **业务含义**：制造部件编号(本厂型号BOM表)
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| comment | string | 是 | - | 制造部件注解 |
| endLayerNum | int? | 是 | - | - |
| flagPM | string | 是 | - | M：制造部件。P：bom物料。F：自制件成品 |
| isManualEditRoute | bool? | 是 | - | - |
| isNoCuCore | bool? | 是 | - | - |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| jobRoutesUUID | string | 是 | - | - |
| layerType | int? | 是 | - | 层类型 0外层， 2内层 |
| layupThickness | decimal? | 是 | - | - |
| leadTime | int? | 是 | - | - |
| lotSize | int? | 是 | - | 最佳批量 |
| mfgPartCode | string | 是 | - | 型号代码 |
| mfgPartName | string | 是 | - | - |
| panelLen | decimal? | 是 | - | A板长 |
| panelLen_B | decimal? | 是 | - | B板长 |
| panelWid | decimal? | 是 | - | A板宽 |
| panelWid_B | decimal? | 是 | - | B板宽 |
| partLevel | int? | 是 | - | 制造周期 |
| pcsOfArray | int? | 是 | - | 单元/交货板数（一块set的pcs数） |
| pcsOfPanel | int? | 是 | - | 单元/拼板数(PCS/SET)A |
| pcsOfPanel_B | int? | 是 | - | 单元/拼板数(PCS/SET)B |
| pnlOfSheet | int? | 是 | - | 单元/开料数(PCS/PNL)A |
| pnlOfSheet_B | int? | 是 | - | 单元/开料数(PCS/PNL)B |
| qtyOfBom | decimal? | 是 | - | 用量 |
| scrapRate | decimal? | 是 | - | 报废率；E_JobMfgPartParams |
| seq | int? | 是 | - | 物料顺序，序列号 |
| sort | string | 是 | - | - |
| startLayerNum | int? | 是 | - | - |
| uuId | string | 是 | - | - |
| version | int? | 是 | - | - |
| unitIdOfBom | int? | 是 | - | 单位（1:PCS,2:SET,3:PNL），对应T_Unit.recId |
| jobRoutesId | int? | 是 | - | 对应E_JobRoutes.recId |
| materialTypeId | int? | 是 | - | 对应S_MaterialType.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| parentId | int? | 是 | - | 父级部件ID，对应E_JobMfgParts.recId |
| unitIdOfStock | int? | 是 | - | 单位，对应T_Unit.recId |
| usedRateOfSheet | decimal? | 是 | - | - |
| ply | int? | 是 | - | 倍数 |
| subMaterialsId | string | 是 | - | 替代物料，对应M_Materials.recId |
- **关联关系**：
  - E_JobMfgParts.jobId = S_Job.recId
  - E_JobMfgParts.unitIdOfBom = T_Unit.recId
  - E_JobMfgParts.jobRoutesId = E_JobRoutes.recId
  - E_JobMfgParts.materialTypeId = S_MaterialType.recId
  - E_JobMfgParts.materialsId = M_Materials.recId
  - E_JobMfgParts.parentId = E_JobMfgParts.recId
  - E_JobMfgParts.unitIdOfStock = T_Unit.recId
  - E_JobMfgParts.subMaterialsId = M_Materials.recId

---

#### 201 工程制作——基本信息——销售部件的参数值对应job这里的 ( E_JobParams )
- **业务含义**：工程制作——基本信息——销售部件的参数值对应job这里的
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | - |
| dataType | string | 是 | - | - |
| dateValue | DateTime? | 是 | - | - |
| floatValue | decimal? | 是 | - | - |
| intValue | int? | 是 | - | - |
| jobId | int? | 是 | - | 生产型号表，对应S_Job.recId |
| listVal | string | 是 | - | - |
| parameterValue | string | 是 | - | - |
| sort | string | 是 | - | - |
| textValue | string | 是 | - | - |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 参数表，对应S_Parameters.recId |
| seq | int? | 是 | - | - |
- **关联关系**：
  - E_JobParams.jobId = S_Job.recId
  - E_JobParams.parametersId = S_Parameters.recId

---

#### 202 流程参数值 ( E_JobRouteParams )
- **业务含义**：流程参数值
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | - |
| dataType | string | 是 | - | - |
| dateValue | DateTime? | 是 | - | - |
| floatValue | decimal? | 是 | - | - |
| intValue | int? | 是 | - | - |
| jobId | int? | 是 | - | 对应S_Job.recId |
| jobRoutesId | int? | 是 | - | 对应E_JobRoutes.recId |
| listVal | string | 是 | - | - |
| mfgpartId | int? | 是 | - | 生产编号，对应E_JobMfgParts.recId |
| parameterValue | string | 是 | - | - |
| seq | int? | 是 | - | - |
| sort | string | 是 | - | - |
| textValue | string | 是 | - | 参数值 |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 参数名称表，对应S_Parameters.recId |
| org_MfgpartId | int? | 是 | ((0)) | - |
- **关联关系**：
  - E_JobRouteParams.jobId = S_Job.recId
  - E_JobRouteParams.jobRoutesId = E_JobRoutes.recId
  - E_JobRouteParams.mfgpartId = E_JobMfgParts.recId
  - E_JobRouteParams.parametersId = S_Parameters.recId

---

#### 203 制造部件流程表 ( E_JobRoutes )
- **业务含义**：制造部件流程表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobId | int? | 是 | - | 对应S_Job.recId |
| mfgpartId | int? | 是 | - | 对应E_JobMfgParts.recId |
| notes | string | 是 | - | - |
| processLibraryId | int? | 是 | - | - |
| seq | int? | 是 | - | - |
| sourceType | int? | 是 | - | - |
| uuId | string | 是 | - | - |
| version | int? | 是 | - | - |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| org_SEQ | int? | 是 | ((0)) | - |
| org_MfgPartId | int? | 是 | ((0)) | - |
- **关联关系**：
  - E_JobRoutes.jobId = S_Job.recId
  - E_JobRoutes.mfgpartId = E_JobMfgParts.recId
  - E_JobRoutes.processId = T_Process.recId

---

#### 204 E_JobSMTBOM ( E_JobSMTBOM )
- **业务含义**：ERP 系统 E_JobSMTBOM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bodyIdentification | string | 是 | - | - |
| bomRemark | string | 是 | - | - |
| custBomQty | decimal? | 是 | - | - |
| custLocationId | string | 是 | - | - |
| custMatCode | string | 是 | - | - |
| custMatName | string | 是 | - | - |
| custMatSpec | string | 是 | - | - |
| direction | string | 是 | - | - |
| itemNo | string | 是 | - | - |
| materialCategory | string | 是 | - | - |
| note | string | 是 | - | - |
| priority | string | 是 | - | - |
| version | int? | 是 | - | - |
| custUnitId | int? | 是 | - | - |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| jobId | int? | 是 | - | 型号表，对应S_Job.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - E_JobSMTBOM.materialsId = M_Materials.recId
  - E_JobSMTBOM.processId = T_Process.recId
  - E_JobSMTBOM.jobId = S_Job.recId
  - E_JobSMTBOM.suppliersId = M_Suppliers.recId

---

#### 205 E_JobTargetHole ( E_JobTargetHole )
- **业务含义**：ERP 系统 E_JobTargetHole 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| jobId | string | 是 | - | s_job 表 |
| seq | string | 是 | - | - |
| holeNo | string | 是 | - | - |
| xVal | string | 是 | - | x值 |
| yVal | string | 是 | - | y值 |
| note | string | 是 | - | - |
| version | string | 是 | - | - |
- **关联关系**：无

---

#### 206 产品分组（流程模版主表 ( E_ProcessLibrary )
- **业务含义**：产品分组（流程模版主表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| isActive | bool? | 是 | - | 状态：1.启用  0.禁用 |
| notes | string | 是 | - | 备注 |
| processLibraryCode | string | 是 | - | 代码 |
| processLibraryName | string | 是 | - | 名称 |
| seq | int? | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 207 风险警示表 ( E_RiskWarning )
- **业务含义**：风险警示表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 表主键 |
| riskType | string | 是 | - | 风险类型：1=客户风险，2=型号风险，3=市场风险 |
| customerId | string | 是 | - | 客户ID，对应S_Customer.recId |
| salesPartsId | string | 是 | - | 销售部件ID，对应S_SalesParts.recId |
| plantsId | string | 是 | - | 工厂ID，对应T_Plants.recId |
| warningMsg | string | 是 | - | 风险警示信息 |
| expired | string | 是 | - | 是否过期 |
| version | string | 是 | - | - |
| lastModifyDate | string | 是 | - | - |
| modifiedBy | string | 是 | - | - |
- **关联关系**：
  - E_RiskWarning.customerId = S_Customer.recId
  - E_RiskWarning.salesPartsId = S_SalesParts.recId
  - E_RiskWarning.plantsId = T_Plants.recId

---

#### 208 大料信息表 ( E_SheetInfo )
- **业务含义**：大料信息表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 209 工程制作——叠构 ( E_StackUpInfo )
- **业务含义**：工程制作——叠构
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| copperDesity | decimal? | 是 | - | 残铜率 |
| cuArea | decimal? | 是 | - | - |
| cuLayerNum | int? | 是 | - | - |
| endLayer | int? | 是 | - | - |
| hoesCuSpec | string | 是 | - | - |
| holesQty | decimal? | 是 | - | - |
| impedanceFlag | bool? | 是 | - | - |
| isNoCuCore | bool? | 是 | - | - |
| jobId | int? | 是 | - | 生产编号，对应S_Job.recId |
| layerName | string | 是 | - | 层名称 |
| layerType | string | 是 | - | 层类型 |
| minDribit | decimal? | 是 | - | - |
| minLine | decimal? | 是 | - | - |
| minLinetoPad | decimal? | 是 | - | - |
| minPadtoPad | decimal? | 是 | - | - |
| minSpec | decimal? | 是 | - | 最小线距 |
| offSet_Mid | int? | 是 | - | - |
| openQty | decimal? | 是 | - | - |
| seq | int? | 是 | - | 序号 |
| startLayer | int? | 是 | - | 开始层 |
| surfaceArea | decimal? | 是 | - | - |
| thickness | decimal? | 是 | - | 材料厚度 |
| uuid | string | 是 | - | UUID |
| version | int? | 是 | - | 记录版本 |
| baseCopperId | int? | 是 | - | 对应S_Conductor.recId |
| botCuId | int? | 是 | - | 下铜，对应S_Conductor.recId |
| finishCopperId | int? | 是 | - | 对应S_Conductor.recId |
| materialFamilyId | int? | 是 | - | 对应S_MaterialFamily.recId |
| materialTypeId | int? | 是 | - | 对应S_MaterialType.recId |
| materialId | int? | 是 | - | 物料，对应M_Materials.recId |
| topCuId | int? | 是 | - | 上铜，对应S_Conductor.recId |
| ifMfgPart | bool? | 是 | - | - |
| plating1 | decimal? | 是 | - | 电镀1 |
| plating2 | decimal? | 是 | - | 电镀2 |
| finishCuThic | decimal? | 是 | - | - |
| matPosTol | decimal? | 是 | - | 正公差 |
| matNegTol | decimal? | 是 | - | 负公差 |
| unionCode | string | 是 | - | 通用材料代码 |
| baseThick | decimal? | 是 | - | - |
| botThick | int? | 是 | - | - |
| dielectricConst | decimal? | 是 | - | - |
| stackupFamily | string | 是 | - | - |
| tg | int? | 是 | - | - |
| topThick | int? | 是 | - | - |
| stackupMatType | string | 是 | - | - |
| resinContent | decimal? | 是 | - | - |
| includeCopper | bool? | 是 | - | - |
| drillType | string | 是 | - | - |
| colour | string | 是 | - | 颜色 |
| haligonfree | bool? | 是 | - | 无卤素 |
| suffix | string | 是 | - | - |
| ply | int? | 是 | - | 倍数 |
| custReqThick | decimal? | 是 | - | 客户要求厚度 |
- **关联关系**：
  - E_StackUpInfo.jobId = S_Job.recId
  - E_StackUpInfo.baseCopperId = S_Conductor.recId
  - E_StackUpInfo.botCuId = S_Conductor.recId
  - E_StackUpInfo.finishCopperId = S_Conductor.recId
  - E_StackUpInfo.materialFamilyId = S_MaterialFamily.recId
  - E_StackUpInfo.materialTypeId = S_MaterialType.recId
  - E_StackUpInfo.materialId = M_Materials.recId
  - E_StackUpInfo.topCuId = S_Conductor.recId

---

#### 210 工具表 ( E_ToolName )
- **业务含义**：工具表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| name | string | 是 | - | 名称 |
| seq | int? | 是 | - | 序号 |
| version | int? | 是 | - | 记录版本 |
| defaulAddFilmTool | bool? | 是 | - | 添加菲林 |
- **关联关系**：无

---

### 2.5 销售模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 211 雇员信息 ( S_BusinessMan )
- **业务含义**：雇员信息
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| address | string | 是 | - | 地址 |
| code | string | 是 | - | 编号 |
| email | string | 是 | - | 邮箱 |
| idCard | string | 是 | - | 身份证 |
| ifActive | bool? | 是 | - | 是否激活  0 否 1 是 |
| ifBusinessMan | bool? | 是 | - | 是否用于业务员 0 否 1 是 |
| ifEmployee | bool? | 是 | - | 是否用于雇员 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| password | string | 是 | - | 密码 |
| sex | string | 是 | - | 性别： M 男 W 女 |
| sort | string | 是 | - | 排序 |
| telephone | string | 是 | - | 电话 |
| version | int? | 是 | - | - |
| zip | string | 是 | - | 邮编 |
| ifAssistant | bool? | 是 | - | 是否用于业务助理 0 否 1 是 |
- **关联关系**：无

---

#### 212 S_CAR ( S_CAR )
- **业务含义**：ERP 系统 S_CAR 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approvedBy | string | 是 | - | - |
| attachId | string | 是 | - | - |
| carNumber | string | 是 | - | - |
| carOwner | string | 是 | - | - |
| carTitle | string | 是 | - | - |
| carVDate | DateTime? | 是 | - | - |
| carVUser | string | 是 | - | - |
| carVerification | string | 是 | - | - |
| complaintDesc | string | 是 | - | - |
| completedDate | DateTime? | 是 | - | - |
| conclusionDesc | string | 是 | - | - |
| customerConfirmPerson | string | 是 | - | - |
| dueDate | DateTime? | 是 | - | - |
| latDate | DateTime? | 是 | - | - |
| latUser | string | 是 | - | - |
| longTermAction | string | 是 | - | - |
| memo | string | 是 | - | - |
| preventionSpread | string | 是 | - | - |
| psDate | DateTime? | 是 | - | - |
| psUser | string | 是 | - | - |
| reportedBy | string | 是 | - | - |
| rootCause | string | 是 | - | - |
| shortTermAction | string | 是 | - | - |
| staDate | DateTime? | 是 | - | - |
| staUser | string | 是 | - | - |
| teamMember | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| complainmentId | int? | 是 | - | 客诉管理，对应S_Complainment.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| jobId | int? | 是 | - | 产品型号，对应S_Job.recId |
| plantId | int? | 是 | - | 工厂，对应T_Plants.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
- **关联关系**：
  - S_CAR.companyId = T_Company.recId
  - S_CAR.complainmentId = S_Complainment.recId
  - S_CAR.customerId = S_Customer.recId
  - S_CAR.jobId = S_Job.recId
  - S_CAR.plantId = T_Plants.recId
  - S_CAR.salesPartId = S_SalesParts.recId

---

#### 213 纸箱定义 ( S_Cartons )
- **业务含义**：纸箱定义
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 214 客诉管理 ( S_Complainment )
- **业务含义**：客诉管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
- **关联关系**：无

---

#### 215 客诉管理审批记录 ( S_ComplainmentHistory )
- **业务含义**：客诉管理审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| complainmentId | int? | 是 | - | 对应S_Complainment.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - S_ComplainmentHistory.complainmentId = S_Complainment.recId
  - S_ComplainmentHistory.myId = T_User.recId

---

#### 216 S_ComplainmentWF ( S_ComplainmentWF )
- **业务含义**：ERP 系统 S_ComplainmentWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 217 铜厚表 ( S_Conductor )
- **业务含义**：铜厚表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| forCoreCu | bool? | 是 | - | 是否用于覆铜板 |
| forLayer | bool? | 是 | - | 是否用于铜层 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| thickness | decimal? | 是 | - | 厚度 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 218 销售订单合同 ( S_Contract )
- **业务含义**：销售订单合同
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| billingAddress | string | 是 | - | 发票地址 |
| contactEmail | string | 是 | - | 送货邮件 |
| contactName | string | 是 | - | 送货人 |
| contactTel | string | 是 | - | 送货电话 |
| contractDate | DateTime? | 是 | - | 合同日期 |
| contractNotes | string | 是 | - | 合同备注 |
| contractNumber | string | 是 | - | - |
| createDate | DateTime? | 是 | - | 建单日期 |
| custContractNumber | string | 是 | - | 客户合同单号 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| rootSOID | int? | 是 | - | - |
| saleType | string | 是 | - | 销售类型：Bonded 保税， ForDomestic 内销， ForExport 外销 |
| shipmentDays | int? | 是 | - | 装运天数 |
| shippingAdress | string | 是 | - | 装运地址 |
| shippingContactEmail | string | 是 | - | 装运邮箱 |
| shippingContactName | string | 是 | - | 装运联系人 |
| shippingContactTel | string | 是 | - | 装运电话 |
| status | string | 是 | - | 单据状态：Action 未提交   Submit 已提交 |
| taxRate | decimal? | 是 | - | 税率 |
| type | string | 是 | - | 类型：'Make' 制造' Sale' 贸易 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| contractTypeId | int? | 是 | - | 订单类型表，对应S_OrderType.recId |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| fobId | int? | 是 | - | 贸易方式，对应T_FOB.recId |
| paymentMethodId | int? | 是 | - | 付款方式，对应T_PaymentMethod.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| shippingId | int? | 是 | - | 运输方式，对应T_Shipping.recId |
- **关联关系**：
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

#### 219 合同明细 ( S_ContractItem )
- **业务含义**：合同明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 220 货币 ( S_ContractItem scti )
- **业务含义**：货币
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 221 合同制造明细---额外费用表 ( S_ContractItemAddCharge )
- **业务含义**：合同制造明细---额外费用表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 金额 |
| freeAmount | decimal? | 是 | - | 免收金额 |
| reference | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| addtionalChargeId | int? | 是 | - | 费用表，对应T_ChargeItem.recId |
| contractItemId | int? | 是 | - | 销售订单合同明细主表，对应S_ContractItem.recId |
- **关联关系**：
  - S_ContractItemAddCharge.addtionalChargeId = T_ChargeItem.recId
  - S_ContractItemAddCharge.contractItemId = S_ContractItem.recId

---

#### 222 合同审核表 ( S_ContractItemHistory )
- **业务含义**：合同审核表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 对应S_ContractItem.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - S_ContractItemHistory.contractItemId = S_ContractItem.recId
  - S_ContractItemHistory.myId = T_User.recId

---

#### 223 销售订单合同明细--修改记录 ( S_ContractItemLog )
- **业务含义**：销售订单合同明细--修改记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| contractItemId | int? | 是 | - | 合同明细表，对应S_ContractItem.recId |
| createTime | DateTime? | 是 | - | 建单时间 |
| destQty | int? | 是 | - | 修改订单数量 |
| note | string | 是 | - | 备注  （内部单号信息） |
| srcQty | int? | 是 | - | 原来的数量 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| destJobId | int? | 是 | - | 修改后的型号，对应S_Job.recId |
| destSalePartId | int? | 是 | - | 修改后的销售部件，对应S_SalePart.recId |
| srcJobId | int? | 是 | - | 原来的型号，对应S_Job.recId |
| srcSalePartId | int? | 是 | - | 原来的销售部件，对应S_SalePart.recId |
- **关联关系**：
  - S_ContractItemLog.contractItemId = S_ContractItem.recId
  - S_ContractItemLog.creatorId = T_User.recId
  - S_ContractItemLog.destJobId = S_Job.recId
  - S_ContractItemLog.destSalePartId = S_SalePart.recId
  - S_ContractItemLog.srcJobId = S_Job.recId
  - S_ContractItemLog.srcSalePartId = S_SalePart.recId

---

#### 224 订单明细参数 ( S_ContractItemParameter )
- **业务含义**：订单明细参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| boolValue | bool? | 是 | - | 布尔值 |
| dataType | string | 是 | - | 参数类型 |
| dateValue | DateTime? | 是 | - | 日期值 |
| floatValue | decimal? | 是 | - | 浮点型值 |
| intValue | int? | 是 | - | 整数值 |
| listVal | string | 是 | - | 参数类型为可选择类型时的数据源 |
| parameterValue | string | 是 | - | 参数值 |
| sort | string | 是 | - | 排序 |
| textValue | string | 是 | - | 文本类型值 |
| parametersId | int? | 是 | - | 参数，对应S_Parameters.recId |
| contractItemId | int? | 是 | - | 合同明细，对应S_ContractItem.recId |
| version | int? | 是 | - | 版本 |
- **关联关系**：
  - S_ContractItemParameter.parametersId = S_Parameters.recId
  - S_ContractItemParameter.contractItemId = S_ContractItem.recId

---

#### 225 S_ContractItemProject ( S_ContractItemProject )
- **业务含义**：ERP 系统 S_ContractItemProject 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| QtyOrdered | int? | 是 | - | - |
| amount | decimal? | 是 | - | - |
| contractItemId | int? | 是 | - | 对应S_ContractItem.recId |
| finishDate | DateTime? | 是 | - | - |
| netAmount | decimal? | 是 | - | - |
| netPrice | decimal? | 是 | - | - |
| price | decimal? | 是 | - | - |
| qtyFree | int? | 是 | - | - |
| taxAmount | decimal? | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | - |
| plantBusinessId | int? | 是 | - | - |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| projectCombinationId | int? | 是 | - | - |
- **关联关系**：
  - S_ContractItemProject.contractItemId = S_ContractItem.recId
  - S_ContractItemProject.plantsId = T_Plants.recId

---

#### 226 S_ContractItemWF ( S_ContractItemWF )
- **业务含义**：ERP 系统 S_ContractItemWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 对应S_ContractItem.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - S_ContractItemWF.contractItemId = S_ContractItem.recId
  - S_ContractItemWF.myId = T_User.recId

---

#### 227 材料销售订单（贸易） ( S_ContractMaterials )
- **业务含义**：材料销售订单（贸易）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | - |
| amount_Invoiced2 | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | - |
| amount_Reconciled2 | decimal? | 是 | - | - |
| bodyIdentification | string | 是 | - | - |
| companyId | int? | 是 | - | - |
| direction | string | 是 | - | - |
| itemNo | string | 是 | - | - |
| materialCategory | string | 是 | - | - |
| note | string | 是 | - | - |
| poItemId | int? | 是 | - | - |
| priceInTax | decimal? | 是 | - | 含税单价 |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| qtyInPO | decimal? | 是 | - | - |
| qtyInSO | decimal? | 是 | - | - |
| qtyOrdered | decimal? | 是 | - | 订单数 |
| qtyOrderedCust | decimal? | 是 | - | - |
| qty_Invoiced | decimal? | 是 | - | - |
| qty_Invoiced2 | decimal? | 是 | - | - |
| qty_Reconciled | decimal? | 是 | - | - |
| qty_Reconciled2 | decimal? | 是 | - | - |
| quantity | decimal? | 是 | - | - |
| requestDate | DateTime? | 是 | - | 需求日期 |
| soNumber | string | 是 | - | 销售订单号 |
| taxRate | decimal? | 是 | - | 税率 |
| taxVal | decimal? | 是 | - | - |
| totalInTax | decimal? | 是 | - | 含税总金额 |
| totalNoTax | decimal? | 是 | - | 不含税总金额 |
| type | int? | 是 | - | - |
| version | int? | 是 | - | - |
| way | string | 是 | - | - |
| contractId | int? | 是 | - | 合同表，对应S_Contract.recId |
| contractItemId | int? | 是 | - | 合同明细，对应S_ContractItem.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
- **关联关系**：
  - S_ContractMaterials.contractId = S_Contract.recId
  - S_ContractMaterials.contractItemId = S_ContractItem.recId
  - S_ContractMaterials.materialsId = M_Materials.recId
  - S_ContractMaterials.processId = T_Process.recId

---

#### 228 销售订单表 ( S_ContractSO )
- **业务含义**：销售订单表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addAmount | decimal? | 是 | - | 额外费用 |
| amount | decimal? | 是 | - | 合计费用 |
| amount_Add | decimal? | 是 | - | 已对账额外费用 |
| amount_Add2 | decimal? | 是 | - | - |
| amount_Invoiced | decimal? | 是 | - | - |
| amount_Invoiced2 | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | - |
| amount_Reconciled2 | decimal? | 是 | - | - |
| assinedQtyInStock | int? | 是 | - | 入库数量（含WIP＋成品分配数量） |
| customerId | int? | 是 | - | 客户表，对应S_Customer.recId |
| discountAmount | decimal? | 是 | - | - |
| exchRate | decimal? | 是 | - | 汇率 |
| ifPO | bool? | 是 | - | - |
| ifReceive | bool? | 是 | - | 审核状态  1已审核 |
| note | string | 是 | - | - |
| plantBusinessItemId | int? | 是 | - | 对应F_PlantBusinessItem.recId |
| price | decimal? | 是 | - | 单价（含税） |
| prodType | string | 是 | - | - |
| qtyFree | int? | 是 | - | - |
| qtyFree_Invoiced | int? | 是 | - | - |
| qtyFree_Invoiced2 | int? | 是 | - | - |
| qtyFree_Reconciled | int? | 是 | - | - |
| qtyFree_Reconciled2 | int? | 是 | - | - |
| qtyOrdered | int? | 是 | - | 订购数量 |
| qtyShipFree | int? | 是 | - | - |
| qtyShipOrdered | int? | 是 | - | - |
| qty_Invoiced | int? | 是 | - | - |
| qty_Invoiced2 | int? | 是 | - | - |
| qty_Reconciled | int? | 是 | - | - |
| qty_Reconciled2 | int? | 是 | - | - |
| qty_inPO | int? | 是 | - | - |
| qty_inPR | int? | 是 | - | - |
| qty_planned | int? | 是 | - | 计划数 |
| qty_tobe_planned | int? | 是 | - | 待计划数 |
| rushAmount | decimal? | 是 | - | - |
| soNumber | string | 是 | - | 出货单号 |
| subAmount | decimal? | 是 | - | - |
| supplierId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| taxAmount | decimal? | 是 | - | - |
| taxRate | decimal? | 是 | - | 税率 |
| toolAmount | decimal? | 是 | - | 工具金额 |
| version | int? | 是 | - | - |
- **关联关系**：
  - S_ContractSO.customerId = S_Customer.recId
  - S_ContractSO.plantBusinessItemId = F_PlantBusinessItem.recId
  - S_ContractSO.supplierId = M_Suppliers.recId

---

#### 229 合同明细 ( S_ContractSO scts )
- **业务含义**：合同明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 230 客户管理 ( S_Customer )
- **业务含义**：客户管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| account | string | 是 | - | 科目 |
| account_ContactEmail | string | 是 | - | 财务联系邮件 |
| account_ContactName | string | 是 | - | 财务联系人 |
| account_ContactTel | string | 是 | - | 财务联系电话 |
| applyInTransit | bool? | 是 | - | 在库存中使用；0: 否, 1: 是 |
| backward | int? | 是 | - | 向后天数 |
| bank | string | 是 | - | 银行存款 |
| billingAdd | string | 是 | - | 发票地址 |
| code | string | 是 | - | 代码 |
| commission | decimal? | 是 | - | 佣金比& |
| creditLimited | decimal? | 是 | - | 授权额度 |
| doSmoothing | bool? | 是 | - | DoSmoothing |
| earlySchedule | int? | 是 | - | 可提前计划天数 |
| ediId | string | 是 | - | EDIID |
| email | string | 是 | - | 邮箱 |
| ename | string | 是 | - | 英文名称 |
| fax | string | 是 | - | 传真 |
| forward | int? | 是 | - | 向前天数 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifDateCode | bool? | 是 | - | 日期代码控制 |
| languageFlag | string | 是 | - | 语言标志 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| mobilePhone | string | 是 | - | 手机 |
| modifiedBy | string | 是 | - | 更新人员 |
| name | string | 是 | - | 名称 |
| nickName | string | 是 | - | 简称 |
| officeAdd | string | 是 | - | 办公地址 |
| planingHorizon | int? | 是 | - | 计划期天数 |
| rawHorizon | int? | 是 | - | 备料天数 |
| regAdd | string | 是 | - | 注册地址 |
| regNo | string | 是 | - | 工商注册号 |
| saleType | string | 是 | - | 贸易类型；Bonded: 保税
ForDomestic: 内销
ForExport: 外销 |
| selfCompanyId | int? | 是 | - | - |
| shipmentChecking | bool? | 是 | - | 对帐检查 |
| smoothingThreshold | int? | 是 | - | Smoothing |
| so_Acknowledgement | bool? | 是 | - | 订单确认 |
| sort | string | 是 | - | 排序 |
| source | string | 是 | - | 来源；Exhibition: 展会
Network: 网络
Popularity: 知名度
BusinessDev: 业务开发
Introduction: 介绍 |
| spare1 | string | 是 | - | 备用字段1 |
| spare2 | string | 是 | - | 备用字段2 |
| spare3 | string | 是 | - | 备用字段3 |
| spare4 | string | 是 | - | 备用字段4 |
| spare5 | string | 是 | - | 备用字段5 |
- **关联关系**：无

---

#### 231 客户管理--客户地址 ( S_CustomerAddress )
- **业务含义**：客户管理--客户地址
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| dateCodeRequired | bool? | 是 | - | 日期代码控制；0: 否; 1: 是 |
| email | string | 是 | - | 邮箱 |
| fax | string | 是 | - | 传真 |
| ifActive | bool? | 是 | - | 是否激活；0: 否; 1: 是 |
| ifConsignment | bool? | 是 | - | 是否寄售；0: 否; 1: 是 |
| languageFlag | string | 是 | - | 语言标志 |
| leadtime | int? | 是 | - | 制造周期 |
| location | string | 是 | - | 储区 |
| packRequirements | string | 是 | - | 包装要求 |
| packs_per_box | decimal? | 是 | - | 每箱小包数 |
| pct_OVER_SHIP | decimal? | 是 | - | 溢装率% |
| qty_OVER_SHIP | decimal? | 是 | - | 溢装数量 |
| qty_per_pack | decimal? | 是 | - | 每包数量 |
| qty_x_out | decimal? | 是 | - | 单废数量 |
| ship_to_address | string | 是 | - | 发货地址 |
| ship_to_contact | string | 是 | - | 收货联系人 |
| ship_to_email | string | 是 | - | 送货联系邮件 |
| ship_to_fax | string | 是 | - | 收货联系传真 |
| ship_to_phone | string | 是 | - | 收货人电话 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | 记录版本 |
| zip | string | 是 | - | 邮编 |
| cartonsId | int? | 是 | - | 对应S_Cartons.recId |
| customerId | int? | 是 | - | 对应S_Customer.recId |
| fobId | int? | 是 | - | 对应T_FOB.recId |
| shippingId | int? | 是 | - | 对应T_Shipping.recId |
| inPackingReportUrl | string | 是 | - | - |
| outPackingReportUrl | string | 是 | - | - |
| taxId | int? | 是 | - | - |
| currencyId | int? | 是 | - | - |
| saleType | string | 是 | - | 贸易类型 |
| megerCarton | bool? | 是 | - | 合拼箱 |
| deliveryNoteReportUrl | string | 是 | - | - |
- **关联关系**：
  - S_CustomerAddress.cartonsId = S_Cartons.recId
  - S_CustomerAddress.customerId = S_Customer.recId
  - S_CustomerAddress.fobId = T_FOB.recId
  - S_CustomerAddress.shippingId = T_Shipping.recId

---

#### 232 客户绑定公司 ( S_CustomerCompany )
- **业务含义**：客户绑定公司
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| modifiedBy | string | 是 | - | 更新人员 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
- **关联关系**：
  - S_CustomerCompany.companyId = T_Company.recId
  - S_CustomerCompany.customerId = S_Customer.recId

---

#### 233 客户管理审批记录 ( S_CustomerHistory )
- **业务含义**：客户管理审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务流程 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 发送描述 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 办理意见 |
| taskDesc | string | 是 | - | 任务描述 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务来源 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| sale | string | 是 | - | - |
- **关联关系**：
  - S_CustomerHistory.customerId = S_Customer.recId
  - S_CustomerHistory.myId = T_User.recId

---

#### 234 客户审批 ( S_CustomerWF )
- **业务含义**：客户审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务流程 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 发送描述 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 办理意见 |
| taskDesc | string | 是 | - | 任务描述 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务来源 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| sale | string | 是 | - | - |
- **关联关系**：
  - S_CustomerWF.customerId = S_Customer.recId
  - S_CustomerWF.myId = T_User.recId

---

#### 235 费用管理 ( S_ExpenseForm )
- **业务含义**：费用管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| enableApproval | bool? | 是 | - | - |
| endDate | DateTime? | 是 | - | 结束时间 |
| enterDate | DateTime? | 是 | - | 录入日期 |
| fromDate | DateTime? | 是 | - | 开启时间 |
| name | string | 是 | - | 费用描述 |
| note | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
- **关联关系**：
  - S_ExpenseForm.companyId = T_Company.recId
  - S_ExpenseForm.creatorId = T_User.recId
  - S_ExpenseForm.flowTypeId = T_FlowType.recId

---

#### 236 费用管理审批记录 ( S_ExpenseFormHistory )
- **业务含义**：费用管理审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| expenseFormId | int? | 是 | - | 对应S_ExpenseForm.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - S_ExpenseFormHistory.expenseFormId = S_ExpenseForm.recId
  - S_ExpenseFormHistory.myId = T_User.recId

---

#### 237 费用管理明细 ( S_ExpenseFormItem )
- **业务含义**：费用管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| actDate | DateTime? | 是 | - | - |
| approveStatus | string | 是 | - | - |
| costVal | decimal? | 是 | - | 费用金额 |
| placeFrom | string | 是 | - | 出发地 |
| ideas | string | 是 | - | - |
| note | string | 是 | - | - |
| placeTo | string | 是 | - | 目的地 |
| version | int? | 是 | - | - |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| expenseFormId | int? | 是 | - | 主表，对应S_ExpenseForm.recId |
| expenseItemId | int? | 是 | - | 费用定义，对应S_ExpenseItem.recId |
- **关联关系**：
  - S_ExpenseFormItem.currencyId = T_Currency.recId
  - S_ExpenseFormItem.customerId = S_Customer.recId
  - S_ExpenseFormItem.expenseFormId = S_ExpenseForm.recId
  - S_ExpenseFormItem.expenseItemId = S_ExpenseItem.recId

---

#### 238 S_ExpenseFormWF ( S_ExpenseFormWF )
- **业务含义**：ERP 系统 S_ExpenseFormWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| expenseFormId | int? | 是 | - | 对应S_ExpenseForm.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - S_ExpenseFormWF.expenseFormId = S_ExpenseForm.recId
  - S_ExpenseFormWF.myId = T_User.recId

---

#### 239 费用定义 ( S_ExpenseItem )
- **业务含义**：费用定义
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 马超 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 240 成品送检单 ( S_FGIIQCRecheck )
- **业务含义**：成品送检单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 送检单号 |
| note | string | 是 | - | 备注 |
| qtyArrayInspection | int? | 是 | - | 送检交货板数SET |
| qtyArrayReStock | int? | 是 | - | 入库SET数 |
| qtyArrayReturn | int? | 是 | - | 返回SET数 |
| qtyArrayScrapped | int? | 是 | - | 报废SET数 |
| qtyPanelInspection | int? | 是 | - | 送检PNL |
| qtyPanelReStock | int? | 是 | - | 入库PNL数 |
| qtyPanelReturn | int? | 是 | - | 返回PNL数 |
| qtyPanelScrapped | int? | 是 | - | 报废PNL数 |
| qtyPcsInspection | int? | 是 | - | 送检PCS |
| qtyPcsReStock | int? | 是 | - | 入库PCS数 |
| qtyPcsReturn | int? | 是 | - | 返回PCS数 |
| qtyPcsScrapped | int? | 是 | - | 报废PCS数 |
| status | string | 是 | - | Active:活动 Submit:提交 IQC:IQC已检验 Close:关闭 Ordered 已下单 Received 已接收 Returned已退回 |
| submissionDate | DateTime? | 是 | - | 提交送检日期 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| fgiInventoryId | int? | 是 | - | 成品库存，对应FGI_Inventory.recId |
| inspectPostId | int? | 是 | - | 对应T_PostRole.recId |
| postRoleId | int? | 是 | - | 604950，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - S_FGIIQCRecheck.creatorId = T_User.recId
  - S_FGIIQCRecheck.fgiInventoryId = FGI_Inventory.recId
  - S_FGIIQCRecheck.inspectPostId = T_PostRole.recId
  - S_FGIIQCRecheck.postRoleId = T_PostRole.recId
  - S_FGIIQCRecheck.warehouseId = T_Warehouse.recId

---

#### 241 成品送检单明细 ( S_FGIIQCRecheckItem )
- **业务含义**：成品送检单明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qtyArrayInspection | int? | 是 | - | 送检SET |
| qtyPanelInspection | int? | 是 | - | 送检PNL |
| qtyPcsInspection | int? | 是 | - | 送检PSC |
| version | int? | 是 | - | - |
| fgiInventoryId | int? | 是 | - | 成品库存表，对应FGI_Inventory.recId |
| fgiSubmissionId | int? | 是 | - | 成品送检单，对应S_FGIIQCRecheck.recId |
- **关联关系**：
  - S_FGIIQCRecheckItem.fgiInventoryId = FGI_Inventory.recId
  - S_FGIIQCRecheckItem.fgiSubmissionId = S_FGIIQCRecheck.recId

---

#### 242 产品型号  生产部件 ( S_Job )
- **业务含义**：产品型号  生产部件
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| analysisCode1 | string | 是 | - | 分析代码1 |
| analysisCode2 | string | 是 | - | 分析代码2 |
| analysisCode3 | string | 是 | - | 分析代码3 |
| analysisCode4 | string | 是 | - | 分析代码4 |
| analysisCode5 | string | 是 | - | 分析代码5 |
| approveStatus | string | 是 | - | 审批状态；Pending: 制作中
Submit: 提交
Waiting: 审批中
Approved: 审批通过
Rejected: 拒绝 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| assignedBy | string | 是 | - | 分配给哪个用户 |
| assignedDate | DateTime? | 是 | - | 分配日期 |
| assignedDesc | string | 是 | - | 分配描述 |
| assignedScenaro | bool? | 是 | - | 指定物料组合 |
| buildMode | string | 是 | - | 叠构方式 |
| camInstruct | string | 是 | - | CAM指示 |
| comment | string | 是 | - | 注解 |
| createBy | string | 是 | - | 创建人员 |
| createDate | DateTime? | 是 | - | 创建日期 |
| culayers | int? | 是 | - | 铜层；1为单面板  2以上双面板 |
| dateCode | string | 是 | - | 周期码 |
| delivery_X | int? | 是 | - | 交付形式X |
| delivery_Y | int? | 是 | - | 交付形式Y |
| designBy | string | 是 | - | 设计 |
| drills | int? | 是 | - | 钻带 |
| enableApproval | bool? | 是 | - | 提交审批 |
| inActive | bool? | 是 | - | 停止使用；0: 活动; 1: 取消 |
| isAssigned | bool? | 是 | - | 已分配 |
| isSymmetry | bool? | 是 | - | - |
| jobStatus | string | 是 | - | MI 状态 |
| leadTime | int? | 是 | - | 制造周期 |
| legendbot | int? | 是 | - | 底层文字 |
| legendtop | int? | 是 | - | 顶层文字 |
| lotSize | int? | 是 | - | 工单基数 |
| maxPartLevel | int? | 是 | - | - |
| mfgTime | int? | 是 | - | 制造周期 |
| miNotes | string | 是 | - | 工程记事 |
| originalStatus | string | 是 | - | - |
| panelLen | decimal? | 是 | - | 拼版长(mm) |
| panelLen_B | decimal? | 是 | - | B拼板板长 |
| panelWid | decimal? | 是 | - | 拼版宽(mm) |
| panelWid_B | decimal? | 是 | - | B拼板板宽 |
| partArea | decimal? | 是 | - | 交货板面积；平方 |
| partFlag | string | 是 | - | 生产编号标志 |
| partHigh | decimal? | 是 | - | 高 |
| partLength | decimal? | 是 | - | 交货板长(mm) |
| partName | string | 是 | - | 部件名称 |
| partNum | string | 是 | - | 产品编码 |
| partRev | string | 是 | - | 生产编号版本 |
| partWid | decimal? | 是 | - | 交货板宽(mm) |
| pcsOfArray | int? | 是 | - | 单元/交货版数 |
| pcsOfPanel | int? | 是 | - | 单元/拼板数 |
| pcsOfPanel_B | int? | 是 | - | 单元/拼板数 B |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| planOnhold | bool? | 是 | ((0)) | 计划暂停；0: 否; 1: 是 |
| pnlOfSheet | int? | 是 | - | 拼版数/开料 |
| pnlOfSheet_B | int? | 是 | - | - |
| releaseOnhold | bool? | 是 | ((0)) | 发放暂停；0: 否; 1: 是 |
| routs | int? | 是 | - | 锣带 |
| scrapRate | decimal? | 是 | - | 报废率 |
| setQty | int? | 是 | - | Set数 |
| shelfLife | int? | 是 | - | 保质期 |
| smbot | int? | 是 | - | 底层阻焊 |
| smtop | int? | 是 | - | 顶层阻焊 |
| soOnhold | bool? | 是 | ((0)) | 销售暂停；0: 否; 1: 是 |
| status | string | 是 | - | 状态；Valid: 审批通过
Active: 制作中 |
| unitWeight | decimal? | 是 | - | 单重(kg) |
| version | int? | 是 | - | 记录版本 |
| xoutMaxQty | int? | 是 | - | 最大叉板数 |
| projectCombinationId | int? | 是 | - | - |
| assignedUserId | int? | 是 | - | 对应T_User.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建档人，对应T_User.recId |
| deliveryUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| flowTypeId | int? | 是 | - | 流程设计，对应T_FlowType.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| productGroupId | int? | 是 | - | 产品分组，对应S_ProductGroup.recId |
| partId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| scenaroId | int? | 是 | - | 材料类型组合，对应S_MaterialTypeCombination.recId |
| customerId | int? | 是 | - | 客户管理，对应S_Customer.recId |
| saleProjectId | int? | 是 | - | 分组，对应S_SaleProject.recId |
| isImportMi | bool? | 是 | - | - |
| modifiedBy | string | 是 | - | 更新人员 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| departmentId | int? | 是 | - | - |
| panelType | string | 是 | - | 板类型 |
| ifHadSMT | bool? | 是 | - | - |
| usedRateOfSheet | decimal? | 是 | - | 大料利用率 |
| sheetLen | decimal? | 是 | - | 大料长(mm) |
| sheetWid | decimal? | 是 | - | 大料宽(mm) |
| type | string | 是 | - | 类型；Sample: 样板
Batch: 批量
Other: 其它
MGSuit: 套版
SubSuit: 套版子板 |
| filmMode | string | 是 | - | - |
| packings | string | 是 | - | 包装信息 |
| panelizerNotes | string | 是 | - | 拼版备注 |
| qtyofPN | int? | 是 | - | - |
| setOfPnl | int? | 是 | - | - |
| costFlag | bool? | 是 | - | 成本状态 |
| costCalUserId | int? | 是 | - | - |
| costCalDate | DateTime? | 是 | - | - |
| costCalNotes | string | 是 | - | - |
| onHoldNotes | string | 是 | - | 备注 |
| receiptTime | DateTime? | 是 | - | 资料接收时间 |
| planFinishTime | DateTime? | 是 | - | - |
| eqSendTime | DateTime? | 是 | - | 客问发出时间 |
| eqReplyTime | DateTime? | 是 | - | 客问回复时间 |
| eqFinishTime | DateTime? | 是 | - | 客问完成时间 |
| miFinishTime | DateTime? | 是 | - | 制作完成时间 |
| eqNotes | string | 是 | - | 客问备注 |
| halogenFree | bool? | 是 | - | 无卤素；0: 否; 1: 是 |
| grossWeight | decimal? | 是 | - | 毛重 |
| stackupNotes | string | 是 | - | - |
| progressStatus | string | 是 | - | 制作状态 |
| productGradeId | int? | 是 | - | 产品等级，对应T_Cate.recId |
| appCategoryId | int? | 是 | - | 产品分类，对应S_ProductCategory.recId |
| cartonsId | int? | 是 | - | - |
| spacerMatId | int? | 是 | - | - |
| packMatId | int? | 是 | - | - |
| qtyOfBagPerCarton | int? | 是 | - | 每箱包数 |
| qtyOfArrayPerBag | int? | 是 | - | 每包板数 |
| ifMixDateCode | bool? | 是 | - | - |
| ifMixXOutCarton | bool? | 是 | - | - |
| ifMixXOutPack | bool? | 是 | - | - |
| plantId | int? | 是 | - | 工厂，对应T_Plants.recId |
| isNewVersion | bool? | 是 | - | - |
| prevVersion_JobId | int? | 是 | - | - |
| residuesLen | decimal? | 是 | - | 余料长 |
| residuesWid | decimal? | 是 | - | 余料宽 |
| residuesRateOfSheet | decimal? | 是 | - | 余料比例 |
| woNum | int? | 是 | - | - |
| rack | string | 是 | - | 货位 |
| panelizerJsonData | string | 是 | - | - |
| custPackNumType | string | 是 | - | 箱包流水类型 |
| inPackingReportUrl | string | 是 | - | - |
| outPackingReportUrl | string | 是 | - | - |
| inPlantPackingReportUrl | string | 是 | - | - |
| outPlantPackingReportUrl | string | 是 | - | - |
| submitDate | DateTime? | 是 | - | 提交日期 |
| ifSubstituteSuppliers | bool? | 是 | - | - |
| laminatedThick | decimal? | 是 | - | 压合后厚度 |
| lamThickPosTol | decimal? | 是 | - | - |
| lamThickNegTol | decimal? | 是 | - | - |
| outLineApproved | bool? | 是 | - | - |
| isImportFromDataFile | bool? | 是 | - | - |
| importStackupImg | bool? | 是 | - | - |
| custMatCode | string | 是 | - | 客户物料编码 |
| endCustomerId | int? | 是 | - | 终端客户，对应S_Customer.recId |
| endCustomer | string | 是 | - | 终端客户 |
| bomTypeCode | string | 是 | - | - |
| hadguestquest | string | 是 | - | 有客问 |
| maxRate | decimal? | 是 | - | 叉板比例% |
| surface | string | 是 | - | 表面处理 |
| etching | string | 是 | - | 蚀刻类型 |
| cuThick | decimal? | 是 | - | 铜厚 |
| isThickCopper | bool? | 是 | - | 厚銅板 |
| pa1 | string | 是 | - | 参数1 |
| pa2 | string | 是 | - | - |
| pa3 | string | 是 | - | - |
| pa4 | string | 是 | - | - |
| pa5 | string | 是 | - | - |
| cartonNetWeight | decimal? | 是 | - | 箱净重 |
| packGrossWeight | decimal? | 是 | - | 包毛重 |
| packNetWeight | decimal? | 是 | - | 包净重 |
| forcedDC | bool? | 是 | - | 强制订单录入周期码 |
| parentId | int? | 是 | - | - |
| inner_ScrapeRate | decimal? | 是 | - | - |
| ifCalWasteUnit | bool? | 是 | - | - |
| arrayWeight | decimal? | 是 | - | - |
| calWasteUnitDate | DateTime? | 是 | - | - |
| wasteCalMsg | string | 是 | - | - |
| projectName | string | 是 | - | 项目名称 |
| sameWarpZonal | bool? | 是 | - | 经纬向一致 |
| endCustPartNum | string | 是 | - | 终端产品编号 |
| endCustPartDesc | string | 是 | - | 终端产品名称 |
| endCustPartRev | string | 是 | - | 终端产品版本 |
| smtBomStatus | string | 是 | - | 元器件BOM状态 |
| smtBomProducerId | int? | 是 | - | - |
| smtBomProduceTime | DateTime? | 是 | - | 最后编辑时间 |
| smtBomSenderId | int? | 是 | - | - |
| smtBomSendTime | DateTime? | 是 | - | - |
| smtBomApproverId | int? | 是 | - | - |
| smtBomApprovalTime | DateTime? | 是 | - | 审批时间 |
| smtBomProcessCode | string | 是 | - | SMT元器件默认使用工艺 |
| auxMatProcess | string | 是 | - | 辅料流程 |
| jobGroupId | int? | 是 | - | - |
| packingModifyDate | DateTime? | 是 | - | - |
| packingModifyUserId | int? | 是 | - | - |
| qualityOnhold | bool? | 是 | - | 品质暂停 |
| saleNote | string | 是 | - | - |
| camStatus | string | 是 | - | CAM状态 |
| camAssignId | int? | 是 | - | - |
| camAssignDate | DateTime? | 是 | - | CAM分配时间 |
| camAssignToId | int? | 是 | - | - |
| camSubmitId | int? | 是 | - | - |
| camSubmitDate | DateTime? | 是 | - | CAM提交时间 |
| camSubmitToId | int? | 是 | - | - |
| camFinishId | int? | 是 | - | - |
| camFinishDate | DateTime? | 是 | - | CAM完成时间 |
| camNotes | string | 是 | - | CAM备注 |
| maxSampleOutput | int? | 是 | - | 样品最大投产量 |
| extraPartNum | string | 是 | - | 辅助编码 |
| qtyOfBagPerPack | int? | 是 | - | - |
| qtyOfPackPerCase | int? | 是 | - | - |
| qtyOfCasePerCarton | int? | 是 | - | - |
| preQualify | bool? | 是 | - | 是否预审单；0: 否; 1: 是 |
| preQualifyNo | string | 是 | - | 预审单号 |
| fromprejobid | int? | 是 | - | 预审单，对应S_Job.recId |
| panelizeId | int? | 是 | - | 默认拼版方案 |
| gbSentTime | DateTime? | 是 | - | GB发出时间 |
| gbReplyTime | DateTime? | 是 | - | GB回复时间 |
| interface_out | int? | 是 | - | - |
| interface_out2 | int? | 是 | - | - |
| packInsideMatId | int? | 是 | - | - |
| ifInterfaceSynchronization | bool? | 是 | - | - |
| isGenSalesPart | bool? | 是 | - | - |
| routeType | int? | 是 | - | 流程类型 |
| panelArea | decimal? | 是 | - | 拼版面积 |
| panelArea_B | decimal? | 是 | - | - |
| pcsLen | decimal? | 是 | - | PCS长(mm) |
| pcsWid | decimal? | 是 | - | PCS宽(mm) |
| pcsArea | decimal? | 是 | - | PCS面积 |
| isTearing | bool? | 是 | - | - |
| firstAssignTime | DateTime? | 是 | - | 一审分配时间 |
| firstAssignToId | int? | 是 | - | - |
| firstFinishTime | DateTime? | 是 | - | 一审完成时间 |
| secondAssignTime | DateTime? | 是 | - | 二审分配时间 |
| secondAssignToId | int? | 是 | - | - |
| secondFinishTime | DateTime? | 是 | - | 二审完成时间 |
| camCheckAssignToId | int? | 是 | - | - |
| camCheckAssignTime | DateTime? | 是 | - | Cam审核分配时间 |
| specSort | int? | 是 | - | - |
| setNetWeightUpperLimit | decimal? | 是 | - | - |
| setNetWeightLowerLimit | decimal? | 是 | - | - |
| packageMaterialsUpperLimit | decimal? | 是 | - | - |
| packageMaterialsLowerLimit | decimal? | 是 | - | - |
| cartonMaterialsUpperLimit | decimal? | 是 | - | - |
| cartonMaterialsLowerLimit | decimal? | 是 | - | - |
| maxForkPlates | int? | 是 | - | - |
| acceptForkPlatesCheck | bool? | 是 | - | - |
| weeklyCheck | bool? | 是 | - | - |
| forkPlatesOrderGeneration | bool? | 是 | - | - |
| mixedForkPacking | bool? | 是 | - | - |
- **关联关系**：
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
  - S_Job.fromprejobid = S_Job.recId

---

#### 243 生产型号审批记录 ( S_JobHistory )
- **业务含义**：生产型号审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务流程 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 发送描述 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 办理意见 |
| taskDesc | string | 是 | - | 任务描述 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务来源 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | cccvvvvv |
| version | int? | 是 | - | 记录版本 |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| partNumberId | int? | 是 | - | 生产编号，对应S_Job.recId |
- **关联关系**：
  - S_JobHistory.myId = T_User.recId
  - S_JobHistory.partNumberId = S_Job.recId

---

#### 244 型号连接销售部件 ( S_JobLink )
- **业务含义**：型号连接销售部件
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| version | int? | 是 | - | 记录版本 |
| jobId | int? | 是 | - | 生产编号，对应S_Job.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| modifyUserId | int? | 是 | - | 更新用户 |
| modifyTime | DateTime? | 是 | - | 最后修改日期 |
- **关联关系**：
  - S_JobLink.jobId = S_Job.recId
  - S_JobLink.salesPartsId = S_SalesParts.recId

---

#### 245 S_JobPrjLink ( S_JobPrjLink )
- **业务含义**：ERP 系统 S_JobPrjLink 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobLinkId | int? | 是 | - | - |
| qty | int? | 是 | - | - |
| salesPartsId | int? | 是 | - | - |
| type | int? | 是 | - | - |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | 对应S_Job.recId |
| projectCombinationId | int? | 是 | - | 对应S_ProjectCombination.recId |
- **关联关系**：
  - S_JobPrjLink.jobId = S_Job.recId
  - S_JobPrjLink.projectCombinationId = S_ProjectCombination.recId

---

#### 246 生产编号审批 ( S_JobWF )
- **业务含义**：生产编号审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务流程 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 发送描述 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 办理意见 |
| taskDesc | string | 是 | - | 任务描述 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务来源 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
| partNumberId | int? | 是 | - | 生产编号，对应S_Job.recId |
- **关联关系**：
  - S_JobWF.myId = T_User.recId
  - S_JobWF.partNumberId = S_Job.recId

---

#### 247 层信息 ( S_LayerType )
- **业务含义**：层信息
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| defaultfor | bool? | 是 | - | 是否默认 |
| layerType | string | 是 | - | 层类型 |
| propertyType | string | 是 | - | 属性类型 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 248 厂商型号 ( S_MaterialFamily )
- **业务含义**：厂商型号
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cafResistant | bool? | 是 | - | cafResistant |
| comment | string | 是 | - | comment |
| defaults | bool? | 是 | - | defaults |
| dk | decimal? | 是 | - | dk |
| flammabilityClass | string | 是 | - | flammabilityClass |
| glassWight | decimal? | 是 | - | glassWight |
| ipcClass | string | 是 | - | ipcClass |
| isFiller | bool? | 是 | - | isFiller |
| isHalogenFree | bool? | 是 | - | isHalogenFree |
| matFamilyCode | string | 是 | - | matFamilyCode |
| matFamilyName | string | 是 | - | matFamilyName |
| remark1 | string | 是 | - | remark1 |
| remark2 | string | 是 | - | remark2 |
| resin | decimal? | 是 | - | resin |
| tg | string | 是 | - | tg |
| uvBlocker | bool? | 是 | - | uvBlocker |
| version | int? | 是 | - | version |
| materialTypeId | int? | 是 | - | 物料类型，对应S_MaterialType.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - S_MaterialFamily.materialTypeId = S_MaterialType.recId
  - S_MaterialFamily.suppliersId = M_Suppliers.recId

---

#### 249 物料类型 ( S_MaterialType )
- **业务含义**：物料类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| isFilm | bool? | 是 | - | isFilm |
| matTypeCode | string | 是 | - | 类型代码 |
| matTypeName | string | 是 | - | 名称 |
| version | int? | 是 | - | - |
| ifRigid | bool? | 是 | ((0)) | 是否用于硬板 0 否 1 是 |
| ifFlex | bool? | 是 | ((0)) | 是否用于软板 0 否 1 是 |
| ifMfgPart | bool? | 是 | ((0)) | 是否用于制造部件 0 否 1 是 |
| ifBOMIssue | bool? | 是 | ((0)) | 是否用于BOM发料 0 否 1 是 |
| ifLackMatCheck | bool? | 是 | ((0)) | 是否用于欠料检查 0 否 1 是 |
- **关联关系**：无

---

#### 250 材料类型组合 ( S_MaterialTypeCombination )
- **业务含义**：材料类型组合
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| scenaro | string | 是 | - | scenaro |
| version | int? | 是 | - | version |
| coreId | int? | 是 | - | coreId，对应S_MaterialFamily.recId |
| prePregid | int? | 是 | - | prePregid，对应S_MaterialFamily.recId |
- **关联关系**：
  - S_MaterialTypeCombination.coreId = S_MaterialFamily.recId
  - S_MaterialTypeCombination.prePregid = S_MaterialFamily.recId

---

#### 251 订单类型 ( S_OrderType )
- **业务含义**：订单类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| contract | bool? | 是 | - | 是否用于合同 0 否 1 是 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| salesOrder | bool? | 是 | - | 是否用于销售单 0 否 1 是 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 252 外协采购单 ( S_OS_PO )
- **业务含义**：外协采购单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addChargeAmount | decimal? | 是 | - | 收费金额 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | 审批状态：Pending 制作中 Waiting 审核中 Approved 审核通过 |
| approveVersion | int? | 是 | - | - |
| contact | string | 是 | - | 订单联系人 |
| contactEmail | string | 是 | - | 订联系邮箱 |
| contactPhone | string | 是 | - | 联系电话 |
| createDate | DateTime? | 是 | - | 建单日期（创建日期） |
| enableApproval | bool? | 是 | - | 审批次数 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| misCharged | decimal? | 是 | - | - |
| noTaxAmount | decimal? | 是 | - | 未税金额 |
| originalStatus | string | 是 | - | - |
| os_PO_Date | DateTime? | 是 | - | 外发日期（采购日期） |
| os_PO_Note | string | 是 | - | 备注 |
| os_PO_Number | string | 是 | - | 外发单号 |
| os_PO_Type | string | 是 | - | 外发类型：Outsourcing |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| soId | int? | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | 单据状态：Active 制作中 Valid 生效(审批通过)，Onhold 暂缓 Cancel 取消 Close 关闭 Void 失效 |
| subAmount | decimal? | 是 | - | 合计金额 |
| taxAmount | decimal? | 是 | - | 税金 |
| toTalAmount | decimal? | 是 | - | 订单金额 |
| type | string | 是 | - | SO 订单外协    WO 工单外协 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| os_PlantId | int? | 是 | - | 外发工厂，对应T_Plants.recId |
| paymentMethodId | int? | 是 | - | 付款方式，对应T_PaymentMethod.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
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

#### 253 外协采购单审批记录 ( S_OS_POHistory )
- **业务含义**：外协采购单审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| os_PO_Id | int? | 是 | - | 对应S_OS_PO.recId |
- **关联关系**：
  - S_OS_POHistory.myId = T_User.recId
  - S_OS_POHistory.os_PO_Id = S_OS_PO.recId

---

#### 254 外协采购明细单 ( S_OS_POItem )
- **业务含义**：外协采购明细单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addChargeAmount | decimal? | 是 | - | 额外金额 |
| amount_Invoiced | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | - |
| approveStatus | string | 是 | - | - |
| committedDate | DateTime? | 是 | - | 提交时间（承诺交期） |
| contractSOId | int? | 是 | - | - |
| ideas | string | 是 | - | - |
| itemId | string | 是 | - | - |
| itemNote | string | 是 | - | 备注 |
| itemType | string | 是 | - | 外发类型：WO工单外发 SO销售外发 |
| leadTime | int? | 是 | - | 提前时间 |
| maxXoutQty | int? | 是 | - | - |
| os_PRItemId | int? | 是 | - | 请购明细，对应S_OS_PRItem.recId |
| percentOfXout | decimal? | 是 | - | - |
| priceInTax | decimal? | 是 | - | 原币含税单价 |
| priceNoTax | decimal? | 是 | - | 原币不含税单价 |
| qty | int? | 是 | - | 采购数量（PCS） |
| qtyArrayDefected | int? | 是 | - | 缺陷数SET |
| qtyArrayRecieved | int? | 是 | - | 接收数SET |
| qtyArrayReturn | int? | 是 | - | 正在退回SET |
| qtyArrayReturned | int? | 是 | - | 已退回数SET |
| qtyArrayReworked | int? | 是 | - | 返工SET |
| qtyArrayScrapped | int? | 是 | - | 报废SET |
| qtyArrayStocked | int? | 是 | - | 正在入库SET(临时) |
| qtyArrayToStock | int? | 是 | - | 已入库SET |
| qtyFree | int? | 是 | - | 赠品SET |
| qtyFree_Invoiced | int? | 是 | - | - |
| qtyFree_Reconciled | int? | 是 | - | - |
| qtyOfShipped | int? | 是 | - | 装运SET |
| qtyPanelDefected | int? | 是 | - | 缺陷数PNL |
| qtyPanelRecieved | int? | 是 | - | 接收数PNL |
| qtyPanelReturn | int? | 是 | - | 正在退回PNL |
| qtyPanelReturned | int? | 是 | - | 已退回数PNL |
| qtyPanelReworked | int? | 是 | - | 返工PNL |
| qtyPanelScrapped | int? | 是 | - | 报废PNL |
| qtyPanelStocked | int? | 是 | - | 正在入库PNL(临时) |
| qtyPanelToStock | int? | 是 | - | 已入库PNL |
| qtyPcsDefected | int? | 是 | - | 缺陷数PCS |
| qtyPcsRecieved | int? | 是 | - | 接收数PCS |
| qtyPcsReturn | int? | 是 | - | 待退回PCS（品质检查“退回”） |
| qtyPcsReturned | int? | 是 | - | 已退回数PCS（外协退货）退货后还可以再接收 |
| qtyPcsReworked | int? | 是 | - | 返工PCS |
| qtyPcsScrapped | int? | 是 | - | 报废PCS（品质检查“报废”） |
| qtyPcsStocked | int? | 是 | - | 已经入库的数量 |
| qtyPcsToStock | int? | 是 | - | 检查后可以入库的数量（合格可以入库的数量包括还没入库的） |
| qtyReceived | int? | 是 | - | 接受数量PCS（根据送货单位） |
| qtyReturned | int? | 是 | - | 采购退回 |
| qty_Invoiced | int? | 是 | - | 对账数 |
| qty_Reconciled | int? | 是 | - | 接收数量 |
| requestDate | DateTime? | 是 | - | 需求日期（客户交期） |
| subAmount | decimal? | 是 | - | 小计 |
| taxAmount | decimal? | 是 | - | 税金 |
| taxRate | decimal? | 是 | - | 税率 |
| toTalAmount | decimal? | 是 | - | 总金额 |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 销售合同明细（对应外协订单），对应S_ContractItem.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| os_PO_Id | int? | 是 | - | 外发采购主表，对应S_OS_PO.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| subcontractTypeId | int? | 是 | - | 外协类型，对应T_SubcontractType.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| qty_Array | int? | 是 | ((0)) | - |
| qty_PNL | int? | 是 | ((0)) | - |
| qtyOfArrayShipped | int? | 是 | ((0)) | - |
| qtyOfPNLShipped | int? | 是 | ((0)) | - |
| ab | string | 是 | - | AB拼板 |
| revStatus | string | 是 | - | 状态 |
- **关联关系**：
  - S_OS_POItem.os_PRItemId = S_OS_PRItem.recId
  - S_OS_POItem.contractItemId = S_ContractItem.recId
  - S_OS_POItem.currencyId = T_Currency.recId
  - S_OS_POItem.jobId = S_Job.recId
  - S_OS_POItem.mfgPartId = E_JobMfgParts.recId
  - S_OS_POItem.os_PO_Id = S_OS_PO.recId
  - S_OS_POItem.salesPartId = S_SalesParts.recId
  - S_OS_POItem.subcontractTypeId = T_SubcontractType.recId
  - S_OS_POItem.unitId = T_Unit.recId

---

#### 255 外发采购明细更改表 ( S_OS_POItemAddCharge )
- **业务含义**：外发采购明细更改表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 原金额 |
| freeAmount | decimal? | 是 | - | 免收金额 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| chargeItemId | int? | 是 | - | 费用表，对应T_ChargeItem.recId |
| os_POItemId | int? | 是 | - | 外协采购明细，对应S_OS_POItem.recId |
- **关联关系**：
  - S_OS_POItemAddCharge.chargeItemId = T_ChargeItem.recId
  - S_OS_POItemAddCharge.os_POItemId = S_OS_POItem.recId

---

#### 256 外协采购单审批 ( S_OS_POWF )
- **业务含义**：外协采购单审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| os_PO_Id | int? | 是 | - | 对应S_OS_PO.recId |
- **关联关系**：
  - S_OS_POWF.myId = T_User.recId
  - S_OS_POWF.os_PO_Id = S_OS_PO.recId

---

#### 257 外协请购单 ( S_OS_PR )
- **业务含义**：外协请购单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addChargeAmount | decimal? | 是 | - | 额外金额 |
| additionalStatus | string | 是 | - | 审批状态   Approved 通过 |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| createDate | DateTime? | 是 | - | 建单日期 |
| enableApproval | bool? | 是 | - | - |
| exchangeRate | decimal? | 是 | - | 汇率 |
| noTaxAmount | decimal? | 是 | - | 不含税总金额 |
| originalStatus | string | 是 | - | - |
| os_PR_Date | DateTime? | 是 | - | 外协请购日期 |
| os_PR_Note | string | 是 | - | 备注 |
| os_PR_Number | string | 是 | - | 外协请购单号 |
| os_PR_Type | string | 是 | - | 外购外协类型：Outsourcing 工单 |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | 单据状态:Cancel 取消 Valid 有效的 |
| subAmount | decimal? | 是 | - | 订购金额 |
| taxAmount | decimal? | 是 | - | 税金 |
| toTalAmount | decimal? | 是 | - | 总计金额 |
| type | string | 是 | - | WO工单外协       SO订单外协 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
| os_PlantId | int? | 是 | - | 外发工厂，对应T_Plants.recId |
| plantsId | int? | 是 | - | 公司，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - S_OS_PR.creatorId = T_User.recId
  - S_OS_PR.currencyId = T_Currency.recId
  - S_OS_PR.flowTypeId = T_FlowType.recId
  - S_OS_PR.os_PlantId = T_Plants.recId
  - S_OS_PR.plantsId = T_Plants.recId
  - S_OS_PR.postRoleId = T_PostRole.recId
  - S_OS_PR.suppliersId = M_Suppliers.recId

---

#### 258 外协请购单审批记录 ( S_OS_PRHistory )
- **业务含义**：外协请购单审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| os_PR_Id | int? | 是 | - | 对应S_OS_PR.recId |
- **关联关系**：
  - S_OS_PRHistory.myId = T_User.recId
  - S_OS_PRHistory.os_PR_Id = S_OS_PR.recId

---

#### 259 外协请购明细单 ( S_OS_PRItem )
- **业务含义**：外协请购明细单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addChargeAmount | decimal? | 是 | - | 额外费用 |
| approveStatus | string | 是 | - | - |
| committedDate | DateTime? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售订单，对应S_ContractSO.recId |
| ideas | string | 是 | - | - |
| itemId | string | 是 | - | - |
| itemNote | string | 是 | - | 备注 |
| leadTime | int? | 是 | - | 制造周期 |
| maxXoutQty | int? | 是 | - | - |
| os_POItemId | int? | 是 | - | - |
| percentOfXout | decimal? | 是 | - | - |
| priceInTax | decimal? | 是 | - | 单价（含税） |
| priceNoTax | decimal? | 是 | - | 不含税单价 |
| qty | int? | 是 | - | 计价数量 |
| qtyFree | int? | 是 | - | 赠品数量 |
| requestDate | DateTime? | 是 | - | 要求交货日期 |
| subAmount | decimal? | 是 | - | 总请购金额 |
| taxAmount | decimal? | 是 | - | 总税额 |
| taxRate | decimal? | 是 | - | 税率 |
| toTalAmount | decimal? | 是 | - | 合计总金额 |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 销售合同明细，对应S_ContractItem.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| os_PR_Id | int? | 是 | - | 请购主表，对应S_OS_PR.recId |
| salesPartId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| subcontractTypeId | int? | 是 | - | 外协类型，对应T_SubcontractType.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| qty_Array | int? | 是 | ((0)) | - |
| qty_PNL | int? | 是 | ((0)) | - |
| ab | string | 是 | - | AB板：A 板 B板 AB板 |
- **关联关系**：
  - S_OS_PRItem.contractSOId = S_ContractSO.recId
  - S_OS_PRItem.contractItemId = S_ContractItem.recId
  - S_OS_PRItem.currencyId = T_Currency.recId
  - S_OS_PRItem.jobId = S_Job.recId
  - S_OS_PRItem.mfgPartId = E_JobMfgParts.recId
  - S_OS_PRItem.os_PR_Id = S_OS_PR.recId
  - S_OS_PRItem.salesPartId = S_SalesParts.recId
  - S_OS_PRItem.subcontractTypeId = T_SubcontractType.recId
  - S_OS_PRItem.unitId = T_Unit.recId

---

#### 260 外协请购明细单修改记录 ( S_OS_PRItemAddCharge )
- **业务含义**：外协请购明细单修改记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 数量 |
| freeAmount | decimal? | 是 | - | 赠品数量 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| chargeItemId | int? | 是 | - | 费用，对应T_ChargeItem.recId |
| os_PRItemId | int? | 是 | - | 外协请购明细单，对应S_OS_PRItem.recId |
- **关联关系**：
  - S_OS_PRItemAddCharge.chargeItemId = T_ChargeItem.recId
  - S_OS_PRItemAddCharge.os_PRItemId = S_OS_PRItem.recId

---

#### 261 S_OS_PRWF ( S_OS_PRWF )
- **业务含义**：ERP 系统 S_OS_PRWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| os_PR_Id | int? | 是 | - | 对应S_OS_PR.recId |
- **关联关系**：
  - S_OS_PRWF.myId = T_User.recId
  - S_OS_PRWF.os_PR_Id = S_OS_PR.recId

---

#### 262 外协装运 ( S_OS_Shipment )
- **业务含义**：外协装运
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| enterDate | DateTime? | 是 | - | 简单日期 |
| note | string | 是 | - | 备注 |
| os_Shipment_Number | string | 是 | - | 装运单号 |
| shipDate | DateTime? | 是 | - | 装运日期 |
| version | int? | 是 | - | - |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| userId | int? | 是 | - | 制单人，对应T_User.recId |
- **关联关系**：
  - S_OS_Shipment.plantsId = T_Plants.recId
  - S_OS_Shipment.postRoleId = T_PostRole.recId
  - S_OS_Shipment.suppliersId = M_Suppliers.recId
  - S_OS_Shipment.userId = T_User.recId

---

#### 263 外协装运明细 ( S_OS_ShipmentItem )
- **业务含义**：外协装运明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | 备注 |
| os_PO_Number | string | 是 | - | 外协采购单 |
| os_poItemId | int? | 是 | - | 外协采购明细表，对应S_OS_POItem.recId |
| qtyShipped | int? | 是 | - | 装运数量PCS |
| version | int? | 是 | - | - |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| os_ShipmentId | int? | 是 | - | 外协装运主表，对应S_OS_Shipment.recId |
| qtyArrayShipped | int? | 是 | ((0)) | 装运数量SET |
| qtyPNLShipped | int? | 是 | ((0)) | 装运数量PNL |
- **关联关系**：
  - S_OS_ShipmentItem.os_poItemId = S_OS_POItem.recId
  - S_OS_ShipmentItem.jobId = S_Job.recId
  - S_OS_ShipmentItem.mfgPartId = E_JobMfgParts.recId
  - S_OS_ShipmentItem.os_ShipmentId = S_OS_Shipment.recId

---

#### 264 外协采购工单表 ( S_OSWO )
- **业务含义**：外协采购工单表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| poItemId | int? | 是 | - | 外发采购明细，对应S_OS_POItem.recId |
| prItemId | int? | 是 | - | 外协请购明细单，对应S_OS_PRItem.recId |
| qty_Array_BACKLOG | int? | 是 | - | - |
| qty_Assigned | int? | 是 | - | - |
| qty_INOS | int? | 是 | - | - |
| qty_PCS_BACKLOG | int? | 是 | - | 外协工单装运数量PCS |
| qty_PNL_BACKLOG | int? | 是 | - | - |
| version | int? | 是 | - | - |
| moRouteId | int? | 是 | - | 制作订单的工艺流程(过数记录明细)，对应P_MORoute.recId |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| qty_PCS_Send | int? | 是 | ((0)) | 外协工单发放PCS |
| qty_Array_Send | int? | 是 | ((0)) | 外协工单发放SET |
| qty_PNL_Send | int? | 是 | ((0)) | 外协工单发放PNL |
| qty_PCS_Req | int? | 是 | ((0)) | 接收PCS |
| qty_Array_Req | int? | 是 | ((0)) | 接收SET |
| qty_PNL_Req | int? | 是 | ((0)) | 接收PNL |
| qtyPcsScrapped | int? | 是 | - | 外协工单报废PCS |
| qtyArrayScrapped | int? | 是 | - | - |
| qtyPanelScrapped | int? | 是 | - | - |
| qty_PCS_rec | string | 是 | - | - |
| qty_Array_rec | string | 是 | - | - |
| qty_PNL_rec | string | 是 | - | - |
| qty_PCS_unpaid | string | 是 | - | - |
| qty_Array_unpaid | string | 是 | - | - |
| qty_PNL_unpaid | string | 是 | - | - |
| qty_PCS_work | string | 是 | - | - |
| qty_Array_work | string | 是 | - | - |
| qty_PNL_work | string | 是 | - | - |
| qty_PCS_return | string | 是 | - | - |
| qty_Array_return | string | 是 | - | - |
| qty_PNL_return | string | 是 | - | - |
- **关联关系**：
  - S_OSWO.poItemId = S_OS_POItem.recId
  - S_OSWO.prItemId = S_OS_PRItem.recId
  - S_OSWO.moRouteId = P_MORoute.recId
  - S_OSWO.woId = P_WO.recId

---

#### 265 外协接收 ( S_OSWOReceipt )
- **业务含义**：外协接收
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| fgiReceiptId | int? | 是 | - | 成品接收表，对应FGI_Receipt.recId |
| os_poItemId | int? | 是 | - | 外发采购明细表，对应S_OS_POItem.recId |
| qty_Array_unpaid | int? | 是 | - | 短交set数 |
| qty_Array_unpaid2 | int? | 是 | - | - |
| qty_Array_unwork | int? | 是 | - | 未加工set数 |
| qty_Array_unwork2 | int? | 是 | - | - |
| qty_Array_work | int? | 是 | - | 已加工set数 |
| qty_Array_work2 | int? | 是 | - | - |
| qty_PCS_unpaid | int? | 是 | - | 短交pcs数 |
| qty_PCS_unpaid2 | int? | 是 | - | - |
| qty_PCS_unwork | int? | 是 | - | 未加工pcs数 |
| qty_PCS_unwork2 | int? | 是 | - | - |
| qty_PCS_work | int? | 是 | - | 已加工pcs数 |
| qty_PCS_work2 | int? | 是 | - | - |
| qty_PNL_unpaid | int? | 是 | - | 短交pnl数 |
| qty_PNL_unpaid2 | int? | 是 | - | - |
| qty_PNL_unwork | int? | 是 | - | 未加工pnl数 |
| qty_PNL_unwork2 | int? | 是 | - | - |
| qty_PNL_work | int? | 是 | - | 已加工pnl数 |
| qty_PNL_work2 | int? | 是 | - | - |
| version | int? | 是 | - | - |
| oswoId | int? | 是 | - | 外协采购工单表，对应S_OSWO.recId |
- **关联关系**：
  - S_OSWOReceipt.fgiReceiptId = FGI_Receipt.recId
  - S_OSWOReceipt.os_poItemId = S_OS_POItem.recId
  - S_OSWOReceipt.oswoId = S_OSWO.recId

---

#### 266 外协采购分配工单表 ( S_OSWOSend )
- **业务含义**：外协采购分配工单表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| iqcId | int? | 是 | - | 制成品检验单，对应FGI_IQC.recId |
| qty_Array | int? | 是 | - | 外协工单本次发放SET |
| qty_PCS | int? | 是 | - | 外协工单本次发放PCS |
| qty_PNL | int? | 是 | - | 外协工单本次发放PNL |
| version | int? | 是 | - | - |
| oswoId | int? | 是 | - | 外协采购关联工单表，对应S_OSWO.recId |
| ifNew | bool? | 是 | - | - |
| receiptStepId | int? | 是 | - | - |
| receiptMoRouteId | int? | 是 | - | - |
| ifReceipt | bool? | 是 | - | - |
| qtyPcsScrapped | int? | 是 | - | 外协工单本次报废PCS |
| qtyArrayScrapped | int? | 是 | - | 外协工单本次报废SET |
| qtyPanelScrapped | int? | 是 | - | 外协工单本次报废PNL |
- **关联关系**：
  - S_OSWOSend.iqcId = FGI_IQC.recId
  - S_OSWOSend.oswoId = S_OSWO.recId

---

#### 267 外协采购工单装运表 ( S_OSWOShipment )
- **业务含义**：外协采购工单装运表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qty_Array | int? | 是 | - | SET |
| qty_PCS | int? | 是 | - | PCS |
| qty_PNL | int? | 是 | - | PNL |
| shipmentItemId | int? | 是 | - | 外协装运明细，对应S_OS_ShipmentItem.recId |
| version | int? | 是 | - | - |
| oswoId | int? | 是 | - | 外协采购工单表，对应S_OSWO.recId |
- **关联关系**：
  - S_OSWOShipment.shipmentItemId = S_OS_ShipmentItem.recId
  - S_OSWOShipment.oswoId = S_OSWO.recId

---

#### 268 销售数据--参数管理 ( S_Parameters )
- **业务含义**：销售数据--参数管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| capabilityDesc | string | 是 | - | 生产能力描述 |
| capabilityMaxVal | decimal? | 是 | - | 生产能力上限 |
| capabilityMinVal | decimal? | 是 | - | 生产能力下限 |
| checkFlag | bool? | 是 | - | 是否检查 |
| code | string | 是 | - | 代码 |
| dataType | string | 是 | - | 参数值类型：TextItem ,FloatItem,SelectItem，CheckboxItem，IntegerItem，DateItem |
| defaultValue | string | 是 | - | 默认值 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifCustomer | bool? | 是 | - | 是否用于客户 |
| ifInspectionReport | bool? | 是 | - | 是否用于检验报告上打印 |
| ifPrdEntry | bool? | 是 | - | 是否用于生产时输入 |
| ifProductionPart | bool? | 是 | - | 是否用于生产部件参数 |
| ifRoute | bool? | 是 | - | 是否用于流程参数 |
| ifSalesPart | bool? | 是 | - | 是否用于销售部件参数 |
| innerLayer | bool? | 是 | - | 是否用内层 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| listVal | string | 是 | - | 参数值 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| outerLayer | bool? | 是 | - | 外层 |
| paramDesc | string | 是 | - | 参数描述 |
| readOnly | bool? | 是 | - | 是否用于只读 |
| required | bool? | 是 | - | 必填 |
| seq | string | 是 | - | - |
| sublayer | bool? | 是 | - | - |
| toleranceAdd | decimal? | 是 | - | - |
| toleranceSub | decimal? | 是 | - | - |
| toleranceType | string | 是 | - | 公差类型: Percentage %   Numerical 数值  None 无 |
| version | int? | 是 | - | - |
| parametersGroupId | int? | 是 | - | 销售数据--参数分组，对应S_ParametersGroup.recId |
| ifCost | bool? | 是 | - | - |
- **关联关系**：
  - S_Parameters.parametersGroupId = S_ParametersGroup.recId

---

#### 269 销售数据--参数分组 ( S_ParametersGroup )
- **业务含义**：销售数据--参数分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 270 客户信息-评审-右侧的参数 ( S_ParameterValue )
- **业务含义**：客户信息-评审-右侧的参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 271 销售数据--产品分类 ( S_ProductCategory )
- **业务含义**：销售数据--产品分类
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| sort | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 272 销售数据--产品分类--公司 ( S_ProductCategoryCompany )
- **业务含义**：销售数据--产品分类--公司
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 273 销售数据--产品分组 ( S_ProductGroup )
- **业务含义**：销售数据--产品分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| builderEarlyDays | int? | 是 | - | 提前制造天数 |
| coreUtilLimit | decimal? | 是 | - | 开料利用率下限 |
| displayImpedance | bool? | 是 | - | 是否显示阻抗信息 |
| displayLayerView | bool? | 是 | - | 是否显示层信息 |
| displayLayup | bool? | 是 | - | 是否显示叠构 |
| displaySMT_BOM | bool? | 是 | - | 是否显示SMT材料 |
| display_BOM | bool? | 是 | - | 是否显示附加材料 |
| disp_Outline | string | 是 | - | 是否显示锣带 |
| lastModifyDate | DateTime? | 是 | - | 最后修改时间 |
| leadtime | int? | 是 | - | 制造周期 |
| lotSize | int? | 是 | - | 最佳批量 |
| minOrderAmount | decimal? | 是 | - | 最小订单金额 |
| minOrderArea | decimal? | 是 | - | 最小订单面积 |
| minOrderQty | decimal? | 是 | - | 最小订单数量 |
| modifiedBy | string | 是 | - | 修改人 |
| productGroupCode | string | 是 | - | 分组代码 |
| productGroupName | string | 是 | - | 分组名称 |
| scrapeRate | decimal? | 是 | - | 报废率 |
| scrapeRateBottom | decimal? | 是 | - | 报废率下限 |
| scrapeRateUpper | decimal? | 是 | - | 报废率上限 |
| shelfLife | int? | 是 | - | 保质期 |
| version | int? | 是 | - | - |
| inspectGroupId | int? | 是 | - | 检验分组，对应T_InspectGroup.recId |
| productCategoryId | int? | 是 | - | 产品分类，对应S_ProductCategory.recId |
| saleProjectId | int? | 是 | - | 销售项目，对应S_SaleProject.recId |
| panelType | string | 是 | - | 板类型：Rigid 硬板 Flex 软板 R-Flex 软硬结合 |
| layNum | string | 是 | - | 层数 |
| idfcode | string | 是 | - | 标识符 |
- **关联关系**：
  - S_ProductGroup.inspectGroupId = T_InspectGroup.recId
  - S_ProductGroup.productCategoryId = S_ProductCategory.recId
  - S_ProductGroup.saleProjectId = S_SaleProject.recId

---

#### 274 销售数据--产品分组--公司 ( S_ProductGroupCompany )
- **业务含义**：销售数据--产品分组--公司
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 275 销售数据--产品分组-参数管理 ( S_ProductGroupSpec )
- **业务含义**：销售数据--产品分组-参数管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| sort | string | 是 | - | 序号 |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 参数管理，对应S_Parameters.recId |
| productGroupId | int? | 是 | - | 产品分组，对应S_ProductGroup.recId |
- **关联关系**：
  - S_ProductGroupSpec.parametersId = S_Parameters.recId
  - S_ProductGroupSpec.productGroupId = S_ProductGroup.recId

---

#### 276 销售数据--项目组合 ( S_ProjectCombination )
- **业务含义**：销售数据--项目组合
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifBom | bool? | 是 | - | 是否用于BOM |
| level | int? | 是 | - | 制造周期 |
| mi | bool? | 是 | - | - |
| name | string | 是 | - | 名称 |
| rootId | int? | 是 | - | 根表 |
| version | int? | 是 | - | - |
| parentId | int? | 是 | - | 对应S_ProjectCombination.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| saleProjectId | int? | 是 | - | 销售项目，对应S_SaleProject.recId |
- **关联关系**：
  - S_ProjectCombination.parentId = S_ProjectCombination.recId
  - S_ProjectCombination.plantsId = T_Plants.recId
  - S_ProjectCombination.postRoleId = T_PostRole.recId
  - S_ProjectCombination.saleProjectId = S_SaleProject.recId

---

#### 277 报价单快速报价结果 ( S_QuickQuoteResult )
- **业务含义**：报价单快速报价结果
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| rfqId | int? | 是 | - | 报价单 |
| jobId | int? | 是 | - | 生产编号 |
| seq | int? | 是 | - | 序号 |
| qty | int? | 是 | - | 订单数量 |
| isBatchSize | bool? | 是 | - | 批次 |
| demand | string | 是 | - | 需求天数 |
| schedules | int? | 是 | - | 需求 |
| targetPrice | decimal? | 是 | - | 格 |
| reportOption | string | 是 | - | 报表选项 |
| isNeedReCal | bool? | 是 | - | 重新计算 |
| standardTime | int? | 是 | - | 天数 |
| area | decimal? | 是 | - | 面积 |
| areaPrice | decimal? | 是 | - | 面积价 |
| pcsPrice | decimal? | 是 | - | 计算价 |
| adjustPrice | decimal? | 是 | - | 调整价 |
| refPrice | decimal? | 是 | - | 参考价 |
| discount | decimal? | 是 | - | 折扣 |
| discountPercent | decimal? | 是 | - | 折扣比 |
| priceAfterDiscount | decimal? | 是 | - | 销售价格 |
| noTaxPrice | decimal? | 是 | - | 未含税销售价 |
| noTaxMoney | decimal? | 是 | - | 未含税金额 |
| note | string | 是 | - | 备注 |
| basicPrice | decimal? | 是 | - | 计价表基价 |
| totalCost | decimal? | 是 | - | 合计 |
| stdCost | decimal? | 是 | - | 成本 |
| deliveryDate | DateTime? | 是 | - | 日期 |
| freightCharge | decimal? | 是 | - | 运费 |
| reservedSpace | decimal? | 是 | - | 留空间 |
| annualFallRatio | decimal? | 是 | - | 降总比例 |
| effectiveDate | DateTime? | 是 | - | 生效日期 |
| effectiveObject | string | 是 | - | 生效对象 |
| effectiveReminder | bool? | 是 | - | 生效提醒 |
| validstatus | string | 是 | - | 效用状态 |
| orgCalPcsPrice | decimal? | 是 | - | 原计算单元价 |
| orgCalAreaPrice | decimal? | 是 | - | 原计算面积价 |
| orgQuotedDate | DateTime? | 是 | - | 原计算日期 |
| lastCalPcsPrice | decimal? | 是 | - | 最后计算单元价 |
| lastCalAreaPrice | decimal? | 是 | - | 最后计算面积价 |
| lastQuotedDate | DateTime? | 是 | - | 最后计算日期 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 278 报价类别 ( S_QuoteCategory )
- **业务含义**：报价类别
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| ifActive | bool? | 是 | - | 是否激活 |
| note | string | 是 | - | 备注 |
| modifiedBy | string | 是 | - | 更新人员 |
| lastmodifydate | DateTime? | 是 | - | 更新时间 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 279 报价分组 ( S_QuoteGroup )
- **业务含义**：报价分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| categoryId | int? | 是 | - | 报价类别 |
| name | string | 是 | - | 名称 |
| sort | string | 是 | - | 排序 |
| note | string | 是 | - | 备注 |
| uuid | string | 是 | - | UUID |
| isIncreasing | bool? | 是 | - | 是否加价分组 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 280 报价参数 ( S_QuoteParameter )
- **业务含义**：报价参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| categoryId | int? | 是 | - | 报价类别 |
| groupId | int? | 是 | - | 报价分组 |
| parameterId | int? | 是 | - | 参数 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 281 客诉管理--扣款明细 ( S_ReturnSO )
- **业务含义**：客诉管理--扣款明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| contractId | int? | 是 | - | 销售合同表，对应S_Contract.recId |
| contractItemId | int? | 是 | - | 销售合同明细表，对应S_ContractItem.recId |
| contractSOId | int? | 是 | - | 销售订单表，对应S_ContractSO.recId |
| creditAmount | decimal? | 是 | - | 扣款金额 |
| creditMemoId | int? | 是 | - | 客户扣款，对应F_AR_CreditMemo.recId |
| customerId | int? | 是 | - | 客户(客体)，对应S_Customer.recId |
| debitMemoId | int? | 是 | - | - |
| exchRate | decimal? | 是 | - | 税率 |
| ifReconcile | bool? | 是 | - | 是否用于对账 |
| note | string | 是 | - | 备注 |
| packingSlipItemContractSOId | int? | 是 | - | - |
| packingSlipItemId | int? | 是 | - | - |
| price | decimal? | 是 | - | 含税单价 |
| qtyReturn | int? | 是 | - | 数量 |
| returnAmount | decimal? | 是 | - | 退货金额（含税金额） |
| supplierId | int? | 是 | - | 供应商(主体)，对应M_Suppliers.recId |
| totalAmount | decimal? | 是 | - | 总计金额（小计） |
| version | int? | 是 | - | - |
| complainmentId | int? | 是 | - | 客诉管理（退货，换货，扣款），对应S_Complainment.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| fromId | int? | 是 | - | 工厂，对应T_Plants.recId |
| providerId | int? | 是 | - | 对应T_Plants.recId |
| toId | int? | 是 | - | 对应T_Plants.recId |
| soReconcileId | string | 是 | - | 销售对账，对应F_AR_SOReconcile.recId |
| invoiceId | string | 是 | - | 销售发票，对应F_AR_Invoice.recId |
| reconcileId | string | 是 | - | - |
| apInvoiceId | string | 是 | - | - |
| taxRate | string | 是 | - | - |
| markupValue | string | 是 | - | - |
| upstatus | string | 是 | - | - |
- **关联关系**：
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

#### 282 报价单 ( S_Rfq )
- **业务含义**：报价单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| rfqNumber | string | 是 | - | 报价单号 |
| companyId | int? | 是 | - | 公司 |
| plantsId | int? | 是 | - | 工厂 |
| customerId | int? | 是 | - | 客户 |
| orderType | string | 是 | - | 订单类型 |
| businessManId | int? | 是 | - | 业务员 |
| jobId | int? | 是 | - | 生产编号 |
| salesPartId | int? | 是 | - | 本厂型号ID |
| partNum | string | 是 | - | 产品编码 |
| partName | string | 是 | - | 部件名称 |
| partRev | string | 是 | - | 生产编号版本 |
| endCustomerId | int? | 是 | - | 终端客户 |
| endCustomer | string | 是 | - | 终端客户 |
| endCustPartNum | string | 是 | - | 终端产品编号 |
| endCustPartDesc | string | 是 | - | 终端产品名称 |
| endCustPartRev | string | 是 | - | 终端产品版本 |
| custMatCode | string | 是 | - | 客户物料编码 |
| productGroupId | int? | 是 | - | 物料分组 |
| quoteCategoryId | int? | 是 | - | 报价分组 |
| projectName | string | 是 | - | 项目名称 |
| reference | string | 是 | - | 凭证摘要 |
| partNotes | string | 是 | - | 生产编号备注 |
| contactName | string | 是 | - | 订单联系人 |
| contactTel | string | 是 | - | 订单联系电话 |
| contactEmail | string | 是 | - | 订单联系邮箱 |
| techContactName | string | 是 | - | 技术联系人 |
| techContactTel | string | 是 | - | 技术联系人电话 |
| techContactEmail | string | 是 | - | 技术联系人邮箱 |
| currencyId | int? | 是 | - | 币种 |
| taxId | int? | 是 | - | 税种 |
| taxRate | decimal? | 是 | - | 税率 |
| fobId | int? | 是 | - | 贸易方式 |
| paymentTermId | int? | 是 | - | 付款周期 |
| paymentMethodId | int? | 是 | - | 付款方式 |
| shippingId | int? | 是 | - | 发货方式 |
| validityPeriod | DateTime? | 是 | - | 有效期 |
| scheduling | DateTime? | 是 | - | 排程 |
| salesUnitId | int? | 是 | - | 销售单元 |
| shippingLocation | string | 是 | - | 发货地点 |
| isGerber | bool? | 是 | - | Gerber |
| isArrayDrawing | bool? | 是 | - | Array Drawing |
| salesNotes | string | 是 | - | 特殊说明 |
| tradeTerms | string | 是 | - | 贸易条款 |
| note | string | 是 | - | 备注 |
| assignQuoteDate | DateTime? | 是 | - | 指派业务组日期 |
| assignCheckDate | DateTime? | 是 | - | 指派审核组日期 |
| assignEngineeringDate | DateTime? | 是 | - | 指派工程组日期 |
| backtoQuoteCheckDate | DateTime? | 是 | - | 返回业务组日期 |
| quoteFinishedDate | DateTime? | 是 | - | 报价完成日期 |
| assignTo | int? | 是 | - | - |
| assignStatus | int? | 是 | - | 指派状态 |
| feedback | string | 是 | - | 反馈 |
| feedbackNotes | string | 是 | - | 丢单备注 |
| exceedCapacityNote | string | 是 | - | 超能力备注 |
| feedbackNotes2 | string | 是 | - | 反馈备注 |
| status | string | 是 | - | 状态 |
| originalStatus | string | 是 | - | 原始状态 |
| flowTypeId | int? | 是 | - | 审批类型 |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| enableApproval | bool? | 是 | - | 提交审批 |
| approveStatus | string | 是 | - | 审批状态 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| creatorId | int? | 是 | - | 创建人 |
| createDate | DateTime? | 是 | - | 创建日期 |
| modifiedBy | string | 是 | - | 更新人员 |
| lastmodifydate | DateTime? | 是 | - | 更新时间 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 283 报价单额外费用 ( S_RfqAddCharge )
- **业务含义**：报价单额外费用
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| rfqId | int? | 是 | - | 报价单 |
| addtionalChargeId | int? | 是 | - | 额外费用 |
| amount | decimal? | 是 | - | 额外金额 |
| freeAmount | decimal? | 是 | - | 免收金额 |
| reference | string | 是 | - | 凭证摘要 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 284 报价单审批历史 ( S_RfqHistory )
- **业务含义**：报价单审批历史
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId |
| approveVersion | int? | 是 | - | 审批版本 |
| executionId | string | 是 | - | - |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskRegainId | string | 是 | - | - |
| businessCode | string | 是 | - | 业务代码 |
| business | string | 是 | - | 业务 |
| businessForm | string | 是 | - | 业务表单 |
| suggest | string | 是 | - | 建议 |
| flowDesc | string | 是 | - | 流程说明 |
| taskFrom | string | 是 | - | 任务表单 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| endTime | DateTime? | 是 | - | 结束时间 |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| myAction | bool? | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| postRoleIds | string | 是 | - | 岗位列表 |
| rfqId | int? | 是 | - | 报价单 |
| myId | int? | 是 | - | 审批人 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 285 报价单参数 ( S_RfqParameter )
- **业务含义**：报价单参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| rfqId | int? | 是 | - | 报价单 |
| parameterId | int? | 是 | - | 参数 |
| groupName | string | 是 | - | 分组名称 |
| groupSort | string | 是 | - | 分组排序 |
| dataType | string | 是 | - | 数据类型 |
| parameterValue | string | 是 | - | 参数值 |
| listVal | string | 是 | - | 参数值 |
| textValue | string | 是 | - | 文本值 |
| intValue | int? | 是 | - | 整数值 |
| floatValue | decimal? | 是 | - | 浮点值 |
| boolValue | bool? | 是 | - | 布尔值 |
| dateValue | DateTime? | 是 | - | 日期值 |
| isIncreasing | bool? | 是 | - | 是否加价参数 |
| isPercent | bool? | 是 | - | 是否百分比加价 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 286 报价单审批 ( S_RfqWF )
- **业务含义**：报价单审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId |
| approveVersion | int? | 是 | - | 审批版本 |
| executionId | string | 是 | - | - |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskRegainId | string | 是 | - | - |
| businessCode | string | 是 | - | 业务代码 |
| business | string | 是 | - | 业务 |
| businessForm | string | 是 | - | 业务表单 |
| suggest | string | 是 | - | 建议 |
| flowDesc | string | 是 | - | 流程说明 |
| taskFrom | string | 是 | - | 任务表单 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| endTime | DateTime? | 是 | - | 结束时间 |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| myAction | bool? | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| postRoleIds | string | 是 | - | 岗位列表 |
| rfqId | int? | 是 | - | 报价单 |
| myId | int? | 是 | - | 审批人 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 287 S_Rpt_Member ( S_Rpt_Member )
- **业务含义**：ERP 系统 S_Rpt_Member 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 表主键 |
| version | string | 是 | - | - |
| parentId | string | 是 | - | 销售代表ID，对应S_Rpt_SalesRepresentative.recId |
| userId | string | 是 | - | 雇员ID，对应S_BusinessMan.recId |
| code | string | 是 | - | 编号 |
| name | string | 是 | - | 名称 |
- **关联关系**：
  - S_Rpt_Member.parentId = S_Rpt_SalesRepresentative.recId
  - S_Rpt_Member.userId = S_BusinessMan.recId

---

#### 288 S_Rpt_SalesRepresentative ( S_Rpt_SalesRepresentative )
- **业务含义**：ERP 系统 S_Rpt_SalesRepresentative 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 表主键 |
| parentNo | string | 是 | - | 父级编号 |
| version | string | 是 | - | - |
| code | string | 是 | - | 销售代表编号 |
| name | string | 是 | - | 销售代表中文名 |
| englishName | string | 是 | - | 销售代表英文名 |
| plantId | string | 是 | - | 工厂ID，对应T_Plants.recId |
| userId | string | 是 | - | 雇员ID，对应S_BusinessMan.recId |
| type | string | 是 | - | 类别(1.组织；2.个人) |
| isExceedTime | string | 是 | - | 是否过期(1.过期；2.正常) |
| phone | string | 是 | - | 电话 |
| telexNumber | string | 是 | - | 电传号码 |
| portraiture | string | 是 | - | 传真号码 |
| postalCode | string | 是 | - | 邮政编码 |
| address | string | 是 | - | 地址 |
| uniqueid | string | 是 | - | 刷新树节点ID |
- **关联关系**：
  - S_Rpt_SalesRepresentative.plantId = T_Plants.recId
  - S_Rpt_SalesRepresentative.userId = S_BusinessMan.recId

---

#### 289 销售项目 ( S_SaleProject )
- **业务含义**：销售项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| modifiedBy | string | 是 | - | 更新人员 |
| name | string | 是 | - | 名称 |
| suffix | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 290 销售预测 ( S_SalesForecast )
- **业务含义**：销售预测
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| area | decimal? | 是 | - | 订单面积 |
| contactEmail | string | 是 | - | 订单联系面积 |
| contactName | string | 是 | - | 订单联系人 |
| contactTel | string | 是 | - | 订单联系电话 |
| createDate | DateTime? | 是 | - | 建单日期 |
| custForecastNumber | string | 是 | - | 客户订单号 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| forecastNumber | string | 是 | - | 销售预测号 |
| note | string | 是 | - | 备注 |
| priceInTax | decimal? | 是 | - | 含税单价 |
| qtyOrdered | int? | 是 | - | 订单数量 |
| qtyScheduling | int? | 是 | - | 排产数量 |
| quantity | int? | 是 | - | 预测数量 |
| shippingAdress | string | 是 | - | 送货地址 |
| shippingContactEmail | string | 是 | - | 送货联系邮箱 |
| shippingContactName | string | 是 | - | 送货联系人 |
| shippingContactTel | string | 是 | - | 送货联系电话 |
| status | string | 是 | - | 单据状态；Active 有效 Close 关闭 |
| taxAmount | decimal? | 是 | - | 税金 |
| taxRate | decimal? | 是 | - | 税率 |
| totalInTax | decimal? | 是 | - | 含税金额 |
| totalNoTax | decimal? | 是 | - | 不含税金额 |
| type | string | 是 | - | 单据类型；Standard 标准  Consignment 寄售 Sample 样板 |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| fobId | int? | 是 | - | 贸易方式，对应T_FOB.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| paymentMethodId | int? | 是 | - | 付款方式，对应T_PaymentMethod.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| postRoleId | int? | 是 | - | 工厂，对应T_PostRole.recId |
| salesPartId | int? | 是 | - | 部件参数，对应S_SalesParts.recId |
| shippingId | int? | 是 | - | 运输方式，对应T_Shipping.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| taxId | int? | 是 | - | 税率 |
| shippingAdressId | int? | 是 | - | 发货地址 |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId |
| approveVersion | int? | 是 | - | 审批版本 |
| originalStatus | string | 是 | - | 原始状态 |
| approveStatus | string | 是 | - | 审批状态 |
| enableApproval | bool? | 是 | - | 是否启用审批 |
| flowTypeId | int? | 是 | - | 审批类型 |
| sfVer | string | 是 | - | 分单版本 |
| canSchedule | bool? | 是 | - | - |
| readyMaterial | bool? | 是 | - | - |
| isHistory | bool? | 是 | - | - |
| forecastPeriodId | int? | 是 | - | 预测期间 |
| startPeriodId | int? | 是 | - | 开始期间 |
| isImportWitCustCode | bool? | 是 | - | - |
| importFilename | string | 是 | - | 导入文件名 |
| importUuid | string | 是 | - | 导入Uuid |
| importFlag | int? | 是 | - | 导入标记 |
| orderSplitVer | int? | 是 | - | - |
- **关联关系**：
  - S_SalesForecast.companyId = T_Company.recId
  - S_SalesForecast.creatorId = T_User.recId
  - S_SalesForecast.currencyId = T_Currency.recId
  - S_SalesForecast.customerId = S_Customer.recId
  - S_SalesForecast.fobId = T_FOB.recId
  - S_SalesForecast.jobId = S_Job.recId
  - S_SalesForecast.paymentMethodId = T_PaymentMethod.recId
  - S_SalesForecast.paymentTermId = T_PaymentTerm.recId
  - S_SalesForecast.postRoleId = T_PostRole.recId
  - S_SalesForecast.salesPartId = S_SalesParts.recId
  - S_SalesForecast.shippingId = T_Shipping.recId
  - S_SalesForecast.unitId = T_Unit.recId

---

#### 291 销售预测审批历史 ( S_SalesForecastHistory )
- **业务含义**：销售预测审批历史
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId |
| approveVersion | int? | 是 | - | 审批版本 |
| executionId | string | 是 | - | - |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskRegainId | string | 是 | - | - |
| businessCode | string | 是 | - | 业务代码 |
| business | string | 是 | - | 业务 |
| businessForm | string | 是 | - | 业务表单 |
| suggest | string | 是 | - | 建议 |
| flowDesc | string | 是 | - | 流程说明 |
| taskFrom | string | 是 | - | 任务表单 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| endTime | DateTime? | 是 | - | 结束时间 |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| myAction | bool? | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| postRoleIds | string | 是 | - | 岗位列表 |
| salesForecastId | int? | 是 | - | 销售预测 |
| myId | int? | 是 | - | 审批人 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 292 销售预测明细 ( S_SalesForecastItem )
- **业务含义**：销售预测明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| note | string | 是 | - | 备注 |
| qtyScheduling | int? | 是 | - | 计划数量 |
| quantity | int? | 是 | - | 数量 |
| requestedDate | DateTime? | 是 | - | 需求日期 |
| version | int? | 是 | - | 记录版本 |
| salesForecastId | int? | 是 | - | 销售预测，对应S_SalesForecast.recId |
| jobId | int? | 是 | - | 生产编号 |
| salesPartId | int? | 是 | - | 销售部件 |
| priceNoTax | decimal? | 是 | - | 不含税价格 |
| serialNo | int? | 是 | - | 序号 |
| priceInTax | decimal? | 是 | - | 含税价格 |
- **关联关系**：
  - S_SalesForecastItem.salesForecastId = S_SalesForecast.recId

---

#### 293 销售预测分单 ( S_SalesForecastSplitting )
- **业务含义**：销售预测分单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| serialNo | int? | 是 | - | 序号 |
| planDelivery | DateTime? | 是 | - | 计划交期 |
| dailyQuantity | int? | 是 | - | 数量 |
| ifFullProcess | bool? | 是 | - | 全制程 |
| plantsId | int? | 是 | - | 工厂 |
| lastRevisedBy | int? | 是 | - | - |
| lastUpdateTime | DateTime? | 是 | - | 最后修改时间 |
| notes | string | 是 | - | 备注 |
| salesForecastItemId | int? | 是 | - | 销售预测 |
| salesForecastId | int? | 是 | - | 销售预测 |
| version | int? | 是 | - | 记录版本 |
| qtyOrdered | int? | 是 | - | 订单数量 |
- **关联关系**：无

---

#### 294 销售预测审批 ( S_SalesForecastWF )
- **业务含义**：销售预测审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| piId | string | 是 | - | 审批流piId |
| pdId | string | 是 | - | 审批流pdId |
| approveVersion | int? | 是 | - | 审批版本 |
| executionId | string | 是 | - | - |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskRegainId | string | 是 | - | - |
| businessCode | string | 是 | - | 业务代码 |
| business | string | 是 | - | 业务 |
| businessForm | string | 是 | - | 业务表单 |
| suggest | string | 是 | - | 建议 |
| flowDesc | string | 是 | - | 流程说明 |
| taskFrom | string | 是 | - | 任务表单 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| endTime | DateTime? | 是 | - | 结束时间 |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| myAction | bool? | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| postRoleIds | string | 是 | - | 岗位列表 |
| salesForecastId | int? | 是 | - | 销售预测 |
| myId | int? | 是 | - | 审批人 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 295 销售部件 ( S_SalesParts )
- **业务含义**：销售部件
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| culayers | int? | 是 | - | 层数 |
| delivery_X | int? | 是 | - | 交付形式X |
| delivery_Y | int? | 是 | - | 交付形式Y |
| drills | int? | 是 | - | 钻带 |
| endCustPartDesc | string | 是 | - | 终端产品名称 |
| endCustPartNum | string | 是 | - | 终端产品编号 |
| endCustPartRev | string | 是 | - | 终端产品版本 |
| endCustomer | string | 是 | - | 终端客户 |
| ifActive | bool? | 是 | - | 是否激活 |
| ifSets | bool? | 是 | - | 是否用于Sets |
| jobSpec | string | 是 | - | 描述 |
| legendbot | int? | 是 | - | 底层文字 |
| legendtop | int? | 是 | - | 顶层文字 |
| minOrderAmount | decimal? | 是 | - | 最小订单金额 |
| minOrderArea | decimal? | 是 | - | 最小订单面积 |
| minOrderQty | decimal? | 是 | - | 最小订单数 |
| note | string | 是 | - | 备注 |
| productHight | decimal? | 是 | - | 高 |
| productLen | decimal? | 是 | - | 长 |
| productWid | decimal? | 是 | - | 宽 |
| routs | int? | 是 | - | - |
| salesPartBOMId | int? | 是 | - | AdditionalBOM，对应S_SalesPartsAdditionalBOM.recId |
| salesPartName | string | 是 | - | 客户型号 |
| salesPartNum | string | 是 | - | 本厂型号(销售部件号) |
| salespartRev | string | 是 | - | 版本 |
| setQty | int? | 是 | - | 单元拼板数 |
| smbot | int? | 是 | - | 底层阻焊 |
| smtop | int? | 是 | - | 顶层阻焊 |
| status | string | 是 | - | Valid 有效 New，对应作废.recId |
| type | string | 是 | - | 类型 ： Sample 样板 Batch 批量 Other 其它 MGSuit 套版主板 SubSuit 套版子板MGSuitSample套板主板样板Semifinished半自制SubSuitSample套板子版样版 |
| unitWeight | decimal? | 是 | - | 重量 |
| version | int? | 是 | - | - |
| xoutQty | int? | 是 | - | 最大叉板数 |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| productGroupId | int? | 是 | - | 产品分组，对应S_ProductGroup.recId |
| projectCombinationId | int? | 是 | - | 销售数据--项目组合，对应S_ProjectCombination.recId |
| appCategoryId | string | 是 | - | 销售数据--产品分类，对应S_ProductCategory.recId |
| salesUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| productGradeId | string | 是 | - | P_MO，对应T_Cate.recId |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| createDate | DateTime? | 是 | - | 制单日期 |
| ifCreateJob | bool? | 是 | - | 是否生成同名生产编号 |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| custMatCode | string | 是 | - | 客户物料编码 |
| endCustomerId | string | 是 | - | 终端客户，对应S_Customer.recId |
| cartonGrossWeight | string | 是 | - | 箱包毛重 |
| cartonNetWeight | string | 是 | - | 箱包净重 |
| isModelRiskPlaceOrder | string | 是 | - | 是否型号风险下单 |
| isModelRiskShipment | string | 是 | - | 是否型号风险出货 |
| isMarketRiskPlaceOrder | string | 是 | - | 是否市场风险下单 |
| isMarketRiskShipment | string | 是 | - | 是否市场风险出货 |
| halogenFree | string | 是 | - | 0有卤，1无卤素 |
| surface | string | 是 | - | 表面处理 |
| soldermask | string | 是 | - | 阻焊颜色 |
| legendColor | string | 是 | - | 字符颜色 |
| archiveStatus | string | 是 | - | 0:建档中 ;1:待MI;2:MI制作中；3：退回建档 ；4：已完成。 |
- **关联关系**：
  - S_SalesParts.salesPartBOMId = S_SalesPartsAdditionalBOM.recId
  - S_SalesParts.status = 作废.recId
  - S_SalesParts.customerId = S_Customer.recId
  - S_SalesParts.productGroupId = S_ProductGroup.recId
  - S_SalesParts.projectCombinationId = S_ProjectCombination.recId
  - S_SalesParts.appCategoryId = S_ProductCategory.recId
  - S_SalesParts.salesUnitId = T_Unit.recId
  - S_SalesParts.productGradeId = T_Cate.recId
  - S_SalesParts.creatorId = T_User.recId
  - S_SalesParts.jobId = S_Job.recId
  - S_SalesParts.endCustomerId = S_Customer.recId

---

#### 296 销售部件--AdditionalBOM ( S_SalesPartsAdditionalBOM )
- **业务含义**：销售部件--AdditionalBOM
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bomQTY | decimal? | 是 | - | BOM数量 |
| version | int? | 是 | - | - |
| bomUnitId | int? | 是 | - | BOM单位，对应T_Unit.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
- **关联关系**：
  - S_SalesPartsAdditionalBOM.bomUnitId = T_Unit.recId
  - S_SalesPartsAdditionalBOM.materialsId = M_Materials.recId
  - S_SalesPartsAdditionalBOM.salesPartsId = S_SalesParts.recId
  - S_SalesPartsAdditionalBOM.stockUnitId = T_Unit.recId

---

#### 297 销售部件层信息表 ( S_SalesPartsLayers )
- **业务含义**：销售部件层信息表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| copperDesity | decimal? | 是 | - | 残铜率 |
| cuArea | decimal? | 是 | - | 铜面积 |
| endLayer | string | 是 | - | 结束层 |
| hoesCuSpec | string | 是 | - | 孔铜要求 |
| holesQty | decimal? | 是 | - | 孔数 |
| impedanceFlag | bool? | 是 | - | 是否用于阻抗 |
| layerName | string | 是 | - | 层名 |
| layerType | string | 是 | - | 层类型 |
| materialTyepId | int? | 是 | - | 物料类型，对应S_MaterialType.recId |
| minDribit | decimal? | 是 | - | 最小钻嘴 |
| minLine | decimal? | 是 | - | 最小线宽 |
| minLinetoPad | decimal? | 是 | - | 最小线到盘 |
| minPadtoPad | decimal? | 是 | - | 最小孔距 |
| minSpec | decimal? | 是 | - | 最少线距 |
| openQty | decimal? | 是 | - | 开窗数 |
| seq | int? | 是 | - | 序号 |
| startLayer | string | 是 | - | 开始层 |
| surfaceArea | decimal? | 是 | - | 暴露面积 |
| version | int? | 是 | - | - |
| baseCopperId | int? | 是 | - | 基铜(铜厚表)，对应S_Conductor.recId |
| finishCopperId | int? | 是 | - | 完成铜厚，对应S_Conductor.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
- **关联关系**：
  - S_SalesPartsLayers.materialTyepId = S_MaterialType.recId
  - S_SalesPartsLayers.baseCopperId = S_Conductor.recId
  - S_SalesPartsLayers.finishCopperId = S_Conductor.recId
  - S_SalesPartsLayers.salesPartsId = S_SalesParts.recId

---

#### 298 销售部件对应产品分组参数值 ( S_SalesPartsParameter )
- **业务含义**：销售部件对应产品分组参数值
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | 下拉选择 SelectItem  文本 TextItem |
| dataType | string | 是 | - | 日期类型 |
| dateValue | DateTime? | 是 | - | 日期数据 |
| floatValue | decimal? | 是 | - | 浮点数据、 |
| intValue | int? | 是 | - | 整数数据 |
| listVal | string | 是 | - | 下拉数据 |
| parameterValue | string | 是 | - | - |
| sort | string | 是 | - | - |
| textValue | string | 是 | - | 参数值 |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 销售数据--参数管理，对应S_Parameters.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
- **关联关系**：
  - S_SalesPartsParameter.parametersId = S_Parameters.recId
  - S_SalesPartsParameter.salesPartsId = S_SalesParts.recId

---

#### 299 销售部件对应套板信息 ( S_SalesPartsSets )
- **业务含义**：销售部件对应套板信息
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| nested_Desc | string | 是 | - | 套板名称 |
| nested_Len | decimal? | 是 | - | 长度 |
| nested_PN | string | 是 | - | 套板编号 |
| nested_Rev | string | 是 | - | 版本 |
| nested_Wid | decimal? | 是 | - | 宽度 |
| qty | int? | 是 | - | 数量 |
| version | int? | 是 | - | - |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
- **关联关系**：
  - S_SalesPartsSets.salesPartsId = S_SalesParts.recId

---

#### 300 销售部件对应PCBA材料单 ( S_SalesPartsSMTBOM )
- **业务含义**：销售部件对应PCBA材料单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bodyIdentification | string | 是 | - | 本体标识 |
| bomRemark | string | 是 | - | BOM备注 |
| custBomQty | decimal? | 是 | - | 数量 |
| custLocationId | string | 是 | - | - |
| custMatCode | string | 是 | - | - |
| custMatName | string | 是 | - | - |
| custMatSpec | string | 是 | - | - |
| direction | string | 是 | - | 方向 |
| itemNo | string | 是 | - | 位号 |
| materialCategory | string | 是 | - | 物料类别 |
| note | string | 是 | - | 备注 |
| priority | string | 是 | - | - |
| version | int? | 是 | - | - |
| custUnitId | int? | 是 | - | 对应T_Unit.recId |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
- **关联关系**：
  - S_SalesPartsSMTBOM.custUnitId = T_Unit.recId
  - S_SalesPartsSMTBOM.materialsId = M_Materials.recId
  - S_SalesPartsSMTBOM.processId = T_Process.recId
  - S_SalesPartsSMTBOM.salesPartsId = S_SalesParts.recId
  - S_SalesPartsSMTBOM.suppliersId = M_Suppliers.recId

---

#### 301 销售订单更改记录 ( S_SalesPlanReview )
- **业务含义**：销售订单更改记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| changeNum | int? | 是 | - | - |
| desDelivery | DateTime? | 是 | - | 修改后的计划交期 |
| desQuantity | int? | 是 | - | 修改后的数量 |
| note | string | 是 | - | 备注 |
| oriDelivery | DateTime? | 是 | - | 原来的计划交期 |
| oriQuantity | int? | 是 | - | 原来的数量 |
| version | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 销售合同明细表，对应S_ContractItem.recId |
| quantity | int? | 是 | ((0)) | 现在的数量 |
| delivery | DateTime? | 是 | - | 现在的计划交期(回复交期) |
| ocnId | int? | 是 | - | - |
| qtyOfPnls | int? | 是 | ((0)) | - |
| ocnQuantity | int? | 是 | ((0)) | - |
| ocnDelivery | DateTime? | 是 | - | - |
| orderDate | DateTime? | 是 | - | 客户交期 |
| ocndesDelivery | DateTime? | 是 | - | - |
- **关联关系**：
  - S_SalesPlanReview.contractItemId = S_ContractItem.recId

---

#### 302 撤销出货表 ( S_ShipmentRevoke )
- **业务含义**：撤销出货表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | 制单日期 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| packingSlipItemId | int? | 是 | - | 成品送货明细表，对应FGI_PackingSlipItem.recId |
| note | string | 是 | - | 备注 |
| qtyofArray | int? | 是 | - | SET |
| qtyofPCS | int? | 是 | - | PCS |
| checkDate | DateTime? | 是 | - | 审核时间 |
| checkNote | string | 是 | - | 审核备注 |
| status | string | 是 | - | 单据状态：TOCheck 待核准  Checked 已核准 |
| checkorId | int? | 是 | - | 审核人，对应T_User.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
- **关联关系**：
  - S_ShipmentRevoke.creatorId = T_User.recId
  - S_ShipmentRevoke.packingSlipItemId = FGI_PackingSlipItem.recId
  - S_ShipmentRevoke.checkorId = T_User.recId
  - S_ShipmentRevoke.customerId = S_Customer.recId

---

#### 303 订单装运表 ( S_SODayShipment )
- **业务含义**：订单装运表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| date | DateTime? | 是 | - | 装运日期 |
| qtyOfArea | decimal? | 是 | - | SET |
| qtyOfPCS | int? | 是 | - | PCS |
| version | int? | 是 | - | - |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
- **关联关系**：
  - S_SODayShipment.plantsId = T_Plants.recId

---

#### 304 备货冲销记录 ( S_SOMatWriteOff )
- **业务含义**：备货冲销记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 305 成品盘点表 ( S_StockCheck )
- **业务含义**：成品盘点表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checkDate | DateTime? | 是 | - | 盘点日期 |
| code | string | 是 | - | 盘点代码 |
| ifCheck0 | bool? | 是 | - | 是否零库存盘点 |
| locked | bool? | 是 | - | 是否锁定 |
| name | string | 是 | - | 名称 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 状态;Open 打开 Close 关闭 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 盘点人员，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
- **关联关系**：
  - S_StockCheck.creatorId = T_User.recId
  - S_StockCheck.fiscalPeriodId = T_FiscalPeriod.recId
  - S_StockCheck.postRoleId = T_PostRole.recId
  - S_StockCheck.warehouseId = T_Warehouse.recId

---

#### 306 成品盘点明细表 ( S_StockCheckItem )
- **业务含义**：成品盘点明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checkQtyOfArray | int? | 是 | - | 盘点SET |
| checkQtyOfUnit | int? | 是 | - | 盘点PCS |
| sysQtyOfArray | int? | 是 | - | 系统SET |
| sysQtyOfUnit | int? | 是 | - | 系统PCS |
| version | int? | 是 | - | - |
| fgiInventoryId | int? | 是 | - | 成品库存，对应FGI_Inventory.recId |
| inventoryCheckReasonId | int? | 是 | - | 盘点原因，对应T_InventoryCheckReason.recId |
| stockCheckId | int? | 是 | - | 成品盘点，对应S_StockCheck.recId |
- **关联关系**：
  - S_StockCheckItem.fgiInventoryId = FGI_Inventory.recId
  - S_StockCheckItem.inventoryCheckReasonId = T_InventoryCheckReason.recId
  - S_StockCheckItem.stockCheckId = S_StockCheck.recId

---

#### 307 工作计划表 ( S_WorkPlan )
- **业务含义**：工作计划表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| enableApproval | bool? | 是 | - | - |
| enterDate | DateTime? | 是 | - | - |
| name | string | 是 | - | - |
| note | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| type | string | 是 | - | WorkPlan |
| version | int? | 是 | - | - |
| weekDate | DateTime? | 是 | - | - |
| businessManId | int? | 是 | - | 对应S_BusinessMan.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| flowTypeId | int? | 是 | - | 审批流程，对应T_FlowType.recId |
- **关联关系**：
  - S_WorkPlan.businessManId = S_BusinessMan.recId
  - S_WorkPlan.companyId = T_Company.recId
  - S_WorkPlan.creatorId = T_User.recId
  - S_WorkPlan.flowTypeId = T_FlowType.recId

---

#### 308 工作计划明细表 ( S_WorkPlanItem )
- **业务含义**：工作计划明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| ideas | string | 是 | - | - |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| weekCode | int? | 是 | - | - |
| workSite | string | 是 | - | - |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| workPlanId | int? | 是 | - | 工作计划，对应S_WorkPlan.recId |
- **关联关系**：
  - S_WorkPlanItem.customerId = S_Customer.recId
  - S_WorkPlanItem.workPlanId = S_WorkPlan.recId

---

#### 309 工作计划审批记录表 ( S_WorkPlantHistory )
- **业务含义**：工作计划审批记录表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| workPlanId | int? | 是 | - | 对应S_WorkPlan.recId |
- **关联关系**：
  - S_WorkPlantHistory.myId = T_User.recId
  - S_WorkPlantHistory.workPlanId = S_WorkPlan.recId

---

#### 310 S_WorkPlantWF ( S_WorkPlantWF )
- **业务含义**：ERP 系统 S_WorkPlantWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| workPlanId | int? | 是 | - | 对应S_WorkPlan.recId |
- **关联关系**：
  - S_WorkPlantWF.myId = T_User.recId
  - S_WorkPlantWF.workPlanId = S_WorkPlan.recId

---

### 2.6 生产模块

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 311 BOM领料批次 ( P_BOMBatching )
- **业务含义**：BOM领料批次
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bomPicklistItemId | int? | 是 | - | BOM领料明细表，对应M_BOMPicklistItem.recId |
| qtyIssued | decimal? | 是 | - | 发料数量 |
| qtyPicking | decimal? | 是 | - | 领料数量 |
| qtyReq | decimal? | 是 | - | 需求数量 |
| version | int? | 是 | - | - |
| mfgPartId | int? | 是 | - | 型号部件表，对应E_JobMfgParts.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| moId | int? | 是 | - | 制造单号，对应P_MO.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| stockUnitId | int? | 是 | - | 入库单位，对应T_Unit.recId |
| warehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| contractItemId | int? | 是 | - | 合同制造明细（没值，勿用），对应S_ContractItem.recId |
| qtyHairBack | decimal? | 是 | - | - |
| qty_Alloc | decimal? | 是 | ((0)) | - |
| materialsCostByPlantId | int? | 是 | - | 对应M_MaterialsCostByPlant.recId |
| orderCode | string | 是 | - | 订单单号（制造单号） |
| qty_Alloc2 | decimal? | 是 | ((0)) | - |
- **关联关系**：
  - P_BOMBatching.bomPicklistItemId = M_BOMPicklistItem.recId
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

#### 312 OCN\ECN管理 ( P_ECN )
- **业务含义**：OCN\ECN管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveStatus | string | 是 | - | 审批状态 |
| approveVersion | int? | 是 | - | 审批版本 |
| contents | string | 是 | - | 内容 |
| createDate | DateTime? | 是 | - | 创建日期 |
| delivery1 | DateTime? | 是 | - | 处理时间1 |
| delivery2 | DateTime? | 是 | - | 处理时间2 |
| delivery3 | DateTime? | 是 | - | 处理时间3 |
| delivery4 | DateTime? | 是 | - | 处理时间4 |
| delivery5 | DateTime? | 是 | - | 处理时间5 |
| desDelivery | DateTime? | 是 | - | 新交期 |
| desQuantity | int? | 是 | - | 新数量 |
| ecnNumber | string | 是 | - | OCN/ECN单号 |
| ecnType | string | 是 | - | 类型；OUT 外部 IN ：内部 |
| enableApproval | bool? | 是 | - | 是否启用审批 |
| ifCancel | bool? | 是 | - | 是否取消 |
| ifDelivery | bool? | 是 | - | 是否交期 |
| ifMI | bool? | 是 | - | 是否工程设计 |
| ifOnhold | bool? | 是 | - | 是否计划暂停 |
| ifOnline | bool? | 是 | - | 是否在线板 |
| ifPayfor | bool? | 是 | - | 是否赔偿 |
| ifQuantity | bool? | 是 | - | - |
| ifSplitDelivery | bool? | 是 | - | - |
| ifStock | bool? | 是 | - | 是否库存板 |
| ifTool | bool? | 是 | - | 是否工具 |
| miChangeType | string | 是 | - | 变更类型；ExistingVersion: 现有版本
UpgradeJOB: 升级生产编号
UpgradeSalesPart：升级销售部件 |
| miChanges | string | 是 | - | 工程设计处理意见 |
| miDate | DateTime? | 是 | - | 处理时间 |
| miNotes | string | 是 | - | 处理备注 |
| newPartName | string | 是 | - | 新型号名称 |
| newPartNum | string | 是 | - | 新型号编号 |
| newPartRev | string | 是 | - | 新版本号 |
| newSalesPartName | string | 是 | - | 新销售名称 |
| newSalesPartNum | string | 是 | - | 新销售编号 |
| newSalesPartRev | string | 是 | - | 新销售版本号 |
| notes | string | 是 | - | 备注 |
| ocnChanges | string | 是 | - | OCN处理意见 |
| ocnDate | DateTime? | 是 | - | OCN处理日期 |
| onlineChanges | string | 是 | - | 在线板处理意见 |
| onlineDate | DateTime? | 是 | - | 在线板处理日期 |
| onlineNotes | string | 是 | - | 在线板备注 |
| orderPrice | decimal? | 是 | - | 订单单价 |
| oriDelivery | DateTime? | 是 | - | 原交期 |
| oriQuantity | int? | 是 | - | 原数量 |
| originalStatus | string | 是 | - | 原始状态 |
| payforAmount | decimal? | 是 | - | 赔偿金额 |
| payforChanges | string | 是 | - | 赔偿意见 |
| payforDate | DateTime? | 是 | - | 赔偿处理日期 |
| payforNotes | string | 是 | - | 赔偿备注 |
| payforReasons | string | 是 | - | 赔偿原因 |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| quantity1 | int? | 是 | - | - |
| quantity2 | int? | 是 | - | - |
| quantity3 | int? | 是 | - | - |
| quantity4 | int? | 是 | - | - |
| quantity5 | int? | 是 | - | - |
| reasons | string | 是 | - | 原因 |
| status | string | 是 | - | 状态 |
| stockChanges | string | 是 | - | 库存板处理意见 |
| stockDate | DateTime? | 是 | - | 库存板处理日期 |
| stockNotes | string | 是 | - | 库存板备注 |
| subject | string | 是 | - | 主题 |
| toolChanges | string | 是 | - | 工具更改要求 |
| toolDate | DateTime? | 是 | - | 工具处理日期 |
| toolNotes | string | 是 | - | 工具备注 |
| type | string | 是 | - | 类型；ECN / OCN |
| uuid | string | 是 | - | UUID |
| version | int? | 是 | - | 记录版本 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| contractSOId | int? | 是 | - | 销售订单业务，对应S_ContractSO.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 审批类型，对应T_FlowType.recId |
| jobId | int? | 是 | - | 生产编号，对应S_Job.recId |
| miUserId | int? | 是 | - | MI执行人员，对应T_User.recId |
| ocnUserId | int? | 是 | - | OCN执行人员，对应T_User.recId |
| onlineUserId | int? | 是 | - | 在线板执行人员，对应T_User.recId |
| payforUserId | int? | 是 | - | 赔偿执行人员，对应T_User.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| salesPartsId | int? | 是 | - | 销售部件，对应S_SalesParts.recId |
| stockUserId | int? | 是 | - | 库存板执行人员，对应T_User.recId |
| toolUserId | int? | 是 | - | 工具执行人员，对应T_User.recId |
| ocnChangeType | string | 是 | ('') | 更改类型 |
| ifUpdateRev | bool? | 是 | ((0)) | - |
| ifOldRevSend | bool? | 是 | ((0)) | - |
| orderOldPrice | decimal? | 是 | ((0)) | 订单原价 |
| actionStatus | string | 是 | ('None') | - |
| newJobId | int? | 是 | - | 新生产编号 |
| newSalesPartId | int? | 是 | - | 新销售部件 |
| oldRevDo | string | 是 | - | 旧版本 |
| oldRevNote | string | 是 | - | 旧版备注 |
| infoType | string | 是 | - | 资料类型 |
| changeProject | string | 是 | - | 变更项目 |
| miIdea | string | 是 | - | 工程意见 |
| instructions | string | 是 | - | 工程指示 |
| qtyOnline | int? | 是 | - | 在线数量 |
| qtyStock | int? | 是 | - | 库存数量 |
| xout | int? | 是 | - | 单废 |
| actionDate | DateTime? | 是 | - | 执行日期 |
| changeGrade | string | 是 | - | 变更等级 |
| mfg | string | 是 | - | 评审 |
| mfgNotes | string | 是 | - | 备注 |
| mfgDate | DateTime? | 是 | - | 处理时间 |
| mfgUserId | int? | 是 | - | - |
| qc | string | 是 | - | 评审 |
| qcNotes | string | 是 | - | 备注 |
| qcDate | DateTime? | 是 | - | 处理时间 |
| qcUserId | int? | 是 | - | - |
| pmc | string | 是 | - | 评审 |
| pmcNotes | string | 是 | - | 备注 |
| pmcDate | DateTime? | 是 | - | 处理时间 |
| pmcUserId | int? | 是 | - | - |
| sop | string | 是 | - | - |
| cp | string | 是 | - | - |
| tecNotes | string | 是 | - | 备注 |
| tecDate | DateTime? | 是 | - | 处理时间 |
| tecUserId | int? | 是 | - | - |
| fmea | string | 是 | - | - |
| onholdWOLogs | string | 是 | - | 暂缓工单 |
| newCustomerId | int? | 是 | - | 新客户 |
| newType | string | 是 | - | 新类型 |
| custMatCode | string | 是 | - | 客户物料编码 |
| importData | bool? | 是 | - | 导入日期 |
| actionDone | bool? | 是 | - | - |
| productGroupId | int? | 是 | - | 产品分组 |
| newProductGroupId | int? | 是 | - | 新产品分组 |
| effectiveMethod | int? | 是 | - | 生效方式 |
| isSampleToBatch | bool? | 是 | - | 样板转批量 |
- **关联关系**：
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

#### 313 OCN\ECN管理-审批记录 ( P_ECNHistory )
- **业务含义**：OCN\ECN管理-审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 审批版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 流程说明 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 建议 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务表单 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| ecnId | int? | 是 | - | OCN/ECN，对应P_ECN.recId |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
- **关联关系**：
  - P_ECNHistory.ecnId = P_ECN.recId
  - P_ECNHistory.myId = T_User.recId

---

#### 314 OCN\ECN管理-工具-工具类型 ( P_ECNLog )
- **业务含义**：OCN\ECN管理-工具-工具类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| createTime | DateTime? | 是 | - | 记录版本 |
| ecnId | int? | 是 | - | 代码，对应P_ECN.recId |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | 记录版本 |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
- **关联关系**：
  - P_ECNLog.ecnId = P_ECN.recId
  - P_ECNLog.creatorId = T_User.recId

---

#### 315 OCN\ECN审核 ( P_ECNTool )
- **业务含义**：OCN\ECN审核
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| handleDate | DateTime? | 是 | - | - |
| handleWay | string | 是 | - | 处理方式 |
| notes | string | 是 | - | 备注 |
| version | int? | 是 | - | 记录版本 |
| ecnId | int? | 是 | - | OCN/ECN |
| handleUserId | int? | 是 | - | - |
| toolTypeId | int? | 是 | - | 工具类型 |
| miToolNameId | int? | 是 | - | MI工具名称 |
| partNum | string | 是 | - | 更改前编号 |
| partNum2 | string | 是 | - | 更改后编号 |
| partRev | string | 是 | - | 更改前版本 |
| partRev2 | string | 是 | - | 更改后版本 |
| upgradeFlag | bool? | 是 | - | 升级版本 |
- **关联关系**：无

---

#### 316 OCN/ECN审批流程 ( P_ECNWF )
- **业务含义**：OCN/ECN审批流程
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| approveVersion | int? | 是 | - | 审批版本 |
| beginTime | DateTime? | 是 | - | 开始时间 |
| business | string | 是 | - | 业务 |
| businessCode | string | 是 | - | 业务代码 |
| businessForm | string | 是 | - | 业务表单 |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | 编辑表单 |
| endTime | DateTime? | 是 | - | 结束时间 |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | 流程说明 |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | 审批人 |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postRoleIds | string | 是 | - | 岗位列表 |
| suggest | string | 是 | - | 建议 |
| taskDesc | string | 是 | - | 任务说明 |
| taskDetails | string | 是 | - | 任务明细 |
| taskFrom | string | 是 | - | 任务表单 |
| taskId | string | 是 | - | 任务 |
| taskName | string | 是 | - | 任务名称 |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | 记录版本 |
| ecnId | int? | 是 | - | OCN/ECN，对应P_ECN.recId |
| myId | int? | 是 | - | 审批人，对应T_User.recId |
- **关联关系**：
  - P_ECNWF.ecnId = P_ECN.recId
  - P_ECNWF.myId = T_User.recId

---

#### 317 MRB检查 ( P_Inspection )
- **业务含义**：MRB检查
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | 建单时间 |
| issueRoutesId | int? | 是 | - | - |
| mrbRequisitionId | int? | 是 | - | MRB接收(MRB检查申请表)，对应P_MRBRequisition.recId |
| note | string | 是 | - | 备注 |
| prd_MO_RoutesId | int? | 是 | - | MO流转记录，对应P_MORoute.recId |
| qty_Array | int? | 是 | - | SET |
| qty_PCS | int? | 是 | - | PCS |
| qty_PNLS | int? | 是 | - | PNL |
| result | string | 是 | - | Scrapped 报废 |
| status | int? | 是 | - | - |
| version | int? | 是 | - | - |
| wip_PCWOId | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| defectId | int? | 是 | - | 缺陷表，对应T_Defect.recId |
| inspectItemsId | int? | 是 | - | MRB检查明细，对应T_InspectItems.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| woId | int? | 是 | - | 工单表，对应P_WO.recId |
| suppliersId | int? | 是 | - | 对应M_Suppliers.recId |
| employeeId | int? | 是 | - | - |
| ttype,offset | string | 是 | - | P_Inspection.ttype=0 offset=1 预报废扣数处理  -- 前工序
P_Inspection.ttype=0 offset=0 预报废没扣数   -- 前工序
P_Inspection.ttype=1真报废  -- 电测后 |
- **关联关系**：
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

#### 318 P_IPQC ( P_IPQC )
- **业务含义**：ERP 系统 P_IPQC 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 记录ID |
| ipqcNumber | string | 是 | - | IPQC单号 |
| woId | string | 是 | - | 工单表（P_WO）记录ID |
| stepsId | string | 是 | - | 工序表（T_Steps）记录ID |
| processId | string | 是 | - | 工艺表（T_Process）记录ID |
| processNumber | string | 是 | - | 工艺号 |
| qty_PNL_BACKLOG | string | 是 | - | PNL数量 |
| qty_Array_BACKLOG | string | 是 | - | SET数量 |
| qty_PCS_BACKLOG | string | 是 | - | PCS数量 |
| judgment | string | 是 | - | 判断（0:不合格，1:合格） |
| status | string | 是 | - | 单据状态 |
| approveStatus | string | 是 | - | 审核状态 |
| version | string | 是 | - | 版本号 |
| modifyUserId | string | 是 | - | 修改人ID |
| modifyTime | string | 是 | - | 修改时间 |
| moRouteId | string | 是 | - | 流转记录表（P_MORoute）记录ID |
- **关联关系**：无

---

#### 319 P_IPQCItem ( P_IPQCItem )
- **业务含义**：ERP 系统 P_IPQCItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 记录ID |
| ipqcId | string | 是 | - | IPQC检验表（P_IPQC）记录ID |
| stepsProcessInspectItemId | string | 是 | - | 工艺定量、定性检验项表（T_StepsProcessInspectItem）记录ID |
| min | string | 是 | - | 最小值 |
| center | string | 是 | - | 中间值 |
| max | string | 是 | - | 最大值 |
| measurements1 | string | 是 | - | 测量值1 |
| measurements2 | string | 是 | - | 测量值2 |
| measurements3 | string | 是 | - | 测量值3 |
| measurements4 | string | 是 | - | 测量值4 |
| measurements5 | string | 是 | - | 测量值5 |
| measurements6 | string | 是 | - | 测量值6 |
| measurements7 | string | 是 | - | 测量值7 |
| measurements8 | string | 是 | - | 测量值8 |
| measurements9 | string | 是 | - | 测量值9 |
| difference | string | 是 | - | 极差值 |
| average | string | 是 | - | 平均值 |
| qty | string | 是 | - | 数量 |
| judgment | string | 是 | - | 判断 |
| version | string | 是 | - | 版本号 |
| modifyUserId | string | 是 | - | 修改人ID |
| modifyTime | string | 是 | - | 修改时间 |
- **关联关系**：无

---

#### 320 合拼单 ( P_MergeOrder )
- **业务含义**：合拼单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 否 | - | 主键 |
| completeDate | string | 是 | - | 完成日期 |
| createDate | string | 是 | - | 创建日期 |
| mergeNumber | string | 是 | - | 合拼单号 |
| note | string | 是 | - | 备注 |
| qtyVote | string | 是 | - | 投产数量 |
| scrapeRate | string | 是 | - | 报废率 |
| source | string | 是 | - | 来源 |
| version | string | 是 | - | - |
| creatorId | string | 是 | - | 创建人；t_use |
| jobId | string | 是 | - | 生产部件id；s_job |
| plantsId | string | 是 | - | 工厂id；T_Plants |
| postRoleId | string | 是 | - | 岗位id；T_PostRole |
| moId | string | 是 | - | 制造订单id；P_MO |
| status | string | 是 | - | 状态 |
| culayers | string | 是 | - | 层数 |
| productGroupId | string | 是 | - | 产品分组id；S_ProductGroup |
| subAfterMoRouteFormMerger | string | 是 | - | 合拼单切开后子部件流程是否来自主单 |
- **关联关系**：无

---

#### 321 合拼明细表 ( P_MergeOrderSO )
- **业务含义**：合拼明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId, | string | 是 | - | 主键 |
| QtyPcsPlanned | string | 是 | - | - |
| qty | string | 是 | - | 数量 |
| qtyArrayPlanned | string | 是 | - | - |
| qtyArrayVote | string | 是 | - | 投产交货板数 |
| qtyPcsVote | string | 是 | - | 投产pcs数 |
| version | string | 是 | - | 备注 |
| contractSOId | string | 是 | - | 销售订单id |
| jobChildrenId | string | 是 | - | job关联合拼表id；E_JobChildren |
| mergeOrderId | string | 是 | - | 合拼主表id；P_MergeOrder |
- **关联关系**：无

---

#### 322 部件表 ( P_MfgPartsInv )
- **业务含义**：部件表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createTime | DateTime? | 是 | - | 建单时间 |
| qtyOfArrs | int? | 是 | - | SET |
| qtyOfArrs_onhand | int? | 是 | - | 在线SET数 |
| qtyOfPcss | int? | 是 | - | PCS |
| qtyOfPcss_onhand | int? | 是 | - | 在线PCS数 |
| qtyOfPnls | int? | 是 | - | PNL |
| qtyOfPnls_onhand | int? | 是 | - | 在线PNL数 |
| version | int? | 是 | - | - |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| userId | int? | 是 | - | 用户表，对应T_User.recId |
| wipWarehouseId | int? | 是 | - | 仓库，对应T_Warehouse.recId |
| stepId | int? | 是 | - | 工序，对应T_Step.recId |
| pwoId | int? | 是 | - | 对应P_WO.recId |
| ifEnd | bool? | 是 | - | 是否是最后一个 .0否  1 是 |
- **关联关系**：
  - P_MfgPartsInv.woId = P_WO.recId
  - P_MfgPartsInv.userId = T_User.recId
  - P_MfgPartsInv.wipWarehouseId = T_Warehouse.recId
  - P_MfgPartsInv.stepId = T_Step.recId
  - P_MfgPartsInv.pwoId = P_WO.recId

---

#### 323 部件使用情况表 ( P_MfgPartsIssue )
- **业务含义**：部件使用情况表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createTime | DateTime? | 是 | - | 建单时间 |
| moBomId | int? | 是 | - | - |
| qtyOfArrs_Assigned | int? | 是 | - | SET |
| qtyOfPcss_Assigned | int? | 是 | - | PCS |
| qtyOfPnls_Assigned | int? | 是 | - | PNL |
| version | int? | 是 | - | - |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| mfgPartsInvId | int? | 是 | - | 部件表，对应P_MfgPartsInv.recId |
| userId | int? | 是 | - | 建单人，对应T_User.recId |
- **关联关系**：
  - P_MfgPartsIssue.woId = P_WO.recId
  - P_MfgPartsIssue.mfgPartsInvId = P_MfgPartsInv.recId
  - P_MfgPartsIssue.userId = T_User.recId

---

#### 324 部件升级记录 ( P_MfgUpRevLog )
- **业务含义**：部件升级记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createTime | DateTime? | 是 | - | - |
| note | string | 是 | - | - |
| woList | string | 是 | - | - |
| creatorId | int? | 是 | - | 建单人呢，对应T_User.recId |
| desJobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| desJobMfgPartId | int? | 是 | - | 产品部件表，对应E_JobMfgParts.recId |
| oriJobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| oriJobMfgPartId | int? | 是 | - | 对应E_JobMfgParts.recId |
| processId | int? | 是 | - | 工序，对应T_Process.recId |
- **关联关系**：
  - P_MfgUpRevLog.creatorId = T_User.recId
  - P_MfgUpRevLog.desJobId = S_Job.recId
  - P_MfgUpRevLog.desJobMfgPartId = E_JobMfgParts.recId
  - P_MfgUpRevLog.oriJobId = S_Job.recId
  - P_MfgUpRevLog.oriJobMfgPartId = E_JobMfgParts.recId
  - P_MfgUpRevLog.processId = T_Process.recId

---

#### 325 制造订单表 ( P_MO )
- **业务含义**：制造订单表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addQtyArray | int? | 是 | - | 生产补投交货板数量(累计) |
| addQtyPcs | int? | 是 | - | 生产补投交货板数量(累计) |
| addQtyPnl | int? | 是 | - | 生产补投交货板数量(累计) |
| createDate | DateTime? | 是 | - | 建单日期 |
| lotsize | int? | 是 | - | 每张LOT生产板数（工单基数） |
| moNumber | string | 是 | - | 制造订单号 |
| note | string | 是 | - | 备注 |
| parentId | int? | 是 | - | 生产补投对应的MO，对应P_MO.recId |
| pcsOfPanel_A | int? | 是 | - | A PCS/PNL   比，对应制造部件.recId |
| pcsOfPanel_B | int? | 是 | - | B PCS/PNL   比 |
| pnlOfSheet_A | int? | 是 | - | A PNL/SET   比 |
| pnlOfSheet_B | int? | 是 | - | B PNL/SET   比 |
| ppp | int? | 是 | - | PCS/SET  比 |
| qtyArray | int? | 是 | - | 交货板数(SET) |
| qtyArray_A | int? | 是 | - | 交货板数_A |
| qtyArray_B | int? | 是 | - | 交货板数_B |
| qtyPanel | int? | 是 | - | 生产板数（PNL） |
| qtyPanel_A | int? | 是 | - | 生产板数_A |
| qtyPanel_B | int? | 是 | - | 生产板数_B |
| qtyPcs | int? | 是 | - | 单元数PCS |
| qtyPcs_A | int? | 是 | - | 单元数_A |
| qtyPcs_B | int? | 是 | - | 单元数_B |
| qtyReqPanel_A | int? | 是 | - | - |
| qtyReqPanel_AB | int? | 是 | - | - |
| qtyReqPanel_B | int? | 是 | - | - |
| qtyReqPcs_A | int? | 是 | - | A板投的数量 |
| qtyReqPcs_AB | int? | 是 | - | AB板投的数量 |
| qtyReqPcs_B | int? | 是 | - | - |
| qtyWO | int? | 是 | - | 工单数量（几张工单） |
| saleType | string | 是 | - | 销售类型：Bonded 保税 ForDomestic 内销 ForExport 外销 |
| type | string | 是 | - | SO=正常投产(销售订单) ReturnRepair=退货返修  Replenishment=补货 StockRepair=仓库返修 ProVote=生产补投 Merger=合拼
补充：MakeToStock=存货补投 |
| scrapeRate | decimal? | 是 | - | 报废率 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 加单人，对应T_User.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| abType | string | 是 | ('') | AB板 |
| qtySO | int? | 是 | - | 计划订单数量PCS(本次计划数) |
| qtyReject | int? | 是 | - | 报废数(累计) |
| qtySOVote | int? | 是 | - | 计划投产数（投产数） |
| qtySheet_A | decimal? | 是 | - | - |
| qtySheet_B | decimal? | 是 | - | - |
| qtySheet_AB | decimal? | 是 | - | - |
| status | string | 是 | - | 单据状态：Active 激活  Order 已下单；（1外协 WOWX; 2未发放 WOWFF; 3已发放 WOYFF; 4暂停 WOZT; 5取消 WOQX; 6完成 WOWC;） |
| dateCode | string | 是 | - | 周期码 |
| lackMatFlag | bool? | 是 | ((1)) | - |
| completeDate | DateTime? | 是 | - | 完成日期 |
| customerId | int? | 是 | - | 对应S_Customer.recId |
| oriJobId | int? | 是 | - | - |
| contractItemId | int? | 是 | - | 销售合同表，对应S_ContractItem.recId |
| soNumber | string | 是 | - | 订单号 |
| actualCost | decimal? | 是 | ((0)) | 含税单价（本位币） |
| xnh_workNo | string | 是 | - | - |
| old_erp_mrbQtys | decimal? | 是 | ((0)) | - |
| old_erp_FGIQtys | decimal? | 是 | ((0)) | - |
| old_erp_ShipQty | decimal? | 是 | ((0)) | - |
| old_erp_StockQty | decimal? | 是 | ((0)) | - |
| old_erp_shipqty_jh | decimal? | 是 | ((0)) | - |
| onhold | bool? | 是 | ((0)) | - |
| oriStatus | string | 是 | - | - |
| mergeOrderId | int? | 是 | - | - |
| qtyPicking | string | 是 | - | 领料数量 |
| qtyIssued | string | 是 | - | 发料数量 |
| synchro | string | 是 | - | 同步状态，0-未同步；1-已同步；2-不同步 |
| dev | string | 是 | - | 研发标识，1是，0否 |
| rdProjectId | string | 是 | - | 项目，对应M_RDProject.recId |
- **关联关系**：
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

#### 326 制造订单表中的BOM ( P_MOBOM )
- **业务含义**：制造订单表中的BOM
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bomPicklistItemId | int? | 是 | - | BOM领料单，对应M_BOMPicklistItem.recId |
| id | string | 是 | - | - |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| note | string | 是 | - | 备注 |
| parentId | string | 是 | - | - |
| per | string | 是 | - | 单位代码 |
| qtyOfBom | decimal? | 是 | - | BOM数量 |
| qty_BOM | decimal? | 是 | - | 需求数量 |
| qty_ISSUED | decimal? | 是 | - | 发料数量 |
| route_STEP_NO | string | 是 | - | - |
| version | int? | 是 | - | - |
| bomUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| moId | int? | 是 | - | 制造单表，对应P_MO.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| contractItemId | int? | 是 | - | 合同表，对应S_ContractItem.recId |
- **关联关系**：
  - P_MOBOM.bomPicklistItemId = M_BOMPicklistItem.recId
  - P_MOBOM.jobId = S_Job.recId
  - P_MOBOM.bomUnitId = T_Unit.recId
  - P_MOBOM.mfgPartId = E_JobMfgParts.recId
  - P_MOBOM.materialsId = M_Materials.recId
  - P_MOBOM.moId = P_MO.recId
  - P_MOBOM.processId = T_Process.recId
  - P_MOBOM.contractItemId = S_ContractItem.recId

---

#### 327 OCN/ECN工单变更 ( P_ModRoute )
- **业务含义**：OCN/ECN工单变更
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| type | string | 是 | - | 类型；增加流程: AddRoute; 删除流程: DelRoute |
| ecnId | int? | 是 | - | OCN/ECN |
| customerId | int? | 是 | - | 客户 |
| jobId | int? | 是 | - | 生产编号 |
| mfgPartsId | int? | 是 | - | 制造部件 |
| moId | int? | 是 | - | 制造订单 |
| startProcessId | int? | 是 | - | 开始流程 |
| endProcessId | int? | 是 | - | 结束流程 |
| modifiedBy | string | 是 | - | 更新人员 |
| lastmodifydate | DateTime? | 是 | - | 更新时间 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 328 OCN/ECN工单变更流程 ( P_ModRouteItem )
- **业务含义**：OCN/ECN工单变更流程
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| modRouteId | int? | 是 | - | 工单变更 |
| processNumber | int? | 是 | - | 工艺号 |
| processId | int? | 是 | - | 工序指针 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 329 MO修改记录 ( P_ModRouteLog )
- **业务含义**：MO修改记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createTime | DateTime? | 是 | - | 创建时间 |
| note | string | 是 | - | 备注 |
| way | string | 是 | - | Add添加  Delete 删除 |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| woId | int? | 是 | - | 工单表，对应P_WO.recId |
- **关联关系**：
  - P_ModRouteLog.creatorId = T_User.recId
  - P_ModRouteLog.processId = T_Process.recId
  - P_ModRouteLog.stepsId = T_Steps.recId
  - P_ModRouteLog.woId = P_WO.recId

---

#### 330 OCN/ECN工单变更参数 ( P_ModRouteParams )
- **业务含义**：OCN/ECN工单变更参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| modRouteId | int? | 是 | - | 工单变更 |
| routeId | int? | 是 | - | 工单变更流程 |
| parametersId | int? | 是 | - | 参数 |
| dataType | string | 是 | - | 数据类型 |
| parameterValue | string | 是 | - | 参数值 |
| listVal | string | 是 | - | 参数值 |
| textValue | string | 是 | - | 文本值 |
| intValue | int? | 是 | - | 整数值 |
| floatValue | decimal? | 是 | - | 浮点值 |
| boolValue | bool? | 是 | - | 布尔值 |
| dateValue | DateTime? | 是 | - | 日期值 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 331 OCN/ECN工单变更工单列表 ( P_ModRouteWO )
- **业务含义**：OCN/ECN工单变更工单列表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| modRouteId | int? | 是 | - | 工单变更 |
| woId | int? | 是 | - | 工单 |
| version | int? | 是 | - | 记录版本 |
- **关联关系**：无

---

#### 332 制造订单中的制造部件 ( P_MOMfgPart )
- **业务含义**：制造订单中的制造部件
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| actionTime | DateTime? | 是 | - | 投产日期 |
| leadTime | int? | 是 | - | 制造周期 |
| leadTime_B | int? | 是 | - | 制造周期_B |
| lotSize | int? | 是 | - | 工单基数_A |
| lotSize_B | int? | 是 | - | 工单基数_B |
| pcsOfArray | int? | 是 | - | PCS/SET比 |
| pcsOfArray_B | int? | 是 | - | PCS/SET比_B |
| pcsOfPanel | int? | 是 | - | PCS/PNL比 |
| pcsOfPanel_B | int? | 是 | - | PCS/PNL比_B |
| scrapRate | decimal? | 是 | - | 报废率 |
| scrapRate_B | decimal? | 是 | - | 报废率_B |
| version | int? | 是 | - | - |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| moId | int? | 是 | - | 制造单表，对应P_MO.recId |
| rejectQtyOfPCS | int? | 是 | ((0)) | - |
| defectQtyOfPCS | int? | 是 | ((0)) | - |
- **关联关系**：
  - P_MOMfgPart.mfgPartId = E_JobMfgParts.recId
  - P_MOMfgPart.moId = P_MO.recId

---

#### 333 制造订单中的制造部件参数 ( P_MOMfgPartParams )
- **业务含义**：制造订单中的制造部件参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | - |
| dataType | string | 是 | - | - |
| dateValue | DateTime? | 是 | - | - |
| floatValue | decimal? | 是 | - | - |
| intValue | int? | 是 | - | intValue |
| jobId | int? | 是 | - | - |
| listVal | string | 是 | - | - |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| moId | int? | 是 | - | - |
| parameterValue | string | 是 | - | - |
| sort | int? | 是 | - | - |
| textValue | string | 是 | - | - |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 对应S_Parameters.recId |
- **关联关系**：
  - P_MOMfgPartParams.mfgPartId = E_JobMfgParts.recId
  - P_MOMfgPartParams.parametersId = S_Parameters.recId

---

#### 334 制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表 ( P_MORoute )
- **业务含义**：制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| costed_FLAG | int? | 是 | - | - |
| cr | decimal? | 是 | - | - |
| inTime | DateTime? | 是 | - | - |
| inspectQty | int? | 是 | - | - |
| moId | int? | 是 | - | 制造单表，对应P_MO.recId |
| note | string | 是 | - | 备注 |
| outTime | DateTime? | 是 | - | - |
| planSeq | int? | 是 | - | - |
| plantDate | DateTime? | 是 | - | 计划日期 |
| processNumber | int? | 是 | - | 序号(步骤号) |
| projectEndTime | DateTime? | 是 | - | - |
| projectStartTime | DateTime? | 是 | - | - |
| qty_Array_BACKLOG | int? | 是 | - | 结存SET |
| qty_Array_Defect | int? | 是 | - | 缺陷SET |
| qty_Array_INTRANSIT | int? | 是 | - | 两步过数的已转出待接收数量_array，对应测试为转出数量.recId |
| qty_Array_Inspection | int? | 是 | - | 送检SET |
| qty_Array_PRODUCED | int? | 是 | - | 产出SET |
| qty_Array_REJECTED | int? | 是 | - | 报废SET |
| qty_Array_Rework | int? | 是 | - | 返工SET |
| qty_PCS_BACKLOG | int? | 是 | - | 结存PCS |
| qty_PCS_Defect | int? | 是 | - | 缺陷PCS |
| qty_PCS_INTRANSIT | int? | 是 | - | 两步过数的已转出待接收数量_PCS，对应测试为转出数量.recId |
| qty_PCS_Inspection | int? | 是 | - | 送检PCS |
| qty_PCS_PRODUCED | int? | 是 | - | 产出PCS |
| qty_PCS_REJECTED | int? | 是 | - | 报废PCS |
| qty_PCS_Rework | int? | 是 | - | 返工PCS |
| qty_PNL_BACKLOG | int? | 是 | - | 结存PNL |
| qty_PNL_Defect | int? | 是 | - | 缺陷PNL |
| qty_PNL_INTRANSIT | int? | 是 | - | 两步过数的已转出待接收数量_PNL，对应测试为转出数量.recId |
| qty_PNL_Inspection | int? | 是 | - | 送检PNL |
| qty_PNL_PRODUCED | int? | 是 | - | 产出PNL |
| qty_PNL_REJECTED | int? | 是 | - | 报废PNL |
| qty_PNL_Rework | int? | 是 | - | 返工PNL |
| reworkId | int? | 是 | - | 返工表，对应P_ReWork.recId |
| reworkQTy | int? | 是 | - | 返工数量PCS |
| reworkRouteId | int? | 是 | - | 返工流转表，对应P_ReworkRoute.recId |
| std_ProcessTime | int? | 是 | - | - |
| stepId | int? | 是 | - | 工序，对应T_Steps.recId |
| stepNotes | string | 是 | - | - |
| stepScrapRate | decimal? | 是 | - | - |
| step_HOLD | bool? | 是 | - | 外协暂停（1：打勾，0：不打勾） |
| subContractQty | int? | 是 | - | - |
| version | int? | 是 | - | - |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| ifBarcodEntry | bool? | 是 | ((1)) | 是否需要过数 0否 1是 |
| qtyShiped | int? | 是 | ((0)) | 装运数量 |
- **关联关系**：
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

#### 335 工单流程参数 ( P_MORouteParams )
- **业务含义**：工单流程参数
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| boolValue | bool? | 是 | - | - |
| dataType | string | 是 | - | 类型：TextItem 文本  SelectItem 可选择 |
| dateValue | DateTime? | 是 | - | - |
| floatValue | decimal? | 是 | - | - |
| intValue | int? | 是 | - | - |
| listVal | string | 是 | - | - |
| moId | int? | 是 | - | 制造单，对应P_MO.recId |
| parameterValue | string | 是 | - | - |
| routeId | int? | 是 | - | 制造单流转表，对应P_MORoute.recId |
| sort | int? | 是 | - | - |
| textValue | string | 是 | - | 文本说明 |
| version | int? | 是 | - | - |
| parametersId | int? | 是 | - | 部件参数表，对应S_Parameters.recId |
- **关联关系**：
  - P_MORouteParams.moId = P_MO.recId
  - P_MORouteParams.routeId = P_MORoute.recId
  - P_MORouteParams.parametersId = S_Parameters.recId

---

#### 336 制造订单\销售订单 ( P_MOSO )
- **业务含义**：制造订单\销售订单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| assinedQtyInStock | int? | 是 | - | 成品分配数量 |
| assinedQtyInWIP | int? | 是 | - | WIP分配数量 |
| note | string | 是 | - | - |
| qtyPcs | int? | 是 | - | 订单数量 |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售订单表，对应S_ContractSO.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| moId | int? | 是 | - | 制造单表，对应P_MO.recId |
- **关联关系**：
  - P_MOSO.contractSOId = S_ContractSO.recId
  - P_MOSO.jobId = S_Job.recId
  - P_MOSO.moId = P_MO.recId

---

#### 337 MRB送检申请 ( P_MRBRequisition )
- **业务含义**：MRB送检申请
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| fixedDate | DateTime? | 是 | - | 确认检查日期 |
| note | string | 是 | - | 备注 |
| qtyArrayDefected | int? | 是 | - | 缺陷SET |
| qtyArrayReturn | int? | 是 | - | 返回SET |
| qtyArrayScrapped | int? | 是 | - | 报废SET |
| qtyPanelDefected | int? | 是 | - | 缺陷PNL |
| qtyPanelReturn | int? | 是 | - | appCategoryId |
| qtyPanelScrapped | int? | 是 | - | 报废PNL |
| qtyPcsDefected | int? | 是 | - | 缺陷PCS |
| qtyPcsReturn | int? | 是 | - | 返回PCS |
| qtyPcsScrapped | int? | 是 | - | 报废PCS |
| qty_Array | int? | 是 | - | 申请SET |
| qty_PCS | int? | 是 | - | 申请PCS |
| qty_PNLS | int? | 是 | - | 申请PNL |
| sendDate | DateTime? | 是 | - | 申请时间 |
| status | int? | 是 | - | 单据状态：0 待检 1 完成 |
| version | int? | 是 | - | - |
| fixedById | int? | 是 | - | 检查人，对应T_User.recId |
| prd_MO_RoutesId | int? | 是 | - | MO流转记录表，对应P_MORoute.recId |
| sendById | int? | 是 | - | 送检人，对应T_User.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| woId | int? | 是 | - | 工单表，对应P_WO.recId |
| employeeId | int? | 是 | - | - |
- **关联关系**：
  - P_MRBRequisition.fixedById = T_User.recId
  - P_MRBRequisition.prd_MO_RoutesId = P_MORoute.recId
  - P_MRBRequisition.sendById = T_User.recId
  - P_MRBRequisition.unitId = T_Unit.recId
  - P_MRBRequisition.woId = P_WO.recId

---

#### 338 MRP物资需求计划 ( P_MRP )
- **业务含义**：MRP物资需求计划
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cutoffDate | DateTime? | 是 | - | 截止日期 |
| note | string | 是 | - | 备注 |
| prId | int? | 是 | - | - |
| transDate | DateTime? | 是 | - | 需求日期 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人呢，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| reqDate | DateTime? | 是 | - | 创建日期 |
| ttype | int? | 是 | ((0)) | - |
- **关联关系**：
  - P_MRP.companyId = T_Company.recId
  - P_MRP.creatorId = T_User.recId
  - P_MRP.plantsId = T_Plants.recId
  - P_MRP.postRoleId = T_PostRole.recId

---

#### 339 P_MRPREQ ( P_MRPREQ )
- **业务含义**：ERP 系统 P_MRPREQ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cutoffDate | DateTime? | 是 | - | - |
| note | string | 是 | - | - |
| prItemId | int? | 是 | - | - |
| qtyInPO | decimal? | 是 | - | - |
| qtyInPR | decimal? | 是 | - | - |
| qtyOfCutOff | decimal? | 是 | - | - |
| qtyRequestTotal | decimal? | 是 | - | - |
| qtyStock | decimal? | 是 | - | - |
| qtyToBestock | decimal? | 是 | - | - |
| totalArea | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| materialsId | int? | 是 | - | 对应M_Materials.recId |
| mrpId | int? | 是 | - | 对应P_MRP.recId |
| qtyInFO | decimal? | 是 | - | - |
| qtyInSO | decimal? | 是 | - | - |
| qtyInMO | decimal? | 是 | - | - |
- **关联关系**：
  - P_MRPREQ.materialsId = M_Materials.recId
  - P_MRPREQ.mrpId = P_MRP.recId

---

#### 340 P_MRPREQItem ( P_MRPREQItem )
- **业务含义**：ERP 系统 P_MRPREQItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| dueDate | DateTime? | 是 | - | - |
| ifCal | bool? | 是 | - | - |
| orderCode | string | 是 | - | - |
| orderId | int? | 是 | - | - |
| orderType | string | 是 | - | - |
| qtyBOM | decimal? | 是 | - | - |
| qtyInOrder | decimal? | 是 | - | - |
| qtyRequest | decimal? | 是 | - | - |
| requestDate | DateTime? | 是 | - | - |
| startDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| bomUnitId | int? | 是 | - | 对应T_Unit.recId |
| materialsId | int? | 是 | - | 对应M_Materials.recId |
| mrpreqId | int? | 是 | - | 对应P_MRPREQ.recId |
| stepsId | int? | 是 | - | 对应T_Steps.recId |
- **关联关系**：
  - P_MRPREQItem.bomUnitId = T_Unit.recId
  - P_MRPREQItem.materialsId = M_Materials.recId
  - P_MRPREQItem.mrpreqId = P_MRPREQ.recId
  - P_MRPREQItem.stepsId = T_Steps.recId

---

#### 341 工单过数记录表 ( P_OutPut )
- **业务含义**：工单过数记录表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| cost_PROD | decimal? | 是 | - | - |
| cost_REJECT | decimal? | 是 | - | - |
| costed_FLAG | bool? | 是 | - | - |
| createDate | DateTime? | 是 | - | 建单时间 |
| endTime | DateTime? | 是 | - | - |
| ifJob | bool? | 是 | - | 结束点 1 结束 |
| moId | int? | 是 | - | 制造单号，对应P_MO.recId |
| nextOutPutRouteId | int? | 是 | - | 下一流转记录表，对应P_OutPutRoute(无效).recId |
| nextPlantId | int? | 是 | - | 一下工厂，对应T_Plants.recId |
| nextProcessId | int? | 是 | - | 下一工艺，对应T_Process.recId |
| note | string | 是 | - | 备注 |
| prd_MO_RoutesId | int? | 是 | - | 制作订单流转记录，对应P_MORoute.recId |
| qty_Array | int? | 是 | - | 产出SET |
| qty_INSP | int? | 是 | - | - |
| qty_PCS | int? | 是 | - | 工单pcs数 |
| qty_PCS_Reject | int? | 是 | - | 报废PCS（没有数据，在P_WO表或P_MORoute里） |
| qty_PNLS | int? | 是 | - | 产出PNL |
| qty_PNLS_Temp | int? | 是 | - | 临时存放PNL |
| receivedTime | DateTime? | 是 | - | 接收时间 |
| reference_number | string | 是 | - | - |
| reworkId | int? | 是 | - | reworkId = 0 --去除返工工单，对应P_ReWork  返工表.recId |
| startTime | DateTime? | 是 | - | 过数时间 |
| status | int? | 是 | - | - |
| stepId | int? | 是 | - | 当前工序，对应T_Step.recId |
| step_seq | int? | 是 | - | 工序号 |
| version | string | 是 | - | None 正常生产  Working 外协 |
| work_centerId | int? | 是 | - | - |
| creatorId | int? | 是 | - | 对应T_User.recId |
| equipmentId | int? | 是 | - | 对应EQ_Equipments.recId |
| outputManId | int? | 是 | - | 对应S_BusinessMan.recId |
| receivedUserId | int? | 是 | - | - |
| unitId | int? | 是 | - | - |
| woId | int? | 是 | - | - |
| jupmuuId | string | 是 | - | - |
| nextStepId | int? | 是 | - | 下一工序 |
| sysOutput | bool? | 是 | ((0)) | 0:正常产出过数，1：系统自动过数属于外协 |
| nextReceiveStepId | int? | 是 | - | 下一接收工序 |
- **关联关系**：
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

#### 342 P_PQE ( P_PQE )
- **业务含义**：ERP 系统 P_PQE 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 记录ID |
| ipqcId | string | 是 | - | IPQC检验表（P_IPQC）记录ID |
| pqeNumber | string | 是 | - | PQE单号 |
| pqeType | string | 是 | - | 类型(1:放行，2:特采，3:等待，4:不等待) |
| lock_processId | string | 是 | - | 锁定工艺 |
| ifRework | string | 是 | - | 是否返工 |
| qty_PNL_REWORK | string | 是 | - | 返工PNL数量 |
| qty_Array_REWORK | string | 是 | - | 返工SET数量 |
| qty_PCS_REWORK | string | 是 | - | 返工PCS数量 |
| ifScrapped | string | 是 | - | 是否报废 |
| qty_PNL_SCRAPPED | string | 是 | - | 报废PNL数量 |
| qty_Array_SCRAPPED | string | 是 | - | 报废SET数量 |
| qty_PCS_SCRAPPED | string | 是 | - | 报废PCS数量 |
| remark | string | 是 | - | 备注 |
| status | string | 是 | - | 单据状态 |
| approveStatus | string | 是 | - | 审核状态 |
| version | string | 是 | - | 版本号 |
| modifyUserId | string | 是 | - | 修改人ID |
| modifyTime | string | 是 | - | 修改时间 |
- **关联关系**：无

---

#### 343 P_RetrospectTool ( P_RetrospectTool )
- **业务含义**：ERP 系统 P_RetrospectTool 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| moRouteId | string | 是 | - | 在制品ID，对应P_MORoute.recId |
| toolId | string | 是 | - | 工具表ID，对应P_Tools.recId |
| quantity | string | 是 | - | 使用数量 |
| note | string | 是 | - | 备注 |
| version | string | 是 | - | - |
- **关联关系**：
  - P_RetrospectTool.moRouteId = P_MORoute.recId
  - P_RetrospectTool.toolId = P_Tools.recId

---

#### 344 返工表 ( P_ReWork )
- **业务含义**：返工表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | - |
| note | string | 是 | - | - |
| plantId | int? | 是 | - | - |
| prd_MO_RoutesId | int? | 是 | - | 制作订单流转记录，对应P_MORoute.recId |
| qty_Array | int? | 是 | - | SET |
| qty_PCS | int? | 是 | - | PCS |
| qty_PNLS | int? | 是 | - | PNL |
| rework_seq | int? | 是 | - | 序号 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
| woId | int? | 是 | - | 工单表，对应P_WO.recId |
| employeeId | int? | 是 | - | 对应T_User.recId |
| return_RouteId | int? | 是 | - | - |
| ifReceive | bool? | 是 | - | 是否接收（1：接收   ，0：没有接收） |
| tempProcessId | int? | 是 | - | 临时工艺，对应T_Process.recId |
| tempStepId | int? | 是 | - | 临时工序，对应T_Step.recId |
| receiptDate | string | 是 | - | 接收时间（为null表是没有接收） |
| receiptEmployeeId | string | 是 | - | 接收雇员表ID（S_BusinessMan） |
| mergeReWorkId | string | 是 | - | - |
- **关联关系**：
  - P_ReWork.prd_MO_RoutesId = P_MORoute.recId
  - P_ReWork.creatorId = T_User.recId
  - P_ReWork.unitId = T_Unit.recId
  - P_ReWork.woId = P_WO.recId
  - P_ReWork.employeeId = T_User.recId
  - P_ReWork.tempProcessId = T_Process.recId
  - P_ReWork.tempStepId = T_Step.recId

---

#### 345 P_ReWorkApplication ( P_ReWorkApplication )
- **业务含义**：ERP 系统 P_ReWorkApplication 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 唯一id |
| plantsId | string | 是 | - | 工厂id，对应T_Plants.recId |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| status | string | 是 | - | 单据状态 |
| approveStatus | string | 是 | - | 审批状态 |
| prd_MO_RoutesId | string | 是 | - | 在制品ID，对应P_MORoute.recId |
| woid | string | 是 | - | 工单，对应P_WO.recId |
| stepId | string | 是 | - | 工序，对应T_Steps.recId |
| processId | string | 是 | - | 工艺，对应T_Process.recId |
| processNumber | string | 是 | - | 工艺号 |
| qty_PCS_Split | string | 是 | - | PCS数量 |
| qty_Array_Split | string | 是 | - | SET数量 |
| qty_PNL_Split | string | 是 | - | PNL数量 |
| type | string | 是 | - | 类型;1手工新建,2联动生成 |
| creatorId | string | 是 | - | 创建人 |
| creatorTime | string | 是 | - | 创建时间 |
| modifiedById | string | 是 | - | 修改人 |
| modifiedTime | string | 是 | - | 修改时间 |
| note | string | 是 | - | 备注 |
| version | string | 是 | - | - |
- **关联关系**：
  - P_ReWorkApplication.plantsId = T_Plants.recId
  - P_ReWorkApplication.prd_MO_RoutesId = P_MORoute.recId
  - P_ReWorkApplication.woid = P_WO.recId
  - P_ReWorkApplication.stepId = T_Steps.recId
  - P_ReWorkApplication.processId = T_Process.recId

---

#### 346 P_ReWorkApplicationProcess ( P_ReWorkApplicationProcess )
- **业务含义**：ERP 系统 P_ReWorkApplicationProcess 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 唯一id |
| ReWorkApplicationId | string | 是 | - | 在制品ID |
| stepId | string | 是 | - | 工序 |
| processId | string | 是 | - | 工艺 |
| processNumber | string | 是 | - | 工艺号 |
| version | string | 是 | - | - |
- **关联关系**：无

---

#### 347 订单BOM表 ( P_SOBOM )
- **业务含义**：订单BOM表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| id | string | 是 | - | - |
| jobId | int? | 是 | - | 生产型号表，对应S_Job.recId |
| note | string | 是 | - | - |
| parentId | string | 是 | - | - |
| per | string | 是 | - | - |
| qtyOfBom | decimal? | 是 | - | BOM数量 |
| qty_BOM | decimal? | 是 | - | - |
| qty_ISSUED | decimal? | 是 | - | - |
| route_STEP_NO | string | 是 | - | - |
| version | int? | 是 | - | - |
| bomUnitId | int? | 是 | - | 单位，对应T_Unit.recId |
| contractItemId | int? | 是 | - | 订单合同表，对应S_ContractItem.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| materialsId | int? | 是 | - | 物料，对应M_Materials.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
- **关联关系**：
  - P_SOBOM.jobId = S_Job.recId
  - P_SOBOM.bomUnitId = T_Unit.recId
  - P_SOBOM.contractItemId = S_ContractItem.recId
  - P_SOBOM.mfgPartId = E_JobMfgParts.recId
  - P_SOBOM.materialsId = M_Materials.recId
  - P_SOBOM.processId = T_Process.recId

---

#### 348 工单拆分记录 ( P_SplitWOLog )
- **业务含义**：工单拆分记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createTime | DateTime? | 是 | - | 创建时间 |
| note | string | 是 | - | 备注 |
| qty_Array | int? | 是 | - | 拆分SET数 |
| qty_PCS | int? | 是 | - | 拆分PCS数 |
| qty_PNLS | int? | 是 | - | 拆分PNL数 |
| stepId | int? | 是 | - | 工序，对应T_Step.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
- **关联关系**：
  - P_SplitWOLog.stepId = T_Step.recId
  - P_SplitWOLog.creatorId = T_User.recId
  - P_SplitWOLog.processId = T_Process.recId
  - P_SplitWOLog.woId = P_WO.recId

---

#### 349 工具申请单 ( P_ToolApply )
- **业务含义**：工具申请单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| chargeType | string | 是 | - | 收费类型：Charge 收费 Free 免费  UnitPrice 单价中 |
| createDate | DateTime? | 是 | - | 建单日期 |
| enableApproval | bool? | 是 | - | - |
| notes | string | 是 | - | 备注 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| prodType | string | 是 | - | 加工方式： Self 自制   Outsourcing 外发 |
| qtyApply | int? | 是 | - | 申领数量 |
| status | string | 是 | - | Valid 状态 |
| toolApplyNumber | string | 是 | - | 工具申请单号 |
| toolDesc | string | 是 | - | 工具描述 |
| toolRefNumber | string | 是 | - | 工具预置编号 |
| uuid | string | 是 | - | - |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售订单，对应S_ContractSO.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| flowTypeId | int? | 是 | - | 审批流程单，对应T_FlowType.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| toolTypeId | int? | 是 | - | 工具类型，对应P_ToolTypes.recId |
- **关联关系**：
  - P_ToolApply.contractSOId = S_ContractSO.recId
  - P_ToolApply.creatorId = T_User.recId
  - P_ToolApply.flowTypeId = T_FlowType.recId
  - P_ToolApply.mfgPartId = E_JobMfgParts.recId
  - P_ToolApply.locationId = T_Location.recId
  - P_ToolApply.plantsId = T_Plants.recId
  - P_ToolApply.postRoleId = T_PostRole.recId
  - P_ToolApply.toolTypeId = P_ToolTypes.recId

---

#### 350 工具申请审批流程记录 ( P_ToolApplyHistory )
- **业务含义**：工具申请审批流程记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| toolApplyId | int? | 是 | - | 对应P_ToolApply.recId |
- **关联关系**：
  - P_ToolApplyHistory.myId = T_User.recId
  - P_ToolApplyHistory.toolApplyId = P_ToolApply.recId

---

#### 351 P_ToolApplyWF ( P_ToolApplyWF )
- **业务含义**：ERP 系统 P_ToolApplyWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| myId | int? | 是 | - | 对应T_User.recId |
| toolApplyId | int? | 是 | - | 对应P_ToolApply.recId |
- **关联关系**：
  - P_ToolApplyWF.myId = T_User.recId
  - P_ToolApplyWF.toolApplyId = P_ToolApply.recId

---

#### 352 工具发放 ( P_ToolIssued )
- **业务含义**：工具发放
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | 建单日期 |
| issuedDate | DateTime? | 是 | - | 发放日期 |
| note | string | 是 | - | 备注 |
| qtyIssued | int? | 是 | - | 发放数量 |
| qtyReturned | int? | 是 | - | 退货数量 |
| refNumber | string | 是 | - | 发放单号 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| issuedById | int? | 是 | - | 发放人，对应T_User.recId |
| pickedById | int? | 是 | - | 领料人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| toolId | int? | 是 | - | 工具表，对应P_Tools.recId |
- **关联关系**：
  - P_ToolIssued.creatorId = T_User.recId
  - P_ToolIssued.issuedById = T_User.recId
  - P_ToolIssued.pickedById = T_User.recId
  - P_ToolIssued.plantsId = T_Plants.recId
  - P_ToolIssued.postRoleId = T_PostRole.recId
  - P_ToolIssued.stepsId = T_Steps.recId
  - P_ToolIssued.toolId = P_Tools.recId

---

#### 353 工具退回 ( P_ToolReturned )
- **业务含义**：工具退回
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| consumed | int? | 是 | - | 消耗寿命 |
| createDate | DateTime? | 是 | - | 制单日期 |
| note | string | 是 | - | 备注 |
| qtyReturned | int? | 是 | - | 退回数量 |
| returnDate | DateTime? | 是 | - | 退回日期 |
| returnNumber | string | 是 | - | 退回单号 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| receivedById | int? | 是 | - | 接收人，对应T_User.recId |
| returnById | int? | 是 | - | 退回人，对应T_User.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| toolId | int? | 是 | - | 工具表，对应P_Tools.recId |
| toolIssuedId | int? | 是 | - | 工具发放，对应P_ToolIssued.recId |
- **关联关系**：
  - P_ToolReturned.creatorId = T_User.recId
  - P_ToolReturned.plantsId = T_Plants.recId
  - P_ToolReturned.postRoleId = T_PostRole.recId
  - P_ToolReturned.receivedById = T_User.recId
  - P_ToolReturned.returnById = T_User.recId
  - P_ToolReturned.stepsId = T_Steps.recId
  - P_ToolReturned.toolId = P_Tools.recId
  - P_ToolReturned.toolIssuedId = P_ToolIssued.recId

---

#### 354 工具登记表 ( P_Tools )
- **业务含义**：工具登记表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| consumed | int? | 是 | - | 消耗寿命 |
| createDate | DateTime? | 是 | - | 建单日期 |
| note | string | 是 | - | 备注 |
| onholdDate | DateTime? | 是 | - | 暂缓日期 |
| qtyIssued | int? | 是 | - | 发放数量 |
| qtyOnhand | int? | 是 | - | 登记数量 |
| remained | int? | 是 | - | 剩余寿命 |
| scrappedDate | DateTime? | 是 | - | 报废日期 |
| status | string | 是 | - | Active 有效 |
| stdLifeSpan | int? | 是 | - | 标准寿命 |
| toolDesc | string | 是 | - | 工具描述 |
| toolNumber | string | 是 | - | 工具编号 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| mfgPartId | int? | 是 | - | 制造部件，对应E_JobMfgParts.recId |
| lifeUnitId | int? | 是 | - | 寿命单位，对应T_Unit.recId |
| locationId | int? | 是 | - | 储区，对应T_Location.recId |
| onholdById | int? | 是 | - | 暂缓操作员，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| scrappedById | int? | 是 | - | 报废人，对应T_User.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
| toolApplyId | int? | 是 | - | 工具申请单，对应P_ToolApply.recId |
| toolTypeId | int? | 是 | - | 工具类型，对应P_ToolTypes.recId |
- **关联关系**：
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

#### 355 工具类型 ( P_ToolTypes )
- **业务含义**：工具类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifLifeSpan | bool? | 是 | - | 是否用于寿命管理 0否 1是 |
| ifMI | bool? | 是 | - | 是否用于工程设计 0否 1是 |
| stdLifeSpan | int? | 是 | - | 标准寿命 |
| toolPrefix | string | 是 | - | 编码规则 |
| toolSeedNum | int? | 是 | - | - |
| toolType | string | 是 | - | 工具类型 |
| toolTypeDesc | string | 是 | - | 工具类型描述 |
| version | int? | 是 | - | - |
| inspectGroupId | int? | 是 | - | 检验分组，对应T_InspectGroup.recId |
| lifeUnitId | int? | 是 | - | 寿命单位，对应T_Unit.recId |
| purchasePostId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| stockUnitId | int? | 是 | - | 库存单位，对应T_Unit.recId |
- **关联关系**：
  - P_ToolTypes.inspectGroupId = T_InspectGroup.recId
  - P_ToolTypes.lifeUnitId = T_Unit.recId
  - P_ToolTypes.purchasePostId = T_PostRole.recId
  - P_ToolTypes.stockUnitId = T_Unit.recId

---

#### 356 工具类型所在仓库 ( P_ToolTypeWarehouse )
- **业务含义**：工具类型所在仓库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| inventory | int? | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 修改日期 |
| maxStockQty | int? | 是 | - | 最大库存 |
| minStockQty | int? | 是 | - | 安全库存 |
| modifiedBy | string | 是 | - | 修改人 |
| reorderQty | int? | 是 | - | 经济订量 |
| version | int? | 是 | - | - |
| locationId | int? | 是 | - | 储区，对应locationId.recId |
| toolTypeId | int? | 是 | - | 工具类型表，对应toolTypeId.recId |
| warehouseId | int? | 是 | - | 仓库，对应warehouseId.recId |
- **关联关系**：
  - P_ToolTypeWarehouse.locationId = locationId.recId
  - P_ToolTypeWarehouse.toolTypeId = toolTypeId.recId
  - P_ToolTypeWarehouse.warehouseId = warehouseId.recId

---

#### 357 P_UpdateLog ( P_UpdateLog )
- **业务含义**：ERP 系统 P_UpdateLog 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| operating | string | 是 | - | 操作类型 |
| operatingTime | string | 是 | - | 操作时间 |
| moduleCode | string | 是 | - | 表单Code |
| tableName | string | 是 | - | 更新表名 |
| fieldName | string | 是 | - | 更新字段名 |
| fieldChineseName | string | 是 | - | 更新字段中文名 |
| tableRecId | string | 是 | - | 更新表唯一id |
| originalValue | string | 是 | - | 原值 |
| newValue | string | 是 | - | 新值 |
| userId | string | 是 | - | 操作人id |
| userName | string | 是 | - | 操作人名称 |
| version | string | 是 | - | - |
| modifyTableRecId | string | 是 | - | 修改表id，对应M_Materials.recId |
| memo | string | 是 | - | 备注 |
- **关联关系**：
  - P_UpdateLog.modifyTableRecId = M_Materials.recId

---

#### 358 工作单号 ( P_WO )
- **业务含义**：工作单号
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | recId（主键） |
| ab | string | 是 | - | AB板类型  A,B,AB |
| moroute | int? | 是 | - | - |
| bindId | int? | 是 | - | - |
| partnum | string | 是 | - | 制造部件code |
| createDate | DateTime? | 是 | - | 制单日期 |
| dateCode | string | 是 | - | 周期码 |
| defect_Array | int? | 是 | - | 缺陷SET |
| defect_PCS | string | 是 | - | 缺陷PCS |
| defect_PNLS | int? | 是 | - | 缺陷PNL |
| endDate | DateTime? | 是 | - | 完工日期 |
| hold_StepNumber | int? | 是 | - | 子层id |
| id | string | 是 | - | - |
| inspectQty | int? | 是 | - | - |
| note | string | 是 | - | - |
| onholdReason | string | 是 | - | - |
| orgStatus | int? | 是 | - | - |
| parentId | string | 是 | - | 主工单（0：主工单 ） |
| planing_Array | int? | 是 | - | 投产set数 |
| planing_PCS | int? | 是 | - | 投产单元数 |
| planing_PNLS | int? | 是 | - | 投产pnl数 |
| qty_Array_BACKLOG | int? | 是 | - | 结存SET数量 |
| qty_Array_PRODUCED | int? | 是 | - | 产出set |
| qty_PCS_BACKLOG | int? | 是 | - | 结存PCS数 |
| qty_PCS_PRODUCED | int? | 是 | - | 产出PCS |
| qty_PNL_BACKLOG | int? | 是 | - | 结存PNL |
| qty_PNL_PRODUCED | int? | 是 | - | 产出PNL |
| reject_Array | int? | 是 | - | 报废SET |
| reject_PCS | int? | 是 | - | 报废PCS |
| reject_PNLS | int? | 是 | - | 报废PNL |
| releaseDate | DateTime? | 是 | - | 发放日期 |
| reworkQTy | int? | 是 | - | 返工数量 |
| rootId | string | 是 | - | 顶层工单id |
| splitId | int? | 是 | - | 拆单，上一级原单recid |
| splitRootId | int? | 是 | - | 拆单，最原始原单recid==对应P_SplitWOLog.WoID，对应P_SplitWOLog=>woId.recId |
| startDate | DateTime? | 是 | - | 开始投产时间 |
| status | int? | 是 | - | 1外协，2未发放，3已发放，4暂停，5取消，6完成 |
| stocked_Array | int? | 是 | - | 入库SET |
| stocked_PCS | int? | 是 | - | 入库PCS |
| subContractQty | int? | 是 | - | - |
- **关联关系**：
  - P_WO.splitRootId = P_SplitWOLog.woId

---

#### 359 工单IQC ( P_WOIQC )
- **业务含义**：工单IQC
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qtyOfPnls | int? | 是 | - | 检查数量pnl |
| version | int? | 是 | - | - |
| fgiiqcTestId | int? | 是 | - | IQC，对应FGI_IQC.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
| woId | int? | 是 | - | 工单表，对应P_WO.recId |
- **关联关系**：
  - P_WOIQC.fgiiqcTestId = FGI_IQC.recId
  - P_WOIQC.jobId = S_Job.recId
  - P_WOIQC.woId = P_WO.recId

---

#### 360 P_WOProcessBack ( P_WOProcessBack )
- **业务含义**：ERP 系统 P_WOProcessBack 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 361 P_WOProcessSend ( P_WOProcessSend )
- **业务含义**：ERP 系统 P_WOProcessSend 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | - |
| qtySend | int? | 是 | - | - |
| sendTime | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| employeeId | int? | 是 | - | 对应S_BusinessMan.recId |
| equipmentId | int? | 是 | - | 对应EQ_Equipments.recId |
| moRouteId | int? | 是 | - | 对应P_MORoute.recId |
| userId | int? | 是 | - | 对应T_User.recId |
| woProcessStockId | int? | 是 | - | - |
- **关联关系**：
  - P_WOProcessSend.employeeId = S_BusinessMan.recId
  - P_WOProcessSend.equipmentId = EQ_Equipments.recId
  - P_WOProcessSend.moRouteId = P_MORoute.recId
  - P_WOProcessSend.userId = T_User.recId

---

#### 362 P_WOProcessStock ( P_WOProcessStock )
- **业务含义**：ERP 系统 P_WOProcessStock 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qtyWork | int? | 是 | - | - |
| updateTime | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| employeeId | int? | 是 | - | 对应S_BusinessMan.recId |
| equipmentId | int? | 是 | - | 对应EQ_Equipments.recId |
| moRouteId | int? | 是 | - | 对应P_MORoute.recId |
- **关联关系**：
  - P_WOProcessStock.employeeId = S_BusinessMan.recId
  - P_WOProcessStock.equipmentId = EQ_Equipments.recId
  - P_WOProcessStock.moRouteId = P_MORoute.recId

---

#### 363 工单对应销售单 ( P_WOSO )
- **业务含义**：工单对应销售单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| B12401281534 | int? | 是 | - | 数量 |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售单，对应S_ContractSO.recId |
| jobId | int? | 是 | - | 生产型号表，对应S_Job.recId |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| salesPlanReviewId | int? | 是 | - | - |
- **关联关系**：
  - P_WOSO.contractSOId = S_ContractSO.recId
  - P_WOSO.jobId = S_Job.recId
  - P_WOSO.woId = P_WO.recId

---

#### 364 P_WOSplitBatchApplication ( P_WOSplitBatchApplication )
- **业务含义**：ERP 系统 P_WOSplitBatchApplication 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | 唯一id |
| plantsId | string | 是 | - | 工厂id，对应T_Plants.recId |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| status | string | 是 | - | 单据状态 |
| approveStatus | string | 是 | - | 审批状态 |
| prd_MO_RoutesId | string | 是 | - | 在制品ID，对应P_MORoute.recId |
| woid | string | 是 | - | 工单，对应P_WO.recId |
| stepId | string | 是 | - | 工序，对应T_Steps.recId |
| processId | string | 是 | - | 工艺，对应T_Process.recId |
| processNumber | string | 是 | - | 工艺号 |
| qty_PNL_Split | string | 是 | - | PCS数量 |
| qty_Array_Split | string | 是 | - | SET数量 |
| qty_PCS_Split | string | 是 | - | PNL数量 |
| type | string | 是 | - | 类型;1成套,2不成套 |
| creatorId | string | 是 | - | 创建人 |
| creatorTime | string | 是 | - | 创建时间 |
| modifiedById | string | 是 | - | 修改人 |
| modifiedTime | string | 是 | - | 修改时间 |
| note | string | 是 | - | 备注 |
| version | string | 是 | - | - |
- **关联关系**：
  - P_WOSplitBatchApplication.plantsId = T_Plants.recId
  - P_WOSplitBatchApplication.prd_MO_RoutesId = P_MORoute.recId
  - P_WOSplitBatchApplication.woid = P_WO.recId
  - P_WOSplitBatchApplication.stepId = T_Steps.recId
  - P_WOSplitBatchApplication.processId = T_Process.recId

---

#### 365 工单转出记录 ( P_WOTransfer )
- **业务含义**：工单转出记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| cost_PROD | decimal? | 是 | - | - |
| cost_REJECT | decimal? | 是 | - | - |
| costed_FLAG | bool? | 是 | - | - |
| createDate | DateTime? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| ifJob | bool? | 是 | - | - |
| jupmuuId | string | 是 | - | - |
| mergeOutPutId | int? | 是 | - | - |
| moId | int? | 是 | - | - |
| nextOutPutRouteId | int? | 是 | - | - |
| nextOutputMORouteId | int? | 是 | - | - |
| nextOutputStepId | int? | 是 | - | - |
| nextPlantId | int? | 是 | - | - |
| nextProcessId | int? | 是 | - | - |
| nextReceiveStepId | int? | 是 | - | - |
| nextStepId | int? | 是 | - | - |
| note | string | 是 | - | - |
| osIqcId | int? | 是 | - | - |
| plantId | int? | 是 | - | - |
| prd_MO_RoutesId | int? | 是 | - | 在制ID，对应P_MORoute.recId |
| qty_Array | int? | 是 | - | - |
| qty_INSP | int? | 是 | - | - |
| qty_PCS | int? | 是 | - | - |
| qty_PCS_Reject | int? | 是 | - | - |
| qty_PNLS | int? | 是 | - | - |
| qty_PNLS_Temp | int? | 是 | - | - |
| receivedTime | DateTime? | 是 | - | - |
| reference_number | string | 是 | - | - |
| reworkId | int? | 是 | - | - |
| splitOutputId | int? | 是 | - | - |
| startTime | DateTime? | 是 | - | - |
| status | int? | 是 | - | - |
| stepId | int? | 是 | - | - |
| step_seq | int? | 是 | - | - |
| sysOutput | bool? | 是 | - | - |
| version | int? | 是 | - | - |
| woType | string | 是 | - | - |
| work_centerId | int? | 是 | - | - |
| creatorId | int? | 是 | - | - |
| equipmentId | int? | 是 | - | - |
| outputManId | int? | 是 | - | - |
| receivedUserId | int? | 是 | - | - |
| unitId | int? | 是 | - | - |
| woId | int? | 是 | - | - |
| outputId | int? | 是 | - | - |
| flg | int? | 是 | - | - |
| partOutPut | bool? | 是 | - | - |
- **关联关系**：
  - P_WOTransfer.prd_MO_RoutesId = P_MORoute.recId

---

### 2.8 财务模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 366 财务应用-成本核算-成本明细 ( F_AccCostWOByPeriod )
- **业务含义**：财务应用-成本核算-成本明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| calRkey | int? | 是 | - | - |
| woId | int? | 是 | - | 工单 |
| periodId | int? | 是 | - | 财务会计期间 |
| qtyPlanned | int? | 是 | - | 投料数量 |
| qtyStocked | int? | 是 | - | 入仓数 |
| qtyWIP | int? | 是 | - | 在线数量 |
| qtyRejected | int? | 是 | - | 报废数量 |
| assemblyCost | decimal? | 是 | - | 子部件成本 |
| bomCost | decimal? | 是 | - | 直接材料成本 |
| overhead | decimal? | 是 | - | 公共成本 |
| addBomCost | decimal? | 是 | - | 间接bom成本 |
| osCost | decimal? | 是 | - | 外协成本 |
| indirectMat | decimal? | 是 | - | 间接材料成本 |
| depreciation | decimal? | 是 | - | 折旧成本 |
| maintenance | decimal? | 是 | - | 维护成本 |
| water | decimal? | 是 | - | 水费 |
| electricity | decimal? | 是 | - | 电费 |
| labor | decimal? | 是 | - | 人工 |
| transport | decimal? | 是 | - | 运输 |
| pub1 | decimal? | 是 | - | 自定义成本1（办公费） |
| pub2 | decimal? | 是 | - | 自定义成本2（低值易耗） |
| pub3 | decimal? | 是 | - | 自定义成本3（劳保） |
| pub4 | decimal? | 是 | - | 自定义成本4（其他） |
| pub5 | decimal? | 是 | - | 自定义成本5（辅助部门） |
| rejectCost | decimal? | 是 | - | 报废成本 |
| totalCostofWO | decimal? | 是 | - | 工单总成本 |
| balanceCost | decimal? | 是 | - | 结存成本 |
| unitCost | decimal? | 是 | - | 单位成本 |
| unitCostEffective | decimal? | 是 | - | 有效单位成本 |
| unitCostStocked | decimal? | 是 | - | 入仓单位成本 |
| version | int? | 是 | - | - |
| initialCost | decimal? | 是 | - | 期初成本 |
| costTransferred | bool? | 是 | - | - |
| woStatus | int? | 是 | - | - |
| innerCostToBalance | bool? | 是 | - | - |
| miBom | string | 是 | - | 非工序发料BOM |
| qtyCheck | string | 是 | - | 盘盈/盘亏数 |
- **关联关系**：无

---

#### 367 工单成本明细 ( F_AccCostWOBySteps )
- **业务含义**：工单成本明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| calRkey | int? | 是 | - | - |
| periodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| stepId | int? | 是 | - | 工序，对应T_Steps.recId |
| woId | int? | 是 | - | 工单，对应P_WO.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| processNumber | int? | 是 | - | 工序序号，对应序号.recId |
| planing_PCS | int? | 是 | - | 投料数量WO |
| qtyOutput | int? | 是 | - | 产出数量 |
| qtyBalance | int? | 是 | - | 结存数量 |
| qtyRejected | int? | 是 | - | 报废数量 |
| qtyOutputAndRejected | int? | 是 | - | 报废加产出 |
| assemblyCost | decimal? | 是 | - | - |
| bomCost | decimal? | 是 | - | 直接成本 |
| addBomCost | decimal? | 是 | - | - |
| osCost | decimal? | 是 | - | 外协成本 |
| indirectMat | decimal? | 是 | - | 间接成本 |
| depreciation | decimal? | 是 | - | 折旧成本 |
| maintenance | decimal? | 是 | - | 维护成本 |
| water | decimal? | 是 | - | 水费 |
| electricity | decimal? | 是 | - | 电费 |
| labor | decimal? | 是 | - | 人工 |
| transport | decimal? | 是 | - | 运输 |
| pub1 | decimal? | 是 | - | - |
| pub2 | decimal? | 是 | - | - |
| pub3 | decimal? | 是 | - | - |
| pub4 | decimal? | 是 | - | - |
| pub5 | decimal? | 是 | - | - |
| totalCostofWO | decimal? | 是 | - | 工单总成本（上工序成本+本工序成本） |
| thisStepCost | decimal? | 是 | - | 当前工序成本 |
| rejectCost | decimal? | 是 | - | 报废成本 |
| balanceCost | decimal? | 是 | - | 结存成本 |
| unitCostPreviousStep | decimal? | 是 | - | 上工序单位成本 |
| unitCost | decimal? | 是 | - | 当前单位成本 |
| unitCostEffective | decimal? | 是 | - | 有效单位成本 |
| unitCostStocked | decimal? | 是 | - | 入仓单位成本 |
| version | int? | 是 | - | - |
| initialCost | decimal? | 是 | - | 期初成本 |
| qtyOsReceived | int? | 是 | - | 外协接收数量 |
| initialCostToCal | decimal? | 是 | - | 期初总成本 |
| balaceCostOfLastPrdProcess | decimal? | 是 | - | - |
| overhead | decimal? | 是 | - | 公共费用 |
| qtyOsOutput | string | 是 | - | 外协数量 |
| miBom | string | 是 | - | 非bom费用 |
| qtyToBeStock | string | 是 | - | 期末待入库数 |
| qtyToBeStockInit | string | 是 | - | 期初待入库数 |
| costToBeStockInit | string | 是 | - | 期初待入库费用 |
| costToBeStock | string | 是 | - | 期末待入库费用 |
- **关联关系**：
  - F_AccCostWOBySteps.periodId = T_FiscalPeriod.recId
  - F_AccCostWOBySteps.stepId = T_Steps.recId
  - F_AccCostWOBySteps.woId = P_WO.recId
  - F_AccCostWOBySteps.processId = T_Process.recId
  - F_AccCostWOBySteps.processNumber = 序号.recId

---

#### 368 财务管理-财务数据-科目分组 ( F_AccountGroups )
- **业务含义**：财务管理-财务数据-科目分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| accountGroupName | string | 是 | - | 科目分组 |
| d_c | string | 是 | - | D:借贷   C 贷方 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 369 F_AccountProjects ( F_AccountProjects )
- **业务含义**：ERP 系统 F_AccountProjects 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| version | string | 是 | - | - |
| accountId | string | 是 | - | - |
| projectId | string | 是 | - | F_Accounts表multipleProjects='Department' 则projectId=T_Department表recId |
| current_b_period_credit | string | 是 | - | - |
| current_b_period_debit | string | 是 | - | - |
| current_beg_balance | string | 是 | - | - |
| current_end_balance | string | 是 | - | - |
| current_f_beg_balance | string | 是 | - | - |
| current_f_period_credit | string | 是 | - | - |
| current_f_period_debit | string | 是 | - | - |
| cyb_PL_Amount | string | 是 | - | - |
| cyb_beg_balance | string | 是 | - | - |
| cyb_credit | string | 是 | - | - |
| cyb_debit | string | 是 | - | - |
| cyb_end_balance | string | 是 | - | - |
| cyb_open | string | 是 | - | - |
| cyf_beg_balance | string | 是 | - | - |
| cyf_credit | string | 是 | - | - |
| cyf_debit | string | 是 | - | - |
| cyf_end_balance | string | 是 | - | - |
| cyf_open | string | 是 | - | - |
| cashProjectId | string | 是 | - | - |
| projectType | string | 是 | - | - |
| act_debit_1 | string | 是 | - | - |
| act_debit_2 | string | 是 | - | - |
| act_debit_3 | string | 是 | - | - |
| act_debit_4 | string | 是 | - | - |
| act_debit_5 | string | 是 | - | - |
| act_debit_6 | string | 是 | - | - |
| act_debit_7 | string | 是 | - | - |
| act_debit_8 | string | 是 | - | - |
| act_debit_9 | string | 是 | - | - |
| act_debit_10 | string | 是 | - | - |
| act_debit_11 | string | 是 | - | - |
| act_debit_12 | string | 是 | - | - |
| act_credit_1 | string | 是 | - | - |
| act_credit_2 | string | 是 | - | - |
| act_credit_3 | string | 是 | - | - |
| act_credit_4 | string | 是 | - | - |
| act_credit_5 | string | 是 | - | - |
| act_credit_6 | string | 是 | - | - |
| act_credit_7 | string | 是 | - | - |
| act_credit_8 | string | 是 | - | - |
| act_credit_9 | string | 是 | - | - |
| act_credit_10 | string | 是 | - | - |
| act_credit_11 | string | 是 | - | - |
| act_credit_12 | string | 是 | - | - |
| beg_balance_1 | string | 是 | - | 1月期初余额本币 |
| beg_balance_2 | string | 是 | - | 2月期初余额本币 |
| beg_balance_3 | string | 是 | - | 3月期初余额本币 |
| beg_balance_4 | string | 是 | - | 4月期初余额本币 |
| beg_balance_5 | string | 是 | - | 5月期初余额本币 |
| beg_balance_6 | string | 是 | - | - |
| beg_balance_7 | string | 是 | - | - |
| beg_balance_8 | string | 是 | - | - |
| beg_balance_9 | string | 是 | - | - |
| beg_balance_10 | string | 是 | - | - |
| beg_balance_11 | string | 是 | - | - |
| beg_balance_12 | string | 是 | - | - |
| end_balance_1 | string | 是 | - | 1月期末余额本币 |
| end_balance_2 | string | 是 | - | 2月期末余额本币 |
| end_balance_3 | string | 是 | - | 3月期末余额本币 |
| end_balance_... | string | 是 | - | 6月期末余额本币 |
| act_credit_ori | string | 是 | - | - |
| act_debit_ori | string | 是 | - | - |
| beg_balance_ori | string | 是 | - | - |
| end_balance_ori | string | 是 | - | - |
| oribeg_balance | string | 是 | - | - |
| oriend_balance | string | 是 | - | - |
| orib_period_credit | string | 是 | - | - |
| orib_period_debit | string | 是 | - | - |
| current_f_end_balance | string | 是 | - | - |
| orifbeg_balance | string | 是 | - | - |
| orifend_balance | string | 是 | - | - |
| act_credit_orif | string | 是 | - | - |
| act_debit_orif | string | 是 | - | - |
| beg_balance_orif | string | 是 | - | - |
| end_balance_orif | string | 是 | - | - |
| beg_balance_f1 | string | 是 | - | 1月原币期初 |
| beg_balance_f2 | string | 是 | - | 2月原币期初 |
| beg_balance_f3 | string | 是 | - | 2月原币期初 |
| beg_balance_f4 | string | 是 | - | 4月原币期初 |
| beg_balance_f5 | string | 是 | - | 5月原币期初 |
| beg_balance_f6 | string | 是 | - | - |
| beg_balance_f7 | string | 是 | - | - |
| beg_balance_f8 | string | 是 | - | - |
| beg_balance_f9 | string | 是 | - | - |
| beg_balance_f10 | string | 是 | - | - |
| beg_balance_f11 | string | 是 | - | - |
| beg_balance_f12 | string | 是 | - | - |
| act_debit_f1 | string | 是 | - | - |
| act_debit_f2 | string | 是 | - | - |
| act_debit_f3 | string | 是 | - | - |
| act_debit_f4 | string | 是 | - | - |
| act_debit_f5 | string | 是 | - | - |
| act_debit_f7 | string | 是 | - | - |
| act_debit_f8 | string | 是 | - | - |
| act_debit_f9 | string | 是 | - | - |
| act_debit_f10 | string | 是 | - | - |
| act_debit_f11 | string | 是 | - | - |
| act_debit_f12 | string | 是 | - | - |
| act_credit_f1 | string | 是 | - | - |
| act_credit_f2 | string | 是 | - | - |
| act_credit_f3 | string | 是 | - | - |
| act_credit_f4 | string | 是 | - | - |
| act_credit_f5 | string | 是 | - | - |
| act_credit_f6 | string | 是 | - | - |
| act_credit_f7 | string | 是 | - | - |
| act_credit_f8 | string | 是 | - | - |
| act_credit_f9 | string | 是 | - | - |
| act_credit_f10 | string | 是 | - | - |
| act_credit_f11 | string | 是 | - | - |
| act_credit_f12 | string | 是 | - | - |
| end_balance_f1 | string | 是 | - | 1月原币期末 |
| end_balance_f2 | string | 是 | - | 2月原币期末 |
| end_balance_f3 | string | 是 | - | 2月原币期末 |
| end_balance_f4 | string | 是 | - | 4月原币期末 |
| end_balance_f5 | string | 是 | - | 5月原币期末 |
| end_balance_f6 | string | 是 | - | - |
| end_balance_f7 | string | 是 | - | - |
| end_balance_f8 | string | 是 | - | - |
| end_balance_f9 | string | 是 | - | - |
| end_balance_f10 | string | 是 | - | - |
| end_balance_f11 | string | 是 | - | - |
| end_balance_f12 | string | 是 | - | - |
| oricyb_debit | string | 是 | - | - |
| oricyb_credit | string | 是 | - | - |
| oricyf_debit | string | 是 | - | - |
| oricyf_credit | string | 是 | - | - |
| ori_cyb_PL_Amount | string | 是 | - | - |
| curr_PL_Amount | string | 是 | - | - |
| pl_Amount1 | string | 是 | - | - |
| pl_Amount2 | string | 是 | - | - |
| pl_Amount3 | string | 是 | - | - |
| pl_Amount4 | string | 是 | - | - |
| pl_Amount5 | string | 是 | - | - |
| pl_Amount6 | string | 是 | - | - |
| pl_Amount7 | string | 是 | - | - |
| pl_Amount8 | string | 是 | - | - |
| pl_Amount9 | string | 是 | - | - |
| pl_Amount10 | string | 是 | - | - |
| pl_Amount11 | string | 是 | - | - |
| pl_Amount12 | string | 是 | - | - |
| cyb_debit_init | string | 是 | - | - |
| cyb_credit_init | string | 是 | - | - |
| cyf_debit_init | string | 是 | - | - |
| cyf_credit_init | string | 是 | - | - |
| cyb_PL_Amount_init | string | 是 | - | - |
- **关联关系**：无

---

#### 370 科目管理 ( F_Accounts )
- **业务含义**：科目管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| accountCode | string | 是 | - | 科目代码 |
| accountCourse | bool? | 是 | - | 记账科目 |
| accountDesc | string | 是 | - | 科目名称 |
| 1， | decimal? | 是 | - | 1月贷方 |
| act_credit_10 | decimal? | 是 | - | - |
| act_credit_11 | decimal? | 是 | - | - |
| act_credit_12 | decimal? | 是 | - | - |
| act_credit_2 | decimal? | 是 | - | - |
| act_credit_3 | decimal? | 是 | - | - |
| act_credit_4 | decimal? | 是 | - | - |
| act_credit_5 | decimal? | 是 | - | - |
| act_credit_6 | decimal? | 是 | - | - |
| act_credit_7 | decimal? | 是 | - | - |
| act_credit_8 | decimal? | 是 | - | - |
| act_credit_9 | decimal? | 是 | - | - |
| act_debit_1 | decimal? | 是 | - | 1月借方 |
| act_debit_10 | decimal? | 是 | - | - |
| act_debit_11 | decimal? | 是 | - | - |
| act_debit_12 | decimal? | 是 | - | - |
| act_debit_2 | decimal? | 是 | - | - |
| act_debit_3 | decimal? | 是 | - | - |
| act_debit_4 | decimal? | 是 | - | - |
| act_debit_5 | decimal? | 是 | - | - |
| act_debit_6 | decimal? | 是 | - | - |
| act_debit_7 | decimal? | 是 | - | - |
| act_debit_8 | decimal? | 是 | - | - |
| act_debit_9 | decimal? | 是 | - | - |
| beg_balance_1 | decimal? | 是 | - | 1月期初（本币） |
| beg_balance_10 | decimal? | 是 | - | 10月期初（本币） |
| beg_balance_11 | decimal? | 是 | - | 11月期初（本币） |
| beg_balance_12 | decimal? | 是 | - | 12月期初（本币） |
| beg_balance_2 | decimal? | 是 | - | 2月期初（本币） |
| beg_balance_3 | decimal? | 是 | - | 3月期初（本币） |
| beg_balance_4 | decimal? | 是 | - | - |
| beg_balance_5 | decimal? | 是 | - | - |
| beg_balance_6 | decimal? | 是 | - | - |
| beg_balance_7 | decimal? | 是 | - | - |
| beg_balance_8 | decimal? | 是 | - | - |
| beg_balance_9 | decimal? | 是 | - | - |
| current_b_period_credit | decimal? | 是 | - | 本币本期发生贷方     --过账后 |
| current_b_period_debit | decimal? | 是 | - | 本币本期发生借方     --过账后 |
| current_beg_balance | decimal? | 是 | - | 本币当期期初余额   --过账后 |
| current_end_balance | decimal? | 是 | - | 本币当期期末余额     --过账后 |
| current_f_period_credit | decimal? | 是 | - | 原币本期发生贷方       --过账后 |
| current_f_period_debit | decimal? | 是 | - | 原币本期发生借方       --过账后 |
| cyb_beg_balance | decimal? | 是 | - | 本币期初金额   --未过账 |
| cyb_credit | decimal? | 是 | - | 本币贷方  --未过账 |
| cyb_debit | decimal? | 是 | - | 本币借方  --未过账 |
| cyb_end_balance | decimal? | 是 | - | 本币期末金额  ---未过账 |
| cyb_open | decimal? | 是 | - | - |
| cyf_beg_balance | decimal? | 是 | - | - |
| cyf_credit | decimal? | 是 | - | - |
| cyf_debit | decimal? | 是 | - | - |
| cyf_end_balance | decimal? | 是 | - | - |
| cyf_open | decimal? | 是 | - | - |
| d_c | string | 是 | - | D:借方   C 贷方 |
| end_balance_1 | decimal? | 是 | - | 1月期末（本币） |
| end_balance_10 | decimal? | 是 | - | 10月期末（本币） |
| end_balance_11 | decimal? | 是 | - | 11月期末（本币） |
| end_balance_12 | decimal? | 是 | - | 12月期末（本币） |
| end_balance_2 | decimal? | 是 | - | 2月期末（本币） |
| end_balance_3 | decimal? | 是 | - | 3月期末（本币） |
| end_balance_4 | decimal? | 是 | - | 4月期末（本币） |
| end_balance_5 | decimal? | 是 | - | 5月期末（本币） |
| end_balance_6 | decimal? | 是 | - | 6月期末（本币） |
| end_balance_7 | decimal? | 是 | - | 7月期末（本币） |
| end_balance_8 | decimal? | 是 | - | 8月期末（本币） |
| end_balance_9 | decimal? | 是 | - | 9月期末（本币） |
| generalLedger | bool? | 是 | - | 总账科目 |
| inactive | bool? | 是 | - | 停止使用 |
| initializeDate | DateTime? | 是 | - | - |
| journal | string | 是 | - | - |
| lastModifyDate | DateTime? | 是 | - | 更新时间 |
| levels | int? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| multi_ColumnAccounts | bool? | 是 | - | 多栏帐科目'Department',则 t_department.recid |
| periodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| rootId | int? | 是 | - | 归属上一级别ID,也可以自身 |
| sourceId | int? | 是 | - | - |
| t_catagory | string | 是 | - | - |
| type | string | 是 | - | 类型：Customer 客户  Suppliers 供应商 MaterialGroup 物料分组  ProductGroup 产品分组 
ToolCategory  工具分类  Department 部门  SubcontractType 外协类型  AssetCategory  产品类别
Cost 成本中心  Other 其它项目 |
| version | int? | 是 | - | - |
| voucherProjctId | int? | 是 | - | 目标对象，对应F_VoucherProject.recId |
| accountGroupId | int? | 是 | - | 科目分组，对应F_AccountGroups.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| currencyId | int? | 是 | - | 货币表，对应T_Currency.recId |
| parentId | int? | 是 | - | 上级ID（父级id），对应F_Accounts.recId |
| projectCatagoryId | int? | 是 | - | 核算项目，对应F_ProjectCatagory.recId |
| mnemonicCode | string | 是 | - | 助词码 |
| finalExchange | bool? | 是 | ((0)) | 期末调汇 |
| cashFlow | bool? | 是 | ((0)) | 现金流量 |
| cyb_PL_Amount | decimal? | 是 | ((0)) | - |
| current_f_beg_balance | decimal? | 是 | ((0)) | - |
| current_f_end_balance | decimal? | 是 | ((0)) | - |
| beg_balance_f1 | decimal? | 是 | ((0)) | 1月期初（外币） |
| beg_balance_f2 | decimal? | 是 | ((0)) | 2月期初（外币） |
| beg_balance_f3 | decimal? | 是 | ((0)) | 3月期初（外币） |
| beg_balance_f4 | decimal? | 是 | ((0)) | 4月期初（外币） |
| beg_balance_f5 | decimal? | 是 | ((0)) | 5月期初（外币） |
| beg_balance_f6 | decimal? | 是 | ((0)) | 6月期初（外币） |
| beg_balance_f7 | decimal? | 是 | ((0)) | 7月期初（外币） |
| beg_balance_f8 | decimal? | 是 | ((0)) | - |
| beg_balance_f9 | decimal? | 是 | ((0)) | - |
| beg_balance_f10 | decimal? | 是 | ((0)) | - |
| beg_balance_f11 | decimal? | 是 | ((0)) | - |
| beg_balance_f12 | decimal? | 是 | ((0)) | - |
| act_debit_f1 | decimal? | 是 | ((0)) | - |
| act_debit_f2 | decimal? | 是 | ((0)) | - |
| act_debit_f3 | decimal? | 是 | ((0)) | - |
| act_debit_f4 | decimal? | 是 | ((0)) | - |
| act_debit_f5 | decimal? | 是 | ((0)) | - |
| act_debit_f6 | decimal? | 是 | ((0)) | - |
| act_debit_f7 | decimal? | 是 | ((0)) | - |
| act_debit_f8 | decimal? | 是 | ((0)) | - |
| act_debit_f9 | decimal? | 是 | ((0)) | - |
| act_debit_f10 | decimal? | 是 | ((0)) | - |
| act_debit_f11 | decimal? | 是 | ((0)) | - |
| act_debit_f12 | decimal? | 是 | ((0)) | - |
| act_credit_f1 | decimal? | 是 | ((0)) | - |
| act_credit_f2 | decimal? | 是 | ((0)) | - |
| act_credit_f3 | decimal? | 是 | ((0)) | - |
| act_credit_f4 | decimal? | 是 | ((0)) | - |
| act_credit_f5 | decimal? | 是 | ((0)) | - |
| act_credit_f6 | decimal? | 是 | ((0)) | - |
| act_credit_f7 | decimal? | 是 | ((0)) | - |
| act_credit_f8 | decimal? | 是 | ((0)) | - |
| act_credit_f9 | decimal? | 是 | ((0)) | - |
| act_credit_f10 | decimal? | 是 | ((0)) | - |
| act_credit_f11 | decimal? | 是 | ((0)) | - |
| act_credit_f12 | decimal? | 是 | ((0)) | - |
| end_balance_f1 | decimal? | 是 | ((0)) | 1月期末（外币） |
| end_balance_f2 | decimal? | 是 | ((0)) | 2月期末（外币） |
| end_balance_f3 | decimal? | 是 | ((0)) | 3月期末（外币） |
| end_balance_f4 | decimal? | 是 | ((0)) | 4月期末（外币） |
| end_balance_f5 | decimal? | 是 | ((0)) | 5月期末（外币） |
| end_balance_f6 | decimal? | 是 | ((0)) | 6月期末（外币） |
| end_balance_f7 | decimal? | 是 | ((0)) | - |
| end_balance_f8 | decimal? | 是 | ((0)) | - |
| end_balance_f9 | decimal? | 是 | ((0)) | - |
| end_balance_f10 | decimal? | 是 | ((0)) | - |
| end_balance_f11 | decimal? | 是 | ((0)) | - |
| end_balance_f12 | decimal? | 是 | ((0)) | - |
| oricyb_debit | decimal? | 是 | ((0)) | - |
| oricyb_credit | decimal? | 是 | ((0)) | - |
| oricyf_debit | decimal? | 是 | ((0)) | - |
| oricyf_credit | decimal? | 是 | ((0)) | - |
| ori_cyb_PL_Amount | decimal? | 是 | ((0)) | - |
| curr_PL_Amount | decimal? | 是 | ((0)) | - |
| pl_Amount1 | decimal? | 是 | ((0)) | - |
| pl_Amount2 | decimal? | 是 | ((0)) | - |
| pl_Amount3 | decimal? | 是 | ((0)) | - |
| pl_Amount4 | decimal? | 是 | ((0)) | - |
| pl_Amount5 | decimal? | 是 | ((0)) | - |
| pl_Amount6 | decimal? | 是 | ((0)) | - |
| pl_Amount7 | decimal? | 是 | ((0)) | - |
| pl_Amount8 | decimal? | 是 | ((0)) | - |
| pl_Amount9 | decimal? | 是 | ((0)) | - |
| pl_Amount10 | decimal? | 是 | ((0)) | - |
| pl_Amount11 | decimal? | 是 | ((0)) | - |
| pl_Amount12 | decimal? | 是 | ((0)) | - |
| multipleProjects | string | 是 | ('') | - |
- **关联关系**：
  - F_Accounts.periodId = T_FiscalPeriod.recId
  - F_Accounts.voucherProjctId = F_VoucherProject.recId
  - F_Accounts.accountGroupId = F_AccountGroups.recId
  - F_Accounts.companyId = T_Company.recId
  - F_Accounts.currencyId = T_Currency.recId
  - F_Accounts.parentId = F_Accounts.recId
  - F_Accounts.projectCatagoryId = F_ProjectCatagory.recId

---

#### 371 F_AllScrapWOCost ( F_AllScrapWOCost )
- **业务含义**：ERP 系统 F_AllScrapWOCost 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| calRkey | string | 是 | - | - |
| woId | string | 是 | - | 工单id |
| periodId | string | 是 | - | - |
| qtyPlanned | string | 是 | - | - |
| qtyStocked | string | 是 | - | - |
| qtyWIP | string | 是 | - | - |
| qtyRejected | string | 是 | - | - |
| rejectCost | string | 是 | - | 拒收成本 |
| totalCostofWO | string | 是 | - | 工单总成本 |
| balanceCost | string | 是 | - | - |
| unitCost | string | 是 | - | - |
| unitCostEffective | string | 是 | - | - |
| unitCostStocked | string | 是 | - | - |
| version | string | 是 | - | - |
| woStatus | string | 是 | - | - |
- **关联关系**：无

---

#### 372 供应商扣款 ( F_AP_DebitMemo )
- **业务含义**：供应商扣款
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| debitMemoAmount | decimal? | 是 | - | 含税金额 |
| debitMemoNumber | string | 是 | - | 扣款单号 |
| enterDate | DateTime? | 是 | - | 录入日期 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| ifReconcile | bool? | 是 | - | 是否已扣款 |
| invoiceId | int? | 是 | - | 采购发票 |
| invoicedAmount | decimal? | 是 | - | 发票金额 |
| isPercentage | bool? | 是 | - | 是否百分百 |
| markupValue | decimal? | 是 | - | - |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| myInvoiceId | int? | 是 | - | - |
| netAmount | decimal? | 是 | - | 未含税金额 |
| note | string | 是 | - | - |
| paymentId | int? | 是 | - | - |
| processedAmount | decimal? | 是 | - | - |
| reconcileId | int? | 是 | - | - |
| referenceNumber | string | 是 | - | - |
| returnOrderId | int? | 是 | - | 退货表，对应M_ReturnOrder.recId |
| rootId | int? | 是 | - | - |
| rootNo | string | 是 | - | - |
| shippingAmount | decimal? | 是 | - | 装运金额 |
| status | string | 是 | - | - |
| taxAmount | decimal? | 是 | - | 税金小计 |
| taxRate | decimal? | 是 | - | 税金 |
| transDate | DateTime? | 是 | - | 扣款日期 |
| type | string | 是 | - | Supplier |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币表，对应T_Currency.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| plantBusinessId | int? | 是 | - | 工厂业务，对应F_PlantBusiness.recId |
| plantBusinessItemId | int? | 是 | - | 工厂业务明细，对应F_PlantBusinessItem.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| targetId | int? | 是 | - | 工厂，对应T_Plants.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | string | 是 | - | - |
| approveVersion | string | 是 | - | - |
| flowTypeId | string | 是 | - | - |
| taxId | string | 是 | - | - |
| deductionId | string | 是 | - | - |
- **关联关系**：
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

#### 373 供应商扣款明细 ( F_AP_DebitMemoItem )
- **业务含义**：供应商扣款明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobId | int? | 是 | - | 对应S_Job.recId |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| poItemId | int? | 是 | - | 采购明细7，对应M_PurchaseOrderItem.FGI_Inventory |
| price | decimal? | 是 | - | 含税单价 |
| qtyDebit | decimal? | 是 | - | 扣款数量 |
| returnOrderItemId | int? | 是 | - | 退货表，对应M_ReturnOrderItem.recId |
| returnSOId | int? | 是 | - | 客诉表，对应S_ReturnSO.recId |
| subAmount | decimal? | 是 | - | 含税金额 |
| subNetAmount | decimal? | 是 | - | 不含税金额 |
| subTaxAmount | decimal? | 是 | - | 税金金额小计 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| debitMemoId | int? | 是 | - | 主表，对应F_AP_DebitMemo.recId |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
- **关联关系**：
  - F_AP_DebitMemoItem.jobId = S_Job.recId
  - F_AP_DebitMemoItem.poItemId = M_PurchaseOrderItem.recId
  - F_AP_DebitMemoItem.returnOrderItemId = M_ReturnOrderItem.recId
  - F_AP_DebitMemoItem.returnSOId = S_ReturnSO.recId
  - F_AP_DebitMemoItem.debitMemoId = F_AP_DebitMemo.recId
  - F_AP_DebitMemoItem.taxId = T_Tax.recId

---

#### 374 应付账款/付款管理 ( F_AP_Disburse )
- **业务含义**：应付账款/付款管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| address1 | string | 是 | - | 地址1 |
| address2 | string | 是 | - | - |
| address3 | string | 是 | - | - |
| analysisCode1 | string | 是 | - | 分析代码1 |
| analysisCode2 | string | 是 | - | - |
| analysisCode3 | string | 是 | - | - |
| analysisCode4 | string | 是 | - | - |
| analysisCode5 | string | 是 | - | - |
| avancedPayAmount | decimal? | 是 | - | 预付款金额 |
| checkDate | DateTime? | 是 | - | 付款日期 |
| checkNumber | string | 是 | - | 支票号 |
| createDate | DateTime? | 是 | - | 建单日期 |
| debitMemoAmount | decimal? | 是 | - | 扣款金额 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| invoiceAmount | decimal? | 是 | - | 应付金额 |
| modifyDate | DateTime? | 是 | - | - |
| note | string | 是 | - | - |
| payId | int? | 是 | - | - |
| payTo | string | 是 | - | - |
| poId | int? | 是 | - | - |
| poNo | string | 是 | - | - |
| sourceId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| sourceName | string | 是 | - | 支付方名称 |
| sourceType | string | 是 | - | 单据类型： |
| status | string | 是 | - | - |
| totalAmount | decimal? | 是 | - | 含税金额 |
| type | string | 是 | - | 收款类型：AvancedPay 预付款
DisburseWriteOff 杂项付款
STD 发票 Supplier 供应商 |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| bankAccountsId | int? | 是 | - | 资产管理，对应F_BankAccounts.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| modifyId | int? | 是 | - | 修改人，对应T_User.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 审批流程表，对应T_FlowType.recId |
| writeOffAmount | decimal? | 是 | ((0)) | 预付款金额 |
- **关联关系**：
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

#### 375 应付账款/付款管理明细 ( F_AP_DisburseItem )
- **业务含义**：应付账款/付款管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 支付金额（付款管理支付金额） |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| disburseId | int? | 是 | - | 主表，对应F_AP_Disburse.recId |
| invoiceId | int? | 是 | - | 发票主表，对应F_AP_Invoice.recId |
| soInvoiceId | int? | 是 | - | 对应F_AR_Invoice.recId |
- **关联关系**：
  - F_AP_DisburseItem.disburseId = F_AP_Disburse.recId
  - F_AP_DisburseItem.invoiceId = F_AP_Invoice.recId
  - F_AP_DisburseItem.soInvoiceId = F_AR_Invoice.recId

---

#### 376 采购发票 ( F_AP_Invoice )
- **业务含义**：采购发票
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| debitAmount | decimal? | 是 | - | 退货&扣款金额 |
| disburseAmount | decimal? | 是 | - | 支付金额（发票已付金额） |
| duedate | DateTime? | 是 | - | 到期日期 |
| enterDate | DateTime? | 是 | - | 录入日期（发票时间） |
| exchangeRate | decimal? | 是 | - | 汇率 |
| invoiceAmount | decimal? | 是 | - | 发票金额 |
| invoiceNumber | string | 是 | - | 发票号码 |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| netAmount | decimal? | 是 | - | 不含税金额 |
| note | string | 是 | - | - |
| outInvoiceNumber | string | 是 | - | 供应商发票号 |
| paidAmount | decimal? | 是 | - | 应付金额 |
| postedDate | DateTime? | 是 | - | 过帐日期 |
| rootId | int? | 是 | - | - |
| rootNo | string | 是 | - | - |
| shippingAmount | decimal? | 是 | - | 装运金额 |
| sourceType | string | 是 | - | 单据类型：WXPO外协，PO原材料，Misc杂项采购，Supplier供应商 |
| status | string | 是 | - | 单据状态：Valid生效，Active 活动 |
| subAmount | decimal? | 是 | - | 含税金额 |
| taxAmount | decimal? | 是 | - | 税金 |
| totalAmount | decimal? | 是 | - | 汇总 |
| transDate | DateTime? | 是 | - | 发票日期 |
| type | string | 是 | - | Supplier |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| targetId | int? | 是 | - | 目标工厂，对应T_Plants.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 流程表，对应T_FlowType.recId |
| taxId | int? | 是 | - | 税率表，对应T_tax.recId |
| taxRate | decimal? | 是 | ((0)) | 税率 |
| plantsCode | string | 是 | ('') | - |
| importData | bool? | 是 | ((0)) | - |
- **关联关系**：
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

#### 377 采购发票明细 ( F_AP_InvoiceItem )
- **业务含义**：采购发票明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Receivables | decimal? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售表，对应S_ContractSo.recId |
| ifMis | bool? | 是 | - | - |
| ifMised | bool? | 是 | - | - |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| netAmount | decimal? | 是 | - | 不含税金额 |
| netPrice | decimal? | 是 | - | 不含税单价 |
| note | string | 是 | - | - |
| packingSlipItemContractSOId | int? | 是 | - | 对应F_PackingSlipItemContractSO.recId |
| packingSlipItemId | int? | 是 | - | 对应M_MaterialPackingSlipItem.recId |
| poItemId | int? | 是 | - | 采购明细表，对应M_PurchaseOrderItem.FGI_Inventory |
| price | decimal? | 是 | - | 含税单价 |
| qtyFree | int? | 是 | - | 赠品数量 |
| qtyInvoiced | decimal? | 是 | - | 开票数量 |
| qty_Receivables | decimal? | 是 | - | 对账数量 |
| receiptItemId | int? | 是 | - | 采购接收表，对应M_ReceiptItem.recId |
| reconcileItemId | int? | 是 | - | 采购对账明细，对应F_AP_ReconcileItems.recId |
| reconcileNumber | string | 是 | - | 发票号码 |
| subAmount | decimal? | 是 | - | 原含税金额小计 |
| taxAmount | decimal? | 是 | - | 税金小计 |
| taxRate | decimal? | 是 | - | 税率 |
| totalAmount | decimal? | 是 | - | 原含税金额+税金小计=小计汇总 |
| version | int? | 是 | - | - |
| apInvoiceId | int? | 是 | - | 主表，对应F_AP_Invoice.recId |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
| importData | bool? | 是 | ((0)) | - |
- **关联关系**：
  - F_AP_InvoiceItem.contractSOId = S_ContractSo.recId
  - F_AP_InvoiceItem.packingSlipItemContractSOId = F_PackingSlipItemContractSO.recId
  - F_AP_InvoiceItem.packingSlipItemId = M_MaterialPackingSlipItem.recId
  - F_AP_InvoiceItem.poItemId = M_PurchaseOrderItem.recId
  - F_AP_InvoiceItem.receiptItemId = M_ReceiptItem.recId
  - F_AP_InvoiceItem.reconcileItemId = F_AP_ReconcileItems.recId
  - F_AP_InvoiceItem.apInvoiceId = F_AP_Invoice.recId
  - F_AP_InvoiceItem.taxId = T_Tax.recId

---

#### 378 采购对账 ( F_AP_Reconcile )
- **业务含义**：采购对账
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| accountPayableAmount | decimal? | 是 | - | 应付金额 |
| addAmount | decimal? | 是 | - | 额外费用 |
| advancePaymentAmount | decimal? | 是 | - | 预付款金额 |
| cutoffDate | DateTime? | 是 | - | 截止日期 |
| debitAmount | decimal? | 是 | - | 退货&扣款金额 |
| enterDate | DateTime? | 是 | - | 录入日期 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| netAmount | decimal? | 是 | - | 未含税金额 |
| note | string | 是 | - | - |
| reconcileNumber | string | 是 | - | 对账单号 |
| sourceType | string | 是 | - | PO 原材料 ，WXPO外协 |
| status | string | 是 | - | Valid生效Active 活动 |
| subAmount | decimal? | 是 | - | 含税金额小计 |
| taxAmount | decimal? | 是 | - | 税金小计 |
| totalAmount | decimal? | 是 | - | 含税金额小计+税金小计 = 汇总 |
| type | string | 是 | - | ReceivedDate |
| version | int? | 是 | - | 修改次数 |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | 审批状态：Approved审批通过，Pending制作中 |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 流程表，对应T_flowType.recId |
| plantsCode | string | 是 | ('') | - |
- **关联关系**：
  - F_AP_Reconcile.companyId = T_Company.recId
  - F_AP_Reconcile.creatorId = T_User.recId
  - F_AP_Reconcile.currencyId = T_Currency.recId
  - F_AP_Reconcile.fiscalPeriodId = T_FiscalPeriod.recId
  - F_AP_Reconcile.plantsId = T_Plants.recId
  - F_AP_Reconcile.postRoleId = T_PostRole.recId
  - F_AP_Reconcile.suppliersId = M_Suppliers.recId
  - F_AP_Reconcile.flowTypeId = T_flowType.recId

---

#### 379 采购对账明细 ( F_AP_ReconcileItems )
- **业务含义**：采购对账明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addAmount | decimal? | 是 | - | 额外金额 |
| amount_Add | decimal? | 是 | - | - |
| amount_Invoiced | decimal? | 是 | - | 对账金额 |
| confirm | bool? | 是 | - | - |
| contractSOId | int? | 是 | - | 对应S_ContractSO.recId |
| ifMis | bool? | 是 | - | - |
| ifMised | bool? | 是 | - | - |
| note | string | 是 | - | - |
| packingSlipItemContractSOId | int? | 是 | - | 对应F_PackingSlipItemContractSO.recId |
| packingSlipItemId | int? | 是 | - | 对应FGI_PackingSlipItem.recId |
| qtyFree | int? | 是 | - | 赠品数量 |
| qty_Invoiced | decimal? | 是 | - | - |
| qty_Receivables | decimal? | 是 | - | 预付数量 |
| receiptItemId | int? | 是 | - | 接收表，对应M_ReceiptItem.recId |
| reconcileQty | decimal? | 是 | - | 对账数量 |
| totalAmount | decimal? | 是 | - | 含税金额 |
| version | int? | 是 | - | - |
| reconcileId | int? | 是 | - | 主表，对应F_AP_Reconcile.recId |
| price | decimal? | 是 | ((0)) | 含税单价 |
| taxRate | decimal? | 是 | ((0)) | 税率 |
| netPrice | decimal? | 是 | ((0)) | 不含税单价 |
| dataRev | int? | 是 | ((1)) | - |
| taxVal | decimal? | 是 | ((0)) | - |
| totalInTax | decimal? | 是 | ((0)) | 含税金额 |
| totalNoTax | decimal? | 是 | ((0)) | 不含税金额 |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
| itemNum | int? | 是 | - | 序号 |
- **关联关系**：
  - F_AP_ReconcileItems.contractSOId = S_ContractSO.recId
  - F_AP_ReconcileItems.packingSlipItemContractSOId = F_PackingSlipItemContractSO.recId
  - F_AP_ReconcileItems.packingSlipItemId = FGI_PackingSlipItem.recId
  - F_AP_ReconcileItems.receiptItemId = M_ReceiptItem.recId
  - F_AP_ReconcileItems.reconcileId = F_AP_Reconcile.recId
  - F_AP_ReconcileItems.taxId = T_Tax.recId

---

#### 380 客户扣款（对账和发票） ( F_AR_CreditMemo )
- **业务含义**：客户扣款（对账和发票）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| anlysisCode1 | string | 是 | - | 自定义数据1 |
| anlysisCode2 | string | 是 | - | 自定义数据2 |
| anlysisCode3 | string | 是 | - | 自定义数据3 |
| creditMemoAmount | decimal? | 是 | - | 含税金额 |
| creditMemoNumber | string | 是 | - | 扣款单号 |
| enterDate | DateTime? | 是 | - | 扣款日期 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| ifReconcile | bool? | 是 | - | 是否已经对账 |
| invoiceId | int? | 是 | - | 采购发票表，对应F_AP_Invoice.recId |
| isPercentage | bool? | 是 | - | 是否百分比 |
| markupValue | decimal? | 是 | - | 标记值 |
| miscAmount | decimal? | 是 | - | 杂项税金 |
| myInvoiceId | int? | 是 | - | - |
| netAmount | decimal? | 是 | - | 未含税金额 |
| note | string | 是 | - | 备注 |
| paymentId | int? | 是 | - | - |
| printedDate | DateTime? | 是 | - | 打印日期 |
| reconcileId | int? | 是 | - | 销售对账主表，对应F_AR_SOReconcile.recId |
| rootId | int? | 是 | - | - |
| rootNo | string | 是 | - | - |
| shippingAmount | decimal? | 是 | - | 装运数量 |
| status | string | 是 | - | Valid 生效  Active 活动 |
| taxAmount | decimal? | 是 | - | 税金小计 |
| taxRate | decimal? | 是 | - | 税率 |
| transDate | DateTime? | 是 | - | 扣款日期 |
| type | string | 是 | - | 类型：Customer |
| version | int? | 是 | - | - |
| anlysisUserId | int? | 是 | - | 使用人，对应T_User.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户，对应S_Customer.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| plantBusinessId | int? | 是 | - | 工厂业务，对应F_PlantBusiness.recId |
| plantBusinessItemId | int? | 是 | - | 工厂业务明细，对应F_PlantBusinessItem.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| targetId | int? | 是 | - | 目标工厂，对应T_Plants.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 流程表，对应T_FlowType.recId |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
| deductionId | int? | 是 | - | 扣款类型表，对应T_ModuleType.recId |
- **关联关系**：
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

#### 381 客户扣款明细 ( F_AR_CreditMemoItem )
- **业务含义**：客户扣款明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jobId | int? | 是 | - | - |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| price | decimal? | 是 | - | 单价 |
| qtyCredit | int? | 是 | - | 扣款数量 |
| returnSOId | int? | 是 | - | 客诉管理--扣款明细，对应S_ReturnSO.recId |
| seq | int? | 是 | - | - |
| subAmount | decimal? | 是 | - | 含税金额 |
| subNetAmount | decimal? | 是 | - | 不含税金额 |
| subTaxAmount | decimal? | 是 | - | 税金 |
| taxRate | decimal? | 是 | - | 税率 |
| version | int? | 是 | - | - |
| creditMemoId | int? | 是 | - | 客户扣款，对应F_AR_CreditMemo.recId |
| taxId | int? | 是 | - | - |
- **关联关系**：
  - F_AR_CreditMemoItem.returnSOId = S_ReturnSO.recId
  - F_AR_CreditMemoItem.creditMemoId = F_AR_CreditMemo.recId

---

#### 382 财务管理-财务应用-应收账款-销售发票 ( F_AR_Invoice )
- **业务含义**：财务管理-财务应用-应收账款-销售发票
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | - |
| addChargeAmount | decimal? | 是 | - | 额外费用 |
| custPOId | int? | 是 | - | - |
| debitAmount | decimal? | 是 | - | 退货&扣款金额 |
| discountAmount | decimal? | 是 | - | 折扣金额 |
| duedate | DateTime? | 是 | - | 到期日期 |
| enterDate | DateTime? | 是 | - | 录入日期 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| invoiceAmount | decimal? | 是 | - | 发票金额 |
| invoiceNumber | string | 否 | - | 发票号 |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| netAmount | decimal? | 是 | - | 不含税金额 |
| note | string | 是 | - | 备注 |
| outInvoiceNumber | string | 是 | - | 客户发票号 |
| paidAmount | decimal? | 是 | - | 应收金额 |
| postedDate | DateTime? | 是 | - | 过帐日期 |
| receivableAmount | decimal? | 是 | - | 应收账款 |
| rootId | int? | 是 | - | - |
| rootNo | string | 是 | - | - |
| shippingAmount | decimal? | 是 | - | 装运金额 |
| sourceType | string | 否 | - | 单据类型：Customer  客户  Product 成品  Material 原材料 |
| status | string | 否 | - | Active 活动，Valid 生效 |
| subAmount | decimal? | 是 | - | 发票金额小计 |
| taxAmount | decimal? | 是 | - | 税金金额小计 |
| totalAmount | decimal? | 是 | - | 发票金额小计+税金金额小计 = 汇总 |
| transDate | DateTime? | 是 | - | 发票日期 |
| type | string | 否 | - | 类型：Reconcile 对账单  Customer 客户 |
| version | int? | 是 | - | - |
| companyId | int | 否 | - | 公司，对应T_Company.recId |
| creatorId | int | 否 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int | 否 | - | 客户，对应S_Customer.recId |
| paymentTermId | int? | 是 | - | 付款周期，对应T_PaymentTerm.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int | 否 | - | 岗位，对应T_PostRole.recId |
| targetId | int? | 是 | - | 目标工厂，对应T_Plants.recId |
| taxRate | decimal? | 是 | - | 税率 |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | 审批状态 ：Approved审批通过，Pending制作中 |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | string | 是 | - | - |
| approveVersion | string | 是 | - | - |
| flowTypeId | string | 是 | - | 流程表，对应T_FlowType.recId |
| taxId | string | 是 | - | 税率表，对应T_Tax.recId |
| plantsCode | string | 是 | - | - |
| importData | string | 是 | - | - |
- **关联关系**：
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

#### 383 销售发票明细 ( F_AR_InvoiceItem )
- **业务含义**：销售发票明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | - |
| addChargeAmount | decimal? | 是 | - | 额外费用 |
| amount_Receivables | decimal? | 是 | - | - |
| discountAmount | decimal? | 是 | - | 折扣金额 |
| ifMis | bool? | 是 | - | - |
| ifMised | bool? | 是 | - | - |
| jobId | int? | 是 | - | 本厂型号表，对应S_JOB.recId |
| materialPackingSlipItemId | int? | 是 | - | - |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| netAmount | decimal? | 是 | - | 未含税金额 |
| netPrice | decimal? | 是 | - | 不含税单价 |
| packingSlipItemContractSOId | int? | 是 | - | - |
| price | decimal? | 是 | - | 含税动脑筋 |
| qtyFree | int? | 是 | - | 赠品送货数量 |
| qtyInvoiced | decimal? | 是 | - | 开票数量 |
| soReconcileItemId | int? | 是 | - | 销售对账明细，对应F_AR_SOReconcileItems.recId |
| reconcileNumber | string | 是 | - | 发票号码 |
| subAmount | decimal? | 是 | - | 含税金额 |
| taxAmount | decimal? | 是 | - | 含税单价 |
| taxRate | decimal? | 是 | - | 税率 |
| totalAmount | decimal? | 是 | - | 发票金额 |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售表，对应S_ContractSO.recId |
| invoiceId | int | 否 | - | 销售发票主表，对应F_AR_Invoice.recId |
| packingSlipItemId | int | 否 | - | 成品出货明细，对应FGI_PackingSlipItem.recId |
| taxId | string | 是 | - | 税率表，对应T_Tax.recId |
- **关联关系**：
  - F_AR_InvoiceItem.jobId = S_JOB.recId
  - F_AR_InvoiceItem.soReconcileItemId = F_AR_SOReconcileItems.recId
  - F_AR_InvoiceItem.contractSOId = S_ContractSO.recId
  - F_AR_InvoiceItem.invoiceId = F_AR_Invoice.recId
  - F_AR_InvoiceItem.packingSlipItemId = FGI_PackingSlipItem.recId
  - F_AR_InvoiceItem.taxId = T_Tax.recId

---

#### 384 收款管理 ( F_AR_Receivable )
- **业务含义**：收款管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| address1 | string | 是 | - | 地址1 |
| address2 | string | 是 | - | - |
| address3 | string | 是 | - | - |
| analysisCode1 | string | 是 | - | 分析代码1 |
| analysisCode2 | string | 是 | - | - |
| analysisCode3 | string | 是 | - | - |
| analysisCode4 | string | 是 | - | - |
| analysisCode5 | string | 是 | - | - |
| avancedPayAmount | decimal? | 是 | - | 预付款金额 |
| checkDate | DateTime? | 是 | - | 收款日期 |
| checkNumber | string | 是 | - | 支票号 |
| createDate | DateTime? | 是 | - | 建单日期 |
| creditMemoAmount | decimal? | 是 | - | 扣款金额 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| invoiceAmount | decimal? | 是 | - | 发票金额 |
| modifyDate | DateTime? | 是 | - | 修改日期 |
| note | string | 是 | - | 备注 |
| payId | int? | 是 | - | - |
| payTo | string | 是 | - | - |
| soId | int? | 是 | - | - |
| soNo | string | 是 | - | - |
| sourceId | int? | 是 | - | - |
| sourceName | string | 是 | - | - |
| sourceType | string | 是 | - | 对应S_Customer.recId |
| status | string | 是 | - | - |
| totalAmount | decimal? | 是 | - | 收款金额 |
| type | string | 是 | - | 收款类型：AvancedPay 预收款
ReceivableWriteOff  杂项收款
STD 发票 Customer 客户 |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| bankAccountsId | int? | 是 | - | 现金账户表，对应F_BankAccounts.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| modifyId | int? | 是 | - | 修改人，对应T_User.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| sourceCode | string | 是 | - | - |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 审批流程表，对应T_FlowType.recId |
| writeOffAmount | decimal? | 是 | ((0)) | - |
- **关联关系**：
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

#### 385 收款管理明细 ( F_AR_ReceivableItem )
- **业务含义**：收款管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 金额 |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| invoiceId | int? | 是 | - | 销售发票，对应F_AR_Invoice.recId |
| receivableId | int? | 是 | - | 收款管理，对应F_AR_Receivable.recId |
| poInvoiceId | int? | 是 | - | 对应F_AP_Invoice.recId |
- **关联关系**：
  - F_AR_ReceivableItem.invoiceId = F_AR_Invoice.recId
  - F_AR_ReceivableItem.receivableId = F_AR_Receivable.recId
  - F_AR_ReceivableItem.poInvoiceId = F_AP_Invoice.recId

---

#### 386 财务管理-财务应用-应收账款-销售对账 ( F_AR_SOReconcile )
- **业务含义**：财务管理-财务应用-应收账款-销售对账
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| accountPayableAmount | decimal? | 是 | - | 应收金额 |
| addAmount | decimal? | 是 | - | 额外费用 |
| advancePaymentAmount | decimal? | 是 | - | 预付款金额 |
| cutoffDate | DateTime? | 是 | - | 截止日期 |
| debitAmount | decimal? | 是 | - | 退货&扣款金额 |
| discountAmount | decimal? | 是 | - | 折扣费用 |
| enterDate | DateTime? | 是 | - | 录入日期 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| invoicedAmount | decimal? | 是 | - | 发票金额 |
| miscAmount | decimal? | 是 | - | 杂项金额 |
| netAmount | decimal? | 是 | - | 未含税金额 |
| note | string | 是 | - | 备注 |
| reconcileNumber | string | 是 | - | 对账单号 |
| status | string | 是 | - | Active  活动   Valid 生效 |
| subAmount | decimal? | 是 | - | 含税金额 |
| taxAmount | decimal? | 是 | - | 税金 |
| totalAmount | decimal? | 是 | - | 对账金额汇总 |
| type | string | 是 | - | Product  成品 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司表，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| customerId | int? | 是 | - | 客户表，对应S_Customer.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| piId | string | 是 | - | - |
| pdId | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | 审批状态 Approved：审批通过 Pending：制作中 Submit :提交 |
| additionalStatus | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| uuid | string | 是 | - | - |
| enableApproval | bool? | 是 | ((0)) | - |
| approveVersion | int? | 是 | ((0)) | - |
| flowTypeId | int? | 是 | - | 流程表，对应T_flowType.recId |
| plantsCode | string | 是 | ('') | - |
- **关联关系**：
  - F_AR_SOReconcile.companyId = T_Company.recId
  - F_AR_SOReconcile.creatorId = T_User.recId
  - F_AR_SOReconcile.currencyId = T_Currency.recId
  - F_AR_SOReconcile.customerId = S_Customer.recId
  - F_AR_SOReconcile.fiscalPeriodId = T_FiscalPeriod.recId
  - F_AR_SOReconcile.plantsId = T_Plants.recId
  - F_AR_SOReconcile.postRoleId = T_PostRole.recId
  - F_AR_SOReconcile.flowTypeId = T_flowType.recId

---

#### 387 销售对账明细 ( F_AR_SOReconcileItems )
- **业务含义**：销售对账明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addAmount | decimal? | 是 | - | 额外费用 |
| amount_Add | decimal? | 是 | - | - |
| amount_Invoiced | decimal? | 是 | - | - |
| confirm | bool? | 是 | - | 是否确认 |
| discountAmount | decimal? | 是 | - | 折旧金额 |
| ifMis | bool? | 是 | - | - |
| ifMised | bool? | 是 | - | - |
| materialPackingSlipItemId | int? | 是 | - | - |
| miscAmount | decimal? | 是 | - | - |
| note | string | 是 | - | 备注 |
| packingSlipItemContractSOId | int? | 是 | - | - |
| qtyFree | int? | 是 | - | 赠品送货数量 |
| qty_Invoiced | decimal? | 是 | - | 已开发票数量 |
| reconcileQty | decimal? | 是 | - | 对账数量 |
| totalAmount | decimal? | 是 | - | 对账金额 |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售表，对应S_ContractSO.recId |
| packingSlipItemId | int? | 是 | - | 成品出货明细，对应FGI_PackingSlipItem.recId |
| soReconcileId | int? | 是 | - | 主表，对应F_AR_SOReconcile.recId |
| price | decimal? | 是 | ((0)) | 含税单价 |
| taxRate | decimal? | 是 | ((0)) | 税率 |
| netPrice | decimal? | 是 | ((0)) | 不含税单价 |
| dataRev | int? | 是 | ((1)) | - |
| taxVal | decimal? | 是 | ((0)) | 税金 |
| totalInTax | decimal? | 是 | ((0)) | 含税金额 |
| totalNoTax | decimal? | 是 | ((0)) | 未含税金额 |
| taxId | int? | 是 | - | 税率表，对应T_Tax.recId |
| ttype | int? | 是 | ((1)) | - |
| begToBeReconciledId | int? | 是 | - | - |
| itemNum | int? | 是 | - | 序号 |
| k_addToolCost | decimal? | 是 | ((0)) | 订单额外费用 |
- **关联关系**：
  - F_AR_SOReconcileItems.contractSOId = S_ContractSO.recId
  - F_AR_SOReconcileItems.packingSlipItemId = FGI_PackingSlipItem.recId
  - F_AR_SOReconcileItems.soReconcileId = F_AR_SOReconcile.recId
  - F_AR_SOReconcileItems.taxId = T_Tax.recId

---

#### 388 财务管理-资产管理-资产类别明细表 ( F_AssetCategoryItem )
- **业务含义**：财务管理-资产管理-资产类别明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| assetAccountId | int? | 是 | - | 对应F_Accounts.recId |
| assetCategoryId | int? | 是 | - | 对应F_AssetCategorys.recId |
| depAddAcountId | int? | 是 | - | 对应F_Accounts.recId |
| depDisposalAccountId | int? | 是 | - | 对应F_Accounts.recId |
| depExpenseAccountId | int? | 是 | - | 对应F_Accounts.recId |
| plantsId | int? | 是 | - | 对应T_Plants.recId |
| prefix | string | 是 | - | 单据前缀 |
| numberMedian | int? | 是 | ((5)) | 流水号位数 |
| serialNumber | int? | 是 | ((0)) | 流水号 |
- **关联关系**：
  - F_AssetCategoryItem.assetAccountId = F_Accounts.recId
  - F_AssetCategoryItem.assetCategoryId = F_AssetCategorys.recId
  - F_AssetCategoryItem.depAddAcountId = F_Accounts.recId
  - F_AssetCategoryItem.depDisposalAccountId = F_Accounts.recId
  - F_AssetCategoryItem.depExpenseAccountId = F_Accounts.recId
  - F_AssetCategoryItem.plantsId = T_Plants.recId

---

#### 389 财务管理-资产管理-资产类别 ( F_AssetCategorys )
- **业务含义**：财务管理-资产管理-资产类别
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| acceleratedfactor | decimal? | 是 | - | 加速因子 |
| assetCatName | string | 是 | - | 资产类别名称 |
| depMethod | string | 是 | - | 折旧方式：Straight-Line 直线 Units-of-Units 产量法
No-Dep 不计提  Accelerated 加速 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| monthsOfLife | int? | 是 | - | 使用月份 |
| netSalvageValue | decimal? | 是 | - | 净残值率 |
| prefix | string | 是 | - | 编号前缀 |
| version | int? | 是 | - | - |
| assetAccountId | int? | 是 | - | 对应F_Accounts.recId |
| depAddAcountId | int? | 是 | - | 对应F_Accounts.recId |
| depExpenseAccountId | int? | 是 | - | 对应F_Accounts.recId |
- **关联关系**：
  - F_AssetCategorys.assetAccountId = F_Accounts.recId
  - F_AssetCategorys.depAddAcountId = F_Accounts.recId
  - F_AssetCategorys.depExpenseAccountId = F_Accounts.recId

---

#### 390 资产变动管理 ( F_AssetChange )
- **业务含义**：资产变动管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| createDate | DateTime? | 是 | - | - |
| enableApproval | bool? | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| reason | string | 是 | - | - |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| version | int? | 是 | - | - |
| assetChangeWayId | int? | 是 | - | 资产变动方式，对应F_AssetChangeWays.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fixedAssetId | int? | 是 | - | 固定资产，对应F_FixedAssets.recId |
| flowTypeId | int? | 是 | - | 流程表，对应T_FlowType.recId |
| postRoleId | int? | 是 | - | 岗位表，对应T_PostRole.recId |
- **关联关系**：
  - F_AssetChange.assetChangeWayId = F_AssetChangeWays.recId
  - F_AssetChange.companyId = T_Company.recId
  - F_AssetChange.creatorId = T_User.recId
  - F_AssetChange.fixedAssetId = F_FixedAssets.recId
  - F_AssetChange.flowTypeId = T_FlowType.recId
  - F_AssetChange.postRoleId = T_PostRole.recId

---

#### 391 F_AssetChangeHistory ( F_AssetChangeHistory )
- **业务含义**：ERP 系统 F_AssetChangeHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 392 资产变动管理明细 ( F_AssetChangeItem )
- **业务含义**：资产变动管理明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| boolValue | bool? | 是 | - | - |
| changeValue | string | 是 | - | - |
| dateValue | DateTime? | 是 | - | - |
| fieldName | string | 是 | - | 字段名称 |
| fileType | string | 是 | - | 数值类型：List 下拉框  Integer 整数值 Float 小数 |
| floatValue | decimal? | 是 | - | - |
| ideas | string | 是 | - | - |
| intValue | int? | 是 | - | - |
| note | string | 是 | - | - |
| oldValue | string | 是 | - | 原值 |
| oldValueText | string | 是 | - | 变动值 |
| sort | int? | 是 | - | - |
| textValue | string | 是 | - | - |
| version | int? | 是 | - | - |
| assetChangeId | int? | 是 | - | 主表，对应F_AssetChange.recId |
- **关联关系**：
  - F_AssetChangeItem.assetChangeId = F_AssetChange.recId

---

#### 393 资产变动方式 ( F_AssetChangeWays )
- **业务含义**：资产变动方式
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| changeWayDesc | string | 是 | - | 资产变动描述 |
| lastModifyDate | DateTime? | 是 | - | 最后修改日期 |
| modifiedBy | string | 是 | - | 修改人 |
| version | int? | 是 | - | - |
| wayType | string | 是 | - | 变动方式：Add  增加  Del 减少 |
- **关联关系**：无

---

#### 394 F_AssetChangeWF ( F_AssetChangeWF )
- **业务含义**：ERP 系统 F_AssetChangeWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 395 资产清理 ( F_AssetDisposal )
- **业务含义**：资产清理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| disposalAmount | decimal? | 是 | - | 清理费用 |
| disposalDate | DateTime? | 是 | - | 清理时间 |
| disposalQuantity | decimal? | 是 | - | 清理数量 |
| exchRate | decimal? | 是 | - | 税率 |
| netAmount | decimal? | 是 | - | 残值收入 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 状态：Active |
| taxAmount | decimal? | 是 | - | 汇总 |
| taxRate | decimal? | 是 | - | 税金 |
| version | int? | 是 | - | - |
| assetChangeWayId | int? | 是 | - | 资产变动方式，对应F_AssetChangeWays.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 用户表，对应T_User.recId |
| currencyId | int? | 是 | - | 货币表，对应T_Currency.recId |
| fixedAssetId | int? | 是 | - | 固定资产，对应F_FixedAssets.recId |
| postRoleId | int? | 是 | - | 岗位表，对应T_PostRole.recId |
- **关联关系**：
  - F_AssetDisposal.assetChangeWayId = F_AssetChangeWays.recId
  - F_AssetDisposal.companyId = T_Company.recId
  - F_AssetDisposal.creatorId = T_User.recId
  - F_AssetDisposal.currencyId = T_Currency.recId
  - F_AssetDisposal.fixedAssetId = F_FixedAssets.recId
  - F_AssetDisposal.postRoleId = T_PostRole.recId

---

#### 396 资产状态 ( F_AssetStatus )
- **业务含义**：资产状态
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| assetStatus | string | 是 | - | 资产状态描述 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 397 现金账户 ( F_BankAccounts )
- **业务含义**：现金账户
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ba_accountNo | string | 是 | - | 银行账号 |
| ba_address | string | 是 | - | 银行地址 |
| ba_name | string | 是 | - | 账号名称 |
| ba_nickName | string | 是 | - | 账号简称 |
| ba_telephone | string | 是 | - | 电话 |
| base_Current_Amount | decimal? | 是 | - | 本币金额 |
| contact1_email | string | 是 | - | 联系邮件1 |
| contact1_name | string | 是 | - | 联系人1 |
| contact1_tel | string | 是 | - | 联系电话1 |
| contact2_email | string | 是 | - | 联系邮件2 |
| contact2_name | string | 是 | - | 联系人2 |
| contact2_tel | string | 是 | - | 联系电话2 |
| nextCheckNumber | string | 是 | - | 下一支票(付款) |
| org_Current_Amount | decimal? | 是 | - | 原币金额 |
| org_beg_balance | decimal? | 是 | - | - |
| org_end_balance | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| ba_accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| bankReconcileSetingId | int? | 是 | - | 对应F_BankReconcileSeting.recId |
| companyId | int? | 是 | - | 恭喜，对应T_Company.recId |
| currencyId | int? | 是 | - | 货币表，对应T_Currency.recId |
| loss_accountId | int? | 是 | - | 汇兑损益表，对应F_Accounts.recId |
| defPayment | bool? | 是 | ((0)) | 默认付款账号 |
| defReceivable | bool? | 是 | ((0)) | 默认收款账号 |
| nextCheckNumber2 | string | 是 | - | 下一支票(收款) |
| suffix | string | 是 | - | - |
| suffix2 | string | 是 | - | - |
| tmonth | int? | 是 | ((0)) | - |
| tmonth2 | int? | 是 | ((0)) | - |
- **关联关系**：
  - F_BankAccounts.ba_accountId = F_Accounts.recId
  - F_BankAccounts.bankReconcileSetingId = F_BankReconcileSeting.recId
  - F_BankAccounts.companyId = T_Company.recId
  - F_BankAccounts.currencyId = T_Currency.recId
  - F_BankAccounts.loss_accountId = F_Accounts.recId

---

#### 398 银行对账 ( F_BankReconcile )
- **业务含义**：银行对账
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| bankReconcileSetingId | int? | 是 | - | 银行对账配置，对应F_BankReconcileSeting.recId |
| code | string | 是 | - | 银行对账账号 |
| createDate | DateTime? | 是 | - | 建单日期 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | - |
| version | int? | 是 | - | - |
| bankAccountsId | int? | 是 | - | 现金账户，对应F_BankAccounts.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位表，对应T_PostRole.recId |
- **关联关系**：
  - F_BankReconcile.bankReconcileSetingId = F_BankReconcileSeting.recId
  - F_BankReconcile.bankAccountsId = F_BankAccounts.recId
  - F_BankReconcile.companyId = T_Company.recId
  - F_BankReconcile.creatorId = T_User.recId
  - F_BankReconcile.fiscalPeriodId = T_FiscalPeriod.recId
  - F_BankReconcile.postRoleId = T_PostRole.recId

---

#### 399 银行对账明细 ( F_BankReconcileItem )
- **业务含义**：银行对账明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| checked | bool? | 是 | - | - |
| note | string | 是 | - | - |
| p1 | string | 是 | - | - |
| p10 | string | 是 | - | - |
| p11 | string | 是 | - | - |
| p12 | string | 是 | - | - |
| p13 | string | 是 | - | - |
| p14 | string | 是 | - | - |
| p15 | string | 是 | - | - |
| p16 | string | 是 | - | - |
| p17 | string | 是 | - | - |
| p18 | string | 是 | - | - |
| p19 | string | 是 | - | - |
| p2 | string | 是 | - | - |
| p20 | string | 是 | - | - |
| p21 | string | 是 | - | - |
| p22 | string | 是 | - | - |
| p23 | string | 是 | - | - |
| p24 | string | 是 | - | - |
| p25 | string | 是 | - | - |
| p26 | string | 是 | - | - |
| p27 | string | 是 | - | - |
| p28 | string | 是 | - | - |
| p29 | string | 是 | - | - |
| p3 | string | 是 | - | - |
| p30 | string | 是 | - | - |
| p4 | string | 是 | - | - |
| p5 | string | 是 | - | - |
| p6 | string | 是 | - | - |
| p7 | string | 是 | - | - |
| p8 | string | 是 | - | - |
| p9 | string | 是 | - | - |
| rowNo | int? | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| bankReconcileId | int? | 是 | - | 对应F_BankReconcile.recId |
- **关联关系**：
  - F_BankReconcileItem.bankReconcileId = F_BankReconcile.recId

---

#### 400 银行对账配置 ( F_BankReconcileSeting )
- **业务含义**：银行对账配置
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| colStart | int? | 是 | - | 列坐标 |
| cols | int? | 是 | - | 列数 |
| name | string | 是 | - | 银行名称 |
| note | string | 是 | - | 备注 |
| rowStart | int? | 是 | - | 行坐标 |
- **关联关系**：无

---

#### 401 银行对账配置明细 ( F_BankReconcileSetingItem )
- **业务含义**：银行对账配置明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| fieldName | string | 是 | - | 字段名称 |
| fieldSeq | int? | 是 | - | - |
| note | string | 是 | - | - |
| systemFied | string | 是 | - | 日期   Date
结算方式 AccountSettle
结算号 SettleNumber
摘要 Desc
对方账号 TargetAccount
借方金额 DebitAmount
贷方金额 CreditAmount |
| bankReconcileSetingId | int? | 是 | - | 主表，对应F_BankReconcileSeting.recId |
- **关联关系**：
  - F_BankReconcileSetingItem.bankReconcileSetingId = F_BankReconcileSeting.recId

---

#### 402 现金账流水 ( F_CashAccount )
- **业务含义**：现金账流水
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| attachQty | int? | 是 | - | - |
| billNumber | string | 是 | - | - |
| closeCashAccountId | int? | 是 | - | - |
| createDate | DateTime? | 是 | - | - |
| description | string | 是 | - | - |
| exchRate | decimal? | 是 | - | - |
| orgAmount | decimal? | 是 | - | - |
| status | string | 是 | - | - |
| transType | string | 是 | - | - |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 对应F_Accounts.recId |
| bankAccountsId | int? | 是 | - | 对应F_BankAccounts.recId |
| companyId | int? | 是 | - | 对应T_Company.recId |
| creatorId | int? | 是 | - | 对应T_User.recId |
| currencyId | int? | 是 | - | 对应T_Currency.recId |
| fiscalPeriodId | int? | 是 | - | 对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 对应T_PostRole.recId |
| projectCatagoryItemId | int? | 是 | - | 对应F_ProjectCatagoryItem.recId |
| voucherId | int? | 是 | - | - |
- **关联关系**：
  - F_CashAccount.accountId = F_Accounts.recId
  - F_CashAccount.bankAccountsId = F_BankAccounts.recId
  - F_CashAccount.companyId = T_Company.recId
  - F_CashAccount.creatorId = T_User.recId
  - F_CashAccount.currencyId = T_Currency.recId
  - F_CashAccount.fiscalPeriodId = T_FiscalPeriod.recId
  - F_CashAccount.postRoleId = T_PostRole.recId
  - F_CashAccount.projectCatagoryItemId = F_ProjectCatagoryItem.recId

---

#### 403 现金账流水明细 ( F_CashAccountItem )
- **业务含义**：现金账流水明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| description | string | 是 | - | - |
| exchRate | decimal? | 是 | - | - |
| orgAmount | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 对应F_Accounts.recId |
| cashAccountId | int? | 是 | - | 对应F_CashAccount.recId |
| currencyId | int? | 是 | - | 对应T_Currency.recId |
| projectCatagoryItemId | int? | 是 | - | 对应F_ProjectCatagoryItem.recId |
| voucherItemId | int? | 是 | - | - |
- **关联关系**：
  - F_CashAccountItem.accountId = F_Accounts.recId
  - F_CashAccountItem.cashAccountId = F_CashAccount.recId
  - F_CashAccountItem.currencyId = T_Currency.recId
  - F_CashAccountItem.projectCatagoryItemId = F_ProjectCatagoryItem.recId

---

#### 404 出纳管理/现金账 ( F_CloseCashAccount )
- **业务含义**：出纳管理/现金账
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| billNumber | string | 是 | - | 现金账号 |
| createDate | DateTime? | 是 | - | 建单日期 |
| cutOffDate | DateTime? | 是 | - | 截止日期 |
| note | string | 是 | - | - |
| status | string | 是 | - | - |
| transType | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
- **关联关系**：
  - F_CloseCashAccount.companyId = T_Company.recId
  - F_CloseCashAccount.creatorId = T_User.recId
  - F_CloseCashAccount.currencyId = T_Currency.recId
  - F_CloseCashAccount.postRoleId = T_PostRole.recId

---

#### 405 出纳管理/现金账明细 ( F_CloseCashAccountItem )
- **业务含义**：出纳管理/现金账明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| cashAccountId | int? | 是 | - | 现金账流水，对应F_CashAccount.recId |
| closeCashAccountId | int? | 是 | - | 现金账，对应F_CloseCashAccount.recId |
| cashAccountItemId | int? | 是 | - | 现金账流水明细，对应F_CashAccountItem.recId |
- **关联关系**：
  - F_CloseCashAccountItem.cashAccountId = F_CashAccount.recId
  - F_CloseCashAccountItem.closeCashAccountId = F_CloseCashAccount.recId
  - F_CloseCashAccountItem.cashAccountItemId = F_CashAccountItem.recId

---

#### 406 期末调汇 ( F_CurrExchAdj )
- **业务含义**：期末调汇
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | - |
| adjDate | DateTime? | 是 | - | 调整日期 |
| ifDone | bool? | 是 | - | 是否完成 1：完成  0：未完成 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| companyId | string | 是 | - | 公司，对应T_Company.recId |
| sysExchRate | bool? | 是 | ((0)) | 是否系统汇率 |
- **关联关系**：
  - F_CurrExchAdj.creatorId = T_User.recId
  - F_CurrExchAdj.currencyId = T_Currency.recId
  - F_CurrExchAdj.fiscalPeriodId = T_FiscalPeriod.recId
  - F_CurrExchAdj.companyId = T_Company.recId

---

#### 407 期末调汇明细 ( F_CurrExchAdjItem )
- **业务含义**：期末调汇明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| adjRate | string | 是 | - | 调整汇率（当月汇率） |
| currencyItemId | string | 是 | - | 原货币（上期id），对应F_CurrExchAdjItem.recId |
| note | string | 是 | - | - |
| orgRate | string | 是 | - | 上期汇率 |
| version | string | 是 | - | - |
| currExchAdjId | string | 是 | - | 主表，对应F_CurrExchAdj.recId |
| currencyId | string | 是 | - | 调整后的货币，对应T_Currency.recId |
| voucherId | int? | 是 | - | 凭证主表，对应F_Voucher.recId |
- **关联关系**：
  - F_CurrExchAdjItem.currencyItemId = F_CurrExchAdjItem.recId
  - F_CurrExchAdjItem.currExchAdjId = F_CurrExchAdj.recId
  - F_CurrExchAdjItem.currencyId = T_Currency.recId
  - F_CurrExchAdjItem.voucherId = F_Voucher.recId

---

#### 408 折旧计提 ( F_Depreciation )
- **业务含义**：折旧计提
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | 折旧金额汇总 |
| createDate | DateTime? | 是 | - | 建单日期 |
| note | string | 是 | - | - |
| status | string | 是 | - | 状态： Active |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司表，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位表，对应T_PostRole.recId |
- **关联关系**：
  - F_Depreciation.companyId = T_Company.recId
  - F_Depreciation.creatorId = T_User.recId
  - F_Depreciation.fiscalPeriodId = T_FiscalPeriod.recId
  - F_Depreciation.postRoleId = T_PostRole.recId

---

#### 409 折旧计提明细表 ( F_DepreciationItem )
- **业务含义**：折旧计提明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| note | string | 是 | - | - |
| version | int? | 是 | - | - |
| depAddAcountId | int? | 是 | - | 借方科目表，对应F_Accounts.recId |
| depExpenseAccountId | int? | 是 | - | 贷方科目表，对应F_Accounts.recId |
| depreciationId | int? | 是 | - | 主表，对应F_Depreciation.recId |
| fixedAssetsId | int? | 是 | - | 固定资产，对应F_FixedAssets.recId |
- **关联关系**：
  - F_DepreciationItem.depAddAcountId = F_Accounts.recId
  - F_DepreciationItem.depExpenseAccountId = F_Accounts.recId
  - F_DepreciationItem.depreciationId = F_Depreciation.recId
  - F_DepreciationItem.fixedAssetsId = F_FixedAssets.recId

---

#### 410 凭证登记 ( F_DiaryAccount )
- **业务含义**：凭证登记
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| additionalStatus | string | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| approvedDate | DateTime? | 是 | - | - |
| copys | int? | 是 | - | 份数 |
| createDate | DateTime? | 是 | - | 建单日期 |
| creditAmount | decimal? | 是 | - | 贷方金额 |
| debitAmount | decimal? | 是 | - | 借方金额 |
| diaryAccountNumber | string | 是 | - | 日记账单号 |
| enCodeId | string | 是 | - | 编号规则 |
| enableApproval | bool? | 是 | - | - |
| fiscalMonth | int? | 是 | - | 月 |
| fiscalYear | int? | 是 | - | 年 |
| ifChangeOrgCurrVal | bool? | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postedDate | DateTime? | 是 | - | - |
| referenceCode | string | 是 | - | 摘要 |
| sourceId | int? | 是 | - | - |
| sourceType | string | 是 | - | DiaryAccount |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | - |
| transType | string | 是 | - | 凭证类型：Pay 付  Change 转 Receive 收 |
| type | string | 是 | - | DiaryAccount |
| version | int? | 是 | - | - |
| approvedId | int? | 是 | - | 审批人，对应T_User.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间表，对应T_FiscalPeriod.recId |
| flowTypeId | int? | 是 | - | 审批流程表，对应T_FlowType.recId |
| postRoleId | int? | 是 | - | 岗位表，对应T_PostRole.recId |
| postedId | int? | 是 | - | 建单人所在岗位表，对应T_User.recId |
| templateId | int? | 是 | - | - |
| voucherId | int? | 是 | - | - |
- **关联关系**：
  - F_DiaryAccount.approvedId = T_User.recId
  - F_DiaryAccount.companyId = T_Company.recId
  - F_DiaryAccount.creatorId = T_User.recId
  - F_DiaryAccount.fiscalPeriodId = T_FiscalPeriod.recId
  - F_DiaryAccount.flowTypeId = T_FlowType.recId
  - F_DiaryAccount.postRoleId = T_PostRole.recId
  - F_DiaryAccount.postedId = T_User.recId

---

#### 411 F_DiaryAccountHistory ( F_DiaryAccountHistory )
- **业务含义**：ERP 系统 F_DiaryAccountHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 412 凭证登记明细表 ( F_DiaryAccountItem )
- **业务含义**：凭证登记明细表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| creditAmount | decimal? | 是 | - | 贷方金额 |
| debitAmount | decimal? | 是 | - | 借方金额 |
| description | string | 是 | - | 描述 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| ideas | string | 是 | - | - |
| orgCurrAmount | decimal? | 是 | - | - |
| org_CreditAmount | decimal? | 是 | - | - |
| org_DebitAmount | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| diaryAccountId | int? | 是 | - | 主表，对应F_DiaryAccount.recId |
| projectId | int? | 是 | - | - |
| voucherTemplateId | int? | 是 | - | - |
| cashProjectId | int? | 是 | - | - |
| projectType | int? | 是 | ((0)) | - |
| voucherItemId | int? | 是 | - | 凭证明细，对应F_VoucherItem.recId |
- **关联关系**：
  - F_DiaryAccountItem.accountId = F_Accounts.recId
  - F_DiaryAccountItem.currencyId = T_Currency.recId
  - F_DiaryAccountItem.diaryAccountId = F_DiaryAccount.recId
  - F_DiaryAccountItem.voucherItemId = F_VoucherItem.recId

---

#### 413 F_DiaryAccountWF ( F_DiaryAccountWF )
- **业务含义**：ERP 系统 F_DiaryAccountWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 414 固定资产 ( F_FixedAssets )
- **业务含义**：固定资产
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| assetsName | string | 是 | - | 资产名称 |
| assetsNumber | string | 是 | - | 资产编号 |
| bookingDate | DateTime? | 是 | - | 入库时间 |
| createDate | DateTime? | 是 | - | 建单时间 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| fileId | string | 是 | - | - |
| hasUsePeriod | int? | 是 | - | 已使用期间数 |
| impairment | decimal? | 是 | - | 减值准备 |
| localAmount | decimal? | 是 | - | 本币金额 |
| manufacturer | string | 是 | - | 制造商 |
| netAmount | decimal? | 是 | - | 净额 |
| netValue | decimal? | 是 | - | 净值 |
| note | string | 是 | - | 备注 |
| oriAmount | decimal? | 是 | - | 原币金额 |
| oriModAmount | decimal? | 是 | - | - |
| preNetResidual | decimal? | 是 | - | 预计净残值 |
| preUsePeriod | int? | 是 | - | 预计使用期间数 |
| production | string | 是 | - | - |
| purchaseAmount | decimal? | 是 | - | 购进金额 |
| purchaseOldAmount | decimal? | 是 | - | 购进累计折旧 |
| quantity | decimal? | 是 | - | 数量 |
| serialNumber | string | 是 | - | 流水号 |
| specifications | string | 是 | - | 规格 |
| status | string | 是 | - | Expire  折旧中 Active 活动 Sell 出售 |
| suppliersName | string | 是 | - | 供应商名称 |
| totalDepreciation | decimal? | 是 | - | 累计折旧 |
| useDate | DateTime? | 是 | - | 使用日期 |
| version | int? | 是 | - | - |
| assetCategoryId | int? | 是 | - | 资产类别，对应F_AssetCategorys.recId |
| assetChangeWayId | int? | 是 | - | 资产变动方式，对应F_AssetChangeWays.recId |
| assetStatusId | int? | 是 | - | 资产状态，对应F_AssetStatus.recId |
| assetUseId | int? | 是 | - | 等级管理表，对应T_Cate.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| currencyId | int? | 是 | - | 货币，对应T_Currency.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| storageLocationId | int? | 是 | - | 对应T_Cate.recId |
| suppliersId | int? | 是 | - | 供应商表，对应M_Suppliers.recId |
| unitId | int? | 是 | - | 对应T_Unit.recId |
| depMethod | string | 是 | - | - |
| netSalvageValue | decimal? | 是 | ((0)) | 尽残值率% |
| stopDepreciation | bool? | 是 | ((0)) | 是否停止折旧计提 |
| equipmentId | string | 是 | - | 设备id，对应EQ_Equipments.recId |
- **关联关系**：
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

#### 415 固定资产明细 ( F_FixedAssetsItem )
- **业务含义**：固定资产明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | 备注 |
| proportion | decimal? | 是 | - | 比例系数 |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| departmentId | int? | 是 | - | 部门设置表，对应T_Department.recId |
| fixedAssetsId | int? | 是 | - | 主表，对应F_FixedAssets.recId |
- **关联关系**：
  - F_FixedAssetsItem.accountId = F_Accounts.recId
  - F_FixedAssetsItem.departmentId = T_Department.recId
  - F_FixedAssetsItem.fixedAssetsId = F_FixedAssets.recId

---

#### 416 科目设定 ( F_GL_Setting )
- **业务含义**：科目设定
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| jt_Code | string | 是 | - | 代码 |
| jt_Name | string | 是 | - | 名称 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| sysFlg | int? | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司表，对应T_Company.recId |
- **关联关系**：
  - F_GL_Setting.companyId = T_Company.recId

---

#### 417 科目设定明细 ( F_GL_SettingItem )
- **业务含义**：科目设定明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| seq | int? | 是 | - | - |
| ttype | string | 是 | - | 类型：Income 费用结转  Invest 收入结转 Profit 投资结转
MFGCost 制造费用  MFGWork 在制品结转
OperatingCost 营业成本结转   Cost 利润分配 |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 原科目表，对应F_Accounts.recId |
| desAccountId | int? | 是 | - | 目的科目表，对应F_Accounts.recId |
| gl_SettingId | int? | 是 | - | 科目设定主表，对应F_GL_Setting.recId |
- **关联关系**：
  - F_GL_SettingItem.accountId = F_Accounts.recId
  - F_GL_SettingItem.desAccountId = F_Accounts.recId
  - F_GL_SettingItem.gl_SettingId = F_GL_Setting.recId

---

#### 418 结存表 ( F_LastPeriodWoBalanceCost )
- **业务含义**：结存表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| periodId | string | 是 | - | 期间id，对应T_FiscalPeriod.recId |
| woId | string | 是 | - | 工单id，对应P_WO.recId |
| processNumber | string | 是 | - | - |
| stepId | string | 是 | - | 工序id，对应T_Steps.recId |
| processId | string | 是 | - | 工艺id，对应T_Process.recId |
| qtyBalance | string | 是 | - | 结存数 |
| balanceCost | string | 是 | - | 结存成本（期末成本） |
| unitCost | string | 是 | - | 单位成本 |
| pcsMIBOMCost | string | 是 | - | - |
| version | string | 是 | - | - |
| companyId | string | 是 | - | 公司id，对应T_Company.recId |
- **关联关系**：
  - F_LastPeriodWoBalanceCost.periodId = T_FiscalPeriod.recId
  - F_LastPeriodWoBalanceCost.woId = P_WO.recId
  - F_LastPeriodWoBalanceCost.stepId = T_Steps.recId
  - F_LastPeriodWoBalanceCost.processId = T_Process.recId
  - F_LastPeriodWoBalanceCost.companyId = T_Company.recId

---

#### 419 F_PackingSlipItemContractSO ( F_PackingSlipItemContractSO )
- **业务含义**：ERP 系统 F_PackingSlipItemContractSO 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount_Invoiced | decimal? | 是 | - | - |
| amount_Invoiced2 | decimal? | 是 | - | - |
| amount_Reconciled | decimal? | 是 | - | - |
| amount_Reconciled2 | decimal? | 是 | - | - |
| qtyFree_Invoiced | int? | 是 | - | - |
| qtyFree_Invoiced2 | int? | 是 | - | - |
| qtyFree_Reconciled | int? | 是 | - | - |
| qtyFree_Reconciled2 | int? | 是 | - | - |
| qty_Invoiced | int? | 是 | - | - |
| qty_Invoiced2 | int? | 是 | - | - |
| qty_Reconciled | int? | 是 | - | - |
| qty_Reconciled2 | int? | 是 | - | - |
| qtyofShipFree | int? | 是 | - | - |
| qtyofShipOrdered | int? | 是 | - | - |
| shippedDate | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| contractSOId | int? | 是 | - | 销售表，对应S_ContractSO.recId |
| packingSlipItemId | int? | 是 | - | 成品出货明细，对应FGI_PackingSlipItem.recId |
| qtyPCSReturnReceipt | int? | 是 | - | - |
- **关联关系**：
  - F_PackingSlipItemContractSO.contractSOId = S_ContractSO.recId
  - F_PackingSlipItemContractSO.packingSlipItemId = FGI_PackingSlipItem.recId

---

#### 420 请款单 ( F_PaymentRequest )
- **业务含义**：请款单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 421 销售单位、财务设置里面的业务类型 ( F_PlantBusiness )
- **业务含义**：销售单位、财务设置里面的业务类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | - |
| businessCode | string | 是 | - | 业务代码 |
| businessName | string | 是 | - | 业务名称 |
| sort | int? | 是 | - | - |
| type | string | 是 | - | 业务类型  应付 ap，应收 ar |
| version | int? | 是 | - | - |
| plantId | int? | 是 | - | 业务主体，对应T_Plants.recId |
| targetId | int? | 是 | - | 目标主体，对应T_Plants.recId |
- **关联关系**：
  - F_PlantBusiness.plantId = T_Plants.recId
  - F_PlantBusiness.targetId = T_Plants.recId

---

#### 422 工厂业务明细 ( F_PlantBusinessItem )
- **业务含义**：工厂业务明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | - |
| ifMake | bool? | 是 | - | - |
| ifMatPO | bool? | 是 | - | - |
| ifPO | bool? | 是 | - | - |
| ifReceive | bool? | 是 | - | - |
| isPercentage | bool? | 是 | - | - |
| markupValue | decimal? | 是 | - | - |
| stepSeq | int? | 是 | - | - |
| version | int? | 是 | - | - |
| currencyId | int? | 是 | - | 对应T_Currency.recId |
| plantBusinessId | int | 否 | - | 对应F_PlantBusiness.recId |
| providerId | int? | 是 | - | 供体，对应T_Plants.recId |
| tradingBusinessId | int? | 是 | - | 对应F_TradingBusiness.recId |
- **关联关系**：
  - F_PlantBusinessItem.currencyId = T_Currency.recId
  - F_PlantBusinessItem.plantBusinessId = F_PlantBusiness.recId
  - F_PlantBusinessItem.providerId = T_Plants.recId
  - F_PlantBusinessItem.tradingBusinessId = F_TradingBusiness.recId

---

#### 423 出纳扎账&财务过账 ( F_Post )
- **业务含义**：出纳扎账&财务过账
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| note | string | 是 | - | - |
| postDate | DateTime? | 是 | - | 扎账日期 |
| postType | string | 是 | - | 出纳扎账：CashierAccount   财务过账： GLPost  成本结转：CarryoverLoss   期末结账：ClosingAccount |
| version | int? | 是 | - | - |
| voucherIds | string | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| status | int? | 是 | ((0)) | - |
- **关联关系**：
  - F_Post.companyId = T_Company.recId
  - F_Post.creatorId = T_User.recId
  - F_Post.fiscalPeriodId = T_FiscalPeriod.recId
  - F_Post.postRoleId = T_PostRole.recId

---

#### 424 出纳扎账明细 ( F_PostItem )
- **业务含义**：出纳扎账明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| b_period_credit | decimal? | 是 | - | 本期发生金额--贷方 |
| b_period_debit | decimal? | 是 | - | 本期发生金额--借方 |
| beg_balance | decimal? | 是 | - | 期初余额--借方 |
| end_balance | decimal? | 是 | - | 期末余额--借方 |
| orib_period_credit | decimal? | 是 | - | - |
| orib_period_debit | decimal? | 是 | - | - |
| oribeg_balance | decimal? | 是 | - | - |
| oriend_balance | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| postId | int? | 是 | - | 主表，对应F_Post.recId |
| act_credit_ori | decimal? | 是 | ((0)) | - |
| act_debit_ori | decimal? | 是 | ((0)) | - |
| beg_balance_ori | decimal? | 是 | ((0)) | - |
| end_balance_ori | decimal? | 是 | ((0)) | - |
| voucherItemIds | string | 是 | - | - |
| orifbeg_balance | decimal? | 是 | ((0)) | 期初余额--贷方 |
| orifend_balance | decimal? | 是 | ((0)) | 期末余额--贷方 |
| orif_period_credit | decimal? | 是 | ((0)) | - |
| orif_period_debit | decimal? | 是 | ((0)) | - |
| fbeg_balance | decimal? | 是 | ((0)) | - |
| fend_balance | decimal? | 是 | ((0)) | - |
| f_period_credit | decimal? | 是 | ((0)) | - |
| f_period_debit | decimal? | 是 | ((0)) | - |
| act_credit_orif | decimal? | 是 | ((0)) | - |
| act_debit_orif | decimal? | 是 | ((0)) | - |
| beg_balance_orif | decimal? | 是 | ((0)) | - |
| end_balance_orif | decimal? | 是 | ((0)) | - |
- **关联关系**：
  - F_PostItem.accountId = F_Accounts.recId
  - F_PostItem.postId = F_Post.recId

---

#### 425 核算项目 ( F_ProjectCatagory )
- **业务含义**：核算项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| name | string | 是 | - | 名称 |
| type | string | 是 | - | 类型 现金流量 CashFlow   其它项目 Other |
| version | int? | 是 | - | - |
| seq | int? | 是 | ((0)) | 排序 |
| companyId | int? | 是 | - | 公司表，对应T_Company.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| cyb_beg_balance | decimal? | 是 | ((0)) | - |
| cyb_add_in | decimal? | 是 | ((0)) | - |
| cyb_add_out | decimal? | 是 | ((0)) | - |
| current_beg_balance | decimal? | 是 | ((0)) | - |
| current_b_period_in | decimal? | 是 | ((0)) | - |
| current_b_period_out | decimal? | 是 | ((0)) | - |
- **关联关系**：
  - F_ProjectCatagory.companyId = T_Company.recId
  - F_ProjectCatagory.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 426 核算项目明细 ( F_ProjectCatagoryItem )
- **业务含义**：核算项目明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| catCode | string | 是 | - | 分类码 |
| ifAccount | bool? | 是 | - | 是否结算 |
| in_out | string | 是 | - | 流向（IN  OUT） |
| prjItemCode | string | 是 | - | 项目代码 |
| prjItemName | string | 是 | - | 项目名称 |
| seq | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
| projectCatagoryId | int? | 是 | - | 核算项目主表，对应F_ProjectCatagory.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| cyb_beg_balance | decimal? | 是 | ((0)) | - |
| cyb_add_in | decimal? | 是 | ((0)) | - |
| cyb_add_out | decimal? | 是 | ((0)) | - |
| current_beg_balance | decimal? | 是 | ((0)) | - |
| current_b_period_in | decimal? | 是 | ((0)) | - |
| current_b_period_out | decimal? | 是 | ((0)) | - |
- **关联关系**：
  - F_ProjectCatagoryItem.projectCatagoryId = F_ProjectCatagory.recId
  - F_ProjectCatagoryItem.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 427 应付暂估 ( F_ProvisionalEstimate )
- **业务含义**：应付暂估
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| enterDate | DateTime? | 是 | - | - |
| estimateNumber | string | 是 | - | 单据号 |
| note | string | 是 | - | - |
| status | string | 是 | - | - |
| type | int? | 是 | - | - |
| uuid | string | 是 | - | - |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| netAmount | decimal? | 是 | ((0)) | 未含税金额 |
| subAmount | decimal? | 是 | ((0)) | 含税金额 |
| taxAmount | decimal? | 是 | ((0)) | 税金 |
| addChargeAmount | decimal? | 是 | ((0)) | - |
| miscAmount | decimal? | 是 | ((0)) | - |
| totalAmount | decimal? | 是 | ((0)) | 合计金额 |
| discountAmount | decimal? | 是 | ((0)) | - |
| orderType | int? | 是 | ((0)) | WIP=2 杂项=4 标准寄售=1 成品=3 |
- **关联关系**：
  - F_ProvisionalEstimate.companyId = T_Company.recId
  - F_ProvisionalEstimate.creatorId = T_User.recId
  - F_ProvisionalEstimate.fiscalPeriodId = T_FiscalPeriod.recId
  - F_ProvisionalEstimate.postRoleId = T_PostRole.recId

---

#### 428 应付暂估明细 ( F_ProvisionalEstimateItem )
- **业务含义**：应付暂估明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| addChargeAmount | decimal? | 是 | - | 额外费用 |
| contractMaterialsId | int? | 是 | - | - |
| contractSOId | int? | 是 | - | - |
| custContractNumber | string | 是 | - | 客户合同编号 |
| discountAmount | decimal? | 是 | - | - |
| exchRate | decimal? | 是 | - | - |
| localAmount | decimal? | 是 | - | 本币金额 |
| materialPackingSlipItemId | int? | 是 | - | - |
| miscAmount | decimal? | 是 | - | - |
| netAmount | decimal? | 是 | - | 不含税金额 |
| netPrice | decimal? | 是 | - | 不含税单价 |
| oriPrice | decimal? | 是 | - | 原含税价 |
| packingSlipItemContractSOId | int? | 是 | - | - |
| packingSlip_Numer | string | 是 | - | - |
| plantCode | string | 是 | - | - |
| poItemId | int? | 是 | - | 采购明细，对应M_PurchaseOrderItem.FGI_Inventory |
| price | decimal? | 是 | - | 含税价格 |
| qty | decimal? | 是 | - | 数量 |
| qtyOrder | decimal? | 是 | - | 订单数量 |
| qtyShiped | decimal? | 是 | - | 接收数量 |
| receiptDate | DateTime? | 是 | - | 接收时间 |
| receiptItemId | int? | 是 | - | 接收表id  orderType=（4，1） 对应M_ReceiptItem， orderType=（2，3） 对应FGI_ReceiptItem |
| receiptNumer | string | 是 | - | 接收单号 |
| shipDate | DateTime? | 是 | - | - |
| soNumber | string | 是 | - | 销售单号 |
| subAmount | decimal? | 是 | - | 含税金额 |
| taxAmount | decimal? | 是 | - | 税金 |
| taxId | int? | 是 | - | - |
| taxRate | decimal? | 是 | - | - |
| totalAmount | decimal? | 是 | - | 小计 |
| type | string | 是 | - | - |
| warehoueingNumber | string | 是 | - | 入仓单号（物料） |
| currencyId | int? | 是 | - | 对应T_Currency.recId |
| customerId | int? | 是 | - | 对应S_Customer.recId |
| jobId | int? | 是 | - | 对应S_Job.recId |
| materialsId | int? | 是 | - | 对应M_Materials.recId |
| provisionalEstimateId | int? | 是 | - | 对应F_ProvisionalEstimate.recId |
| salesPartId | int? | 是 | - | 对应S_SalesParts.recId |
| suppliersId | int? | 是 | - | 对应M_Suppliers.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
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

#### 429 凭证摘要 ( F_RefLib )
- **业务含义**：凭证摘要
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| classLevel | int? | 是 | - | 级别 |
| note | string | 是 | - | 备注 |
| refCode | string | 是 | - | 代码 |
| refDesc | string | 是 | - | 名称 |
| rootId | int? | 是 | - | - |
| version | int? | 是 | - | - |
| parentId | int? | 是 | - | 上级ID，对应F_RefLib.recId |
- **关联关系**：
  - F_RefLib.parentId = F_RefLib.recId

---

#### 430 交易业务 ( F_TradingBusiness )
- **业务含义**：交易业务
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| stepDesc | string | 是 | - | 流程描述 |
| toType | string | 是 | - | - |
| version | string | 是 | - | - |
| fromId | string | 是 | - | 主体，对应T_Plants.recId |
| toId | string | 是 | - | 客体，对应T_Plants.recId |
- **关联关系**：
  - F_TradingBusiness.fromId = T_Plants.recId
  - F_TradingBusiness.toId = T_Plants.recId

---

#### 431 凭证 ( F_Voucher )
- **业务含义**：凭证
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 记录主键 |
| additionalStatus | string | 是 | - | 记录版本 |
| approveStatus | string | 是 | - | 审批状态 |
| approveVersion | int? | 是 | - | 流程重审版本 |
| approvedDate | DateTime? | 是 | - | 审批日期 |
| copys | int? | 是 | - | 份数 |
| createDate | DateTime? | 是 | - | 创建日期 |
| creditAmount | decimal? | 是 | - | 贷方本币金额 |
| debitAmount | decimal? | 是 | - | 借方本币金额 |
| enCodeId | string | 是 | - | 编号规则 |
| enableApproval | bool? | 是 | - | 提交审批 |
| fiscalMonth | int? | 是 | - | 月份 |
| fiscalYear | int? | 是 | - | 年份 |
| ifChangeOrgCurrVal | bool? | 是 | - | 是否修改本币金额时不该变原币金额 |
| originalStatus | string | 是 | - | 原始状态 |
| pdId | string | 是 | - | 审批流pdId |
| piId | string | 是 | - | 审批流piId |
| postedDate | DateTime? | 是 | - | - |
| referenceCode | string | 是 | - | 参考代码 |
| sourceId | int? | 是 | - | 来源ID；sourceType="Invoice" :F_AR_Invoice
sourceType:="APInvoice":F_AP_Invoice
sourceType="DebitMemo"：F_AP_DebitMemo
sourceType="Disburse"：F_AP_Disburse
sourceType="Receivable"：F_AR_Receivable
sourceType="DisburseWriteOff"：
sourceType="CreditMemo"：F_AR_CreditMemo
F_AP_Disburse
   
sourcetype= "FGIMonthlyClosingIQCOut"=F_POST
sourcetype= "FGIMonthlyClosingStockCheck"=F_POST
sourcetype= "FGIMonthlyClosingScrapped"=F_POST
sourcetype= "FGIMonthlyClosingStock"=F_POST
sourcetype= "FGIMonthlyClosingShipment"=F_POST
sourcetype= "MonthlyClosingIssue"=F_POST
sourcetype= "CarryoverLossMFGCost"=F_POST |
| sourceType | string | 是 | - | 来源类型；APInvoice: 采购发票
APProvisionalEstimate: 应付暂估
APProvisionalEstimate2: 应付暂估回冲
CreditMemo: 客户扣款
DebitMemo: 供应商扣款
Depreciation: 折旧计提
DiaryAccount: 凭证登记
Disburse: 采购付款
FGICurrentInvoice: 成品本期开票
FGICurrentShip: 成品本期出货
FGIMonthlyClosingShipment: 成品出货
FGIMonthlyClosingStockCheck: 成品盘点
Invoice: 销售发票
MonthlyClosingIssue: 月结发料
MonthlyClosingStockCheck: 原材料盘点
Receivable: 销售收款
ReceivableWriteOff: 预收款冲销
Voucher: 凭证管理
CurrExchAdj: 汇兑损益 |
| startTaskName | string | 是 | - | - |
| status | string | 是 | - | 单据状态；Valid：生效。Active：活动. Pending制作中 |
| transType | string | 是 | - | Pay 付  Change 转 Receive 收 |
| type | string | 是 | - | 类型 |
| version | int? | 是 | - | 记录版本 |
| voucherNumber | string | 是 | - | 凭证号码 |
| approvedId | int? | 是 | - | 审批人，对应T_User.recId |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 创建人，对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 会计期间，对应T_FiscalPeriod.recId |
| flowTypeId | int? | 是 | - | 审批流程类型，对应T_FlowType.recId |
| postRoleId | int? | 是 | - | 岗位，对应T_PostRole.recId |
| postedId | int? | 是 | - | 岗位创建人，对应T_User.recId |
| postedRoleId | int? | 是 | - | 创建人所在岗位，对应T_PostRole.recId |
| circular | bool? | 是 | ((0)) | 循环 |
| interval | int? | 是 | ((0)) | 间隔 |
| entDate | string | 是 | - | 创建日期 |
| templateType | string | 是 | - | 模板类型 |
| interface_out | string | 是 | - | 打印时间 |
- **关联关系**：
  - F_Voucher.approvedId = T_User.recId
  - F_Voucher.companyId = T_Company.recId
  - F_Voucher.creatorId = T_User.recId
  - F_Voucher.fiscalPeriodId = T_FiscalPeriod.recId
  - F_Voucher.flowTypeId = T_FlowType.recId
  - F_Voucher.postRoleId = T_PostRole.recId
  - F_Voucher.postedId = T_User.recId
  - F_Voucher.postedRoleId = T_PostRole.recId

---

#### 432 凭证描述 ( F_VoucherDesc )
- **业务含义**：凭证描述
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| description | string | 是 | - | 描述 |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| ttype | string | 是 | - | 类型：INV_STD_PO 采购发票  INV_STD_SO 销售发票
RECEIVABLE 销售收入 DISBURSEMENT 采购支出
CreditMemo 客户扣款 DebitMemo 供应商扣款
CurrExchAdj 汇率调整 Depreciation-Assign 折旧计提
DiaryAccount 凭证登记 Depreciation-Clear 资产清理 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 433 凭证审批历史记录 ( F_VoucherHistory )
- **业务含义**：凭证审批历史记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 434 凭证明细 ( F_VoucherItem )
- **业务含义**：凭证明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveStatus | string | 是 | - | - |
| creditAmount | decimal? | 是 | - | 贷方金额 |
| debitAmount | decimal? | 是 | - | 借方金额 |
| description | string | 是 | - | 凭证摘要 |
| exchangeRate | decimal? | 是 | - | 汇率 |
| ideas | string | 是 | - | 汇率 |
| orgCurrAmount | decimal? | 是 | - | 原币金额 |
| org_CreditAmount | decimal? | 是 | - | - |
| org_DebitAmount | decimal? | 是 | - | - |
| projectId | int? | 是 | - | 项目 (还没有完全测试，他会依据不同类型对应不同的表)
projectType ：
9:T_SubcontractType
17：T_Category
1：M_Suppliers
2：S_Customer，4.T_Department， |
| projectType | int? | 是 | - | 1:供应商，9：外发项目，2：客户   ；17：物料分类，4：折旧费，13F_ProjectCatagoryItem、 18：S_ProductGroup |
| version | int? | 是 | - | - |
| accountId | int? | 是 | - | 科目表，对应F_Accounts.recId |
| currencyId | int? | 是 | - | 币种，对应T_Currency.recId |
| voucherId | int? | 是 | - | 凭证主表，对应F_Voucher.recId |
| cashProjectId | int? | 是 | - | 项目核算表，对应F_ProjectCatagoryItem.recId |
| ifPost | bool? | 是 | ((0)) | 是否过账（1已过帐，0未过账） |
- **关联关系**：
  - F_VoucherItem.accountId = F_Accounts.recId
  - F_VoucherItem.currencyId = T_Currency.recId
  - F_VoucherItem.voucherId = F_Voucher.recId
  - F_VoucherItem.cashProjectId = F_ProjectCatagoryItem.recId

---

#### 435 F_VoucherProject ( F_VoucherProject )
- **业务含义**：ERP 系统 F_VoucherProject 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| projectId | string | 是 | - | P_OCNItem |
| projectType | string | 是 | - | - |
| voucherId | string | 是 | - | 凭证主表，对应F_Voucher.recId |
| voucherItemId | string | 是 | - | 凭证详情表，对应F_VoucherItem.recId |
| localAmount | string | 是 | - | - |
| orgAmount | string | 是 | - | - |
- **关联关系**：
  - F_VoucherProject.voucherId = F_Voucher.recId
  - F_VoucherProject.voucherItemId = F_VoucherItem.recId

---

#### 436 凭证审批记录 ( F_VoucherWF )
- **业务含义**：凭证审批记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

### 2.9 成本模块

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 437 产品项目 ( C_CostSetting )
- **业务含义**：产品项目
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| costItemCode | string | 是 | - | 费用代码 |
| costItemDesc | string | 是 | - | 费用名称 |
| seq | int? | 是 | - | 排序 |
| version | int? | 是 | - | 修改次数 |
| accountId | int? | 是 | - | 权益表，对应F_Accounts.recId |
| company | int? | 是 | - | 公司，对应T_Company.recId |
| costTypeId | int? | 是 | - | 项目类型表，对应C_CostType.recId |
| parametersId | int? | 是 | - | 成本参数，对应S_Parameters.recId |
- **关联关系**：
  - C_CostSetting.accountId = F_Accounts.recId
  - C_CostSetting.company = T_Company.recId
  - C_CostSetting.costTypeId = C_CostType.recId
  - C_CostSetting.parametersId = S_Parameters.recId

---

#### 438 成本设置对应工艺和工序 ( C_CostSettingItem )
- **业务含义**：成本设置对应工艺和工序
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| rate | decimal? | 是 | - | 比率 |
| ratedOutput | decimal? | 是 | - | 标准成本 |
| seq | int? | 是 | - | 排序 |
| stdCost | decimal? | 是 | - | 额定产量 |
| version | int? | 是 | - | - |
| costSettingId | int? | 是 | - | 成本项目主表，对应C_CostSetting.recId |
| parametersId | int? | 是 | - | 成本参数，对应S_Parameters.recId |
| stepsProcessId | int? | 是 | - | 工序对应工艺表，对应T_StepsProcess.recId |
- **关联关系**：
  - C_CostSettingItem.costSettingId = C_CostSetting.recId
  - C_CostSettingItem.parametersId = S_Parameters.recId
  - C_CostSettingItem.stepsProcessId = T_StepsProcess.recId

---

#### 439 费用分组（费用管理） ( C_CostSharing )
- **业务含义**：费用分组（费用管理）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| createDate | DateTime? | 是 | - | 创建时间 |
| note | string | 是 | - | 备注 |
| status | string | 是 | - | 状态Compelete 完成 Active 活动 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| creatorId | int? | 是 | - | 对应T_User.recId |
| fiscalPeriodId | int? | 是 | - | 对应T_FiscalPeriod.recId |
| type | string | 是 | - | 类型  Intial  初始化 Standard  标准 |
- **关联关系**：
  - C_CostSharing.companyId = T_Company.recId
  - C_CostSharing.creatorId = T_User.recId
  - C_CostSharing.fiscalPeriodId = T_FiscalPeriod.recId

---

#### 440 费用分组明细（费用管理明细） ( C_CostSharingItem )
- **业务含义**：费用分组明细（费用管理明细）
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| status | string | 是 | - | - |
| updateTime | DateTime? | 是 | - | - |
| version | int? | 是 | - | - |
| costSettingId | int? | 是 | - | 对应C_CostSetting.recId |
| costSharingId | int? | 是 | - | 对应C_CostSharing.recId |
| userId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - C_CostSharingItem.costSettingId = C_CostSetting.recId
  - C_CostSharingItem.costSharingId = C_CostSharing.recId
  - C_CostSharingItem.userId = T_User.recId

---

#### 441 费用管理--项目明细 ( C_CostSharingItemCount )
- **业务含义**：费用管理--项目明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| output | decimal? | 是 | - | - |
| rate | decimal? | 是 | - | - |
| ratedOutput | decimal? | 是 | - | - |
| stdCost | decimal? | 是 | - | - |
| unitCost | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| costSharingItemId | int? | 是 | - | - |
| parametersId | int? | 是 | - | - |
| publicCostItemId | int? | 是 | - | - |
| stepsId | int? | 是 | - | - |
| ifLayer | bool? | 是 | - | - |
- **关联关系**：无

---

#### 442 C_CostSharingOutputDetail ( C_CostSharingOutputDetail )
- **业务含义**：ERP 系统 C_CostSharingOutputDetail 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| costSettingId | string | 是 | - | - |
| costSharingItemId | string | 是 | - | - |
| stepsId | string | 是 | - | - |
| jobId | string | 是 | - | - |
| mfgpartId | string | 是 | - | - |
| qtyOutput | string | 是 | - | - |
| qtyRejected | string | 是 | - | - |
| paramVal | string | 是 | - | - |
| allAreas | string | 是 | - | - |
| version | string | 是 | - | - |
- **关联关系**：无

---

#### 443 项目类型 ( C_CostType )
- **业务含义**：项目类型
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| autoCal | string | 是 | - | - |
| code | string | 是 | - | 代码 |
| name | string | 是 | - | 名称 |
| systemId | string | 是 | - | 对应T_SystemConfig.recId |
- **关联关系**：
  - C_CostType.systemId = T_SystemConfig.recId

---

#### 444 直接成本 ( C_DirectBomCost )
- **业务含义**：直接成本
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 445 C_FinancialReport ( C_FinancialReport )
- **业务含义**：ERP 系统 C_FinancialReport 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 446 C_FinancialReportItem ( C_FinancialReportItem )
- **业务含义**：ERP 系统 C_FinancialReportItem 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 447 C_JobCostPeriods ( C_JobCostPeriods )
- **业务含义**：ERP 系统 C_JobCostPeriods 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| avgUnitCost | string | 是 | - | 当期的累计平均价格 |
- **关联关系**：无

---

#### 448 工单明细成本 ( C_JobWoDetailsCalStatus )
- **业务含义**：工单明细成本
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 449 C_StepIndirecMatCost ( C_StepIndirecMatCost )
- **业务含义**：ERP 系统 C_StepIndirecMatCost 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| companyId | int? | 是 | - | - |
| fiscalPeriodId | int? | 是 | - | - |
| flg | int? | 是 | - | - |
| indirectMatCost | decimal? | 是 | - | - |
| processId | int? | 是 | - | - |
| stepId | int? | 是 | - | - |
| temp | bool? | 是 | - | - |
| uuid | string | 是 | - | - |
- **关联关系**：无

---

### 2.11 设备管理

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 450 设备管理表 ( EQ_Equipments )
- **业务含义**：设备管理表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| alertDay | DateTime? | 是 | - | 保养预警时间 |
| eqCode | string | 是 | - | 设备编号 |
| eqDesc | string | 是 | - | 设备说明 |
| eqName | string | 是 | - | 设备名称 |
| eqType | string | 是 | - | 类型; Production=生产 、NonProductive=非生产 |
| ifActive | bool? | 是 | - | 是否激活 1.是 0.否 |
| installDate | DateTime? | 是 | - | 安装日期 |
| keyNotes | string | 是 | - | 重要说明 |
| maintenanceEndDate | DateTime? | 是 | - | 保养终止日期 |
| seqNumber | string | 是 | - | 序号 |
| typeNumber | string | 是 | - | 型号 |
| uuid | string | 是 | - | - |
| vendor | string | 是 | - | 制造商 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| fixedAssetsId | int? | 是 | - | 固定资产，对应F_FixedAssets.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| pmGroupId | int? | 是 | - | 维修分组，对应PM_Group.recId |
| processId | int? | 是 | - | 工艺，对应T_Process.recId |
| stepsId | int? | 是 | - | 工序，对应T_Steps.recId |
| suppliersId | int? | 是 | - | 供应商，对应M_Suppliers.recId |
| postRoleId | string | 是 | - | 岗位，对应T_PostRole.recId |
| departmentId | int? | 是 | - | 部门，对应T_Department.recId |
- **关联关系**：
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

#### 451 设备保养管理 ( EQ_MLO )
- **业务含义**：设备保养管理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| PlanEndingTime | DateTime? | 是 | - | - |
| PlanStartTime | DateTime? | 是 | - | - |
| approveStatus | string | 是 | - | - |
| approveVersion | int? | 是 | - | - |
| confirmTime | DateTime? | 是 | - | - |
| createTime | DateTime? | 是 | - | - |
| cycleTime | int? | 是 | - | - |
| enableApproval | bool? | 是 | - | - |
| endingTime | DateTime? | 是 | - | - |
| ifStoped | bool? | 是 | - | - |
| ifSubcontract | bool? | 是 | - | - |
| lastEditedDateTime | DateTime? | 是 | - | - |
| mloNumber | string | 是 | - | - |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| priority | int? | 是 | - | - |
| qtyofMinsInStop | int? | 是 | - | - |
| requestDesc | string | 是 | - | - |
| solutionDesc | string | 是 | - | - |
| startTime | DateTime? | 是 | - | - |
| status | string | 是 | - | - |
| stopEndTime | DateTime? | 是 | - | - |
| stopStartTime | DateTime? | 是 | - | - |
| suggestedEndingTime | DateTime? | 是 | - | - |
| suggestedNotes | string | 是 | - | - |
| suggestedStartTime | DateTime? | 是 | - | - |
| uuid | string | 是 | - | - |
| version | int? | 是 | - | - |
| workDate | int? | 是 | - | - |
| workTime | DateTime? | 是 | - | - |
| closedById | int? | 是 | - | 对应T_User.recId |
| confirmedById | int? | 是 | - | 对应T_User.recId |
| creatorId | int? | 是 | - | 建单人，对应T_User.recId |
| departmentId | int? | 是 | - | 部门表，对应T_Department.recId |
| flowTypeId | int? | 是 | - | 对应T_FlowType.recId |
| lastEditedById | int? | 是 | - | 对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| pmTypeId | int? | 是 | - | 对应PM_Types.recId |
| preventiveId | int? | 是 | - | 对应EQ_Preventives.recId |
| processId | int? | 是 | - | 工艺表，对应T_Process.recId |
- **关联关系**：
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

#### 452 EQ_MLOEmployees ( EQ_MLOEmployees )
- **业务含义**：ERP 系统 EQ_MLOEmployees 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| version | int? | 是 | - | - |
| employeeId | int? | 是 | - | - |
| mloId | int? | 是 | - | - |
- **关联关系**：无

---

#### 453 EQ_MLOEQ ( EQ_MLOEQ )
- **业务含义**：ERP 系统 EQ_MLOEQ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| version | int? | 是 | - | - |
| equipmentId | int? | 是 | - | - |
| mloId | int? | 是 | - | - |
- **关联关系**：无

---

#### 454 EQ_MLOHistory ( EQ_MLOHistory )
- **业务含义**：ERP 系统 EQ_MLOHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| approveVersion | int? | 是 | - | - |
| beginTime | DateTime? | 是 | - | - |
| business | string | 是 | - | - |
| businessCode | string | 是 | - | - |
| businessForm | string | 是 | - | - |
| cway | bool? | 是 | - | - |
| editForm | bool? | 是 | - | - |
| endTime | DateTime? | 是 | - | - |
| executionId | string | 是 | - | - |
| flowDesc | string | 是 | - | - |
| historyQuery | bool? | 是 | - | - |
| myAction | bool? | 是 | - | - |
| myName | string | 是 | - | - |
| orgs | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| postRoleIds | string | 是 | - | - |
| suggest | string | 是 | - | - |
| taskDesc | string | 是 | - | - |
| taskDetails | string | 是 | - | - |
| taskFrom | string | 是 | - | - |
| taskId | string | 是 | - | - |
| taskName | string | 是 | - | - |
| taskRegainId | string | 是 | - | - |
| version | int? | 是 | - | - |
| mloId | int? | 是 | - | 对应EQ_MLO.recId |
| myId | int? | 是 | - | 对应T_User.recId |
- **关联关系**：
  - EQ_MLOHistory.mloId = EQ_MLO.recId
  - EQ_MLOHistory.myId = T_User.recId

---

#### 455 设备保养明细 ( EQ_MLOMaterials )
- **业务含义**：设备保养明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| changedTime | DateTime? | 是 | - | - |
| cycleTime | int? | 是 | - | - |
| qtyIssued | decimal? | 是 | - | - |
| qtyReq | decimal? | 是 | - | - |
| qtyRetruned | decimal? | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| mloId | int? | 是 | - | 设备保养主表，对应EQ_MLO.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - EQ_MLOMaterials.materialsId = M_Materials.recId
  - EQ_MLOMaterials.mloId = EQ_MLO.recId
  - EQ_MLOMaterials.unitId = T_Unit.recId

---

#### 456 EQ_MLOTasks ( EQ_MLOTasks )
- **业务含义**：ERP 系统 EQ_MLOTasks 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 457 设备保养审批 ( EQ_MLOWF )
- **业务含义**：设备保养审批
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 458 P_MORouteParams ( EQ_PMO )
- **业务含义**：P_MORouteParams
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| approveStatus | int? | 是 | - | 审批状态：'Pending'制作中，'Approved' 生效 |
| approveVersion | string | 是 | - | - |
| breakDownDesc | DateTime? | 是 | - | 故障说明 |
| confirmTime | DateTime? | 是 | - | 故障时间 |
| createTime | bool? | 是 | - | 建单时间 |
| enableApproval | DateTime? | 是 | - | - |
| endingTime | bool? | 是 | - | 维修结束时间 |
| ifStoped | string | 是 | - | - |
| issueDesc | DateTime? | 是 | - | - |
| lastEditedDateTime | string | 是 | - | - |
| orderStatus | string | 是 | - | 单据状态：'Close'关闭，'Maintenance'维修中，'ToConfirm'待确认 |
| originalStatus | string | 是 | - | - |
| pdId | string | 是 | - | - |
| piId | string | 是 | - | - |
| pmoNumber | int? | 是 | - | 维修单号 |
| qtyofMinsInStop | DateTime? | 是 | - | - |
| reportDateTime | string | 是 | - | - |
| requestDesc | string | 是 | - | - |
| solutionDesc | DateTime? | 是 | - | - |
| startTime | string | 是 | - | 维修开始时间 |
| status | DateTime? | 是 | - | - |
| stopEndTime | DateTime? | 是 | - | - |
| stopStartTime | string | 是 | - | - |
| urgencyLevel | string | 是 | - | - |
| uuid | int? | 是 | - | - |
| version | int? | 是 | - | - |
| closedById | int? | 是 | - | - |
| confirmedById | int? | 是 | - | - |
| creatorId | int? | 是 | - | - |
| departmentId | int? | 是 | - | 部门表，对应T_Department.recId |
| enterById | int? | 是 | - | - |
| equipmentId | int? | 是 | - | 设备管理表，对应EQ_Equipments.recId |
| flowTypeId | int? | 是 | - | - |
| lastEditedById | int? | 是 | - | - |
| plantsId | string | 是 | - | - |
| repairCost | string | 是 | - | 维修金额 |
| repairman | string | 是 | - | 维修人 |
- **关联关系**：
  - EQ_PMO.departmentId = T_Department.recId
  - EQ_PMO.equipmentId = EQ_Equipments.recId

---

#### 459 设备维修管理关联雇员表 ( EQ_PMOEmployees )
- **业务含义**：设备维修管理关联雇员表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| version | int? | 是 | - | - |
| employeeId | int? | 是 | - | 雇员rkey |
| pmoId | int? | 是 | - | 设备维修管理，对应EQ_PMO.recId |
- **关联关系**：
  - EQ_PMOEmployees.pmoId = EQ_PMO.recId

---

#### 460 设备维修管理--审核记录 ( EQ_PMOHistory )
- **业务含义**：设备维修管理--审核记录
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 461 设备维修管理--物料 ( EQ_PMOMaterials )
- **业务含义**：设备维修管理--物料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int? | 是 | - | - |
| changedTime | DateTime? | 是 | - | - |
| cycleTime | int? | 是 | - | - |
| qtyIssued | decimal? | 是 | - | - |
| qtyReq | decimal? | 是 | - | - |
| qtyRetruned | decimal? | 是 | - | - |
| type | string | 是 | - | - |
| version | int? | 是 | - | - |
| materialsId | int? | 是 | - | 物料表，对应M_Materials.recId |
| pmoId | int? | 是 | - | 设备维修管理，对应EQ_PMO.recId |
| unitId | int? | 是 | - | 单位，对应T_Unit.recId |
- **关联关系**：
  - EQ_PMOMaterials.materialsId = M_Materials.recId
  - EQ_PMOMaterials.pmoId = EQ_PMO.recId
  - EQ_PMOMaterials.unitId = T_Unit.recId

---

#### 462 设备维修管理--任务 ( EQ_PMOTasks )
- **业务含义**：设备维修管理--任务
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 463 EQ_PMOWF ( EQ_PMOWF )
- **业务含义**：ERP 系统 EQ_PMOWF 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 464 设备保养定义关联设备表 ( EQ_PreventiveEQ )
- **业务含义**：设备保养定义关联设备表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| version | string | 是 | - | - |
| equipmentId | string | 是 | - | 设备管理表，对应EQ_Equipments.recId |
| preventiveId | string | 是 | - | 设备保养管理表，对应EQ_Preventives.recId |
- **关联关系**：
  - EQ_PreventiveEQ.equipmentId = EQ_Equipments.recId
  - EQ_PreventiveEQ.preventiveId = EQ_Preventives.recId

---

#### 465 保养类型和物料关联表 ( EQ_PreventiveMaterials )
- **业务含义**：保养类型和物料关联表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| qty | string | 是 | - | 数量 |
| type | string | 是 | - | 类型 |
| version | string | 是 | - | - |
| materialsId | string | 是 | - | 物料表，对应M_Materials.recId |
| preventiveId | string | 是 | - | 设备保养管理表，对应EQ_Preventives.recId |
| unitId | string | 是 | - | - |
- **关联关系**：
  - EQ_PreventiveMaterials.materialsId = M_Materials.recId
  - EQ_PreventiveMaterials.preventiveId = EQ_Preventives.recId

---

#### 466 设备保养定义 ( EQ_Preventives )
- **业务含义**：设备保养定义
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | string | 是 | - | - |
| cycleTime | string | 是 | - | 周期 |
| ifSubcontract | string | 是 | - | 外包 |
| lastPrevDateTime | string | 是 | - | 上次保养时间 |
| nextPrevDateTime | string | 是 | - | 下次保养时间 |
| note | string | 是 | - | 备注 |
| prevCode | string | 是 | - | 代码 |
| prevDesc | string | 是 | - | 描述 |
| priority | string | 是 | - | 优先级 |
| uuid | string | 是 | - | - |
| version | string | 是 | - | - |
| workDate | string | 是 | - | 工作时间 |
| workTime | string | 是 | - | - |
| creatorId | string | 是 | - | - |
| plantsId | string | 是 | - | - |
| pmGroupId | string | 是 | - | 维修分组ID，对应PM_Group.recId |
| pmTypeId | string | 是 | - | 保养类型；1-月度  2-半年度，对应PM_Types.recId |
| processId | string | 是 | - | - |
| ifEmail | string | 是 | - | 邮件 |
| ifTimingData | string | 是 | - | 定时任务 |
| cron | string | 是 | - | 定时表达式 |
| type | string | 是 | - | 类型：0: 设备保养; 1 - 仪器检验；2 - 点检定义 |
| timingadvance | string | 是 | - | 定时提前时间 |
| timingAdvanceUnit | string | 是 | - | 定时提前单位 |
| departmentId | string | 是 | - | 部门ID，对应T_Department.recId |
- **关联关系**：
  - EQ_Preventives.pmGroupId = PM_Group.recId
  - EQ_Preventives.pmTypeId = PM_Types.recId
  - EQ_Preventives.departmentId = T_Department.recId

---

#### 467 设备保养定义管理任务表 ( EQ_PreventiveTasks )
- **业务含义**：设备保养定义管理任务表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qtyofHours | string | 是 | - | 工时 |
| version | string | 是 | - | 修改次数 |
| preventiveId | string | 是 | - | 保养/点检定义ID，对应EQ_Preventives.recId |
| taskId | string | 是 | - | 保养/点检任务ID，对应PM_tasks.recId |
- **关联关系**：
  - EQ_PreventiveTasks.preventiveId = EQ_Preventives.recId
  - EQ_PreventiveTasks.taskId = PM_tasks.recId

---

#### 468 设备管理--物料 ( EQ_Spareparts )
- **业务含义**：设备管理--物料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| materialsId | string | 是 | - | 物料表，对应M_Materials.recId |
| equipmentId | string | 是 | - | 设备管理，对应EQ_Equipments.recId |
- **关联关系**：
  - EQ_Spareparts.materialsId = M_Materials.recId
  - EQ_Spareparts.equipmentId = EQ_Equipments.recId

---

#### 469 故障现象 ( PM_Faults )
- **业务含义**：故障现象
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| FaultDesc | string | 是 | - | 描述 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活  0否  1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 470 维修分组 ( PM_Group )
- **业务含义**：维修分组
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| groupCode | string | 是 | - | 代码 |
| groupDesc | string | 是 | - | 描述 |
| groupName | string | 是 | - | 维修分组 |
| ifActive | bool? | 是 | - | 是否激活   0 否  1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| version | int? | 是 | - | - |
| companyId | int? | 是 | - | 公司，对应T_Company.recId |
| userId | int? | 是 | - | 制单人，对应T_User.recId |
- **关联关系**：
  - PM_Group.companyId = T_Company.recId
  - PM_Group.userId = T_User.recId

---

#### 471 维修分组--用户 ( PM_GroupEmployees )
- **业务含义**：维修分组--用户
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| groupID | int? | 是 | - | 对应PM_Group.recId |
| lastModifyDate | DateTime? | 是 | - | - |
| modifiedBy | string | 是 | - | - |
| version | int? | 是 | - | - |
| employeeID | int? | 是 | - | 对应S_BusinessMan.recId |
- **关联关系**：
  - PM_GroupEmployees.groupID = PM_Group.recId
  - PM_GroupEmployees.employeeID = S_BusinessMan.recId

---

#### 472 维修发料 ( PM_IssueForm )
- **业务含义**：维修发料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | 制单日期 |
| issueNumber | string | 是 | - | 发料单号 |
| note | string | 是 | - | 备注 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| pickedById | int? | 是 | - | 领料人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
- **关联关系**：
  - PM_IssueForm.creatorId = T_User.recId
  - PM_IssueForm.pickedById = T_User.recId
  - PM_IssueForm.plantsId = T_Plants.recId

---

#### 473 维修发料-维修单和保养单 ( PM_IssueFormItem )
- **业务含义**：维修发料-维修单和保养单
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qtyofIssued | decimal? | 是 | - | - |
| type | int? | 是 | - | - |
| version | int? | 是 | - | - |
| issueFormId | int? | 是 | - | 维修发料，对应PM_IssueForm.recId |
| mloMaterialId | int? | 是 | - | 保养管理，对应EQ_MLOMaterials.recId |
| pmoMaterialId | int? | 是 | - | 维修管理，对应EQ_PMOMaterials.recId |
- **关联关系**：
  - PM_IssueFormItem.issueFormId = PM_IssueForm.recId
  - PM_IssueFormItem.mloMaterialId = EQ_MLOMaterials.recId
  - PM_IssueFormItem.pmoMaterialId = EQ_PMOMaterials.recId

---

#### 474 维修退料批次 ( PM_IssueReturnBatch )
- **业务含义**：维修退料批次
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| averageUnitCost | decimal? | 是 | - | 单价 |
| inventoryId | int? | 是 | - | 物料库存 |
| issueReturnBatchId | int? | 是 | - | 维修发料-维修单和保养单，对应PM_IssueFormItem.recId |
| issuereturnItemId | int? | 是 | - | 维修退料明细表，对应PM_IssueFormItem.recId |
| ma_Cost | decimal? | 是 | - | 不含税单价 |
| note | string | 是 | - | - |
| poItemId | int? | 是 | - | - |
| quantity | decimal? | 是 | - | 数量 |
| type | int? | 是 | - | - |
| version | int? | 是 | - | - |
| inventoryBatchId | int? | 是 | - | 物料库存批次，对应M_InventoryBatch.recId |
| actionDate | DateTime? | 是 | - | - |
| locked | bool? | 是 | - | - |
- **关联关系**：
  - PM_IssueReturnBatch.issueReturnBatchId = PM_IssueFormItem.recId
  - PM_IssueReturnBatch.issuereturnItemId = PM_IssueFormItem.recId
  - PM_IssueReturnBatch.inventoryBatchId = M_InventoryBatch.recId

---

#### 475 故障原因 ( PM_Reasons )
- **业务含义**：故障原因
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| reasonDesc | string | 是 | - | 描述 |
| sort | string | 是 | - | 排序 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

#### 476 维修退料 ( PM_ReturnForm )
- **业务含义**：维修退料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| createDate | DateTime? | 是 | - | 制单日期 |
| note | string | 是 | - | 备注 |
| returnNumber | string | 是 | - | 退料单号 |
| version | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| returnById | int? | 是 | - | 退料人，对应T_User.recId |
- **关联关系**：
  - PM_ReturnForm.creatorId = T_User.recId
  - PM_ReturnForm.plantsId = T_Plants.recId
  - PM_ReturnForm.returnById = T_User.recId

---

#### 477 维修退料明细 ( PM_ReturnFormItem )
- **业务含义**：维修退料明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| qtyofReturned | decimal? | 是 | - | 数量 |
| type | int? | 是 | - | - |
| version | int? | 是 | - | - |
| issueFormItemId | int? | 是 | - | 维修领料明细，对应PM_IssueFormItem.recId |
| returnFormId | int? | 是 | - | 维修退料主表，对应PM_ReturnForm.recId |
- **关联关系**：
  - PM_ReturnFormItem.issueFormItemId = PM_IssueFormItem.recId
  - PM_ReturnFormItem.returnFormId = PM_ReturnForm.recId

---

#### 478 标准任务 ( PM_Tasks )
- **业务含义**：标准任务
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| isDemand | bool? | 是 | - | 是否维修 0 否 1 是 |
| isPreventive | bool? | 是 | - | 保养任务 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| qtyOfHours | decimal? | 是 | - | 标准工时 |
| sort | string | 是 | - | 排序 |
| taskCode | string | 是 | - | 代码 |
| taskDesc | string | 是 | - | 描述 |
| taskName | string | 是 | - | 名称 |
| version | int? | 是 | - | - |
| userId | int? | 是 | - | 制单人，对应T_User.recId |
- **关联关系**：
  - PM_Tasks.userId = T_User.recId

---

#### 479 业务员 ( PM_Types )
- **业务含义**：业务员
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| code | string | 是 | - | 代码 |
| ifActive | bool? | 是 | - | 是否激活 0 否 1 是 |
| lastModifyDate | DateTime? | 是 | - | 修改时间 |
| modifiedBy | string | 是 | - | 修改人 |
| name | string | 是 | - | 名称 |
| sort | string | 是 | - | - |
| tdays | int? | 是 | - | 保养周期 |
| version | int? | 是 | - | - |
- **关联关系**：无

---

### 2.12 APS排程

> 本章节数据来源于 Excel 工作表：`APS数据库`

#### 480 设备 ( EQUIPMENT )
- **业务含义**：设备
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| RKEY | string | 是 | - | - |
| EQ_CODE | string | 是 | - | 设备代码 |
| EQ_NAME | string | 是 | - | 设备名称 |
| LOCATION | string | 是 | - | - |
| CALENDARID | string | 是 | - | - |
| EFFICIENCY | string | 是 | - | - |
| PROPERTY | string | 是 | - | 加工类型 |
| TTYPE | string | 是 | - | 类型 |
| TRANSQTY | string | 是 | - | - |
| ISTRANSQTYBYPCS | string | 是 | - | - |
| MaxBatchSize | string | 是 | - | 最大批量加工数 |
| MinBatchSize | string | 是 | - | 最小批量加工数 |
| CapacityUnit_ID | string | 是 | - | - |
| Capacity_Value | string | 是 | - | - |
| Site_ID | string | 是 | - | - |
| SEQINSTEP | string | 是 | - | - |
| MINSTEPSCHEDULINGSEQ | string | 是 | - | - |
| vertical_EqGroup | string | 是 | - | - |
- **关联关系**：无

---

#### 481 EQUIPMENT_GROUP ( EQUIPMENT_GROUP )
- **业务含义**：ERP 系统 EQUIPMENT_GROUP 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| RKEY | string | 是 | - | - |
| EQG_CODE | string | 是 | - | 设备群组代码 |
| EQG_NAME | string | 是 | - | 设备群组名称 |
| SITE_ID | string | 是 | - | - |
| PrepareTime_Determine | string | 是 | - | - |
- **关联关系**：无

---

#### 482 工序表 ( STEP )
- **业务含义**：工序表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| RKEY | long? | 是 | - | - |
| STEP_CODE | string | 是 | - | 工艺代码 |
| STEP_NAME | string | 是 | - | 工艺名称 |
| WORKSTATIONID | string | 是 | - | - |
| EQG_ID | string | 是 | - | - |
| PREPARE_TIME | decimal? | 是 | - | - |
| SETUP_TIME | decimal? | 是 | - | - |
| PROCESS_TIME | decimal? | 是 | - | - |
| POST_OP_TIME | decimal? | 是 | - | - |
| TRANSFER_TIME | decimal? | 是 | - | - |
| POSTSETUP_TIME | decimal? | 是 | - | - |
| YIELDRATE | decimal? | 是 | - | - |
| MATERIALD | string | 是 | - | - |
| IF_SCHEDULED | bool? | 是 | - | - |
| BARCODE_ENTRY | bool? | 是 | - | - |
| TTYPE | int? | 是 | - | - |
| TransQty | int? | 是 | - | - |
| TransferType | int? | 是 | - | 工序转移类型 |
| SCHEDULINGSEQ | int? | 是 | - | - |
| PROPERITY | decimal? | 是 | - | - |
| SITEID | string | 是 | - | - |
| DefaultedStep | bool? | 是 | - | - |
| sortSEQ | int? | 是 | - | - |
| EnterTime | DateTime? | 是 | - | - |
| ISRELEASESTEP | bool? | 是 | - | - |
| erp_stepId | string | 是 | - | 工序id |
| erp_stepName | string | 是 | - | 工序名称 |
| groupSEQ | decimal? | 是 | - | - |
| AllowSplitStep | bool? | 是 | - | - |
- **关联关系**：无

---

### 2.13 工作流引擎

> 本章节数据来源于 Excel 工作表：`字段注释、表名`

#### 483 JBPM4_DEPLOYMENT ( JBPM4_DEPLOYMENT )
- **业务含义**：ERP 系统 JBPM4_DEPLOYMENT 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 484 JBPM4_DEPLOYPROP ( JBPM4_DEPLOYPROP )
- **业务含义**：ERP 系统 JBPM4_DEPLOYPROP 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 485 JBPM4_EXECUTION ( JBPM4_EXECUTION )
- **业务含义**：ERP 系统 JBPM4_EXECUTION 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 486 JBPM4_HIST_ACTINST ( JBPM4_HIST_ACTINST )
- **业务含义**：ERP 系统 JBPM4_HIST_ACTINST 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 487 JBPM4_HIST_DETAIL ( JBPM4_HIST_DETAIL )
- **业务含义**：ERP 系统 JBPM4_HIST_DETAIL 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 488 JBPM4_HIST_PROCINST ( JBPM4_HIST_PROCINST )
- **业务含义**：ERP 系统 JBPM4_HIST_PROCINST 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 489 JBPM4_HIST_TASK ( JBPM4_HIST_TASK )
- **业务含义**：ERP 系统 JBPM4_HIST_TASK 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 490 JBPM4_HIST_VAR ( JBPM4_HIST_VAR )
- **业务含义**：ERP 系统 JBPM4_HIST_VAR 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 491 JBPM4_ID_GROUP ( JBPM4_ID_GROUP )
- **业务含义**：ERP 系统 JBPM4_ID_GROUP 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 492 JBPM4_ID_MEMBERSHIP ( JBPM4_ID_MEMBERSHIP )
- **业务含义**：ERP 系统 JBPM4_ID_MEMBERSHIP 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 493 JBPM4_ID_USER ( JBPM4_ID_USER )
- **业务含义**：ERP 系统 JBPM4_ID_USER 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 494 JBPM4_JOB ( JBPM4_JOB )
- **业务含义**：ERP 系统 JBPM4_JOB 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 495 JBPM4_LOB ( JBPM4_LOB )
- **业务含义**：ERP 系统 JBPM4_LOB 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 496 JBPM4_PARTICIPATION ( JBPM4_PARTICIPATION )
- **业务含义**：ERP 系统 JBPM4_PARTICIPATION 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 497 JBPM4_PROPERTY ( JBPM4_PROPERTY )
- **业务含义**：ERP 系统 JBPM4_PROPERTY 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 498 JBPM4_SWIMLANE ( JBPM4_SWIMLANE )
- **业务含义**：ERP 系统 JBPM4_SWIMLANE 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 499 JBPM4_TASK ( JBPM4_TASK )
- **业务含义**：ERP 系统 JBPM4_TASK 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 500 JBPM4_VARIABLE ( JBPM4_VARIABLE )
- **业务含义**：ERP 系统 JBPM4_VARIABLE 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

### 2.14 自定义表

> 本章节数据来源于 Excel 工作表：`自定义表、表名`

#### 501 A_AAA ( A_AAA )
- **业务含义**：ERP 系统 A_AAA 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 502 a_allMaterialsFromZB20170221 ( a_allMaterialsFromZB20170221 )
- **业务含义**：ERP 系统 a_allMaterialsFromZB20170221 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 503 a_backup_deletedMatrlList_20170325 ( a_backup_deletedMatrlList_20170325 )
- **业务含义**：ERP 系统 a_backup_deletedMatrlList_20170325 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 504 a_CustomerfromZB20170221 ( a_CustomerfromZB20170221 )
- **业务含义**：ERP 系统 a_CustomerfromZB20170221 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 505 a_CustomerfromZB20170221-1 ( a_CustomerfromZB20170221-1 )
- **业务含义**：ERP 系统 a_CustomerfromZB20170221-1 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 506 a_DeletedMtrlList_20170325 ( a_DeletedMtrlList_20170325 )
- **业务含义**：ERP 系统 a_DeletedMtrlList_20170325 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 507 a_FGI_Inevneotyr_20170506 ( a_FGI_Inevneotyr_20170506 )
- **业务含义**：ERP 系统 a_FGI_Inevneotyr_20170506 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 508 a_fgibal_20170401 ( a_fgibal_20170401 )
- **业务含义**：ERP 系统 a_fgibal_20170401 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 509 a_FGIStock0401 ( a_FGIStock0401 )
- **业务含义**：ERP 系统 a_FGIStock0401 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 510 a_import_fgi-0301 ( a_import_fgi-0301 )
- **业务含义**：ERP 系统 a_import_fgi-0301 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 511 a_import_Materials-0301 ( a_import_Materials-0301 )
- **业务含义**：ERP 系统 a_import_Materials-0301 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 512 a_log1_02262017922PM ( a_log1_02262017922PM )
- **业务含义**：ERP 系统 a_log1_02262017922PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 513 a_log1_02262017923PM ( a_log1_02262017923PM )
- **业务含义**：ERP 系统 a_log1_02262017923PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 514 a_log1_022720171031PM ( a_log1_022720171031PM )
- **业务含义**：ERP 系统 a_log1_022720171031PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 515 a_log1_02282017943PM ( a_log1_02282017943PM )
- **业务含义**：ERP 系统 a_log1_02282017943PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 516 a_log1_03162017933PM ( a_log1_03162017933PM )
- **业务含义**：ERP 系统 a_log1_03162017933PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 517 a_log1_03312017615PM ( a_log1_03312017615PM )
- **业务含义**：ERP 系统 a_log1_03312017615PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 518 a_log1_03312017617PM ( a_log1_03312017617PM )
- **业务含义**：ERP 系统 a_log1_03312017617PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 519 a_log1_03312017657PM ( a_log1_03312017657PM )
- **业务含义**：ERP 系统 a_log1_03312017657PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 520 a_log2_02262017922PM ( a_log2_02262017922PM )
- **业务含义**：ERP 系统 a_log2_02262017922PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 521 a_log2_02262017923PM ( a_log2_02262017923PM )
- **业务含义**：ERP 系统 a_log2_02262017923PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 522 a_log2_02282017943PM ( a_log2_02282017943PM )
- **业务含义**：ERP 系统 a_log2_02282017943PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 523 a_log2_03312017615PM ( a_log2_03312017615PM )
- **业务含义**：ERP 系统 a_log2_03312017615PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 524 a_log2_03312017617PM ( a_log2_03312017617PM )
- **业务含义**：ERP 系统 a_log2_03312017617PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 525 a_log2_03312017657PM ( a_log2_03312017657PM )
- **业务含义**：ERP 系统 a_log2_03312017657PM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 526 a_log2_041012017657AM ( a_log2_041012017657AM )
- **业务含义**：ERP 系统 a_log2_041012017657AM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 527 a_log2_041112017657AM ( a_log2_041112017657AM )
- **业务含义**：ERP 系统 a_log2_041112017657AM 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 528 a_log2_20170403 ( a_log2_20170403 )
- **业务含义**：ERP 系统 a_log2_20170403 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 529 a_mtrlBal_20170401 ( a_mtrlBal_20170401 )
- **业务含义**：ERP 系统 a_mtrlBal_20170401 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 530 a_mtrlbal_20170401_1 ( a_mtrlbal_20170401_1 )
- **业务含义**：ERP 系统 a_mtrlbal_20170401_1 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 531 a_oldErp_So$ ( a_oldErp_So$ )
- **业务含义**：ERP 系统 a_oldErp_So$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 532 a_olderp_so2$ ( a_olderp_so2$ )
- **业务含义**：ERP 系统 a_olderp_so2$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 533 a_P_MOROUTE_20170506 ( a_P_MOROUTE_20170506 )
- **业务含义**：ERP 系统 a_P_MOROUTE_20170506 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 534 a_SM_FromZB20170220 ( a_SM_FromZB20170220 )
- **业务含义**：ERP 系统 a_SM_FromZB20170220 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 535 a_UpdatePanelSize_20170302 ( a_UpdatePanelSize_20170302 )
- **业务含义**：ERP 系统 a_UpdatePanelSize_20170302 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 536 a_UpdatePanelSize_20170302_1 ( a_UpdatePanelSize_20170302_1 )
- **业务含义**：ERP 系统 a_UpdatePanelSize_20170302_1 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 537 a_旧成品库存$ ( a_旧成品库存$ )
- **业务含义**：ERP 系统 a_旧成品库存$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 538 a_物料批次货位$ ( a_物料批次货位$ )
- **业务含义**：ERP 系统 a_物料批次货位$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 539 a_物料批次货位2$ ( a_物料批次货位2$ )
- **业务含义**：ERP 系统 a_物料批次货位2$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 540 a_物料批次货位3$ ( a_物料批次货位3$ )
- **业务含义**：ERP 系统 a_物料批次货位3$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 541 alan_materails_20170211 ( alan_materails_20170211 )
- **业务含义**：ERP 系统 alan_materails_20170211 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 542 alan_parameter_mapping ( alan_parameter_mapping )
- **业务含义**：ERP 系统 alan_parameter_mapping 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 543 工厂管理-应收应付 ( F_AccountSetting1 )
- **业务含义**：工厂管理-应收应付
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 544 F_AccountSetting2 ( F_AccountSetting2 )
- **业务含义**：ERP 系统 F_AccountSetting2 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 545 F_AccountSetting3 ( F_AccountSetting3 )
- **业务含义**：ERP 系统 F_AccountSetting3 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 546 F_AccountSetting4 ( F_AccountSetting4 )
- **业务含义**：ERP 系统 F_AccountSetting4 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 547 fgi_inventory_0427_2200 ( fgi_inventory_0427_2200 )
- **业务含义**：ERP 系统 fgi_inventory_0427_2200 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 548 FGI_Inventory_backup_0420 ( FGI_Inventory_backup_0420 )
- **业务含义**：ERP 系统 FGI_Inventory_backup_0420 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 549 FGI_Inventory_BAK20170407 ( FGI_Inventory_BAK20170407 )
- **业务含义**：ERP 系统 FGI_Inventory_BAK20170407 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 550 fgi_inventory_bak_0429 ( fgi_inventory_bak_0429 )
- **业务含义**：ERP 系统 fgi_inventory_bak_0429 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 551 FGI_StockFormItem_bak0407 ( FGI_StockFormItem_bak0407 )
- **业务含义**：ERP 系统 FGI_StockFormItem_bak0407 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 552 FGI_StockFormItem_moid_bak ( FGI_StockFormItem_moid_bak )
- **业务含义**：ERP 系统 FGI_StockFormItem_moid_bak 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 553 M_MaterialsWarehouse_bak ( M_MaterialsWarehouse_bak )
- **业务含义**：ERP 系统 M_MaterialsWarehouse_bak 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 554 M_MaterialsWarehouse_bak0413 ( M_MaterialsWarehouse_bak0413 )
- **业务含义**：ERP 系统 M_MaterialsWarehouse_bak0413 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 555 p_bombatching_0413 ( p_bombatching_0413 )
- **业务含义**：ERP 系统 p_bombatching_0413 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 556 xnh_ChangedToConsigment_411 ( xnh_ChangedToConsigment_411 )
- **业务含义**：ERP 系统 xnh_ChangedToConsigment_411 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 557 xnh_ChangedToConsigment_412 ( xnh_ChangedToConsigment_412 )
- **业务含义**：ERP 系统 xnh_ChangedToConsigment_412 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 558 xnh_reworkChangeLog-返工工序记录 ( xnh_reworkChangeLog-返工工序记录 )
- **业务含义**：ERP 系统 xnh_reworkChangeLog-返工工序记录 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 559 xnh_奇立04010405_1724_item ( xnh_奇立04010405_1724_item )
- **业务含义**：ERP 系统 xnh_奇立04010405_1724_item 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 560 xnh_底油线路 ( xnh_底油线路 )
- **业务含义**：ERP 系统 xnh_底油线路 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 561 xnh_贵阳海信_item ( xnh_贵阳海信_item )
- **业务含义**：ERP 系统 xnh_贵阳海信_item 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 562 xnh_达信20170405001_item ( xnh_达信20170405001_item )
- **业务含义**：ERP 系统 xnh_达信20170405001_item 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 563 xnh_高效170331_item ( xnh_高效170331_item )
- **业务含义**：ERP 系统 xnh_高效170331_item 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 564 操作员$ ( 操作员$ )
- **业务含义**：ERP 系统 操作员$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 565 转序员$ ( 转序员$ )
- **业务含义**：ERP 系统 转序员$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

### 2.15 其它

> 本章节数据来源于 Excel 工作表：`字段注释、成本、表名`

#### 566 物料 ( -MO已分配数量-SO已分配数量 )
- **业务含义**：物料
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| plantsId | int? | 是 | - | 工厂，对应T_Plants.recId |
| qtyOfSO | decimal? | 是 | - | SO需求数量 |
| lastStockDate | DateTime? | 是 | - | - |
| mosoUpdateDate | DateTime? | 是 | - | - |
- **关联关系**：
  - -MO已分配数量-SO已分配数量.plantsId = T_Plants.recId

---

#### 567 财务管理-财务数据-科目管理上级 ( A_account )
- **业务含义**：财务管理-财务数据-科目管理上级
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| type | string | 是 | - | - |
| levels | string | 是 | - | 1 2 级别 |
| accountCode | string | 是 | - | - |
| accountDesc | string | 是 | - | - |
| 助记码 | string | 是 | - | - |
| currency | string | 是 | - | - |
| 计量单位 | string | 是 | - | - |
| 辅助账类型 | string | 是 | - | - |
| 账页格式 | string | 是 | - | - |
| DC | string | 是 | - | - |
| 受控系统 | string | 是 | - | - |
| 是否封存 | string | 是 | - | - |
| 银行账 | string | 是 | - | - |
| 日记账 | string | 是 | - | - |
| 自定义类型 | string | 是 | - | - |
- **关联关系**：无

---

#### 568 a_addlPHPart ( a_addlPHPart )
- **业务含义**：ERP 系统 a_addlPHPart 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 569 a_AllInfo ( a_AllInfo )
- **业务含义**：ERP 系统 a_AllInfo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 570 a_atom ( a_atom )
- **业务含义**：ERP 系统 a_atom 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 571 a_CoreToBeFixed ( a_CoreToBeFixed )
- **业务含义**：ERP 系统 a_CoreToBeFixed 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 572 a_DeletedJob ( a_DeletedJob )
- **业务含义**：ERP 系统 a_DeletedJob 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 573 a_deletespds ( a_deletespds )
- **业务含义**：ERP 系统 a_deletespds 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 574 a_drill ( a_drill )
- **业务含义**：ERP 系统 a_drill 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 575 a_drill_adjustbase ( a_drill_adjustbase )
- **业务含义**：ERP 系统 a_drill_adjustbase 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 576 a_fgi_batch ( a_fgi_batch )
- **业务含义**：ERP 系统 a_fgi_batch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 577 a_FGI_Inventory ( a_FGI_Inventory )
- **业务含义**：ERP 系统 a_FGI_Inventory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 578 a_importSO_AE ( a_importSO_AE )
- **业务含义**：ERP 系统 a_importSO_AE 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 579 a_ImportSO_Flex ( a_ImportSO_Flex )
- **业务含义**：ERP 系统 a_ImportSO_Flex 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 580 a_importSO_PPC ( a_importSO_PPC )
- **业务含义**：ERP 系统 a_importSO_PPC 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 581 a_JobRouteParam ( a_JobRouteParam )
- **业务含义**：ERP 系统 a_JobRouteParam 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 582 a_JobRoutes ( a_JobRoutes )
- **业务含义**：ERP 系统 a_JobRoutes 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 583 a_laminate ( a_laminate )
- **业务含义**：ERP 系统 a_laminate 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 584 a_Materials ( a_Materials )
- **业务含义**：ERP 系统 a_Materials 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 585 a_MaterialsFromWH ( a_MaterialsFromWH )
- **业务含义**：ERP 系统 a_MaterialsFromWH 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 586 a_materialwithoutwh ( a_materialwithoutwh )
- **业务含义**：ERP 系统 a_materialwithoutwh 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 587 A_MET2 ( A_MET2 )
- **业务含义**：ERP 系统 A_MET2 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 588 a_OdrBatch ( a_OdrBatch )
- **业务含义**：ERP 系统 a_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 589 a_old_erp_so ( a_old_erp_so )
- **业务含义**：ERP 系统 a_old_erp_so 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 590 a_osScrapHistory ( a_osScrapHistory )
- **业务含义**：ERP 系统 a_osScrapHistory 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 591 A_PARTTODOLIST ( A_PARTTODOLIST )
- **业务含义**：ERP 系统 A_PARTTODOLIST 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 592 a_poList ( a_poList )
- **业务含义**：ERP 系统 a_poList 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 593 a_PP_FromZB20170220 ( a_PP_FromZB20170220 )
- **业务含义**：ERP 系统 a_PP_FromZB20170220 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 594 a_ReWo_Status ( a_ReWo_Status )
- **业务含义**：ERP 系统 a_ReWo_Status 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 595 a_reworkhistory-返工单 ( a_reworkhistory-返工单 )
- **业务含义**：ERP 系统 a_reworkhistory-返工单 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 596 a_Route ( a_Route )
- **业务含义**：ERP 系统 a_Route 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 597 a_ScrapHistory-外发报废 ( a_ScrapHistory-外发报废 )
- **业务含义**：ERP 系统 a_ScrapHistory-外发报废 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 598 a_stepInfo ( a_stepInfo )
- **业务含义**：ERP 系统 a_stepInfo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 599 A_Title ( A_Title )
- **业务含义**：ERP 系统 A_Title 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 600 a_wo_Rework ( a_wo_Rework )
- **业务含义**：ERP 系统 a_wo_Rework 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 601 a_yd ( a_yd )
- **业务含义**：ERP 系统 a_yd 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 602 ab_OdrBatch ( ab_OdrBatch )
- **业务含义**：ERP 系统 ab_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 603 供应商 ( AND scts.fromId=scti.plantsId )
- **业务含义**：供应商
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| toId | int? | 是 | - | 往哪个工厂，对应T_Plants.recId |
| qty | int? | 是 | ((0)) | - |
| markupValue | decimal? | 是 | ((0)) | - |
| isPercentage | bool? | 是 | ((0)) | - |
| qtyStocked | int? | 是 | ((0)) | 入库数量 |
| qtyReturnRepair | int? | 是 | ((0)) | - |
| soPrice | string | 是 | - | 销售订单价格 |
- **关联关系**：
  - AND scts.fromId=scti.plantsId.toId = T_Plants.recId

---

#### 604 发放人 ( and 主工单.Id=子工单.parentId )
- **业务含义**：发放人
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qty_PCS_PRODUCED_Temp | int? | 是 | - | - |
| qty_Array_PRODUCED_Temp | int? | 是 | - | - |
| qty_PNL_PRODUCED_Temp | int? | 是 | - | - |
| orderType | string | 是 | - | 工单类型（退货返修，仓库返修，生产等） |
| YD_org_woNumber | string | 是 | - | - |
| org_woNumber | string | 是 | - | - |
| xnh_pcs_temp | int? | 是 | ((0)) | - |
| xnh_set_temp | int? | 是 | ((0)) | - |
| xnh_pnl_temp | int? | 是 | ((0)) | - |
| stockRouteId | int? | 是 | - | - |
| upgradeTime | DateTime? | 是 | - | - |
| receiptStepId | int? | 是 | - | - |
| receiptMoRouteId | int? | 是 | - | - |
| ifReceipt | bool? | 是 | - | - |
| sc_PCS | int? | 是 | - | 外协数量 |
| sc_Array | int? | 是 | - | - |
| sc_PNLS | int? | 是 | - | - |
| mergeWoId | int? | 是 | - | 母作业单ID |
| mergeOrderSOId | int? | 是 | - | 母订单ID |
| allowMove | bool? | 是 | - | allowMove=0不允许作MRB检查 |
| splitMoRouteid | string | 是 | - | 拆分在上一级工单的做在工序--P_SplitWOLog.processID |
| taxesFlag | string | 是 | - | 保税类型 - Bonded: 保税; Taxes: 课税 |
| taxesCode | string | 是 | - | 保税代码 |
| synchro | string | 是 | - | 同步状态，0-未同步；1-已同步；2-不同步 |
| splitBatchId | string | 是 | - | 拆批申请ID，对应P_WOSplitBatchApplication.recId |
- **关联关系**：
  - and 主工单.Id=子工单.parentId.splitBatchId = P_WOSplitBatchApplication.recId

---

#### 605 物料批次库存 ( b_matrl )
- **业务含义**：物料批次库存
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| code | string | 是 | - | 物料代码 |
| name | string | 是 | - | 物料名称 |
| whcode | string | 是 | - | 仓库代码 |
| whname | string | 是 | - | 仓库名称 |
| lcode | string | 是 | - | 仓位代码 |
| lname | string | 是 | - | 仓位名称 |
| flat | string | 是 | - | 货位 |
| qty | double? | 是 | - | 数量 |
| batchno | double? | 是 | - | 内部批号 |
| unit | string | 是 | - | 单位 |
| mfgDate | DateTime? | 是 | - | 制造时间 |
| ExprieDate | DateTime? | 是 | - | 入库时间 |
| note | string | 是 | - | 备注 |
| taxRate | double? | 是 | - | 税率（%） |
| price | double? | 是 | - | 单价 |
| amt | double? | 是 | - | 总计 |
| supplierBatch | string | 是 | - | 供应商批号 |
| UNITWeigth | double? | 是 | - | 单重 |
| whptr | int? | 是 | - | 仓库ID，对应T_Warehouse.recId |
| locptr | int? | 是 | - | 仓位ID，对应T_Location.recId |
| matrlPtr | int? | 是 | - | 物料ID，对应M_Materials.recId |
| recId | decimal? | 是 | - | - |
| ref | string | 是 | - | - |
| REF1 | int? | 是 | - | - |
- **关联关系**：
  - b_matrl.whptr = T_Warehouse.recId
  - b_matrl.locptr = T_Location.recId
  - b_matrl.matrlPtr = M_Materials.recId

---

#### 606 b_Update_JobCustomer ( b_Update_JobCustomer )
- **业务含义**：ERP 系统 b_Update_JobCustomer 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 607 b_Update_SalesPartCustomer ( b_Update_SalesPartCustomer )
- **业务含义**：ERP 系统 b_Update_SalesPartCustomer 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 608 B_USER_WIP01 ( B_USER_WIP01 )
- **业务含义**：ERP 系统 B_USER_WIP01 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 609 ba ( ba )
- **业务含义**：ERP 系统 ba 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 610 e2 ( e2 )
- **业务含义**：ERP 系统 e2 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| recId | int | 否 | - | 主键 |
| amount | decimal? | 是 | - | - |
| output | decimal? | 是 | - | 工序产出 |
| rate | decimal? | 是 | - | - |
| ratedOutput | decimal? | 是 | - | - |
| stdCost | decimal? | 是 | - | - |
| unitCost | decimal? | 是 | - | - |
| version | int? | 是 | - | - |
| costSharingItemId | int? | 是 | - | 费用分组明细 |
| parametersId | int? | 是 | - | - |
| publicCostItemId | int? | 是 | - | - |
| stepsId | string | 是 | - | 工序表id |
| ifLayer | string | 是 | - | - |
- **关联关系**：无

---

#### 611 fgi_cartonsnumber ( fgi_cartonsnumber )
- **业务含义**：ERP 系统 fgi_cartonsnumber 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 612 寄售 ( fgi_sotransfer )
- **业务含义**：寄售
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 613 客户备份信息 ( IMP_CustInfo )
- **业务含义**：客户备份信息
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| CustNo | string | 是 | - | 客户代码 |
| CustID | string | 是 | - | 客户ID代码 |
| CustName | string | 是 | - | 客户名称 |
| ECustName | string | 是 | - | - |
| Country | string | 是 | - | - |
| Continent | string | 是 | - | - |
| CustKind | string | 是 | - | - |
| CustType | string | 是 | - | - |
| Address | string | 是 | - | - |
| FAddress | string | 是 | - | - |
| EAddress | string | 是 | - | - |
| RegAddress | string | 是 | - | - |
| RegNo | string | 是 | - | - |
| EstablishDate | DateTime? | 是 | - | - |
| MajorGoods | string | 是 | - | - |
| MajorMarket | string | 是 | - | - |
| PayDay | int? | 是 | - | - |
| PayMode | string | 是 | - | - |
| Currency | string | 是 | - | - |
| CreditAmount | double? | 是 | - | - |
| CustGrade | string | 是 | - | - |
| CustAb | string | 是 | - | - |
| HomePage | string | 是 | - | - |
| Phone | string | 是 | - | - |
| Phone2 | string | 是 | - | - |
| Phone3 | string | 是 | - | - |
| Fax | string | 是 | - | - |
| Fax2 | string | 是 | - | - |
| Fax3 | string | 是 | - | - |
| Mobile | string | 是 | - | - |
| Mobile2 | string | 是 | - | - |
| Mobile3 | string | 是 | - | - |
| Email | string | 是 | - | - |
| Email2 | string | 是 | - | - |
| Email3 | string | 是 | - | - |
| ContactMan | string | 是 | - | - |
| ContactMan2 | string | 是 | - | - |
| ContactMan3 | string | 是 | - | - |
| Position1 | string | 是 | - | - |
| Position2 | string | 是 | - | - |
| Position3 | string | 是 | - | - |
| InDept | string | 是 | - | - |
| InDept2 | string | 是 | - | - |
| InDept3 | string | 是 | - | - |
| ShipAddrA | string | 是 | - | - |
| ShipAddrB | string | 是 | - | - |
| ShipAddrC | string | 是 | - | - |
| InvoiceAddr | string | 是 | - | - |
| SettleMode | string | 是 | - | - |
| PayTerm | string | 是 | - | - |
| ParType | string | 是 | - | - |
| MoreClass | bool? | 是 | - | - |
| DisCount | bool? | 是 | - | - |
| Delivchk | bool? | 是 | - | - |
| SellMan | string | 是 | - | - |
| SellType | string | 是 | - | - |
| DCBy | string | 是 | - | - |
| DCDate | DateTime? | 是 | - | - |
| Remark | string | 是 | - | - |
| CustNotice | string | 是 | - | - |
| IsAudit | bool? | 是 | - | - |
| IsApprove | bool? | 是 | - | - |
| InvoiceName | string | 是 | - | - |
| InvoiceTaxNo | string | 是 | - | - |
| InvoiceAddrPhone | string | 是 | - | - |
| InvoiceBankAcct | string | 是 | - | - |
| ExportLastTotal | double? | 是 | - | - |
| ExportLastAdvance | double? | 是 | - | - |
| ExportLastMode | string | 是 | - | - |
| ExportNextTotal | double? | 是 | - | - |
| ExportNextAdvance | double? | 是 | - | - |
| ExportNextMode | string | 是 | - | - |
| InternalLastTotal | double? | 是 | - | - |
| InternalLastAdvance | double? | 是 | - | - |
| InternalLastMode | string | 是 | - | - |
| InternalNextTotal | double? | 是 | - | - |
| InternalNextAdvance | double? | 是 | - | - |
| InternalNextMode | string | 是 | - | - |
| BuyerAmount | double? | 是 | - | - |
| BuyerQty | int? | 是 | - | - |
| DelMark | bool? | 是 | - | - |
| ApplyBy | string | 是 | - | - |
| ApplyDate | DateTime? | 是 | - | - |
| ApprovedBy | string | 是 | - | - |
| ApprovedDate | DateTime? | 是 | - | - |
| CreateBy | string | 是 | - | - |
| CreateDate | DateTime? | 是 | - | - |
| AuditedBy | string | 是 | - | - |
| AuditedDate | DateTime? | 是 | - | - |
| UpdateBy | string | 是 | - | - |
| UpdateDate | DateTime? | 是 | - | - |
| IsCredit | bool? | 是 | - | - |
| UnlockDate | DateTime? | 是 | - | - |
| UnlockMan | string | 是 | - | - |
| middleman | bool? | 是 | - | - |
- **关联关系**：无

---

#### 614 IMP_CustMapping ( IMP_CustMapping )
- **业务含义**：ERP 系统 IMP_CustMapping 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 615 IMP_OdrBatch ( IMP_OdrBatch )
- **业务含义**：ERP 系统 IMP_OdrBatch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 616 IMP_OdrProdNo ( IMP_OdrProdNo )
- **业务含义**：ERP 系统 IMP_OdrProdNo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 617 imp_OrderList ( imp_OrderList )
- **业务含义**：ERP 系统 imp_OrderList 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 618 IMP_PnInfo ( IMP_PnInfo )
- **业务含义**：ERP 系统 IMP_PnInfo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 619 IMP_User ( IMP_User )
- **业务含义**：ERP 系统 IMP_User 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 620 钻孔历史记录表 ( org_DrillDetails )
- **业务含义**：钻孔历史记录表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| JobId | int? | 是 | - | 型号表，对应S_Job.recId |
| TechNo | string | 是 | - | - |
| ToolSEQ | string | 是 | - | 刀序 |
| HoleFlag | string | 是 | - | 标记 |
| PTH | string | 是 | - | - |
| FSize | string | 是 | - | 要求尺寸 |
| TOL | string | 是 | - | 正负公差 |
| HOLES | string | 是 | - | - |
| PNLHOLES | string | 是 | - | 拼板孔数 |
| NOTE | string | 是 | - | 备注 |
| SEQ | int? | 是 | - | 序号 |
- **关联关系**：
  - org_DrillDetails.JobId = S_Job.recId

---

#### 621 qty_Order ( qty_Order )
- **业务含义**：ERP 系统 qty_Order 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| version | int? | 是 | - | - |
| woNumber | string | 是 | - | 工单号P_WO.woNumber 开头 RR  退货返修 RW：仓库返修 |
| xout_MinQty | int? | 是 | - | - |
| creatorId | int? | 是 | - | 制单人，对应T_User.recId |
| jobId | int? | 是 | - | 生产型号，对应S_Job.recId |
- **关联关系**：
  - qty_Order.creatorId = T_User.recId
  - qty_Order.jobId = S_Job.recId

---

#### 622 rpt_moRoute_snap ( rpt_moRoute_snap )
- **业务含义**：ERP 系统 rpt_moRoute_snap 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 623 rpt_ShopFloorInfo ( rpt_ShopFloorInfo )
- **业务含义**：ERP 系统 rpt_ShopFloorInfo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 624 rpt_ShopFloorSummary ( rpt_ShopFloorSummary )
- **业务含义**：ERP 系统 rpt_ShopFloorSummary 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 625 rpt_StepMapping ( rpt_StepMapping )
- **业务含义**：ERP 系统 rpt_StepMapping 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 626 rpt_targetInfo ( rpt_targetInfo )
- **业务含义**：ERP 系统 rpt_targetInfo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 627 来自工厂默认等于1，筛掉海外数据 ( scts.contractItemId=scti.recId )
- **业务含义**：来自工厂默认等于1，筛掉海外数据
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 628 面积表 ( VPartArea )
- **业务含义**：面积表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 629 W_DailyStepWipOutPut ( W_DailyStepWipOutPut )
- **业务含义**：ERP 系统 W_DailyStepWipOutPut 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 630 W_WIP ( W_WIP )
- **业务含义**：ERP 系统 W_WIP 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 631 W_WIPFieldDisplay ( W_WIPFieldDisplay )
- **业务含义**：ERP 系统 W_WIPFieldDisplay 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 632 W_WIPQueryExecute ( W_WIPQueryExecute )
- **业务含义**：ERP 系统 W_WIPQueryExecute 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 633 W_WIPStepDetails ( W_WIPStepDetails )
- **业务含义**：ERP 系统 W_WIPStepDetails 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 634 月结主表 ( WIP_Backlog )
- **业务含义**：月结主表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 635 WIP_PC ( WIP_PC )
- **业务含义**：ERP 系统 WIP_PC 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 636 WIP_PCSteps ( WIP_PCSteps )
- **业务含义**：ERP 系统 WIP_PCSteps 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 637 WIP_PCWO ( WIP_PCWO )
- **业务含义**：ERP 系统 WIP_PCWO 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 638 wo_Rework$ ( wo_Rework$ )
- **业务含义**：ERP 系统 wo_Rework$ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 639 xnh_BOMBatch ( xnh_BOMBatch )
- **业务含义**：ERP 系统 xnh_BOMBatch 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 640 xnh_BOMBatch2 ( xnh_BOMBatch2 )
- **业务含义**：ERP 系统 xnh_BOMBatch2 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 641 xnh_ChangedtobePlaned ( xnh_ChangedtobePlaned )
- **业务含义**：ERP 系统 xnh_ChangedtobePlaned 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 642 xnh_DeletedLock ( xnh_DeletedLock )
- **业务含义**：ERP 系统 xnh_DeletedLock 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 643 成品入库 ( xnh_fgi_stockForm )
- **业务含义**：成品入库
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 644 成品入库明细 ( xnh_fgi_stockFormItem )
- **业务含义**：成品入库明细
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 645 xnh_fgi_stockformitemwo ( xnh_fgi_stockformitemwo )
- **业务含义**：ERP 系统 xnh_fgi_stockformitemwo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 646 xnh_last3setp ( xnh_last3setp )
- **业务含义**：ERP 系统 xnh_last3setp 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 647 xnh_OrderDateChanged ( xnh_OrderDateChanged )
- **业务含义**：ERP 系统 xnh_OrderDateChanged 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 648 xnh_orphanPart ( xnh_orphanPart )
- **业务含义**：ERP 系统 xnh_orphanPart 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 649 xnh_OSMORoute ( xnh_OSMORoute )
- **业务含义**：ERP 系统 xnh_OSMORoute 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 650 xnh_qtyshipped ( xnh_qtyshipped )
- **业务含义**：ERP 系统 xnh_qtyshipped 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 651 xnh_resetPlanningedQty ( xnh_resetPlanningedQty )
- **业务含义**：ERP 系统 xnh_resetPlanningedQty 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 652 xnh_stockedIn ( xnh_stockedIn )
- **业务含义**：ERP 系统 xnh_stockedIn 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 653 xnh_wipBalance ( xnh_wipBalance )
- **业务含义**：ERP 系统 xnh_wipBalance 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 654 xnh_wo ( xnh_wo )
- **业务含义**：ERP 系统 xnh_wo 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 655 xnh_wotemp ( xnh_wotemp )
- **业务含义**：ERP 系统 xnh_wotemp 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 656 xnh_woTempQty ( xnh_woTempQty )
- **业务含义**：ERP 系统 xnh_woTempQty 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 657 zb_materials ( zb_materials )
- **业务含义**：ERP 系统 zb_materials 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 658 set数量 ( · )
- **业务含义**：set数量
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| mfgDate | string | 是 | - | 生产日期 |
| expiryDate | string | 是 | - | 过期日期 |
| note2 | string | 是 | - | 备注2 |
| note3 | string | 是 | - | 备注3 |
| note4 | string | 是 | - | 备注4 |
| customerNote1 | string | 是 | - | 客户备注1 |
| customerNote2 | string | 是 | - | 客户备注2 |
| customerNote3 | string | 是 | - | 客户备注3 |
| customerNote4 | string | 是 | - | 客户备注4 |
| customerNote5 | string | 是 | - | 客户备注5 |
| customerNote6 | string | 是 | - | 客户备注6 |
| contractSOId | string | 是 | - | 销售订单id(注意是关联contractItemId) |
| outsideNumber | string | 是 | - | 外箱单号 |
- **关联关系**：无

---

#### 659 不需要接收 ( 不需要接收 )
- **业务含义**：ERP 系统 不需要接收 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qty_planned | int? | 是 | ((0)) | 已经计划数量 |
| qty_tobe_planned | int? | 是 | ((0)) | 待计划数量 |
| qtyLackMated | int? | 是 | ((0)) | - |
| ifNew | bool? | 是 | - | 是否新单 0 否 1 是 |
| EnterDate | DateTime? | 是 | (getdate()) | 建单日期 |
| qtyOrderReturned | int? | 是 | - | 退货数量（客诉）“客诉类型（除“投诉”所有的类型）”（qty_Repaired+qty_Returned） |
| qtyOrderArrayReturned | int? | 是 | - | - |
| qty_undo | int? | 是 | - | 撤销出货数量 |
| forecastOrderId | int? | 是 | - | 对应的预测订单id |
| qtyForecasted | int? | 是 | ((0)) | 预测数量（累计）--备货订单的已核销数量 |
| ifForecast | bool? | 是 | ((0)) | 是否预测（0：正常，1：预测） |
| non_Planned | string | 是 | - | 不投产订单 1是 0否 |
| dirShipment | string | 是 | - | 直接出货 |
| soPriceWithTax | string | 是 | - | 基于销售单位的原币含税单价-如下单单位为set,则是SET单价 |
| soPriceWithoutTax | string | 是 | - | 基于销售单位的原币不含税单价 |
| LinkSoCode | string | 是 | - | 关联订单号 |
| moduletypeid | string | 是 | - | 销售自定义分类 |
- **关联关系**：无

---

#### 660 工厂 ( 主工单.moId=子工单.moId )
- **业务含义**：工厂
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 661 采购受理 ( 供应商 )
- **业务含义**：采购受理
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 662 化验 ( 化验 )
- **业务含义**：ERP 系统 化验 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 663 MO已分配数量 ( 可入库数量-MO需求数量 )
- **业务含义**：MO已分配数量
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qtySO_Alloc | decimal? | 是 | ((0)) | SO已分配数量 |
| qtySafeStock | decimal? | 是 | ((0)) | 安全库存 |
- **关联关系**：无

---

#### 664 可分配数量=库存数量+可入库数量 ( 可分配数量=库存数量+可入库数量 )
- **业务含义**：ERP 系统 可分配数量=库存数量+可入库数量 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 665 可用数量=库存数量+ ( 可用数量=库存数量+ )
- **业务含义**：ERP 系统 可用数量=库存数量+ 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 666 请购数量 ( 在途可分配数=请购数+采购数 )
- **业务含义**：请购数量
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qtyInPO | decimal? | 是 | ((0)) | 采购数量 |
| qtyTOStock | decimal? | 是 | ((0)) | 可入库数量 |
| qtyToPR | decimal? | 是 | ((0)) | 待请购数 |
| prnote | string | 是 | - | - |
| qtyMO_Alloc2 | decimal? | 是 | ((0)) | 在途MO已分配数量 |
| qtySO_Alloc2 | decimal? | 是 | ((0)) | 在途SO已分配数量 |
- **关联关系**：无

---

#### 667 制造部件 ( 工单对应的制造部件号 )
- **业务含义**：制造部件
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 668 制造单表 ( 工单有主卡和子卡 )
- **业务含义**：制造单表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 669 下一个工序 ( 空数据 )
- **业务含义**：下一个工序
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| nextOutputMORouteId | int? | 是 | - | 下一个制造单流转表，对应P_MORoute.recId |
| qtyWork | int? | 是 | ((0)) | - |
| qtySend | int? | 是 | ((0)) | - |
| qtyWorkBack | int? | 是 | ((0)) | - |
| qtyUnWorkBack | int? | 是 | ((0)) | - |
| iqcId | int? | 是 | - | 送检表，对应FGI_IQC.recId |
| wip_Unit | string | 是 | - | - |
| wip_Qty | int? | 是 | - | - |
| os_Unit | string | 是 | - | - |
| os_qty | int? | 是 | - | - |
| routeActive | int? | 是 | ((1)) | - |
| sc_pnl | int? | 是 | ((0)) | 外协PNL |
| sc_Arr | int? | 是 | ((0)) | 外协SET |
| sc_Pcs | int? | 是 | ((0)) | 外协PCS |
| sc_rejPnl | int? | 是 | ((0)) | - |
| sc_rejArr | int? | 是 | ((0)) | - |
| sc_rejPcs | int? | 是 | ((0)) | - |
| pc_pnl | int? | 是 | ((0)) | - |
| pc_Arr | int? | 是 | ((0)) | - |
| pc_Pcs | int? | 是 | ((0)) | - |
| carryoverWO | bool? | 是 | ((0)) | - |
| org_pcs_backlog | int? | 是 | - | - |
| allowOs | bool? | 是 | - | - |
| osIqcId | int? | 是 | - | - |
| mergeRouteId | int? | 是 | - | - |
| reworkRootRouteId | int? | 是 | - | - |
| backlogUnitId | int? | 是 | - | 结存单位，对应T_Unit.recId |
| pendingStatus | int? | 是 | - | 加工状态，对应1进站,2上机,3下机,4出站,5转出.recId |
| operateInformation | string | 是 | - | 上机信息，对应工具,物料,参数.recId |
| isLock | int? | 是 | ((0)) | 锁定，对应0正常1锁定2预警3超时锁定4超时预警.recId |
- **关联关系**：
  - 空数据.nextOutputMORouteId = P_MORoute.recId
  - 空数据.iqcId = FGI_IQC.recId
  - 空数据.backlogUnitId = T_Unit.recId
  - 空数据.pendingStatus = 1进站,2上机,3下机,4出站,5转出.recId
  - 空数据.operateInformation = 工具,物料,参数.recId
  - 空数据.isLock = 0正常1锁定2预警3超时锁定4超时预警.recId

---

#### 670 补货，投诉， ( 补货，投诉， )
- **业务含义**：ERP 系统 补货，投诉， 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 671 退货，换货，返修（新出单） ( 退货，换货，返修（新出单） )
- **业务含义**：ERP 系统 退货，换货，返修（新出单） 业务数据表
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| — | — | — | — | 数据字典中暂无字段明细 |
- **关联关系**：无

---

#### 672 审批通过时间 ( 需要接收（成品接收客户类型） )
- **业务含义**：审批通过时间
- **所属数据库**：思方云2 ERP
| 字段名 | 字段类型 | 是否为空 | 默认值 | 说明 |
|--------|----------|----------|--------|------|
| qty_Replenishment | int? | 是 | - | 补货数量（客诉） |
- **关联关系**：无

---

## 三、表关系说明

### 3.1 核心关联关系摘录

以下摘录各业务模块中部分主外键关联，完整关联见第二章各表「关联关系」小节。

### 3.1 基础模块

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
| 9 | T_Category.inspectGroupId = T_InspectGroup.recId |
| 10 | T_Category.inspectPostId = T_PostRole.recId |
| 11 | T_Category.parentId = T_Category.recId |
| 12 | T_Category.postRoleId = T_PostRole.recId |

### 3.2 物料模块

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
| 9 | M_BOMIssueItem.mfgPartId = E_JobMfgParts.recId |
| 10 | M_BOMPicklist.companyId = T_Company.recId |
| 11 | M_BOMPicklist.creatorId = T_User.recId |
| 12 | M_BOMPicklist.departmentId = T_Department.recId |

### 3.3 成品模块

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
| 9 | FGI_IQC.flowTypeId = T_FlowType.recId |
| 10 | FGI_IQC.jobId = S_Job.recId |
| 11 | FGI_IQC.plantsId = T_Plants.recId |
| 12 | FGI_IQC.postRoleId = T_PostRole.recId |

### 3.4 工程模块

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
| 9 | E_DrillTitle.jobId = S_Job.recId |
| 10 | E_DrillTitle.mfgpartId = E_JobMfgParts.recId |
| 11 | E_FPCToolTable.jobId = S_JOB.recId |
| 12 | E_JobImages.jobId = S_Job.recId |

### 3.5 销售模块

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
| 9 | S_Contract.companyId = T_Company.recId |
| 10 | S_Contract.contractTypeId = S_OrderType.recId |
| 11 | S_Contract.creatorId = T_User.recId |
| 12 | S_Contract.currencyId = T_Currency.recId |

### 3.6 生产模块

| 序号 | 关联关系 |
|------|----------|
| 1 | P_BOMBatching.bomPicklistItemId = M_BOMPicklistItem.recId |
| 2 | P_BOMBatching.mfgPartId = E_JobMfgParts.recId |
| 3 | P_BOMBatching.materialsId = M_Materials.recId |
| 4 | P_BOMBatching.moId = P_MO.recId |
| 5 | P_BOMBatching.processId = T_Process.recId |
| 6 | P_BOMBatching.stockUnitId = T_Unit.recId |
| 7 | P_BOMBatching.warehouseId = T_Warehouse.recId |
| 8 | P_BOMBatching.stepsId = T_Steps.recId |
| 9 | P_BOMBatching.contractItemId = S_ContractItem.recId |
| 10 | P_BOMBatching.materialsCostByPlantId = M_MaterialsCostByPlant.recId |
| 11 | P_ECN.companyId = T_Company.recId |
| 12 | P_ECN.contractSOId = S_ContractSO.recId |

### 3.7 财务模块

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
| 9 | F_AP_DebitMemo.postRoleId = T_PostRole.recId |
| 10 | F_AP_DebitMemo.suppliersId = M_Suppliers.recId |
| 11 | F_AP_DebitMemo.targetId = T_Plants.recId |
| 12 | F_AP_DebitMemoItem.jobId = S_Job.recId |

### 3.8 成本模块

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
| 9 | C_CostSharing.creatorId = T_User.recId |
| 10 | C_CostSharing.fiscalPeriodId = T_FiscalPeriod.recId |
| 11 | C_CostSharingItem.costSettingId = C_CostSetting.recId |
| 12 | C_CostSharingItem.costSharingId = C_CostSharing.recId |

### 3.2 推荐补充模板

| 主表 | 外键表 | 关系类型 | 说明 |
|------|--------|----------|------|
| 待补充 | 待补充 | 待补充 | 待补充 |

## 四、数据字典速查

### 4.1 表清单

| 序号 | 表名 | 表注释 | 所属数据库 | 字段数量 |
|------|------|----------|------------|----------|
| 1 | T_AppSeting | 系统设定 | 思方云2 ERP | 310 |
| 2 | T_Area | 区域 | 思方云2 ERP | 16 |
| 3 | T_AtomLog | 系统日志 | 思方云2 ERP | 8 |
| 4 | T_Business | 业务表 | 思方云2 ERP | 10 |
| 5 | T_BusinessItem | 流程设计--流程分类 | 思方云2 ERP | 11 |
| 6 | T_Cate | 等级管理表 | 思方云2 ERP | 15 |
| 7 | T_Category | 物料类别表（物料分组 | 思方云2 ERP | 82 |
| 8 | T_CategoryItem | 物料类别明细表（储区） | 思方云2 ERP | 6 |
| 9 | T_ChargeItem | 附加费用 | 思方云2 ERP | 12 |
| 10 | T_Company | 公司管理 | 思方云2 ERP | 121 |
| 11 | T_Currency | 币种 | 思方云2 ERP | 11 |
| 12 | T_CurrencyItem | 币种兑换明细 | 思方云2 ERP | 9 |
| 13 | T_CustomScript | 自定义脚本 | 思方云2 ERP | 12 |
| 14 | T_CustTable | 自定义表 | 思方云2 ERP | 0 |
| 15 | T_CustTableValue | 自定义表明细 | 思方云2 ERP | 0 |
| 16 | T_Defect | 缺陷表 | 思方云2 ERP | 14 |
| 17 | T_Department | 部门表 | 思方云2 ERP | 12 |
| 18 | T_DepartmentUser | 部门--用户表 | 思方云2 ERP | 6 |
| 19 | T_Document | 文件上传记录 | 思方云2 ERP | 20 |
| 20 | T_ExportSetting | 导出设置 | 思方云2 ERP | 9 |
| 21 | T_ExportSettingItem | 导出设置明细 | 思方云2 ERP | 4 |
| 22 | T_ExportSettingUrl | 导出设置URL | 思方云2 ERP | 7 |
| 23 | T_FiscalPeriod | 会计期间 | 思方云2 ERP | 10 |
| 24 | T_Flow | 流程设计主表 | 思方云2 ERP | 12 |
| 25 | T_FlowType | 流程设计 | 思方云2 ERP | 15 |
| 26 | T_FOB | 贸易方式 | 思方云2 ERP | 9 |
| 27 | T_FunctionRight | 系统模块功能表 | 思方云2 ERP | 14 |
| 28 | T_Group | 用户组管理 | 思方云2 ERP | 9 |
| 29 | T_GroupUser | 用户组--用户 | 思方云2 ERP | 6 |
| 30 | T_Inspect | 检验分组--检验项目 | 思方云2 ERP | 4 |
| 31 | T_InspectGroup | 检验分组 | 思方云2 ERP | 12 |
| 32 | T_InspectItems | 检验项目 | 思方云2 ERP | 15 |
| 33 | T_InventoryCheckReason | 盘点原因 | 思方云2 ERP | 12 |
| 34 | T_JSONHistory | JSON接口日志 | 思方云2 ERP | 11 |
| 35 | T_Linkman | 联系人 | 思方云2 ERP | 13 |
| 36 | T_Location | 储区表 | 思方云2 ERP | 15 |
| 37 | T_Module | 模块表 | 思方云2 ERP | 12 |
| 38 | T_ModuleType | 模组类型 | 思方云2 ERP | 0 |
| 39 | T_MyModule | 用户模块权限表 | 思方云2 ERP | 4 |
| 40 | T_Notepad | 记事本 | 思方云2 ERP | 10 |
| 41 | T_NotepadGroup | 记事分组表 | 思方云2 ERP | 11 |
| 42 | T_NumberControl | 单据号码表 | 思方云2 ERP | 14 |
| 43 | T_PaymentMethod | 付款方式 | 思方云2 ERP | 9 |
| 44 | T_PaymentTerm | 付款周期 | 思方云2 ERP | 12 |
| 45 | T_Plants | 工厂 | 思方云2 ERP | 175 |
| 46 | T_PostRole | 岗位 | 思方云2 ERP | 11 |
| 47 | T_PostRoleModule | 岗位模块 | 思方云2 ERP | 6 |
| 48 | T_Process | 工艺表 | 思方云2 ERP | 24 |
| 49 | T_ProcessDefect | 工艺缺陷报废 | 思方云2 ERP | 5 |
| 50 | T_ProcessEmployee | 工艺--雇员权限(工程设计流程权限) | 思方云2 ERP | 7 |
| 51 | T_ProcessParameter | 工艺流程参数表 | 思方云2 ERP | 5 |
| 52 | T_ProcessPlant | 工艺管理--工厂 | 思方云2 ERP | 4 |
| 53 | T_ProductCategoryPlant | 销售数据--产品分类--工厂 | 思方云2 ERP | 4 |
| 54 | T_Racks | 货架表 | 思方云2 ERP | 5 |
| 55 | T_ReportSeting | 表单设定 | 思方云2 ERP | 21 |
| 56 | T_Shipping | 运输方式 | 思方云2 ERP | 10 |
| 57 | T_StepEmployee | 工序--雇员权限(过数权限) | 思方云2 ERP | 7 |
| 58 | T_StepIndiectMatLink | 工序--间接材料 | 思方云2 ERP | 11 |
| 59 | T_Steps | 工序表 | 思方云2 ERP | 44 |
| 60 | T_StepsProcess | 工序关联工艺 | 思方云2 ERP | 23 |
| 61 | T_StepsProcessInspectItem | 工艺定量、定性检验项表 | 思方云2 ERP | 11 |
| 62 | T_SubcontractType | 外协类型 | 思方云2 ERP | 11 |
| 63 | T_SubcontractTypeItem | 外协类型明细表 | 思方云2 ERP | 7 |
| 64 | T_SubcontractTypeParams | 外协类型-参数表 | 思方云2 ERP | 7 |
| 65 | T_SystemConfig | 系统配置表 | 思方云2 ERP | 9 |
| 66 | T_SystemLog | 系统日志 | 思方云2 ERP | 9 |
| 67 | T_Tax | 税率表 | 思方云2 ERP | 13 |
| 68 | T_Text | 记事本 | 思方云2 ERP | 0 |
| 69 | T_Unit | 单位 | 思方云2 ERP | 15 |
| 70 | T_UseProcess | T_UseProcess | 思方云2 ERP | 11 |
| 71 | T_User | 用户表 | 思方云2 ERP | 24 |
| 72 | T_UserFunctionRight | 用户功能表 | 思方云2 ERP | 7 |
| 73 | T_UserModule | 用户模块 | 思方云2 ERP | 7 |
| 74 | T_UserPlant | 用户所在工厂权限 | 思方云2 ERP | 6 |
| 75 | T_UserPostRole | 用户--岗位 | 思方云2 ERP | 6 |
| 76 | T_Warehouse | 仓库 | 思方云2 ERP | 25 |
| 77 | T_WarehouseKeepers | 仓库人员明细 | 思方云2 ERP | 0 |
| 78 | T_Workshop | T_Workshop | 思方云2 ERP | 9 |
| 79 | M_BOMIssue | BOM发料 | 思方云2 ERP | 9 |
| 80 | M_BOMIssueItem | BOM发料明细表 | 思方云2 ERP | 13 |
| 81 | M_BOMPicklist | BOM领料单 | 思方云2 ERP | 26 |
| 82 | M_BOMPicklistHistory | BOM领料单审批记录 | 思方云2 ERP | 28 |
| 83 | M_BOMPicklistItem | BOM领料单明细 | 思方云2 ERP | 23 |
| 84 | M_BOMPicklistItemBatch | BOM领料批次 | 思方云2 ERP | 13 |
| 85 | M_BOMPicklistWF | BOM领料外发 | 思方云2 ERP | 28 |
| 86 | M_Consignment | 寄送表 | 思方云2 ERP | 6 |
| 87 | M_Envelope | 物料数据--包线管理 | 思方云2 ERP | 23 |
| 88 | M_EnvelopeHistory | M_EnvelopeHistory | 思方云2 ERP | 0 |
| 89 | M_EnvelopeItem | 物料数据--包线管理明细 | 思方云2 ERP | 10 |
| 90 | M_EnvelopeWF | M_EnvelopeWF | 思方云2 ERP | 0 |
| 91 | M_Inventory | 物料库存 | 思方云2 ERP | 10 |
| 92 | M_InventoryBatch | 物料批次库存 | 思方云2 ERP | 40 |
| 93 | M_InventoryBatch_bak0413 | M_InventoryBatch_bak0413 | 思方云2 ERP | 0 |
| 94 | M_InventorybatchRemaining | 碎料管理 | 思方云2 ERP | 29 |
| 95 | M_InventoryCheck | 库存检验 | 思方云2 ERP | 13 |
| 96 | M_InventoryCheckItem | 库存检验明细 | 思方云2 ERP | 13 |
| 97 | M_InventoryMiscBatch | 杂项领料中的物料 | 思方云2 ERP | 18 |
| 98 | M_InventoryOut | 模组 | 思方云2 ERP | 12 |
| 99 | M_IQC | 物料IQC报废 | 思方云2 ERP | 40 |
| 100 | M_IQCHistory | M_IQCHistory | 思方云2 ERP | 28 |
| 101 | M_IQCItem | 物料IQC报废明细表 | 思方云2 ERP | 9 |
| 102 | M_IQCRecheck | 物料送检单管理 | 思方云2 ERP | 18 |
| 103 | M_IQCResult | 物料检验 报废原因 | 思方云2 ERP | 9 |
| 104 | M_IQCWF | M_IQCWF | 思方云2 ERP | 28 |
| 105 | M_MaterialIssueRequest | 领料和退料表 | 思方云2 ERP | 32 |
| 106 | M_MaterialIssueRequestHistory | 领料和退料审批历史 | 思方云2 ERP | 28 |
| 107 | M_MaterialIssueRequestItem | 领料和退料明细表 | 思方云2 ERP | 28 |
| 108 | M_MaterialIssueRequestWF | 领料和退料审批流程 | 思方云2 ERP | 28 |
| 109 | M_MaterialPackingSlipItem | 材料装运明细表 | 思方云2 ERP | 23 |
| 110 | M_MaterialPriceChangedItem | 采购报价明细表 | 思方云2 ERP | 19 |
| 111 | M_Materials | 物料表 | 思方云2 ERP | 117 |
| 112 | M_MaterialsCompany | 物料所属公司 | 思方云2 ERP | 5 |
| 113 | M_MaterialsCostByPlant | 物料可分配数量表(占用) | 思方云2 ERP | 8 |
| 114 | M_MaterialsIssueNote | 发料和退回表 | 思方云2 ERP | 16 |
| 115 | M_MaterialsIssueNoteItem | 发料和退回明细 | 思方云2 ERP | 0 |
| 116 | M_MaterialsIssueNoteItemBatch | 物料发料和退回批次 | 思方云2 ERP | 15 |
| 117 | M_MaterialsWarehouse | 物料所在仓库 | 思方云2 ERP | 11 |
| 118 | M_MonthlyClosing | 月结记账表 | 思方云2 ERP | 22 |
| 119 | M_MonthlyClosingDepartment | 物料月结部门表 | 思方云2 ERP | 22 |
| 120 | M_MonthlyClosingItem | 月结记账明细表 | 思方云2 ERP | 38 |
| 121 | M_PurchaseOrder | 采购单 | 思方云2 ERP | 0 |
| 122 | M_PurchaseOrderHistory | 采购审批表 | 思方云2 ERP | 28 |
| 123 | M_PurchaseOrderItem | 采购明细单 | 思方云2 ERP | 56 |
| 124 | M_PurchaseOrderWF | 采购待审批 | 思方云2 ERP | 28 |
| 125 | M_PurchasingBudget | 采购预算 | 思方云2 ERP | 0 |
| 126 | M_PurchasingBudgetItem | 预算明细（用户） | 思方云2 ERP | 0 |
| 127 | M_RDProject | 项目管理 | 思方云2 ERP | 0 |
| 128 | M_Receipt | 物料接收 | 思方云2 ERP | 17 |
| 129 | M_ReceiptItem | 物料接收明细 | 思方云2 ERP | 52 |
| 130 | M_ReplaceMaterials | M_ReplaceMaterials | 思方云2 ERP | 8 |
| 131 | M_Requisitions | 请购单 | 思方云2 ERP | 24 |
| 132 | M_RequisitionsHistory | 请购审批表 | 思方云2 ERP | 28 |
| 133 | M_RequisitionsItem | 请购明细单 | 思方云2 ERP | 21 |
| 134 | M_RequisitionsItemAccepted | 请购受理表 | 思方云2 ERP | 35 |
| 135 | M_RequisitionsWF | M_RequisitionsWF | 思方云2 ERP | 28 |
| 136 | M_ReturnOrder | 退货表 | 思方云2 ERP | 13 |
| 137 | M_ReturnOrderItem | 退货明细表 | 思方云2 ERP | 11 |
| 138 | M_SPDS | SPDS管理 | 思方云2 ERP | 35 |
| 139 | M_SPDSHistory | M_SPDSHistory | 思方云2 ERP | 28 |
| 140 | M_SPDSItem | SPDS管理明细 | 思方云2 ERP | 12 |
| 141 | M_SPDSWF | M_SPDSWF | 思方云2 ERP | 28 |
| 142 | M_StepCheck | M_StepCheck | 思方云2 ERP | 10 |
| 143 | M_StepCheckItem | M_StepCheckItem | 思方云2 ERP | 16 |
| 144 | M_Suppliers | 供应商资料 | 思方云2 ERP | 71 |
| 145 | M_SuppliersCompany | 供应商所属公司 | 思方云2 ERP | 5 |
| 146 | M_SuppliersHistory | 供应商审批记录 | 思方云2 ERP | 28 |
| 147 | M_SuppliersWF | M_SuppliersWF | 思方云2 ERP | 28 |
| 148 | M_Transfer | 调拨管理 | 思方云2 ERP | 14 |
| 149 | M_TransferItem | 调拨管理明细 | 思方云2 ERP | 12 |
| 150 | M_Warehousing | 物料入库 | 思方云2 ERP | 14 |
| 151 | M_WarehousingItem | 物料入库明细 | 思方云2 ERP | 26 |
| 152 | FGI_CartonsNumber | 装箱单编号表（箱包表） | 思方云2 ERP | 32 |
| 153 | FGI_Inventory | 成品库存 | 思方云2 ERP | 63 |
| 154 | FGI_InventoryOut | 成品出库批次号表 | 思方云2 ERP | 15 |
| 155 | FGI_IQC | 制成品检验单 | 思方云2 ERP | 61 |
| 156 | FGI_IQCHistory | FGI_IQCHistory | 思方云2 ERP | 28 |
| 157 | FGI_IQCItem | 检验项目 | 思方云2 ERP | 7 |
| 158 | FGI_IQCResult | 检验结果表 | 思方云2 ERP | 12 |
| 159 | FGI_IQCWF | FGI_IQCWF | 思方云2 ERP | 28 |
| 160 | FGI_JobIssueNote | FGI_JobIssueNote | 思方云2 ERP | 15 |
| 161 | FGI_JobIssueNoteItem | FGI_JobIssueNoteItem | 思方云2 ERP | 9 |
| 162 | FGI_JobIssueNoteItemBatch | FGI_JobIssueNoteItemBatch | 思方云2 ERP | 10 |
| 163 | FGI_JobIssueRequest | FGI_JobIssueRequest | 思方云2 ERP | 22 |
| 164 | FGI_JobIssueRequestHistory | FGI_JobIssueRequestHistory | 思方云2 ERP | 28 |
| 165 | FGI_JobIssueRequestItem | FGI_JobIssueRequestItem | 思方云2 ERP | 14 |
| 166 | FGI_JobIssueRequestWF | FGI_JobIssueRequestWF | 思方云2 ERP | 28 |
| 167 | FGI_MonthlyClosing | 成品月结 | 思方云2 ERP | 10 |
| 168 | FGI_MonthlyClosingItem | 成品月结明细 | 思方云2 ERP | 72 |
| 169 | FGI_PackingItem | 成品装箱单 | 思方云2 ERP | 20 |
| 170 | FGI_PackingSlip | 成品出货 | 思方云2 ERP | 52 |
| 171 | FGI_PackingSlipCartonsNumber | 箱包关联表 | 思方云2 ERP | 6 |
| 172 | FGI_PackingSlipHistory | FGI_PackingSlipHistory | 思方云2 ERP | 28 |
| 173 | FGI_PackingSlipItem | 成品出货明细表 | 思方云2 ERP | 48 |
| 174 | FGI_PackingSlipWF | FGI_PackingSlipWF | 思方云2 ERP | 28 |
| 175 | FGI_PackNumber | 箱包，包明细表 | 思方云2 ERP | 47 |
| 176 | FGI_PalletNumber | 卡板表 | 思方云2 ERP | 24 |
| 177 | FGI_Receipt | 制成品接收单 | 思方云2 ERP | 16 |
| 178 | FGI_ReceiptItem | 制成品接收单明细 | 思方云2 ERP | 59 |
| 179 | FGI_ReturnOrder | 成品退货表 | 思方云2 ERP | 13 |
| 180 | FGI_ReturnOrderItem | 成品退货明细表 | 思方云2 ERP | 13 |
| 181 | FGI_ScrapSheet | 成品报废 | 思方云2 ERP | 11 |
| 182 | FGI_ScrapSheetItem | 成品报废明细 | 思方云2 ERP | 9 |
| 183 | FGI_StockForm | 成品入库 | 思方云2 ERP | 0 |
| 184 | FGI_StockFormItem | 成品入库明细 | 思方云2 ERP | 58 |
| 185 | FGI_StockFormItemWO | 生产入库 | 思方云2 ERP | 9 |
| 186 | FGI_StockFormJob | 生产入库型号关联表 | 思方云2 ERP | 18 |
| 187 | FGI_Transfer | 成品转仓表 | 思方云2 ERP | 11 |
| 188 | FGI_TransferItem | 成品转仓明细表 | 思方云2 ERP | 11 |
| 189 | E_BoardTypeParameterSettings | 成德区分参数展示主表 | 思方云2 ERP | 0 |
| 190 | E_CostJobMfgPartsParams | 部件成本参数 | 思方云2 ERP | 7 |
| 191 | E_CustomScriptSetting | 工程流程那里添加的自定义脚本表 | 思方云2 ERP | 0 |
| 192 | E_DrillDetails | 钻孔设计 | 思方云2 ERP | 32 |
| 193 | E_DrillTitle | 钻带表 | 思方云2 ERP | 17 |
| 194 | E_FPCToolTable | 工具表 | 思方云2 ERP | 9 |
| 195 | E_Impedance | 阻抗表 | 思方云2 ERP | 0 |
| 196 | E_JobChildren | JOB关联合拼表 | 思方云2 ERP | 0 |
| 197 | E_JobImages | 生产型号图片 | 思方云2 ERP | 10 |
| 198 | E_JobLayers | 工作层  层信息 | 思方云2 ERP | 24 |
| 199 | E_JobMfgPartParams | 工程制作——流程——部件参数表 | 思方云2 ERP | 15 |
| 200 | E_JobMfgParts | 制造部件编号(本厂型号BOM表) | 思方云2 ERP | 40 |
| 201 | E_JobParams | 工程制作——基本信息——销售部件的参数值对应job这里的 | 思方云2 ERP | 14 |
| 202 | E_JobRouteParams | 流程参数值 | 思方云2 ERP | 17 |
| 203 | E_JobRoutes | 制造部件流程表 | 思方云2 ERP | 12 |
| 204 | E_JobSMTBOM | E_JobSMTBOM | 思方云2 ERP | 19 |
| 205 | E_JobTargetHole | E_JobTargetHole | 思方云2 ERP | 8 |
| 206 | E_ProcessLibrary | 产品分组（流程模版主表 | 思方云2 ERP | 7 |
| 207 | E_RiskWarning | 风险警示表 | 思方云2 ERP | 10 |
| 208 | E_SheetInfo | 大料信息表 | 思方云2 ERP | 0 |
| 209 | E_StackUpInfo | 工程制作——叠构 | 思方云2 ERP | 54 |
| 210 | E_ToolName | 工具表 | 思方云2 ERP | 5 |
| 211 | S_BusinessMan | 雇员信息 | 思方云2 ERP | 19 |
| 212 | S_CAR | S_CAR | 思方云2 ERP | 34 |
| 213 | S_Cartons | 纸箱定义 | 思方云2 ERP | 9 |
| 214 | S_Complainment | 客诉管理 | 思方云2 ERP | 1 |
| 215 | S_ComplainmentHistory | 客诉管理审批记录 | 思方云2 ERP | 28 |
| 216 | S_ComplainmentWF | S_ComplainmentWF | 思方云2 ERP | 0 |
| 217 | S_Conductor | 铜厚表 | 思方云2 ERP | 8 |
| 218 | S_Contract | 销售订单合同 | 思方云2 ERP | 32 |
| 219 | S_ContractItem | 合同明细 | 思方云2 ERP | 0 |
| 220 | S_ContractItem scti | 货币 | 思方云2 ERP | 0 |
| 221 | S_ContractItemAddCharge | 合同制造明细---额外费用表 | 思方云2 ERP | 7 |
| 222 | S_ContractItemHistory | 合同审核表 | 思方云2 ERP | 28 |
| 223 | S_ContractItemLog | 销售订单合同明细--修改记录 | 思方云2 ERP | 12 |
| 224 | S_ContractItemParameter | 订单明细参数 | 思方云2 ERP | 13 |
| 225 | S_ContractItemProject | S_ContractItemProject | 思方云2 ERP | 16 |
| 226 | S_ContractItemWF | S_ContractItemWF | 思方云2 ERP | 28 |
| 227 | S_ContractMaterials | 材料销售订单（贸易） | 思方云2 ERP | 36 |
| 228 | S_ContractSO | 销售订单表 | 思方云2 ERP | 43 |
| 229 | S_ContractSO scts | 合同明细 | 思方云2 ERP | 0 |
| 230 | S_Customer | 客户管理 | 思方云2 ERP | 44 |
| 231 | S_CustomerAddress | 客户管理--客户地址 | 思方云2 ERP | 34 |
| 232 | S_CustomerCompany | 客户绑定公司 | 思方云2 ERP | 5 |
| 233 | S_CustomerHistory | 客户管理审批记录 | 思方云2 ERP | 29 |
| 234 | S_CustomerWF | 客户审批 | 思方云2 ERP | 29 |
| 235 | S_ExpenseForm | 费用管理 | 思方云2 ERP | 19 |
| 236 | S_ExpenseFormHistory | 费用管理审批记录 | 思方云2 ERP | 28 |
| 237 | S_ExpenseFormItem | 费用管理明细 | 思方云2 ERP | 13 |
| 238 | S_ExpenseFormWF | S_ExpenseFormWF | 思方云2 ERP | 28 |
| 239 | S_ExpenseItem | 费用定义 | 思方云2 ERP | 9 |
| 240 | S_FGIIQCRecheck | 成品送检单 | 思方云2 ERP | 23 |
| 241 | S_FGIIQCRecheckItem | 成品送检单明细 | 思方云2 ERP | 7 |
| 242 | S_Job | 产品型号  生产部件 | 思方云2 ERP | 240 |
| 243 | S_JobHistory | 生产型号审批记录 | 思方云2 ERP | 28 |
| 244 | S_JobLink | 型号连接销售部件 | 思方云2 ERP | 6 |
| 245 | S_JobPrjLink | S_JobPrjLink | 思方云2 ERP | 8 |
| 246 | S_JobWF | 生产编号审批 | 思方云2 ERP | 28 |
| 247 | S_LayerType | 层信息 | 思方云2 ERP | 5 |
| 248 | S_MaterialFamily | 厂商型号 | 思方云2 ERP | 20 |
| 249 | S_MaterialType | 物料类型 | 思方云2 ERP | 10 |
| 250 | S_MaterialTypeCombination | 材料类型组合 | 思方云2 ERP | 5 |
| 251 | S_OrderType | 订单类型 | 思方云2 ERP | 11 |
| 252 | S_OS_PO | 外协采购单 | 思方云2 ERP | 37 |
| 253 | S_OS_POHistory | 外协采购单审批记录 | 思方云2 ERP | 28 |
| 254 | S_OS_POItem | 外协采购明细单 | 思方云2 ERP | 70 |
| 255 | S_OS_POItemAddCharge | 外发采购明细更改表 | 思方云2 ERP | 7 |
| 256 | S_OS_POWF | 外协采购单审批 | 思方云2 ERP | 28 |
| 257 | S_OS_PR | 外协请购单 | 思方云2 ERP | 30 |
| 258 | S_OS_PRHistory | 外协请购单审批记录 | 思方云2 ERP | 28 |
| 259 | S_OS_PRItem | 外协请购明细单 | 思方云2 ERP | 33 |
| 260 | S_OS_PRItemAddCharge | 外协请购明细单修改记录 | 思方云2 ERP | 7 |
| 261 | S_OS_PRWF | S_OS_PRWF | 思方云2 ERP | 28 |
| 262 | S_OS_Shipment | 外协装运 | 思方云2 ERP | 10 |
| 263 | S_OS_ShipmentItem | 外协装运明细 | 思方云2 ERP | 11 |
| 264 | S_OSWO | 外协采购工单表 | 思方云2 ERP | 32 |
| 265 | S_OSWOReceipt | 外协接收 | 思方云2 ERP | 23 |
| 266 | S_OSWOSend | 外协采购分配工单表 | 思方云2 ERP | 14 |
| 267 | S_OSWOShipment | 外协采购工单装运表 | 思方云2 ERP | 7 |
| 268 | S_Parameters | 销售数据--参数管理 | 思方云2 ERP | 32 |
| 269 | S_ParametersGroup | 销售数据--参数分组 | 思方云2 ERP | 9 |
| 270 | S_ParameterValue | 客户信息-评审-右侧的参数 | 思方云2 ERP | 0 |
| 271 | S_ProductCategory | 销售数据--产品分类 | 思方云2 ERP | 9 |
| 272 | S_ProductCategoryCompany | 销售数据--产品分类--公司 | 思方云2 ERP | 0 |
| 273 | S_ProductGroup | 销售数据--产品分组 | 思方云2 ERP | 29 |
| 274 | S_ProductGroupCompany | 销售数据--产品分组--公司 | 思方云2 ERP | 0 |
| 275 | S_ProductGroupSpec | 销售数据--产品分组-参数管理 | 思方云2 ERP | 5 |
| 276 | S_ProjectCombination | 销售数据--项目组合 | 思方云2 ERP | 12 |
| 277 | S_QuickQuoteResult | 报价单快速报价结果 | 思方云2 ERP | 41 |
| 278 | S_QuoteCategory | 报价类别 | 思方云2 ERP | 8 |
| 279 | S_QuoteGroup | 报价分组 | 思方云2 ERP | 8 |
| 280 | S_QuoteParameter | 报价参数 | 思方云2 ERP | 6 |
| 281 | S_ReturnSO | 客诉管理--扣款明细 | 思方云2 ERP | 31 |
| 282 | S_Rfq | 报价单 | 思方云2 ERP | 69 |
| 283 | S_RfqAddCharge | 报价单额外费用 | 思方云2 ERP | 7 |
| 284 | S_RfqHistory | 报价单审批历史 | 思方云2 ERP | 28 |
| 285 | S_RfqParameter | 报价单参数 | 思方云2 ERP | 17 |
| 286 | S_RfqWF | 报价单审批 | 思方云2 ERP | 28 |
| 287 | S_Rpt_Member | S_Rpt_Member | 思方云2 ERP | 6 |
| 288 | S_Rpt_SalesRepresentative | S_Rpt_SalesRepresentative | 思方云2 ERP | 16 |
| 289 | S_SaleProject | 销售项目 | 思方云2 ERP | 6 |
| 290 | S_SalesForecast | 销售预测 | 思方云2 ERP | 57 |
| 291 | S_SalesForecastHistory | 销售预测审批历史 | 思方云2 ERP | 28 |
| 292 | S_SalesForecastItem | 销售预测明细 | 思方云2 ERP | 12 |
| 293 | S_SalesForecastSplitting | 销售预测分单 | 思方云2 ERP | 13 |
| 294 | S_SalesForecastWF | 销售预测审批 | 思方云2 ERP | 28 |
| 295 | S_SalesParts | 销售部件 | 思方云2 ERP | 57 |
| 296 | S_SalesPartsAdditionalBOM | 销售部件--AdditionalBOM | 思方云2 ERP | 7 |
| 297 | S_SalesPartsLayers | 销售部件层信息表 | 思方云2 ERP | 23 |
| 298 | S_SalesPartsParameter | 销售部件对应产品分组参数值 | 思方云2 ERP | 13 |
| 299 | S_SalesPartsSets | 销售部件对应套板信息 | 思方云2 ERP | 9 |
| 300 | S_SalesPartsSMTBOM | 销售部件对应PCBA材料单 | 思方云2 ERP | 19 |
| 301 | S_SalesPlanReview | 销售订单更改记录 | 思方云2 ERP | 17 |
| 302 | S_ShipmentRevoke | 撤销出货表 | 思方云2 ERP | 13 |
| 303 | S_SODayShipment | 订单装运表 | 思方云2 ERP | 6 |
| 304 | S_SOMatWriteOff | 备货冲销记录 | 思方云2 ERP | 0 |
| 305 | S_StockCheck | 成品盘点表 | 思方云2 ERP | 13 |
| 306 | S_StockCheckItem | 成品盘点明细表 | 思方云2 ERP | 9 |
| 307 | S_WorkPlan | 工作计划表 | 思方云2 ERP | 20 |
| 308 | S_WorkPlanItem | 工作计划明细表 | 思方云2 ERP | 9 |
| 309 | S_WorkPlantHistory | 工作计划审批记录表 | 思方云2 ERP | 28 |
| 310 | S_WorkPlantWF | S_WorkPlantWF | 思方云2 ERP | 28 |
| 311 | P_BOMBatching | BOM领料批次 | 思方云2 ERP | 19 |
| 312 | P_ECN | OCN\ECN管理 | 思方云2 ERP | 130 |
| 313 | P_ECNHistory | OCN\ECN管理-审批记录 | 思方云2 ERP | 28 |
| 314 | P_ECNLog | OCN\ECN管理-工具-工具类型 | 思方云2 ERP | 6 |
| 315 | P_ECNTool | OCN\ECN审核 | 思方云2 ERP | 14 |
| 316 | P_ECNWF | OCN/ECN审批流程 | 思方云2 ERP | 28 |
| 317 | P_Inspection | MRB检查 | 思方云2 ERP | 22 |
| 318 | P_IPQC | P_IPQC | 思方云2 ERP | 16 |
| 319 | P_IPQCItem | P_IPQCItem | 思方云2 ERP | 22 |
| 320 | P_MergeOrder | 合拼单 | 思方云2 ERP | 18 |
| 321 | P_MergeOrderSO | 合拼明细表 | 思方云2 ERP | 10 |
| 322 | P_MfgPartsInv | 部件表 | 思方云2 ERP | 15 |
| 323 | P_MfgPartsIssue | 部件使用情况表 | 思方云2 ERP | 10 |
| 324 | P_MfgUpRevLog | 部件升级记录 | 思方云2 ERP | 10 |
| 325 | P_MO | 制造订单表 | 思方云2 ERP | 69 |
| 326 | P_MOBOM | 制造订单表中的BOM | 思方云2 ERP | 18 |
| 327 | P_ModRoute | OCN/ECN工单变更 | 思方云2 ERP | 12 |
| 328 | P_ModRouteItem | OCN/ECN工单变更流程 | 思方云2 ERP | 5 |
| 329 | P_ModRouteLog | MO修改记录 | 思方云2 ERP | 8 |
| 330 | P_ModRouteParams | OCN/ECN工单变更参数 | 思方云2 ERP | 13 |
| 331 | P_ModRouteWO | OCN/ECN工单变更工单列表 | 思方云2 ERP | 4 |
| 332 | P_MOMfgPart | 制造订单中的制造部件 | 思方云2 ERP | 17 |
| 333 | P_MOMfgPartParams | 制造订单中的制造部件参数 | 思方云2 ERP | 15 |
| 334 | P_MORoute | 制作订单的工艺流程(过数记录明细)云1的online表，老系统的56表 | 思方云2 ERP | 51 |
| 335 | P_MORouteParams | 工单流程参数 | 思方云2 ERP | 14 |
| 336 | P_MOSO | 制造订单\销售订单 | 思方云2 ERP | 9 |
| 337 | P_MRBRequisition | MRB送检申请 | 思方云2 ERP | 24 |
| 338 | P_MRP | MRP物资需求计划 | 思方云2 ERP | 12 |
| 339 | P_MRPREQ | P_MRPREQ | 思方云2 ERP | 17 |
| 340 | P_MRPREQItem | P_MRPREQItem | 思方云2 ERP | 16 |
| 341 | P_OutPut | 工单过数记录表 | 思方云2 ERP | 38 |
| 342 | P_PQE | P_PQE | 思方云2 ERP | 19 |
| 343 | P_RetrospectTool | P_RetrospectTool | 思方云2 ERP | 6 |
| 344 | P_ReWork | 返工表 | 思方云2 ERP | 21 |
| 345 | P_ReWorkApplication | P_ReWorkApplication | 思方云2 ERP | 21 |
| 346 | P_ReWorkApplicationProcess | P_ReWorkApplicationProcess | 思方云2 ERP | 6 |
| 347 | P_SOBOM | 订单BOM表 | 思方云2 ERP | 16 |
| 348 | P_SplitWOLog | 工单拆分记录 | 思方云2 ERP | 10 |
| 349 | P_ToolApply | 工具申请单 | 思方云2 ERP | 26 |
| 350 | P_ToolApplyHistory | 工具申请审批流程记录 | 思方云2 ERP | 28 |
| 351 | P_ToolApplyWF | P_ToolApplyWF | 思方云2 ERP | 28 |
| 352 | P_ToolIssued | 工具发放 | 思方云2 ERP | 15 |
| 353 | P_ToolReturned | 工具退回 | 思方云2 ERP | 16 |
| 354 | P_Tools | 工具登记表 | 思方云2 ERP | 25 |
| 355 | P_ToolTypes | 工具类型 | 思方云2 ERP | 13 |
| 356 | P_ToolTypeWarehouse | 工具类型所在仓库 | 思方云2 ERP | 11 |
| 357 | P_UpdateLog | P_UpdateLog | 思方云2 ERP | 15 |
| 358 | P_WO | 工作单号 | 思方云2 ERP | 40 |
| 359 | P_WOIQC | 工单IQC | 思方云2 ERP | 6 |
| 360 | P_WOProcessBack | P_WOProcessBack | 思方云2 ERP | 0 |
| 361 | P_WOProcessSend | P_WOProcessSend | 思方云2 ERP | 10 |
| 362 | P_WOProcessStock | P_WOProcessStock | 思方云2 ERP | 7 |
| 363 | P_WOSO | 工单对应销售单 | 思方云2 ERP | 7 |
| 364 | P_WOSplitBatchApplication | P_WOSplitBatchApplication | 思方云2 ERP | 21 |
| 365 | P_WOTransfer | 工单转出记录 | 思方云2 ERP | 48 |
| 366 | F_AccCostWOByPeriod | 财务应用-成本核算-成本明细 | 思方云2 ERP | 38 |
| 367 | F_AccCostWOBySteps | 工单成本明细 | 思方云2 ERP | 48 |
| 368 | F_AccountGroups | 财务管理-财务数据-科目分组 | 思方云2 ERP | 4 |
| 369 | F_AccountProjects | F_AccountProjects | 思方云2 ERP | 149 |
| 370 | F_Accounts | 科目管理 | 思方云2 ERP | 162 |
| 371 | F_AllScrapWOCost | F_AllScrapWOCost | 思方云2 ERP | 16 |
| 372 | F_AP_DebitMemo | 供应商扣款 | 思方云2 ERP | 50 |
| 373 | F_AP_DebitMemoItem | 供应商扣款明细 | 思方云2 ERP | 15 |
| 374 | F_AP_Disburse | 应付账款/付款管理 | 思方云2 ERP | 47 |
| 375 | F_AP_DisburseItem | 应付账款/付款管理明细 | 思方云2 ERP | 7 |
| 376 | F_AP_Invoice | 采购发票 | 思方云2 ERP | 47 |
| 377 | F_AP_InvoiceItem | 采购发票明细 | 思方云2 ERP | 27 |
| 378 | F_AP_Reconcile | 采购对账 | 思方云2 ERP | 36 |
| 379 | F_AP_ReconcileItems | 采购对账明细 | 思方云2 ERP | 28 |
| 380 | F_AR_CreditMemo | 客户扣款（对账和发票） | 思方云2 ERP | 51 |
| 381 | F_AR_CreditMemoItem | 客户扣款明细 | 思方云2 ERP | 14 |
| 382 | F_AR_Invoice | 财务管理-财务应用-应收账款-销售发票 | 思方云2 ERP | 50 |
| 383 | F_AR_InvoiceItem | 销售发票明细 | 思方云2 ERP | 26 |
| 384 | F_AR_Receivable | 收款管理 | 思方云2 ERP | 48 |
| 385 | F_AR_ReceivableItem | 收款管理明细 | 思方云2 ERP | 7 |
| 386 | F_AR_SOReconcile | 财务管理-财务应用-应收账款-销售对账 | 思方云2 ERP | 38 |
| 387 | F_AR_SOReconcileItems | 销售对账明细 | 思方云2 ERP | 32 |
| 388 | F_AssetCategoryItem | 财务管理-资产管理-资产类别明细表 | 思方云2 ERP | 12 |
| 389 | F_AssetCategorys | 财务管理-资产管理-资产类别 | 思方云2 ERP | 13 |
| 390 | F_AssetChange | 资产变动管理 | 思方云2 ERP | 19 |
| 391 | F_AssetChangeHistory | F_AssetChangeHistory | 思方云2 ERP | 0 |
| 392 | F_AssetChangeItem | 资产变动管理明细 | 思方云2 ERP | 17 |
| 393 | F_AssetChangeWays | 资产变动方式 | 思方云2 ERP | 6 |
| 394 | F_AssetChangeWF | F_AssetChangeWF | 思方云2 ERP | 0 |
| 395 | F_AssetDisposal | 资产清理 | 思方云2 ERP | 17 |
| 396 | F_AssetStatus | 资产状态 | 思方云2 ERP | 5 |
| 397 | F_BankAccounts | 现金账户 | 思方云2 ERP | 30 |
| 398 | F_BankReconcile | 银行对账 | 思方云2 ERP | 12 |
| 399 | F_BankReconcileItem | 银行对账明细 | 思方云2 ERP | 37 |
| 400 | F_BankReconcileSeting | 银行对账配置 | 思方云2 ERP | 6 |
| 401 | F_BankReconcileSetingItem | 银行对账配置明细 | 思方云2 ERP | 6 |
| 402 | F_CashAccount | 现金账流水 | 思方云2 ERP | 21 |
| 403 | F_CashAccountItem | 现金账流水明细 | 思方云2 ERP | 11 |
| 404 | F_CloseCashAccount | 出纳管理/现金账 | 思方云2 ERP | 13 |
| 405 | F_CloseCashAccountItem | 出纳管理/现金账明细 | 思方云2 ERP | 6 |
| 406 | F_CurrExchAdj | 期末调汇 | 思方云2 ERP | 10 |
| 407 | F_CurrExchAdjItem | 期末调汇明细 | 思方云2 ERP | 9 |
| 408 | F_Depreciation | 折旧计提 | 思方云2 ERP | 10 |
| 409 | F_DepreciationItem | 折旧计提明细表 | 思方云2 ERP | 8 |
| 410 | F_DiaryAccount | 凭证登记 | 思方云2 ERP | 36 |
| 411 | F_DiaryAccountHistory | F_DiaryAccountHistory | 思方云2 ERP | 0 |
| 412 | F_DiaryAccountItem | 凭证登记明细表 | 思方云2 ERP | 19 |
| 413 | F_DiaryAccountWF | F_DiaryAccountWF | 思方云2 ERP | 0 |
| 414 | F_FixedAssets | 固定资产 | 思方云2 ERP | 45 |
| 415 | F_FixedAssetsItem | 固定资产明细 | 思方云2 ERP | 7 |
| 416 | F_GL_Setting | 科目设定 | 思方云2 ERP | 8 |
| 417 | F_GL_SettingItem | 科目设定明细 | 思方云2 ERP | 7 |
| 418 | F_LastPeriodWoBalanceCost | 结存表 | 思方云2 ERP | 12 |
| 419 | F_PackingSlipItemContractSO | F_PackingSlipItemContractSO | 思方云2 ERP | 20 |
| 420 | F_PaymentRequest | 请款单 | 思方云2 ERP | 0 |
| 421 | F_PlantBusiness | 销售单位、财务设置里面的业务类型 | 思方云2 ERP | 8 |
| 422 | F_PlantBusinessItem | 工厂业务明细 | 思方云2 ERP | 13 |
| 423 | F_Post | 出纳扎账&财务过账 | 思方云2 ERP | 11 |
| 424 | F_PostItem | 出纳扎账明细 | 思方云2 ERP | 29 |
| 425 | F_ProjectCatagory | 核算项目 | 思方云2 ERP | 15 |
| 426 | F_ProjectCatagoryItem | 核算项目明细 | 思方云2 ERP | 16 |
| 427 | F_ProvisionalEstimate | 应付暂估 | 思方云2 ERP | 20 |
| 428 | F_ProvisionalEstimateItem | 应付暂估明细 | 思方云2 ERP | 41 |
| 429 | F_RefLib | 凭证摘要 | 思方云2 ERP | 8 |
| 430 | F_TradingBusiness | 交易业务 | 思方云2 ERP | 6 |
| 431 | F_Voucher | 凭证 | 思方云2 ERP | 40 |
| 432 | F_VoucherDesc | 凭证描述 | 思方云2 ERP | 6 |
| 433 | F_VoucherHistory | 凭证审批历史记录 | 思方云2 ERP | 0 |
| 434 | F_VoucherItem | 凭证明细 | 思方云2 ERP | 18 |
| 435 | F_VoucherProject | F_VoucherProject | 思方云2 ERP | 7 |
| 436 | F_VoucherWF | 凭证审批记录 | 思方云2 ERP | 0 |
| 437 | C_CostSetting | 产品项目 | 思方云2 ERP | 9 |
| 438 | C_CostSettingItem | 成本设置对应工艺和工序 | 思方云2 ERP | 9 |
| 439 | C_CostSharing | 费用分组（费用管理） | 思方云2 ERP | 10 |
| 440 | C_CostSharingItem | 费用分组明细（费用管理明细） | 思方云2 ERP | 7 |
| 441 | C_CostSharingItemCount | 费用管理--项目明细 | 思方云2 ERP | 13 |
| 442 | C_CostSharingOutputDetail | C_CostSharingOutputDetail | 思方云2 ERP | 11 |
| 443 | C_CostType | 项目类型 | 思方云2 ERP | 5 |
| 444 | C_DirectBomCost | 直接成本 | 思方云2 ERP | 0 |
| 445 | C_FinancialReport | C_FinancialReport | 思方云2 ERP | 0 |
| 446 | C_FinancialReportItem | C_FinancialReportItem | 思方云2 ERP | 0 |
| 447 | C_JobCostPeriods | C_JobCostPeriods | 思方云2 ERP | 1 |
| 448 | C_JobWoDetailsCalStatus | 工单明细成本 | 思方云2 ERP | 0 |
| 449 | C_StepIndirecMatCost | C_StepIndirecMatCost | 思方云2 ERP | 9 |
| 450 | EQ_Equipments | 设备管理表 | 思方云2 ERP | 24 |
| 451 | EQ_MLO | 设备保养管理 | 思方云2 ERP | 42 |
| 452 | EQ_MLOEmployees | EQ_MLOEmployees | 思方云2 ERP | 4 |
| 453 | EQ_MLOEQ | EQ_MLOEQ | 思方云2 ERP | 4 |
| 454 | EQ_MLOHistory | EQ_MLOHistory | 思方云2 ERP | 28 |
| 455 | EQ_MLOMaterials | 设备保养明细 | 思方云2 ERP | 11 |
| 456 | EQ_MLOTasks | EQ_MLOTasks | 思方云2 ERP | 0 |
| 457 | EQ_MLOWF | 设备保养审批 | 思方云2 ERP | 0 |
| 458 | EQ_PMO | P_MORouteParams | 思方云2 ERP | 38 |
| 459 | EQ_PMOEmployees | 设备维修管理关联雇员表 | 思方云2 ERP | 4 |
| 460 | EQ_PMOHistory | 设备维修管理--审核记录 | 思方云2 ERP | 0 |
| 461 | EQ_PMOMaterials | 设备维修管理--物料 | 思方云2 ERP | 11 |
| 462 | EQ_PMOTasks | 设备维修管理--任务 | 思方云2 ERP | 0 |
| 463 | EQ_PMOWF | EQ_PMOWF | 思方云2 ERP | 0 |
| 464 | EQ_PreventiveEQ | 设备保养定义关联设备表 | 思方云2 ERP | 4 |
| 465 | EQ_PreventiveMaterials | 保养类型和物料关联表 | 思方云2 ERP | 7 |
| 466 | EQ_Preventives | 设备保养定义 | 思方云2 ERP | 25 |
| 467 | EQ_PreventiveTasks | 设备保养定义管理任务表 | 思方云2 ERP | 4 |
| 468 | EQ_Spareparts | 设备管理--物料 | 思方云2 ERP | 2 |
| 469 | PM_Faults | 故障现象 | 思方云2 ERP | 8 |
| 470 | PM_Group | 维修分组 | 思方云2 ERP | 10 |
| 471 | PM_GroupEmployees | 维修分组--用户 | 思方云2 ERP | 6 |
| 472 | PM_IssueForm | 维修发料 | 思方云2 ERP | 8 |
| 473 | PM_IssueFormItem | 维修发料-维修单和保养单 | 思方云2 ERP | 7 |
| 474 | PM_IssueReturnBatch | 维修退料批次 | 思方云2 ERP | 14 |
| 475 | PM_Reasons | 故障原因 | 思方云2 ERP | 8 |
| 476 | PM_ReturnForm | 维修退料 | 思方云2 ERP | 8 |
| 477 | PM_ReturnFormItem | 维修退料明细 | 思方云2 ERP | 6 |
| 478 | PM_Tasks | 标准任务 | 思方云2 ERP | 13 |
| 479 | PM_Types | 业务员 | 思方云2 ERP | 9 |
| 480 | EQUIPMENT | 设备 | 思方云2 ERP | 18 |
| 481 | EQUIPMENT_GROUP | EQUIPMENT_GROUP | 思方云2 ERP | 5 |
| 482 | STEP | 工序表 | 思方云2 ERP | 29 |
| 483 | JBPM4_DEPLOYMENT | JBPM4_DEPLOYMENT | 思方云2 ERP | 0 |
| 484 | JBPM4_DEPLOYPROP | JBPM4_DEPLOYPROP | 思方云2 ERP | 0 |
| 485 | JBPM4_EXECUTION | JBPM4_EXECUTION | 思方云2 ERP | 0 |
| 486 | JBPM4_HIST_ACTINST | JBPM4_HIST_ACTINST | 思方云2 ERP | 0 |
| 487 | JBPM4_HIST_DETAIL | JBPM4_HIST_DETAIL | 思方云2 ERP | 0 |
| 488 | JBPM4_HIST_PROCINST | JBPM4_HIST_PROCINST | 思方云2 ERP | 0 |
| 489 | JBPM4_HIST_TASK | JBPM4_HIST_TASK | 思方云2 ERP | 0 |
| 490 | JBPM4_HIST_VAR | JBPM4_HIST_VAR | 思方云2 ERP | 0 |
| 491 | JBPM4_ID_GROUP | JBPM4_ID_GROUP | 思方云2 ERP | 0 |
| 492 | JBPM4_ID_MEMBERSHIP | JBPM4_ID_MEMBERSHIP | 思方云2 ERP | 0 |
| 493 | JBPM4_ID_USER | JBPM4_ID_USER | 思方云2 ERP | 0 |
| 494 | JBPM4_JOB | JBPM4_JOB | 思方云2 ERP | 0 |
| 495 | JBPM4_LOB | JBPM4_LOB | 思方云2 ERP | 0 |
| 496 | JBPM4_PARTICIPATION | JBPM4_PARTICIPATION | 思方云2 ERP | 0 |
| 497 | JBPM4_PROPERTY | JBPM4_PROPERTY | 思方云2 ERP | 0 |
| 498 | JBPM4_SWIMLANE | JBPM4_SWIMLANE | 思方云2 ERP | 0 |
| 499 | JBPM4_TASK | JBPM4_TASK | 思方云2 ERP | 0 |
| 500 | JBPM4_VARIABLE | JBPM4_VARIABLE | 思方云2 ERP | 0 |
| 501 | A_AAA | A_AAA | 思方云2 ERP | 0 |
| 502 | a_allMaterialsFromZB20170221 | a_allMaterialsFromZB20170221 | 思方云2 ERP | 0 |
| 503 | a_backup_deletedMatrlList_20170325 | a_backup_deletedMatrlList_20170325 | 思方云2 ERP | 0 |
| 504 | a_CustomerfromZB20170221 | a_CustomerfromZB20170221 | 思方云2 ERP | 0 |
| 505 | a_CustomerfromZB20170221-1 | a_CustomerfromZB20170221-1 | 思方云2 ERP | 0 |
| 506 | a_DeletedMtrlList_20170325 | a_DeletedMtrlList_20170325 | 思方云2 ERP | 0 |
| 507 | a_FGI_Inevneotyr_20170506 | a_FGI_Inevneotyr_20170506 | 思方云2 ERP | 0 |
| 508 | a_fgibal_20170401 | a_fgibal_20170401 | 思方云2 ERP | 0 |
| 509 | a_FGIStock0401 | a_FGIStock0401 | 思方云2 ERP | 0 |
| 510 | a_import_fgi-0301 | a_import_fgi-0301 | 思方云2 ERP | 0 |
| 511 | a_import_Materials-0301 | a_import_Materials-0301 | 思方云2 ERP | 0 |
| 512 | a_log1_02262017922PM | a_log1_02262017922PM | 思方云2 ERP | 0 |
| 513 | a_log1_02262017923PM | a_log1_02262017923PM | 思方云2 ERP | 0 |
| 514 | a_log1_022720171031PM | a_log1_022720171031PM | 思方云2 ERP | 0 |
| 515 | a_log1_02282017943PM | a_log1_02282017943PM | 思方云2 ERP | 0 |
| 516 | a_log1_03162017933PM | a_log1_03162017933PM | 思方云2 ERP | 0 |
| 517 | a_log1_03312017615PM | a_log1_03312017615PM | 思方云2 ERP | 0 |
| 518 | a_log1_03312017617PM | a_log1_03312017617PM | 思方云2 ERP | 0 |
| 519 | a_log1_03312017657PM | a_log1_03312017657PM | 思方云2 ERP | 0 |
| 520 | a_log2_02262017922PM | a_log2_02262017922PM | 思方云2 ERP | 0 |
| 521 | a_log2_02262017923PM | a_log2_02262017923PM | 思方云2 ERP | 0 |
| 522 | a_log2_02282017943PM | a_log2_02282017943PM | 思方云2 ERP | 0 |
| 523 | a_log2_03312017615PM | a_log2_03312017615PM | 思方云2 ERP | 0 |
| 524 | a_log2_03312017617PM | a_log2_03312017617PM | 思方云2 ERP | 0 |
| 525 | a_log2_03312017657PM | a_log2_03312017657PM | 思方云2 ERP | 0 |
| 526 | a_log2_041012017657AM | a_log2_041012017657AM | 思方云2 ERP | 0 |
| 527 | a_log2_041112017657AM | a_log2_041112017657AM | 思方云2 ERP | 0 |
| 528 | a_log2_20170403 | a_log2_20170403 | 思方云2 ERP | 0 |
| 529 | a_mtrlBal_20170401 | a_mtrlBal_20170401 | 思方云2 ERP | 0 |
| 530 | a_mtrlbal_20170401_1 | a_mtrlbal_20170401_1 | 思方云2 ERP | 0 |
| 531 | a_oldErp_So$ | a_oldErp_So$ | 思方云2 ERP | 0 |
| 532 | a_olderp_so2$ | a_olderp_so2$ | 思方云2 ERP | 0 |
| 533 | a_P_MOROUTE_20170506 | a_P_MOROUTE_20170506 | 思方云2 ERP | 0 |
| 534 | a_SM_FromZB20170220 | a_SM_FromZB20170220 | 思方云2 ERP | 0 |
| 535 | a_UpdatePanelSize_20170302 | a_UpdatePanelSize_20170302 | 思方云2 ERP | 0 |
| 536 | a_UpdatePanelSize_20170302_1 | a_UpdatePanelSize_20170302_1 | 思方云2 ERP | 0 |
| 537 | a_旧成品库存$ | a_旧成品库存$ | 思方云2 ERP | 0 |
| 538 | a_物料批次货位$ | a_物料批次货位$ | 思方云2 ERP | 0 |
| 539 | a_物料批次货位2$ | a_物料批次货位2$ | 思方云2 ERP | 0 |
| 540 | a_物料批次货位3$ | a_物料批次货位3$ | 思方云2 ERP | 0 |
| 541 | alan_materails_20170211 | alan_materails_20170211 | 思方云2 ERP | 0 |
| 542 | alan_parameter_mapping | alan_parameter_mapping | 思方云2 ERP | 0 |
| 543 | F_AccountSetting1 | 工厂管理-应收应付 | 思方云2 ERP | 0 |
| 544 | F_AccountSetting2 | F_AccountSetting2 | 思方云2 ERP | 0 |
| 545 | F_AccountSetting3 | F_AccountSetting3 | 思方云2 ERP | 0 |
| 546 | F_AccountSetting4 | F_AccountSetting4 | 思方云2 ERP | 0 |
| 547 | fgi_inventory_0427_2200 | fgi_inventory_0427_2200 | 思方云2 ERP | 0 |
| 548 | FGI_Inventory_backup_0420 | FGI_Inventory_backup_0420 | 思方云2 ERP | 0 |
| 549 | FGI_Inventory_BAK20170407 | FGI_Inventory_BAK20170407 | 思方云2 ERP | 0 |
| 550 | fgi_inventory_bak_0429 | fgi_inventory_bak_0429 | 思方云2 ERP | 0 |
| 551 | FGI_StockFormItem_bak0407 | FGI_StockFormItem_bak0407 | 思方云2 ERP | 0 |
| 552 | FGI_StockFormItem_moid_bak | FGI_StockFormItem_moid_bak | 思方云2 ERP | 0 |
| 553 | M_MaterialsWarehouse_bak | M_MaterialsWarehouse_bak | 思方云2 ERP | 0 |
| 554 | M_MaterialsWarehouse_bak0413 | M_MaterialsWarehouse_bak0413 | 思方云2 ERP | 0 |
| 555 | p_bombatching_0413 | p_bombatching_0413 | 思方云2 ERP | 0 |
| 556 | xnh_ChangedToConsigment_411 | xnh_ChangedToConsigment_411 | 思方云2 ERP | 0 |
| 557 | xnh_ChangedToConsigment_412 | xnh_ChangedToConsigment_412 | 思方云2 ERP | 0 |
| 558 | xnh_reworkChangeLog-返工工序记录 | xnh_reworkChangeLog-返工工序记录 | 思方云2 ERP | 0 |
| 559 | xnh_奇立04010405_1724_item | xnh_奇立04010405_1724_item | 思方云2 ERP | 0 |
| 560 | xnh_底油线路 | xnh_底油线路 | 思方云2 ERP | 0 |
| 561 | xnh_贵阳海信_item | xnh_贵阳海信_item | 思方云2 ERP | 0 |
| 562 | xnh_达信20170405001_item | xnh_达信20170405001_item | 思方云2 ERP | 0 |
| 563 | xnh_高效170331_item | xnh_高效170331_item | 思方云2 ERP | 0 |
| 564 | 操作员$ | 操作员$ | 思方云2 ERP | 0 |
| 565 | 转序员$ | 转序员$ | 思方云2 ERP | 0 |
| 566 | -MO已分配数量-SO已分配数量 | 物料 | 思方云2 ERP | 4 |
| 567 | A_account | 财务管理-财务数据-科目管理上级 | 思方云2 ERP | 15 |
| 568 | a_addlPHPart | a_addlPHPart | 思方云2 ERP | 0 |
| 569 | a_AllInfo | a_AllInfo | 思方云2 ERP | 0 |
| 570 | a_atom | a_atom | 思方云2 ERP | 0 |
| 571 | a_CoreToBeFixed | a_CoreToBeFixed | 思方云2 ERP | 0 |
| 572 | a_DeletedJob | a_DeletedJob | 思方云2 ERP | 0 |
| 573 | a_deletespds | a_deletespds | 思方云2 ERP | 0 |
| 574 | a_drill | a_drill | 思方云2 ERP | 0 |
| 575 | a_drill_adjustbase | a_drill_adjustbase | 思方云2 ERP | 0 |
| 576 | a_fgi_batch | a_fgi_batch | 思方云2 ERP | 0 |
| 577 | a_FGI_Inventory | a_FGI_Inventory | 思方云2 ERP | 0 |
| 578 | a_importSO_AE | a_importSO_AE | 思方云2 ERP | 0 |
| 579 | a_ImportSO_Flex | a_ImportSO_Flex | 思方云2 ERP | 0 |
| 580 | a_importSO_PPC | a_importSO_PPC | 思方云2 ERP | 0 |
| 581 | a_JobRouteParam | a_JobRouteParam | 思方云2 ERP | 0 |
| 582 | a_JobRoutes | a_JobRoutes | 思方云2 ERP | 0 |
| 583 | a_laminate | a_laminate | 思方云2 ERP | 0 |
| 584 | a_Materials | a_Materials | 思方云2 ERP | 0 |
| 585 | a_MaterialsFromWH | a_MaterialsFromWH | 思方云2 ERP | 0 |
| 586 | a_materialwithoutwh | a_materialwithoutwh | 思方云2 ERP | 0 |
| 587 | A_MET2 | A_MET2 | 思方云2 ERP | 0 |
| 588 | a_OdrBatch | a_OdrBatch | 思方云2 ERP | 0 |
| 589 | a_old_erp_so | a_old_erp_so | 思方云2 ERP | 0 |
| 590 | a_osScrapHistory | a_osScrapHistory | 思方云2 ERP | 0 |
| 591 | A_PARTTODOLIST | A_PARTTODOLIST | 思方云2 ERP | 0 |
| 592 | a_poList | a_poList | 思方云2 ERP | 0 |
| 593 | a_PP_FromZB20170220 | a_PP_FromZB20170220 | 思方云2 ERP | 0 |
| 594 | a_ReWo_Status | a_ReWo_Status | 思方云2 ERP | 0 |
| 595 | a_reworkhistory-返工单 | a_reworkhistory-返工单 | 思方云2 ERP | 0 |
| 596 | a_Route | a_Route | 思方云2 ERP | 0 |
| 597 | a_ScrapHistory-外发报废 | a_ScrapHistory-外发报废 | 思方云2 ERP | 0 |
| 598 | a_stepInfo | a_stepInfo | 思方云2 ERP | 0 |
| 599 | A_Title | A_Title | 思方云2 ERP | 0 |
| 600 | a_wo_Rework | a_wo_Rework | 思方云2 ERP | 0 |
| 601 | a_yd | a_yd | 思方云2 ERP | 0 |
| 602 | ab_OdrBatch | ab_OdrBatch | 思方云2 ERP | 0 |
| 603 | AND scts.fromId=scti.plantsId | 供应商 | 思方云2 ERP | 7 |
| 604 | and 主工单.Id=子工单.parentId | 发放人 | 思方云2 ERP | 25 |
| 605 | b_matrl | 物料批次库存 | 思方云2 ERP | 24 |
| 606 | b_Update_JobCustomer | b_Update_JobCustomer | 思方云2 ERP | 0 |
| 607 | b_Update_SalesPartCustomer | b_Update_SalesPartCustomer | 思方云2 ERP | 0 |
| 608 | B_USER_WIP01 | B_USER_WIP01 | 思方云2 ERP | 0 |
| 609 | ba | ba | 思方云2 ERP | 0 |
| 610 | e2 | e2 | 思方云2 ERP | 13 |
| 611 | fgi_cartonsnumber | fgi_cartonsnumber | 思方云2 ERP | 0 |
| 612 | fgi_sotransfer | 寄售 | 思方云2 ERP | 0 |
| 613 | IMP_CustInfo | 客户备份信息 | 思方云2 ERP | 95 |
| 614 | IMP_CustMapping | IMP_CustMapping | 思方云2 ERP | 0 |
| 615 | IMP_OdrBatch | IMP_OdrBatch | 思方云2 ERP | 0 |
| 616 | IMP_OdrProdNo | IMP_OdrProdNo | 思方云2 ERP | 0 |
| 617 | imp_OrderList | imp_OrderList | 思方云2 ERP | 0 |
| 618 | IMP_PnInfo | IMP_PnInfo | 思方云2 ERP | 0 |
| 619 | IMP_User | IMP_User | 思方云2 ERP | 0 |
| 620 | org_DrillDetails | 钻孔历史记录表 | 思方云2 ERP | 11 |
| 621 | qty_Order | qty_Order | 思方云2 ERP | 5 |
| 622 | rpt_moRoute_snap | rpt_moRoute_snap | 思方云2 ERP | 0 |
| 623 | rpt_ShopFloorInfo | rpt_ShopFloorInfo | 思方云2 ERP | 0 |
| 624 | rpt_ShopFloorSummary | rpt_ShopFloorSummary | 思方云2 ERP | 0 |
| 625 | rpt_StepMapping | rpt_StepMapping | 思方云2 ERP | 0 |
| 626 | rpt_targetInfo | rpt_targetInfo | 思方云2 ERP | 0 |
| 627 | scts.contractItemId=scti.recId | 来自工厂默认等于1，筛掉海外数据 | 思方云2 ERP | 0 |
| 628 | VPartArea | 面积表 | 思方云2 ERP | 0 |
| 629 | W_DailyStepWipOutPut | W_DailyStepWipOutPut | 思方云2 ERP | 0 |
| 630 | W_WIP | W_WIP | 思方云2 ERP | 0 |
| 631 | W_WIPFieldDisplay | W_WIPFieldDisplay | 思方云2 ERP | 0 |
| 632 | W_WIPQueryExecute | W_WIPQueryExecute | 思方云2 ERP | 0 |
| 633 | W_WIPStepDetails | W_WIPStepDetails | 思方云2 ERP | 0 |
| 634 | WIP_Backlog | 月结主表 | 思方云2 ERP | 0 |
| 635 | WIP_PC | WIP_PC | 思方云2 ERP | 0 |
| 636 | WIP_PCSteps | WIP_PCSteps | 思方云2 ERP | 0 |
| 637 | WIP_PCWO | WIP_PCWO | 思方云2 ERP | 0 |
| 638 | wo_Rework$ | wo_Rework$ | 思方云2 ERP | 0 |
| 639 | xnh_BOMBatch | xnh_BOMBatch | 思方云2 ERP | 0 |
| 640 | xnh_BOMBatch2 | xnh_BOMBatch2 | 思方云2 ERP | 0 |
| 641 | xnh_ChangedtobePlaned | xnh_ChangedtobePlaned | 思方云2 ERP | 0 |
| 642 | xnh_DeletedLock | xnh_DeletedLock | 思方云2 ERP | 0 |
| 643 | xnh_fgi_stockForm | 成品入库 | 思方云2 ERP | 0 |
| 644 | xnh_fgi_stockFormItem | 成品入库明细 | 思方云2 ERP | 0 |
| 645 | xnh_fgi_stockformitemwo | xnh_fgi_stockformitemwo | 思方云2 ERP | 0 |
| 646 | xnh_last3setp | xnh_last3setp | 思方云2 ERP | 0 |
| 647 | xnh_OrderDateChanged | xnh_OrderDateChanged | 思方云2 ERP | 0 |
| 648 | xnh_orphanPart | xnh_orphanPart | 思方云2 ERP | 0 |
| 649 | xnh_OSMORoute | xnh_OSMORoute | 思方云2 ERP | 0 |
| 650 | xnh_qtyshipped | xnh_qtyshipped | 思方云2 ERP | 0 |
| 651 | xnh_resetPlanningedQty | xnh_resetPlanningedQty | 思方云2 ERP | 0 |
| 652 | xnh_stockedIn | xnh_stockedIn | 思方云2 ERP | 0 |
| 653 | xnh_wipBalance | xnh_wipBalance | 思方云2 ERP | 0 |
| 654 | xnh_wo | xnh_wo | 思方云2 ERP | 0 |
| 655 | xnh_wotemp | xnh_wotemp | 思方云2 ERP | 0 |
| 656 | xnh_woTempQty | xnh_woTempQty | 思方云2 ERP | 0 |
| 657 | zb_materials | zb_materials | 思方云2 ERP | 0 |
| 658 | · | set数量 | 思方云2 ERP | 13 |
| 659 | 不需要接收 | 不需要接收 | 思方云2 ERP | 17 |
| 660 | 主工单.moId=子工单.moId | 工厂 | 思方云2 ERP | 0 |
| 661 | 供应商 | 采购受理 | 思方云2 ERP | 0 |
| 662 | 化验 | 化验 | 思方云2 ERP | 0 |
| 663 | 可入库数量-MO需求数量 | MO已分配数量 | 思方云2 ERP | 2 |
| 664 | 可分配数量=库存数量+可入库数量 | 可分配数量=库存数量+可入库数量 | 思方云2 ERP | 0 |
| 665 | 可用数量=库存数量+ | 可用数量=库存数量+ | 思方云2 ERP | 0 |
| 666 | 在途可分配数=请购数+采购数 | 请购数量 | 思方云2 ERP | 6 |
| 667 | 工单对应的制造部件号 | 制造部件 | 思方云2 ERP | 0 |
| 668 | 工单有主卡和子卡 | 制造单表 | 思方云2 ERP | 0 |
| 669 | 空数据 | 下一个工序 | 思方云2 ERP | 30 |
| 670 | 补货，投诉， | 补货，投诉， | 思方云2 ERP | 0 |
| 671 | 退货，换货，返修（新出单） | 退货，换货，返修（新出单） | 思方云2 ERP | 0 |
| 672 | 需要接收（成品接收客户类型） | 审批通过时间 | 思方云2 ERP | 1 |

---
