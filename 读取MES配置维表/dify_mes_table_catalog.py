# -*- coding: utf-8 -*-
# 【Dify 代码节点专用 · 由 build_mes_catalog_bundle.py 自动生成，请勿手改】
# 维护：改 中络项目MES 系统表名清单V1.2.md → python3 build_mes_catalog_bundle.py → 复制到 Dify
#
# 通用加速：按用户问题对全表清单做相关性排序，仅 Top-N 送入「分析业务表」LLM（无业务硬编码）。
# 版本：DIFY_CATALOG_NODE_VERSION=4
#
# 入参：user_question（接 {{#sys.query#}}）
# 出参（均为 string）：
#   table_catalog — 排序后的候选清单（接到分析业务表 LLM，替代全量 177 张表）
#   table_count   — 候选表数量
#   char_count    — 候选清单字符数
#   rank_mode     — ranked | full
#   char_count_full — 全量精简清单字符数（排查用）

_EMBEDDED_CATALOG_SLIM = "# MES 表清单（精简·选表用，仅表名+业务含义）\n# 格式：TBL_XXX | 中文表名 | 业务含义\n\nTBL_SYS_DICTIONARY | 数据字典 | 描述了大部分字符串常量对应的中文含义\nTBL_SYS_ORGANIZATION | 组织机构表 | 描述系统中包含的组织信息\nTBL_SYS_PARAM | 系统参数配置表 | 描述系统中各种基础运行插件参数\nTBL_SYS_PARAM_TYPE | 系统参数分类表 | 描述系统参数的分类类型\nTBL_SYS_ROLE | 系统角色表 | 描述系统用户角色列表\nTBL_SYS_SERVER | 系统服务配置表 | 描述系统各服务配置信息\nTBL_SYS_TEMPLATE_CONFIG | 系统模板配置表 | 描述系统配置文件模板功能的相关数据\nTBL_SYS_USER | 系统用户表 | 描述所有的系统用户信息\nTBL_SYS_USER_ORG_MAP | 用户组织关系 | 描述了用户与组织关联的信息\nTBL_SYS_USER_ROLE_MAP | 用户角色关系表 | 描述了用户与角色关联的信息\nTBL_BD_CUSTOMER | 客户信息表 | 维护工厂的所有的客户信息，包括客户编号和客户名称等\nTBL_BD_ITEM | 产品和物料信息表 | 包含了工厂中所有生产产品、原材料物料的信息，信息从ERP系统同步而来\nTBL_BD_ITEM_TYPE | 产品和物料类型表 | 描述了TBL_BD_ITEM表中的生产产品、物料可对应的类型\nTBL_BD_PROCESS | 工序工艺信息表 | 包含了工厂中的所有的生产工序信息\nTBL_BD_PROCESS_OUTS | 外协产品工序表 | 包含了需要外协的生产产品与其外协工序的关联关系\nTBL_BD_RULE | 编码规则定义表 | 包含了在MES系统中维护的编码规则列表\nTBL_BD_SUPPLIER | 供应商信息表 | 包含了在MES系统中维护的物料供应商、设备供应商信息列表\nTBL_BD_TEMPLATE | 模板信息表 | 包含MES系统中维护的可打印的标签的模板配置信息\nTBL_BD_TEMPLATE_GROUP | 模板分组表 | 包含MES系统中维护的可打印的标签的模板的组别信息\nTBL_BD_WC | 工作中心表 | 包含MES系统中维护的工作中心信息，包括生产设备、环境设备、测试设备等\nTBL_BD_WC_ITEMTYPE_LINK | 工作中心与物料类别关联 | 描述了哪些类型的物料可与哪个工作中心进行关联，关联信息用于后续物料防错逻辑\nTBL_BD_WC_PROCESS_LINK | 工作中心与工序关系表 | 描述了哪些工序与哪个工作中心进行关联\nTBL_MD_DATASET | 数据集 | 包含MES系统中维护的数据集信息，可用于后续配置表单页面、配置打印数据等\nTBL_MSG_EVENT | 消息事件表 | 包含了需要推送的特定消息具体事件描述\nTBL_MSG_GROUP | 消息群组 | 包含了消息推送程序可推送的群组，推送事件以群组为单位\nTBL_MSG_GROUP_USER | 消息群组和用户 | 包含了推送群组与MES系统用户之间的关联关系\nTBL_MSG_PUSH_FREQUENCY | 预警频率配置表 | 描述消息推送事件的推送频率的配置信息\nTBL_MSG_SEND_LOG | 消息发送日志表 | 包含了消息推送事件发送的日志记录信息\nTBL_MSG_USER | 消息推送用户 | 包含了MES系统用户与企业微信账号的对应关系\nTBL_EAP_ALARM | 设备报警记录 | 包含了在边缘网关中联机的设备的所有的报警信息\nTBL_EAP_AOI_DETECTIONS | AOI或者VRS数据主表 | 包含了AOI设备和VRS设备的检测数据主体信息\nTBL_EAP_AOI_DETECTIONS_DTL | AOI或VRS数据明细表 | 包含了AOI设备和VRS设备的检测数据明细信息\nTBL_EAP_API_RECORDS | 联机API调用记录 | 包含所有通过WebAPI进行联机的设备的接口调用日志\nTBL_EAP_AUTO_PULL_MACHINE | 放板机状态监控表 | 描述每台放板机的实时状态，状态信息每两分钟更新一次\nTBL_EAP_BT_PARAM | 班通参数主表 | 描述了班通线宽测量仪的下发配方参数主表信息\nTBL_EAP_BT_PARAM_DTL | 班通参数明细表 | 描述了班通线宽测量仪的下发配方参数具体项目信息\nTBL_EAP_CURRENT_DATA | 联机测点TAG实时状态表 | 包含了在边缘网关中联机的设备的所配置的测点的实时采集数值\nTBL_EAP_DATA_YYYYMM | 联机数据测点采集信息表(分表) | 包含了在边缘网关中联机的设备的所配置的测点的历史采集数值\nTBL_EAP_DEVICE | 联机设备列表 | 包含了在边缘网关中联机的设备主体信息\nTBL_EAP_GE_PARAM | 今明图电参数 | 包含今明图电生产参数下发配方的配置信息\nTBL_EAP_GE_PARAM_CHANGE_LOG | 图电参数变更记录表 | 包含今明图电生产参数下发配方信息的变更记录\nTBL_EAP_GE_PARAM_USE_LOG | 图电参数下发记录 | 包含今明图电生产参数下发配方的下发记录\nTBL_EAP_GOLD_NICKEL_TESTER_RECORD | 金镍测试仪上传数据主表，沉金 | 包含金镍测试仪上传的沉金部分的测试主体数据\nTBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL | 金镍测试仪上传数据明细表，沉金 | 包含金镍测试仪上传的沉金部分的测试项目明细数据\nTBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN | 金镍测试仪主表，沉锡 | 包含金镍测试仪上传的沉锡部分的测试主体数据\nTBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL | 金镍测试仪明细表，沉锡 | 包含金镍测试仪上传的沉锡部分的测试项目明细数据\nTBL_EAP_HAOS_PARAM | 浩硕打靶机参数 | 包含浩硕打靶机生产参数下发配方的配置信息\nTBL_EAP_HEARTBEAT | 放板机心跳记录 | 包含每台放板机上传的心跳记录\nTBL_EAP_HONGSHENG_RECORDS | 宏胜裁磨机结批数据 | 宏胜裁磨机上传的生产数据主表\nTBL_EAP_HONGSHENG_TM_RECORDS | 宏胜测厚机测试数据 | 宏胜裁磨机上传的测试数据\nTBL_EAP_HQ_PRESS_PRODUCTION | 活全压机数据 | 活全压机的生产数据，由定时器从其它数据库定时采集更新\nTBL_EAP_LDI_LOG | LDI生产日志记录表 | 包含了LDI的生产记录数据\nTBL_EAP_LDI_PARAM | LDI参数 | 包含LDI生产参数下发配方的配置信息\nTBL_EAP_LWT_DETECTIONS | 班通检测主记录表 | 包含班通线宽测量仪上传的测量记录主体信息\nTBL_EAP_LWT_DETECTIONS_DTL | 班通检测明细记录表 | 包含班通线宽测量仪上传的测量记录项目明细信息\nTBL_EAP_MASON_DETECTIONS | 麦逊检测结果主表 | 包含麦逊设备上传的检测记录主体信息\nTBL_EAP_MASON_DETECTIONS_DTL | 麦逊检测结果明细表 | 包含麦逊设备上传的测量记录项目明细信息\nTBL_EAP_PATTERN_PLAT | 图形电镀检测主记录表 | 包含图形电镀设备上传的检测记录主体信息\nTBL_EAP_PATTERN_PLAT_ITEM | 图形电镀检测明细表 | 包含图形电镀设备上传的检测记录项目明细信息\nTBL_EAP_PERIOD | 设备状态时段记录表 | 记录每个设备的状态发生变化的开始时间到结束时间\nTBL_EAP_PMS_CONTENT | 汉印喷印机内容配置表 | 包含汉印喷印机的下发喷印内容的数据配置信息\nTBL_EAP_PMS_PROD | 汉印生产记录主表 | 包含汉印喷印机上传的生产记录主体信息\nTBL_EAP_PMS_PROD_DTL | 汉印生产记录明细表 | 包含汉印喷印机上传的生产记录项目明细信息\nTBL_EAP_SHUTDOWN_RECORD | 放板机关机记录表 | 包含所有放板机的掉线记录日志\nTBL_EAP_STATUS | 设备状态采集记录表 | 包含了在边缘网关中联机的设备的运行状态的实时采集数值\nTBL_EAP_TAG | 测点配置表 | 包含了在边缘网关中联机的设备的所有测点的配置信息\nTBL_EAP_THREE_D_DATA | 三次元数据 | 包含三次元设备上传的测量数据信息\nTBL_EAP_THREE_D_ITEM | 三次元数据明细 | 包含三次元设备上传的测量数据项目明细信息\nTBL_EAP_THREE_D_RECORD | 三次元文件记录主表 | 包含三次元设备上传的测量数据信息的日志\nTBL_EAP_TIME_RANGE_CONTROL | 放板机时间范围管控 | 描述了放板机的禁止运行时间的配置情况\nTBL_EAP_YUHUI_TEST_RECORDS | 誉汇测试记录主表 | 包含誉汇测试机设备上传的测试数据主体信息\nTBL_EAP_YUHUI_TEST_RECORDS_DTL | 誉汇测试记录明细表 | 包含誉汇测试机设备上传的测试数据项目明细信息\nTBL_ABNORMAL_DATA_POOL | 锁机锁卡异常数据表 | 包含触发锁机锁卡条件的异常数据，在进行确认后会进行删除\nTBL_PATTERN_HAOSHUO_PRODUCTION_RECORD | 浩硕图形电镀生产记录主表 | 包含浩硕图形电镀设备上传的生产记录主体信息\nTBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL | 浩硕图形电镀生产记录明细表 | 包含浩硕图形电镀设备上传的生产记录明细信息\nTBL_QM_ASSAY_LOG | 化验任务记录表 | 包含了由定时程序定时生成的药水化验任务\nTBL_QM_ASSAY_LOG_ITEM | 化验任务明细表 | 包含了由定时程序定时生成的药水化验任务的化验项目明细信息\nTBL_QM_CC_EXCEPTION | 客诉异常报告信息表 | 包含客户对产品质量问题投诉报告的信息\nTBL_QM_COMPLAINT | 品质投诉记录表 | 包含客户对产品质量问题投诉的记录\nTBL_QM_COMPLAINT_IMAGE | 品质投诉图片表 | 包含客户对产品质量问题投诉的记录的图片信息\nTBL_QM_INSPECT_RECORD | 检验记录主表 | 包含IPQC首件检验记录的主体信息列表\nTBL_QM_INSPECTION_RECORD_ITEM | 检验记录明细表 | 包含IPQC首件检验记录的明细项目信息\nTBL_QM_MEDICINE_TANK | 药缸信息表 | 包含药水化验缸体的配置信息\nTBL_QM_PL_LOG | 物理实验室送检记录主表 | 包含产品送检物理实验室的检验记录信息\nTBL_QM_PL_LOG_ITEM | 物理实验室送检记录明细表 | 包含产品送检物理实验室的检验记录的项目明细信息\nTBL_ESOP_CONTACT_FORM | 联络单信息表 | 包含了MES系统中维护的内部联络单列表信息\nTBL_ESOP_COUNTERSIGN | 4M文件会签信息表 | 包含了MES系统中维护的4M变更单的会签信息\nTBL_ESOP_FILE | ESOP文件主表 | 包含了MES系统中维护的相关文件信息\nTBL_ESOP_FILE_CATEGORY | ESOP文件目录表 | 描述了MES系统中维护的文件的目录信息\nTBL_ESOP_FILE_SIGN | 文件手写体信息 | 包含某些文件会签时需要用到的手写体信息\nTBL_ESOP_FILE_TYPE | ESOP文件类型表 | 定义了所有上传的文件可能对应的文件类型信息\nTBL_ESOP_TEMPORARY_CHANGE_ORDER | 4M临时变更单 | 包含4M临时变更单的列表，在物料防错时需要校验订单号对应的变更情况\nTBL_FOURM_CHANGE_ITEM_LOG | 4M变更料号日志表 | 包含4M临时变更单的详细板料变更信息，即变更前板料和变更后板料\nTBL_EAM_PM_TEMP_WC_LINK | 模板关联工作中心 | 描述了设备点检或设备保养模板与工作中心的关联关系\nTBL_NP_TEMPLATE | 模板主表 | 包含所有的设备点检和设备保养模板信息\nTBL_NP_TEMPLATE_CHANGE | 模板变更主表 | 描述设备点检模板或设备保养模板的变更情况\nTBL_NP_TEMPLATE_CHANGE_ITEM | 模板变更明细表 | 描述设备点检模板或设备保养模板的项目明细的变更情况\nTBL_NP_TEMPLATE_ITEM | 模板项配置表 | 包含所有的设备点检和设备保养模板的详细项目信息\nTBL_EAM_ERROR_CODE | 设备故障代码表 | 描述了设备的各种故障情况的代码以及说明\nTBL_EAM_FREQUENCY | 设备保养频次配置表 | 描述了设备点检或设备保养的任务频率常量信息\nTBL_EAM_MAINTAIN_TASK | 保养任务主表 | 包含了由定时程序定时生成的设备保养任务\nTBL_EAM_MAINTAIN_TASK_CHANGE_LOG | 保养任务时间变更日志表 | 包含了更改保养任务时间的操作日志\nTBL_EAM_MAINTAIN_TASK_ITEM | 保养任务明细表 | 包含了由定时程序定时生成的设备保养任务的项目明细\nTBL_EAM_MAINTAIN_TASK_ITEM_IMG | 保养任务明细图片表 | 包含了提交设备保养结果时附带的图片信息\nTBL_EAM_REPAIR | 维修工单主表 | 包含了设备维修的记录信息\nTBL_EAM_REPAIR_IMG | 维修图片记录表 | 包含了提交设备维修结果时附带的图片信息\nTBL_EAM_REPAIR_MAN | 指派人员列表 | 描述了维修可指派的人员的列表信息\nTBL_EAM_REPAIR_MATERIAL | 维修耗材记录表 | 包含提交设备维修结果时报告的耗材信息\nTBL_SFC_DBFC_USER | 叠板防错用户 | 维护系统用户和指定设备的绑定关系\nTBL_SFC_PACKAGE | 包装信息表 | 包含包装工序中所有的内包和外包信息\nTBL_SFC_PACKAGE_LABEL_LINK | 包装模板与物料/客户关联表 | 描述了包装模板与物料、客户的绑定关系\nTBL_SFC_PACKAGE_LOG | 包装操作日志表 | 包含包装条码的操作日志\nTBL_SFC_PACKAGE_RULE | 包装规则主表 | 包含了所有指定客户的包装规格的信息\nTBL_SFC_PACKAGE_RULE_EXT | 包装规则扩展配置表 | 包含了所有指定客户的包装规格的扩展配置信息\nTBL_SFC_PACKAGE_RULE_LINK | 包装规则与物料/客户关联表 | 描述了包装规则与物料或客户的关联关系\nTBL_SFC_RECIPE_LOT | 不合格工单配方信息表 | 包含VCP电镀工序的参数配方的信息\nTBL_SFC_RECIPE_LOT_LINK | 不合格工单配方项目明细表 | 包含VCP电镀工序的参数配方的详细项目信息\nTBL_SFC_RECIPE_PRODUCT | 按产品维度的配方信息主表 | 包含VCP电镀工序的以产品为单位的参数配方的信息\nTBL_SFC_RECIPE_PRODUCT_LINK | 产品配方项目明细表 | 包含VCP电镀工序的以产品为单位的参数配方的详细项目信息\nTBL_SFC_WS_LOG | 生产记录表 | 以工序为单位记录某张工单在某个设备上的生产记录信息\nTBL_SFC_WS_LOG_ITEM | 生产记录项目明细 | 记录某条生产记录中包含的详细生产相关参数值信息\nTBL_SFC_WS_TEMPLATE_CONFIG | 工位报工模板配置表 | 记录了关于生产记录模板的配置信息\nTBL_SFC_WS_TEMPLATE_LINK | 工作中心与模板关联配置表 | 记录了工作中心与生产记录模板关联的信息\nTBL_MO | 工单信息表 | 记录了所有工单的相关信息\nTBL_MO_OUTS | 外协工单信息表 | 记录了外协工单的相关信息\nTBL_OUTSOURCE_SHIFT_EMPLOYEE | 外协班次员工配置表 | 包含外协工序对应员工和班次的配置信息\nTBL_WMS_ITEM_BARCODE | 物料条码表 | 包含物料供应商在MES系统中打印的物料条码列表\nTBL_WMS_ITEM_PACKING_BARCODE | 物料包装条码表 | 包含物料供应商在MES系统中打印的包装箱条码列表\nTBL_WMS_LINE_RECORD | 线别仓操作记录 | 包含线边仓中的物料的操作记录信息\nTBL_WMS_LOCATION | 仓库货位 | 包含仓库货位与仓库的关联关系信息\nTBL_WMS_MANTISSA_RECORD | 尾数仓操作记录 | 包含尾数仓中的物料的操作记录信息\nTBL_WMS_PICKING_LOG | MES领料记录 | 包含MES系统中的领料记录(与ERP领料记录不同)\nTBL_WMS_PICKING_LOG_DTL | 领料记录明细 | 包含MES系统中的领料记录明细信息(与ERP领料记录不同)\nTBL_WMS_WAREHOUSE | 仓库主数据表 | 包含了仓库列表信息\nTBL_WMS_WAREHOUSE_TYPE | 仓库类型 | 包含了仓库类型信息\nTBL_WMS_AREA | 仓库区域 | 包含了仓库所属区域的信息\nTBL_WMS_BARCODE_SPLIT_RECORD | 条码拆分记录表 | 记录了物料条码的拆分记录信息\nTBL_WMS_PRINT_LOG | 仓库物料标签打印日志表 | 记录了仓库根据库存打印的物料条码的日志信息\nTBL_WMS_STOCK_BARCODE_LINK | ERP库存与打印条码关联表 | 记录ERP库存物料与打印的物料条码的关联关系\nTBL_SRM_PO | 采购单 | 包含从ERP系统同步到MES系统的采购单信息\nTBL_SRM_PO_DELIVERY | 采购订单交付表 | 包含已交付的采购单信息\nTBL_SRM_PO_DETAIL | 采购订单明细 | 包含从ERP系统同步到MES系统的采购单明细信息\nTBL_SRM_RECEIVING | 收货单主表 | 包含从ERP系统同步到MES系统的收货单信息\nTBL_SRM_RECEIVING_BARCODE | 收货单条码关联表 | 包含收获单明细与对应物料条码的关联信息\nTBL_SRM_RECEIVING_DTL | 收货单明细表 | 包含从ERP系统同步到MES系统的收货单明细信息\nTBL_SHEET_LINK_PP | 供应商替代关联表 | 描述了物料供应商之间的可替代关系\nTBL_MO_BARCODE_PROD_LINK | 工单与条码生产关联表 | 包含工单与条码在工序生产时的关联绑定信息\nTBL_SPC_CONTROL_CHARACTERISTIC | SPC管控特性主表 | 描述了各工序的SPC管控配置相关信息\nTBL_SPC_CONTROL_CHARACTERISTIC_ITEM_LINK | SPC管控特性与对象关联表 | 描述SPC具体管控配置与产品料号关联关系\nTBL_SPC_CONTROL_CHARACTERISTIC_LIMIT | SPC管控特性控制限配置表 | 描述了SPC管控配置相关控制限信息\nTBL_SPC_CONTROL_CHARACTERISTIC_RULE_LINK | SPC管控特性与判异规则关联表 | 描述SPC具体管控配置与判异规则的关联关系\nTBL_SPC_DATA_REAL | SPC实时采样数据表 | 包含了每个进行SPC管控的产品料号的采样数据\nTBL_SPC_RULE_OF_DISSENT | SPC判异规则定义表 | 描述具体的SPC判异规则\nTBL_OQC_SHIPMENT_GENERATE | 出货报告生成 | 包含已经生成的出货报告的生成过程的相关信息\nTBL_OQC_SHIPMENT_GENERATE_LOG | 出货报告生成记录 | 包含生成出货报告的日志信息\nTBL_OQC_SHIPMENT_ITEM_LINK | 出货报告料号关联表 | 描述了出货报告与产品料号的关联信息\nTBL_OQC_SHIPMENT_REPORT | 出货报告表 | 包含所有的出货报告列表\nTBL_OQC_SHIPMENT_REPORT_TYPE | 出货报告类型表 | 描述了出货报告的类型信息\nTBL_PM_TEMPLATE_LINK_DEVICE | 模板与工作中心关联采集设备 | 描述设备点检模板与工作中心和设备信息关联信息\nTBL_SJSKDATA_YYYYMM | 锁机锁卡读码记录表 | 以分表的形式描述了每个月的锁机锁卡模块的读码记录\nTBL_SJSKEQPINFO | 读码设备实时工单信息表 | 描述每个锁机锁卡设备实时状态信息\nTBL_EAP_ALARM_CONTROL_LINK | 设备报警项关联配置表 | 包含了每个锁机锁卡设备需要关联的报警TAG配置信息\nTBL_EAP_ITEM_CONTROL_LINK | 设备关联料号 | 包含了每个锁机锁卡设备需要关联的可放行料号的配置信息\nTBL_EAP_POTION_ITEM_CONTROL_LINK | 设备关联药水化验项目 | 包含了每个锁机锁卡设备需要关联的药水化验项目的配置信息\nTBL_EAP_PRODUCE_CONTROL_DEVICE | 生产管控设备配置表 | 描述了每个需要管控的锁机锁卡设备配置信息\nTBL_FA_TXDD_KTHD | 图形电镀孔铜厚度测量 | 包含图形电镀各个孔铜测量点的厚度测量信息\nTBL_FA_TXDD_MAIN | 图像电镀FA信息主表 | 包含图形电镀FA主表相关信息\nTBL_FA_TXDD_QPBT | 图形电镀切片表铜 | 包含图形电镀切片表铜测量点的测量信息\nTBL_FA_TXDD_SKKJ | 图形电镀蚀刻后孔径测量 | 包含图形电镀蚀刻后各孔径测量点的测量信息\nTBL_FA_TXDD_SKXK | 图形电镀蚀刻后线宽 | 包含图形电镀蚀刻后线宽测量点的测量信息\nTBL_FA_TXDD_XHCL | 图形电镀锡厚测量 | 包含图形电镀锡厚测量点的测量信息\nTBL_FA_TXDD_ZKCS | 图形电镀阻抗测试 | 包含图形电镀阻抗测量点的测量信息\nTBL_FA_YHYJ_MAIN | 压合压机 | 包含压合工序FA主表相关信息\nTBL_FA_YHYJ_MI | 压合压机MI实测 | 包含压机实际测量数据\nTBL_MEP_MATERIAL_PARAM | 重点物料参数维护 | 包含重点产品料号和历史异常料号的相关参数维护信息"
_EMBEDDED_CATALOG_FULL_CHAR_COUNT = "67434"
_EMBEDDED_TABLE_COUNT = "175"

# -*- coding: utf-8 -*-
"""通用表清单相关性排序：按用户问题对精简 catalog 行打分，缩小 LLM 选表范围。"""

import re
from typing import Dict, List, Set, Tuple

_CJK_RUN = re.compile(r"[\u4e00-\u9fff]+")
_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+")
_TABLE_LINE = re.compile(r"^(TBL_\w+|VW_\w+|VM_\w+|VIEW_\w+|ERP_\w+)\s*\|")

_SFC_PRODUCTION_KW = ("生产记录", "报工", "过站", "产出")
_PROCESS_KW = ("工序",)


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


def _apply_intent_boosts(question: str, scored: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """按问题意图调整分数：生产记录类问题优先 SFC 报工表，弱化仅设备日志命中「生产记录」的表。"""
    q = question or ""
    if not any(k in q for k in _SFC_PRODUCTION_KW):
        return scored

    boosted: List[Tuple[int, str]] = []
    process_boost = any(k in q for k in _PROCESS_KW)
    for s, ln in scored:
        tname, label, biz = _parse_line(ln)
        if any(k in q for k in _SFC_PRODUCTION_KW):
            if tname == "TBL_SFC_WS_LOG":
                s += 300
            elif tname == "TBL_SFC_WS_LOG_ITEM":
                s += 200
            elif tname.startswith("TBL_SFC_WS_"):
                s += 80
            elif "生产记录" in label:
                s += 60
            elif "生产记录" in biz and tname.startswith(("TBL_EAP_", "TBL_PATTERN_")):
                s -= 150
        if process_boost and tname == "TBL_BD_PROCESS":
            s += 80
        boosted.append((s, ln))

    boosted.sort(key=lambda x: (-x[0], x[1]))
    return boosted


def _infer_related_tables(tname: str, all_names: Set[str]) -> List[str]:
    """主表/主记录选中时，补全常见子表（MAIN→MI、LOG→LOG_ITEM 等）。"""
    related: List[str] = []
    if tname.endswith("_MAIN"):
        mi = tname[:-5] + "_MI"
        if mi in all_names:
            related.append(mi)
    item = tname + "_ITEM"
    if item in all_names:
        related.append(item)
    if tname.endswith("_REPAIR"):
        for suffix in ("_IMG", "_MATERIAL"):
            cand = tname + suffix
            if cand in all_names:
                related.append(cand)
    return related


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
    top_n: int = 35,
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
    picked = picked[: top_n + 5]

    body = [ln for _, ln in picked]
    ranked = "\n".join(header + [""] + body).strip()
    return ranked, len(body), "ranked"

def main(user_question="", **kwargs):
    """Dify 入口：嵌入清单 + 通用相关性排序，不读磁盘。"""
    q = str(user_question or kwargs.get("user_question") or kwargs.get("query") or "").strip()
    full_slim = _EMBEDDED_CATALOG_SLIM
    ranked, n_ranked, mode = rank_catalog_lines(q, full_slim, top_n=35, min_score=10)
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
