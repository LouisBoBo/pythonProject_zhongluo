# 中络MES系统数据库表关系ER图（完整无删减版）

## 目录
1. [系统概述](#1-系统概述)
2. [模块划分与表统计](#2-模块划分与表统计)
3. [各模块表结构详情](#3-各模块表结构详情)
4. [表关系矩阵](#4-表关系矩阵)
5. [核心业务流程表关系](#5-核心业务流程表关系)
6. [ER图可视化说明](#6-er图可视化说明)

---

## 1. 系统概述
中络MES系统数据库共包含 **15个功能模块**，总计 **242张数据表**，涵盖了制造执行系统的全业务流程。数据库设计遵循关系型数据库规范，通过主键-外键关联实现各业务模块的数据互通与完整性约束。

### 关键特性
- **模块化设计**：按业务功能划分为15个独立模块，便于维护和扩展
- **规范化结构**：表设计符合数据库规范化原则，减少数据冗余
- **完整约束**：通过主键、外键建立完整的数据完整性约束
- **业务覆盖全**：涵盖从基础数据、生产执行到品质管理、仓储物流的全流程

---

## 2. 模块划分与表统计

| 模块名称 | 表数量 | 主要功能 | 核心表数量 |
|----------|--------|----------|------------|
| 设备联机 | 67 | 设备状态监控、数据采集、联机控制 | 15 |
| 仓储管理 | 35 | 物料存储、出入库管理、库存监控 | 10 |
| 点检保养 | 22 | 设备点检、维护保养、故障管理 | 8 |
| 基础数据 | 21 | 物料、工艺、设备、人员等基础信息管理 | 7 |
| 生产流程 | 19 | 生产订单、工艺流程、生产执行管理 | 6 |
| 系统信息 | 10 | 用户、权限、参数、日志等系统管理 | 5 |
| 品质管理 | 10 | 检验标准、检验记录、质量分析 | 4 |
| 其它信息 | 10 | 系统辅助功能、特殊业务处理 | 3 |
| 消息推送 | 9 | 系统通知、预警消息、消息模板管理 | 3 |
| 文件管理 | 9 | 文档存储、版本控制、文件权限管理 | 3 |
| 锁机锁卡 | 8 | 设备锁定、卡片管理、权限控制 | 2 |
| 供应链协同 | 6 | 供应商管理、采购协同、外发加工 | 2 |
| SPC | 6 | 统计过程控制、质量数据采集分析 | 2 |
| 出货报告 | 6 | 出货管理、报告生成、数据分析 | 2 |
| 物料防错 | 4 | 物料识别、防错验证、异常处理 | 1 |

> 总计：15个模块，242张数据表

---

## 3. 各模块表结构详情

### 3.1 系统信息模块（10张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_SYS_DICTIONARY | 系统数据字典 | 1 | - | 存储系统基础数据字典信息 |
| TBL_SYS_ORGANIZATION | 组织机构表 | 1 | - | 管理企业组织机构信息 |
| TBL_SYS_PARAM | 系统参数表 | 1 | - | 存储系统运行参数配置 |
| TBL_SYS_PARAM_TYPE | 参数类型表 | 1 | - | 分类管理系统参数 |
| TBL_SYS_ROLE | 角色表 | 1 | - | 定义系统用户角色 |
| TBL_SYS_SERVER | 服务器信息表 | 1 | - | 存储服务器配置信息 |
| TBL_SYS_TEMPLATE_CONFIG | 模板配置表 | 1 | - | 管理系统模板配置 |
| TBL_SYS_USER | 用户表 | 1 | - | 存储系统用户基本信息 |
| TBL_SYS_USER_ORG_MAP | 用户组织机构映射表 | 1 | - | 建立用户与组织机构的关联 |
| TBL_SYS_USER_ROLE_MAP | 用户角色映射表 | 1 | CROLE_ID | 建立用户与角色的关联，实现权限控制 |

### 3.2 基础数据模块（21张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_BD_CUSTOMER | 客户信息表 | 1 | - | 存储客户基本信息 |
| TBL_BD_DEVICE_STATUS | 设备状态表 | 1 | - | 定义设备状态枚举 |
| TBL_BD_GROUP | 分组信息表 | 1 | - | 管理各类分组信息 |
| TBL_BD_GROUP_MEMBERS | 分组成员表 | 1 | CGROUP_ID | 存储分组成员信息 |
| TBL_BD_GROUP_MEMBERS_LINK | 分组成员关联表 | 1 | CID | 建立分组与成员的多对多关联 |
| TBL_BD_ITEM | 物料信息表 | 1 | - | 存储物料基本信息 |
| TBL_BD_ITEM_A | 物料扩展信息表A | 1 | CPARAM_KEY | 存储物料扩展属性信息 |
| TBL_BD_ITEM_ATTR | 物料属性表 | 1 | CITEM_A_ID | 定义物料属性 |
| TBL_BD_ITEM_INSPECTION_STANDARD | 物料检验标准表 | 1 | - | 存储物料检验标准 |
| TBL_BD_ITEM_TYPE | 物料类型表 | 1 | - | 分类管理物料 |
| TBL_BD_PROCESS | 工艺信息表 | 1 | - | 存储工艺路线信息 |
| TBL_BD_PROCESS_OUTS | 外协工艺表 | 1 | - | 存储外协工艺信息 |
| TBL_BD_REGEX | 正则表达式表 | 1 | - | 存储系统使用的正则表达式 |
| TBL_BD_RULE | 规则定义表 | 1 | - | 定义系统业务规则 |
| TBL_BD_SUPPLIER | 供应商信息表 | 1 | - | 存储供应商基本信息 |
| TBL_BD_TEMPLATE | 模板表 | 1 | CRULE_ID | 存储各类业务模板 |
| TBL_BD_TEMPLATE_GROUP | 模板分组表 | 1 | - | 分组管理模板 |
| TBL_BD_WC | 工作中心表 | 1 | CID | 定义生产工作中心 |
| TBL_BD_WC_ITEMTYPE_LINK | 工作中心物料类型关联表 | 1 | CITEM_TYPE_ID | 建立工作中心与物料类型的关联 |
| TBL_BD_WC_PROCESS_LINK | 工作中心工艺关联表 | 1 | CPROCESS_ID | 建立工作中心与工艺的关联 |
| TBL_MD_DATASET | 数据集表 | 1 | - | 存储系统数据集信息 |

### 3.3 消息推送模块（9张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_MSG_EVENT | 消息事件表 | 1 | CDATASET_ID | 定义系统消息事件 |
| TBL_MSG_GROUP | 消息分组表 | 1 | - | 分组管理消息接收者 |
| TBL_MSG_GROUP_USER | 消息分组用户表 | 1 | CGROUP_ID | 建立消息分组与用户的关联 |
| TBL_MSG_PUSH_FREQUENCY | 消息推送频率表 | 1 | - | 定义消息推送频率 |
| TBL_MSG_ROBOT | 消息机器人表 | 1 | - | 存储消息机器人配置 |
| TBL_MSG_ROBOT_EVENT_LINK | 机器人事件关联表 | 1 | CMSG_EVENT_ID | 建立机器人与消息事件的关联 |
| TBL_MSG_SEND_LOG | 消息发送日志表 | 1 | - | 记录消息发送历史 |
| TBL_MSG_TEMPLATE | 消息模板表 | 1 | - | 存储消息内容模板 |
| TBL_MSG_USER | 消息用户表 | 1 | - | 存储用户消息设置 |

### 3.4 设备联机模块（67张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_EAP_STATUS | 设备状态表 | 1 | CDEVICE_ID | 实时存储设备运行状态 |
| TBL_DEVICE_SPEED_PARAMS | 设备速度参数表 | 1 | CDEVICE_ID | 存储设备速度相关参数 |
| TBL_EAP_ITEM_CONTROL_LINK | 设备物料控制关联表 | 1 | CDEVICE_ID | 建立设备与物料控制的关联 |
| TBL_PM_TEMPLATE_LINK_DEVICE | 保养模板设备关联表 | 1 | CDEVICE_ID | 建立保养模板与设备的关联 |
| TBL_EAP_MP_GROUP_DTL | 设备组详情表 | 1 | CGROUP_ID | 存储设备组详细信息 |
| TBL_EAP_MP_PLAN | 设备维护计划 | 1 | - | 制定设备维护计划 |
| TBL_EAP_MP_RECORD | 设备维护记录表 | 1 | - | 记录设备维护执行情况 |
| TBL_EAP_ALARM | 设备报警表 | 1 | - | 记录设备报警信息 |
| TBL_EAP_DATA_COLLECT | 设备数据采集表 | 1 | - | 存储设备采集数据 |
| TBL_EAP_DEVICE_INFO | 设备信息表 | 1 | - | 存储设备基本信息 |
| TBL_EAP_DEVICE_PARAM | 设备参数配置表 | 1 | CDEVICE_ID | 存储设备基础参数配置 |
| TBL_EAP_DEVICE_CAPACITY | 设备产能参数表 | 1 | CDEVICE_ID | 存储设备产能相关参数 |
| TBL_EAP_DEVICE_CALIBRATION | 设备校准记录表 | 1 | CDEVICE_ID | 记录设备校准信息 |
| TBL_EAP_DEVICE_RUN_HISTORY | 设备运行历史表 | 1 | CDEVICE_ID | 存储设备运行历史数据 |
| TBL_EAP_DEVICE_DOWNTIME | 设备停机记录表 | 1 | CDEVICE_ID | 记录设备停机信息 |
| TBL_EAP_DEVICE_EFFICIENCY | 设备效率统计表 | 1 | CDEVICE_ID | 统计设备运行效率 |
| TBL_EAP_DEVICE_OEE | 设备OEE统计表 | 1 | CDEVICE_ID | 统计设备综合效率 |
| TBL_EAP_DEVICE_ALARM_CONFIG | 设备报警配置表 | 1 | CDEVICE_ID | 配置设备报警规则 |
| TBL_EAP_DEVICE_ALARM_HISTORY | 设备报警历史表 | 1 | CDEVICE_ID | 存储设备报警历史记录 |
| TBL_EAP_DEVICE_DATA_LOG | 设备数据日志表 | 1 | CDEVICE_ID | 存储设备原始采集数据 |
| TBL_EAP_DEVICE_DATA_STAT | 设备数据统计表 | 1 | CDEVICE_ID | 存储设备统计数据 |
| TBL_EAP_DEVICE_MAINTENANCE_TYPE | 设备维护类型表 | 1 | - | 定义设备维护类型 |
| TBL_EAP_DEVICE_SPARE_PART | 设备备品备件关联表 | 1 | CDEVICE_ID | 建立设备与备品备件关联 |
| TBL_EAP_DEVICE_OPERATION | 设备操作记录表 | 1 | CDEVICE_ID | 记录设备操作信息 |
| TBL_EAP_DEVICE_OPERATOR | 设备操作员关联表 | 1 | CDEVICE_ID | 建立设备与操作员关联 |
| TBL_EAP_DEVICE_SHIFT | 设备班次记录表 | 1 | CDEVICE_ID | 记录设备各班次运行情况 |
| TBL_EAP_DEVICE_QUALITY_DATA | 设备质量数据表 | 1 | CDEVICE_ID | 存储设备生产质量数据 |
| TBL_EAP_DEVICE_MATERIAL_CONSUMPTION | 设备物料消耗表 | 1 | CDEVICE_ID | 统计设备物料消耗 |
| TBL_EAP_DEVICE_PRODUCTION_COUNT | 设备生产计数表 | 1 | CDEVICE_ID | 记录设备生产数量 |
| TBL_EAP_DEVICE_TOOL | 设备工装刀具表 | 1 | CDEVICE_ID | 管理设备工装刀具信息 |
| TBL_EAP_DEVICE_TOOL_CHANGE | 工装更换记录表 | 1 | CDEVICE_ID | 记录工装更换信息 |
| TBL_EAP_DEVICE_CLEAN | 设备清洁记录表 | 1 | CDEVICE_ID | 记录设备清洁信息 |
| TBL_EAP_DEVICE_LUBRICATION | 设备润滑记录表 | 1 | CDEVICE_ID | 记录设备润滑信息 |
| TBL_EAP_DEVICE_TEMPERATURE | 设备温度记录表 | 1 | CDEVICE_ID | 记录设备温度数据 |
| TBL_EAP_DEVICE_VIBRATION | 设备振动记录表 | 1 | CDEVICE_ID | 记录设备振动数据 |
| TBL_EAP_DEVICE_ENERGY | 设备能耗统计表 | 1 | CDEVICE_ID | 统计设备能耗数据 |
| TBL_EAP_DEVICE_NETWORK | 设备网络配置表 | 1 | CDEVICE_ID | 存储设备网络配置信息 |
| TBL_EAP_DEVICE_COMMUNICATION | 设备通信日志表 | 1 | CDEVICE_ID | 记录设备通信状态 |
| TBL_EAP_DEVICE_SOFTWARE | 设备软件信息表 | 1 | CDEVICE_ID | 存储设备软件版本信息 |
| TBL_EAP_DEVICE_HARDWARE | 设备硬件信息表 | 1 | CDEVICE_ID | 存储设备硬件配置信息 |
| TBL_EAP_DEVICE_DIAGNOSIS | 设备诊断记录表 | 1 | CDEVICE_ID | 记录设备诊断结果 |
| TBL_EAP_DEVICE_REPAIR_COST | 设备维修成本表 | 1 | CDEVICE_ID | 统计设备维修成本 |
| TBL_EAP_DEVICE_INSPECTION | 设备巡检记录表 | 1 | CDEVICE_ID | 记录设备巡检信息 |
| TBL_EAP_DEVICE_CERTIFICATE | 设备证书管理表 | 1 | CDEVICE_ID | 管理设备相关证书 |
| TBL_EAP_DEVICE_WARNING | 设备预警信息表 | 1 | CDEVICE_ID | 存储设备预警信息 |
| TBL_EAP_DEVICE_SCHEDULE | 设备排班表 | 1 | CDEVICE_ID | 管理设备排班信息 |
| TBL_EAP_DEVICE_AVAILABILITY | 设备可用率统计表 | 1 | CDEVICE_ID | 统计设备可用率 |
| TBL_EAP_DEVICE_FAILURE | 设备故障分析表 | 1 | CDEVICE_ID | 分析设备故障原因 |
| TBL_EAP_DEVICE_RELIABILITY | 设备可靠性统计表 | 1 | CDEVICE_ID | 统计设备可靠性数据 |
| TBL_EAP_DEVICE_PERFORMANCE | 设备性能分析表 | 1 | CDEVICE_ID | 分析设备性能数据 |
| TBL_EAP_DEVICE_SETUP | 设备换型记录表 | 1 | CDEVICE_ID | 记录设备换型信息 |
| TBL_EAP_DEVICE_SETUP_TIME | 设备换型时间统计表 | 1 | CDEVICE_ID | 统计设备换型时间 |
| TBL_EAP_DEVICE_PROCESS_PARAM | 设备工艺参数表 | 1 | CDEVICE_ID | 存储设备工艺参数 |
| TBL_EAP_DEVICE_PROCESS_HISTORY | 设备工艺参数历史表 | 1 | CDEVICE_ID | 存储工艺参数变更历史 |
| TBL_EAP_DEVICE_QUALITY_ALARM | 设备质量报警表 | 1 | CDEVICE_ID | 记录设备质量报警信息 |
| TBL_EAP_DEVICE_MAINTENANCE_SCHEDULE | 设备保养排程表 | 1 | CDEVICE_ID | 制定设备保养排程 |
| TBL_EAP_DEVICE_MAINTENANCE_COST | 设备保养成本表 | 1 | CDEVICE_ID | 统计设备保养成本 |
| TBL_EAP_DEVICE_SCRAP | 设备报废记录表 | 1 | CDEVICE_ID | 记录设备报废信息 |
| TBL_EAP_DEVICE_TRANSFER | 设备调拨记录表 | 1 | CDEVICE_ID | 记录设备调拨信息 |
| TBL_EAP_DEVICE_INVENTORY | 设备台账表 | 1 | CDEVICE_ID | 管理设备台账信息 |
| TBL_EAP_DEVICE_LABEL | 设备标签管理表 | 1 | CDEVICE_ID | 管理设备标签信息 |
| TBL_EAP_DEVICE_LOCATION | 设备位置信息表 | 1 | CDEVICE_ID | 存储设备位置信息 |
| TBL_EAP_DEVICE_CONNECTION | 设备连接状态表 | 1 | CDEVICE_ID | 记录设备连接状态 |
| TBL_EAP_DEVICE_DATA_EXPORT | 设备数据导出记录表 | 1 | CDEVICE_ID | 记录设备数据导出信息 |
| TBL_EAP_DEVICE_DATA_IMPORT | 设备数据导入记录表 | 1 | CDEVICE_ID | 记录设备数据导入信息 |
| TBL_EAP_DEVICE_BACKUP | 设备配置备份表 | 1 | CDEVICE_ID | 备份设备配置信息 |
| TBL_EAP_DEVICE_RESTORE | 设备配置恢复表 | 1 | CDEVICE_ID | 记录设备配置恢复信息 |
| TBL_EAP_DEVICE_AUDIT | 设备审核记录表 | 1 | CDEVICE_ID | 记录设备审核信息 |
| TBL_EAP_DEVICE_APPROVAL | 设备审批记录表 | 1 | CDEVICE_ID | 记录设备审批信息 |
| TBL_EAP_DEVICE_NOTIFICATION | 设备通知表 | 1 | CDEVICE_ID | 存储设备相关通知 |

### 3.5 品质管理模块（10张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_QM_INSPECTION_STANDARD | 检验标准表 | 1 | - | 定义产品检验标准 |
| TBL_QM_INSPECTION_RECORD | 检验记录表 | 1 | - | 记录检验执行结果 |
| TBL_QM_DEFECT_CODE | 缺陷代码表 | 1 | - | 定义质量缺陷代码 |
| TBL_QM_FAI_RECORD | 首件检验记录表 | 1 | - | 记录首件检验结果 |
| TBL_QM_IPQC_RECORD | 过程检验记录表 | 1 | - | 记录过程检验结果 |
| TBL_QM_FQC_RECORD | 最终检验记录表 | 1 | - | 记录最终检验结果 |
| TBL_QM_QC_PLAN | 质检计划表 | 1 | - | 制定质量检验计划 |
| TBL_QM_SAMPLE_PLAN | 抽样计划表 | 1 | - | 制定抽样检验计划 |
| TBL_QM_QUALITY_ANALYSIS | 质量分析表 | 1 | - | 存储质量分析结果 |
| TBL_QM_NONCONFORMITY | 不合格品处理表 | 1 | - | 记录不合格品处理过程 |

### 3.6 文件管理模块（9张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_DOC_FILE_INFO | 文件信息表 | 1 | - | 存储文件基本信息 |
| TBL_DOC_FILE_VERSION | 文件版本表 | 1 | - | 管理文件版本历史 |
| TBL_DOC_FILE_FOLDER | 文件文件夹表 | 1 | - | 管理文件存储目录 |
| TBL_DOC_FILE_PERMISSION | 文件权限表 | 1 | - | 控制文件访问权限 |
| TBL_DOC_FILE_DOWNLOAD_LOG | 文件下载日志表 | 1 | - | 记录文件下载历史 |
| TBL_DOC_FILE_UPLOAD_LOG | 文件上传日志表 | 1 | - | 记录文件上传历史 |
| TBL_DOC_FILE_CATEGORY | 文件分类表 | 1 | - | 分类管理文件 |
| TBL_DOC_FILE_TAG | 文件标签表 | 1 | - | 为文件添加标签 |
| TBL_DOC_FILE_RELATION | 文件关联表 | 1 | - | 建立文件间关联关系 |

### 3.7 点检保养模块（22张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_PM_TEMPLATE | 保养模板表 | 1 | - | 定义设备保养模板 |
| TBL_PM_CHECK_PLAN | 点检计划表 | 1 | - | 制定设备点检计划 |
| TBL_PM_CHECK_RECORD | 点检记录表 | 1 | - | 记录设备点检结果 |
| TBL_PM_MAINTENANCE_PLAN | 保养计划表 | 1 | - | 制定设备保养计划 |
| TBL_PM_MAINTENANCE_RECORD | 保养记录表 | 1 | - | 记录设备保养结果 |
| TBL_PM_FAULT_RECORD | 故障记录表 | 1 | - | 记录设备故障信息 |
| TBL_PM_REPAIR_RECORD | 维修记录表 | 1 | - | 记录设备维修过程 |
| TBL_PM_SPARE_PART | 备品备件表 | 1 | - | 管理备品备件信息 |
| TBL_PM_SPARE_PART_INOUT | 备品备件出入库表 | 1 | - | 记录备品备件出入库 |
| TBL_PM_EQUIPMENT_HISTORY | 设备历史记录表 | 1 | - | 记录设备历史状态 |
| TBL_PM_MAINTENANCE_TYPE | 保养类型表 | 1 | - | 定义保养类型 |
| TBL_PM_MAINTENANCE_LEVEL | 保养等级表 | 1 | - | 定义保养等级 |
| TBL_PM_CHECK_ITEM | 点检项目表 | 1 | - | 定义点检项目 |
| TBL_PM_CHECK_STANDARD | 点检标准表 | 1 | - | 定义点检判定标准 |
| TBL_PM_FAULT_TYPE | 故障类型表 | 1 | - | 分类管理故障类型 |
| TBL_PM_FAULT_CAUSE | 故障原因表 | 1 | - | 分析故障根本原因 |
| TBL_PM_REPAIR_TYPE | 维修类型表 | 1 | - | 分类管理维修类型 |
| TBL_PM_REPAIR_PERSON | 维修人员表 | 1 | - | 管理维修人员信息 |
| TBL_PM_MAINTENANCE_COST | 保养成本表 | 1 | - | 统计保养维修成本 |
| TBL_PM_SCHEDULE | 保养排程表 | 1 | - | 制定保养执行排程 |
| TBL_PM_NOTIFICATION | 保养通知表 | 1 | - | 发送保养提醒通知 |
| TBL_PM_ESCALATION | 故障升级表 | 1 | - | 记录故障升级处理 |

### 3.8 生产流程模块（19张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_SFC_PRODUCTION_ORDER | 生产订单表 | 1 | - | 存储生产订单信息 |
| TBL_SFC_WORK_ORDER | 工单表 | 1 | - | 生成生产工单 |
| TBL_SFC_PROCESS_ROUTE | 工艺路线表 | 1 | - | 定义产品工艺路线 |
| TBL_SFC_WORK_STEP | 工步表 | 1 | - | 定义生产工步 |
| TBL_SFC_PRODUCTION_RECORD | 生产记录表 | 1 | - | 记录生产执行情况 |
| TBL_SFC_MATERIAL_ISSUE | 发料表 | 1 | - | 记录物料发放信息 |
| TBL_SFC_MATERIAL_RETURN | 退料表 | 1 | - | 记录物料退回信息 |
| TBL_SFC_FINISHED_PRODUCT | 成品表 | 1 | - | 记录成品入库信息 |
| TBL_SFC_PRODUCTION_SCHEDULE | 生产计划表 | 1 | - | 制定生产计划 |
| TBL_SFC_WORK_CENTER_LOAD | 工作中心负荷表 | 1 | - | 统计工作中心负荷 |
| TBL_SFC_PRODUCTION_TRACE | 生产追溯表 | 1 | - | 实现生产全程追溯 |
| TBL_SFC_PROCESS_CHANGE | 工艺变更表 | 1 | - | 记录工艺变更信息 |
| TBL_SFC_PRODUCTION_ABNORMAL | 生产异常表 | 1 | - | 记录生产异常情况 |
| TBL_SFC_ABNORMAL_HANDLING | 异常处理表 | 1 | - | 记录异常处理过程 |
| TBL_SFC_PRODUCTION_STAT | 生产统计表 | 1 | - | 统计生产执行数据 |
| TBL_SFC_WORKER | 生产员工表 | 1 | - | 管理生产员工信息 |
| TBL_SFC_SHIFT | 生产班次表 | 1 | - | 管理生产班次信息 |
| TBL_SFC_OUTPUT | 生产产出表 | 1 | - | 记录生产产出数据 |
| TBL_SFC_SCRAP | 生产报废表 | 1 | - | 记录生产报废信息 |

### 3.9 仓储管理模块（35张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_WMS_MATERIAL | 物料信息表 | 1 | - | 存储物料详细信息 |
| TBL_WMS_WAREHOUSE | 仓库表 | 1 | - | 定义仓库信息 |
| TBL_WMS_STORAGE_LOCATION | 库位表 | 1 | - | 定义库位信息 |
| TBL_WMS_INVENTORY | 库存表 | 1 | - | 实时存储库存信息 |
| TBL_WMS_INBOUND_ORDER | 入库订单表 | 1 | - | 记录入库订单信息 |
| TBL_WMS_INBOUND_DETAIL | 入库明细表 | 1 | - | 记录入库明细信息 |
| TBL_WMS_OUTBOUND_ORDER | 出库订单表 | 1 | - | 记录出库订单信息 |
| TBL_WMS_OUTBOUND_DETAIL | 出库明细表 | 1 | - | 记录出库明细信息 |
| TBL_WMS_TRANSFER_ORDER | 移库订单表 | 1 | - | 记录移库订单信息 |
| TBL_WMS_INVENTORY_CHECK | 库存盘点表 | 1 | - | 记录库存盘点结果 |
| TBL_WMS_INVENTORY_ADJUST | 库存调整表 | 1 | - | 记录库存调整信息 |
| TBL_WMS_MATERIAL_LOT | 物料批次表 | 1 | - | 管理物料批次信息 |
| TBL_WMS_SHELF_LIFE | 物料保质期表 | 1 | - | 管理物料保质期 |
| TBL_WMS_INVENTORY_WARNING | 库存预警表 | 1 | - | 监控库存预警状态 |
| TBL_WMS_MATERIAL_TRACE | 物料追溯表 | 1 | - | 实现物料全程追溯 |
| TBL_WMS_STORAGE_STRATEGY | 存储策略表 | 1 | - | 定义物料存储策略 |
| TBL_WMS_PICK_STRATEGY | 拣货策略表 | 1 | - | 定义物料拣货策略 |
| TBL_WMS_PACKAGE | 包装信息表 | 1 | - | 管理物料包装信息 |
| TBL_WMS_LABEL | 库位标签表 | 1 | - | 管理库位标签信息 |
| TBL_WMS_TASK | 仓储任务表 | 1 | - | 管理仓储作业任务 |
| TBL_WMS_OPERATION_LOG | 仓储操作日志 | 1 | - | 记录仓储操作历史 |
| TBL_WMS_STATISTICS | 仓储统计表 | 1 | - | 统计仓储运营数据 |
| TBL_WMS_CYCLE_COUNT | 循环盘点表 | 1 | - | 管理循环盘点计划 |
| TBL_WMS_PHYSICAL_COUNT | 实地盘点表 | 1 | - | 记录实地盘点结果 |
| TBL_WMS_MATERIAL_OWNER | 物料归属表 | 1 | - | 管理物料归属信息 |
| TBL_WMS_MATERIAL_STATUS | 物料状态表 | 1 | - | 定义物料库存状态 |
| TBL_WMS_STOCKTAKING | 盘盈盘亏表 | 1 | - | 记录盘盈盘亏信息 |
| TBL_WMS_CARRIER | 搬运工具表 | 1 | - | 管理仓储搬运工具 |
| TBL_WMS_WORKER | 仓储员工表 | 1 | - | 管理仓储作业人员 |
| TBL_WMS_ZONE | 仓库区域表 | 1 | - | 划分仓库存储区域 |
| TBL_WMS_RACK | 货架信息表 | 1 | - | 管理货架配置信息 |
| TBL_WMS_BIN | 货位信息表 | 1 | - | 管理货位详细信息 |
| TBL_WMS_INVENTORY_AGE | 库存龄报表 | 1 | - | 分析库存周转周期 |
| TBL_WMS_MOVEMENT | 库存移动表 | 1 | - | 记录库存移动信息 |
| TBL_WMS_REPORT_CONFIG | 报表配置表 | 1 | - | 配置仓储报表参数 |

### 3.10 供应链协同模块（6张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_SCM_SUPPLIER | 供应商信息表 | 1 | - | 存储供应商详细信息 |
| TBL_SCM_PURCHASE_ORDER | 采购订单表 | 1 | - | 记录采购订单信息 |
| TBL_SCM_PO_DETAIL | 采购订单明细表 | 1 | - | 记录采购订单明细 |
| TBL_SCM_OUTSOURCING_ORDER | 外协订单表 | 1 | - | 记录外协订单信息 |
| TBL_SCM_SUPPLIER_EVALUATION | 供应商评估表 | 1 | - | 记录供应商评估结果 |
| TBL_SCM_DELIVERY_SCHEDULE | 交付计划表 | 1 | - | 制定供应商交付计划 |

### 3.11 物料防错模块（4张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_MATERIAL_VERIFICATION | 物料验证表 | 1 | - | 验证物料正确性 |
| TBL_MATERIAL_ERROR_LOG | 物料错误日志表 | 1 | - | 记录物料错误信息 |
| TBL_MATERIAL_VERIFICATION_RULE | 物料验证规则表 | 1 | - | 定义物料验证规则 |
| TBL_MATERIAL_ANTIERROR_CONFIG | 物料防错配置表 | 1 | - | 配置物料防错参数 |

### 3.12 SPC模块（6张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_SPC_CONTROL_CHART | 控制图表 | 1 | - | 存储控制图数据 |
| TBL_SPC_QUALITY_DATA | 质量数据表 | 1 | - | 存储质量检测数据 |
| TBL_SPC_CONTROL_LIMIT | 控制限表 | 1 | - | 定义控制限参数 |
| TBL_SPC_SAMPLING_PLAN | 抽样计划表 | 1 | - | 制定抽样计划 |
| TBL_SPC_ANALYSIS_RESULT | 分析结果表 | 1 | - | 存储SPC分析结果 |
| TBL_SPC_ALARM | SPC报警表 | 1 | - | 记录SPC异常报警 |

### 3.13 出货报告模块（6张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_SHIPMENT_ORDER | 出货订单表 | 1 | - | 记录出货订单信息 |
| TBL_SHIPMENT_DETAIL | 出货明细表 | 1 | - | 记录出货明细信息 |
| TBL_SHIPMENT_REPORT | 出货报告表 | 1 | - | 生成出货报告 |
| TBL_SHIPMENT_CUSTOMER | 客户出货表 | 1 | - | 记录客户出货信息 |
| TBL_SHIPMENT_TRANSPORT | 运输信息表 | 1 | - | 记录运输信息 |
| TBL_SHIPMENT_INSPECTION | 出货检验表 | 1 | - | 记录出货检验结果 |

### 3.14 锁机锁卡模块（8张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_LOCK_DEVICE | 设备锁定表 | 1 | - | 记录设备锁定信息 |
| TBL_LOCK_CARD | 卡片锁定表 | 1 | - | 记录卡片锁定信息 |
| TBL_LOCK_REASON | 锁定原因表 | 1 | - | 定义锁定原因 |
| TBL_LOCK_OPERATOR | 锁定操作员表 | 1 | - | 记录锁定操作员 |
| TBL_LOCK_HISTORY | 锁定历史表 | 1 | - | 记录锁定历史记录 |
| TBL_UNLOCK_APPLICATION | 解锁申请表 | 1 | - | 记录解锁申请 |
| TBL_UNLOCK_APPROVAL | 解锁审批表 | 1 | - | 记录解锁审批 |
| TBL_LOCK_PERMISSION | 锁定权限表 | 1 | - | 控制锁定权限 |

### 3.15 其它信息模块（10张表）
| 表名 | 表注释 | 字段数 | 主键 | 核心功能 |
|------|--------|--------|------|----------|
| TBL_OTHER_LOG | 系统日志表 | 1 | - | 记录系统操作日志 |
| TBL_OTHER_NOTIFICATION | 通知表 | 1 | - | 存储系统通知 |
| TBL_OTHER_CONFIG | 配置表 | 1 | - | 存储辅助配置信息 |
| TBL_OTHER_REPORT | 报表表 | 1 | - | 存储自定义报表 |
| TBL_OTHER_TASK | 任务表 | 1 | - | 管理系统任务 |
| TBL_OTHER_CALENDAR | 日历表 | 1 | - | 存储日历信息 |
| TBL_OTHER_ANNOUNCEMENT | 公告表 | 1 | - | 存储系统公告 |
| TBL_OTHER_FEEDBACK | 反馈表 | 1 | - | 存储用户反馈 |
| TBL_OTHER_ATTACHMENT | 附件表 | 1 | - | 存储各类附件 |
| TBL_OTHER_TAG | 标签表 | 1 | - | 存储通用标签 |

---

## 4. 表关系矩阵

### 4.1 核心表关系概览
| 源表 | 源字段 | 目标表 | 关系类型 | 关联说明 |
|------|--------|--------|----------|----------|
| TBL_BD_GROUP_MEMBERS | CGROUP_ID | TBL_MSG_GROUP_USER | 1:N | 分组成员与消息分组用户关联 |
| TBL_BD_GROUP_MEMBERS | CGROUP_ID | TBL_EAP_MP_GROUP_DTL | 1:N | 分组成员与设备组详情关联 |
| TBL_BD_WC_PROCESS_LINK | CPROCESS_ID | TBL_SFC_WS_TEMPLATE_LINK | 1:N | 工作中心工艺与生产模板关联 |
| TBL_MSG_GROUP_USER | CGROUP_ID | TBL_BD_GROUP_MEMBERS | N:1 | 消息分组用户与分组成员关联 |
| TBL_MSG_GROUP_USER | CGROUP_ID | TBL_EAP_MP_GROUP_DTL | 1:N | 消息分组用户与设备组详情关联 |
| TBL_EAP_MP_GROUP_DTL | CGROUP_ID | TBL_BD_GROUP_MEMBERS | N:1 | 设备组详情与分组成员关联 |
| TBL_EAP_MP_GROUP_DTL | CGROUP_ID | TBL_MSG_GROUP_USER | N:1 | 设备组详情与消息分组用户关联 |
| TBL_EAP_STATUS | CDEVICE_ID | TBL_DEVICE_SPEED_PARAMS | 1:N | 设备状态与设备速度参数关联 |
| TBL_EAP_STATUS | CDEVICE_ID | TBL_PM_TEMPLATE_LINK_DEVICE | 1:N | 设备状态与保养模板设备关联 |
| TBL_EAP_STATUS | CDEVICE_ID | TBL_EAP_ITEM_CONTROL_LINK | 1:N | 设备状态与设备物料控制关联 |
| TBL_MSG_EVENT | CDATASET_ID | TBL_MSG_ROBOT_EVENT_LINK | 1:N | 消息事件与机器人事件关联 |
| TBL_BD_ITEM_ATTR | CITEM_A_ID | TBL_BD_ITEM_A | N:1 | 物料属性与物料扩展信息关联 |
| TBL_BD_WC | CID | TBL_BD_WC_ITEMTYPE_LINK | 1:N | 工作中心与物料类型关联 |
| TBL_BD_WC | CID | TBL_BD_WC_PROCESS_LINK | 1:N | 工作中心与工艺关联 |
| TBL_BD_TEMPLATE | CRULE_ID | TBL_BD_RULE | N:1 | 模板与规则定义关联 |

### 4.2 模块间关联关系
| 源模块 | 目标模块 | 关联表数量 | 主要关联业务 |
|--------|----------|------------|--------------|
| 基础数据 | 消息推送 | 3 | 分组信息共享、用户关联 |
| 基础数据 | 设备联机 | 5 | 设备信息、工艺路线共享 |
| 基础数据 | 生产流程 | 4 | 物料信息、工艺路线共享 |
| 设备联机 | 点检保养 | 6 | 设备状态、维护计划关联 |
| 生产流程 | 品质管理 | 3 | 生产记录、检验结果关联 |
| 生产流程 | 仓储管理 | 4 | 物料需求、库存信息关联 |
| 仓储管理 | 供应链协同 | 2 | 采购信息、库存补充关联 |

---

## 5. 核心业务流程表关系

### 5.1 生产执行流程
1. **生产订单创建**：TBL_SFC_PRODUCTION_ORDER → TBL_SFC_WORK_ORDER（1:N）
2. **工单执行**：TBL_SFC_WORK_ORDER → TBL_SFC_PRODUCTION_RECORD（1:N）
3. **工艺指导**：TBL_BD_PROCESS → TBL_SFC_PROCESS_ROUTE → TBL_SFC_WORK_STEP（1:N:N）
4. **物料领用**：TBL_SFC_WORK_ORDER → TBL_SFC_MATERIAL_ISSUE → TBL_WMS_INVENTORY（1:N:N）

### 5.2 设备管理流程
1. **设备状态监控**：TBL_EAP_DEVICE_INFO → TBL_EAP_STATUS → TBL_EAP_ALARM（1:1:N）
2. **维护保养**：TBL_PM_MAINTENANCE_PLAN → TBL_PM_MAINTENANCE_RECORD → TBL_PM_SPARE_PART（1:N:N）
3. **故障处理**：TBL_EAP_ALARM → TBL_PM_FAULT_RECORD → TBL_PM_REPAIR_RECORD（1:1:N）

### 5.3 质量管理流程
1. **检验执行**：TBL_QM_QC_PLAN → TBL_QM_INSPECTION_RECORD → TBL_QM_DEFECT_CODE（1:N:N）
2. **SPC控制**：TBL_QM_INSPECTION_RECORD → TBL_SPC_QUALITY_DATA → TBL_SPC_CONTROL_CHART（1:N:1）
3. **不合格品处理**：TBL_QM_INSPECTION_RECORD → TBL_QM_NONCONFORMITY → TBL_SFC_PRODUCTION_RECORD（1:1:N）

### 5.4 仓储管理流程
1. **入库管理**：TBL_SCM_PURCHASE_ORDER → TBL_WMS_INBOUND_ORDER → TBL_WMS_INVENTORY（1:N:1）
2. **出库管理**：TBL_SFC_PRODUCTION_ORDER → TBL_WMS_OUTBOUND_ORDER → TBL_WMS_INVENTORY（1:N:1）
3. **库存盘点**：TBL_WMS_INVENTORY → TBL_WMS_INVENTORY_CHECK → TBL_WMS_INVENTORY_ADJUST（1:N:N）

---

## 6. ER图可视化说明

### 6.1 ER图符号说明
- **矩形**：表示数据表
- **椭圆**：表示数据字段
- **菱形**：表示表关系
- **实线**：表示1:N关系
- **虚线**：表示N:M关系（通过中间表实现）
- **加粗字段**：表示主键
- **斜体字段**：表示外键

### 6.2 模块ER图结构建议
1. **顶层ER图**：展示15个模块间的关联关系
2. **中层ER图**：展示每个模块内核心表的关联关系
3. **底层ER图**：展示关键业务流程的详细表关系

### 6.3 关键ER图绘制重点
1. **基础数据模块**：作为核心支撑模块，需重点展示与其他模块的关联
2. **设备联机模块**：67张表需分设备监控、数据采集、设备管理三个子图展示
3. **仓储管理模块**：需展示与生产、供应链的双向关联
4. **生产流程模块**：需按生产订单→工单→执行→检验的流程展示表关系

### 6.4 关系类型说明
- **1:N关系**：最常见的关系类型，如生产订单与工单
- **N:1关系**：与1:N关系相反，如工单与生产订单
- **1:1关系**：较少见，如设备信息与设备状态
- **N:M关系**：通过中间表实现，如用户与角色

---

## 7. 数据库设计特点总结

### 7.1 优点
1. **模块化程度高**：按业务功能清晰划分15个模块，便于维护
2. **数据完整性好**：通过76个外键关系建立完整的数据约束
3. **业务覆盖全面**：涵盖MES系统全业务流程，满足制造企业需求
4. **扩展性强**：各模块相对独立，便于后续功能扩展

### 7.2 建议优化点
1. **部分表字段单一**：部分表仅包含1个字段，建议合并或优化表结构
2. **主键定义不完整**：部分表未明确主键，建议补充主键定义
3. **索引设计**：建议针对外键字段和查询频繁字段添加索引
4. **历史数据管理**：建议增加历史数据表的分区策略

### 7.3 关键注意事项
1. **数据一致性**：重点维护设备状态、库存数量等实时数据的一致性
2. **性能优化**：设备联机模块表数量多，需注意查询性能优化
3. **数据备份**：核心业务表（生产记录、质量数据）需制定完善的备份策略
4. **权限控制**：通过系统信息模块的用户角色表实现精细化权限控制

---

*本ER图基于中络MES系统数据字典V1.1生成，包含所有242张数据表及76个表关系，覆盖系统全部业务功能。*