# 中络MES系统数据库表结构汇总文档（含品质客诉模块）

## 文档说明
本文档汇总了中络MES系统中10个核心模块的所有数据库表结构信息，包括系统信息、基础数据、消息推送、设备联机、品质管理、文件管理、点检保养、生产流程、仓储管理、品质客诉。

## 统计概览

| 模块名称 | 表数量 | 字段总数 | 占比 |
|----------|--------|----------|------|
| 系统信息 | 10 | 88 | 100.0% |
| 基础数据 | 21 | 130 | 59.6% |
| 消息推送 | 9 | 46 | 17.4% |
| 设备联机 | 68 | 903 | 77.4% |
| 品质管理 | 10 | 259 | 18.2% |
| 品质客诉 | 14 | 378 | 21.0% |
| 文件管理 | 9 | 108 | 5.6% |
| 点检保养 | 22 | 383 | 16.7% |
| 生产流程 | 19 | 327 | 12.5% |
| 仓储管理 | 35 | 386 | 12.8% |
| **合计** | **217** | **3008** | **100.0%** |

---

## 系统信息模块

### TBL_SYS_DICTIONARY (数据字典)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCODE_PATH | string | 字典描述 |
| CDIC_CODE | string | 字典代码 |
| CDIC_DESC | string | 字典描述 |
| CDIC_GROUP_VALUE_EXPRESSION | string | 字典值表达式 |
| CDIC_GROUP_VALUE_TYPE | string | 字典值类型 |
| CDIC_NAME | string | 字典名称 |
| CDIC_TYPE | string | 字典类型 |
| CDIC_VALUE | string | 字典值 |
| CDIC_VALUE_EX | string | 字典值扩展 |
| CIS_CATEGORY | string | 是否系统级 |
| CIS_DEFAULT | string | 是否默认 |
| CIS_SYS | string | 是否系统级 |
| CNAME_PATH | string | 字典描述 |
| CPARENT | string | 父字典ID |
| CPARENT_DIC_ID | long | 父字典ID |
| CSEQ | int? | 字典在分组中的顺序 |

### TBL_SYS_ORGANIZATION (组织机构表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CORG_NAME | string | 组织名称 |
| CORG_NO | string | 组织编码 |
| CPARENT_ORG_ID | long? | 上级组织ID |

### TBL_SYS_PARAM (系统参数配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIS_SYS | string | 是否系统级 |
| CPARAM_CODE | string | 参数编码 |
| CPARAM_DESC | string | 参数描述 |
| CPARAM_NAME | string | 参数名称 |
| CPARAM_TYPE | long? | 参数分类(来源TBL_SYS_PARAM_TYPE) |
| CPARAM_VALUE | string | 参数值 |
| CPARAM_VALUE_EXPR | string | 参数校验表达式(正规则表达式，用于检验) |
| CPARAM_VALUE_EXT | string | 参数扩展值 |
| CPARAM_VALUE_SHOW_TYPE | string | 参数值显示类型(下拉框、文本框、复选框等) |
| CPARAM_VALUE_SOURCE | string | 参数值来源 |
| CPARAM_VALUE_TYPE | string | 参数值类型(来自于数据字典(用于值转换):整型、字符串、BOOL、FLOAT) |
| CREMARK | string | 备注信息 |
| CSEQ | int? | 参数在分组中的顺序 |

### TBL_SYS_PARAM_TYPE (系统参数分类表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPARAM_TYPE_DESC | string | 类别描述 |
| CPARAM_TYPE_NAME | string | 类别名称 |
| CPARAM_TYPE_NO | string | 类别代码 |
| CPARAM_TYPE_PATH | string | 类别路径 |
| CPARENT_ID | long | 上级分类 |
| CREMARK | string | 备注 |
| CSEQ | int? | 父级下的顺序号 |

### TBL_SYS_ROLE (系统角色表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CROLE_CODE | string | 角色编码 |
| CROLE_NAME | string | 角色名称 |

### TBL_SYS_SERVER (系统服务配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CSERVICE_NAME | string | 服务名称 |
| CSERVICE_NO | string | 服务编码 |
| CSERVICE_PASSWORD | string | 服务密码 |
| CSERVICE_PATH | string | 服务地址 |
| CSERVICE_USER | string | 服务账号 |

### TBL_SYS_TEMPLATE_CONFIG (系统模板配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBINDING | string | Excel单元格绑定数据源信息序列化后的json字符串 |
| CBUCKET_NAME | string | 模板文件MinIO桶名称 |
| CCODE | string | 模板编码 |
| CDATA | string | 绑定数据源列表序列化后的json字符串 |
| CDESC | string | 模板描述 |
| CFILE_NAME | string | 上传的模板文件名称 |
| CFILE_PATH | string | 模板文件MinIO路径 |
| CNAME | string | 模板名称 |
| DataSetId | long | 数据集Id |
| DataSetName | string | 数据集名称 |
| DataSourceId | long | 数据源Id |
| DataSourceName | string | 数据源名称 |
| ObjectName | string | 对象名称 |

### TBL_SYS_USER (系统用户表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUR_HOST | string | 当前登录主机 |
| CDATETIME_LAST_LOCKED_OUT | DateTime | 最后锁定时间 |
| CDATETIME_LAST_LOGIN | DateTime | 最后登录时间 |
| CDEFAULT_HOST | string | 默认登录主机 |
| CDISPLAY_NAME | string | 用户显示名 |
| CDISPLAY_NAME | string |  |
| CEMAIL | string | 邮箱 |
| CENTERPRISE_CODE | long |  |
| CFAILED_ATTEMPT_COUNT | int | 登录失败次数 |
| CFAILED_ATTEMPT_START | DateTime | 失败计数开始时间 |
| CGENDER | string | 性别 |
| CGENDER | string |  |
| CID | long |  |
| CIS_LOCKED_OUT | string | 是否锁定 |
| CIS_ONLINE | string | 是否在线 |
| CMOBILEPHONE | string | 手机号 |
| CMOBILEPHONE | string |  |
| CORG_CODE | long |  |
| CPASSWORD | string | 密码 |
| CUSER_NAME | string | 用户账号 |
| CUSER_NAME | string |  |
| CUSER_TYPE | string | 用户类型 |
| CUSER_TYPE | string |  |

### TBL_SYS_USER_ORG_MAP (用户组织关系)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIS_DEFAULT | string | 是否默认组织 |
| CIS_DEPT_MANAGER | string | 是否部门负责人 |
| CORG_ID | long | 组织ID |
| CUSER_ID | long | 用户ID |

### TBL_SYS_USER_ROLE_MAP (用户角色关系表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CROLE_ID | long | 角色ID |
| CUSER_ID | long | 用户ID |

---

## 基础数据模块

### TBL_BD_CUSTOMER (客户信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CUSTOMER_NAME | string | 客户名称 |
| CUSTOMER_NO | string | 客户编号 |

### TBL_BD_DEVICE_STATUS (采集设备实时状态表，疑似弃用)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 记录创建时间 |
| CID | long | 主键ID |
| CSTATUS_CODE | int | 设备状态编码 |
| CSTATUS_NAME | string | 设备状态名称 |

### TBL_BD_GROUP (组别)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CGROUP_NAME | string | 组别名称 |
| CGROUP_NO | string | 组别编号 |

### TBL_BD_GROUP_MEMBERS (组员)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CGROUP_ID | long | 组别 |
| CUSER_NAME | string | 姓名 |
| CUSER_NO | string | 工号 |

### TBL_BD_GROUP_MEMBERS_LINK (组别与成员关系映射表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CID | long |  |
| GROUP_ID | long | 组别ID（关联组别主表） |
| USER_ID | long | 用户ID（关联用户主表） |

### TBL_BD_ITEM (产品和物料信息表)
（**说明**：**物料类型名称 / 类型编码**不在本表；字段 **`CITEM_TYPE_ID`** 须关联 **`TBL_BD_ITEM_TYPE`**，在类型表上使用 **`CITEM_TYPE_NAME`、`CITEM_TYPE_NO`** 等。勿在本表上写 **`CITEM_TYPE_NAME`**，否则现场常见错误 **207**。）
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBOX_QTY | decimal? | 每箱标准数 |
| CCUSTOMER_MATER_NAME | string | 客户物料名称 |
| CCUSTOMER_MATER_NO | string | 客户物料编号 |
| CCUSTOMER_MATERIAL | string | 客户材料 |
| CCUSTOMER_MODEL | string | 客户型号 |
| CHEIGHT | decimal? | 高度 |
| CITEM_DESC | string | 产品描述 |
| CITEM_NAME | string | 产品名称 |
| CITEM_NO | string | 产品编号 |
| CITEM_SOURCE | string | 产品来源 |
| CITEM_SPEC | string | 产品规格 |
| CITEM_TYPE_ID | long? | 产品类型ID |
| CITEM_VERSION | string | 产品版本 |
| CITEM_WEIGHT | decimal? | 产品单重 |
| CLEN | decimal? | 长度 |
| CPACKAGE_QTY | decimal? | 单包数量 |
| CPLATE_WEIGHT | decimal? | 隔板重量 |
| CROUTE_ID | string | 工艺路线ID |
| CTYPE | string? | 类型 |
| CUSTOMER_CODE | string | 客户代码 |
| CWIDTH | decimal? | 宽度 |

### TBL_BD_ITEM_A (产品属性)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPARAM_KEY | string | 属性键 |
| CPARAM_VALUE | string | 属性默认值 |

### TBL_BD_ITEM_ATTR (产品属性)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_A_ID | long | 物料属性配置ID（关联属性定义表） |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CPARAM_KEY | string | 属性键 |
| CPARAM_VALUE | string | 属性值 |

### TBL_BD_ITEM_INSPECTION_STANDARD (物料检验标准配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOMPARE_SYMBOL | string | 比较符号 |
| CINSPECTION_TYPE | string | 检验类型 |
| CITEM_ID | Int64 | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CMAX_STANDARD | decimal? | 标准上限 |
| CMAX_TOLERANCE | decimal? | 最大公差 |
| CMAX_WARN | decimal? | 预警值上限 |
| CMIN_STANDARD | decimal? | 标准下限 |
| CMIN_TOLERANCE | decimal? | 最小公差 |
| CMIN_WARN | decimal? | 预警值下限 |
| CPROCESS_ID | Int64 | 工序ID |
| CREAL_MAX_STANDARD | decimal? | 实际标准上限 |
| CREAL_MIN_STANDARD | decimal? | 实际标准下限 |
| CREMARK | string | 备注 |
| CSTANDARD | string | 标准文本值 |
| CTEMP_ID | Int64 | 模板ID |
| CTEMP_ITEM_ID | Int64 | 模板项ID |
| CTYPE | int | 标准类型（1按上下限、2比较符） |

### TBL_BD_ITEM_TYPE (产品和物料类型表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CID | long | 主键；与 **`TBL_BD_ITEM.CITEM_TYPE_ID`** 关联 |
| CITEM_CONTROL_TYPE | long? | 物料管控类型 |
| CITEM_TYPE_BARCODE | string | 物料类型条码 |
| CITEM_TYPE_NAME | string | 物料类型名称 |
| CITEM_TYPE_NO | string | 物料类型编码 |
| CITEM_TYPE_PATH | string | 类型层级路径 |
| CPARENT_TYPE_ID | long? | 上级类型ID |
| CREMARK | string | 备注 |
| CSEQ | int | 排序号 |
| CSOURCE_ID | string | 来源系统ID |

### TBL_BD_PROCESS (工序工艺信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIS_COUNT | string | 是否计数工序 |
| CPARENT_PROCESS_ID | long? | 上级工序ID |
| CPROCESS_CONTROL_TYPE | long? | 工序管控类型 |
| CPROCESS_DESC | string | 工序描述 |
| CPROCESS_NAME | string | 工序名称 |
| CPROCESS_NO | string | 工序编码 |
| CPROCESS_PATH | string | 工序路径 |
| CPROCESS_SEQ | int? | 工序顺序 |
| CPROCESS_SHORT_CODE | string | 工序简称 |
| CPROCESS_TYPE_ID | long? | 工序类型ID |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源系统ID |

### TBL_BD_PROCESS_OUTS (外协产品工序表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPROCESS_CONTROL_TYPE | long? | 工序管控类型 |
| CPROCESS_DESC | string | 工序描述 |
| CPROCESS_ID | long? | 标准工序ID |
| CPROCESS_NAME | string | 工序名称 |
| CPROCESS_NO | string | 工序编码 |
| CPROCESS_SHORT_CODE | string | 工序简称 |
| CPRODUCT_ITEM_NO | string | 外协产品料号 |

### TBL_BD_REGEX (正则校验规则表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CREGEX_DESC | string | 规则描述 |
| CREGEX_NAME | string | 规则名称 |
| CREGEX_NO | string | 规则编码 |

### TBL_BD_RULE (编码规则定义表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CRULE_NAME | string | 规则名称 |
| CRULE_NO | string | 规则编码 |

### TBL_BD_SUPPLIER (供应商信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CADDRESS | string | 地址 |
| CEMAIL | string | 电子邮箱 |
| CPHONE | string | 联系电话 |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源系统ID |
| CSUPPLIER_DESC | string | 供应商描述 |
| CSUPPLIER_NAME | string | 供应商全称 |
| CSUPPLIER_NO | string | 供应商编码 |
| CSUPPLIER_SHORT | string | 供应商简称 |
| CSUPPLIER_SHORT_NO | string | 供应商简称编码 |
| CSUPPLIER_TYPE_ID | Int64? | 供应商类型ID |
| CUSER | string | 联系人 |

### TBL_BD_TEMPLATE (模板信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CRULE_ID | long? | 条码规则ID |
| CTEMPLATE_GROUP_ID | long | 模板分组ID |
| CTEMPLATE_NAME | string | 模板名称 |
| CTEMPLATE_NO | string | 模板编码 |
| CTEMPLATE_PATH | string | 模板层级路径 |

### TBL_BD_TEMPLATE_GROUP (模板分组表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CTEMPLATE_GROUP_NAME | string | 模板分组名称 |
| CTEMPLATE_GROUP_NO | string | 模板分组编码 |

### TBL_BD_WC (工作中心表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CID | long | 主键ID |
| CIS_LINK_CONFIG | string | 是否已配置管控信息（Y已配置，N或空未配置） |
| CIS_LINK_TYPE | string | 是否已配置关联物料类别（Y已配置，N或空未配置） |
| CPARENT | long? | 上级工作中心ID |
| CWC_NAME | string | 工作中心名称 |
| CWC_NO | string | 工作中心编码 |
| CWC_TYPE | long? | 工作中心类型 |

### TBL_BD_WC_ITEMTYPE_LINK (工作中心关联模板)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_TYPE_ID | long? | 物料类型ID |
| CREMARK | string | 备注 |
| CWC_ID | long | 工作中心ID |

### TBL_BD_WC_PROCESS_LINK (工作中心与工序关系表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPROCESS_ID | long | 工序ID |
| CSEQ | int? | 工序顺序 |
| CWC_ID | long | 工作中心ID |

### TBL_MD_DATASET (数据集)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATASET_CONDITION | string | 数据集参数Json字符串 |
| CDATASET_TYPE | DataSetTypeEnum | 数据集类型（0:表,1:视图,2:自定义脚本,3:存储过程） |
| CDATASOURCE_ID | long | 数据源ID |
| CNAME | string | 数据集名称 |

---

## 消息推送模块

### TBL_MSG_EVENT (消息事件表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATASET_ID | long? | 数据集ID |
| CDESC | string | 描述 |
| CEXPRESSION | string | 表达式 |
| CFREQUENCY | long? | 频率(0:小时,1:每天,2:每周,3:每月) |
| CINDICAROR | string | 指标 |
| CMSG_GROUP_ID | long? | 消息群组ID |
| CRULE | string | 规则 |
| CSCHEDULE_TASK_ID | int? | 调度任务ID |
| CSEQ | int? | 序号 |
| CSTATUS | string | 达成状态 |
| CTARGET | string | 目标 |
| CTEMPLATE_ID | long? | 消息模板ID |

### TBL_MSG_GROUP (消息群组)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CGROUP_CODE | string | 群组编码 |
| CGROUP_DESC | string | 群组描述 |
| CGROUP_NAME | string | 群组名称 |
| CTHIRD_PARTY_PARAM | string | 第三方参数 |

### TBL_MSG_GROUP_USER (消息群组和用户)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CGROUP_ID | long | 群组ID |
| CUSER_ID | long | 用户ID |

### TBL_MSG_PUSH_FREQUENCY (预警频率配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDESC | string | 描述 |
| CSCHEDULE | string | 频率(Cron表达式) |
| CSEQ | int? | 序号 |

### TBL_MSG_ROBOT (推送机器人)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CROBOT_NAME | string | 机器人名称 |
| CROBOT_TYPE | string | 机器人类型 |
| CWEBHOOK_URL | string | 机器人Webhook地址 |

### TBL_MSG_ROBOT_EVENT_LINK (推送事件机器人关联)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CMSG_EVENT_ID | long? | 推送事件ID |
| CROBOT_ID | long? | 机器人ID |

### TBL_MSG_SEND_LOG (消息发送日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CACCEPT_DATETIME | DateTime? | 接收日期 |
| CCLOSE_DATETIME | DateTime? | 关闭日期 |
| CCONFIRM_DATETIME | DateTime? | 确认日期 |
| CDELETE_DATETIME | DateTime? | 删除日期 |
| CMSG_CONTENT | string | 消息内容 |
| CREMARK | string | 备注 |
| CSEND_DATETIME | DateTime? | 发送日期 |
| CSEND_TYPE | string | 发送类型 |
| CSTATUS | int? | 状态 |
| CUSER_ID | string | 处理人 |

### TBL_MSG_TEMPLATE (消息模板)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCODE | string | 模板编码 |
| CCONTENT | string | 正文 |
| CPARAMS | string | 模板参数(JSON) |
| CSUB_TITLE | string | 子标题 |
| CTEMPLATE_TYPE | string | 消息类型(1:企业微信,2:钉钉,3:Email) |
| CTITLE | string | 标题 |

### TBL_MSG_USER (消息推送用户)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CACCOUNT | string | 账号 |
| CUSER_ID | long? | 用户表ID |
| CUSER_NAME | string | 姓名 |
| CUSER_TYPE | string | 类型 |

---

## 设备联机模块

### TBL_ABNORMAL_DATA_POOL (锁机锁卡异常数据表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CABNORMAL_TYPE | string | 异常类型 |
| CDEVICE_NAME | string | 设备名(可空) |
| CFOREIGN_KEY_ID | long? | 外键ID |
| CFOREIGN_TABLE | string | 外键对应的表 |
| CIDENTIFY_FIELD | string | 校验识别字段 |
| CREMARK | string | 备注 |
| CTEMPLATE_ITEM_NAME | string | 模板项目名(可空) |
| CTEMPLATE_NAME | string | 模板名(可空) |

### TBL_DEVICE_SPEED_PARAMS (设备速度参数配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_ID | int | 设备ID |
| CDEVICE_NAME | string | 设备名称 |
| CSPEED | decimal? | 速度参数值 |
| CTAG_ID | int? | 测点ID |
| CTAG_NAME | string | 测点名称 |

### TBL_EAP_ALARM (设备报警记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_LEVEL | int? | 报警等级 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CEND_TIME | DateTime? | 报警结束时间 |
| CERROR_ID | int? | 报警类型ID |
| CERROR_MESSAGE | string | 报警信息 |
| CERROR_NO | string | 报警编码 |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CLOT_NO | string | 批次号 |
| CORDER_NO | string | 工单号 |
| CSTART_TIME | DateTime? | 报警开始时间 |
| CUSER_CREATED | string | 创建人 |

### TBL_EAP_AOI_DETECTIONS (AOI或者VRS数据主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 板码 |
| CBRAND | string | 品牌 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CLAYER | string | 层别 |
| CLOT_NO | string | 批次号 |
| CMAP_ITEM_NO | string | 映射料号 |
| CORDER_NO | string | 工单号 |
| CPRINT_CODE | string | 印码 |
| CRESULT | string | 检测结果 |
| CTEST_END_TIME | DateTime? | 测试结束时间 |
| CTEST_START_TIME | DateTime? | 测试开始时间 |
| CTEST_TIME | string | 检测时间 |
| CTOTAL_QTY | int? | 总数量 |
| CUSER_CREATED | string | 创建人 |

### TBL_EAP_AOI_DETECTIONS_DTL (AOI或VRS状态明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEFECT_NO | string | 缺陷编号 |
| CDETECTION_ID | long | 主表ID |
| CID | long | 主键ID |
| CIMG_PATH | string | 图片路径 |
| CIS_FLAG | int? | 标记位 |
| CNG_CONTENT | string | NG内容 |
| CNG_NO | string | NG编号 |
| COORDINATE_X | string | X坐标 |
| COORDINATE_Y | string | Y坐标 |
| CPOSITION | string | 位置 |
| CSERVER_IMG_PATH | string? | 服务器上图片路径 |

### TBL_EAP_API_RECORDS (联机API调用记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATA_ID | string | 数据主键ID |
| CDATA_TYPE | string | 数据类型（如 GET/POST） |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_NAME | string | 设备名称 |
| CID | long | 主键ID |
| CINTERFACE | string | 接口地址 |
| CINTERFACE_NAME | string | 接口名称 |
| CREMARK | string | 备注 |
| CREQUEST | string | 请求报文 |
| CRESPONSE | string | 响应报文 |
| CSERVER_ID | string | 服务器标识 |

### TBL_EAP_AUTO_PULL_MACHINE (放板机状态监控表，两分钟更新一次)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_MODIFIED | DateTime | 修改时间 |
| CID | long |  |
| CIS_BOARD | string | 是否有板 |
| CIS_MES_MODEL | string | 是否MES模式 |
| CIS_ONLINE | string | 是否在线 |
| CIS_RUN | string | 是否运行 |
| CPULL_MACHINE_NAME | string | 放板机名称 |
| CPULL_MACHINE_NO | string | 放板机编号（后面加"-放板机"为配置的DEVICE_NAME） |

### TBL_EAP_BT_PARAM (班通参数主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_NO | string | 料号 |
| CLAYER_NAME | string | 层别名称 |
| CPART_NUM | string | 制造部件 |
| CPROCESS | string | 工序 |

### TBL_EAP_BT_PARAM_DTL (班通参数明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATA_TYPE | string | 数据类型 |
| CMAIN_ID | long | 主表ID |
| CMAX_VALUE | decimal? | 最大值 |
| CMEASURE_ITEM_NAME | string | 测量项目名称 |
| CMEASURE_TYPE | string | 测量类型 |
| CMIN_VALUE | decimal? | 最小值 |
| CSTAND_VALUE | decimal? | 标准值 |

### TBL_EAP_CURRENT_DATA (联机测点TAG实时状态表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDEVICE_NAME | string | 设备名称 |
| CDEVICE_SERIAL | int | 设备序号 |
| CDT | DateTime? | 数据时间 |
| CSERVER_SERIAL | int | 服务器序号 |
| CTAG_ID | int | 测点ID（关联测点配置）, 对应TBL_EAP_TAG.CTAG_ID |
| CTAG_NAME | string | 测点名称 |
| CTYPE | string | 数据类型 |
| CVALUE | float? | 数值 |
| CVALUE_STRING | string | 字符串值 |
| CVALUE_TYPE | int | 值类型 |

### TBL_EAP_DATA (EAP采集数据表)
> **注意**：现场库与文档**列名/列集合常不一致**（`CID`、`CDT`、`CTYPE`、`CVALUE_TYPE`、`CVALUE_STRING`、`CSERVER_ID`、`CVALUE` 等易 **207**）。**首查请用** `SELECT TOP (100) * FROM dbo.TBL_EAP_DATA`，再以 `INFORMATION_SCHEMA.COLUMNS` 为准。

| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDT | DateTime | 数据时间（库中常无） |
| CID | long | 主键ID（库中列名可能非 CID） |
| CSERVER_ID | int | 服务器ID |
| CTAG_ID | int | 测点ID（关联测点配置）, 对应TBL_EAP_TAG.CTAG_ID |
| CTYPE | string | 数据类型（库中常无此列名） |
| CVALUE | float? | 数值（库中可能无或列名不同） |
| CVALUE_STRING | string | 字符串值（**库中常无此列名**，易 207） |
| CVALUE_TYPE | int | 值类型（库中常无或与文档不一致） |

### TBL_EAP_DATA_CONTENT (EAP数据内容记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUR_DATE | DateTime | 当前时间 |
| CDATA | string | 数据内容 |
| CDATA_ID | string | 数据ID |
| CDATA_TYPE | string | 数据类型 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE | string | 设备标识 |
| CID | long | 主键ID |
| CREMARK | string | 备注 |
| CSERVER | string | 服务器标识 |

### TBL_EAP_DATA_YYYYMM (联机数据测点采集信息表(分表))
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? |  |
| CDEVICE_ID | int? |  |
| CDT | DateTime? |  |
| CID | long |  |
| CSERVER_ID | int? |  |
| CTAG_ID | int? | 测点ID（关联测点配置）, 对应TBL_EAP_TAG.CTAG_ID |
| CTYPE | string |  |
| CVALUE | float? |  |
| CVALUE_STRING | string |  |
| CVALUE_TYPE | byte? |  |

### TBL_EAP_DEVICE (联机设备列表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CADDRESS | string | 设备地址 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime | 修改时间 |
| CDEVICE_ID | int | 设备编号 |
| CDEVICE_NAME | string | 设备名称 |
| CDEVICE_SERIAL | int | 设备序号 |
| CID | long | 主键ID |
| CIP | string | 设备IP |
| CLOT | string | 当前批次号 |
| COEE | decimal? | OEE指标 |
| CPORT | int? | 设备端口 |
| CPRODUCT | string | 当前产品信息 |
| CREMARK | string | 备注 |
| CSERVER_SERIAL | int | 服务器序号 |
| CSTATUS | int | 设备状态码 |
| CSTATUS_TIME | DateTime | 状态更新时间 |

### TBL_EAP_GE_PARAM (今明图电参数)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAREA_C | decimal | C面积 |
| CAREA_S | decimal | S面积 |
| CCU_DEN | decimal | 铜密度 |
| CCU_TIME | int | 铜时间 |
| CFB | string | A/B挂 |
| CITEM_NO | string | 料号 |
| CPARAM_STATUS | string | 参数状态  => 试板参数: TESTPLATE   生产参数: PRODUCTION |
| CPART_NUM | string | 制造部件 |
| CREMARK | string | 备注 |
| CSN_DEN | decimal | 锡密度 |
| CSN_TIME | int | 锡时间 |
| CSTATUS | int | 状态 |
| CUSE_COUNT | int? | 使用次数 |

### TBL_EAP_GE_PARAM_CHANGE_LOG (图电参数变更记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAAREA_C | decimal | 变更后C面积 |
| CAAREA_S | decimal | 变更后S面积 |
| CACU_DEN | decimal | 变更后铜密度 |
| CACU_TIME | int | 变更后铜时间 |
| CASN_DEN | decimal | 变更后锡密度 |
| CASN_TIME | int | 变更后锡时间 |
| CBAREA_C | decimal? | 变更前C面积 |
| CBAREA_S | decimal? | 变更前S面积 |
| CBCU_DEN | decimal? | 变更前铜密度 |
| CBCU_TIME | int? | 变更前铜时间 |
| CBSN_DEN | decimal? | 变更前锡密度 |
| CBSN_TIME | int? | 变更前锡时间 |
| CPARAMS_ID | long | 参数主表ID（TBL_EAP_GE_PARAM.CID） |

### TBL_EAP_GE_PARAM_USE_LOG (图电参数下发记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CMACHINE_NAME | string | 机台名称 |
| CPARAMS_ID | long | 参数主表ID |
| CWO | string | 工单号 |

### TBL_EAP_GOLD_NICKEL_TESTER_RECORD (金镍测试仪上传数据主表，沉金)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAU_AVG | decimal? | 金含量平均值 |
| CAU_CV | decimal | 金含量变异系数 |
| CAU_DEVIATION | decimal? | 金含量偏差 |
| CAU_MAX_VALUE | decimal? | 金含量最大值 |
| CAU_MIN_VALUE | decimal? | 金含量最小值 |
| CAU_RANGE | decimal? | 金含量范围 |
| CFILE_NAME | string | 文件名 |
| CIMG_1 | string? | 图片1 |
| CIMG_2 | string? | 图片2 |
| CITEM | string | 项目 |
| CMACHINE_TIME | DateTime? | 机器时间 |
| CNI_AVG | decimal? | 镍含量平均值 |
| CNI_CV | decimal? | 镍含量变异系数 |
| CNI_DEVIATION | decimal? | 镍含量偏差 |
| CNI_MAX_VALUE | decimal? | 镍含量最大值 |
| CNI_MIN_VALUE | decimal? | 镍含量最小值 |
| CNI_RANGE | decimal? | 镍含量范围 |
| COPERATOR | string | 操作员 |
| CPROCESS_NAME | string | 过程名称 |
| CPROGRAM_NAME | string | 程序名称 |
| CSAMPLE_NAME | string | 样品名称 |
| CSAMPLE_NO | string | 样品编号 |

### TBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL (金镍测试仪上传数据明细表，沉金)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAU_VALUE | decimal? | 金测量值 |
| CNI_VALUE | decimal? | 镍测量值 |
| CRECORD_ID | long | 主表ID |
| CSEQ | int? | 序号 |

### TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN (金镍测试仪主表，沉锡)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFILE_NAME | string | 文件名 |
| CIMG_1 | string? | 图片1 |
| CIMG_2 | string? | 图片2 |
| CITEM | string | 项目 |
| CMACHINE_TIME | DateTime? | 机器时间 |
| COPERATOR | string | 操作员 |
| CPROCESS_NAME | string | 过程名称 |
| CPROGRAM_NAME | string | 程序名称 |
| CSAMPLE_NAME | string | 样品名称 |
| CSAMPLE_NO | string | 样品编号 |
| CSN_AVG | decimal? | 锡含量平均值 |
| CSN_CV | decimal | 锡含量变异系数 |
| CSN_DEVIATION | decimal? | 锡含量偏差 |
| CSN_MAX_VALUE | decimal? | 锡含量最大值 |
| CSN_MIN_VALUE | decimal? | 锡含量最小值 |
| CSN_RANGE | decimal? | 锡含量范围 |

### TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL (金镍测试仪明细表，沉锡)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CRECORD_ID | long | 主表ID |
| CSEQ | int? | 序号 |
| CSN_VALUE | decimal? | 锡测量值 |

### TBL_EAP_HAOS_PARAM (浩硕打靶机参数)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间（datetime类型，允许为空） |
| CDATETIME_MODIFIED | DateTime? | 修改时间（datetime类型，允许为空） |
| CDistA1A2 | decimal? | AIA2靶距（decimal类型，精度18位，小数位6位，允许为空） |
| CDistA1B1 | decimal? | AIB1靶距（decimal类型，精度18位，小数位6位，允许为空） |
| CDistA1C1_X | decimal? | A1C1 X距离（decimal类型，精度18位，小数位6位，允许为空） |
| CDistA1C1_Y | decimal? | A1C1 Y距离（decimal类型，精度18位，小数位6位，允许为空） |
| CDistC1C2 | decimal? | CIC2靶距（decimal类型，精度18位，小数位6位，允许为空） |
| CDistC1D1 | decimal? | CID1靶距（decimal类型，精度18位，小数位6位，允许为空） |
| CDrillstyle | string | 钻靶型式（varchar类型，长度50，允许为空） |
| CENTERPRISE_CODE | long? | 企业编码（bigint类型，允许为空） |
| CFrontToA1A2 | decimal? | AIA2至板前缘（decimal类型，精度18位，小数位6位，允许为空） |
| CID | long |  |
| CINSTANCE_ID | string | 实例ID（varchar类型，长度256，允许为空） |
| CJobname | string | 料号（varchar类型，长度50，允许为空） |
| CLength | decimal? | 板长（decimal类型，精度18位，小数位6位，允许为空） |
| CLot_NO | string | 批次号（varchar类型，长度256，不允许为空） |
| CORG_CODE | long? | 组织编码（bigint类型，允许为空） |
| Count | int? | 数量（int类型，允许为空） |
| CRecipetime | string | 配方生成时间戳（varchar类型，长度50，允许为空） |
| CROWREMARK | string | 行备注（varchar(max)类型，允许为空，可存储长文本） |
| CSTATE | string | 状态（char类型，长度1，允许为空） |
| CThickness | decimal? | 板厚（decimal类型，精度18位，小数位6位，允许为空） |
| CUSER_CREATED | string | 创建人（varchar类型，长度256，允许为空） |
| CUSER_MODIFIED | string | 修改人（varchar类型，长度256，允许为空） |
| CWidth | decimal? | 板宽（decimal类型，精度18位，小数位6位，允许为空） |

### TBL_EAP_HEARTBEAT (放板机心跳记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_NAME | string | 设备名称 |
| CLOGIN_USER | string | 登录用户 |
| CREMARK | string | 备注 |

### TBL_EAP_HEARTBEATS (心跳记录表，疑似弃用)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CHEARTBEAT_NUM | long | 心跳序号 |
| CID | long | 主键ID |

### TBL_EAP_HONGSHENG_RECORDS (宏胜裁磨机结批数据)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CID | long |  |
| CITEM_NO | string | 料号 |
| CLOT_IN_QTY | int? | 投入数量 |
| CLOT_NO | string | 批次号 |
| CLOT_OUT_QTY | int? | 产出数量 |
| CLOT_QTY | int? | 批次数量 |

### TBL_EAP_HONGSHENG_TM_RECORDS (宏胜测厚机测试数据)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| Average | string | 平均值 |
| CCOUNT | string | 计数值 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CID | long | 主键ID |
| Container | string | 容器号 |
| CopperLowerLimit | string | 铜厚下限 |
| CopperThickness | string | 铜厚测量值 |
| CopperUpperLimit | string | 铜厚上限 |
| CPERCENT | string | 百分比 |
| CTIME | string | 测量时间 |
| DeviceCode | string | 设备编码 |
| DeviceName | string | 设备名称 |
| DeviceStatus | string | 设备状态 |
| DivFact | string | 分度系数 |
| DownCuResult | string | 下铜判定结果 |
| JudgmentResults | string | 判定结果 |
| LeftPointA | string | 左侧A点测量值 |
| LeftPointB | string | 左侧B点测量值 |
| LeftPointC | string | 左侧C点测量值 |
| LeftPointD | string | 左侧D点测量值 |
| LowerCopper | string | 下铜厚测量值 |
| LowerCopperlowerlimit | string | 下铜厚下限 |
| LowerCopperupperlimit | string | 下铜厚上限 |
| LowerLimit | string | 板厚下限 |
| MACHINE_IP | string | 设备IP |
| MeanValue | string | 均值 |
| MethodName | string | 上报方法名 |
| MiddlePointA | string | 中间A点测量值 |
| MiddlePointB | string | 中间B点测量值 |
| MiddlePointC | string | 中间C点测量值 |
| MiddlePointD | string | 中间D点测量值 |
| PartNo | string | 料号 |
| RightPointA | string | 右侧A点测量值 |
| RightPointB | string | 右侧B点测量值 |
| RightPointC | string | 右侧C点测量值 |
| RightPointD | string | 右侧D点测量值 |
| Thickness | string | 板厚测量值 |
| UpCuResult | string | 上铜判定结果 |
| UpperLimit | string | 板厚上限 |

### TBL_EAP_HQ_PRESS_PRODUCTION (活全压机数据，每两分钟从Mysql采集)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_NO | string? | 设备编号 |
| CID | long |  |
| Job_No | string | 作业号 |
| Lot_No | string | 批次号 |
| Mat_Pcs | string | 板数 |
| Mat_Press_PV | string | 材料压力实测值 |
| Mat_Press_SV | string | 材料压力设定值 |
| Mat_Size_L | string | 物料长度 |
| Mat_Size_W | string | 物料宽度 |
| Now_Vacuum | string | 当前真空度 |
| Part_No | string | 料号 |
| PRESS_TPDIS_LYR01 | string | 层厚度偏差01 |
| PRESS_TPDIS_LYR02 | string | 层厚度偏差02 |
| PRESS_TPDIS_LYR03 | string | 层厚度偏差03 |
| PRESS_TPDIS_LYR04 | string | 层厚度偏差04 |
| PRESS_TPDIS_LYR05 | string | 层厚度偏差05 |
| PRESS_TPDIS_LYR06 | string | 层厚度偏差06 |
| PRESS_TPDIS_LYR07 | string | 层厚度偏差07 |
| PRESS_TPDIS_LYR08 | string | 层厚度偏差08 |
| PRESS_TPDIS_LYR09 | string | 层厚度偏差09 |
| PRESS_TPDIS_LYR10 | string | 层厚度偏差10 |
| PRESS_TPDIS_LYR11 | string | 层厚度偏差11 |
| PRESS_TPDIS_LYR12 | string | 层厚度偏差12 |
| PRESS_TPDIS_LYR13 | string | 层厚度偏差13 |
| PRESS_TPDIS_LYR14 | string | 层厚度偏差14 |
| PRESS_TPDIS_LYR15 | string | 层厚度偏差15 |
| PRESS_TPDIS_LYR16 | string | 层厚度偏差16 |
| PRESS_TPDIS_LYR17 | string | 层厚度偏差17 |
| PRESS_TPDIS_LYR18 | string | 层厚度偏差18 |
| PRESS_TPDIS_LYR19 | string | 层厚度偏差19 |
| PRESS_TPDIS_LYR20 | string | 层厚度偏差20 |
| PRESS_TPDIS_MAT01 | string | 材料厚度偏差01 |
| PRESS_TPDIS_MAT02 | string | 材料厚度偏差02 |
| PRESS_TPDIS_MAT03 | string | 材料厚度偏差03 |
| PRESS_TPDIS_MAT04 | string | 材料厚度偏差04 |
| PRESS_TPDIS_MAT05 | string | 材料厚度偏差05 |
| PRESS_TPDIS_MAT06 | string | 材料厚度偏差06 |
| PRESS_TPDIS_MAT07 | string | 材料厚度偏差07 |
| PRESS_TPDIS_MAT08 | string | 材料厚度偏差08 |
| PRESS_TPDIS_MAT09 | string | 材料厚度偏差09 |
| PRESS_TPDIS_MAT10 | string | 材料厚度偏差10 |
| PRESS_TPDIS_MAT11 | string | 材料厚度偏差11 |
| PRESS_TPDIS_MAT12 | string | 材料厚度偏差12 |
| Recipe_Name | string | 配方名称 |
| System_Press | string | 系统压力 |
| TEMP_AVG | string | 平均温度 |
| TEMP_SV | string | 温度设定值 |
| Time_Stamp | DateTime | 时间戳 |
| Time_Stamp_ms | int? | 时间戳毫秒 |

### TBL_EAP_HQ_PRESS_PRODUCTION_ONSUBMIT (活全压机生成记录，手动提交)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_NO | string? | 设备编号 |
| CID | long |  |
| Job_No | string | 作业号 |
| Lot_No | string | 批次号 |
| Mat_Pcs | string | 板数 |
| Mat_Press_PV | string | 材料压力实测值 |
| Mat_Press_SV | string | 材料压力设定值 |
| Mat_Size_L | string | 物料长度 |
| Mat_Size_W | string | 物料宽度 |
| Now_Vacuum | string | 当前真空度 |
| Part_No | string | 料号 |
| PRESS_TPDIS_LYR01 | string | 层厚度偏差01 |
| PRESS_TPDIS_LYR02 | string | 层厚度偏差02 |
| PRESS_TPDIS_LYR03 | string | 层厚度偏差03 |
| PRESS_TPDIS_LYR04 | string | 层厚度偏差04 |
| PRESS_TPDIS_LYR05 | string | 层厚度偏差05 |
| PRESS_TPDIS_LYR06 | string | 层厚度偏差06 |
| PRESS_TPDIS_LYR07 | string | 层厚度偏差07 |
| PRESS_TPDIS_LYR08 | string | 层厚度偏差08 |
| PRESS_TPDIS_LYR09 | string | 层厚度偏差09 |
| PRESS_TPDIS_LYR10 | string | 层厚度偏差10 |
| PRESS_TPDIS_LYR11 | string | 层厚度偏差11 |
| PRESS_TPDIS_LYR12 | string | 层厚度偏差12 |
| PRESS_TPDIS_LYR13 | string | 层厚度偏差13 |
| PRESS_TPDIS_LYR14 | string | 层厚度偏差14 |
| PRESS_TPDIS_LYR15 | string | 层厚度偏差15 |
| PRESS_TPDIS_LYR16 | string | 层厚度偏差16 |
| PRESS_TPDIS_LYR17 | string | 层厚度偏差17 |
| PRESS_TPDIS_LYR18 | string | 层厚度偏差18 |
| PRESS_TPDIS_LYR19 | string | 层厚度偏差19 |
| PRESS_TPDIS_LYR20 | string | 层厚度偏差20 |
| PRESS_TPDIS_MAT01 | string | 材料厚度偏差01 |
| PRESS_TPDIS_MAT02 | string | 材料厚度偏差02 |
| PRESS_TPDIS_MAT03 | string | 材料厚度偏差03 |
| PRESS_TPDIS_MAT04 | string | 材料厚度偏差04 |
| PRESS_TPDIS_MAT05 | string | 材料厚度偏差05 |
| PRESS_TPDIS_MAT06 | string | 材料厚度偏差06 |
| PRESS_TPDIS_MAT07 | string | 材料厚度偏差07 |
| PRESS_TPDIS_MAT08 | string | 材料厚度偏差08 |
| PRESS_TPDIS_MAT09 | string | 材料厚度偏差09 |
| PRESS_TPDIS_MAT10 | string | 材料厚度偏差10 |
| PRESS_TPDIS_MAT11 | string | 材料厚度偏差11 |
| PRESS_TPDIS_MAT12 | string | 材料厚度偏差12 |
| Recipe_Name | string | 配方名称 |
| System_Press | string | 系统压力 |
| TEMP_AVG | string | 平均温度 |
| TEMP_SV | string | 温度设定值 |
| Time_Stamp | DateTime? | 时间戳 |
| Time_Stamp_ms | int? | 时间戳毫秒 |

### TBL_EAP_LDI_JOB (LDI作业参数记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUR_DATE | DateTime? | 当前时间 |
| CHEIGHT | string | 板长 |
| CIS_COPPER | string | 是否含铜 |
| CITEM_NO | string | 产品型号 |
| CJOB_NAME | string? | 料号名称 |
| CLAYER_NAME_A | string | 层次 |
| CLAYER_NAME_B | string | 层次 |
| CLOT_NO | string? | 流程卡号 |
| CMACHINE_CODE | string? | 设备编号 |
| CMAKE_PART | string | 制造部件 |
| CORDER_NO | string? | 工单 |
| CPLATE | string | 板材铜厚 |
| CRESISNAME | string | 干膜 |
| CSCALE_X | string | 涨缩系数 |
| CSCALE_Y | string | 涨缩系数 |
| CSERIAL_NO | string? | 产品型号 |
| CTHICKNESS | string | 板厚 |
| CUSER_NAME | string? | 用户名称 |
| CWIDTH | string | 板宽 |

### TBL_EAP_LDI_LOG (LDI生产日志记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDRY_FILM | string | 干膜参数 |
| CEND_TIME | string | 结束时间 |
| CEXPOSURE | string | 曝光参数 |
| CFACE | string | 面别 |
| CFLOOR | string | 层别 |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CJOB_NAME | string | 作业名称 |
| CLAYER_NAME | string | 层名称 |
| CLOT_NO | string | 批次号 |
| CMACHINE_CODE | string | 设备代码 |
| CORDER_NO | string | 工单号 |
| CPE_THRESHOLD | string | PE阈值 |
| CSCALE_MODE | string | 缩放模式 |
| CSCALE_X | string | X方向缩放 |
| CSCALE_Y | string | Y方向缩放 |
| CSTART_TIME | string | 开始时间 |

### TBL_EAP_LDI_PARAM (LDI参数)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAB | string | AB板 |
| CBOARD_LENGTH | decimal? | 板长 |
| CBOARD_THICKNESS | decimal? | 板厚 |
| CBOARD_WIDTH | decimal? | 板宽 |
| CBOT_ALIGNMENT_LAYER | string | BOT对位层 |
| CBOT_LAYER | string | BOT层 |
| CCONTAINS_COPPER | string | 是否含铜 |
| CCOPPER_THICKNESS | string | 板材铜厚 |
| CDRY_FILM_NAME | string | 干膜名称 |
| CEXPANSION_X | decimal? | 涨缩系数X |
| CEXPANSION_Y | decimal? | 涨缩系数Y |
| CISSUED_MESSAGE | string | 下发失败消息 |
| CISSUED_RESULT | string | 下发结果 |
| CITEM_NO | string | 料号 |
| CPART_NUM | string | 制造部件 |
| CREMARK | string | 备注 |
| CSTATUS | int | 状态 |
| CTGZ_FILE_PATH | string | tgz文件地址 |
| CTOP_ALIGNMENT_LAYER | string | TOP对位层 |
| CTOP_LAYER | string | TOP层 |

### TBL_EAP_LWT_DETECTIONS (班通检测主记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDEVICE_NAME | string | 设备名称 |
| CID | long | 主键ID |
| CID_NO | string | 标识编号 |
| CITEM | string | 检测项目 |
| CLAYER | string | 层别 |
| CLOT_NO | string | 工单号 |
| CMAX_VALUE | decimal? | 最大值 |
| CMIN_VALUE | decimal? | 最小值 |
| CSTAND_VALUE | decimal? | 标准值 |

### TBL_EAP_LWT_DETECTIONS_DTL (班通检测明细记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CID | long | 主键ID |
| CIMAGE_DATA | string | 图片数据 |
| CIMAGE_NAME | string | 图片名称 |
| CIMAGE_PATH | string | 图片路径 |
| CIMAGE_SIZE | int? | 图片大小 |
| CIMAGE_TYPE | string | 图片类型 |
| CITEM | string | 检测项目 |
| CITEM_CODE | string | 项目编码 |
| CMAIN_ID | long | 主表ID |
| CMAX_VALUE | decimal? | 最大值 |
| CMIN_VALUE | decimal? | 最小值 |
| CNUMBER | string | 序号 |
| CREAL_VALUE | decimal? | 实测值 |
| CREMARK | string | 备注 |
| CRESULT | string | 检测结果 |
| CSTAND_VALUE | decimal? | 标准值 |

### TBL_EAP_MASON_DETECTIONS (麦逊检测结果主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOUNT | int | 上传记录数 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CID | long | 主键ID |
| CMACHINE_NO | string | 设备编码 |
| CUSER_NO | string? | 用户编号 |

### TBL_EAP_MASON_DETECTIONS_DTL (麦逊检测结果明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBATCH_NO | string | 批次号 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDETECT_DATE | DateTime | 检测时间 |
| CDETECT_RESULT | string | 检测结果 |
| CDETECT_STEP | string | 检测步骤 |
| CID | long | 主键ID |
| CIR | decimal | IR值 |
| CITEM_NO | string | 料号 |
| CLOT_NO | string | 工单号 |
| CMAIN_ID | long | 主表ID |
| CNG_MESSAGE | string | NG信息（坏点信息） |
| CNG_SEQ | string | NG序号 |
| CPCB_NO | string | PCB编号 |
| CQR_CODE | string | 二维码 |
| CRDSON | decimal | RDSON值 |
| CREMARK | string | 备注 |
| CTOTAL_POINT | int | 总测点数 |
| CWEB_STRUCT | string | 网结构 |

### TBL_EAP_MP_GROUP (测点组)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFREQUENCY | int? | 采集频率 |
| CGROUP_NAME | string | 组名称 |
| CMP_QTY | int | 测点数量 |

### TBL_EAP_MP_GROUP_DTL (测点组明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CGROUP_ID | long? | 组ID |
| CSERVER | string | 服务器 |
| CTAG_ID | int | 测点ID（关联测点配置）, 对应TBL_EAP_TAG.CTAG_ID |
| CTAG_NAME | string | 测点名称 |

### TBL_EAP_M_PARTOP (图电料号工艺参数表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CC_MJ | string | 电铜面积 |
| CCU_DENSITY | string | 电铜密度 |
| CCU_T | string | 电铜时间 |
| CNEWDATE | string | 更新时间字符串 |
| CPART_NAME | string | 料号名称 |
| CPART_OP | string | 制程工序 |
| CS_MJ | string | 电锡面积 |
| CSN_DENSITY | string | 电锡密度 |
| CSN_T | string | 电锡时间 |

### TBL_EAP_PATTERN_PLAT (图形电镀检测主记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOPPER_HOLE | double | 铜孔 |
| CCUSTOMER_NO | string | 客户代码 |
| CDAY | DateTime? | 日期 |
| CFILE_NAME | string | 文件名称 |
| CITEM_NO | string | 生产编号 |
| CPROCESS_ID | long? | 工序ID |
| CREMARK | string | 备注 |
| CRESULT | string? | 判定结果 |
| CRESULT_MIN | double | 结果最小值 |
| CSHIFFT | string? | 班次 |

### TBL_EAP_PATTERN_PLAT_ITEM (图形电镀检测明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPATTERN_PLAT_ID | long | 主表ID |
| CRESULT_DATA_1 | double? | 检测值1 |
| CRESULT_DATA_2 | double? | 检测值2 |
| CRESULT_DATA_3 | double? | 检测值3 |
| CRESULT_DATA_4 | double? | 检测值4 |
| CRESULT_DATA_5 | double? | 检测值5 |

### TBL_EAP_PERIOD (设备状态时段记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CEND_TIME | DateTime? | 时段结束时间 |
| CID | long | 主键ID |
| CIS_END | char | 是否已结束 |
| CSTART_TIME | DateTime | 时段开始时间 |
| CSTATUS | int | 状态码 |

### TBL_EAP_PMS_CONTENT (汉印喷印机内容配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCONTENT | string | 内容 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CLABEL_H | decimal? | 标签高度 |
| CLABEL_W | decimal? | 标签宽度 |
| CLAYER | string | 层别 |
| CPOSITION_CONTER_X | decimal? | 中心点X坐标 |
| CPOSITION_CONTER_Y | decimal? | 中心点Y坐标 |
| CPOSITION_X | decimal? | X坐标 |
| CPOSITION_Y | decimal? | Y坐标 |
| CREF_ID | string? | 关联编号 |
| CREMARK | string | 备注 |

### TBL_EAP_PMS_PROD (汉印生产记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CFACE | string | 面别 |
| CID | long | 主键ID |
| CPNL_CODE | string | PNL条码 |
| CRESULT | string | 结果 |
| CWON | string | 工单号 |

### TBL_EAP_PMS_PROD_DTL (汉印生产记录明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCONTENT | string | 内容 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CID | long | 主键ID |
| CPROD_ID | long? | 主表ID |
| CREF_ID | int | 关联编号 |

### TBL_EAP_SHOOT_ITEM (打靶结果明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME | DateTime | 生产时间 |
| CDAY | string | 日期 |
| CFILE_NAME | string | 文件名称 |
| CFILE_PATH | string | 文件路径 |
| CITEM_NO | string | 产品料号 |
| CREMARK | string | 备注 |
| CRESULT_X | string | X坐标结果 |
| CRESULT_Y | string | Y坐标结果 |
| CSEQ | int | 序号 |
| CTIME | string | 时间 |
| CWC_CODE | string | 机型 |
| CXCOORDINAT | double | X坐标 |
| CYCOORDINAT | double | Y坐标 |

### TBL_EAP_SHUTDOWN_RECORD (放板机关机记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_NAME | string | 设备名称 |
| CLOGIN_USER | string | 登录用户 |
| CMSG | string | 消息内容 |
| CMSG_TYPE | string | 消息类型 |
| CREMARK | string | 备注 |

### TBL_EAP_STATUS (设备状态采集记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDURATION | decimal | 持续时长 |
| CEXTRA | string | 扩展信息 |
| CFILE_NAME | string | 来源文件名 |
| CITEM_NO | string | 料号 |
| CLOT | string | 批次号 |
| CMACHINE_NAME | string | 设备名称 |
| CMACHINE_TIME | DateTime | 设备时间 |
| CMACHINE_USER | string | 操作用户 |
| CMANUAL_STATUS | int | 手动状态码 |
| COEE | decimal | OEE值 |
| CPROGRESS | decimal | 进度 |
| CQTY | decimal | 数量 |
| CREMARK | string | 备注 |
| CSTATUS | int | 状态码 |
| CSTATUS_START_TIME | DateTime | 状态开始时间 |
| CTEXT | string | 文本内容 |
| CUNIT_STATUS | string | 机台状态文本 |
| CVERSION | string | 版本 |

### TBL_EAP_TAG (测点配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDEVICE_NAME | string | 设备描述 |
| CDEVICE_SERIAL | short? | 设备序号 |
| CENTERPRISE_CODE | string | 企业编码 |
| CGROUP_NAME | string | 类别名称 |
| CGROUP_SERIAL | short | 类别序号 |
| CID | long | 主键ID |
| CINSTANCE_ID | string | 实例ID |
| CMAX_VALUE | decimal? | 最大值 |
| CMIN_VALUE | decimal? | 最小值 |
| CORG_CODE | string | 组织编码 |
| CRADIX | int | 进制 |
| CROWREMARK | string | 行备注 |
| CSEQ | int | 排序号 |
| CSERVER_ID | string | 服务器ID |
| CSERVER_NAME | string | 服务器名称 |
| CSERVER_SERIAL | int | 服务器序号 |
| CSHOW_TYPE | string | 显示类型 |
| CSTATE | char | 数据状态 |
| CTAG_ALIAS | string | 参数别名 |
| CTAG_DESC | string | 参数描述 |
| CTAG_ID | int | 测点ID（关联测点配置）, 对应TBL_EAP_TAG.CTAG_ID |
| CTAG_NAME | string | 参数集名称 |
| CTAG_PATH | string | 参数路径 |
| CTAG_SERIAL | short | 测点序号 |
| CUNIT | string | 单位 |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |

### TBL_EAP_THREE_D_DATA (三次元数据)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CA | decimal? | A参数 |
| CAVERAGE_VALUE | double? | 平均值 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime | 修改时间 |
| CDAY | DateTime? | 日期 |
| CDEVIATION | decimal? | 标准差 |
| CID | long | 主键ID |
| CITEM | string | 项目名称 |
| CLOW_TOLERANCE | double | 下公差 |
| CMAX_VALUE | decimal? | 最大值 |
| CMEASURE_VALUE | double | 测量值 |
| CMIN_VALUE | decimal? | 最小值 |
| CMISCOUNT | double | 误差 |
| CP | decimal? | 过程能力指数P |
| CPK | decimal? | 过程能力指数CPK |
| CRECORD_ID | long | 记录ID |
| CRESULT | string | 判定 |
| CSAMPLE_COUNT | int? | 样本大小 |
| CSHIFFT | string? | 班次 |
| CSTANDARD | double | 标准值 |
| CTYPE | string | 型式 |
| CUNIT | string | 单位 |
| CUP_TOLERANCE | double | 上公差 |
| CUSER_CREATED | string | 创建人 |
| CUSER_MODIFIED | string | 修改人 |

### TBL_EAP_THREE_D_ITEM (三次元数据明细)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDAY | DateTime? | 日期 |
| CDEVICE_ID | long | 项目分组ID |
| CDEVICE_NAME | string | 项目名称 |
| CDEVICE_SEQ | int | 项目序号 |
| CFILE_NAME | string | 文件路径 |
| CFLAG | int? | 标记位 |
| CLOW_TOLERANCE | double | 下公差 |
| CMEASURE_VALUE | double | 测量值 |
| CMISCOUNT | double | 误差 |
| CRESULT | string | 判定 |
| CSHIFFT | string? | 班次 |
| CSTANDARD | double | 标准值 |
| CUP_TOLERANCE | double | 上公差 |

### TBL_EAP_THREE_D_RECORD (三次元文件记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDATETIME_MODIFIED | DateTime | 修改时间 |
| CDAY | DateTime? | 日期 |
| CFILE_NAME | string | 文件路径 |
| CID | long | 主键ID |
| CPROCESS_ID | long? | 工序ID |
| CSHIFFT | string? | 班次 |
| CUSER_CREATED | string | 创建人 |
| CUSER_MODIFIED | string | 修改人 |

### TBL_EAP_TIME_RANGE_CONTROL (放板机时间范围管控)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CEND_TIME | TimeSpan? | 结束时间 |
| CFREQUENCY | string | 生效频率 |
| CPARENT_DEVICE | string | 父设备标识 |
| CSTART_TIME | TimeSpan? | 开始时间 |

### TBL_EAP_T_ALARM (报警记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| C_ID | int | 报警ID |
| CALARM | string | 报警内容 |
| CCLEAR_DATE | DateTime | 清除时间 |
| COCCUR_DATE | DateTime | 发生时间 |

### TBL_EAP_T_OPERATION (操作记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| COPERATION_AUTHOR | string | 操作人 |
| COPERATION_CONTENT | string | 操作内容 |
| COPERATION_DATE | DateTime | 操作时间 |
| COPERATION_TYPE | string | 操作类型 |

### TBL_EAP_T_OPERATION2 (操作记录表（扩展）)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| COPERATION_AUTHOR | string | 操作人 |
| COPERATION_CONTENT | string | 操作内容 |
| COPERATION_DATE | DateTime | 操作时间 |
| COPERATION_TYPE | string | 操作类型 |

### TBL_EAP_T_OUT_HISTORY (图电出板历史记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| C10T | string | 10#时间 |
| C11T | string | 11#时间 |
| C12T | string | 12#时间 |
| C1T | string | 1#时间 |
| C2T | string | 2#时间 |
| C3T | string | 3#时间 |
| C4T | string | 4#时间 |
| C5T | string | 5#时间 |
| C6T | string | 6#时间 |
| C7T | string | 7#时间 |
| C8T | string | 8#时间 |
| C9T | string | 9#时间 |
| CCUCAH_A | string | 电铜C-AH |
| CCUNO | string | 电铜槽号 |
| CCUPT_A | string | 电铜时间 |
| CCUSAH_A | string | 电铜S-AH |
| CCUST_A | string | 电铜设时 |
| CFB_NO | string | 飞靶编号 |
| CINLOAD_TIME | string | 上板时间 |
| CPART_AB | string | A/B靶 |
| CPART_NAMEA | string | 电锡料号 |
| CPART_SUMA | string | 电锡数量 |
| CSNCAH_A | string | 电锡C-AH |
| CSNNO | string | 电锡槽号 |
| CSNPT_A | string | 电锡时间 |
| CSNSAH_A | string | 电锡S-AH |
| CSNST_A | string | 电锡设时 |
| CUNLOAD_TIME | string | 下板时间 |

### TBL_EAP_WHC (文坦验孔机主记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBATCH | string | 批次 |
| CBATCH_TYPE | string | 批次类型 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDEVICE_NAME | string | 设备名称 |
| CEXTEND_DATA | string | 扩展数据 |
| CID | long | 主键ID |
| COPERATOR_NAME | string | 操作员 |
| CREMARK | string | 备注 |
| CREQUEST_ID | string | 请求ID |
| CSERVICE_NAME | string | 服务名称 |
| CTIME_STAMP | DateTime | 时间戳 |

### TBL_EAP_WHC_DTL (文坦验孔机明细记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CID | long | 主键ID |
| CMACHINE_TIME | DateTime | 设备时间 |
| CSERVER_ID | int | 服务器ID |
| CTYPE | string | 数据类型 |
| CVALUE | float? | 数值 |
| CVALUE_STRING | string | 字符串值 |
| CVALUE_TYPE | int? | 值类型 |
| CWHC_ID | long | 主表ID |

### TBL_EAP_YUHUI_TEST_RECORDS (誉汇测试记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBOARD_COUNT | int | 板数量 |
| CBOARD_TYPE | string | 板类型 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CDEVICE_NAME | string | 设备名称 |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CORDER_NO | string | 工单号 |
| CTEST_TIME | DateTime? | 检测时间 |

### TBL_EAP_YUHUI_TEST_RECORDS_DTL (誉汇测试记录明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAREA | string | 区域 |
| CBOARD_SEQ | string | 板序号 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDOWN_BOUND | decimal? | 下限 |
| CERR_VALUE | decimal? | 误差值 |
| CID | long | 主键ID |
| CINNER_SEQ | int? | 板内序号 |
| CITEM | string | 量测项目 |
| CITEM_TYPE | string | 项目类型 |
| CMAIN_ID | long | 主表ID |
| CN_TOL | decimal? | 负公差 |
| CP_TOL | decimal? | 正公差 |
| CPOSITION_END | string | 结束位置 |
| CPOSITION_START | string | 起始位置 |
| CREAL_VALUE | decimal? | 实测值 |
| CRESULT | string | 检测结果 |
| CSTAND_VALUE | decimal? | 标准值 |
| CUNIT | string | 单位 |
| CUP_BOUND | decimal? | 上限 |

### TBL_EAP_YULIGHT_DETECTIONS_PCS (宇之光生产记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CEND_TIME | DateTime | 结束时间 |
| CFILENAME | string | 文件名 |
| CFROM_TICKET | string | 来源票号 |
| CID | long | 主键ID |
| CIS_REPAIR | int | 是否返修 |
| COPENCUT | int | 开路数量 |
| CPCS_ID | string | PCS编号 |
| CPNL_ID | string | PNL编号 |
| CRESULT | int | 检测结果 |
| CSHORTCUT | int | 短路数量 |
| CSTART_TIME | DateTime | 开始时间 |

### TBL_EAP_YULIGHT_DETECTIONS_PNL (宇之光PNL检测记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CADJAENCY | int | 邻接短路数 |
| CDATETIME_CREATED | DateTime | 创建时间 |
| CDEVICE_ID | int | 设备ID， 对应TBL_EAP_DEVICE.CDEVICE_ID |
| CEND_TIME | DateTime | 结束时间 |
| CFILENAME | string | 文件名 |
| CFROM_TICKET | string | 来源票号 |
| CHEIGHT | string | 高度 |
| CID | long | 主键ID |
| CIS_ABORT | int | 是否中止 |
| CIS_REPAIR | int | 是否返修 |
| CPCS_COUNT | int | PCS总数 |
| CPCS_NG | int | PCS不良数 |
| CPCS_OK | int | PCS良品数 |
| CPNL_ID | string | PNL编号 |
| CRESULT | string | 检测结果 |
| CSTART_TIME | DateTime | 开始时间 |
| CTEST_POINTS | int | 测试点数 |
| CTOTAL_NETS | int | 总网络数 |
| CWIDTH | string | 宽度 |

### TBL_HAOSHUO_TASK_RESULT (浩硕设备任务回传结果表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCODE | string | 结果代码 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID |
| CID | long | 唯一标识 |
| CJOB_NAME | string | 任务名称 |
| CLOT_ID | string | 批次ID |
| CMACH_CODE | string | 设备代码 |
| CMESSAGE | string | 结果消息 |
| CWO | string | 工单号 |

### TBL_HPL_SEND_LOG (水平线参数下发接口发送日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_NAME | string | 设备名称 |
| CPARAMS | string | 发送参数 |
| CREMARK | string | 备注 |
| CRESULT | string | 返回结果 |
| CWONUMBER | string | 工单号 |

### TBL_JINMING_TASK_RESULT (今明设备任务回传结果表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCODE | string | 结果代码 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDEVICE_ID | int? | 设备ID |
| CID | long | 唯一标识 |
| CJOB_NAME | string | 任务名称 |
| CLOT_ID | string | 批次ID |
| CMACH_CODE | string | 设备代码 |
| CMESSAGE | string | 结果消息 |
| CWO | string | 工单号 |

### TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD (浩硕生产记录实体类)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 板边码 |
| CDEFECTS | string | XY明细坐标 |
| CID | long | 主键ID |
| CITEM_NO | string | 料号 |
| CLOT_NO | string? | 工单 |
| CMACHINE_CODE | string | 设备代码 |
| CPRODUCTION_END_TIME | string | 打靶完成时间 |
| CPRODUCTION_START_TIME | string | 开始打靶时间 |
| CUSER_CREATED | string | 人员 |

### TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL (浩硕图形电镀生产记录明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCORDINATE_X | string | X涨缩 |
| CCORDINATE_Y | string | Y涨缩 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDETECTION_ID | long | 主表CID（TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD） |
| CID | long | 主键ID |
| CMACHINE_CODE | string | 设备代码 |
| CRESULT | string | 判定结果 |
| CSTAN_X | decimal? | X标准值 |
| CSTAN_Y | decimal? | Y标准值 |
| DISTANCE_X | string | X坐标 |
| DISTANCE_Y | string | Y坐标 |

### TBL_PATTERN_PLATING_PRODUCTION_RECORD (图电生产记录实体类)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| A_B_TARGET | string | A/B靶 |
| ACID_1_TIME | string | 酸1时间 |
| ACID_2_TIME | string | 酸2时间 |
| BOARD_COUNT | int? | 板数 |
| CID | long | 主键ID |
| COPPER_ELECTROLYSIS_C_AH | string | 电铜C-AH |
| COPPER_ELECTROLYSIS_S_AH | string | 电铜S-AH |
| COPPER_ELECTROLYSIS_SETTING_TIME | string | 电铜设时 |
| COPPER_ELECTROLYSIS_TANK | string | 电铜槽 |
| COPPER_ELECTROLYSIS_TIME | string | 电铜时间 |
| CREATION_TIME | DateTime | 创建时间 |
| DEGREASING_TIME | string | 除油时间 |
| FLYING_TARGET_SERIAL_NUMBER | string | 飞靶流水号 |
| LOADING_TIME | string | 上板时间 |
| MACH_CODE | string | 设备代码 |
| MATERIAL_NUMBER | string | 料号 |
| MICROETCHING_TIME | string | 微蚀时间 |
| TIN_ELECTROLYSIS_C_AH | string | 电锡C-AH |
| TIN_ELECTROLYSIS_S_AH | string | 电锡S-AH |
| TIN_ELECTROLYSIS_SETTING_TIME | string | 电锡设时 |
| TIN_ELECTROLYSIS_TANK | string | 电锡槽 |
| TIN_ELECTROLYSIS_TIME | string | 电锡时间 |
| UNLOADING_TIME | string | 下板时间 |
| WATER_WASH_TIME_14 | string | 14#水洗时间 |
| WATER_WASH_TIME_15 | string | 15#水洗时间 |
| WATER_WASH_TIME_17 | string | 17#水洗时间 |
| WATER_WASH_TIME_18 | string | 18#水洗时间 |
| WATER_WASH_TIME_19 | string | 19#水洗时间 |
| WATER_WASH_TIME_20 | string | 20#水洗时间 |
| WATER_WASH_TIME_8 | string | 8#水洗时间 |
| WATER_WASH_TIME_9 | string | 9#水洗时间 |

---

## 品质管理模块

### TBL_QM_ASSAY_LOG (化验任务记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CASSAY_RESULT | int | 化验结果：1正常、2异常 |
| CASSAY_STATUS | int | 化验状态 |
| CASSAY_TIME | DateTime? | 化验时间 |
| CASSAY_USER | string | 化验人 |
| CBASE_TASK_NO | string | 基础任务编号 |
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_STATUS | int | 审核状态 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER | string | 审核人 |
| CIS_OPEN_LINE | string | 是否开线前分析 |
| CMEDICINE_TANK_ID | long | 药缸ID |
| CRECEIVE_TIME | DateTime? | 接收时间 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CSAMPLE_BARCODE | string | 样品条码 |
| CSAMPLE_REMARK | string | 取样备注 |
| CSAMPLE_TIME | DateTime? | 取样时间 |
| CSAMPLE_USER | string | 取样人 |
| CSHIFT | string | 班次 |
| CTASK_NO | string | 任务编号 |
| CTASK_STAND_TIME_E | DateTime? | 任务标准结束时间 |
| CTASK_STAND_TIME_S | DateTime? | 任务标准开始时间 |
| CTASK_STATUS | int | 任务状态 |
| CTASK_TAG | string | 任务标签 |
| CTASK_TYPE | int | 任务类型 |
| CTEMPLATE_ID | long | 模板ID |
| CWC_ID | long | 工作中心ID |

### TBL_QM_ASSAY_LOG_ITEM (化验任务明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警值上限 |
| CALARM_MIN_VALUE | decimal? | 预警值下限 |
| CASSAY_LOG_ID | long | 化验主表ID |
| CCHECK_CONTENT | long? | 校验内容ID |
| CCHECK_WAY | int? | 校验方式 |
| CCORRECTIVE_ACTION | string | 纠正措施 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CEND_VALUE | string | 终值 |
| CENTERPRISE_CODE | long? | 企业代码 |
| CFORMULA | string | 补加量公式 |
| CID | long | 主键ID |
| CINPUT_FORMULA | string | 结果值计算公式 |
| CINPUT_TYPE | int? | 录入框类型 |
| CINPUT_VALUE | string? | 录入值 |
| CINSTANCE_ID | string | 实例ID |
| CIS_CHECK_RESULT | string | 是否校验 |
| CIS_CONFIRM | int? | 是否已确认添加 |
| CIS_MUST | string | 是否必填 |
| CITEM_FREQ_ID | long? | 任务频率ID |
| CLIST_SOURCE | string | 下拉框数据源 |
| CLIST_SOURCE_TYPE | int? | 下拉框数据源类型 |
| CORG_CODE | long? | 组织代码 |
| CPROCESS_INFO | string | 原因分析 |
| CREMARK | string | 备注 |
| CREPLENISHMENT | string | 补加量 |
| CRESULT | int? | 结果：0不合格、1合格 |
| CRETEST_RESULT | int? | 复测结果 |
| CRETEST_TIME | DateTime? | 复测时间 |
| CRETEST_USER | string | 复测人 |
| CRETEST_VALUE | string | 复测值 |
| CROWREMARK | string | 行备注 |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 是否允许等于上限 |
| CSTANDARD_MAX_VALUE | decimal? | 标准值上限 |
| CSTANDARD_MIN_ALLOW | string | 是否允许等于下限 |
| CSTANDARD_MIN_VALUE | decimal? | 标准值下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CSTART_VALUE | string | 始值 |
| CSTATE | string | 状态 |
| CTEMPLATE_ITEM_CODE | string | 项目编码 |
| CTEMPLATE_ITEM_DESC | string | 项目描述 |
| CTEMPLATE_ITEM_NAME | string | 项目名称 |
| CTEMPLATE_ITEM_TAG | string | 项目标签 |
| CTITRATION_VALUE | string | 滴定值 |
| CUNIT | string | 单位 |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |

### TBL_QM_CC_EXCEPTION (客诉异常报告信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAUDIT_MAN | string | 审核人 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CBAD_QTY | decimal? | 不良数量 |
| CBAD_RATIO | string | 不良比例 |
| CBAD_TYPE | string | 不良类型 |
| CCHECK_USER | string | 检查人 |
| CCOMPLAINT_LEVEL | string | 客诉等级 |
| CCUR_PROCESS | int? | 当前流程 |
| CCUSTOMER_MODEL | string | 客户型号 |
| CCUSTOMER_NO | string | 客户代码 |
| CDATA_TYPE | int | 数据类型 |
| CDUTY_PROCESS_ID | long? | 责任工序ID, TBL_BD_PROCESS表CID |
| CDUTY_PROCESS_USER | string | 责任工序责任人 |
| CEFFECT_VERIFICATION | string | 效果验证 |
| CEXCEP_CODE | string | 报告编号 |
| CEXCEP_DESC | string | 异常描述 |
| CEXCEP_PROCESS_ID | long | 异常发生工序ID, TBL_BD_PROCESS表CID |
| CFEEDBACK_DATE | DateTime? | 反馈日期 |
| CIPQA_AUDIT_MAN | string | IPQA审核人 |
| CIPQA_AUDIT_REMARK | string | IPQA审核备注 |
| CIPQA_AUDIT_STATUS | int? | IPQA审核状态 |
| CIPQA_AUDIT_TIME | DateTime? | IPQA审核时间 |
| CIPQA_TIME | DateTime? | IPQA处理时间 |
| CIS_SYNC_CUSTOMER | string | 是否同步客户 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CITEM_NO | string | 产品型号 |
| CMATERIAL_PLACE | string | 生产场所 |
| CNEED_DATE | DateTime? | 要求日期 |
| COCCUR_DATE | DateTime? | 发生时间 |
| COCCUR_PLACE | string | 发送地点 |
| COUT_CAUSE_STATUS | int | 流出原因分析状态 |
| COUT_IMPLEMENT_STATUS | int | 流出执行状态 |
| COUT_MEASURE_STATUS | int | 流出措施状态 |
| COUT_PROCESS_ID | long | 流出工序ID, TBL_BD_PROCESS表CID |
| COUT_PROCESS_USER | string | 流出工序责任人 |
| CPREVENT_STATUS | int | 预防状态 |
| CPRO_CAUSE_STATUS | int | 生产原因分析状态 |
| CPRO_IMPLEMENT_STATUS | int | 生产执行状态 |
| CPRO_MEASURE_STATUS | int | 生产措施状态 |
| CPRODUCT_STAGE | int? | 产品阶段 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CSHIPMENT_QTY | decimal? | 出货数量 |
| CSTATUS | int? | 状态：1待开始、2进行中、3已完成、4已退回 |

### TBL_QM_COMPLAINT (品质投诉记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| C8D_NUMBER | string | 8D编号 |
| CAFFECTED_AMOUNT | string | 受影响金额 |
| CCOMPLAINT_DATE | DateTime? | 投诉日期 |
| CCOMPLAINT_TYPE | string | 客诉类型 |
| CCUSTOMER_CODE | string | 客户编码 |
| CCUSTOMER_MODEL | string | 客户型号 |
| CCYCLE | string | 周期 |
| CDEFECT_QUANTITY | int? | 不良数量 |
| CDEFECT_RATE | string | 不良比例 |
| CFABRIC_MODEL | string | 本厂型号 |
| CHANDLING_METHOD | string | 处理方式 |
| CIS_MP | bool | 是否生成防错计划（true=是，false=否） |
| COCCURRENCE_PROCESS | string | 发生工序 |
| COUTFLOW_PROCESS | string | 流出工序 |
| CPROBLEM_DESC | string | 问题描述 |
| CRESPONSIBLE_PERSON | string | 责任人 |
| CRESPONSIBLE_UNIT | string | 责任单位 |

### TBL_QM_COMPLAINT_IMAGE (品质投诉图片表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOMPLAINT_ID | long | 投诉记录ID（外键，对应 TBL_QM_COMPLAINT.CID） |
| CFILE_NAME | string | 文件名称 |
| CFILE_PATH | string | Minio文件存储路径 |

### TBL_QM_INSPECTION_RECORD_ITEM (检验记录明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警上限 |
| CALARM_MIN_VALUE | decimal? | 预警下限 |
| CIMG | string | 图片Base64编码 |
| CINPUT_VALUE | string | 输入值 |
| CINSEPCT_WAY | int | 检验方式 |
| CINSPECTION_RECORD_ID | long | 检验记录主表ID |
| CINSPECTION_TOOL_CID | long? | 检验工具ID |
| CIS_PHYSICS_LAB | string | 是否送物理实验室 |
| CREMARK | string | 备注 |
| CRESULT | int | 检验结果：0不合格，1合格 |
| CSAMPLE_QTY | string | 抽样数量 |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 标准上限是否允许等于 |
| CSTANDARD_MAX_VALUE | decimal? | 标准上限 |
| CSTANDARD_MIN_ALLOW | string | 标准下限是否允许等于 |
| CSTANDARD_MIN_VALUE | decimal? | 标准下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CTEMPLATE_ITEM_CODE | string | 模板项目编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项目描述 |
| CTEMPLATE_ITEM_ID | long | 模板项目ID |
| CTEMPLATE_ITEM_NAME | string | 模板项目名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项目标签 |
| CUNIT | string | 单位 |
| LOWER_TOLERANCE | decimal? | 下公差 |
| orientation | string | 图片方向 |
| UPPER_TOLERANCE | decimal? | 上公差 |
| url | string | 图片地址 |

### TBL_QM_INSPECT_RECORD (检验记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER_NAME | string | 审核人 |
| CDECISION_MODE | int | 判定模式：1系统自动判定、2用户人为判定 |
| CINSPECT_CODE | string | 检验单号 |
| CINSPECT_QTY | decimal? | 检验数量 |
| CINSPECT_TIME | DateTime? | 检验时间 |
| CINSPECT_TYPE | int | 检验类型 |
| CINSPECT_USER_NAME | string | 检验人 |
| CIS_LAB | string | 是否送实验室 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLAB_INSPECT_REMARK | string | 实验室检验备注 |
| CLAB_INSPECT_TIME | DateTime? | 实验室检验时间 |
| CLAB_INSPECT_USER_NAME | string | 实验室检验人 |
| CLAB_RECEIVE_TIME | DateTime? | 实验室接收时间 |
| CLAB_RECEIVE_USER_NAME | string | 实验室接收人 |
| CMO_LOT | string | 工单批次 |
| CNG_DISPOSAL | string | 不良处置 |
| CPROCESS_ID | long | 工序ID |
| CREMARK | string | 备注 |
| CRESULT | int | 检验结果：1合格、2不合格 |
| CSCAN_BARCODE | string | 扫描条码 |
| CSHIFT | string | 班次 |
| CSTATUS | int | 状态：0待检验、1已检验待审核、2审核通过、3审核驳回 |
| CSUBMIT_QTY | decimal? | 报检数量 |
| CTEMPLATE_ID | long | 模板ID |
| CUNIT | string | 单位 |
| CUSTOMER_CODE | string | 客户编码 |

### TBL_QM_MEDICINE_TANK (药缸信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CMEDICINE_TANK_NAME | string | 药缸名称 |
| CMEDICINE_TANK_NO | string | 药缸编号 |
| CREMARK | string | 备注 |
| CTEMPLATE_ID | long? | 模板ID |
| CWC_ID | long | 工作中心ID |

### TBL_QM_PL_LOG (物理实验室送检记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER | string | 审核人 |
| CINSPECT_CODE | string | 检验单号 |
| CINSPECT_QTY | decimal? | 检验数量 |
| CINSPECT_REMARK | string | 检验备注 |
| CINSPECT_TIME | DateTime? | 检验时间 |
| CINSPECT_TYPE | int? | 检验类型 |
| CINSPECT_USER | string | 检验人 |
| CIS_LAB | string | 是否送检（Y：IPQC送检，N：物理实验室自行提交） |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CMO_LOT | string | 工单批次 |
| CNG_DISPOSAL | string | 不良处置 |
| CORDER_ID | long | 订单ID |
| CPOSITION | string | 送检位置 |
| CPROCESS_ID | long | 工序ID |
| CRECEIVE_TIME | DateTime? | 接收时间 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CRESULT | int? | 结果 |
| CSCAN_BARCODE | string | 扫描条码 |
| CSHIFT | string | 班次 |
| CSTATUS | int? | 状态 |
| CSUBMIT_QTY | decimal? | 报检数量 |
| CSUBMIT_REMARK | string | 送检备注 |
| CSUBMIT_REQUEST | string | 送检要求 |
| CSUBMIT_TIME | DateTime? | 送检时间 |
| CSUBMIT_USER | string | 送检人 |
| CTEMPLATE_ID | long | 模板ID |
| CTEST_ITEM_ID | long | 检测项目ID |
| CTEST_ITEM_NAME | string | 检测项目名称 |
| CUNIT | string | 单位 |
| CUSTOMER_CODE | string | 客户编码 |
| CWC_ID | long | 工作中心ID |

### TBL_QM_PL_LOG_ITEM (物理实验室送检记录明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警上限 |
| CALARM_MIN_VALUE | decimal? | 预警下限 |
| CINPUT_VALUE | string | 输入值 |
| CINPUT_VALUE_COUNT | int | 输入值数量，默认1 |
| CPL_LOG_ID | long | 送检主表ID |
| CPOSITION | string | 位置 |
| CREMARK | string | 备注 |
| CRESULT | int? | 判定结果 |
| CSCRAP_QTY | int | 报废数量 |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 标准上限是否允许等于 |
| CSTANDARD_MAX_VALUE | decimal? | 标准上限 |
| CSTANDARD_MIN_ALLOW | string | 标准下限是否允许等于 |
| CSTANDARD_MIN_VALUE | decimal? | 标准下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CSUBMIT_REQUEST | string | 送检要求 |
| CTEMPLATE_ITEM_CODE | string | 模板项目编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项目描述 |
| CTEMPLATE_ITEM_ID | long | 模板项目ID |
| CTEMPLATE_ITEM_NAME | string | 模板项目名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项目标签 |
| CTEXTBOX_QTY | int | 文本框数量 |
| CUNIT | string | 单位 |

---

## 品质客诉模块

### TBL_NP_TEMPLATE (检验模板信息主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CTEMPLATE_CODE | string | 模板编码 |
| CTEMPLATE_NAME | string | 模板名称 |
| CTEMPLATE_TYPE_ID | long? | 模板类型标识 |

### TBL_NP_TEMPLATE_CHANGE (模板信息变更主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPROVAL_ID | long? | 审批流标识 |
| CAUDIT_REMARK | string | 审核备注 |
| CAUDIT_STATUS | int | 审核状态 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CAUDIT_USER_ID | string | 审核人标识 |
| CCHANGE_REMARK | string | 变更备注 |
| CCHANGE_TIME | DateTime | 变更时间 |
| CCHANGE_USER_ID | string | 变更人标识 |
| CGROUP_ID | long | 分组标识 |
| CIS_NEW | string | 是否新增 |
| CTEMPLATE_CODE | string | 模板编码 |
| CTEMPLATE_DESC | string | 模板描述 |
| CTEMPLATE_NAME | string | 模板名称 |
| CTEMPLATE_TYPE_ID | long | 模板类型标识， TBL_NP_TEMPLATE_TYPE.CID |
| CTEMPLATE_VERSION | double | 模板版本 |

### TBL_NP_TEMPLATE_CHANGE_ITEM (模板明细信息变更表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 报警最大值（原值） |
| CALARM_MAX_VALUE_EDIT | decimal? | 报警最大值（变更后） |
| CALARM_MIN_VALUE | decimal? | 报警最小值（原值） |
| CALARM_MIN_VALUE_EDIT | decimal? | 报警最小值（变更后） |
| CCHECK_CONTENT | long | 检测内容标识（原值） |
| CCHECK_CONTENT_EDIT | long | 检测内容标识（变更后） |
| CCHECK_WAY | int | 检测方式（原值） |
| CCHECK_WAY_EDIT | int | 检测方式（变更后） |
| CDEFAULT_VALUE | string | 默认值（原值） |
| CDEFAULT_VALUE_EDIT | string | 默认值（变更后） |
| CDEFAULT_VALUE_TYPE | int | 默认值类型（原值） |
| CDEFAULT_VALUE_TYPE_EDIT | int | 默认值类型（变更后） |
| CDEVIATION_TYPE | int | 偏差类型（原值） |
| CDEVIATION_TYPE_EDIT | int | 偏差类型（变更后） |
| CFORMULA | string | 公式（原值） |
| CFORMULA_EDIT | string | 公式（变更后） |
| CINPUT_FORMULA | string | 输入公式（原值） |
| CINPUT_FORMULA_EDIT | string | 输入公式（变更后） |
| CINPUT_TYPE | int | 输入类型（原值） |
| CINPUT_TYPE_EDIT | int | 输入类型（变更后） |
| CIS_CHECK_RESULT | string | 是否参与结果判定（原值） |
| CIS_CHECK_RESULT_EDIT | string | 是否参与结果判定（变更后） |
| CIS_CHEMISTAY_LAB | string | 是否送化学实验室（原值） |
| CIS_CHEMISTAY_LAB_EDIT | string | 是否送化学实验室（变更后） |
| CIS_KEY_ITEM | string | 是否关键项（原值） |
| CIS_KEY_ITEM_EDIT | string | 是否关键项（变更后） |
| CIS_MUST | string | 是否必填（原值） |
| CIS_MUST_EDIT | string | 是否必填（变更后） |
| CIS_PHYSICS_LAB | string | 是否送物理实验室（原值） |
| CIS_PHYSICS_LAB_EDIT | string | 是否送物理实验室（变更后） |
| CIS_SHOW_STANDARD | string | 是否显示标准值（原值） |
| CIS_SHOW_STANDARD_EDIT | string | 是否显示标准值（变更后） |
| CITEM_FREQ_PERIOD_ID | long | 频次周期标识（原值） |
| CITEM_FREQ_PERIOD_ID_EDIT | long | 频次周期标识（变更后） |
| CLIST_SOURCE | string | 列表来源（原值） |
| CLIST_SOURCE_EDIT | string | 列表来源（变更后） |
| CLIST_SOURCE_TYPE | int | 列表来源类型（原值） |
| CLIST_SOURCE_TYPE_EDIT | int | 列表来源类型（变更后） |
| CSEQ | int | 排序序号（原值） |
| CSEQ_EDIT | int | 排序序号（变更后） |
| CSTANDARD_MAX_ALLOW | string | 标准最大允许值（原值） |
| CSTANDARD_MAX_ALLOW_EDIT | string | 标准最大允许值（变更后） |
| CSTANDARD_MAX_VALUE | decimal? | 标准最大值（原值） |
| CSTANDARD_MAX_VALUE_EDIT | decimal? | 标准最大值（变更后） |
| CSTANDARD_MIN_ALLOW | string | 标准最小允许值（原值） |
| CSTANDARD_MIN_ALLOW_EDIT | string | 标准最小允许值（变更后） |
| CSTANDARD_MIN_VALUE | decimal? | 标准最小值（原值） |
| CSTANDARD_MIN_VALUE_EDIT | decimal? | 标准最小值（变更后） |
| CSTANDARD_VALUE | string | 标准值（原值） |
| CSTANDARD_VALUE_EDIT | string | 标准值（变更后） |
| CSTANDARD_VALUE_TYPE | int | 标准值类型（原值） |
| CSTANDARD_VALUE_TYPE_EDIT | int | 标准值类型（变更后） |
| CSUM_FIELD | string | 求和字段（原值） |
| CSUM_FIELD_EDIT | string | 求和字段（变更后） |
| CTEMPLATE_CHANGE_ID | long | 变更ID， 对应TBL_NP_TEMPLATE_CHANGE.CID |
| CTEMPLATE_ITEM_CODE | string | 模板项编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项描述（原值） |
| CTEMPLATE_ITEM_DESC_EDIT | string | 模板项描述（变更后） |
| CTEMPLATE_ITEM_NAME | string | 模板项名称（原值） |
| CTEMPLATE_ITEM_NAME_EDIT | string | 模板项名称（变更后） |
| CTEMPLATE_ITEM_TAG | string | 模板项标签（原值） |
| CTEMPLATE_ITEM_TAG_EDIT | string | 模板项标签（变更后） |
| CTOOL_ID | long | 工具标识（原值） |
| CTOOL_ID_EDIT | long | 工具标识（变更后） |
| CUNIT | string | 单位（原值） |
| CUNIT_EDIT | string | 单位（变更后） |

### TBL_NP_TEMPLATE_ITEM (模板明细信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal | 报警最大值 |
| CALARM_MIN_VALUE | decimal | 报警最小值 |
| CCHECK_CONTENT | long | 检测内容标识 |
| CCHECK_WAY | int | 检测方式 |
| CDEFAULT_VALUE | string | 默认值 |
| CDEFAULT_VALUE_TYPE | int | 默认值类型 |
| CDEVIATION_TYPE | int | 偏差类型 |
| CINPUT_TYPE | int | 输入类型 |
| CIS_CHECK_RESULT | string | 是否参与结果判定 |
| CIS_CHEMISTAY_LAB | string | 是否送化学实验室 |
| CIS_KEY_ITEM | string | 是否关键项 |
| CIS_MUST | string | 是否必填 |
| CIS_PHYSICS_LAB | string | 是否送物理实验室 |
| CIS_SHOW_STANDARD | string | 是否显示标准值 |
| CITEM_FREQ_PERIOD_ID | long | 项目频次周期标识 |
| CLIST_SOURCE | string | 列表来源 |
| CLIST_SOURCE_TYPE | int | 列表来源类型 |
| CSEQ | int | 排序序号 |
| CSTANDARD_MAX_ALLOW | string | 标准最大允许值 |
| CSTANDARD_MAX_VALUE | decimal? | 标准最大值 |
| CSTANDARD_MIN_ALLOW | string | 标准最小允许值 |
| CSTANDARD_MIN_VALUE | decimal? | 标准最小值 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int | 标准值类型 |
| CSTANDRAD_SOURCE | string | 标准来源 |
| CSUM_FIELD | string | 求和字段 |
| CTEMPLATE_ID | long | 模板ID， 对应TBL_NP_TEMPLATE.CID |
| CTEMPLATE_ITEM_CODE | string | 模板项编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项描述 |
| CTEMPLATE_ITEM_NAME | string | 模板项名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项标签 |
| CTOOL_ID | long | 工具标识 |
| CUNIT | string | 单位 |
| LOWER_TOLERANCE | decimal? | 下公差 |
| UPPER_TOLERANCE | decimal? | 上公差 |

### TBL_QM_ASSAY_LOG (化验任务记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CASSAY_RESULT | int | 化验结果：1正常、2异常 |
| CASSAY_STATUS | int | 化验状态 |
| CASSAY_TIME | DateTime? | 化验时间 |
| CASSAY_USER | string | 化验人 |
| CBASE_TASK_NO | string | 基础任务编号 |
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_STATUS | int | 审核状态 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER | string | 审核人 |
| CIS_OPEN_LINE | string | 是否开线前分析 |
| CMEDICINE_TANK_ID | long | 药缸ID |
| CRECEIVE_TIME | DateTime? | 接收时间 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CSAMPLE_BARCODE | string | 样品条码 |
| CSAMPLE_REMARK | string | 取样备注 |
| CSAMPLE_TIME | DateTime? | 取样时间 |
| CSAMPLE_USER | string | 取样人 |
| CSHIFT | string | 班次 |
| CTASK_NO | string | 任务编号 |
| CTASK_STAND_TIME_E | DateTime? | 任务标准结束时间 |
| CTASK_STAND_TIME_S | DateTime? | 任务标准开始时间 |
| CTASK_STATUS | int | 任务状态 |
| CTASK_TAG | string | 任务标签 |
| CTASK_TYPE | int | 任务类型 |
| CTEMPLATE_ID | long | 模板ID |
| CWC_ID | long | 工作中心ID |

### TBL_QM_ASSAY_LOG_ITEM (化验任务明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警值上限 |
| CALARM_MIN_VALUE | decimal? | 预警值下限 |
| CASSAY_LOG_ID | long | 化验主表ID，对应TBL_QM_ASSAY_LOG.CID |
| CCHECK_CONTENT | long? | 校验内容ID |
| CCHECK_WAY | int? | 校验方式 |
| CCORRECTIVE_ACTION | string | 纠正措施 |
| CDATETIME_CREATED | DateTime? |  |
| CDATETIME_MODIFIED | DateTime? |  |
| CEND_VALUE | string | 终值 |
| CENTERPRISE_CODE | long? |  |
| CFORMULA | string | 补加量公式 |
| CID | long |  |
| CINPUT_FORMULA | string | 结果值计算公式 |
| CINPUT_TYPE | int? | 录入框类型 |
| CINPUT_VALUE | string? | 录入值 |
| CINSTANCE_ID | string |  |
| CIS_CHECK_RESULT | string | 是否校验 |
| CIS_CONFIRM | int? | 是否已确认添加 |
| CIS_MUST | string | 是否必填 |
| CITEM_FREQ_ID | long? | 任务频率ID |
| CLIST_SOURCE | string | 下拉框数据源 |
| CLIST_SOURCE_TYPE | int? | 下拉框数据源类型 |
| CORG_CODE | long? |  |
| CPROCESS_INFO | string | 原因分析 |
| CREMARK | string | 备注 |
| CREPLENISHMENT | string | 补加量 |
| CRESULT | int? | 结果：0不合格、1合格 |
| CRETEST_RESULT | int? | 复测结果 |
| CRETEST_TIME | DateTime? | 复测时间 |
| CRETEST_USER | string | 复测人 |
| CRETEST_VALUE | string | 复测值 |
| CROWREMARK | string |  |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 是否允许等于上限 |
| CSTANDARD_MAX_VALUE | decimal? | 标准值上限 |
| CSTANDARD_MIN_ALLOW | string | 是否允许等于下限 |
| CSTANDARD_MIN_VALUE | decimal? | 标准值下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CSTART_VALUE | string | 始值 |
| CSTATE | string |  |
| CTEMPLATE_ITEM_CODE | string | 项目编码 |
| CTEMPLATE_ITEM_DESC | string | 项目描述 |
| CTEMPLATE_ITEM_NAME | string | 项目名称 |
| CTEMPLATE_ITEM_TAG | string | 项目标签 |
| CTITRATION_VALUE | string | 滴定值 |
| CUNIT | string | 单位 |
| CUSER_CREATED | string |  |
| CUSER_MODIFIED | string |  |

### TBL_QM_CC_EXCEPTION (客诉异常报告信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAUDIT_MAN | string | 审核人 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CBAD_QTY | decimal? | 不良数量 |
| CBAD_RATIO | string | 不良比例 |
| CBAD_TYPE | string | 不良类型 |
| CCHECK_USER | string | 检查人 |
| CCOMPLAINT_LEVEL | string | 客诉等级 |
| CCUR_PROCESS | int? | 当前流程 |
| CCUSTOMER_MODEL | string | 客户型号 |
| CCUSTOMER_NO | string | 客户代码 |
| CDATA_TYPE | int | 数据类型 |
| CDUTY_PROCESS_ID | long? | 责任工序ID, TBL_BD_PROCESS表CID |
| CDUTY_PROCESS_USER | string | 责任工序责任人 |
| CEFFECT_VERIFICATION | string | 效果验证 |
| CEXCEP_CODE | string | 报告编号 |
| CEXCEP_DESC | string | 异常描述 |
| CEXCEP_PROCESS_ID | long | 异常发生工序ID, TBL_BD_PROCESS表CID |
| CFEEDBACK_DATE | DateTime? | 反馈日期 |
| CIPQA_AUDIT_MAN | string | IPQA审核人 |
| CIPQA_AUDIT_REMARK | string | IPQA审核备注 |
| CIPQA_AUDIT_STATUS | int? | IPQA审核状态 |
| CIPQA_AUDIT_TIME | DateTime? | IPQA审核时间 |
| CIPQA_TIME | DateTime? | IPQA处理时间 |
| CIS_SYNC_CUSTOMER | string | 是否同步客户 |
| CITEM_ID | long? | 产品ID |
| CITEM_NO | string | 产品型号 |
| CMATERIAL_PLACE | string | 生产场所 |
| CNEED_DATE | DateTime? | 要求日期 |
| COCCUR_DATE | DateTime? | 发生时间 |
| COCCUR_PLACE | string | 发送地点 |
| COUT_CAUSE_STATUS | int | 流出原因分析状态 |
| COUT_IMPLEMENT_STATUS | int | 流出执行状态 |
| COUT_MEASURE_STATUS | int | 流出措施状态 |
| COUT_PROCESS_ID | long | 流出工序ID, TBL_BD_PROCESS表CID |
| COUT_PROCESS_USER | string | 流出工序责任人 |
| CPREVENT_STATUS | int | 预防状态 |
| CPRO_CAUSE_STATUS | int | 生产原因分析状态 |
| CPRO_IMPLEMENT_STATUS | int | 生产执行状态 |
| CPRO_MEASURE_STATUS | int | 生产措施状态 |
| CPRODUCT_STAGE | int? | 产品阶段 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CSHIPMENT_QTY | decimal? | 出货数量 |
| CSTATUS | int? | 状态：1待开始、2进行中、3已完成、4已退回 |

### TBL_QM_COMPLAINT (客诉品质记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| C8D_NUMBER | string | 8D编号 |
| CAFFECTED_AMOUNT | string | 受影响金额 |
| CCOMPLAINT_DATE | DateTime? | 投诉日期 |
| CCOMPLAINT_TYPE | string | 客诉类型 |
| CCUSTOMER_CODE | string | 客户编码 |
| CCUSTOMER_MODEL | string | 客户型号 |
| CCYCLE | string | 周期 |
| CDEFECT_QUANTITY | int? | 不良数量 |
| CDEFECT_RATE | string | 不良比例 |
| CFABRIC_MODEL | string | 本厂型号 |
| CHANDLING_METHOD | string | 处理方式 |
| CIS_MP | bool | 是否生成防错计划（true=是，false=否） |
| COCCURRENCE_PROCESS | string | 发生工序 |
| COUTFLOW_PROCESS | string | 流出工序 |
| CPROBLEM_DESC | string | 问题描述 |
| CRESPONSIBLE_PERSON | string | 责任人 |
| CRESPONSIBLE_UNIT | string | 责任单位 |

### TBL_QM_COMPLAINT_IMAGE (客诉品质记录图片表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOMPLAINT_ID | long | 投诉记录ID（外键，对应 TBL_QM_COMPLAINT.CID） |
| CFILE_NAME | string | 文件名称 |
| CFILE_PATH | string | Minio文件存储路径 |

### TBL_QM_INSPECTION_RECORD_ITEM (IPQC检验项目明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警上限 |
| CALARM_MIN_VALUE | decimal? | 预警下限 |
| CIMG | string | 图片Base64编码 |
| CINPUT_VALUE | string | 输入值 |
| CINSEPCT_WAY | int | 检验方式 |
| CINSPECTION_RECORD_ID | long | 检验记录ID |
| CINSPECTION_TOOL_CID | long? | 检验工具ID |
| CIS_PHYSICS_LAB | string | 是否送物理实验室 |
| CREMARK | string | 备注 |
| CRESULT | int | 检验结果：0不合格，1合格 |
| CSAMPLE_QTY | string | 抽样数量 |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 标准上限是否允许等于 |
| CSTANDARD_MAX_VALUE | decimal? | 标准上限 |
| CSTANDARD_MIN_ALLOW | string | 标准下限是否允许等于 |
| CSTANDARD_MIN_VALUE | decimal? | 标准下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CTEMPLATE_ITEM_CODE | string | 模板项目编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项目描述 |
| CTEMPLATE_ITEM_ID | long | 模板项目ID |
| CTEMPLATE_ITEM_NAME | string | 模板项目名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项目标签 |
| CUNIT | string | 单位 |
| LOWER_TOLERANCE | decimal? | 下公差 |
| orientation | string | 图片方向 |
| UPPER_TOLERANCE | decimal? | 上公差 |
| url | string | 图片地址 |

### TBL_QM_INSPECT_RECORD (IPQC检验记录主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER_NAME | string | 审核人 |
| CDECISION_MODE | int | 判定模式：1系统自动判定、2用户人为判定 |
| CINSPECT_CODE | string | 检验单号 |
| CINSPECT_QTY | decimal? | 检验数量 |
| CINSPECT_TIME | DateTime? | 检验时间 |
| CINSPECT_TYPE | int | 检验类型 |
| CINSPECT_USER_NAME | string | 检验人 |
| CIS_LAB | string | 是否送实验室 |
| CITEM_ID | long? | 物料ID |
| CLAB_INSPECT_REMARK | string | 实验室检验备注 |
| CLAB_INSPECT_TIME | DateTime? | 实验室检验时间 |
| CLAB_INSPECT_USER_NAME | string | 实验室检验人 |
| CLAB_RECEIVE_TIME | DateTime? | 实验室接收时间 |
| CLAB_RECEIVE_USER_NAME | string | 实验室接收人 |
| CMO_LOT | string | 工单批次 |
| CNG_DISPOSAL | string | 不良处置 |
| CPROCESS_ID | long | 工序ID |
| CREMARK | string | 备注 |
| CRESULT | int | 检验结果：1合格、2不合格 |
| CSCAN_BARCODE | string | 扫描条码 |
| CSHIFT | string | 班次 |
| CSTATUS | int | 状态：0待检验、1已检验待审核、2审核通过、3审核驳回 |
| CSUBMIT_QTY | decimal? | 报检数量 |
| CTEMPLATE_ID | long | 模板ID，对应TBL_NP_TEMPLATE.CID |
| CUNIT | string | 单位 |
| CUSTOMER_CODE | string | 客户编码 |

### TBL_QM_MEDICINE_TANK (药缸信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CMEDICINE_TANK_NAME | string | 药缸名称 |
| CMEDICINE_TANK_NO | string | 药缸编号 |
| CREMARK | string | 备注 |
| CTEMPLATE_ID | long? | 模板ID |
| CWC_ID | long | 工作中心ID |

### TBL_QM_PL_LOG (物理实验室送检记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER | string | 审核人 |
| CINSPECT_CODE | string | 检验单号 |
| CINSPECT_QTY | decimal? | 检验数量 |
| CINSPECT_REMARK | string | 检验备注 |
| CINSPECT_TIME | DateTime? | 检验时间 |
| CINSPECT_TYPE | int? | 检验类型 |
| CINSPECT_USER | string | 检验人 |
| CIS_LAB | string | 是否送检（Y：IPQC送检，N：物理实验室自行提交） |
| CITEM_ID | long | 物料ID |
| CMO_LOT | string | 工单批次 |
| CNG_DISPOSAL | string | 不良处置 |
| CORDER_ID | long | 订单ID |
| CPOSITION | string | 送检位置 |
| CPROCESS_ID | long | 工序ID |
| CRECEIVE_TIME | DateTime? | 接收时间 |
| CRECEIVE_USER | string | 接收人 |
| CREMARK | string | 备注 |
| CRESULT | int? | 结果 |
| CSCAN_BARCODE | string | 扫描条码 |
| CSHIFT | string | 班次 |
| CSTATUS | int? | 状态 |
| CSUBMIT_QTY | decimal? | 报检数量 |
| CSUBMIT_REMARK | string | 送检备注 |
| CSUBMIT_REQUEST | string | 送检要求 |
| CSUBMIT_TIME | DateTime? | 送检时间 |
| CSUBMIT_USER | string | 送检人 |
| CTEMPLATE_ID | long | 模板ID，对应TBL_NP_TEMPLATE.CID |
| CTEST_ITEM_ID | long | 检测项目ID |
| CTEST_ITEM_NAME | string | 检测项目名称 |
| CUNIT | string | 单位 |
| CUSTOMER_CODE | string | 客户编码 |
| CWC_ID | long | 工作中心ID |

### TBL_QM_PL_LOG_ITEM (物理实验室送检项目明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警上限 |
| CALARM_MIN_VALUE | decimal? | 预警下限 |
| CINPUT_VALUE | string | 输入值 |
| CINPUT_VALUE_COUNT | int | 输入值数量，默认1 |
| CPL_LOG_ID | long | 送检主表ID |
| CPOSITION | string | 位置 |
| CREMARK | string | 备注 |
| CRESULT | int? | 判定结果 |
| CSCRAP_QTY | int | 报废数量 |
| CSEQ | int? | 顺序号 |
| CSTANDARD_MAX_ALLOW | string | 标准上限是否允许等于 |
| CSTANDARD_MAX_VALUE | decimal? | 标准上限 |
| CSTANDARD_MIN_ALLOW | string | 标准下限是否允许等于 |
| CSTANDARD_MIN_VALUE | decimal? | 标准下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int? | 标准值类型 |
| CSUBMIT_REQUEST | string | 送检要求 |
| CTEMPLATE_ITEM_CODE | string | 模板项目编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项目描述 |
| CTEMPLATE_ITEM_ID | long | 模板项目ID |
| CTEMPLATE_ITEM_NAME | string | 模板项目名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项目标签 |
| CTEXTBOX_QTY | int | 文本框数量 |
| CUNIT | string | 单位 |

---

## 文件管理模块

### TBL_ESOP_CONTACT_FORM (联络单信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPLICANT_NO | string | 申请编号 |
| CAPPROVAL_DATE | DateTime? | 批准日期 |
| CAPPROVAL_DESC | string | 批准意见 |
| CAPPROVAL_RESULT | int? | 批准结果：1同意、2驳回 |
| CAPPROVAL_USER | string | 批准人 |
| CBACKGROUND | string | 背景 |
| CCATEGORY | string | 分类 |
| CCOUNTERSIGN | int? | 会签状态：1会签完成 |
| CFILE_PATH | string | 附件 |
| CISSUE_DATE | DateTime? | 发出日期 |
| CISSUE_USER | string | 发出人 |
| CPRESENTATION | string | 呈送 |
| CREVIEW_DATE | DateTime? | 审核日期 |
| CREVIEW_DESC | string | 审核意见 |
| CREVIEW_RESULT | int? | 审核结果：1同意、2驳回 |
| CREVIEW_USER | string | 审核人 |
| CSHADOW_COPY | string | 影送 |
| CSUBJECT | string | 主题 |

### TBL_ESOP_COUNTERSIGN (4M文件会签信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATE | DateTime? | 会签日期 |
| CDEPT_NAME | string | 会签部门 |
| CMAIN_ID | long | 主表ID |
| CREMARK | string | 会签备注 |
| CTYPE | int? | 类型（1:4M文件、2:联络单） |
| CUSER_NAME | string | 会签人 |

### TBL_ESOP_FILE (ESOP文件主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAUDIT_MAN | string | 审核人 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CCOMPANY | string | 测试公司 |
| CEXPIRY_DATE | DateTime? | 有效期 |
| CFILE_CATEGORY | long? | 文件分类ID |
| CFILE_LEVEL | string | 文件等级 |
| CFILE_NAME | string | 文件名称 |
| CFILE_NO | string | 文件编号 |
| CFILE_PATH | string | 文件路径 |
| CFILE_TYPE | long | 文件类型ID |
| CFILE_VERSION | string | 文件版本 |
| CIS_AUDIT | string | 是否审核 |
| CMODEL | string | 型号 |
| CREMARK | string | 备注 |
| CREPORT_STATUS | int? | 测试报告状态：1正常、2临期（距到期时间30天内）、3过期 |
| CREPORT_TYPE | string | 报告类型 |
| CSCRAP_REMARK | string | 报废备注 |
| CSCRAP_TIME | DateTime? | 报废时间 |
| CSCRAP_USER | string | 报废人 |
| CSTATUS | int? | 状态（1正常、2报废） |
| CSUPPLIER | string | 供应商 |
| CTEMP_NAME | string | 模板名称 |
| CTEMP_NO | string | 模板编号 |
| CTEST_DATE | DateTime? | 测试日期 |
| CTYPE | string | 类型 |
| CURL | string | 文件访问地址 |

### TBL_ESOP_FILE_CATEGORY (ESOP文件分类表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFILE_CATEGORY_NAME | string | 分类名称 |
| CFILE_CATEGORY_NO | string | 分类编号 |
| CFILE_CATEGORY_PATH | string | 分类层级路径 |
| CPARENT_ID | long | 上级分类ID |
| CSEQ | int | 排序号 |

### TBL_ESOP_FILE_SIGN (文件手写体信息)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFILE_PATH | string | 签名文件路径 |
| CFILE_TYPE | string | 签名文件类型 |
| CUSER_NAME | string | 用户姓名 |
| CUSER_NO | string | 用户工号 |

### TBL_ESOP_FILE_TYPE (ESOP文件类型表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFILE_EXTENDED | string | 允许的文件后缀 |
| CTYPE_DESC | string | 类型描述 |
| CTYPE_NAME | string | 类型名称 |
| CTYPE_NO | string | 类型编号 |

### TBL_ESOP_TEMPLATE (ESOP模板关联表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFILE_ID | long? | 文件ID |
| CTEMP_FACTORY | string | 工厂 |
| CTEMP_ID | long? | 模板ID |
| CTEMP_MODEL | string | 型号 |
| CTEMP_NO | string | 模板编号 |

### TBL_ESOP_TEMPORARY_CHANGE_ORDER (4M临时变更单)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAFTER_ITEM | string | 变更后料号 |
| CAPPLICANT_DATE | DateTime? | 申请日期 |
| CAPPLICANT_DEPARTMENT | string | 申请部门 |
| CAPPLICANT_NAME | string | 申请人 |
| CAPPLICANT_NO | string | 申请编号 |
| CAPPLY_SOP | bool? | 申请标准化 |
| CAPPLY_VERIFY | bool? | 申请重新验证 |
| CATTACHMENT_AFTER | string | 上传附件（变更后） |
| CATTACHMENT_BEFORE | string | 上传附件（变更前） |
| CBEFORE_ITEM | string | 变更前料号 |
| CCHANGE_AFTER | string | 变更后 |
| CCHANGE_BEFORE | string | 变更前 |
| CCHANGE_PERIOD | string | 变更期限 |
| CCONFIRM_DATE | DateTime? | 品质确认时间 |
| CCONFIRM_USER | string | 品质确认人 |
| CCOUNTERSIGN | int? | 会签状态：1会签完成 |
| CCUSTOMER_APPLY | bool? | 是否向客户提出申请 |
| CERP_FILE_NO | string | ERP文件 |
| CEXECUTION_DATE | DateTime? | 执行变更日期 |
| CEXPIRY_DATE | DateTime? | 有效期 |
| CINVOLVED_ITEM_NO | string | 涉及料号 |
| CINVOLVED_MACHINE | bool? | 涉及机器 |
| CINVOLVED_MATERIAL | bool? | 涉及材料 |
| CINVOLVED_METHOD | bool? | 涉及方法 |
| CINVOLVED_PROCESS | string | 涉及变更工序 |
| CINVOLVED_USER | bool? | 涉及人员 |
| CIS_RECOVERY | bool? | 恢复原状 |
| CNEW_4M_NAME | string | 新4M名称 |
| CORDER_NUMBER | string | 订单号 |
| CPREVIOUS_INVENTORY_HANDLING | string | 变更前在制品、库存品处理方式 |
| CREASON_AND_PURPOSE | string | 变更原因及目的 |
| CREVIEW_DATE | DateTime? | 审核时间 |
| CREVIEW_DESC | string | 审核意见 |
| CREVIEW_RESULT | int? | 审核结果：1同意、2不同意、2其他 |
| CREVIEW_TODO | bool | 是否生成代码事项 |
| CREVIEW_USER | string | 审核人 |

### TBL_FOURM_CHANGE_ITEM_LOG (4M变更料号日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAFTER_ITEM | string | 变更后料号 |
| CBEFOR_ITEM | string | 变更前料号 |
| CFOURM_ID | long | 表单ID |
| CPART | string | 部件 |

---

## 点检保养模块

### TBL_EAM_EQUIPMENT (设备主数据表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPROACH_DATE | DateTime? | 进厂日期 |
| CASSET_NUMBER | string | 资产编号 |
| CBRAND | string | 品牌 |
| CCAPACITY | string | 产能 |
| CDEPT_ID | Int64? | 责任部门ID |
| CDUTY_DEPT_NO | string | 责任部门编号 |
| CDUTY_PERSON_NO | string | 责任人工号 |
| CENTER_DATE | DateTime? | 验收日期 |
| CEQUIPMENT_CODE | string | 设备编码 |
| CEQUIPMENT_MODEL | string | 设备型号 |
| CEQUIPMENT_NAME | string | 设备名称 |
| CEQUIPMENT_SUPPLIER | string | 设备供应商 |
| CFACTORY_EQUIPMENT_CODE | string | 厂内设备编码 |
| CIS_CONNECT | string | 是否联网 |
| CLIABLE_PERSON | string | 责任人 |
| CLINK | string | 联系方式 |
| CMANUFACTURING_DATE | DateTime? | 出厂日期 |
| CPURCHASE_WAY | string | 采购方式 |
| CQTY | string | 数量 |
| CREMARK | string | 备注 |
| CSPEC | string | 规格 |
| CSTATUS | string | 设备状态 |
| CSUPPLIER_NO | string | 供应商编号 |
| CTYPE_ID | Int64? | 设备类型ID |
| CUSE_DEPT_NO | string | 使用部门编号 |
| CWC_ID | Int64? | 工作中心ID |
| CWORK_CENTER_CID | Int64? | 工作中心CID |
| CWORK_SHOP_NO | string | 车间编号 |
| CWORKSHOP | string | 车间 |

### TBL_EAM_EQUIPMENT_TYPE (设备类型信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CEQUIPMENT_TYPE_CODE | string | 设备类型编码 |
| CEQUIPMENT_TYPE_DESC | string | 设备类型描述 |
| CEQUIPMENT_TYPE_GROUP | string | 设备类型分组 |
| CEQUIPMENT_TYPE_NAME | string | 设备类型名称 |

### TBL_EAM_ERROR_CODE (设备故障代码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CERROR_CODE | string | 故障代码 |
| CERROR_DESC | string | 故障描述 |
| CERROR_LEVEL | string | 故障等级 |
| CERROR_NAME | string | 故障名称 |
| CERROR_TYPE | string | 故障类型 |

### TBL_EAM_FREQUENCY (设备保养频次配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCOUNT | int | 频次数值 |
| CCOUNT_UNIT | string | 计数单位 |
| CFREQ_DESC | string | 频次说明 |
| CFREQ_NAME | string | 频次名称 |
| CFREQ_UNIT | string | 频次单位 |

### TBL_EAM_MAINTAIN_STANDARD_IMG (保养标准图片表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIMAGE_PATH | string | 图片路径 |
| CITEM_ID | Int64 | 保养模板项目ID |

### TBL_EAM_MAINTAIN_TASK (保养任务主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPROVAL_ID | Int64 | 审批流ID |
| CAPPROVAL_STATUS | Int32 | 审批状态 |
| CBASE_TASK_NO | String | 基准任务编号 |
| CCHECK_REMARK | string | 点检备注 |
| CCHECK_STATUS | int | 点检状态 |
| CEMPOLYEE_NAME | String | 执行人姓名 |
| CEMPOLYEE_NO | String | 执行人工号 |
| CIS_INTERVAL | bool | 是否按间隔生成任务 |
| CMAINTAIN_TIME | DateTime? | 保养执行时间 |
| CREMARK | string | 备注 |
| CRESULT | String | 保养结果 |
| CTASK_CREATED_TIME | DateTime? | 任务创建时间 |
| CTASK_NO | String | 任务编码 |
| CTASK_STAND_TIME_E | DateTime? | 标准结束时间 |
| CTASK_STAND_TIME_S | DateTime? | 标准开始时间 |
| CTASK_STATUS | Int32 | 任务状态（0待执行,1已执行,2已关闭(未执行)） |
| CTASK_TAG | String | 任务标签（用于区分任务属于哪一个频次的第几次任务） |
| CTASK_TYPE | String | 任务类型（自动任务、手动任务、主动任务） |
| CTEMP_ID | Int64 | 模板ID |
| CTEMP_NAME | String | 模板名称 |
| CTEMP_NO | String | 模板编号 |
| CWC_ID | Int64 | 工作中心ID |

### TBL_EAM_MAINTAIN_TASK_CHANGE_LOG (保养任务时间变更日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CNEW_TIME | string | 新计划时间 |
| COLD_TIME | string | 原计划时间 |
| CREMARK | string | 备注 |
| CTASK_ID | long | 任务ID |

### TBL_EAM_MAINTAIN_TASK_ITEM (保养任务明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX | Decimal | 报警上限 |
| CALARM_MIN | Decimal | 报警下限 |
| CDEFAULT_VALUE | String | 默认值 |
| CHID | Int64 | 任务主表ID |
| CINPUT_TYPE | String | 输入类型 |
| CINPUT_VALUE | String | 输入值 |
| CIS_CHECK_RESULT | Boolean | 是否校验结果 |
| CIS_INTERVAL | Boolean | 是否按间隔生成任务 |
| CIS_KEY_ITEM | Boolean | 是否关键项 |
| CIS_MUST | Boolean | 是否必填 |
| CIS_MUST_UPLOAD_IMG | bool | 是否必须上传图片 |
| CIS_REGULAR | Boolean | 是否正则校验 |
| CIS_SERVICE_CHECK | Boolean | 是否服务校验 |
| CIS_SHOW_STANDARD | bool | 是否显示标准值 |
| CIS_SHOW_UPLOAD_IMG | bool | 是否显示上传图片入口 |
| CITEM_DESC | String | 项目描述 |
| CITEM_FREQ | String | 项目频次 |
| CITEM_ID | Int64 | 模板项ID |
| CITEM_NAME | String | 项目名称 |
| CITEM_NO | String | 项目编号 |
| CITEM_TAG | String | 项目标记 |
| CLIST_SOURCE | String | 下拉数据源 |
| CREGULAR | String | 正则表达式 |
| CREGULAR_TIPS | String | 正则提示 |
| CREMARK | string | 备注 |
| CRESULT | string | 检查结果 |
| CSEQ | int | 排序 |
| CSERVICE | String | 服务地址 |
| CSTANDARD_VALUE | String | 标准值 |
| CTEMP_ID | Int64 | 模板ID |
| CUNIT | String | 单位 |
| CWARM_MAX | Decimal | 预警上限 |
| CWARM_MIN | Decimal | 预警下限 |

### TBL_EAM_MAINTAIN_TASK_ITEM_IMG (保养任务明细图片表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIMAGE_PATH | string | 图片路径 |
| CITEM_ID | Int64 | 保养任务明细ID |

### TBL_EAM_MAINTAIN_TEMPLATE_ITEMS (保养模板项目表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX | Decimal | 报警上限 |
| CALARM_MIN | Decimal | 报警下限 |
| CDEFAULT_VALUE | String | 默认值 |
| CINPUT_TYPE | String | 输入类型 |
| CIS_CHECK_RESULT | Boolean | 是否校验结果 |
| CIS_INTERVAL | Boolean | 是否按间隔生成任务 |
| CIS_KEY_ITEM | Boolean | 是否关键项 |
| CIS_MUST | Boolean | 是否必填 |
| CIS_MUST_UPLOAD_IMG | bool | 是否必须上传图片 |
| CIS_REGULAR | Boolean | 是否正则校验 |
| CIS_SERVICE_CHECK | Boolean | 是否服务校验 |
| CIS_SHOW_STANDARD | bool | 是否显示标准值 |
| CIS_SHOW_UPLOAD_IMG | bool | 是否显示上传图片入口 |
| CITEM_DESC | String | 项目描述 |
| CITEM_FREQ | String | 项目频次 |
| CITEM_NAME | String | 项目名称 |
| CITEM_NO | String | 项目编号 |
| CITEM_TAG | String | 项目标记 |
| CLIST_SOURCE | String | 下拉数据源 |
| CREGULAR | String | 正则表达式 |
| CREGULAR_TIPS | String | 正则提示 |
| CSEQ | int | 排序 |
| CSERVICE | String | 服务地址 |
| CSTANDARD_VALUE | String | 标准值 |
| CTEMP_ID | Int64 | 模板ID |
| CUNIT | String | 单位 |
| CWARM_MAX | Decimal | 预警上限 |
| CWARM_MIN | Decimal | 预警下限 |

### TBL_EAM_MAINTAIN_TEMP_D (保养模板变更历史明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX | Decimal | 报警上限 |
| CALARM_MAX_EDIT | Decimal | 变更后报警上限 |
| CALARM_MIN | Decimal | 报警下限 |
| CALARM_MIN_EDIT | Decimal | 变更后报警下限 |
| CDEFAULT_VALUE | String | 默认值 |
| CDEFAULT_VALUE_EDIT | String | 变更后默认值 |
| CHID | Int64 | 变更主表ID |
| CINPUT_TYPE | String | 输入类型 |
| CINPUT_TYPE_EDIT | String | 变更后输入类型 |
| CIS_CHECK_RESULT | Boolean | 是否校验结果 |
| CIS_CHECK_RESULT_EDIT | Boolean | 变更后是否校验结果 |
| CIS_INTERVAL | Boolean | 是否按间隔生成任务 |
| CIS_INTERVAL_EDIT | Boolean | 变更后是否按间隔生成任务 |
| CIS_KEY_ITEM | Boolean | 是否关键项 |
| CIS_KEY_ITEM_EDIT | Boolean | 变更后是否关键项 |
| CIS_MUST | Boolean | 是否必填 |
| CIS_MUST_EDIT | Boolean | 变更后是否必填 |
| CIS_MUST_UPLOAD_IMG | bool | 是否必须上传图片 |
| CIS_MUST_UPLOAD_IMG_EDIT | bool | 变更后是否必须上传图片 |
| CIS_REGULAR | Boolean | 是否正则校验 |
| CIS_REGULAR_EDIT | Boolean | 变更后是否正则校验 |
| CIS_SERVICE_CHECK | Boolean | 是否服务校验 |
| CIS_SERVICE_CHECK_EDIT | Boolean | 变更后是否服务校验 |
| CIS_SHOW_STANDARD | bool | 是否显示标准值 |
| CIS_SHOW_STANDARD_EDIT | bool | 变更后是否显示标准值 |
| CIS_SHOW_UPLOAD_IMG | bool | 是否显示上传图片入口 |
| CIS_SHOW_UPLOAD_IMG_EDIT | bool | 变更后是否显示上传图片入口 |
| CITEM_DESC | String | 项目描述 |
| CITEM_DESC_EDIT | String | 变更后项目描述 |
| CITEM_FREQ | String | 项目频次 |
| CITEM_FREQ_EDIT | String | 变更后项目频次 |
| CITEM_ID | Int64 | 项目ID |
| CITEM_NAME | String | 项目名称 |
| CITEM_NAME_EDIT | String | 变更后项目名称 |
| CITEM_NO | String | 项目编号 |
| CITEM_TAG | String | 项目标记 |
| CITEM_TAG_EDIT | String | 变更后项目标签 |
| CLIST_SOURCE | String | 下拉数据源 |
| CLIST_SOURCE_EDIT | String | 变更后下拉数据源 |
| CREGULAR | String | 正则表达式 |
| CREGULAR_EDIT | String | 变更后正则表达式 |
| CREGULAR_TIPS | String | 正则提示 |
| CREGULAR_TIPS_EDIT | String | 变更后正则提示 |
| CSEQ | int | 排序 |
| CSEQ_EDIT | int | 变更后排序 |
| CSERVICE | String | 服务地址 |
| CSERVICE_EDIT | String | 变更后服务地址 |
| CSTANDARD_VALUE | String | 标准值 |
| CSTANDARD_VALUE_EDIT | String | 变更后标准值 |
| CTEMP_ID | Int64 | 模板ID |
| CUNIT | String | 单位 |
| CUNIT_EDIT | String | 变更后单位 |
| CWARM_MAX | Decimal | 预警上限 |
| CWARM_MAX_EDIT | Decimal | 变更后预警上限 |
| CWARM_MIN | Decimal | 预警下限 |
| CWARM_MIN_EDIT | Decimal | 变更后预警下限 |

### TBL_EAM_MAINTAIN_TEMP_WC_LINK (保养模板与工作中心关联表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CTEMP_ID | Int64 | 模板ID |
| CWC_ID | Int64 | 工作中心ID |

### TBL_EAM_PM_TEMPLATE_ITEMS (点检模板项目明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX | decimal? | 报警上限 |
| CALARM_MIN | decimal? | 报警下限 |
| CDEFAULT_VALUE | string | 默认值 |
| CINPUT_TYPE | string | 输入类型 |
| CIS_CHECK_RESULT | bool | 是否参与结果判定 |
| CIS_INTERVAL | Boolean? | 是否区间录入 |
| CIS_KEY_ITEM | bool | 是否关键项 |
| CIS_MUST | bool | 是否必填 |
| CIS_MUST_UPLOAD_IMG | bool | 是否必须上传图片 |
| CIS_REGULAR | bool | 是否正则校验 |
| CIS_SERVICE_CHECK | bool | 是否服务端校验 |
| CIS_SHOW_STANDARD | bool | 是否显示标准值 |
| CIS_SHOW_UPLOAD_IMG | bool | 是否显示上传图片 |
| CITEM_DESC | string | 项目描述 |
| CITEM_FREQ | string | 项目频率 |
| CITEM_NAME | string | 项目名称 |
| CITEM_NO | string | 项目编号 |
| CITEM_TAG | string | 项目标记 |
| CLIST_SOURCE | string | 列表数据源 |
| CREGULAR | string | 正则表达式 |
| CREGULAR_TIPS | string | 正则提示 |
| CSEQ | int | 排序号 |
| CSERVICE | string | 服务配置 |
| CSTANDARD_VALUE | string | 标准值 |
| CTEMP_ID | long | 模板ID |
| CUNIT | string | 单位 |
| CWARM_MAX | decimal? | 预警上限 |
| CWARM_MIN | decimal? | 预警下限 |

### TBL_EAM_PM_TEMP_WC_LINK (模板关联工作中心)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CTEMP_ID | long? | 模板ID |
| CWC_ID | long? | 工作中心ID |

### TBL_EAM_REPAIR (维修工单主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPLY_DATE | DateTime? | 报修时间 |
| CAPPLY_MAN | string | 报修人工号 |
| CASSIGNMENT_DATE | DateTime? | 指派时间 |
| CASSIGNMENT_MAN | string | 指派人工号 |
| CAUDIT_DEPARTMNT | string | 审核部门 |
| CAUDIT_STATUS | string | 审核状态 |
| CAUDIT_USERNAME | string | 审核/驳回人（T-SQL 中文别名须 **`AS [审核/驳回人]`**，勿裸写 **`AS 审核/驳回人`**，否则错误 **102**） |
| CCAUSE | string | 故障根因 |
| CCLOSE_DATE | DateTime? | 关闭时间 |
| CCLOSE_MAN | string | 关闭人工号 |
| CDEMAND_DATE | DateTime? | 要求完成时间 |
| CEND_REPAIR_DATE | DateTime? | 结束维修时间 |
| CERROR_DESC | string | 故障描述 |
| CERROR_ID | Int64 | 故障代码ID |
| CERROR_REASON | string | 故障原因描述 |
| CIS_PRODUCT | string | 是否停产（Y/N） |
| CIS_URGENT | string | 是否紧急（Y/N） |
| CODE | string | 用户工号（**部分现场库无此列**，查 `TBL_EAM_REPAIR` 报 **207** 时勿直接使用；以 `INFORMATION_SCHEMA.COLUMNS` 为准） |
| CPLAN_COMPLETE_DATE | DateTime? | 计划完成时间 |
| CPRIORITY | int | 优先级 |
| CREMARK | string | 备注 |
| CREPAIR_CODE | string | 维修单编号 |
| CREPAIR_DESC | string | 维修措施说明 |
| CREPAIR_MAN | string | 维修人工号 |
| CSCORE | int | 评分 |
| CSTART_REPAIR_DATE | DateTime? | 开始维修时间 |
| CSTATUS | string | 工单状态 |
| CWAIT_MATERIAL_DATE | DateTime? | 开始待料时间 |
| CWC_CHILDREN | long? | 设备故障子节点(设备ID) |
| CWC_ID | Int64 | 工作中心ID |
| NAME | string | 用户姓名（**部分现场库无此列**，查 `TBL_EAM_REPAIR` 报 **207** 时勿直接使用；`CODE` 也可能不存在，请先以 `INFORMATION_SCHEMA.COLUMNS` 或 `SELECT TOP (n) *` 实际列为准） |

### TBL_EAM_REPAIR_IMG (维修图片记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CIMAGE_PATH | string | 图片路径 |
| CREPAIR_ID | Int64 | 维修单ID |
| CTYPE | int | 图片类型（1故障图片，2维修图片） |

### TBL_EAM_REPAIR_MAN (指派人员列表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CREPAIR_CODE | string | 维修单编号 |
| CREPAIR_ID | long | 维修单ID |
| CREPAIR_MAN_CODE_PRE | string | 指派人账号 |
| CREPAIR_MAN_NAME_PRE | string | 指派人名称 |

### TBL_EAM_REPAIR_MATERIAL (维修耗材记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CMATERIAL_NAME | string | 物料名称 |
| CMATERIAL_SPEC | string | 物料规格 |
| CQTY | int | 数量 |
| CREPAIR_ID | Int64 | 维修单ID |

### TBL_NP_TEMPLATE (模板主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CTEMPLATE_CODE | string | 模板编码 |
| CTEMPLATE_NAME | string | 模板名称 |
| CTEMPLATE_TYPE_ID | long? | 模板类型标识 |

### TBL_NP_TEMPLATE_CHANGE (模板变更主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPROVAL_ID | long? | 审批流标识 |
| CAUDIT_REMARK | string | 审核备注 |
| CAUDIT_STATUS | int | 审核状态 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CAUDIT_USER_ID | string | 审核人标识 |
| CCHANGE_REMARK | string | 变更备注 |
| CCHANGE_TIME | DateTime | 变更时间 |
| CCHANGE_USER_ID | string | 变更人标识 |
| CGROUP_ID | long | 分组标识 |
| CIS_NEW | string | 是否新增 |
| CTEMPLATE_CODE | string | 模板编码 |
| CTEMPLATE_DESC | string | 模板描述 |
| CTEMPLATE_NAME | string | 模板名称 |
| CTEMPLATE_TYPE_ID | long | 模板类型标识， TBL_NP_TEMPLATE_TYPE.CID |
| CTEMPLATE_VERSION | double | 模板版本 |

### TBL_NP_TEMPLATE_CHANGE_ITEM (模板变更明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 报警最大值（原值） |
| CALARM_MAX_VALUE_EDIT | decimal? | 报警最大值（变更后） |
| CALARM_MIN_VALUE | decimal? | 报警最小值（原值） |
| CALARM_MIN_VALUE_EDIT | decimal? | 报警最小值（变更后） |
| CCHECK_CONTENT | long | 检测内容标识（原值） |
| CCHECK_CONTENT_EDIT | long | 检测内容标识（变更后） |
| CCHECK_WAY | int | 检测方式（原值） |
| CCHECK_WAY_EDIT | int | 检测方式（变更后） |
| CDEFAULT_VALUE | string | 默认值（原值） |
| CDEFAULT_VALUE_EDIT | string | 默认值（变更后） |
| CDEFAULT_VALUE_TYPE | int | 默认值类型（原值） |
| CDEFAULT_VALUE_TYPE_EDIT | int | 默认值类型（变更后） |
| CDEVIATION_TYPE | int | 偏差类型（原值） |
| CDEVIATION_TYPE_EDIT | int | 偏差类型（变更后） |
| CFORMULA | string | 公式（原值） |
| CFORMULA_EDIT | string | 公式（变更后） |
| CINPUT_FORMULA | string | 输入公式（原值） |
| CINPUT_FORMULA_EDIT | string | 输入公式（变更后） |
| CINPUT_TYPE | int | 输入类型（原值） |
| CINPUT_TYPE_EDIT | int | 输入类型（变更后） |
| CIS_CHECK_RESULT | string | 是否参与结果判定（原值） |
| CIS_CHECK_RESULT_EDIT | string | 是否参与结果判定（变更后） |
| CIS_CHEMISTAY_LAB | string | 是否送化学实验室（原值） |
| CIS_CHEMISTAY_LAB_EDIT | string | 是否送化学实验室（变更后） |
| CIS_KEY_ITEM | string | 是否关键项（原值） |
| CIS_KEY_ITEM_EDIT | string | 是否关键项（变更后） |
| CIS_MUST | string | 是否必填（原值） |
| CIS_MUST_EDIT | string | 是否必填（变更后） |
| CIS_PHYSICS_LAB | string | 是否送物理实验室（原值） |
| CIS_PHYSICS_LAB_EDIT | string | 是否送物理实验室（变更后） |
| CIS_SHOW_STANDARD | string | 是否显示标准值（原值） |
| CIS_SHOW_STANDARD_EDIT | string | 是否显示标准值（变更后） |
| CITEM_FREQ_PERIOD_ID | long | 频次周期标识（原值） |
| CITEM_FREQ_PERIOD_ID_EDIT | long | 频次周期标识（变更后） |
| CLIST_SOURCE | string | 列表来源（原值） |
| CLIST_SOURCE_EDIT | string | 列表来源（变更后） |
| CLIST_SOURCE_TYPE | int | 列表来源类型（原值） |
| CLIST_SOURCE_TYPE_EDIT | int | 列表来源类型（变更后） |
| CSEQ | int | 排序序号（原值） |
| CSEQ_EDIT | int | 排序序号（变更后） |
| CSTANDARD_MAX_ALLOW | string | 标准最大允许值（原值） |
| CSTANDARD_MAX_ALLOW_EDIT | string | 标准最大允许值（变更后） |
| CSTANDARD_MAX_VALUE | decimal? | 标准最大值（原值） |
| CSTANDARD_MAX_VALUE_EDIT | decimal? | 标准最大值（变更后） |
| CSTANDARD_MIN_ALLOW | string | 标准最小允许值（原值） |
| CSTANDARD_MIN_ALLOW_EDIT | string | 标准最小允许值（变更后） |
| CSTANDARD_MIN_VALUE | decimal? | 标准最小值（原值） |
| CSTANDARD_MIN_VALUE_EDIT | decimal? | 标准最小值（变更后） |
| CSTANDARD_VALUE | string | 标准值（原值） |
| CSTANDARD_VALUE_EDIT | string | 标准值（变更后） |
| CSTANDARD_VALUE_TYPE | int | 标准值类型（原值） |
| CSTANDARD_VALUE_TYPE_EDIT | int | 标准值类型（变更后） |
| CSUM_FIELD | string | 求和字段（原值） |
| CSUM_FIELD_EDIT | string | 求和字段（变更后） |
| CTEMPLATE_CHANGE_ID | long | 变更ID， 对应TBL_NP_TEMPLATE_CHANGE.CID |
| CTEMPLATE_ITEM_CODE | string | 模板项编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项描述（原值） |
| CTEMPLATE_ITEM_DESC_EDIT | string | 模板项描述（变更后） |
| CTEMPLATE_ITEM_NAME | string | 模板项名称（原值） |
| CTEMPLATE_ITEM_NAME_EDIT | string | 模板项名称（变更后） |
| CTEMPLATE_ITEM_TAG | string | 模板项标签（原值） |
| CTEMPLATE_ITEM_TAG_EDIT | string | 模板项标签（变更后） |
| CTOOL_ID | long | 工具标识（原值） |
| CTOOL_ID_EDIT | long | 工具标识（变更后） |
| CUNIT | string | 单位（原值） |
| CUNIT_EDIT | string | 单位（变更后） |

### TBL_NP_TEMPLATE_ITEM (模板项配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal | 报警最大值 |
| CALARM_MIN_VALUE | decimal | 报警最小值 |
| CCHECK_CONTENT | long | 检测内容标识 |
| CCHECK_WAY | int | 检测方式 |
| CDEFAULT_VALUE | string | 默认值 |
| CDEFAULT_VALUE_TYPE | int | 默认值类型 |
| CDEVIATION_TYPE | int | 偏差类型 |
| CINPUT_TYPE | int | 输入类型 |
| CIS_CHECK_RESULT | string | 是否参与结果判定 |
| CIS_CHEMISTAY_LAB | string | 是否送化学实验室 |
| CIS_KEY_ITEM | string | 是否关键项 |
| CIS_MUST | string | 是否必填 |
| CIS_PHYSICS_LAB | string | 是否送物理实验室 |
| CIS_SHOW_STANDARD | string | 是否显示标准值 |
| CITEM_FREQ_PERIOD_ID | long | 项目频次周期标识 |
| CLIST_SOURCE | string | 列表来源 |
| CLIST_SOURCE_TYPE | int | 列表来源类型 |
| CSEQ | int | 排序序号 |
| CSTANDARD_MAX_ALLOW | string | 标准最大允许值 |
| CSTANDARD_MAX_VALUE | decimal? | 标准最大值 |
| CSTANDARD_MIN_ALLOW | string | 标准最小允许值 |
| CSTANDARD_MIN_VALUE | decimal? | 标准最小值 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int | 标准值类型 |
| CSTANDRAD_SOURCE | string | 标准来源 |
| CSUM_FIELD | string | 求和字段 |
| CTEMPLATE_ID | long | 模板ID， 对应TBL_NP_TEMPLATE.CID |
| CTEMPLATE_ITEM_CODE | string | 模板项编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项描述 |
| CTEMPLATE_ITEM_NAME | string | 模板项名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项标签 |
| CTOOL_ID | long | 工具标识 |
| CUNIT | string | 单位 |
| LOWER_TOLERANCE | decimal? | 下公差 |
| UPPER_TOLERANCE | decimal? | 上公差 |

---

## 生产流程模块

### TBL_MO (工单信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CACTULA_END_TIME | DateTime? | 实际完成时间 |
| CACTULA_START_TIME | DateTime? | 实际生产时间 |
| CCOMPLETED_QTY | decimal? | 完工数量 |
| CCUST_ORDER | string | 客户订单 |
| CIS_ACTIVITY | string | 是否激活 |
| CIS_MANUAL | string | 是否手工创建 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLEVEL | int? | 级别 |
| CMO_LOT | string | 工单批次 |
| CORDER_DATETIME | DateTime? | 工单日期 |
| CORDER_NO | string | 工单编号 |
| CPARENT_ID | string | 父级工单编号 |
| CPLAN_END_TIME | DateTime? | 预计完成时间 |
| CPLAN_QTY | decimal? | 计划数量 |
| CPLAN_START_TIME | DateTime? | 预计生产时间 |
| CPROCESS_ID | long? | 工序ID |
| CREMARK | string | 备注 |
| CROUTE_ID | long? | 工艺路线ID |
| CSCHEDULE_QTY | decimal? | 已排产数量 |
| CSEQ | int? | 工单批次中的顺序 |
| CSO_DTL_ID | string | 销售单明细ID |
| CSOURCE_ID | string | 来源ID |
| CSOURCE_ORDER_NO | string | 来源工单编号 |
| CSTATUS | int? | 工单状态 |
| CTYPE_ID | long? | 工单类型ID |
| CUST_CODE | string | 客户代码 |
| CWC_ID | long? | 工作中心ID |

### TBL_MO_FAKE (虚拟工单表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CACTULA_END_TIME | DateTime? | 实际完成时间 |
| CACTULA_START_TIME | DateTime? | 实际生产时间 |
| CCOMPLETED_QTY | decimal? | 完工数量 |
| CCUST_ORDER | string | 客户订单 |
| CIS_ACTIVITY | string | 是否激活 |
| CIS_MANUAL | string | 是否手工创建 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLEVEL | int? | 级别 |
| CMO_LOT | string | 工单批次 |
| CORDER_DATETIME | DateTime? | 工单日期 |
| CORDER_NO | string | 工单编号 |
| CPARENT_ID | string | 父级工单编号 |
| CPLAN_END_TIME | DateTime? | 预计完成时间 |
| CPLAN_QTY | decimal? | 计划数量 |
| CPLAN_START_TIME | DateTime? | 预计生产时间 |
| CPROCESS_ID | long? | 工序ID |
| CREMARK | string | 备注 |
| CROUTE_ID | long? | 工艺路线ID |
| CSCHEDULE_QTY | decimal? | 已排产数量 |
| CSEQ | int? | 工单批次中的顺序 |
| CSO_DTL_ID | string | 销售单明细ID |
| CSOURCE_ID | string | 来源ID |
| CSOURCE_ORDER_NO | string | 来源工单编号 |
| CSTATUS | int? | 工单状态 |
| CTYPE_ID | long? | 工单类型ID |
| CUST_CODE | string | 客户代码 |
| CWC_ID | long? | 工作中心ID |

### TBL_MO_OUTS (外协工单信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_NO | string | 料号 |
| CMO_LOT | string | 工单批次 |
| COS_NO | string | 外协订单号 |
| CQTY | int | 数量 |
| CSO_NO | string | 销售订单号 |

### TBL_OUTSOURCE_SHIFT_EMPLOYEE (外协班次员工配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CREATED_TIME | string | 创建时间 |
| CWC_ID | long | 工作中心ID |
| ID | int | 主键ID |
| SHIFT_CODE | string | 班次编码 |
| UPDATED_TIME | string | 更新时间 |
| USER_ID | long | 员工用户ID |

### TBL_SFC_DBFC_USER (叠板防错用户)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEVICE_NO | string | 设备编码 |
| CUSER_NAME | string | 用户账号 |

### TBL_SFC_PACKAGE (包装信息表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| CBATCH_NUMBER | string | 批次号 |
| CCUSTOMER_CODE | string | 客户编码 |
| CCUSTOMER_ITEM_NAME | string | 客户品名 |
| CCUSTOMER_ITEM_NO | string | 客户料号 |
| CCYCLE | string | 周期 |
| CINVENTORY_STATUS | int? | 库存状态：0待提交、1待入库、2已入库、3已出库 |
| CIS_REPRINT | string | 是否补打 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLEVEL | int? | 包装层级 |
| CLOCATION_ID | long? | 货位ID |
| CMO_ID | string | 工单ID |
| CMO_LOT | string | 工单批次 |
| CNET_WEIGHT | decimal? | 净重 |
| CORDER_ID | long? | 订单ID |
| CORDER_NO | string | 订单号 |
| CPACKING_TIME | DateTime? | 包装时间 |
| CPARAM_VALUE | string | 参数值（板厚） |
| CPARENT_ID | long? | 父级包装ID |
| CQTY | decimal? | 数量 |
| CREMARK | string | 备注 |
| CSALES_ORDER | string | 销售订单 |
| CSET_PCS_QTY | int? | SET开板数 |
| CSET_X_QTY | int? | SET叉板数 |
| CSOURCE_BARCODE | string | 补打前的箱号 |
| CSPLIT_DATETIME | DateTime? | 拆分时间 |
| CSPLIT_ID | long? | 上级条码ID |
| CSTATUS | string | 状态，来源数据字典 |
| CWEIGHT | decimal? | 毛重 |
| CX_QTY | string | 叉板数 |
| EXPAND1 | string | 扩展字段1（内箱3045流水号） |
| ScrapDateTime | string | 报废时间 |
| ScrapUser | string | 报废人 |
| XOUT | string | 叉板值 |

### TBL_SFC_PACKAGE_LABEL_LINK (包装模板与物料/客户关联表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUSTOMER_ID | long? | 客户ID |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CREMARK | string | 备注 |
| CTEMPLATE_ID | long | 模板ID |

### TBL_SFC_PACKAGE_LOG (包装操作日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| COPERATE_TYPE | int? | 操作类型 |
| CREMARK | string | 备注 |

### TBL_SFC_PACKAGE_RULE (包装规则主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBOX_TYPE | string | 箱型 |
| CBOX_WEIGHT | decimal? | 箱重 |
| CDEVIATION | decimal? | 重量偏差 |
| CFAIL_RULE | int? | 失败处理规则 |
| CHEIGHT | decimal? | 高度 |
| CIS_MULTI_CYCLE | string | 是否允许多周期混装 |
| CIS_MULTI_ITEM | string | 是否允许多料号混装 |
| CIS_MULTI_LOT | string | 是否允许多批次混装 |
| CIS_MULTI_ORDER | string | 是否允许多工单混装 |
| CIS_MULTI_X | string | 是否允许多叉板值混装 |
| CLEN | decimal? | 长度 |
| CMAX_QTY | decimal? | 最大装箱数量 |
| CMIN_QTY | decimal? | 最小装箱数量 |
| CPKG_WEIGHT | decimal? | 包装重量 |
| CREMARK | string | 备注 |
| CRULE_NAME | string | 规则名称 |
| CRULE_TYPE | int | 规则类型 |
| CTOTAL_WEIGHT | decimal? | 总重量 |
| CWIDTH | decimal? | 宽度 |

### TBL_SFC_PACKAGE_RULE_EXT (包装规则扩展配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CEXTEND_1 | string | 板间隔纸 |
| CEXTEND_10 | string | 有无工艺边 |
| CEXTEND_11 | string | 有无RoHS |
| CEXTEND_12 | string | 纸箱要求 |
| CEXTEND_13 | string | 填充方式 |
| CEXTEND_14 | string | 每箱重量 |
| CEXTEND_15 | string | 特别要求 |
| CEXTEND_16 | string | 封箱方式 |
| CEXTEND_17 | string | 打带方式 |
| CEXTEND_18 | string | 外箱标签 |
| CEXTEND_19 | string | 外箱其他标识 |
| CEXTEND_2 | string | 上下垫板 |
| CEXTEND_20 | string | 其他特别要求 |
| CEXTEND_21 | string | 有无卤素 |
| CEXTEND_22 | string | 有无HF |
| CEXTEND_23 | string | 有无工艺边 |
| CEXTEND_24 | string | 有无RoHS |
| CEXTEND_3 | string | 干燥剂 |
| CEXTEND_4 | string | 湿度卡 |
| CEXTEND_5 | string | 包装方式 |
| CEXTEND_6 | string | 小包标签 |
| CEXTEND_7 | string | 其他特别要求 |
| CEXTEND_8 | string | 有无卤素 |
| CEXTEND_9 | string | 有无HF |
| CIMAGE_DATA | string | 图片 |
| CPACKAGE_RULE_ID | long | 主表ID |

### TBL_SFC_PACKAGE_RULE_LINK (包装规则与物料/客户关联表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUSTOMER_ID | long? | 客户ID |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CPACKAGE_RULE_ID | long? | 包装规则ID |
| CREMARK | string | 备注 |

### TBL_SFC_RECIPE_LOT (按工单批次的配方申请主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAPPLY_NO | string | 申请编号 |
| CAUDIT_DESC | string | 审核说明 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CAUDIT_USER | string | 审核人 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CENTERPRISE_CODE | long? | 企业代码 |
| CID | long | 主键ID |
| CINSTANCE_ID | string | 实例ID |
| CITEM_NAME | string | 料号名称 |
| CMO_LOT | string | 工单批次 |
| CORDER_NO | string | 订单号 |
| CORG_CODE | long? | 组织代码 |
| CPROCESS_ID | long? | 工序ID |
| CREMARK | string | 备注 |
| CROWREMARK | string | 行备注 |
| CSTATE | string | 状态标识 |
| CSTATUS | int? | 审核状态 |
| CSU_ID | long? | 提交用户ID |
| CSU_R_ID | long? | 申请单关联ID |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |
| CVERSION | int? | 版本 |

### TBL_SFC_RECIPE_LOT_LINK (工单批次配方项目明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CENTERPRISE_CODE | long? | 企业代码 |
| CEXPRESSION | string | 校验表达式 |
| CID | long | 主键ID |
| CINSTANCE_ID | string | 实例ID |
| CMAX_TOLERANCE | decimal? | 最大公差 |
| CMAX_VALUE | decimal? | 最大值 |
| CMIN_TOLERANCE | decimal? | 最小公差 |
| CMIN_VALUE | decimal? | 最小值 |
| CORG_CODE | long? | 组织代码 |
| CR_LOT_ID | long | 配方批次主表ID |
| CREAL_VALUE | string | 实际值 |
| CREMARK | string | 备注 |
| CRI_DATA_TYPE | string | 数据类型 |
| CRI_DATA_UNIT | string | 数据单位 |
| CRI_DESC | string | 配方项描述 |
| CRI_ID | long? | 配方项ID |
| CRI_NAME | string | 配方项名称 |
| CRI_NO | string | 配方项编码 |
| CRI_TYPE | int? | 项目类型 |
| CROWREMARK | string | 行备注 |
| CSEQ | int? | 排序号 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTATE | string | 状态标识 |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |
| CVALUE_TYPE | int? | 值类型 |

### TBL_SFC_RECIPE_PRODUCT (按产品维度的配方申请主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAUDIT_DESC | string | 审核说明 |
| CAUDIT_TIME | DateTime? | 审核时间 |
| CAUDIT_USER | string | 审核人 |
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CDD_TYPE | string | 打点类型 |
| CENTERPRISE_CODE | long? | 企业代码 |
| CID | long | 主键ID |
| CINSTANCE_ID | string | 实例ID |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CORG_CODE | long? | 组织代码 |
| CPROCESS_ID | long? | 工序ID |
| CREMARK | string | 备注 |
| CROWREMARK | string | 行备注 |
| CSTATE | string | 状态标识 |
| CSTATUS | int? | 审核状态 |
| CSU_ID | long | 提交用户ID |
| CSU_R_ID | long | 申请单关联ID |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |
| CVERSION | int? | 版本 |

### TBL_SFC_RECIPE_PRODUCT_LINK (产品配方项目明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDATETIME_CREATED | DateTime? | 创建时间 |
| CDATETIME_MODIFIED | DateTime? | 修改时间 |
| CENTERPRISE_CODE | long? | 企业代码 |
| CEXPRESSION | string | 校验表达式 |
| CID | long | 主键ID |
| CINSTANCE_ID | string | 实例ID |
| CMAX_TOLERANCE | decimal? | 最大公差 |
| CMAX_VALUE | decimal? | 最大值 |
| CMIN_TOLERANCE | decimal? | 最小公差 |
| CMIN_VALUE | decimal? | 最小值 |
| CORG_CODE | long? | 组织代码 |
| CR_PRODUCT_ID | long | 产品配方主表ID |
| CREAL_VALUE | string | 实际值 |
| CREMARK | string | 备注 |
| CRI_DATA_TYPE | string | 数据类型 |
| CRI_DATA_UNIT | string | 数据单位 |
| CRI_DESC | string | 配方项描述 |
| CRI_ID | long? | 配方项ID |
| CRI_NAME | string | 配方项名称 |
| CRI_NO | string | 配方项编码 |
| CRI_TYPE | int? | 项目类型 |
| CROWREMARK | string | 行备注 |
| CSEQ | int? | 排序号 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTATE | string | 状态标识 |
| CUSER_CREATED | string | 创建用户 |
| CUSER_MODIFIED | string | 修改用户 |
| CVALUE_TYPE | int? | 值类型 |

### TBL_SFC_WS_LOG (生产记录表)

**SQL 生成强制列名**：客户编码在库中、在本文中均为 **`CUSTOMER_CODE`**。**`CCUSTOMER_CODE` 在本表无效**（执行必报错 **207**）；任何检索片段、旧文档若写 **`CCUSTOMER_CODE`** 与本表同段，**视为错误，勿用于 T-SQL**。

| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CID | long | 主键ID；与 **`TBL_SFC_WS_LOG_ITEM.CWS_LOG_ID`** 关联时使用 **`l.CID = i.CWS_LOG_ID`**（主表**无** `CWS_LOG_ID` 列） |
| BOARD_TYPE | string | 板类型 |
| CCHECK_REMARK | string | 审核备注 |
| CCHECK_TIME | DateTime? | 审核时间 |
| CCHECK_USER_NAME | string | 审核人账号 |
| CEND_TIME | DateTime? | 完工时间 |
| CEND_USER_NAME | string | 完工人账号 |
| CIS_CHECK | string | 是否已审核 |
| CIS_FINISH | string | 是否完工 |
| CIS_WIP | string | 是否已过数 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLEVEL | string | 等级 |
| CMO_LOT | string | 工单批次 |
| CNG_NUMBER | decimal? | 不良数量 |
| CNUMBER_TYPE | int? | 数量类型 |
| CORDER_ID | long? | 订单ID |
| CPROCESS_ID | long | 工序ID |
| CREMARK | string | 备注 |
| CSCAN_BARCODE | string | 扫描条码 |
| CSCRAP_NUMBER | decimal? | 报废数量 |
| CSHIFT | string | 班次 |
| CSTART_TIME | DateTime? | 开工时间 |
| CSTART_USER_NAME | string | 开工人账号 |
| CSTATUS | int? | 0待审核、1已通过、2已驳回 |
| CTEMPLATE_ID | long | 模板ID |
| CUNIT | string | 单位 |
| CUSTOMER_CODE | string | 客户编码（**仅此拼写**；勿写 **`CCUSTOMER_CODE`**） |
| CWC_ID | long | 工作中心ID |
| CWORK_NUMBER | decimal | 工作数量 |
| CWORK_TYPE | int | 1正常生产记录(检验生产记录)2批量生产记录3无工单生产记录4历史记录新增5FQC生产记录 |

**命名注意（中络现场与 SQL 生成）**：客户编码列为 **`CUSTOMER_CODE`**（**勿**误写为 **`CCUSTOMER_CODE`**，否则 SQL Server 报 **207**）。扫描条码列为 **`CSCAN_BARCODE`**（**勿**写 **`CSCANNED_BARCODE`**、**`CSCANN_BARCODE`**）。工单关联优先 **`CMO_LOT`**；**`CORDER_ID`** 部分库无此列，以现场为准。**联表明细 `TBL_SFC_WS_LOG_ITEM`**：主表用 **`CID`**，子表用 **`CWS_LOG_ID`**，**禁止** **`ON l.CWS_LOG_ID = i.CWS_LOG_ID`**（主表无 **`CWS_LOG_ID`**，必 **207**）。

### TBL_SFC_WS_LOG_ITEM (生产记录项目明细)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CALARM_MAX_VALUE | decimal? | 预警上限 |
| CALARM_MIN_VALUE | decimal? | 预警下限 |
| CINPUT_VALUE | string | 输入值 |
| CREMARK | string | 备注 |
| CRESULT | int | 结果 |
| CSEQ | int | 排序号 |
| CSTANDARD_MAX_ALLOW | string | 标准上限是否允许等于 |
| CSTANDARD_MAX_VALUE | decimal? | 标准上限 |
| CSTANDARD_MIN_ALLOW | string | 标准下限是否允许等于 |
| CSTANDARD_MIN_VALUE | decimal? | 标准下限 |
| CSTANDARD_VALUE | string | 标准值 |
| CSTANDARD_VALUE_TYPE | int | 标准值类型 |
| CTEMPLATE_ITEM_CODE | string | 模板项编码 |
| CTEMPLATE_ITEM_DESC | string | 模板项描述 |
| CTEMPLATE_ITEM_NAME | string | 模板项名称 |
| CTEMPLATE_ITEM_TAG | string | 模板项标签 |
| CUNIT | string | 单位 |
| CWS_LOG_ID | long | 生产记录主表ID |

### TBL_SFC_WS_TEMPLATE_CONFIG (工位报工模板配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CFIRST_COMMIT_TIMESPAN | int? | 一次报工自动补全时间差（min） |
| CIS_AUTO_GET_NUMBER | string | 是否自动获取数量 |
| CIS_CONTROL_NUMBER | string | 是否管控数量 |
| CIS_FIRST_COMMIT | string | 是否一次报工 |
| CIS_GET_LAST_DATA | string | 是否赋值上次记录 |
| CIS_IGNORE_ITEM | string | 赋值上次记录时是否忽略产品 |
| CIS_IPQC_FIRST | string | 是否需要IPQC首件管控 |
| CIS_KEYPART_MANAGE | string | 是否关键物料管控 |
| CIS_LOCK_NUMBER | string | 是否锁定数量 |
| CIS_NO_ORDER | string | 是否允许无工单生产记录 |
| CIS_PM | string | 是否校验设备点检 |
| CIS_WIP_TEMPLATE | string | 是否过数模板 |
| CNEXT_TIMESPAN | int? | 相同lot卡下一次开工最小时间间隔（min） |
| COVERDUE_TIME | int? | 超期时间 |
| CREMARK | string | 备注 |
| CSE_TIMESPAN | int? | 开工完工最小时间间隔（min） |
| CTEMPLATE_ID | long | 模板ID |
| CUNIT | string | 默认单位 |
| CWARNING_TIME | int? | 预警时间 |

### TBL_SFC_WS_TEMPLATE_LINK (工位模板关联配置表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPROCESS_ID | long | 工序ID |
| CREMARK | string | 备注 |
| CTEMPLATE_ID | long | 模板ID |
| CWC_ID | long | 工作中心ID |

---

## 仓储管理模块

### TBL_WMS_AREA (仓库区域)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CAREA_CODE | string | 区域代码 |
| CAREA_DESC | string | 区域描述 |
| CAREA_NAME | string | 区域名称 |
| CPERSON_ID | string | 区域管理员ID |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源ID |
| CWAREHOUSE_ID | long? | 仓库ID |

### TBL_WMS_BARCODE_SPLIT_RECORD (条码拆分记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CREMARK | string | 备注 |
| CSOURCE_BARCODE_ID | long? | 来源条码ID |
| CSPLIT_QTY | decimal? | 拆分数量 |
| CSPLIT_TIME | DateTime? | 拆分时间 |
| CSPLIT_USER | string | 拆分人 |
| CTARGET_BARCODE_ID | long? | 目标条码ID |

### TBL_WMS_ITEM_BARCODE (物料条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBALANCE_QTY | decimal? | 剩余数量 |
| CBARCODE | string | 条码 |
| CBARCODE_TYPE | string | 条码类型 |
| CCYCLE | string | 周期 |
| CEFFECTIVE_STATUS | int? | 是否超期 2 已超期 |
| CERP_LOT_NO | string | ERP批次号 |
| CEXPIRATION_TIME | DateTime? | 有效日期 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long? | 货位ID |
| CLOSS_QTY | decimal? | 调整数量 |
| CLOT_NO | string | 批次号 |
| CPACKING_DATETIME | DateTime? | 包箱时间 |
| CPACKING_ID | long? | 包装条码ID |
| CPI_DTL_ID | long? | 入库明细ID |
| CPLAIN_CODE | string | 料盘编码 |
| CPRINT_TIMES | int? | 打印次数 |
| CPRODUCTION_DATETIME | DateTime? | 生产时间 |
| CQTY | decimal? | 条码数量 |
| CREMARK | string | 备注 |
| CSCRAP_TIME | DateTime? | 条码报废时间 |
| CSO_NO | string | 销售订单 |
| CSOURCE_ID | long? | 来源ID(来源于TBL_SRM_PO_DETAIL) |
| CSPLIT_DATETIME | DateTime? | 拆分时间 |
| CSPLIT_ID | long | 上级条码ID |
| CSRC_ID | long? | 来源记录ID（这里保存的是采购订单交付表的ID） |
| CSRC_TYPE | string | 来源类型 |
| CSTATUS | string | 条码状态 |
| CSTORAGE_TIME | DateTime? | 入库日期 |
| CSUPPLIER_ID | long? | 供应商ID |
| CSUPPLIER_LOT_NO | string | 供应商批号 |
| CUNIT | string | 单位 |
| CUSE_QTY | decimal? | 使用数量 |

### TBL_WMS_ITEM_BARCODE_HISTORY (物料条码操作历史表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码编码 |
| CBARCODE_STATUS | string | 条码状态 |
| CQTY | object | 数量 |
| CREMARK | string | 备注 |

### TBL_WMS_ITEM_LOCATION (物料默认货位)
（**说明**：本表一般为 **`CITEM_ID` + `CLOCATION_ID`**；**货位编码**多在 **`TBL_WMS_LOCATION.CLOCATION_CODE`**，勿默认本表有 **`CLOCATION_CODE`**。）
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long | 货位ID |

### TBL_WMS_ITEM_PACKING_BARCODE (物料包装条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 包装条码 |
| CPARENT_ID | long | 上级包装ID |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源ID |
| CSTATUS | string | 状态 |
| CBARCODE | string | 条码 |
| CPARENT_ID | long | 父级 |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源ID |
| CSTATUS | string | 关闭状态 |

### TBL_WMS_ITEM_TEMPLATE (物料标签绑定表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CITEM_TYPE_ID | long? | 物料类型ID |
| MINTEMPLATEID | long? | 最小包装模板ID |
| PACKTEMPLATEID | long? | 包装箱模板ID |

### TBL_WMS_LINE_BARCODE_RECORD (线边仓条码出入记录表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE_ID | long? | 条码ID |
| CIN_TIME | DateTime? | 入仓时间 |
| CIN_USER | string | 入仓人 |
| CLOCATION_SN | string | 货位条码 |
| COUT_QTY | int? | 已出仓数量 |
| COUT_TIME | DateTime? | 出仓时间 |
| COUT_USER | string | 出仓人 |
| CQTY | int? | 数量 |
| CREMARK | string | 备注 |
| CSTATUS | int? | 状态（1未出仓，2已出仓） |
| CWAREHOUSE_ID | long? | 仓库ID |

### TBL_WMS_LINE_RECORD (线别仓操作记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CATTRIBUTE | string | 属性 |
| CIN_TIME | DateTime? | 入仓时间 |
| CIN_USER | string | 入仓人 |
| CITEM_NAME | string | 产品 |
| CLOCATION_SN | string | 货位条码 |
| CORDER_NO | string | 工单 |
| COUT_QTY | int? | 已出仓数量 |
| COUT_TIME | DateTime? | 出仓时间 |
| COUT_USER | string | 出仓人 |
| CPROCESS | string | 工艺 |
| CQTY | int? | 数量 |
| CREMARK | string | 备注 |
| CSTATUS | int | 1已入仓、2已出仓 |
| CTG_VALUE | string | TG值 |
| CWAREHOUSE_ID | long | 中转仓ID |

### TBL_WMS_LINE_WAREHOUSE (线别仓)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 产品条码 |
| CCURRENT_QTY | decimal | 上料后剩余数 |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CMI_DTL_ID | long? | 备料单子表Id |
| COVER_QTY | decimal? | 超发数量 |
| CQTY | decimal | 备料数量 |
| CREASON | string? | 产品到线边仓来的原因 |
| CREMARKS | string? | 备注 |
| CREQUIRE_QTY | decimal | 领料需求数 |
| CSTATUS | int | 状态  【0：未上料 1：已上料】 |
| CWC_ID | long? | 线体id |
| CWORKSHOP_ID | long | 车间id |

### TBL_WMS_LINE_WAREHOUSE_RECORD (线别仓记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 产品条码 |
| CBARCODE_QTY | decimal | 条码数量 |
| CCURRENT_QTY | decimal | 当前数量 |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CITEM_NAME | string | 产品名称 |
| CITEM_NO | string | 产品编号 |
| CMI_DTL_ID | long | 备料单子表id |
| CMI_NO | string | 备料单号 |
| CQTY | decimal | 数量 |
| CREASON | string? | 原因 |
| CREMARKS | string? | 备注 |
| CSOURCE_ID | long? | 来源id |

### TBL_WMS_LOCATION (仓库货位)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CID | long | 主键；常见与 **`TBL_WMS_ITEM_BARCODE.CLOCATION_ID`**、**`TBL_WMS_ITEM_LOCATION.CLOCATION_ID`** 等关联 |
| CLOCATION_SN | string | 货位编码/货位条码 |
| CWAREHOUSE_ID | long | 仓库ID |
| CAREA_ID | long? | 库区 |
| CLOCATION_CODE | string | 货位编码 |
| CLOCATION_NAME | string | 货位名称 |
| CLOCATION_SN | string | 货位条码 |
| CMAX_CAPACITY | decimal? | 最大容量 |
| CMAX_WEIGHT | decimal? | 最大重量 |
| CPACKING_SEQ | int? | 拣货顺序 |
| CREMARK | string | 备注 |
| CSHELVES_CODE | string | 货架编码 |
| CSHELVES_NAME | string | 货架名称 |
| CSOURCE_ID | string | 来源ID |
| CTYPE | string | 货位类型 |
| CWAREHOUSE_ID | long? | 仓库ID |

### TBL_WMS_MANTISSA_RECORD (尾数仓操作记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| CCYCLE | string | 周期 |
| CIN_TIME | DateTime? | 入仓时间 |
| CIN_USER | string | 入仓人 |
| CITEM_NAME | string | 产品 |
| CLOCATION_SN | string | 货位条码 |
| COUT_QTY | int? | 已出仓数量 |
| COUT_TIME | DateTime? | 出仓时间 |
| COUT_USER | string | 出仓人 |
| CQTY | int? | 数量 |
| CREMARK | string | 备注 |
| CSTATUS | int | 1已入仓、2已出仓 |
| CWAREHOUSE_ID | long | 尾数仓ID |

### TBL_WMS_MI (备料单主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CDEPARTMENT_CODE | string | 部门编码 |
| CDEPARTMENT_ID | string | 生产部门ID |
| CMI_DATETIME | DateTime? | 备料单日期 |
| CMI_NO | string | 单号 |
| CMI_TYPE | string | 备料来源单类型 |
| CMITEM_USER | string | 物料员 |
| CMO | string | 生产工单号 |
| CMO_ID | string | 生产工单ID |
| CREMARK | string | 备注 |
| CSOURCE_BILL_ID | string | 来源ID |
| CSOURCE_BILL_NO | string | 来源单号 |
| CSOURCE_BILL_TYPE | string | 来源单源类型 |
| CSTATUS | string | 状态 |
| CWAREHOUSE_ID | long | 仓库ID |
| CWC_ID | long? | 线体Id |

### TBL_WMS_MI_BARCODE (备料条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| CMI_DTL_ID | long | 备料单明细ID |
| CQTY | decimal | 条码发料数量 |

### TBL_WMS_MI_DTL (备料单子表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long | 货位ID |
| CLOSS_RATE | decimal? | 生产损耗率 |
| CMI_ID | long | 主表ID |
| CMO_QTY | decimal? | 工单标准用量 |
| CQTY | decimal? | 应发数量 |
| CREMARK | string | 备注 |
| CRETURN_QTY | decimal? | 退料数量 |
| CSEND_QTY | decimal? | 累计发料数量 |
| CSOURCE_BILL_ID | string | 来源ID |
| CSOURCE_BILL_NO | string | 来源单号 |
| CSOURCE_BILL_ROW | int? | 来源单行 |
| CSOURCE_BILL_TYPE | string | 来源单源类型 |
| CSTATION_CODE | string | 工站编码 |
| CSTATUS | string | 状态 |
| CUNIT | string | 单位 |
| CWP_CODE | string | 工序编码 |

### TBL_WMS_PACKAGE_IN_RECORDS (入库记录表)
（**说明**：货位维度为 **`CLOCATION_CODE`（字符串）**，不是 **`CLOCATION_ID`**；与 **`TBL_WMS_ITEM_LOCATION.CLOCATION_ID`** 衔接须经过 **`TBL_WMS_LOCATION`** 转换。**报废数量 `CSCRAP_QTY`** 不在本主表字段列表，而在 **`TBL_WMS_PACKAGE_IN_RECORDS_BOXES`**。）
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBOX_QTY | int? | 箱数 |
| CDEF_QTY | int? | 叉板数 |
| CIFMIX | string | 是否叉板混箱 |
| CITEM_NO | string | 料号 |
| CITEM_VERSION | string | 料号版本 |
| CLOCATION_CODE | string | 货位编码 |
| CP_IN_CODE | string | 入库单号 |
| CPACK_QTY | int? | 每箱包装数量 |
| CPCS_QTY | int? | 总数 |
| CQUALITY_QTY | int? | 正品数 |
| CWAREHOUSE_CODE | string | 仓库编码 |

### TBL_WMS_PACKAGE_IN_RECORDS_BOXES (入库记录外箱详情表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBOX_CODE | string | 外箱条码 |
| CDATE_CODE | string | 日期码 |
| CPCS_QTY | int? | 箱内PCS数量 |
| CRECORD_ID | long? | 入库记录主表ID |
| CSCRAP_QTY | int? | 报废数量 |
| CTYPE | int? | 明细类型 |
| CX_OUT | string | 外箱扩展标识 |

### TBL_WMS_PI (出入库主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBILL_SOURCE | string | 单据来源 |
| CBILL_TYPE | string | 单据类型 |
| CCUSTOMER_CODE | string | 客户编码 |
| CDEPT_CODE | string | 部门编码 |
| CERP_STATUS | int? | ERP接口状态；0新增；1修改；2删除；9调用成功，10调用失败 |
| COPERATE_TYPE | int | 1扫码入库、2数量入库 |
| CPI_DATETIME | DateTime? | 业务日期 |
| CPI_NO | string | 单号 |
| CRB_FLAG | int? | 红蓝标识；1为正；-1为负--入库为'1' -1 |
| CREMARK | string | 备注 |
| CSALESMAN_CODE | string | 业务员编码 |
| CSOURCE_ID | string | 来源ID |
| CSR_FLAG | int? | 收发标志；1为收；0为发--入库为'0'  0 |
| CSUPPLIER_ID | long? | 供应商ID |
| CWAREHOUSE_ID | long? | 仓库ID |
| CWAREHOUSE_USER | string | 仓管员 |

### TBL_WMS_PICKING_LOG (领料记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CPICKING_CODE | string | 领料单号 |
| CPICKING_QTY | decimal? | 领料数量 |
| CREMARK | string | 备注 |
| CUSER_NAME | string | 领料人 |

### TBL_WMS_PICKING_LOG_DTL (领料记录明细)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE_ID | long? | 条码ID |
| CPICKING_ID | long? | 领料主表ID |
| CQTY | decimal? | 领料数量 |
| CREMARK | string | 备注 |
| CBARCODE_ID | long? | 条码ID |
| CPICKING_ID | long? | 领料记录主表ID |
| CQTY | decimal? | 领料数量 |
| CREMARK | string | 备注 |

### TBL_WMS_PI_BARCODE (出入库条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| CPI_DTL_ID | long | 出入库子表ID |
| CQTY | decimal? | 条码数量 |
| CSTATUS | int? | 状态；0待入库，1已入库，2已备料，3已出库 |

### TBL_WMS_PI_DTL (出入库明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBATCH_NO | string | 批号 |
| CCYCLE | string | 周期 |
| CDETAILS | string | 明细 |
| CERP_STATUS | int? | ERP接口状态；0新增；1修改；2删除；9调用成功，10调用失败 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long? | 货位ID |
| CMO | string | 生产工单号 |
| CNUMBER | int? | 实际出入库件数 |
| CPI_ID | long | 出入库主表ID |
| CPO | string | 采购订单号 |
| CQTY | decimal? | 实际出入库数量 |
| CRB_FLAG | int? | 红蓝标识；1为正；-1为负 |
| CREMARK | string | 备注 |
| CSALE_NO | string | 销售订单号 |
| CSOURCE_BILL_ID | long | 来源单ID；收货单：收货单子表ID |
| CSOURCE_BILL_NO | string | 来源单单号；收货单：收货单号 |
| CSOURCE_BILL_TYPE | string | 来源单类型；收货单、工单领料单、其他领料、退料… |
| CSOURCE_ID | string | 来源ID |
| CSTATUS | int? | 状态；0待入库，1已入库，2已备料，3已出库 |

### TBL_WMS_PRINT_LOG (WMS标签打印日志表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| lotcode | string | 批次号 |
| materialcode | string | 物料编码 |
| materialname | string | 物料名称 |
| order | string | 单据号 |
| printer | string | 打印机名称 |
| qty | int | 打印数量 |

### TBL_WMS_PRODUCT_BARCODE (成品仓条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBALANCE_QTY | decimal? | 剩余数量 |
| CBARCODE | string | 条码 |
| CBARCODE_TYPE | string | 条码类型 |
| CEXPIRATION_TIME | DateTime? | 有效日期 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long? | 货位ID |
| CLOSS_QTY | decimal? | 调整数量 |
| CLOT_NO | string | 批次号 |
| CPACKING_DATETIME | DateTime? | 包箱时间 |
| CPACKING_ID | long? | 包装条码ID |
| CPI_DTL_ID | long? | 入库单明细ID |
| CPRINT_TIMES | int? | 打印次数 |
| CPRODUCTION_DATETIME | DateTime? | 生产时间 |
| CQTY | decimal? | 条码数量 |
| CREMARK | string | 备注 |
| CSCRAP_TIME | DateTime? | 条码报废时间 |
| CSOURCE_ID | long? | 来源ID(来源于TBL_SRM_PO_DETAIL) |
| CSPLIT_DATETIME | DateTime? | 拆分时间 |
| CSPLIT_ID | long? | 上级条码ID |
| CSRC_ID | long? | 来源记录ID（这里保存的是采购订单交付表的ID） |
| CSRC_TYPE | string | 来源类型 |
| CSTATUS | string | 条码状态 |
| CSUPPLIER_ID | long? | 供应商ID |
| CSUPPLIER_LOT_NO | string | 供应商批号 |
| CUNIT | string | 单位 |
| CUSE_QTY | decimal? | 使用数量 |

### TBL_WMS_PS (出货单主表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCHECK_USER | string | 检验员编码 |
| CCUSTOMER_ID | long? | 客户ID |
| CDELIVERY_USER | string | 送货员编码 |
| CDEPARTMENT_ID | long? | 销售部门ID |
| CPS_DATETIME | DateTime? | 日期 |
| CPS_NO | string | 单号 |
| CPS_TYPE | string | 类型 |
| CREMARK | string | 备注 |
| CSALESMAN_CODE | string | 业务员编码 |
| CSOURCE_BILL_ID | string | 来源ID |
| CSTATUS | int? | 状态 |
| CWAREHOUSE_ID | long? | 仓库ID |
| CWAREHOUSE_USER | string | 仓管员编码 |

### TBL_WMS_PS_BARCODE (出货单条码表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE | string | 条码 |
| CPS_DTL_ID | long | 出货单子表ID |

### TBL_WMS_PS_DTL (出货单明细表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUSTOMER_BILL_NO | string | 客户订单号 |
| CCUSTOMER_BILL_ROW | string | 客户订单行 |
| CCUSTOMER_ITEM_CODE | string | 客户物料编码 |
| CITEM_ID | long? | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOC_ID | long? | 货位ID |
| CMI_QTY | decimal? | 备货数量 |
| CPS_QTY | decimal? | CPS_QTY	发货数量 |
| CPSID | long? | 主表关联ID |
| CQTY | decimal? | 订单数量 |
| CSALES_BILL_NO | string | 销售订单号 |
| CSALES_BILL_ROW | string | 销售订单行 |
| CSHIPMENTS_QTY | decimal? | 累计备货数量 |
| CSHIPMENTS_SUM_QTY | decimal? | 累计出货数量 |
| CSOURCE_BILL_ID | string | 来源ID |
| CSTATUS | int? | 状态 |
| CUNIT | string | 单位 |
| REMARK | string | 备注 |

### TBL_WMS_RETURN_MATERIAL (生产退料记录)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCONFIRM_DATE | DateTime? | 确认时间 |
| CCONFIRM_USER | string | 确认人 |
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long | 货位ID |
| CMI_DTL_ID | long | 备料单子表ID |
| CREMARK | string | 备注 |
| CRETURN_QTY | decimal? | 退料数量 |
| CRETURN_TYPE | string | 退料类型 |
| CSTATUS | int? | 状态：0待入库、1已入库 |

### TBL_WMS_SALES_ORDER (销售订单表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CCUSTOMER_CODE | string | 客户编码 |
| CCUSTOMER_ID | string | 客户ID |
| CDELIVERY_ADDR | string | 交货地址 |
| CORIG_CUSTOMER | string | CORIG_CUSTOMER	关联原客户 |
| CREMARK | string | 备注 |
| CRESERVE1 | DateTime? | 预留字段1 |
| CRESERVE10 | string | 预留字段10 |
| CRESERVE2 | DateTime? | 预留字段2 |
| CRESERVE3 | DateTime? | 预留字段3 |
| CRESERVE4 | string | 预留字段4 |
| CRESERVE5 | string | 预留字段5 |
| CRESERVE6 | string | 预留字段6 |
| CRESERVE7 | string | 预留字段7 |
| CRESERVE8 | string | 预留字段8 |
| CRESERVE9 | string | 预留字段9 |
| CSALES_DEPT | string | 销售部门ID |
| CSALES_MAN | string | 业务员 |
| CSO_NO | string | 订单号 |
| CSO_TIME | DateTime? | 订单日期 |
| CSO_TYPE | string | 订单类型 |
| CSOURCE_ID | string | 来源ID |
| CSTATUS | string | 状态 |

### TBL_WMS_STOCKTAKING (盘点单)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CEND_DATE | DateTime | 盘点结束日期 |
| CREMARK | string | 备注 |
| CSTART_DATE | DateTime | 盘点开始日期 |
| CSTATUS | int | 单据状态  1待提交、2已提交 |
| CSTOCKTAKING_NO | string | 盘点单 |
| CSTOCKTAKING_TYPE | string | 盘点类型  数据字典 WMS_STOCKTAKING_TYPE |
| CUSER_NAME | string | 盘点员 |
| CWAREHOUSE_ID | long | 仓库ID |

### TBL_WMS_STOCKTAKING_DTL (盘点单明细表)
（**说明**：部分中络现场库**未部署**该对象，`SELECT` 报 **`Invalid object name`**（错误 **208**）时勿假定存在；盘点业务请以现场 **`sys.tables`** 或 **`INFORMATION_SCHEMA`** 核实真实表名。明细段下列字段以设计文档为准，**无 `CSTATUS` 列**，单据状态见主表 **`TBL_WMS_STOCKTAKING`**。）
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CITEM_ID | long | 外键，产品或物料ID  对应 [TBL_BD_ITEM].[CID] |
| CLOCATION_ID | long | 货位ID  TBL_WMS_LOCATION |
| CLOSS_QTY | double | 盘亏数量 |
| CQTY | double | 盘点数量 |
| CREMARK | string | 备注 |
| CSTOCKTAKING_ID | long | 主表ID  TBL_WMS_STOCKTAKING |
| CSURPLUS_QTY | double | 盘盈数量 |
| CWAREHOUSE_ID | long | 仓库ID  TBL_WMS_WAREHOUSE |

### TBL_WMS_STOCK_BARCODE_LINK (ERP库存与打印条码关联表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CBARCODE_ID | long | 打印条码记录ID |
| CREMARK | string | 备注 |
| CSTOCK_ID | long | ERP库存记录ID |

### TBL_WMS_WAREHOUSE (仓库主数据表)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CWAREHOUSE_CODE | string | 仓库编码 |
| CWAREHOUSE_NAME | string | 仓库名称 |
| CWAREHOUSE_TYPE_ID | long? | 仓库类型ID |
| CDEPARTMENT_CODE | string | 部门编码 |
| CIS_BATCH | string | 是否批号 |
| CIS_POSITION | string | 是否货位 |
| CIS_PRINT | string | 是否打条码 |
| CPERSON_ID | string | 管理员ID |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源ID |
| CWAREHOUSE_ADDRESS | string | 地址 |
| CWAREHOUSE_CODE | string | 仓库编码 |
| CWAREHOUSE_NAME | string | 仓库名称 |
| CWAREHOUSE_TYPE_ID | long | 仓库分类ID |

### TBL_WMS_WAREHOUSE_TYPE (仓库类型)
| 字段名 | 字段类型 | 字段注释 |
|--------|----------|----------|
| CWAREHOUSE_TYPE_CODE | string | 仓库类型编码 |
| CWAREHOUSE_TYPE_NAME | string | 仓库类型名称 |
| CIS_BATCH_CTRL | string | 是否批号 |
| CIS_CHECK | string | 是否检验 |
| CIS_LOCATION_CTRL | string | 是否货位 |
| CIS_PRINT | string | 是否打条码 |
| CREMARK | string | 备注 |
| CSOURCE_ID | string | 来源ID |
| CWAREHOUSE_TYPE_CODE | string | 类别代码 |
| CWAREHOUSE_TYPE_NAME | string | 类别名称 |
| CWAREHOUSE_TYPE_PROPERTY | string | 仓库属性 |

---

## 文档更新记录
| 更新时间 | 更新内容 | 版本 |
|----------|----------|------|
| 本次更新 | 新增品质客诉模块，包含14张表、378个字段 | V2.0 |
| 初始版本 | 包含9个核心模块，203张表、2630个字段 | V1.0 |

## 备注说明
1. 本文档基于中络MES系统数据字典V1.0及品质客诉相关数据字典生成
2. 字段类型中的"?"表示该字段允许为空
3. 部分表注释可能为空，建议结合业务场景进一步完善
4. 品质客诉模块包含检验模板、化验记录、客诉管理等核心业务表
5. 建议定期更新此文档以保持与实际系统结构的一致性
