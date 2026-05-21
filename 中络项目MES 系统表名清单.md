# MES系统数据字典（精简版）

## 一、系统信息

### 1. TBL_SYS_DICTIONARY（数据字典）
- **业务含义**：存储系统数据字典，用于维护下拉选项、枚举值等基础数据。
- **关联关系**：
  - TBL_SYS_DICTIONARY.CPARENT_DIC_ID = TBL_SYS_DICTIONARY.CID


----------------------

### 2. TBL_SYS_ORGANIZATION（组织机构表）
- **业务含义**：组织机构表，存储公司、部门、车间等组织架构信息。
- **关联关系**：
  - TBL_SYS_ORGANIZATION.CPARENT_ORG_ID = TBL_SYS_ORGANIZATION.CID

----------------------

### 3. TBL_SYS_PARAM（系统参数配置表）
- **业务含义**：系统参数配置表，存储系统运行所需的各类参数配置。
- **关联关系**：
  - TBL_SYS_PARAM.CPARAM_TYPE = TBL_SYS_PARAM_TYPE.CID

----------------------

### 4. TBL_SYS_PARAM_TYPE（系统参数分类表）
- **业务含义**：系统参数分类表，对系统参数进行分类管理。
- **关联关系**：
  - TBL_SYS_PARAM_TYPE.CPARENT_ID = TBL_SYS_PARAM_TYPE.CID

----------------------

### 5. TBL_SYS_ROLE（系统角色表）
- **业务含义**：系统角色表，定义用户角色。
- **关联关系**：无

----------------------

### 6. TBL_SYS_SERVER（系统服务配置表）
- **业务含义**：系统服务配置表，存储各服务连接配置。
- **关联关系**：无

----------------------

### 7. TBL_SYS_TEMPLATE_CONFIG（系统模板配置表）
- **业务含义**：系统模板配置表，存储Excel导出/打印模板配置。
- **关联关系**：无

----------------------

### 8. TBL_SYS_USER（系统用户表）
- **业务含义**：系统用户表，存储登录用户账号信息。
- **关联关系**：
  - TBL_SYS_USER.CORG_CODE = TBL_SYS_ORGANIZATION.CORG_NO
  - TBL_SYS_USER.CID = TBL_SYS_USER_ORG_MAP.CUSER_ID
  - TBL_SYS_USER.CID = TBL_SYS_USER_ROLE_MAP.CUSER_ID

----------------------

### 9. TBL_SYS_USER_ORG_MAP（用户组织关系）
- **业务含义**：用户与组织关联表，记录用户所属组织及默认组织。
- **关联关系**：
  - TBL_SYS_USER_ORG_MAP.CUSER_ID = TBL_SYS_USER.CID
  - TBL_SYS_USER_ORG_MAP.CORG_ID = TBL_SYS_ORGANIZATION.CID

----------------------

### 10. TBL_SYS_USER_ROLE_MAP（用户角色关系表）
- **业务含义**：用户与角色关联表，记录用户分配的角色。
- **关联关系**：
  - TBL_SYS_USER_ROLE_MAP.CUSER_ID = TBL_SYS_USER.CID
  - TBL_SYS_USER_ROLE_MAP.CROLE_ID = TBL_SYS_ROLE.CID

---

## 二、基础数据

----------------------

### 11. TBL_BD_CUSTOMER（客户信息表）
- **业务含义**：客户主数据表，存储客户基本信息。
- **关联关系**：无

----------------------

### 12. TBL_BD_DEVICE_STATUS（采集设备实时状态表）
- **业务含义**：采集设备实时状态表（疑似弃用），记录设备状态。
- **关联关系**：无

----------------------

### 13. TBL_BD_GROUP（组别）
- **业务含义**：组别主表，定义各类业务组。
- **关联关系**：无

----------------------

### 14. TBL_BD_GROUP_MEMBERS（组员）
- **业务含义**：组员信息表，存储组员基本信息。
- **关联关系**：无

----------------------

### 15. TBL_BD_GROUP_MEMBERS_LINK（组别与成员关系映射表）
- **业务含义**：组别与成员关联表，建立组和用户的多对多关系。
- **关联关系**：
  - TBL_BD_GROUP_MEMBERS_LINK.GROUP_ID = TBL_BD_GROUP.CID
  - TBL_BD_GROUP_MEMBERS_LINK.USER_ID = TBL_SYS_USER.CID

----------------------

### 16. TBL_BD_ITEM（产品和物料信息表）
- **业务含义**：产品和物料主数据表，存储料号、规格、客户物料信息等。
- **关联关系**：
  - TBL_BD_ITEM.CITEM_TYPE_ID = TBL_BD_ITEM_TYPE.CID
  - TBL_BD_ITEM.CUSTOMER_CODE = TBL_BD_CUSTOMER.CUSTOMER_NO

----------------------

### 17. TBL_BD_ITEM_A（产品属性）
- **业务含义**：产品属性定义表，存储属性键值对模板。
- **关联关系**：无

----------------------

### 18. TBL_BD_ITEM_ATTR（产品属性）
- **业务含义**：产品属性值表，存储具体物料的实际属性值。
- **关联关系**：
  - TBL_BD_ITEM_ATTR.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 19. TBL_BD_ITEM_INSPECTION_STANDARD（物料检验标准配置表）
- **业务含义**：物料检验标准配置表，定义各工序的检验标准。
- **关联关系**：
  - TBL_BD_ITEM_INSPECTION_STANDARD.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_BD_ITEM_INSPECTION_STANDARD.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 20. TBL_BD_ITEM_TYPE（产品和物料类型表）
- **业务含义**：物料类型定义表，支持树形分类。
- **关联关系**：
  - TBL_BD_ITEM_TYPE.CPARENT_TYPE_ID = TBL_BD_ITEM_TYPE.CID

----------------------

### 21. TBL_BD_PROCESS（工序工艺信息表）
- **业务含义**：工序主数据表，定义生产工艺路线中的各工序。
- **关联关系**：
  - TBL_BD_PROCESS.CPARENT_PROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 22. TBL_BD_PROCESS_OUTS（外协产品工序表）
- **业务含义**：外协产品工序定义表，存储外协工序信息。
- **关联关系**：
  - TBL_BD_PROCESS_OUTS.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 23. TBL_BD_REGEX（正则校验规则表）
- **业务含义**：正则校验规则表，存储输入校验规则。
- **关联关系**：无

----------------------

### 24. TBL_BD_RULE（编码规则定义表）
- **业务含义**：编码规则定义表，定义各类业务单据编号规则。
- **关联关系**：无

----------------------

### 25. TBL_BD_SUPPLIER（供应商信息表）
- **业务含义**：供应商主数据表，存储供应商基本信息。
- **关联关系**：无

----------------------

### 26. TBL_BD_TEMPLATE（模板信息表）
- **业务含义**：模板信息表，存储各类业务模板。
- **关联关系**：无

----------------------

### 27. TBL_BD_TEMPLATE_GROUP（模板分组表）
- **业务含义**：模板分组表，对模板进行分类。
- **关联关系**：无

----------------------

### 28. TBL_BD_WC（工作中心表）
- **业务含义**：工作中心主数据表，定义生产线、机台等生产单元。
- **关联关系**：
  - TBL_BD_WC.CPARENT = TBL_BD_WC.CID

----------------------

### 29. TBL_BD_WC_ITEMTYPE_LINK（工作中心关联模板）
- **业务含义**：工作中心与物料类型关联表。
- **关联关系**：
  - TBL_BD_WC_ITEMTYPE_LINK.CWC_ID = TBL_BD_WC.CID
  - TBL_BD_WC_ITEMTYPE_LINK.CITEM_TYPE_ID = TBL_BD_ITEM_TYPE.CID

----------------------

### 30. TBL_BD_WC_PROCESS_LINK（工作中心与工序关系表）
- **业务含义**：工作中心与工序关联表，定义工作中心可执行的工序。
- **关联关系**：
  - TBL_BD_WC_PROCESS_LINK.CWC_ID = TBL_BD_WC.CID
  - TBL_BD_WC_PROCESS_LINK.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 31. TBL_MD_DATASET（数据集）
- **业务含义**：数据集定义表，配置报表/模板的数据来源。
- **关联关系**：无

---

## 三、消息推送

----------------------

### 32. TBL_MSG_EVENT（消息事件表）
- **业务含义**：消息事件配置表，定义触发消息推送的条件和规则。
- **关联关系**：
  - TBL_MSG_EVENT.CMSG_GROUP_ID = TBL_MSG_GROUP.CID
  - TBL_MSG_EVENT.CTEMPLATE_ID = TBL_MSG_TEMPLATE.CID

----------------------

### 33. TBL_MSG_GROUP（消息群组）
- **业务含义**：消息群组表，定义接收消息的群组。
- **关联关系**：无

----------------------

### 34. TBL_MSG_GROUP_USER（消息群组和用户）
- **业务含义**：消息群组与用户关联表。
- **关联关系**：
  - TBL_MSG_GROUP_USER.CGROUP_ID = TBL_MSG_GROUP.CID
  - TBL_MSG_GROUP_USER.CUSER_ID = TBL_SYS_USER.CID

----------------------

### 35. TBL_MSG_PUSH_FREQUENCY（预警频率配置表）
- **业务含义**：消息推送频率配置表，使用Cron表达式定义推送周期。
- **关联关系**：无

----------------------

### 36. TBL_MSG_ROBOT（推送机器人）
- **业务含义**：消息机器人配置表，存储第三方机器人Webhook信息。
- **关联关系**：无

----------------------

### 37. TBL_MSG_ROBOT_EVENT_LINK（推送事件机器人关联）
- **业务含义**：消息事件与机器人关联表。
- **关联关系**：
  - TBL_MSG_ROBOT_EVENT_LINK.CMSG_EVENT_ID = TBL_MSG_EVENT.CID
  - TBL_MSG_ROBOT_EVENT_LINK.CROBOT_ID = TBL_MSG_ROBOT.CID

----------------------

### 38. TBL_MSG_SEND_LOG（消息发送日志表）
- **业务含义**：消息发送日志表，记录所有消息推送历史。
- **关联关系**：无

----------------------

### 39. TBL_MSG_TEMPLATE（消息模板）
- **业务含义**：消息模板表，定义推送消息的内容格式。
- **关联关系**：无

----------------------

### 40. TBL_MSG_USER（消息推送用户）
- **业务含义**：消息推送用户表，存储第三方消息平台用户信息。
- **关联关系**：
  - TBL_MSG_USER.CUSER_ID = TBL_SYS_USER.CID

---

## 四、设备联机

----------------------

### 41. TBL_EAP_ALARM（设备报警记录）
- **业务含义**：设备报警记录表，记录设备产生的报警信息。
- **关联关系**：
  - TBL_EAP_ALARM.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 42. TBL_EAP_AOI_DETECTIONS（AOI或者VRS数据主表）
- **业务含义**：AOI或VRS检测数据主表，记录自动光学检测结果。
- **关联关系**：
  - TBL_EAP_AOI_DETECTIONS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 43. TBL_EAP_AOI_DETECTIONS_DTL（AOI或VRS状态明细表）
- **业务含义**：AOI检测明细表，记录每个缺陷的详细信息。
- **关联关系**：
  - TBL_EAP_AOI_DETECTIONS_DTL.CDETECTION_ID = TBL_EAP_AOI_DETECTIONS.CID

----------------------

### 44. TBL_EAP_API_RECORDS（联机API调用记录）
- **业务含义**：设备联机API调用记录表，记录接口请求响应日志。
- **关联关系**：无

----------------------

### 45. TBL_EAP_AUTO_PULL_MACHINE（放板机状态监控表）
- **业务含义**：放板机状态监控表，每两分钟更新一次设备状态。
- **关联关系**：无

----------------------

### 46. TBL_EAP_BT_PARAM（班通参数主表）
- **业务含义**：班通设备参数主表，存储工艺参数。
- **关联关系**：无

----------------------

### 47. TBL_EAP_BT_PARAM_DTL（班通参数明细表）
- **业务含义**：班通设备参数明细表，存储具体参数项。
- **关联关系**：
  - TBL_EAP_BT_PARAM_DTL.CMAIN_ID = TBL_EAP_BT_PARAM.CID

----------------------

### 48. TBL_EAP_CURRENT_DATA（联机测点TAG实时状态表）
- **业务含义**：设备测点实时数据表，存储最新的采集值。
- **关联关系**：
  - TBL_EAP_CURRENT_DATA.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_CURRENT_DATA.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------

### 49. TBL_EAP_DATA（EAP采集数据表）
- **业务含义**：设备采集历史数据表，存储测点历史值。
- **关联关系**：
  - TBL_EAP_DATA.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_DATA.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------

### 50. TBL_EAP_DATA_CONTENT（EAP数据内容记录表）
- **业务含义**：EAP原始数据内容记录表，存储完整的报文数据。
- **关联关系**：无

----------------------

### 51. TBL_EAP_DATA_YYYYMM（联机数据测点采集信息表(分表)）
- **业务含义**：设备采集数据按月分表，存储历史数据。
- **关联关系**：无

----------------------

### 52. TBL_EAP_DEVICE（联机设备列表）
- **业务含义**：设备主数据表，存储所有联机设备信息。
- **关联关系**：无

----------------------

### 53. TBL_EAP_GE_PARAM（今明图电参数）
- **业务含义**：今明图电设备参数表，存储电镀工艺参数。
- **关联关系**：无

----------------------

### 54. TBL_EAP_GE_PARAM_CHANGE_LOG（图电参数变更记录表）
- **业务含义**：图电参数变更日志表，记录参数修改历史。
- **关联关系**：
  - TBL_EAP_GE_PARAM_CHANGE_LOG.CPARAMS_ID = TBL_EAP_GE_PARAM.CID

----------------------

### 55. TBL_EAP_GE_PARAM_USE_LOG（图电参数下发记录）
- **业务含义**：图电参数下发记录表，记录参数下发到机台的历史。
- **关联关系**：
  - TBL_EAP_GE_PARAM_USE_LOG.CPARAMS_ID = TBL_EAP_GE_PARAM.CID

----------------------

### 56. TBL_EAP_GOLD_NICKEL_TESTER_RECORD（金镍测试仪上传数据主表，沉金）
- **业务含义**：沉金工序金镍测试仪数据主表。
- **关联关系**：无

----------------------

### 57. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL（金镍测试仪上传数据明细表，沉金）
- **业务含义**：沉金工序金镍测试仪数据明细表。
- **关联关系**：
  - TBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL.CRECORD_ID = TBL_EAP_GOLD_NICKEL_TESTER_RECORD.CID

----------------------

### 58. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN（金镍测试仪主表，沉锡）
- **业务含义**：沉锡工序金镍测试仪数据主表。
- **关联关系**：无

----------------------

### 59. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL（金镍测试仪明细表，沉锡）
- **业务含义**：沉锡工序金镍测试仪数据明细表。
- **关联关系**：
  - TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL.CRECORD_ID = TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN.CID

----------------------

### 60. TBL_EAP_HAOS_PARAM（浩硕打靶机参数）
- **业务含义**：浩硕打靶机参数表，存储钻靶参数。
- **关联关系**：无

----------------------

### 61. TBL_EAP_HEARTBEAT（放板机心跳记录）
- **业务含义**：放板机心跳记录表，监控设备在线状态。
- **关联关系**：无

----------------------

### 62. TBL_EAP_HEARTBEATS（心跳记录表，疑似弃用）
- **业务含义**：设备心跳记录表（疑似弃用）。
- **关联关系**：
  - TBL_EAP_HEARTBEATS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 63. TBL_EAP_HONGSHENG_RECORDS（宏胜裁磨机结批数据）
- **业务含义**：宏胜裁磨机结批数据记录表。
- **关联关系**：
  - TBL_EAP_HONGSHENG_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 64. TBL_EAP_HONGSHENG_TM_RECORDS（宏胜测厚机测试数据）
- **业务含义**：宏胜测厚机铜厚/板厚测试数据表。
- **关联关系**：
  - TBL_EAP_HONGSHENG_TM_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 65. TBL_EAP_HQ_PRESS_PRODUCTION（活全压机数据）
- **业务含义**：活全压机生产数据表，每两分钟从MySQL采集。
- **关联关系**：无

----------------------

### 66. TBL_EAP_HQ_PRESS_PRODUCTION_ONSUBMIT（活全压机生成记录，手动提交）
- **业务含义**：活全压机手动提交的生产记录。
- **关联关系**：无

----------------------

### 67. TBL_EAP_LDI_JOB（LDI作业参数记录表）
- **业务含义**：LDI曝光机作业参数记录表。
- **关联关系**：无

----------------------

### 68. TBL_EAP_LDI_LOG（LDI生产日志记录表）
- **业务含义**：LDI曝光机生产日志记录表。
- **关联关系**：无

----------------------

### 69. TBL_EAP_LDI_PARAM（LDI参数）
- **业务含义**：LDI设备参数配置表。
- **关联关系**：无

----------------------

### 70. TBL_EAP_LWT_DETECTIONS（班通检测主记录表）
- **业务含义**：班通检测设备检测结果主表。
- **关联关系**：
  - TBL_EAP_LWT_DETECTIONS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 71. TBL_EAP_LWT_DETECTIONS_DTL（班通检测明细记录表）
- **业务含义**：班通检测设备检测结果明细表。
- **关联关系**：
  - TBL_EAP_LWT_DETECTIONS_DTL.CMAIN_ID = TBL_EAP_LWT_DETECTIONS.CID

----------------------

### 72. TBL_EAP_M_PARTOP（图电料号工艺参数表）
- **业务含义**：图电工序料号工艺参数表。
- **关联关系**：无

----------------------

### 73. TBL_EAP_MASON_DETECTIONS（麦逊检测结果主表）
- **业务含义**：麦逊检测设备检测结果主表。
- **关联关系**：无

----------------------

### 74. TBL_EAP_MASON_DETECTIONS_DTL（麦逊检测结果明细表）
- **业务含义**：麦逊检测设备检测结果明细表。
- **关联关系**：
  - TBL_EAP_MASON_DETECTIONS_DTL.CMAIN_ID = TBL_EAP_MASON_DETECTIONS.CID

----------------------

### 75. TBL_EAP_MP_GROUP（测点组）
- **业务含义**：设备测点分组表，将相关测点组合管理。
- **关联关系**：无

----------------------

### 76. TBL_EAP_MP_GROUP_DTL（测点组明细表）
- **业务含义**：测点组明细表，记录组内测点。
- **关联关系**：
  - TBL_EAP_MP_GROUP_DTL.CGROUP_ID = TBL_EAP_MP_GROUP.CID
  - TBL_EAP_MP_GROUP_DTL.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------

### 77. TBL_EAP_PATTERN_PLAT（图形电镀检测主记录表）
- **业务含义**：图形电镀检测结果主表。
- **关联关系**：无

----------------------

### 78. TBL_EAP_PATTERN_PLAT_ITEM（图形电镀检测明细表）
- **业务含义**：图形电镀检测结果明细表。
- **关联关系**：
  - TBL_EAP_PATTERN_PLAT_ITEM.CPATTERN_PLAT_ID = TBL_EAP_PATTERN_PLAT.CID

----------------------

### 79. TBL_EAP_PERIOD（设备状态时段记录表）
- **业务含义**：设备状态时段记录表，记录设备状态持续时间。
- **关联关系**：
  - TBL_EAP_PERIOD.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 80. TBL_EAP_PMS_CONTENT（汉印喷印机内容配置表）
- **业务含义**：汉印喷印机喷印内容配置表。
- **关联关系**：
  - TBL_EAP_PMS_CONTENT.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 81. TBL_EAP_PMS_PROD（汉印生产记录主表）
- **业务含义**：汉印喷印机生产记录主表。
- **关联关系**：
  - TBL_EAP_PMS_PROD.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 82. TBL_EAP_PMS_PROD_DTL（汉印生产记录明细表）
- **业务含义**：汉印喷印机生产记录明细表。
- **关联关系**：
  - TBL_EAP_PMS_PROD_DTL.CPROD_ID = TBL_EAP_PMS_PROD.CID

----------------------

### 83. TBL_EAP_SHOOT_ITEM（打靶结果明细表）
- **业务含义**：打靶机测量结果明细表。
- **关联关系**：无

----------------------

### 84. TBL_EAP_SHUTDOWN_RECORD（放板机关机记录表）
- **业务含义**：放板机关机记录表。
- **关联关系**：无

----------------------

### 85. TBL_EAP_STATUS（设备状态采集记录表）
- **业务含义**：设备状态实时采集记录表。
- **关联关系**：
  - TBL_EAP_STATUS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 86. TBL_EAP_T_ALARM（报警记录表）
- **业务含义**：设备报警记录表（简版）。
- **关联关系**：无

----------------------

### 87. TBL_EAP_T_OPERATION（操作记录表）
- **业务含义**：设备操作记录表。
- **关联关系**：无

----------------------

### 88. TBL_EAP_T_OPERATION2（操作记录表（扩展））
- **业务含义**：设备操作记录扩展表。
- **关联关系**：无

----------------------

### 89. TBL_EAP_T_OUT_HISTORY（图电出板历史记录表）
- **业务含义**：图电工序出板历史记录表。
- **关联关系**：无

----------------------

### 90. TBL_EAP_TAG（测点配置表）
- **业务含义**：设备测点配置表，定义采集点信息。
- **关联关系**：
  - TBL_EAP_TAG.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 91. TBL_EAP_THREE_D_DATA（三次元数据）
- **业务含义**：三次元测量数据表。
- **关联关系**：
  - TBL_EAP_THREE_D_DATA.CRECORD_ID = TBL_EAP_THREE_D_RECORD.CID

----------------------

### 92. TBL_EAP_THREE_D_ITEM（三次元数据明细）
- **业务含义**：三次元测量数据明细表。
- **关联关系**：无

----------------------

### 93. TBL_EAP_THREE_D_RECORD（三次元文件记录主表）
- **业务含义**：三次元测量文件记录主表。
- **关联关系**：无

----------------------

### 94. TBL_EAP_TIME_RANGE_CONTROL（放板机时间范围管控）
- **业务含义**：放板机时间范围管控配置表。
- **关联关系**：无

----------------------

### 95. TBL_EAP_WHC（文坦验孔机主记录表）
- **业务含义**：文坦验孔机检测记录主表。
- **关联关系**：
  - TBL_EAP_WHC.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 96. TBL_EAP_WHC_DTL（文坦验孔机明细记录表）
- **业务含义**：文坦验孔机检测记录明细表。
- **关联关系**：
  - TBL_EAP_WHC_DTL.CWHC_ID = TBL_EAP_WHC.CID
  - TBL_EAP_WHC_DTL.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 97. TBL_EAP_YUHUI_TEST_RECORDS（誉汇测试记录主表）
- **业务含义**：誉汇测试设备检测记录主表。
- **关联关系**：
  - TBL_EAP_YUHUI_TEST_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 98. TBL_EAP_YUHUI_TEST_RECORDS_DTL（誉汇测试记录明细表）
- **业务含义**：誉汇测试设备检测记录明细表。
- **关联关系**：
  - TBL_EAP_YUHUI_TEST_RECORDS_DTL.CMAIN_ID = TBL_EAP_YUHUI_TEST_RECORDS.CID

----------------------

### 99. TBL_EAP_YULIGHT_DETECTIONS_PCS（宇之光生产记录）
- **业务含义**：宇之光检测设备PCS级生产记录。
- **关联关系**：
  - TBL_EAP_YULIGHT_DETECTIONS_PCS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 100. TBL_EAP_YULIGHT_DETECTIONS_PNL（宇之光PNL检测记录表）
- **业务含义**：宇之光检测设备PNL级检测记录。
- **关联关系**：
  - TBL_EAP_YULIGHT_DETECTIONS_PNL.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 101. TBL_ABNORMAL_DATA_POOL（锁机锁卡异常数据表）
- **业务含义**：锁机锁卡异常数据记录表。
- **关联关系**：无

----------------------

### 102. TBL_DEVICE_SPEED_PARAMS（设备速度参数配置表）
- **业务含义**：设备速度参数配置表。
- **关联关系**：
  - TBL_DEVICE_SPEED_PARAMS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_DEVICE_SPEED_PARAMS.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------

### 103. TBL_HPL_SEND_LOG（水平线参数下发接口发送日志表）
- **业务含义**：水平线参数下发接口调用日志。
- **关联关系**：无

----------------------

### 104. TBL_JINMING_TASK_RESULT（今明设备任务回传结果表）
- **业务含义**：今明设备任务执行结果回传表。
- **关联关系**：
  - TBL_JINMING_TASK_RESULT.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 105. TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD（浩硕生产记录实体类）
- **业务含义**：浩硕图形电镀生产记录主表。
- **关联关系**：无

----------------------

### 106. TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL（浩硕图形电镀生产记录明细表）
- **业务含义**：浩硕图形电镀生产记录明细表。
- **关联关系**：
  - TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL.CDETECTION_ID = TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD.CID

----------------------

### 107. TBL_PATTERN_PLATING_PRODUCTION_RECORD（图电生产记录实体类）
- **业务含义**：图电工序生产记录实体表。
- **关联关系**：无

---

## 五、品质管理

----------------------

### 108. TBL_QM_ASSAY_LOG（化验任务记录表）
- **业务含义**：化验任务记录主表，记录药水化验任务信息。
- **关联关系**：
  - TBL_QM_ASSAY_LOG.CMEDICINE_TANK_ID = TBL_QM_MEDICINE_TANK.CID
  - TBL_QM_ASSAY_LOG.CWC_ID = TBL_BD_WC.CID

----------------------

### 109. TBL_QM_ASSAY_LOG_ITEM（化验任务明细表）
- **业务含义**：化验任务明细表，记录化验项目的具体值和判定。
- **关联关系**：
  - TBL_QM_ASSAY_LOG_ITEM.CASSAY_LOG_ID = TBL_QM_ASSAY_LOG.CID

----------------------

### 110. TBL_QM_CC_EXCEPTION（客诉异常报告信息表）
- **业务含义**：客户投诉异常报告主表，记录客诉及处理流程。
- **关联关系**：
  - TBL_QM_CC_EXCEPTION.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_CC_EXCEPTION.CEXCEP_PROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_CC_EXCEPTION.CDUTY_PROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_CC_EXCEPTION.COUT_PROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 111. TBL_QM_COMPLAINT（品质投诉记录表）
- **业务含义**：品质投诉记录表，记录投诉信息及8D报告关联。
- **关联关系**：无

----------------------

### 112. TBL_QM_COMPLAINT_IMAGE（品质投诉图片表）
- **业务含义**：品质投诉图片表，存储投诉相关图片。
- **关联关系**：
  - TBL_QM_COMPLAINT_IMAGE.CCOMPLAINT_ID = TBL_QM_COMPLAINT.CID

----------------------

### 113. TBL_QM_INSPECT_RECORD（品质检验记录主表）
- **业务含义**：品质检验记录主表，记录IPQC/FQC等检验任务。
- **关联关系**：
  - TBL_QM_INSPECT_RECORD.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_INSPECT_RECORD.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------

### 114. TBL_QM_INSPECTION_RECORD_ITEM（品质检验记录明细表）
- **业务含义**：品质检验记录明细表，记录检验项目的具体值。
- **关联关系**：
  - TBL_QM_INSPECTION_RECORD_ITEM.CINSPECTION_RECORD_ID = TBL_QM_INSPECT_RECORD.CID

----------------------

### 115. TBL_QM_MEDICINE_TANK（药缸信息表）
- **业务含义**：药缸信息表，存储药水缸体信息。
- **关联关系**：
  - TBL_QM_MEDICINE_TANK.CWC_ID = TBL_BD_WC.CID

----------------------

### 116. TBL_QM_PL_LOG（物理实验室送检记录主表）
- **业务含义**：物理实验室送检记录主表。
- **关联关系**：
  - TBL_QM_PL_LOG.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_PL_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_PL_LOG.CWC_ID = TBL_BD_WC.CID

----------------------

### 117. TBL_QM_PL_LOG_ITEM（物理实验室送检记录明细表）
- **业务含义**：物理实验室送检记录明细表。
- **关联关系**：
  - TBL_QM_PL_LOG_ITEM.CPL_LOG_ID = TBL_QM_PL_LOG.CID

---

## 六、文件管理

----------------------

### 118. TBL_ESOP_CONTACT_FORM（联络单信息表）
- **业务含义**：联络单信息表，存储内部联络单流程数据。
- **关联关系**：无

----------------------

### 119. TBL_ESOP_COUNTERSIGN（4M文件会签信息表）
- **业务含义**：4M文件/联络单会签信息记录。
- **关联关系**：无

----------------------

### 120. TBL_ESOP_FILE（ESOP文件主表）
- **业务含义**：ESOP文件管理主表，存储文件元数据。
- **关联关系**：无

----------------------

### 121. TBL_ESOP_FILE_CATEGORY（ESOP文件分类表）
- **业务含义**：ESOP文件分类表，支持树形分类。
- **关联关系**：
  - TBL_ESOP_FILE_CATEGORY.CPARENT_ID = TBL_ESOP_FILE_CATEGORY.CID

----------------------

### 122. TBL_ESOP_FILE_SIGN（文件手写体信息）
- **业务含义**：文件手写体签名信息存储。
- **关联关系**：无

----------------------

### 123. TBL_ESOP_FILE_TYPE（ESOP文件类型表）
- **业务含义**：ESOP文件类型定义表。
- **关联关系**：无

----------------------

### 124. TBL_ESOP_TEMPLATE（ESOP模板关联表）
- **业务含义**：ESOP模板与文件关联表。
- **关联关系**：无

----------------------

### 125. TBL_ESOP_TEMPORARY_CHANGE_ORDER（4M临时变更单）
- **业务含义**：4M临时变更申请单，记录人机料法变更。
- **关联关系**：无

----------------------

### 126. TBL_FOURM_CHANGE_ITEM_LOG（4M变更料号日志表）
- **业务含义**：4M变更涉及的料号变更日志。
- **关联关系**：无

---

## 七、点检保养

----------------------

### 127. TBL_EAM_PM_TEMP_WC_LINK（模板关联工作中心）
- **业务含义**：点检/保养模板与工作中心关联表。
- **关联关系**：
  - TBL_EAM_PM_TEMP_WC_LINK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_PM_TEMP_WC_LINK.CWC_ID = TBL_BD_WC.CID

----------------------

### 128. TBL_NP_TEMPLATE（模板主表）
- **业务含义**：点检/保养模板主表。
- **关联关系**：无

----------------------

### 129. TBL_NP_TEMPLATE_CHANGE（模板变更主表）
- **业务含义**：模板变更记录主表，记录模板版本变更。
- **关联关系**：无

----------------------

### 130. TBL_NP_TEMPLATE_CHANGE_ITEM（模板变更明细表）
- **业务含义**：模板变更明细表，记录模板项变更前后值。
- **关联关系**：
  - TBL_NP_TEMPLATE_CHANGE_ITEM.CTEMPLATE_CHANGE_ID = TBL_NP_TEMPLATE_CHANGE.CID

----------------------

### 131. TBL_NP_TEMPLATE_ITEM（模板项配置表）
- **业务含义**：点检/保养模板项配置表。
- **关联关系**：
  - TBL_NP_TEMPLATE_ITEM.CTEMPLATE_ID = TBL_NP_TEMPLATE.CID

----------------------

### 132. TBL_EAM_PM_TEMPLATE_ITEMS（点检模板项目明细表）
- **业务含义**：点检模板项目明细表。
- **关联关系**：无

----------------------

### 133. TBL_EAM_EQUIPMENT（设备主数据表）
- **业务含义**：设备主数据表，存储设备基础信息。
- **关联关系**：
  - TBL_EAM_EQUIPMENT.CWC_ID = TBL_BD_WC.CID

----------------------

### 134. TBL_EAM_EQUIPMENT_TYPE（设备类型信息表）
- **业务含义**：设备类型定义表。
- **关联关系**：无

----------------------

### 135. TBL_EAM_ERROR_CODE（设备故障代码表）
- **业务含义**：设备故障代码定义表。
- **关联关系**：无

----------------------

### 136. TBL_EAM_FREQUENCY（设备保养频次配置表）
- **业务含义**：设备保养频次配置表。
- **关联关系**：无

----------------------

### 137. TBL_EAM_MAINTAIN_STANDARD_IMG（保养标准图片表）
- **业务含义**：保养标准图片存储表。
- **关联关系**：无

----------------------

### 138. TBL_EAM_MAINTAIN_TASK（保养任务主表）
- **业务含义**：保养任务主表，记录保养任务执行情况。
- **关联关系**：
  - TBL_EAM_MAINTAIN_TASK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_MAINTAIN_TASK.CWC_ID = TBL_BD_WC.CID

----------------------

### 139. TBL_EAM_MAINTAIN_TASK_CHANGE_LOG（保养任务时间变更日志表）
- **业务含义**：保养任务计划时间变更日志。
- **关联关系**：
  - TBL_EAM_MAINTAIN_TASK_CHANGE_LOG.CTASK_ID = TBL_EAM_MAINTAIN_TASK.CID

----------------------

### 140. TBL_EAM_MAINTAIN_TASK_ITEM（保养任务明细表）
- **业务含义**：保养任务明细表，记录保养项目的执行值和结果。
- **关联关系**：
  - TBL_EAM_MAINTAIN_TASK_ITEM.CHID = TBL_EAM_MAINTAIN_TASK.CID

----------------------

### 141. TBL_EAM_MAINTAIN_TASK_ITEM_IMG（保养任务明细图片表）
- **业务含义**：保养任务明细图片存储表。
- **关联关系**：
  - TBL_EAM_MAINTAIN_TASK_ITEM_IMG.CITEM_ID = TBL_EAM_MAINTAIN_TASK_ITEM.CID

----------------------

### 142. TBL_EAM_MAINTAIN_TEMP_D（保养模板变更历史明细表）
- **业务含义**：保养模板变更历史明细表。
- **关联关系**：无

----------------------

### 143. TBL_EAM_MAINTAIN_TEMP_WC_LINK（保养模板与工作中心关联表）
- **业务含义**：保养模板与工作中心关联表。
- **关联关系**：
  - TBL_EAM_MAINTAIN_TEMP_WC_LINK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_MAINTAIN_TEMP_WC_LINK.CWC_ID = TBL_BD_WC.CID

----------------------

### 144. TBL_EAM_MAINTAIN_TEMPLATE_ITEMS（保养模板项目表）
- **业务含义**：保养模板项目定义表。
- **关联关系**：无

----------------------

### 145. TBL_EAM_REPAIR（维修工单主表）
- **业务含义**：设备维修工单主表，记录报修、维修、关闭全流程。
- **关联关系**：
  - TBL_EAM_REPAIR.CWC_ID = TBL_BD_WC.CID
  - TBL_EAM_REPAIR.CERROR_ID = TBL_EAM_ERROR_CODE.CID

----------------------

### 146. TBL_EAM_REPAIR_IMG（维修图片记录表）
- **业务含义**：维修工单图片记录表。
- **关联关系**：
  - TBL_EAM_REPAIR_IMG.CREPAIR_ID = TBL_EAM_REPAIR.CID

----------------------

### 147. TBL_EAM_REPAIR_MAN（指派人员列表）
- **业务含义**：维修工单指派人员记录。
- **关联关系**：
  - TBL_EAM_REPAIR_MAN.CREPAIR_ID = TBL_EAM_REPAIR.CID

----------------------

### 148. TBL_EAM_REPAIR_MATERIAL（维修耗材记录表）
- **业务含义**：维修工单耗材使用记录。
- **关联关系**：
  - TBL_EAM_REPAIR_MATERIAL.CREPAIR_ID = TBL_EAM_REPAIR.CID

---

## 八、生产流程

----------------------

### 149. TBL_SFC_WS_LOG（生产记录表）
- **业务含义**：工位报工/检验类生产记录主表（数量、班次、条码、模板等）。
- **关联关系**：
  - TBL_SFC_WS_LOG.CMO_LOT = TBL_MO.CMO_LOT
  - TBL_SFC_WS_LOG.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_SFC_WS_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SFC_WS_LOG.CWC_ID = TBL_BD_WC.CID

----------------------

### 150. TBL_SFC_WS_LOG_ITEM（生产记录项目明细）
- **业务含义**：生产记录项目明细表，记录报工时填写的检验项目值。
- **关联关系**：
  - TBL_SFC_WS_LOG_ITEM.CWS_LOG_ID = TBL_SFC_WS_LOG.CID

----------------------

### 151. TBL_SFC_WS_TEMPLATE_CONFIG（工位报工模板配置表）
- **业务含义**：工位报工模板配置表，控制报工界面行为。
- **关联关系**：无

----------------------

### 152. TBL_SFC_WS_TEMPLATE_LINK（工位模板关联配置表）
- **业务含义**：工位模板与工序/工作中心关联表。
- **关联关系**：
  - TBL_SFC_WS_TEMPLATE_LINK.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SFC_WS_TEMPLATE_LINK.CWC_ID = TBL_BD_WC.CID

----------------------

### 153. TBL_MO（工单信息表）
- **业务含义**：生产工单主表，记录工单计划与执行信息。
- **关联关系**：
  - TBL_MO.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_MO.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_MO.CWC_ID = TBL_BD_WC.CID

----------------------

### 154. TBL_MO_FAKE（虚拟工单表）
- **业务含义**：虚拟工单表，用于特殊场景（如无工单生产）。
- **关联关系**：无

----------------------

### 155. TBL_MO_OUTS（外协工单信息表）
- **业务含义**：外协工单信息表，记录外协订单关联。
- **关联关系**：无

----------------------

### 156. TBL_SFC_DBFC_USER（叠板防错用户）
- **业务含义**：叠板防错功能授权用户表。
- **关联关系**：无

----------------------

### 157. TBL_SFC_PACKAGE（包装信息表）
- **业务含义**：成品/半成品包装信息主表。
- **关联关系**：
  - TBL_SFC_PACKAGE.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 158. TBL_SFC_PACKAGE_LABEL_LINK（包装模板与物料/客户关联表）
- **业务含义**：包装模板与物料/客户的关联配置。
- **关联关系**：无

----------------------

### 159. TBL_SFC_PACKAGE_LOG（包装操作日志表）
- **业务含义**：包装操作日志记录。
- **关联关系**：无

----------------------

### 160. TBL_SFC_PACKAGE_RULE（包装规则主表）
- **业务含义**：包装规则配置主表。
- **关联关系**：无

----------------------

### 161. TBL_SFC_PACKAGE_RULE_EXT（包装规则扩展配置表）
- **业务含义**：包装规则扩展属性配置。
- **关联关系**：
  - TBL_SFC_PACKAGE_RULE_EXT.CPACKAGE_RULE_ID = TBL_SFC_PACKAGE_RULE.CID

----------------------

### 162. TBL_SFC_PACKAGE_RULE_LINK（包装规则与物料/客户关联表）
- **业务含义**：包装规则与物料/客户关联配置。
- **关联关系**：无

----------------------

### 163. TBL_SFC_RECIPE_LOT（按工单批次的配方申请主表）
- **业务含义**：按工单批次申请的配方记录主表。
- **关联关系**：无

----------------------

### 164. TBL_SFC_RECIPE_LOT_LINK（工单批次配方项目明细表）
- **业务含义**：工单批次配方的具体项目明细。
- **关联关系**：
  - TBL_SFC_RECIPE_LOT_LINK.CR_LOT_ID = TBL_SFC_RECIPE_LOT.CID

----------------------

### 165. TBL_SFC_RECIPE_PRODUCT（按产品维度的配方申请主表）
- **业务含义**：按产品物料维度申请的配方记录主表。
- **关联关系**：
  - TBL_SFC_RECIPE_PRODUCT.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 166. TBL_SFC_RECIPE_PRODUCT_LINK（产品配方项目明细表）
- **业务含义**：产品配方的具体项目明细。
- **关联关系**：
  - TBL_SFC_RECIPE_PRODUCT_LINK.CR_PRODUCT_ID = TBL_SFC_RECIPE_PRODUCT.CID

----------------------

### 167. TBL_OUTSOURCE_SHIFT_EMPLOYEE（外协班次员工配置表）
- **业务含义**：外协工厂班次与员工配置表。
- **关联关系**：无

---

## 九、仓储管理

----------------------

### 168. TBL_WMS_ITEM_BARCODE（物料条码表）
- **业务含义**：物料条码主表，存储库存条码及数量信息。
- **关联关系**：
  - TBL_WMS_ITEM_BARCODE.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_ITEM_BARCODE.CLOCATION_ID = TBL_WMS_LOCATION.CID

----------------------

### 169. TBL_WMS_ITEM_PACKING_BARCODE（物料包装条码表）
- **业务含义**：物料包装层级条码关联表。
- **关联关系**：无

----------------------

### 170. TBL_WMS_LINE_BARCODE_RECORD（线边仓条码出入记录表）
- **业务含义**：线边仓条码出入库操作记录。
- **关联关系**：无

----------------------

### 171. TBL_WMS_LINE_RECORD（线别仓操作记录）
- **业务含义**：线别仓操作记录表。
- **关联关系**：无

----------------------

### 172. TBL_WMS_LOCATION（仓库货位）
- **业务含义**：仓库货位主数据表。
- **关联关系**：
  - TBL_WMS_LOCATION.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------

### 173. TBL_WMS_MANTISSA_RECORD（尾数仓操作记录）
- **业务含义**：尾数仓操作记录表。
- **关联关系**：无

----------------------

### 174. TBL_WMS_PACKAGE_IN_RECORDS（入库记录表）
- **业务含义**：成品/物料入库记录主表。
- **关联关系**：无

----------------------

### 175. TBL_WMS_PACKAGE_IN_RECORDS_BOXES（入库记录外箱详情表）
- **业务含义**：入库记录外箱明细表。
- **关联关系**：
  - TBL_WMS_PACKAGE_IN_RECORDS_BOXES.CRECORD_ID = TBL_WMS_PACKAGE_IN_RECORDS.CID

----------------------

### 176. TBL_WMS_PICKING_LOG（领料记录）
- **业务含义**：领料记录主表。
- **关联关系**：无

----------------------

### 177. TBL_WMS_PICKING_LOG_DTL（领料记录明细）
- **业务含义**：领料记录明细表。
- **关联关系**：
  - TBL_WMS_PICKING_LOG_DTL.CPICKING_ID = TBL_WMS_PICKING_LOG.CID

----------------------

### 178. TBL_WMS_WAREHOUSE（仓库主数据表）
- **业务含义**：仓库主数据表。
- **关联关系**：
  - TBL_WMS_WAREHOUSE.CWAREHOUSE_TYPE_ID = TBL_WMS_WAREHOUSE_TYPE.CID

----------------------

### 179. TBL_WMS_WAREHOUSE_TYPE（仓库类型）
- **业务含义**：仓库类型定义表。
- **关联关系**：无

----------------------

### 180. TBL_WMS_AREA（仓库区域）
- **业务含义**：仓库区域定义表。
- **关联关系**：
  - TBL_WMS_AREA.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------

### 181. TBL_WMS_BARCODE_SPLIT_RECORD（条码拆分记录表）
- **业务含义**：条码拆分操作记录。
- **关联关系**：无

----------------------

### 182. TBL_WMS_ITEM_BARCODE_HISTORY（物料条码操作历史表）
- **业务含义**：物料条码操作历史记录。
- **关联关系**：无

----------------------

### 183. TBL_WMS_ITEM_LOCATION（物料默认货位）
- **业务含义**：物料默认货位配置表。
- **关联关系**：
  - TBL_WMS_ITEM_LOCATION.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_ITEM_LOCATION.CLOCATION_ID = TBL_WMS_LOCATION.CID

----------------------

### 184. TBL_WMS_ITEM_TEMPLATE（物料标签绑定表）
- **业务含义**：物料与标签模板绑定关系。
- **关联关系**：无

----------------------

### 185. TBL_WMS_MI（备料单主表）
- **业务含义**：备料单主表，记录生产备料需求。
- **关联关系**：
  - TBL_WMS_MI.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------

### 186. TBL_WMS_MI_BARCODE（备料条码表）
- **业务含义**：备料单关联条码记录。
- **关联关系**：无

----------------------

### 187. TBL_WMS_MI_DTL（备料单子表）
- **业务含义**：备料单明细表，记录备料物料及数量。
- **关联关系**：
  - TBL_WMS_MI_DTL.CMI_ID = TBL_WMS_MI.CID
  - TBL_WMS_MI_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 188. TBL_WMS_PI（出入库主表）
- **业务含义**：出入库单据主表。
- **关联关系**：
  - TBL_WMS_PI.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------

### 189. TBL_WMS_PI_BARCODE（出入库条码表）
- **业务含义**：出入库单据关联条码记录。
- **关联关系**：
  - TBL_WMS_PI_BARCODE.CPI_DTL_ID = TBL_WMS_PI_DTL.CID

----------------------

### 190. TBL_WMS_PI_DTL（出入库明细表）
- **业务含义**：出入库单据明细表。
- **关联关系**：
  - TBL_WMS_PI_DTL.CPI_ID = TBL_WMS_PI.CID
  - TBL_WMS_PI_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 191. TBL_WMS_PRINT_LOG（WMS标签打印日志表）
- **业务含义**：WMS标签打印日志记录。
- **关联关系**：无

----------------------

### 192. TBL_WMS_PRODUCT_BARCODE（成品仓条码表）
- **业务含义**：成品仓条码库存表。
- **关联关系**：无

----------------------

### 193. TBL_WMS_PS（出货单主表）
- **业务含义**：出货单主表，记录销售出库信息。
- **关联关系**：无

----------------------

### 194. TBL_WMS_PS_BARCODE（出货单条码表）
- **业务含义**：出货单关联条码记录。
- **关联关系**：
  - TBL_WMS_PS_BARCODE.CPS_DTL_ID = TBL_WMS_PS_DTL.CID

----------------------

### 195. TBL_WMS_PS_DTL（出货单明细表）
- **业务含义**：出货单明细表。
- **关联关系**：
  - TBL_WMS_PS_DTL.CPSID = TBL_WMS_PS.CID
  - TBL_WMS_PS_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 196. TBL_WMS_SALES_ORDER（销售订单表）
- **业务含义**：销售订单主表。
- **关联关系**：无

----------------------

### 197. TBL_WMS_STOCK_BARCODE_LINK（ERP库存与打印条码关联表）
- **业务含义**：ERP库存记录与打印条码关联。
- **关联关系**：无

----------------------

### 198. TBL_WMS_STOCKTAKING_DTL（盘点单明细表）
- **业务含义**：盘点单明细表。
- **关联关系**：
  - TBL_WMS_STOCKTAKING_DTL.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_STOCKTAKING_DTL.CLOCATION_ID = TBL_WMS_LOCATION.CID

---

## 十、供应链协同

----------------------

### 199. TBL_SRM_PO（采购单）
- **业务含义**：采购订单主表。
- **关联关系**：
  - TBL_SRM_PO.CSUPPLIER_ID = TBL_BD_SUPPLIER.CID

----------------------

### 200. TBL_SRM_PO_DELIVERY（采购订单交付表）
- **业务含义**：采购订单交付计划表。
- **关联关系**：
  - TBL_SRM_PO_DELIVERY.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 201. TBL_SRM_PO_DETAIL（采购订单明细）
- **业务含义**：采购订单明细表。
- **关联关系**：
  - TBL_SRM_PO_DETAIL.CPO_ID = TBL_SRM_PO.CID
  - TBL_SRM_PO_DETAIL.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 202. TBL_SRM_RECEIVING（收货单主表）
- **业务含义**：采购收货单主表。
- **关联关系**：
  - TBL_SRM_RECEIVING.CSUPPLIER_ID = TBL_BD_SUPPLIER.CID

----------------------

### 203. TBL_SRM_RECEIVING_BARCODE（收货单条码关联表）
- **业务含义**：收货单关联条码记录。
- **关联关系**：
  - TBL_SRM_RECEIVING_BARCODE.CRECEIVING_DTL_ID = TBL_SRM_RECEIVING_DTL.CID

----------------------

### 204. TBL_SRM_RECEIVING_DTL（收货单明细表）
- **业务含义**：收货单明细表，记录收货物料及检验结果。
- **关联关系**：
  - TBL_SRM_RECEIVING_DTL.CRECEIVING_ID = TBL_SRM_RECEIVING.CID
  - TBL_SRM_RECEIVING_DTL.CITEM_ID = TBL_BD_ITEM.CID

---

## 十一、物料防错

----------------------

### 205. TBL_SHEET_LINK_PP（供应商替代关联表）
- **业务含义**：供应商替代关系配置表。
- **关联关系**：无

----------------------

### 206. TBL_ITEM_LINK_SUPPLIER（料号与供应商关联表）
- **业务含义**：物料与供应商关联配置表。
- **关联关系**：无

----------------------

### 207. TBL_MO_BARCODE_PROD_LINK（工单与条码生产关联表）
- **业务含义**：工单与生产条码关联记录。
- **关联关系**：无

----------------------

### 208. TBL_PRESTK_RECORD（预叠操作记录表）
- **业务含义**：预叠操作记录表。
- **关联关系**：无

---

## 十二、SPC

----------------------

### 209. TBL_SPC_CONTROL_CHARACTERISTIC（SPC管控特性主表）
- **业务含义**：SPC统计过程控制特性定义表。
- **关联关系**：
  - TBL_SPC_CONTROL_CHARACTERISTIC.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SPC_CONTROL_CHARACTERISTIC.CWC_ID = TBL_BD_WC.CID

----------------------

### 210. TBL_SPC_CONTROL_CHARACTERISTIC_ITEM_LINK（SPC管控特性与对象关联表）
- **业务含义**：SPC特性与料号/模板关联表。
- **关联关系**：
  - TBL_SPC_CONTROL_CHARACTERISTIC_ITEM_LINK.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------

### 211. TBL_SPC_CONTROL_CHARACTERISTIC_LIMIT（SPC管控特性控制限配置表）
- **业务含义**：SPC控制图控制限配置表。
- **关联关系**：
  - TBL_SPC_CONTROL_CHARACTERISTIC_LIMIT.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------

### 212. TBL_SPC_CONTROL_CHARACTERISTIC_RULE_LINK（SPC管控特性与判异规则关联表）
- **业务含义**：SPC特性与判异规则关联表。
- **关联关系**：
  - TBL_SPC_CONTROL_CHARACTERISTIC_RULE_LINK.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------

### 213. TBL_SPC_DATA_REAL（SPC实时采样数据表）
- **业务含义**：SPC实时采样数据记录表。
- **关联关系**：
  - TBL_SPC_DATA_REAL.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------

### 214. TBL_SPC_RULE_OF_DISSENT（SPC判异规则定义表）
- **业务含义**：SPC判异规则定义表。
- **关联关系**：无

---

## 十三、出货报告

----------------------

### 215. TBL_OQC_SHIPMENT_GENERATE（出货报告生成）
- **业务含义**：出货报告生成记录主表。
- **关联关系**：无

----------------------

### 216. TBL_OQC_SHIPMENT_GENERATE_LOG（出货报告生成记录）
- **业务含义**：出货报告生成历史版本记录。
- **关联关系**：无

----------------------

### 217. TBL_OQC_SHIPMENT_ITEM_LINK（出货报告料号关联表）
- **业务含义**：出货报告与料号关联表。
- **关联关系**：
  - TBL_OQC_SHIPMENT_ITEM_LINK.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 218. TBL_OQC_SHIPMENT_REPORT（出货报告表）
- **业务含义**：出货报告定义主表。
- **关联关系**：无

----------------------

### 219. TBL_OQC_SHIPMENT_REPORT_TYPE（出货报告类型表）
- **业务含义**：出货报告类型定义表。
- **关联关系**：无

----------------------

### 220. TBL_OQC_SHIPMENT_TEMPLATE_LINK（出货报告模板关联表）
- **业务含义**：出货报告与模板关联表。
- **关联关系**：无

---

## 十四、锁机锁卡

----------------------

### 221. TBL_PM_ITEM_LINK_TAG（点检项目与测点关联表）
- **业务含义**：点检项目与设备测点关联配置。
- **关联关系**：无

----------------------

### 222. TBL_PM_TEMPLATE_LINK_DEVICE（模板与工作中心关联采集设备）
- **业务含义**：点检模板与采集设备关联表。
- **关联关系**：无

----------------------

### 223. TBL_SJSKDATA_YYYYMM（锁机锁卡读码记录表）
- **业务含义**：锁机锁卡设备读码记录表（按月分表）。
- **关联关系**：无

----------------------

### 224. TBL_SJSKEQPINFO（读码设备实时工单信息表）
- **业务含义**：读码设备当前/下一工单信息表。
- **关联关系**：无

----------------------

### 225. TBL_EAP_ALARM_CONTROL_LINK（设备报警项关联配置表）
- **业务含义**：设备报警项与测点关联配置。
- **关联关系**：
  - TBL_EAP_ALARM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 226. TBL_EAP_ITEM_CONTROL_LINK（设备关联料号）
- **业务含义**：设备可生产物料关联配置。
- **关联关系**：
  - TBL_EAP_ITEM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_ITEM_CONTROL_LINK.CITEM_ID = TBL_BD_ITEM.CID

----------------------

### 227. TBL_EAP_POTION_ITEM_CONTROL_LINK（设备关联药水化验项目）
- **业务含义**：设备与药水化验项目关联配置。
- **关联关系**：
  - TBL_EAP_POTION_ITEM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------

### 228. TBL_EAP_PRODUCE_CONTROL_DEVICE（生产管控设备配置表）
- **业务含义**：生产管控设备开关配置表。
- **关联关系**：
  - TBL_EAP_PRODUCE_CONTROL_DEVICE.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

---

## 十五、其它信息

----------------------

### 229. TBL_FA_TXDD_KTHD（图形电镀孔铜厚度测量）
- **业务含义**：图形电镀孔铜厚度测量数据表。
- **关联关系**：
  - TBL_FA_TXDD_KTHD.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 230. TBL_FA_TXDD_MAIN（图像电镀FA信息主表）
- **业务含义**：图形电镀FA（首件确认）信息主表。
- **关联关系**：无

----------------------

### 231. TBL_FA_TXDD_QPBT（图形电镀切片表铜）
- **业务含义**：图形电镀切片表铜测量数据。
- **关联关系**：
  - TBL_FA_TXDD_QPBT.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 232. TBL_FA_TXDD_SKKJ（图形电镀蚀刻后孔径测量）
- **业务含义**：图形电镀蚀刻后孔径测量数据。
- **关联关系**：
  - TBL_FA_TXDD_SKKJ.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 233. TBL_FA_TXDD_SKXK（图形电镀蚀刻后线宽）
- **业务含义**：图形电镀蚀刻后线宽/线隙测量数据。
- **关联关系**：
  - TBL_FA_TXDD_SKXK.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 234. TBL_FA_TXDD_XHCL（图形电镀锡厚测量）
- **业务含义**：图形电镀锡厚测量数据。
- **关联关系**：
  - TBL_FA_TXDD_XHCL.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 235. TBL_FA_TXDD_ZKCS（图形电镀阻抗测试）
- **业务含义**：图形电镀阻抗测试数据。
- **关联关系**：
  - TBL_FA_TXDD_ZKCS.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------

### 236. TBL_FA_YHYJ_MAIN（压合压机）
- **业务含义**：压合压机FA（首件确认）信息主表。
- **关联关系**：无

----------------------

### 237. TBL_FA_YHYJ_MI（压合压机MI实测）
- **业务含义**：压合压机MI（制造指示）实测数据。
- **关联关系**：
  - TBL_FA_YHYJ_MI.CMAIN_ID = TBL_FA_YHYJ_MAIN.CID

----------------------

### 238. TBL_MEP_MATERIAL_PARAM（重点物料参数维护）
- **业务含义**：重点物料/ NPI物料参数维护表。
- **关联关系**：
  - TBL_MEP_MATERIAL_PARAM.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_MEP_MATERIAL_PARAM.CPROCESS_ID = TBL_BD_PROCESS.CID
