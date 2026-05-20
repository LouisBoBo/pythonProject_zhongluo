MES系统数据字典
一、系统信息
1. TBL_SYS_DICTIONARY（数据字典）
- 业务含义：存储系统数据字典，用于维护下拉选项、枚举值等基础数据。
- 字段列表：
  - CCODE_PATH string 字典描述
  - CDIC_CODE string 字典代码
  - CDIC_DESC string 字典描述
  - CDIC_GROUP_VALUE_EXPRESSION string 字典值表达式
  - CDIC_GROUP_VALUE_TYPE string 字典值类型
  - CDIC_NAME string 字典名称
  - CDIC_TYPE string 字典类型
  - CDIC_VALUE string 字典值
  - CDIC_VALUE_EX string 字典值扩展
  - CIS_CATEGORY string 是否系统级
  - CIS_DEFAULT string 是否默认
  - CIS_SYS string 是否系统级
  - CNAME_PATH string 字典描述
  - CPARENT string 父字典ID
  - CPARENT_DIC_ID long 父字典ID
  - CSEQ int? 字典在分组中的顺序
- 关联关系：
  - TBL_SYS_DICTIONARY.CPARENT_DIC_ID = TBL_SYS_DICTIONARY.CID

----------------------
2. TBL_SYS_ORGANIZATION（组织机构表）
- 业务含义：组织机构表，存储公司、部门、车间等组织架构信息。
- 字段列表：
  - CID long 主键ID
  - CORG_NAME string 组织名称
  - CORG_NO string 组织编码
  - CPARENT_ORG_ID long? 上级组织ID
- 关联关系：
  - TBL_SYS_ORGANIZATION.CPARENT_ORG_ID = TBL_SYS_ORGANIZATION.CID

----------------------
3. TBL_SYS_PARAM（系统参数配置表）
- 业务含义：系统参数配置表，存储系统运行所需的各类参数配置。
- 字段列表：
  - CID long 主键ID
  - CIS_SYS string 是否系统级
  - CPARAM_CODE string 参数编码
  - CPARAM_DESC string 参数描述
  - CPARAM_NAME string 参数名称
  - CPARAM_TYPE long? 参数分类
  - CPARAM_VALUE string 参数值
  - CPARAM_VALUE_EXPR string 参数校验表达式
  - CPARAM_VALUE_EXT string 参数扩展值
  - CPARAM_VALUE_SHOW_TYPE string 参数值显示类型
  - CPARAM_VALUE_SOURCE string 参数值来源
  - CPARAM_VALUE_TYPE string 参数值类型
  - CREMARK string 备注信息
  - CSEQ int? 参数在分组中的顺序
- 关联关系：
  - TBL_SYS_PARAM.CPARAM_TYPE = TBL_SYS_PARAM_TYPE.CID

----------------------
4. TBL_SYS_PARAM_TYPE（系统参数分类表）
- 业务含义：系统参数分类表，对系统参数进行分类管理。
- 字段列表：
  - CID long 主键ID
  - CPARAM_TYPE_DESC string 类别描述
  - CPARAM_TYPE_NAME string 类别名称
  - CPARAM_TYPE_NO string 类别代码
  - CPARAM_TYPE_PATH string 类别路径
  - CPARENT_ID long 上级分类
  - CREMARK string 备注
  - CSEQ int? 父级下的顺序号
- 关联关系：
  - TBL_SYS_PARAM_TYPE.CPARENT_ID = TBL_SYS_PARAM_TYPE.CID

----------------------
5. TBL_SYS_ROLE（系统角色表）
- 业务含义：系统角色表，定义用户角色。
- 字段列表：
  - CID long 主键ID
  - CROLE_CODE string 角色编码
  - CROLE_NAME string 角色名称

----------------------
6. TBL_SYS_SERVER（系统服务配置表）
- 业务含义：系统服务配置表，存储各服务连接配置。
- 字段列表：
  - CID long 主键ID
  - CSERVICE_NAME string 服务名称
  - CSERVICE_NO string 服务编码
  - CSERVICE_PASSWORD string 服务密码
  - CSERVICE_PATH string 服务地址
  - CSERVICE_USER string 服务账号

----------------------
7. TBL_SYS_TEMPLATE_CONFIG（系统模板配置表）
- 业务含义：系统模板配置表，存储Excel导出/打印模板配置。
- 字段列表：
  - CID long 主键ID
  - CBINDING string Excel单元格绑定数据源信息序列化后的json字符串
  - CBUCKET_NAME string 模板文件MinIO桶名称
  - CCODE string 模板编码
  - CDATA string 绑定数据源列表序列化后的json字符串
  - CDESC string 模板描述
  - CFILE_NAME string 上传的模板文件名称
  - CFILE_PATH string 模板文件MinIO路径
  - CNAME string 模板名称
  - DataSetId long 数据集Id
  - DataSetName string 数据集名称
  - DataSourceId long 数据源Id
  - DataSourceName string 数据源名称
  - ObjectName string 对象名称

----------------------
8. TBL_SYS_USER（系统用户表）
- 业务含义：系统用户表，存储登录用户账号信息。
- 字段列表：
  - CID long 主键ID
  - CCUR_HOST string 当前登录主机
  - CDATETIME_LAST_LOCKED_OUT DateTime 最后锁定时间
  - CDATETIME_LAST_LOGIN DateTime 最后登录时间
  - CDEFAULT_HOST string 默认登录主机
  - CDISPLAY_NAME string 用户显示名
  - CEMAIL string 邮箱
  - CENTERPRISE_CODE long 企业编码
  - CFAILED_ATTEMPT_COUNT int 登录失败次数
  - CFAILED_ATTEMPT_START DateTime 失败计数开始时间
  - CGENDER string 性别
  - CIS_LOCKED_OUT string 是否锁定
  - CIS_ONLINE string 是否在线
  - CMOBILEPHONE string 手机号
  - CORG_CODE long 组织编码
  - CPASSWORD string 密码
  - CUSER_NAME string 用户账号
  - CUSER_TYPE string 用户类型
- 关联关系：
  - TBL_SYS_USER.CORG_CODE = TBL_SYS_ORGANIZATION.CORG_NO
  - TBL_SYS_USER.CID = TBL_SYS_USER_ORG_MAP.CUSER_ID
  - TBL_SYS_USER.CID = TBL_SYS_USER_ROLE_MAP.CUSER_ID

----------------------
9. TBL_SYS_USER_ORG_MAP（用户组织关系）
- 业务含义：用户与组织关联表，记录用户所属组织及默认组织。
- 字段列表：
  - CID long 主键ID
  - CIS_DEFAULT string 是否默认组织
  - CIS_DEPT_MANAGER string 是否部门负责人
  - CORG_ID long 组织ID
  - CUSER_ID long 用户ID
- 关联关系：
  - TBL_SYS_USER_ORG_MAP.CUSER_ID = TBL_SYS_USER.CID
  - TBL_SYS_USER_ORG_MAP.CORG_ID = TBL_SYS_ORGANIZATION.CID

----------------------
10. TBL_SYS_USER_ROLE_MAP（用户角色关系表）
- 业务含义：用户与角色关联表，记录用户分配的角色。
- 字段列表：
  - CID long 主键ID
  - CROLE_ID long 角色ID
  - CUSER_ID long 用户ID
- 关联关系：
  - TBL_SYS_USER_ROLE_MAP.CUSER_ID = TBL_SYS_USER.CID
  - TBL_SYS_USER_ROLE_MAP.CROLE_ID = TBL_SYS_ROLE.CID

---
二、基础数据

----------------------
11. TBL_BD_CUSTOMER（客户信息表）
- 业务含义：客户主数据表，存储客户基本信息。
- 字段列表：
  - CID long 主键ID
  - CUSTOMER_NAME string 客户名称
  - CUSTOMER_NO string 客户编号

----------------------
12. TBL_BD_DEVICE_STATUS（采集设备实时状态表）
- 业务含义：采集设备实时状态表（疑似弃用），记录设备状态。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 记录创建时间
  - CSTATUS_CODE int 设备状态编码
  - CSTATUS_NAME string 设备状态名称

----------------------
13. TBL_BD_GROUP（组别）
- 业务含义：组别主表，定义各类业务组。
- 字段列表：
  - CID long 主键ID
  - CGROUP_NAME string 组别名称
  - CGROUP_NO string 组别编号

----------------------
14. TBL_BD_GROUP_MEMBERS（组员）
- 业务含义：组员信息表，存储组员基本信息。
- 字段列表：
  - CID long 主键ID
  - CGROUP_ID long 组别ID
  - CUSER_NAME string 姓名
  - CUSER_NO string 工号

----------------------
15. TBL_BD_GROUP_MEMBERS_LINK（组别与成员关系映射表）
- 业务含义：组别与成员关联表，建立组和用户的多对多关系。
- 字段列表：
  - CID long 主键ID
  - GROUP_ID long 组别ID
  - USER_ID long 用户ID
- 关联关系：
  - TBL_BD_GROUP_MEMBERS_LINK.GROUP_ID = TBL_BD_GROUP.CID
  - TBL_BD_GROUP_MEMBERS_LINK.USER_ID = TBL_SYS_USER.CID

----------------------
16. TBL_BD_ITEM（产品和物料信息表）
- 业务含义：产品和物料主数据表，存储料号、规格、客户物料信息等。
- 字段列表：
  - CID long 主键ID
  - CBOX_QTY decimal? 每箱标准数
  - CCUSTOMER_MATER_NAME string 客户物料名称
  - CCUSTOMER_MATER_NO string 客户物料编号
  - CCUSTOMER_MATERIAL string 客户材料
  - CCUSTOMER_MODEL string 客户型号
  - CHEIGHT decimal? 高度
  - CITEM_DESC string 产品描述
  - CITEM_NAME string 产品名称
  - CITEM_NO string 产品编号
  - CITEM_SOURCE string 产品来源
  - CITEM_SPEC string 产品规格
  - CITEM_TYPE_ID long? 产品类型ID
  - CITEM_VERSION string 产品版本
  - CITEM_WEIGHT decimal? 产品单重
  - CLEN decimal? 长度
  - CPACKAGE_QTY decimal? 单包数量
  - CPLATE_WEIGHT decimal? 隔板重量
  - CROUTE_ID string 工艺路线ID
  - CTYPE string? 类型
  - CUSTOMER_CODE string 客户代码
  - CWIDTH decimal? 宽度
- 关联关系：
  - TBL_BD_ITEM.CITEM_TYPE_ID = TBL_BD_ITEM_TYPE.CID
  - TBL_BD_ITEM.CUSTOMER_CODE = TBL_BD_CUSTOMER.CUSTOMER_NO

----------------------
17. TBL_BD_ITEM_A（产品属性）
- 业务含义：产品属性定义表，存储属性键值对模板。
- 字段列表：
  - CID long 主键ID
  - CPARAM_KEY string 属性键
  - CPARAM_VALUE string 属性默认值

----------------------
18. TBL_BD_ITEM_ATTR（产品属性）
- 业务含义：产品属性值表，存储具体物料的实际属性值。
- 字段列表：
  - CID long 主键ID
  - CITEM_A_ID long 物料属性配置ID
  - CITEM_ID long 物料ID
  - CPARAM_KEY string 属性键
  - CPARAM_VALUE string 属性值
- 关联关系：
  - TBL_BD_ITEM_ATTR.CITEM_ID = TBL_BD_ITEM.CID

----------------------
19. TBL_BD_ITEM_INSPECTION_STANDARD（物料检验标准配置表）
- 业务含义：物料检验标准配置表，定义各工序的检验标准。
- 字段列表：
  - CID long 主键ID
  - CCOMPARE_SYMBOL string 比较符号
  - CINSPECTION_TYPE string 检验类型
  - CITEM_ID Int64 物料ID
  - CMAX_STANDARD decimal? 标准上限
  - CMAX_TOLERANCE decimal? 最大公差
  - CMAX_WARN decimal? 预警值上限
  - CMIN_STANDARD decimal? 标准下限
  - CMIN_TOLERANCE decimal? 最小公差
  - CMIN_WARN decimal? 预警值下限
  - CPROCESS_ID Int64 工序ID
  - CREAL_MAX_STANDARD decimal? 实际标准上限
  - CREAL_MIN_STANDARD decimal? 实际标准下限
  - CREMARK string 备注
  - CSTANDARD string 标准文本值
  - CTEMP_ID Int64 模板ID
  - CTEMP_ITEM_ID Int64 模板项ID
  - CTYPE int 标准类型
- 关联关系：
  - TBL_BD_ITEM_INSPECTION_STANDARD.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_BD_ITEM_INSPECTION_STANDARD.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------
20. TBL_BD_ITEM_TYPE（产品和物料类型表）
- 业务含义：物料类型定义表，支持树形分类。
- 字段列表：
  - CID long 主键ID
  - CITEM_CONTROL_TYPE long? 物料管控类型
  - CITEM_TYPE_BARCODE string 物料类型条码
  - CITEM_TYPE_NAME string 物料类型名称
  - CITEM_TYPE_NO string 物料类型编码
  - CITEM_TYPE_PATH string 类型层级路径
  - CPARENT_TYPE_ID long? 上级类型ID
  - CREMARK string 备注
  - CSEQ int 排序号
  - CSOURCE_ID string 来源系统ID
- 关联关系：
  - TBL_BD_ITEM_TYPE.CPARENT_TYPE_ID = TBL_BD_ITEM_TYPE.CID

----------------------
21. TBL_BD_PROCESS（工序工艺信息表）
- 业务含义：工序主数据表，定义生产工艺路线中的各工序。
- 字段列表：
  - CID long 主键ID
  - CIS_COUNT string 是否计数工序
  - CPARENT_PROCESS_ID long? 上级工序ID
  - CPROCESS_CONTROL_TYPE long? 工序管控类型
  - CPROCESS_DESC string 工序描述
  - CPROCESS_NAME string 工序名称
  - CPROCESS_NO string 工序编码
  - CPROCESS_PATH string 工序路径
  - CPROCESS_SEQ int? 工序顺序
  - CPROCESS_SHORT_CODE string 工序简称
  - CPROCESS_TYPE_ID long? 工序类型ID
  - CREMARK string 备注
  - CSOURCE_ID string 来源系统ID
- 关联关系：
  - TBL_BD_PROCESS.CPARENT_PROCESS_ID = TBL_BD_PROCESS.CID

----------------------
22. TBL_BD_PROCESS_OUTS（外协产品工序表）
- 业务含义：外协产品工序定义表，存储外协工序信息。
- 字段列表：
  - CID long 主键ID
  - CPROCESS_CONTROL_TYPE long? 工序管控类型
  - CPROCESS_DESC string 工序描述
  - CPROCESS_ID long? 标准工序ID
  - CPROCESS_NAME string 工序名称
  - CPROCESS_NO string 工序编码
  - CPROCESS_SHORT_CODE string 工序简称
  - CPRODUCT_ITEM_NO string 外协产品料号
- 关联关系：
  - TBL_BD_PROCESS_OUTS.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------
23. TBL_BD_REGEX（正则校验规则表）
- 业务含义：正则校验规则表，存储输入校验规则。
- 字段列表：
  - CID long 主键ID
  - CREGEX_DESC string 规则描述
  - CREGEX_NAME string 规则名称
  - CREGEX_NO string 规则编码

----------------------
24. TBL_BD_RULE（编码规则定义表）
- 业务含义：编码规则定义表，定义各类业务单据编号规则。
- 字段列表：
  - CID long 主键ID
  - CRULE_NAME string 规则名称
  - CRULE_NO string 规则编码

----------------------
25. TBL_BD_SUPPLIER（供应商信息表）
- 业务含义：供应商主数据表，存储供应商基本信息。
- 字段列表：
  - CID long 主键ID
  - CADDRESS string 地址
  - CEMAIL string 电子邮箱
  - CPHONE string 联系电话
  - CREMARK string 备注
  - CSOURCE_ID string 来源系统ID
  - CSUPPLIER_DESC string 供应商描述
  - CSUPPLIER_NAME string 供应商全称
  - CSUPPLIER_NO string 供应商编码
  - CSUPPLIER_SHORT string 供应商简称
  - CSUPPLIER_SHORT_NO string 供应商简称编码
  - CSUPPLIER_TYPE_ID Int64? 供应商类型ID
  - CUSER string 联系人

----------------------
26. TBL_BD_TEMPLATE（模板信息表）
- 业务含义：模板信息表，存储各类业务模板。
- 字段列表：
  - CID long 主键ID
  - CRULE_ID long? 条码规则ID
  - CTEMPLATE_GROUP_ID long 模板分组ID
  - CTEMPLATE_NAME string 模板名称
  - CTEMPLATE_NO string 模板编码
  - CTEMPLATE_PATH string 模板层级路径

----------------------
27. TBL_BD_TEMPLATE_GROUP（模板分组表）
- 业务含义：模板分组表，对模板进行分类。
- 字段列表：
  - CID long 主键ID
  - CTEMPLATE_GROUP_NAME string 模板分组名称
  - CTEMPLATE_GROUP_NO string 模板分组编码

----------------------
28. TBL_BD_WC（工作中心表）
- 业务含义：工作中心主数据表，定义生产线、机台等生产单元。
- 字段列表：
  - CID long 主键ID
  - CIS_LINK_CONFIG string 是否已配置管控信息
  - CIS_LINK_TYPE string 是否已配置关联物料类别
  - CPARENT long? 上级工作中心ID
  - CWC_NAME string 工作中心名称
  - CWC_NO string 工作中心编码
  - CWC_TYPE long? 工作中心类型
- 关联关系：
  - TBL_BD_WC.CPARENT = TBL_BD_WC.CID

----------------------
29. TBL_BD_WC_ITEMTYPE_LINK（工作中心关联模板）
- 业务含义：工作中心与物料类型关联表。
- 字段列表：
  - CID long 主键ID
  - CITEM_TYPE_ID long? 物料类型ID
  - CREMARK string 备注
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_BD_WC_ITEMTYPE_LINK.CWC_ID = TBL_BD_WC.CID
  - TBL_BD_WC_ITEMTYPE_LINK.CITEM_TYPE_ID = TBL_BD_ITEM_TYPE.CID

----------------------
30. TBL_BD_WC_PROCESS_LINK（工作中心与工序关系表）
- 业务含义：工作中心与工序关联表，定义工作中心可执行的工序。
- 字段列表：
  - CID long 主键ID
  - CPROCESS_ID long 工序ID
  - CSEQ int? 工序顺序
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_BD_WC_PROCESS_LINK.CWC_ID = TBL_BD_WC.CID
  - TBL_BD_WC_PROCESS_LINK.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------
31. TBL_MD_DATASET（数据集）
- 业务含义：数据集定义表，配置报表/模板的数据来源。
- 字段列表：
  - CID long 主键ID
  - CDATASET_CONDITION string 数据集参数Json字符串
  - CDATASET_TYPE DataSetTypeEnum 数据集类型
  - CDATASOURCE_ID long 数据源ID
  - CNAME string 数据集名称
  - desc string 参数描述
  - key string 参数名称
  - value string 参数值

---
三、消息推送

----------------------
32. TBL_MSG_EVENT（消息事件表）
- 业务含义：消息事件配置表，定义触发消息推送的条件和规则。
- 字段列表：
  - CID long 主键ID
  - CDATASET_ID long? 数据集ID
  - CDESC string 描述
  - CEXPRESSION string 表达式
  - CFREQUENCY long? 频率
  - CINDICAROR string 指标
  - CMSG_GROUP_ID long? 消息群组ID
  - CRULE string 规则
  - CSCHEDULE_TASK_ID int? 调度任务ID
  - CSEQ int? 序号
  - CSTATUS string 达成状态
  - CTARGET string 目标
  - CTEMPLATE_ID long? 消息模板ID
- 关联关系：
  - TBL_MSG_EVENT.CMSG_GROUP_ID = TBL_MSG_GROUP.CID
  - TBL_MSG_EVENT.CTEMPLATE_ID = TBL_MSG_TEMPLATE.CID

----------------------
33. TBL_MSG_GROUP（消息群组）
- 业务含义：消息群组表，定义接收消息的群组。
- 字段列表：
  - CID long 主键ID
  - CGROUP_CODE string 群组编码
  - CGROUP_DESC string 群组描述
  - CGROUP_NAME string 群组名称
  - CTHIRD_PARTY_PARAM string 第三方参数

----------------------
34. TBL_MSG_GROUP_USER（消息群组和用户）
- 业务含义：消息群组与用户关联表。
- 字段列表：
  - CID long 主键ID
  - CGROUP_ID long 群组ID
  - CUSER_ID long 用户ID
- 关联关系：
  - TBL_MSG_GROUP_USER.CGROUP_ID = TBL_MSG_GROUP.CID
  - TBL_MSG_GROUP_USER.CUSER_ID = TBL_SYS_USER.CID

----------------------
35. TBL_MSG_PUSH_FREQUENCY（预警频率配置表）
- 业务含义：消息推送频率配置表，使用Cron表达式定义推送周期。
- 字段列表：
  - CID long 主键ID
  - CDESC string 描述
  - CSCHEDULE string 频率
  - CSEQ int? 序号

----------------------
36. TBL_MSG_ROBOT（推送机器人）
- 业务含义：消息机器人配置表，存储第三方机器人Webhook信息。
- 字段列表：
  - CID long 主键ID
  - CROBOT_NAME string 机器人名称
  - CROBOT_TYPE string 机器人类型
  - CWEBHOOK_URL string 机器人Webhook地址

----------------------
37. TBL_MSG_ROBOT_EVENT_LINK（推送事件机器人关联）
- 业务含义：消息事件与机器人关联表。
- 字段列表：
  - CID long 主键ID
  - CMSG_EVENT_ID long? 推送事件ID
  - CROBOT_ID long? 机器人ID
- 关联关系：
  - TBL_MSG_ROBOT_EVENT_LINK.CMSG_EVENT_ID = TBL_MSG_EVENT.CID
  - TBL_MSG_ROBOT_EVENT_LINK.CROBOT_ID = TBL_MSG_ROBOT.CID

----------------------
38. TBL_MSG_SEND_LOG（消息发送日志表）
- 业务含义：消息发送日志表，记录所有消息推送历史。
- 字段列表：
  - CID long 主键ID
  - CACCEPT_DATETIME DateTime? 接收日期
  - CCLOSE_DATETIME DateTime? 关闭日期
  - CCONFIRM_DATETIME DateTime? 确认日期
  - CDELETE_DATETIME DateTime? 删除日期
  - CMSG_CONTENT string 消息内容
  - CREMARK string 备注
  - CSEND_DATETIME DateTime? 发送日期
  - CSEND_TYPE string 发送类型
  - CSTATUS int? 状态
  - CUSER_ID string 处理人

----------------------
39. TBL_MSG_TEMPLATE（消息模板）
- 业务含义：消息模板表，定义推送消息的内容格式。
- 字段列表：
  - CID long 主键ID
  - CCODE string 模板编码
  - CCONTENT string 正文
  - CPARAMS string 模板参数
  - CSUB_TITLE string 子标题
  - CTEMPLATE_TYPE string 消息类型
  - CTITLE string 标题

----------------------
40. TBL_MSG_USER（消息推送用户）
- 业务含义：消息推送用户表，存储第三方消息平台用户信息。
- 字段列表：
  - CID long 主键ID
  - CACCOUNT string 账号
  - CUSER_ID long? 用户表ID
  - CUSER_NAME string 姓名
  - CUSER_TYPE string 类型
- 关联关系：
  - TBL_MSG_USER.CUSER_ID = TBL_SYS_USER.CID

---
四、设备联机

----------------------
41. TBL_EAP_ALARM（设备报警记录）
- 业务含义：设备报警记录表，记录设备产生的报警信息。
- 字段列表：
  - CID long 主键ID
  - CALARM_LEVEL int? 报警等级
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int 设备ID
  - CEND_TIME DateTime? 报警结束时间
  - CERROR_ID int? 报警类型ID
  - CERROR_MESSAGE string 报警信息
  - CERROR_NO string 报警编码
  - CITEM_NO string 料号
  - CLOT_NO string 批次号
  - CORDER_NO string 工单号
  - CSTART_TIME DateTime? 报警开始时间
  - CUSER_CREATED string 创建人
- 关联关系：
  - TBL_EAP_ALARM.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
42. TBL_EAP_AOI_DETECTIONS（AOI或者VRS数据主表）
- 业务含义：AOI或VRS检测数据主表，记录自动光学检测结果。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 板码
  - CBRAND string 品牌
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int 设备ID
  - CITEM_NO string 料号
  - CLAYER string 层别
  - CLOT_NO string 批次号
  - CMAP_ITEM_NO string 映射料号
  - CORDER_NO string 工单号
  - CPRINT_CODE string 印码
  - CRESULT string 检测结果
  - CTEST_END_TIME DateTime? 测试结束时间
  - CTEST_START_TIME DateTime? 测试开始时间
  - CTEST_TIME string 检测时间
  - CTOTAL_QTY int? 总数量
  - CUSER_CREATED string 创建人
- 关联关系：
  - TBL_EAP_AOI_DETECTIONS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
43. TBL_EAP_AOI_DETECTIONS_DTL（AOI或VRS状态明细表）
- 业务含义：AOI检测明细表，记录每个缺陷的详细信息。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEFECT_NO string 缺陷编号
  - CDETECTION_ID long 主表ID
  - CIMG_PATH string 图片路径
  - CIS_FLAG int? 标记位
  - CNG_CONTENT string NG内容
  - CNG_NO string NG编号
  - COORDINATE_X string X坐标
  - COORDINATE_Y string Y坐标
  - CPOSITION string 位置
  - CSERVER_IMG_PATH string? 服务器上图片路径
- 关联关系：
  - TBL_EAP_AOI_DETECTIONS_DTL.CDETECTION_ID = TBL_EAP_AOI_DETECTIONS.CID

----------------------
44. TBL_EAP_API_RECORDS（联机API调用记录）
- 业务含义：设备联机API调用记录表，记录接口请求响应日志。
- 字段列表：
  - CID long 主键ID
  - CDATA_ID string 数据主键ID
  - CDATA_TYPE string 数据类型
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_NAME string 设备名称
  - CINTERFACE string 接口地址
  - CINTERFACE_NAME string 接口名称
  - CREMARK string 备注
  - CREQUEST string 请求报文
  - CRESPONSE string 响应报文
  - CSERVER_ID string 服务器标识

----------------------
45. TBL_EAP_AUTO_PULL_MACHINE（放板机状态监控表）
- 业务含义：放板机状态监控表，每两分钟更新一次设备状态。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_MODIFIED DateTime 修改时间
  - CIS_BOARD string 是否有板
  - CIS_MES_MODEL string 是否MES模式
  - CIS_ONLINE string 是否在线
  - CIS_RUN string 是否运行
  - CPULL_MACHINE_NAME string 放板机名称
  - CPULL_MACHINE_NO string 放板机编号

----------------------
46. TBL_EAP_BT_PARAM（班通参数主表）
- 业务含义：班通设备参数主表，存储工艺参数。
- 字段列表：
  - CID long 主键ID
  - CITEM_NO string 料号
  - CLAYER_NAME string 层别名称
  - CPART_NUM string 制造部件
  - CPROCESS string 工序

----------------------
47. TBL_EAP_BT_PARAM_DTL（班通参数明细表）
- 业务含义：班通设备参数明细表，存储具体参数项。
- 字段列表：
  - CID long 主键ID
  - CDATA_TYPE string 数据类型
  - CMAIN_ID long 主表ID
  - CMAX_VALUE decimal? 最大值
  - CMEASURE_ITEM_NAME string 测量项目名称
  - CMEASURE_TYPE string 测量类型
  - CMIN_VALUE decimal? 最小值
  - CSTAND_VALUE decimal? 标准值
- 关联关系：
  - TBL_EAP_BT_PARAM_DTL.CMAIN_ID = TBL_EAP_BT_PARAM.CID

----------------------
48. TBL_EAP_CURRENT_DATA（联机测点TAG实时状态表）
- 业务含义：设备测点实时数据表，存储最新的采集值。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int 设备ID
  - CDEVICE_NAME string 设备名称
  - CDEVICE_SERIAL int 设备序号
  - CDT DateTime? 数据时间
  - CSERVER_SERIAL int 服务器序号
  - CTAG_ID int 测点ID
  - CTAG_NAME string 测点名称
  - CTYPE string 数据类型
  - CVALUE float? 数值
  - CVALUE_STRING string 字符串值
  - CVALUE_TYPE int 值类型
- 关联关系：
  - TBL_EAP_CURRENT_DATA.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_CURRENT_DATA.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------
49. TBL_EAP_DATA（EAP采集数据表）
- 业务含义：设备采集历史数据表，存储测点历史值。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CDT DateTime 数据时间
  - CSERVER_ID int 服务器ID
  - CTAG_ID int 测点ID
  - CTYPE string 数据类型
  - CVALUE float? 数值
  - CVALUE_STRING string 字符串值
  - CVALUE_TYPE int 值类型
- 关联关系：
  - TBL_EAP_DATA.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_DATA.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------
50. TBL_EAP_DATA_CONTENT（EAP数据内容记录表）
- 业务含义：EAP原始数据内容记录表，存储完整的报文数据。
- 字段列表：
  - CID long 主键ID
  - CCUR_DATE DateTime 当前时间
  - CDATA string 数据内容
  - CDATA_ID string 数据ID
  - CDATA_TYPE string 数据类型
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE string 设备标识
  - CREMARK string 备注
  - CSERVER string 服务器标识

----------------------
51. TBL_EAP_DATA_YYYYMM（联机数据测点采集信息表(分表)）
- 业务含义：设备采集数据按月分表，存储历史数据。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDEVICE_ID int? 设备ID
  - CDT DateTime? 数据时间
  - CSERVER_ID int? 服务器ID
  - CTAG_ID int? 测点ID
  - CTYPE string 数据类型
  - CVALUE float? 数值
  - CVALUE_STRING string 字符串值
  - CVALUE_TYPE byte? 值类型

----------------------
52. TBL_EAP_DEVICE（联机设备列表）
- 业务含义：设备主数据表，存储所有联机设备信息。
- 字段列表：
  - CID long 主键ID
  - CADDRESS string 设备地址
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime 修改时间
  - CDEVICE_ID int 设备编号
  - CDEVICE_NAME string 设备名称
  - CDEVICE_SERIAL int 设备序号
  - CIP string 设备IP
  - CLOT string 当前批次号
  - COEE decimal? OEE指标
  - CPORT int? 设备端口
  - CPRODUCT string 当前产品信息
  - CREMARK string 备注
  - CSERVER_SERIAL int 服务器序号
  - CSTATUS int 设备状态码
  - CSTATUS_TIME DateTime 状态更新时间

----------------------
53. TBL_EAP_GE_PARAM（今明图电参数）
- 业务含义：今明图电设备参数表，存储电镀工艺参数。
- 字段列表：
  - CID long 主键ID
  - CAREA_C decimal C面积
  - CAREA_S decimal S面积
  - CCU_DEN decimal 铜密度
  - CCU_TIME int 铜时间
  - CFB string A/B挂
  - CITEM_NO string 料号
  - CPARAM_STATUS string 参数状态
  - CPART_NUM string 制造部件
  - CREMARK string 备注
  - CSN_DEN decimal 锡密度
  - CSN_TIME int 锡时间
  - CSTATUS int 状态
  - CUSE_COUNT int? 使用次数

----------------------
54. TBL_EAP_GE_PARAM_CHANGE_LOG（图电参数变更记录表）
- 业务含义：图电参数变更日志表，记录参数修改历史。
- 字段列表：
  - CID long 主键ID
  - CAAREA_C decimal 变更后C面积
  - CAAREA_S decimal 变更后S面积
  - CACU_DEN decimal 变更后铜密度
  - CACU_TIME int 变更后铜时间
  - CASN_DEN decimal 变更后锡密度
  - CASN_TIME int 变更后锡时间
  - CBAREA_C decimal? 变更前C面积
  - CBAREA_S decimal? 变更前S面积
  - CBCU_DEN decimal? 变更前铜密度
  - CBCU_TIME int? 变更前铜时间
  - CBSN_DEN decimal? 变更前锡密度
  - CBSN_TIME int? 变更前锡时间
  - CPARAMS_ID long 参数主表ID
- 关联关系：
  - TBL_EAP_GE_PARAM_CHANGE_LOG.CPARAMS_ID = TBL_EAP_GE_PARAM.CID

----------------------
55. TBL_EAP_GE_PARAM_USE_LOG（图电参数下发记录）
- 业务含义：图电参数下发记录表，记录参数下发到机台的历史。
- 字段列表：
  - CID long 主键ID
  - CMACHINE_NAME string 机台名称
  - CPARAMS_ID long 参数主表ID
  - CWO string 工单号
- 关联关系：
  - TBL_EAP_GE_PARAM_USE_LOG.CPARAMS_ID = TBL_EAP_GE_PARAM.CID

----------------------
56. TBL_EAP_GOLD_NICKEL_TESTER_RECORD（金镍测试仪上传数据主表，沉金）
- 业务含义：沉金工序金镍测试仪数据主表。
- 字段列表：
  - CID long 主键ID
  - CAU_AVG decimal? 金含量平均值
  - CAU_CV decimal 金含量变异系数
  - CAU_DEVIATION decimal? 金含量偏差
  - CAU_MAX_VALUE decimal? 金含量最大值
  - CAU_MIN_VALUE decimal? 金含量最小值
  - CAU_RANGE decimal? 金含量范围
  - CFILE_NAME string 文件名
  - CIMG_1 string? 图片1
  - CIMG_2 string? 图片2
  - CITEM string 项目
  - CMACHINE_TIME DateTime? 机器时间
  - CNI_AVG decimal? 镍含量平均值
  - CNI_CV decimal? 镍含量变异系数
  - CNI_DEVIATION decimal? 镍含量偏差
  - CNI_MAX_VALUE decimal? 镍含量最大值
  - CNI_MIN_VALUE decimal? 镍含量最小值
  - CNI_RANGE decimal? 镍含量范围
  - COPERATOR string 操作员
  - CPROCESS_NAME string 过程名称
  - CPROGRAM_NAME string 程序名称
  - CSAMPLE_NAME string 样品名称
  - CSAMPLE_NO string 样品编号

----------------------
57. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL（金镍测试仪上传数据明细表，沉金）
- 业务含义：沉金工序金镍测试仪数据明细表。
- 字段列表：
  - CID long 主键ID
  - CAU_VALUE decimal? 金测量值
  - CNI_VALUE decimal? 镍测量值
  - CRECORD_ID long 主表ID
  - CSEQ int? 序号
- 关联关系：
  - TBL_EAP_GOLD_NICKEL_TESTER_RECORD_DETAIL.CRECORD_ID = TBL_EAP_GOLD_NICKEL_TESTER_RECORD.CID

----------------------
58. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN（金镍测试仪主表，沉锡）
- 业务含义：沉锡工序金镍测试仪数据主表。
- 字段列表：
  - CID long 主键ID
  - CFILE_NAME string 文件名
  - CIMG_1 string? 图片1
  - CIMG_2 string? 图片2
  - CITEM string 项目
  - CMACHINE_TIME DateTime? 机器时间
  - COPERATOR string 操作员
  - CPROCESS_NAME string 过程名称
  - CPROGRAM_NAME string 程序名称
  - CSAMPLE_NAME string 样品名称
  - CSAMPLE_NO string 样品编号
  - CSN_AVG decimal? 锡含量平均值
  - CSN_CV decimal 锡含量变异系数
  - CSN_DEVIATION decimal? 锡含量偏差
  - CSN_MAX_VALUE decimal? 锡含量最大值
  - CSN_MIN_VALUE decimal? 锡含量最小值
  - CSN_RANGE decimal? 锡含量范围

----------------------
59. TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL（金镍测试仪明细表，沉锡）
- 业务含义：沉锡工序金镍测试仪数据明细表。
- 字段列表：
  - CID long 主键ID
  - CRECORD_ID long 主表ID
  - CSEQ int? 序号
  - CSN_VALUE decimal? 锡测量值
- 关联关系：
  - TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN_DETAIL.CRECORD_ID = TBL_EAP_GOLD_NICKEL_TESTER_RECORD_SN.CID

----------------------
60. TBL_EAP_HAOS_PARAM（浩硕打靶机参数）
- 业务含义：浩硕打靶机参数表，存储钻靶参数。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDistA1A2 decimal? A1A2靶距
  - CDistA1B1 decimal? A1B1靶距
  - CDistA1C1_X decimal? A1C1 X距离
  - CDistA1C1_Y decimal? A1C1 Y距离
  - CDistC1C2 decimal? C1C2靶距
  - CDistC1D1 decimal? C1D1靶距
  - CDrillstyle string 钻靶型式
  - CENTERPRISE_CODE long? 企业编码
  - CFrontToA1A2 decimal? A1A2至板前缘
  - CINSTANCE_ID string 实例ID
  - CJobname string 料号
  - CLength decimal? 板长
  - CLot_NO string 批次号
  - CORG_CODE long? 组织编码
  - Count int? 数量
  - CRecipetime string 配方生成时间戳
  - CROWREMARK string 行备注
  - CSTATE string 状态
  - CThickness decimal? 板厚
  - CUSER_CREATED string 创建人
  - CUSER_MODIFIED string 修改人
  - CWidth decimal? 板宽

----------------------
61. TBL_EAP_HEARTBEAT（放板机心跳记录）
- 业务含义：放板机心跳记录表，监控设备在线状态。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_NAME string 设备名称
  - CLOGIN_USER string 登录用户
  - CREMARK string 备注

----------------------
62. TBL_EAP_HEARTBEATS（心跳记录表，疑似弃用）
- 业务含义：设备心跳记录表（疑似弃用）。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CHEARTBEAT_NUM long 心跳序号
- 关联关系：
  - TBL_EAP_HEARTBEATS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
63. TBL_EAP_HONGSHENG_RECORDS（宏胜裁磨机结批数据）
- 业务含义：宏胜裁磨机结批数据记录表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int 设备ID
  - CITEM_NO string 料号
  - CLOT_IN_QTY int? 投入数量
  - CLOT_NO string 批次号
  - CLOT_OUT_QTY int? 产出数量
  - CLOT_QTY int? 批次数量
- 关联关系：
  - TBL_EAP_HONGSHENG_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
64. TBL_EAP_HONGSHENG_TM_RECORDS（宏胜测厚机测试数据）
- 业务含义：宏胜测厚机铜厚/板厚测试数据表。
- 字段列表：
  - CID long 主键ID
  - Average string 平均值
  - CCOUNT string 计数值
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - Container string 容器号
  - CopperLowerLimit string 铜厚下限
  - CopperThickness string 铜厚测量值
  - CopperUpperLimit string 铜厚上限
  - CPERCENT string 百分比
  - CTIME string 测量时间
  - DeviceCode string 设备编码
  - DeviceName string 设备名称
  - DeviceStatus string 设备状态
  - DivFact string 分度系数
  - DownCuResult string 下铜判定结果
  - JudgmentResults string 判定结果
  - LeftPointA string 左侧A点测量值
  - LeftPointB string 左侧B点测量值
  - LeftPointC string 左侧C点测量值
  - LeftPointD string 左侧D点测量值
  - LowerCopper string 下铜厚测量值
  - LowerCopperlowerlimit string 下铜厚下限
  - LowerCopperupperlimit string 下铜厚上限
  - LowerLimit string 板厚下限
  - MACHINE_IP string 设备IP
  - MeanValue string 均值
  - MethodName string 上报方法名
  - MiddlePointA string 中间A点测量值
  - MiddlePointB string 中间B点测量值
  - MiddlePointC string 中间C点测量值
  - MiddlePointD string 中间D点测量值
  - PartNo string 料号
  - RightPointA string 右侧A点测量值
  - RightPointB string 右侧B点测量值
  - RightPointC string 右侧C点测量值
  - RightPointD string 右侧D点测量值
  - Thickness string 板厚测量值
  - UpCuResult string 上铜判定结果
  - UpperLimit string 板厚上限
- 关联关系：
  - TBL_EAP_HONGSHENG_TM_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
65. TBL_EAP_HQ_PRESS_PRODUCTION（活全压机数据）
- 业务含义：活全压机生产数据表，每两分钟从MySQL采集。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_NO string? 设备编号
  - Job_No string 作业号
  - Lot_No string 批次号
  - Mat_Pcs string 板数
  - Mat_Press_PV string 材料压力实测值
  - Mat_Press_SV string 材料压力设定值
  - Mat_Size_L string 物料长度
  - Mat_Size_W string 物料宽度
  - Now_Vacuum string 当前真空度
  - Part_No string 料号
  - PRESS_TPDIS_LYR01~20 string 层厚度偏差01~20
  - PRESS_TPDIS_MAT01~12 string 材料厚度偏差01~12
  - Recipe_Name string 配方名称
  - System_Press string 系统压力
  - TEMP_AVG string 平均温度
  - TEMP_SV string 温度设定值
  - Time_Stamp DateTime 时间戳
  - Time_Stamp_ms int? 时间戳毫秒

----------------------
66. TBL_EAP_HQ_PRESS_PRODUCTION_ONSUBMIT（活全压机生成记录，手动提交）
- 业务含义：活全压机手动提交的生产记录。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_NO string? 设备编号
  - Job_No string 作业号
  - Lot_No string 批次号
  - Mat_Pcs string 板数
  - Mat_Press_PV string 材料压力实测值
  - Mat_Press_SV string 材料压力设定值
  - Mat_Size_L string 物料长度
  - Mat_Size_W string 物料宽度
  - Now_Vacuum string 当前真空度
  - Part_No string 料号
  - PRESS_TPDIS_LYR01~20 string 层厚度偏差01~20
  - PRESS_TPDIS_MAT01~12 string 材料厚度偏差01~12
  - Recipe_Name string 配方名称
  - System_Press string 系统压力
  - TEMP_AVG string 平均温度
  - TEMP_SV string 温度设定值
  - Time_Stamp DateTime? 时间戳
  - Time_Stamp_ms int? 时间戳毫秒

----------------------
67. TBL_EAP_LDI_JOB（LDI作业参数记录表）
- 业务含义：LDI曝光机作业参数记录表。
- 字段列表：
  - CID long 主键ID
  - CCUR_DATE DateTime? 当前时间
  - CHEIGHT string 板长
  - CIS_COPPER string 是否含铜
  - CITEM_NO string 产品型号
  - CJOB_NAME string? 料号名称
  - CLAYER_NAME_A string 层次
  - CLAYER_NAME_B string 层次
  - CLOT_NO string? 流程卡号
  - CMACHINE_CODE string? 设备编号
  - CMAKE_PART string 制造部件
  - CORDER_NO string? 工单
  - CPLATE string 板材铜厚
  - CRESISNAME string 干膜
  - CSCALE_X string 涨缩系数
  - CSCALE_Y string 涨缩系数
  - CSERIAL_NO string? 产品型号
  - CTHICKNESS string 板厚
  - CUSER_NAME string? 用户名称
  - CWIDTH string 板宽

----------------------
68. TBL_EAP_LDI_LOG（LDI生产日志记录表）
- 业务含义：LDI曝光机生产日志记录表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDRY_FILM string 干膜参数
  - CEND_TIME string 结束时间
  - CEXPOSURE string 曝光参数
  - CFACE string 面别
  - CFLOOR string 层别
  - CITEM_NO string 料号
  - CJOB_NAME string 作业名称
  - CLAYER_NAME string 层名称
  - CLOT_NO string 批次号
  - CMACHINE_CODE string 设备代码
  - CORDER_NO string 工单号
  - CPE_THRESHOLD string PE阈值
  - CSCALE_MODE string 缩放模式
  - CSCALE_X string X方向缩放
  - CSCALE_Y string Y方向缩放
  - CSTART_TIME string 开始时间

----------------------
69. TBL_EAP_LDI_PARAM（LDI参数）
- 业务含义：LDI设备参数配置表。
- 字段列表：
  - CID long 主键ID
  - CAB string AB板
  - CBOARD_LENGTH decimal? 板长
  - CBOARD_THICKNESS decimal? 板厚
  - CBOARD_WIDTH decimal? 板宽
  - CBOT_ALIGNMENT_LAYER string BOT对位层
  - CBOT_LAYER string BOT层
  - CCONTAINS_COPPER string 是否含铜
  - CCOPPER_THICKNESS string 板材铜厚
  - CDRY_FILM_NAME string 干膜名称
  - CEXPANSION_X decimal? 涨缩系数X
  - CEXPANSION_Y decimal? 涨缩系数Y
  - CISSUED_MESSAGE string 下发失败消息
  - CISSUED_RESULT string 下发结果
  - CITEM_NO string 料号
  - CPART_NUM string 制造部件
  - CREMARK string 备注
  - CSTATUS int 状态
  - CTGZ_FILE_PATH string tgz文件地址
  - CTOP_ALIGNMENT_LAYER string TOP对位层
  - CTOP_LAYER string TOP层

----------------------
70. TBL_EAP_LWT_DETECTIONS（班通检测主记录表）
- 业务含义：班通检测设备检测结果主表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - CDEVICE_NAME string 设备名称
  - CID_NO string 标识编号
  - CITEM string 检测项目
  - CLAYER string 层别
  - CLOT_NO string 工单号
  - CMAX_VALUE decimal? 最大值
  - CMIN_VALUE decimal? 最小值
  - CSTAND_VALUE decimal? 标准值
- 关联关系：
  - TBL_EAP_LWT_DETECTIONS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
71. TBL_EAP_LWT_DETECTIONS_DTL（班通检测明细记录表）
- 业务含义：班通检测设备检测结果明细表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CIMAGE_DATA string 图片数据
  - CIMAGE_NAME string 图片名称
  - CIMAGE_PATH string 图片路径
  - CIMAGE_SIZE int? 图片大小
  - CIMAGE_TYPE string 图片类型
  - CITEM string 检测项目
  - CITEM_CODE string 项目编码
  - CMAIN_ID long 主表ID
  - CMAX_VALUE decimal? 最大值
  - CMIN_VALUE decimal? 最小值
  - CNUMBER string 序号
  - CREAL_VALUE decimal? 实测值
  - CREMARK string 备注
  - CRESULT string 检测结果
  - CSTAND_VALUE decimal? 标准值
- 关联关系：
  - TBL_EAP_LWT_DETECTIONS_DTL.CMAIN_ID = TBL_EAP_LWT_DETECTIONS.CID

----------------------
72. TBL_EAP_M_PARTOP（图电料号工艺参数表）
- 业务含义：图电工序料号工艺参数表。
- 字段列表：
  - CID long 主键ID
  - CC_MJ string 电铜面积
  - CCU_DENSITY string 电铜密度
  - CCU_T string 电铜时间
  - CNEWDATE string 更新时间字符串
  - CPART_NAME string 料号名称
  - CPART_OP string 制程工序
  - CS_MJ string 电锡面积
  - CSN_DENSITY string 电锡密度
  - CSN_T string 电锡时间

----------------------
73. TBL_EAP_MASON_DETECTIONS（麦逊检测结果主表）
- 业务含义：麦逊检测设备检测结果主表。
- 字段列表：
  - CID long 主键ID
  - CCOUNT int 上传记录数
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CMACHINE_NO string 设备编码
  - CUSER_NO string? 用户编号

----------------------
74. TBL_EAP_MASON_DETECTIONS_DTL（麦逊检测结果明细表）
- 业务含义：麦逊检测设备检测结果明细表。
- 字段列表：
  - CID long 主键ID
  - CBATCH_NO string 批次号
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDETECT_DATE DateTime 检测时间
  - CDETECT_RESULT string 检测结果
  - CDETECT_STEP string 检测步骤
  - CIR decimal IR值
  - CITEM_NO string 料号
  - CLOT_NO string 工单号
  - CMAIN_ID long 主表ID
  - CNG_MESSAGE string NG信息
  - CNG_SEQ string NG序号
  - CPCB_NO string PCB编号
  - CQR_CODE string 二维码
  - CRDSON decimal RDSON值
  - CREMARK string 备注
  - CTOTAL_POINT int 总测点数
  - CWEB_STRUCT string 网结构
- 关联关系：
  - TBL_EAP_MASON_DETECTIONS_DTL.CMAIN_ID = TBL_EAP_MASON_DETECTIONS.CID

----------------------
75. TBL_EAP_MP_GROUP（测点组）
- 业务含义：设备测点分组表，将相关测点组合管理。
- 字段列表：
  - CID long 主键ID
  - CFREQUENCY int? 采集频率
  - CGROUP_NAME string 组名称
  - CMP_QTY int 测点数量

----------------------
76. TBL_EAP_MP_GROUP_DTL（测点组明细表）
- 业务含义：测点组明细表，记录组内测点。
- 字段列表：
  - CID long 主键ID
  - CGROUP_ID long? 组ID
  - CSERVER string 服务器
  - CTAG_ID int 测点ID
  - CTAG_NAME string 测点名称
- 关联关系：
  - TBL_EAP_MP_GROUP_DTL.CGROUP_ID = TBL_EAP_MP_GROUP.CID
  - TBL_EAP_MP_GROUP_DTL.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------
77. TBL_EAP_PATTERN_PLAT（图形电镀检测主记录表）
- 业务含义：图形电镀检测结果主表。
- 字段列表：
  - CID long 主键ID
  - CCOPPER_HOLE double 铜孔
  - CCUSTOMER_NO string 客户代码
  - CDAY DateTime? 日期
  - CFILE_NAME string 文件名称
  - CITEM_NO string 生产编号
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CRESULT string? 判定结果
  - CRESULT_MIN double 结果最小值
  - CSHIFFT string? 班次

----------------------
78. TBL_EAP_PATTERN_PLAT_ITEM（图形电镀检测明细表）
- 业务含义：图形电镀检测结果明细表。
- 字段列表：
  - CID long 主键ID
  - CPATTERN_PLAT_ID long 主表ID
  - CRESULT_DATA_1 double? 检测值1
  - CRESULT_DATA_2 double? 检测值2
  - CRESULT_DATA_3 double? 检测值3
  - CRESULT_DATA_4 double? 检测值4
  - CRESULT_DATA_5 double? 检测值5
- 关联关系：
  - TBL_EAP_PATTERN_PLAT_ITEM.CPATTERN_PLAT_ID = TBL_EAP_PATTERN_PLAT.CID

----------------------
79. TBL_EAP_PERIOD（设备状态时段记录表）
- 业务含义：设备状态时段记录表，记录设备状态持续时间。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int 设备ID
  - CEND_TIME DateTime? 时段结束时间
  - CIS_END char 是否已结束
  - CSTART_TIME DateTime 时段开始时间
  - CSTATUS int 状态码
- 关联关系：
  - TBL_EAP_PERIOD.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
80. TBL_EAP_PMS_CONTENT（汉印喷印机内容配置表）
- 业务含义：汉印喷印机喷印内容配置表。
- 字段列表：
  - CID long 主键ID
  - CCONTENT string 内容
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - CITEM_NO string 料号
  - CLABEL_H decimal? 标签高度
  - CLABEL_W decimal? 标签宽度
  - CLAYER string 层别
  - CPOSITION_CONTER_X decimal? 中心点X坐标
  - CPOSITION_CONTER_Y decimal? 中心点Y坐标
  - CPOSITION_X decimal? X坐标
  - CPOSITION_Y decimal? Y坐标
  - CREF_ID string? 关联编号
  - CREMARK string 备注
- 关联关系：
  - TBL_EAP_PMS_CONTENT.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
81. TBL_EAP_PMS_PROD（汉印生产记录主表）
- 业务含义：汉印喷印机生产记录主表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - CFACE string 面别
  - CPNL_CODE string PNL条码
  - CRESULT string 结果
  - CWON string 工单号
- 关联关系：
  - TBL_EAP_PMS_PROD.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
82. TBL_EAP_PMS_PROD_DTL（汉印生产记录明细表）
- 业务含义：汉印喷印机生产记录明细表。
- 字段列表：
  - CID long 主键ID
  - CCONTENT string 内容
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CPROD_ID long? 主表ID
  - CREF_ID int 关联编号
- 关联关系：
  - TBL_EAP_PMS_PROD_DTL.CPROD_ID = TBL_EAP_PMS_PROD.CID

----------------------
83. TBL_EAP_SHOOT_ITEM（打靶结果明细表）
- 业务含义：打靶机测量结果明细表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME DateTime 生产时间
  - CDAY string 日期
  - CFILE_NAME string 文件名称
  - CFILE_PATH string 文件路径
  - CITEM_NO string 产品料号
  - CREMARK string 备注
  - CRESULT_X string X坐标结果
  - CRESULT_Y string Y坐标结果
  - CSEQ int 序号
  - CTIME string 时间
  - CWC_CODE string 机型
  - CXCOORDINAT double X坐标
  - CYCOORDINAT double Y坐标

----------------------
84. TBL_EAP_SHUTDOWN_RECORD（放板机关机记录表）
- 业务含义：放板机关机记录表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_NAME string 设备名称
  - CLOGIN_USER string 登录用户
  - CMSG string 消息内容
  - CMSG_TYPE string 消息类型
  - CREMARK string 备注

----------------------
85. TBL_EAP_STATUS（设备状态采集记录表）
- 业务含义：设备状态实时采集记录表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID int 设备ID
  - CDURATION decimal 持续时长
  - CEXTRA string 扩展信息
  - CFILE_NAME string 来源文件名
  - CITEM_NO string 料号
  - CLOT string 批次号
  - CMACHINE_NAME string 设备名称
  - CMACHINE_TIME DateTime 设备时间
  - CMACHINE_USER string 操作用户
  - CMANUAL_STATUS int 手动状态码
  - COEE decimal OEE值
  - CPROGRESS decimal 进度
  - CQTY decimal 数量
  - CREMARK string 备注
  - CSTATUS int 状态码
  - CSTATUS_START_TIME DateTime 状态开始时间
  - CTEXT string 文本内容
  - CUNIT_STATUS string 机台状态文本
  - CVERSION string 版本
- 关联关系：
  - TBL_EAP_STATUS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
86. TBL_EAP_T_ALARM（报警记录表）
- 业务含义：设备报警记录表（简版）。
- 字段列表：
  - C_ID int 报警ID
  - CALARM string 报警内容
  - CCLEAR_DATE DateTime 清除时间
  - COCCUR_DATE DateTime 发生时间

----------------------
87. TBL_EAP_T_OPERATION（操作记录表）
- 业务含义：设备操作记录表。
- 字段列表：
  - CID long 主键ID
  - COPERATION_AUTHOR string 操作人
  - COPERATION_CONTENT string 操作内容
  - COPERATION_DATE DateTime 操作时间
  - COPERATION_TYPE string 操作类型

----------------------
88. TBL_EAP_T_OPERATION2（操作记录表（扩展））
- 业务含义：设备操作记录扩展表。
- 字段列表：
  - CID long 主键ID
  - COPERATION_AUTHOR string 操作人
  - COPERATION_CONTENT string 操作内容
  - COPERATION_DATE DateTime 操作时间
  - COPERATION_TYPE string 操作类型

----------------------
89. TBL_EAP_T_OUT_HISTORY（图电出板历史记录表）
- 业务含义：图电工序出板历史记录表。
- 字段列表：
  - CID long 主键ID
  - C10T string 10#时间
  - C11T string 11#时间
  - C12T string 12#时间
  - C1T string 1#时间
  - C2T string 2#时间
  - C3T string 3#时间
  - C4T string 4#时间
  - C5T string 5#时间
  - C6T string 6#时间
  - C7T string 7#时间
  - C8T string 8#时间
  - C9T string 9#时间
  - CCUCAH_A string 电铜C-AH
  - CCUNO string 电铜槽号
  - CCUPT_A string 电铜时间
  - CCUSAH_A string 电铜S-AH
  - CCUST_A string 电铜设时
  - CFB_NO string 飞靶编号
  - CINLOAD_TIME string 上板时间
  - CPART_AB string A/B靶
  - CPART_NAMEA string 电锡料号
  - CPART_SUMA string 电锡数量
  - CSNCAH_A string 电锡C-AH
  - CSNNO string 电锡槽号
  - CSNPT_A string 电锡时间
  - CSNSAH_A string 电锡S-AH
  - CSNST_A string 电锡设时
  - CUNLOAD_TIME string 下板时间

----------------------
90. TBL_EAP_TAG（测点配置表）
- 业务含义：设备测点配置表，定义采集点信息。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime 修改时间
  - CDEVICE_ID int? 设备ID
  - CDEVICE_NAME string 设备描述
  - CDEVICE_SERIAL short? 设备序号
  - CENTERPRISE_CODE string 企业编码
  - CGROUP_NAME string 类别名称
  - CGROUP_SERIAL short 类别序号
  - CINSTANCE_ID string 实例ID
  - CMAX_VALUE decimal? 最大值
  - CMIN_VALUE decimal? 最小值
  - CORG_CODE string 组织编码
  - CRADIX int 进制
  - CROWREMARK string 行备注
  - CSEQ int 排序号
  - CSERVER_ID string 服务器ID
  - CSERVER_NAME string 服务器名称
  - CSERVER_SERIAL int 服务器序号
  - CSHOW_TYPE string 显示类型
  - CSTATE char 数据状态
  - CTAG_ALIAS string 参数别名
  - CTAG_DESC string 参数描述
  - CTAG_ID int 测点ID
  - CTAG_NAME string 参数集名称
  - CTAG_PATH string 参数路径
  - CTAG_SERIAL short 测点序号
  - CUNIT string 单位
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
- 关联关系：
  - TBL_EAP_TAG.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
91. TBL_EAP_THREE_D_DATA（三次元数据）
- 业务含义：三次元测量数据表。
- 字段列表：
  - CID long 主键ID
  - CA decimal? A参数
  - CAVERAGE_VALUE double? 平均值
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime 修改时间
  - CDAY DateTime? 日期
  - CDEVIATION decimal? 标准差
  - CITEM string 项目名称
  - CLOW_TOLERANCE double 下公差
  - CMAX_VALUE decimal? 最大值
  - CMEASURE_VALUE double 测量值
  - CMIN_VALUE decimal? 最小值
  - CMISCOUNT double 误差
  - CP decimal? 过程能力指数P
  - CPK decimal? 过程能力指数CPK
  - CRECORD_ID long 记录ID
  - CRESULT string 判定
  - CSAMPLE_COUNT int? 样本大小
  - CSHIFFT string? 班次
  - CSTANDARD double 标准值
  - CTYPE string 型式
  - CUNIT string 单位
  - CUP_TOLERANCE double 上公差
  - CUSER_CREATED string 创建人
  - CUSER_MODIFIED string 修改人
- 关联关系：
  - TBL_EAP_THREE_D_DATA.CRECORD_ID = TBL_EAP_THREE_D_RECORD.CID

----------------------
92. TBL_EAP_THREE_D_ITEM（三次元数据明细）
- 业务含义：三次元测量数据明细表。
- 字段列表：
  - CID long 主键ID
  - CDAY DateTime? 日期
  - CDEVICE_ID long 项目分组ID
  - CDEVICE_NAME string 项目名称
  - CDEVICE_SEQ int 项目序号
  - CFILE_NAME string 文件路径
  - CFLAG int? 标记位
  - CLOW_TOLERANCE double 下公差
  - CMEASURE_VALUE double 测量值
  - CMISCOUNT double 误差
  - CRESULT string 判定
  - CSHIFFT string? 班次
  - CSTANDARD double 标准值
  - CUP_TOLERANCE double 上公差

----------------------
93. TBL_EAP_THREE_D_RECORD（三次元文件记录主表）
- 业务含义：三次元测量文件记录主表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDATETIME_MODIFIED DateTime 修改时间
  - CDAY DateTime? 日期
  - CFILE_NAME string 文件路径
  - CPROCESS_ID long? 工序ID
  - CSHIFFT string? 班次
  - CUSER_CREATED string 创建人
  - CUSER_MODIFIED string 修改人

----------------------
94. TBL_EAP_TIME_RANGE_CONTROL（放板机时间范围管控）
- 业务含义：放板机时间范围管控配置表。
- 字段列表：
  - CID long 主键ID
  - CEND_TIME TimeSpan? 结束时间
  - CFREQUENCY string 生效频率
  - CPARENT_DEVICE string 父设备标识
  - CSTART_TIME TimeSpan? 开始时间

----------------------
95. TBL_EAP_WHC（文坦验孔机主记录表）
- 业务含义：文坦验孔机检测记录主表。
- 字段列表：
  - CID long 主键ID
  - CBATCH string 批次
  - CBATCH_TYPE string 批次类型
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CDEVICE_NAME string 设备名称
  - CEXTEND_DATA string 扩展数据
  - COPERATOR_NAME string 操作员
  - CREMARK string 备注
  - CREQUEST_ID string 请求ID
  - CSERVICE_NAME string 服务名称
  - CTIME_STAMP DateTime 时间戳
- 关联关系：
  - TBL_EAP_WHC.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
96. TBL_EAP_WHC_DTL（文坦验孔机明细记录表）
- 业务含义：文坦验孔机检测记录明细表。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CMACHINE_TIME DateTime 设备时间
  - CSERVER_ID int 服务器ID
  - CTYPE string 数据类型
  - CVALUE float? 数值
  - CVALUE_STRING string 字符串值
  - CVALUE_TYPE int? 值类型
  - CWHC_ID long 主表ID
- 关联关系：
  - TBL_EAP_WHC_DTL.CWHC_ID = TBL_EAP_WHC.CID
  - TBL_EAP_WHC_DTL.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
97. TBL_EAP_YUHUI_TEST_RECORDS（誉汇测试记录主表）
- 业务含义：誉汇测试设备检测记录主表。
- 字段列表：
  - CID long 主键ID
  - CBOARD_COUNT int 板数量
  - CBOARD_TYPE string 板类型
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - CDEVICE_NAME string 设备名称
  - CITEM_NO string 料号
  - CORDER_NO string 工单号
  - CTEST_TIME DateTime? 检测时间
- 关联关系：
  - TBL_EAP_YUHUI_TEST_RECORDS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
98. TBL_EAP_YUHUI_TEST_RECORDS_DTL（誉汇测试记录明细表）
- 业务含义：誉汇测试设备检测记录明细表。
- 字段列表：
  - CID long 主键ID
  - CAREA string 区域
  - CBOARD_SEQ string 板序号
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDOWN_BOUND decimal? 下限
  - CERR_VALUE decimal? 误差值
  - CINNER_SEQ int? 板内序号
  - CITEM string 量测项目
  - CITEM_TYPE string 项目类型
  - CMAIN_ID long 主表ID
  - CN_TOL decimal? 负公差
  - CP_TOL decimal? 正公差
  - CPOSITION_END string 结束位置
  - CPOSITION_START string 起始位置
  - CREAL_VALUE decimal? 实测值
  - CRESULT string 检测结果
  - CSTAND_VALUE decimal? 标准值
  - CUNIT string 单位
  - CUP_BOUND decimal? 上限
- 关联关系：
  - TBL_EAP_YUHUI_TEST_RECORDS_DTL.CMAIN_ID = TBL_EAP_YUHUI_TEST_RECORDS.CID

----------------------
99. TBL_EAP_YULIGHT_DETECTIONS_PCS（宇之光生产记录）
- 业务含义：宇之光检测设备PCS级生产记录。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CEND_TIME DateTime 结束时间
  - CFILENAME string 文件名
  - CFROM_TICKET string 来源票号
  - CIS_REPAIR int 是否返修
  - COPENCUT int 开路数量
  - CPCS_ID string PCS编号
  - CPNL_ID string PNL编号
  - CRESULT int 检测结果
  - CSHORTCUT int 短路数量
  - CSTART_TIME DateTime 开始时间
- 关联关系：
  - TBL_EAP_YULIGHT_DETECTIONS_PCS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
100. TBL_EAP_YULIGHT_DETECTIONS_PNL（宇之光PNL检测记录表）
- 业务含义：宇之光检测设备PNL级检测记录。
- 字段列表：
  - CID long 主键ID
  - CADJAENCY int 邻接短路数
  - CDATETIME_CREATED DateTime 创建时间
  - CDEVICE_ID int 设备ID
  - CEND_TIME DateTime 结束时间
  - CFILENAME string 文件名
  - CFROM_TICKET string 来源票号
  - CHEIGHT string 高度
  - CIS_ABORT int 是否中止
  - CIS_REPAIR int 是否返修
  - CPCS_COUNT int PCS总数
  - CPCS_NG int PCS不良数
  - CPCS_OK int PCS良品数
  - CPNL_ID string PNL编号
  - CRESULT string 检测结果
  - CSTART_TIME DateTime 开始时间
  - CTEST_POINTS int 测试点数
  - CTOTAL_NETS int 总网络数
  - CWIDTH string 宽度
- 关联关系：
  - TBL_EAP_YULIGHT_DETECTIONS_PNL.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
101. TBL_ABNORMAL_DATA_POOL（锁机锁卡异常数据表）
- 业务含义：锁机锁卡异常数据记录表。
- 字段列表：
  - CID long 主键ID
  - CABNORMAL_TYPE string 异常类型
  - CDEVICE_NAME string 设备名
  - CFOREIGN_KEY_ID long? 外键ID
  - CFOREIGN_TABLE string 外键对应的表
  - CIDENTIFY_FIELD string 校验识别字段
  - CREMARK string 备注
  - CTEMPLATE_ITEM_NAME string 模板项目名
  - CTEMPLATE_NAME string 模板名

----------------------
102. TBL_DEVICE_SPEED_PARAMS（设备速度参数配置表）
- 业务含义：设备速度参数配置表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID int 设备ID
  - CDEVICE_NAME string 设备名称
  - CSPEED decimal? 速度参数值
  - CTAG_ID int? 测点ID
  - CTAG_NAME string 测点名称
- 关联关系：
  - TBL_DEVICE_SPEED_PARAMS.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_DEVICE_SPEED_PARAMS.CTAG_ID = TBL_EAP_TAG.CTAG_ID

----------------------
103. TBL_HPL_SEND_LOG（水平线参数下发接口发送日志表）
- 业务含义：水平线参数下发接口调用日志。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_NAME string 设备名称
  - CPARAMS string 发送参数
  - CREMARK string 备注
  - CRESULT string 返回结果
  - CWONUMBER string 工单号

----------------------
104. TBL_JINMING_TASK_RESULT（今明设备任务回传结果表）
- 业务含义：今明设备任务执行结果回传表。
- 字段列表：
  - CID long 主键ID
  - CCODE string 结果代码
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDEVICE_ID int? 设备ID
  - CJOB_NAME string 任务名称
  - CLOT_ID string 批次ID
  - CMACH_CODE string 设备代码
  - CMESSAGE string 结果消息
  - CWO string 工单号
- 关联关系：
  - TBL_JINMING_TASK_RESULT.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
105. TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD（浩硕生产记录实体类）
- 业务含义：浩硕图形电镀生产记录主表。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 板边码
  - CDEFECTS string XY明细坐标
  - CITEM_NO string 料号
  - CLOT_NO string? 工单
  - CMACHINE_CODE string 设备代码
  - CPRODUCTION_END_TIME string 打靶完成时间
  - CPRODUCTION_START_TIME string 开始打靶时间
  - CUSER_CREATED string 人员

----------------------
106. TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL（浩硕图形电镀生产记录明细表）
- 业务含义：浩硕图形电镀生产记录明细表。
- 字段列表：
  - CID long 主键ID
  - CCORDINATE_X string X涨缩
  - CCORDINATE_Y string Y涨缩
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDETECTION_ID long 主表CID
  - CMACHINE_CODE string 设备代码
  - CRESULT string 判定结果
  - CSTAN_X decimal? X标准值
  - CSTAN_Y decimal? Y标准值
  - DISTANCE_X string X坐标
  - DISTANCE_Y string Y坐标
- 关联关系：
  - TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL.CDETECTION_ID = TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD.CID

----------------------
107. TBL_PATTERN_PLATING_PRODUCTION_RECORD（图电生产记录实体类）
- 业务含义：图电工序生产记录实体表。
- 字段列表：
  - CID long 主键ID
  - A_B_TARGET string A/B靶
  - ACID_1_TIME string 酸1时间
  - ACID_2_TIME string 酸2时间
  - BOARD_COUNT int? 板数
  - COPPER_ELECTROLYSIS_C_AH string 电铜C-AH
  - COPPER_ELECTROLYSIS_S_AH string 电铜S-AH
  - COPPER_ELECTROLYSIS_SETTING_TIME string 电铜设时
  - COPPER_ELECTROLYSIS_TANK string 电铜槽
  - COPPER_ELECTROLYSIS_TIME string 电铜时间
  - CREATION_TIME DateTime 创建时间
  - DEGREASING_TIME string 除油时间
  - FLYING_TARGET_SERIAL_NUMBER string 飞靶流水号
  - LOADING_TIME string 上板时间
  - MACH_CODE string 设备代码
  - MATERIAL_NUMBER string 料号
  - MICROETCHING_TIME string 微蚀时间
  - TIN_ELECTROLYSIS_C_AH string 电锡C-AH
  - TIN_ELECTROLYSIS_S_AH string 电锡S-AH
  - TIN_ELECTROLYSIS_SETTING_TIME string 电锡设时
  - TIN_ELECTROLYSIS_TANK string 电锡槽
  - TIN_ELECTROLYSIS_TIME string 电锡时间
  - UNLOADING_TIME string 下板时间
  - WATER_WASH_TIME_14 string 14#水洗时间
  - WATER_WASH_TIME_15 string 15#水洗时间
  - WATER_WASH_TIME_17 string 17#水洗时间
  - WATER_WASH_TIME_18 string 18#水洗时间
  - WATER_WASH_TIME_19 string 19#水洗时间
  - WATER_WASH_TIME_20 string 20#水洗时间
  - WATER_WASH_TIME_8 string 8#水洗时间
  - WATER_WASH_TIME_9 string 9#水洗时间

---
五、品质管理

----------------------
108. TBL_QM_ASSAY_LOG（化验任务记录表）
- 业务含义：化验任务记录主表，记录药水化验任务信息。
- 字段列表：
  - CID long 主键ID
  - CASSAY_RESULT int 化验结果
  - CASSAY_STATUS int 化验状态
  - CASSAY_TIME DateTime? 化验时间
  - CASSAY_USER string 化验人
  - CBASE_TASK_NO string 基础任务编号
  - CCHECK_REMARK string 审核备注
  - CCHECK_STATUS int 审核状态
  - CCHECK_TIME DateTime? 审核时间
  - CCHECK_USER string 审核人
  - CIS_OPEN_LINE string 是否开线前分析
  - CMEDICINE_TANK_ID long 药缸ID
  - CRECEIVE_TIME DateTime? 接收时间
  - CRECEIVE_USER string 接收人
  - CREMARK string 备注
  - CSAMPLE_BARCODE string 样品条码
  - CSAMPLE_REMARK string 取样备注
  - CSAMPLE_TIME DateTime? 取样时间
  - CSAMPLE_USER string 取样人
  - CSHIFT string 班次
  - CTASK_NO string 任务编号
  - CTASK_STAND_TIME_E DateTime? 任务标准结束时间
  - CTASK_STAND_TIME_S DateTime? 任务标准开始时间
  - CTASK_STATUS int 任务状态
  - CTASK_TAG string 任务标签
  - CTASK_TYPE int 任务类型
  - CTEMPLATE_ID long 模板ID
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_QM_ASSAY_LOG.CMEDICINE_TANK_ID = TBL_QM_MEDICINE_TANK.CID
  - TBL_QM_ASSAY_LOG.CWC_ID = TBL_BD_WC.CID

----------------------
109. TBL_QM_ASSAY_LOG_ITEM（化验任务明细表）
- 业务含义：化验任务明细表，记录化验项目的具体值和判定。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal? 预警值上限
  - CALARM_MIN_VALUE decimal? 预警值下限
  - CASSAY_LOG_ID long 化验主表ID
  - CCHECK_CONTENT long? 校验内容ID
  - CCHECK_WAY int? 校验方式
  - CCORRECTIVE_ACTION string 纠正措施
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CEND_VALUE string 终值
  - CENTERPRISE_CODE long? 企业代码
  - CFORMULA string 补加量公式
  - CINPUT_FORMULA string 结果值计算公式
  - CINPUT_TYPE int? 录入框类型
  - CINPUT_VALUE string? 录入值
  - CINSTANCE_ID string 实例ID
  - CIS_CHECK_RESULT string 是否校验
  - CIS_CONFIRM int? 是否已确认添加
  - CIS_MUST string 是否必填
  - CITEM_FREQ_ID long? 任务频率ID
  - CLIST_SOURCE string 下拉框数据源
  - CLIST_SOURCE_TYPE int? 下拉框数据源类型
  - CORG_CODE long? 组织代码
  - CPROCESS_INFO string 原因分析
  - CREMARK string 备注
  - CREPLENISHMENT string 补加量
  - CRESULT int? 结果
  - CRETEST_RESULT int? 复测结果
  - CRETEST_TIME DateTime? 复测时间
  - CRETEST_USER string 复测人
  - CRETEST_VALUE string 复测值
  - CROWREMARK string 行备注
  - CSEQ int? 顺序号
  - CSTANDARD_MAX_ALLOW string 是否允许等于上限
  - CSTANDARD_MAX_VALUE decimal? 标准值上限
  - CSTANDARD_MIN_ALLOW string 是否允许等于下限
  - CSTANDARD_MIN_VALUE decimal? 标准值下限
  - CSTANDARD_VALUE string 标准值
  - CSTANDARD_VALUE_TYPE int? 标准值类型
  - CSTART_VALUE string 始值
  - CSTATE string 状态
  - CTEMPLATE_ITEM_CODE string 项目编码
  - CTEMPLATE_ITEM_DESC string 项目描述
  - CTEMPLATE_ITEM_NAME string 项目名称
  - CTEMPLATE_ITEM_TAG string 项目标签
  - CTITRATION_VALUE string 滴定值
  - CUNIT string 单位
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
- 关联关系：
  - TBL_QM_ASSAY_LOG_ITEM.CASSAY_LOG_ID = TBL_QM_ASSAY_LOG.CID

----------------------
110. TBL_QM_CC_EXCEPTION（客诉异常报告信息表）
- 业务含义：客户投诉异常报告主表，记录客诉及处理流程。
- 字段列表：
  - CID long 主键ID
  - CAUDIT_MAN string 审核人
  - CAUDIT_TIME DateTime? 审核时间
  - CBAD_QTY decimal? 不良数量
  - CBAD_RATIO string 不良比例
  - CBAD_TYPE string 不良类型
  - CCHECK_USER string 检查人
  - CCOMPLAINT_LEVEL string 客诉等级
  - CCUR_PROCESS int? 当前流程
  - CCUSTOMER_MODEL string 客户型号
  - CCUSTOMER_NO string 客户代码
  - CDATA_TYPE int 数据类型
  - CDUTY_PROCESS_ID long? 责任工序ID
  - CDUTY_PROCESS_USER string 责任工序责任人
  - CEFFECT_VERIFICATION string 效果验证
  - CEXCEP_CODE string 报告编号
  - CEXCEP_DESC string 异常描述
  - CEXCEP_PROCESS_ID long 异常发生工序ID
  - CFEEDBACK_DATE DateTime? 反馈日期
  - CIPQA_AUDIT_MAN string IPQA审核人
  - CIPQA_AUDIT_REMARK string IPQA审核备注
  - CIPQA_AUDIT_STATUS int? IPQA审核状态
  - CIPQA_AUDIT_TIME DateTime? IPQA审核时间
  - CIPQA_TIME DateTime? IPQA处理时间
  - CIS_SYNC_CUSTOMER string 是否同步客户
  - CITEM_ID long? 物料ID
  - CITEM_NO string 产品型号
  - CMATERIAL_PLACE string 生产场所
  - CNEED_DATE DateTime? 要求日期
  - COCCUR_DATE DateTime? 发生时间
  - COCCUR_PLACE string 发送地点
  - COUT_CAUSE_STATUS int 流出原因分析状态
  - COUT_IMPLEMENT_STATUS int 流出执行状态
  - COUT_MEASURE_STATUS int 流出措施状态
  - COUT_PROCESS_ID long 流出工序ID
  - COUT_PROCESS_USER string 流出工序责任人
  - CPREVENT_STATUS int 预防状态
  - CPRO_CAUSE_STATUS int 生产原因分析状态
  - CPRO_IMPLEMENT_STATUS int 生产执行状态
  - CPRO_MEASURE_STATUS int 生产措施状态
  - CPRODUCT_STAGE int? 产品阶段
  - CRECEIVE_USER string 接收人
  - CREMARK string 备注
  - CSHIPMENT_QTY decimal? 出货数量
  - CSTATUS int? 状态
- 关联关系：
  - TBL_QM_CC_EXCEPTION.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_CC_EXCEPTION.CEXCEP_PROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_CC_EXCEPTION.CDUTY_PROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_CC_EXCEPTION.COUT_PROCESS_ID = TBL_BD_PROCESS.CID

----------------------
111. TBL_QM_COMPLAINT（品质投诉记录表）
- 业务含义：品质投诉记录表，记录投诉信息及8D报告关联。
- 字段列表：
  - CID long 主键ID
  - C8D_NUMBER string 8D编号
  - CAFFECTED_AMOUNT string 受影响金额
  - CCOMPLAINT_DATE DateTime? 投诉日期
  - CCOMPLAINT_TYPE string 客诉类型
  - CCUSTOMER_CODE string 客户编码
  - CCUSTOMER_MODEL string 客户型号
  - CCYCLE string 周期
  - CDEFECT_QUANTITY int? 不良数量
  - CDEFECT_RATE string 不良比例
  - CFABRIC_MODEL string 本厂型号
  - CHANDLING_METHOD string 处理方式
  - CIS_MP bool 是否生成防错计划
  - COCCURRENCE_PROCESS string 发生工序
  - COUTFLOW_PROCESS string 流出工序
  - CPROBLEM_DESC string 问题描述
  - CRESPONSIBLE_PERSON string 责任人
  - CRESPONSIBLE_UNIT string 责任单位

----------------------
112. TBL_QM_COMPLAINT_IMAGE（品质投诉图片表）
- 业务含义：品质投诉图片表，存储投诉相关图片。
- 字段列表：
  - CID long 主键ID
  - CCOMPLAINT_ID long 投诉记录ID
  - CFILE_NAME string 文件名称
  - CFILE_PATH string Minio文件存储路径
- 关联关系：
  - TBL_QM_COMPLAINT_IMAGE.CCOMPLAINT_ID = TBL_QM_COMPLAINT.CID

----------------------
113. TBL_QM_INSPECT_RECORD（品质检验记录主表）
- 业务含义：品质检验记录主表，记录IPQC/FQC等检验任务。
- 字段列表：
  - CID long 主键ID
  - CCHECK_REMARK string 审核备注
  - CCHECK_TIME DateTime? 审核时间
  - CCHECK_USER_NAME string 审核人
  - CDECISION_MODE int 判定模式
  - CINSPECT_CODE string 检验单号
  - CINSPECT_QTY decimal? 检验数量
  - CINSPECT_TIME DateTime? 检验时间
  - CINSPECT_TYPE int 检验类型
  - CINSPECT_USER_NAME string 检验人
  - CIS_LAB string 是否送实验室
  - CITEM_ID long? 物料ID
  - CLAB_INSPECT_REMARK string 实验室检验备注
  - CLAB_INSPECT_TIME DateTime? 实验室检验时间
  - CLAB_INSPECT_USER_NAME string 实验室检验人
  - CLAB_RECEIVE_TIME DateTime? 实验室接收时间
  - CLAB_RECEIVE_USER_NAME string 实验室接收人
  - CMO_LOT string 工单批次
  - CNG_DISPOSAL string 不良处置
  - CPROCESS_ID long 工序ID
  - CREMARK string 备注
  - CRESULT int 检验结果
  - CSCAN_BARCODE string 扫描条码
  - CSHIFT string 班次
  - CSTATUS int 状态
  - CSUBMIT_QTY decimal? 报检数量
  - CTEMPLATE_ID long 模板ID
  - CUNIT string 单位
  - CUSTOMER_CODE string 客户编码
- 关联关系：
  - TBL_QM_INSPECT_RECORD.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_INSPECT_RECORD.CPROCESS_ID = TBL_BD_PROCESS.CID

----------------------
114. TBL_QM_INSPECTION_RECORD_ITEM（品质检验记录明细表）
- 业务含义：品质检验记录明细表，记录检验项目的具体值。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal? 预警上限
  - CALARM_MIN_VALUE decimal? 预警下限
  - CIMG string 图片Base64编码
  - CINPUT_VALUE string 输入值
  - CINSEPCT_WAY int 检验方式
  - CINSPECTION_RECORD_ID long 检验记录主表ID
  - CINSPECTION_TOOL_CID long? 检验工具ID
  - CIS_PHYSICS_LAB string 是否送物理实验室
  - CREMARK string 备注
  - CRESULT int 检验结果
  - CSAMPLE_QTY string 抽样数量
  - CSEQ int? 顺序号
  - CSTANDARD_MAX_ALLOW string 标准上限是否允许等于
  - CSTANDARD_MAX_VALUE decimal? 标准上限
  - CSTANDARD_MIN_ALLOW string 标准下限是否允许等于
  - CSTANDARD_MIN_VALUE decimal? 标准下限
  - CSTANDARD_VALUE string 标准值
  - CSTANDARD_VALUE_TYPE int? 标准值类型
  - CTEMPLATE_ITEM_CODE string 模板项目编码
  - CTEMPLATE_ITEM_DESC string 模板项目描述
  - CTEMPLATE_ITEM_ID long 模板项目ID
  - CTEMPLATE_ITEM_NAME string 模板项目名称
  - CTEMPLATE_ITEM_TAG string 模板项目标签
  - CUNIT string 单位
  - LOWER_TOLERANCE decimal? 下公差
  - orientation string 图片方向
  - UPPER_TOLERANCE decimal? 上公差
  - url string 图片地址
- 关联关系：
  - TBL_QM_INSPECTION_RECORD_ITEM.CINSPECTION_RECORD_ID = TBL_QM_INSPECT_RECORD.CID

----------------------
115. TBL_QM_MEDICINE_TANK（药缸信息表）
- 业务含义：药缸信息表，存储药水缸体信息。
- 字段列表：
  - CID long 主键ID
  - CMEDICINE_TANK_NAME string 药缸名称
  - CMEDICINE_TANK_NO string 药缸编号
  - CREMARK string 备注
  - CTEMPLATE_ID long? 模板ID
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_QM_MEDICINE_TANK.CWC_ID = TBL_BD_WC.CID

----------------------
116. TBL_QM_PL_LOG（物理实验室送检记录主表）
- 业务含义：物理实验室送检记录主表。
- 字段列表：
  - CID long 主键ID
  - CCHECK_REMARK string 审核备注
  - CCHECK_TIME DateTime? 审核时间
  - CCHECK_USER string 审核人
  - CINSPECT_CODE string 检验单号
  - CINSPECT_QTY decimal? 检验数量
  - CINSPECT_REMARK string 检验备注
  - CINSPECT_TIME DateTime? 检验时间
  - CINSPECT_TYPE int? 检验类型
  - CINSPECT_USER string 检验人
  - CIS_LAB string 是否送检
  - CITEM_ID long 物料ID
  - CMO_LOT string 工单批次
  - CNG_DISPOSAL string 不良处置
  - CORDER_ID long 订单ID
  - CPOSITION string 送检位置
  - CPROCESS_ID long 工序ID
  - CRECEIVE_TIME DateTime? 接收时间
  - CRECEIVE_USER string 接收人
  - CREMARK string 备注
  - CRESULT int? 结果
  - CSCAN_BARCODE string 扫描条码
  - CSHIFT string 班次
  - CSTATUS int? 状态
  - CSUBMIT_QTY decimal? 报检数量
  - CSUBMIT_REMARK string 送检备注
  - CSUBMIT_REQUEST string 送检要求
  - CSUBMIT_TIME DateTime? 送检时间
  - CSUBMIT_USER string 送检人
  - CTEMPLATE_ID long 模板ID
  - CTEST_ITEM_ID long 检测项目ID
  - CTEST_ITEM_NAME string 检测项目名称
  - CUNIT string 单位
  - CUSTOMER_CODE string 客户编码
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_QM_PL_LOG.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_QM_PL_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_QM_PL_LOG.CWC_ID = TBL_BD_WC.CID

----------------------
117. TBL_QM_PL_LOG_ITEM（物理实验室送检记录明细表）
- 业务含义：物理实验室送检记录明细表。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal? 预警上限
  - CALARM_MIN_VALUE decimal? 预警下限
  - CINPUT_VALUE string 输入值
  - CINPUT_VALUE_COUNT int 输入值数量
  - CPL_LOG_ID long 送检主表ID
  - CPOSITION string 位置
  - CREMARK string 备注
  - CRESULT int? 判定结果
  - CSCRAP_QTY int 报废数量
  - CSEQ int? 顺序号
  - CSTANDARD_MAX_ALLOW string 标准上限是否允许等于
  - CSTANDARD_MAX_VALUE decimal? 标准上限
  - CSTANDARD_MIN_ALLOW string 标准下限是否允许等于
  - CSTANDARD_MIN_VALUE decimal? 标准下限
  - CSTANDARD_VALUE string 标准值
  - CSTANDARD_VALUE_TYPE int? 标准值类型
  - CSUBMIT_REQUEST string 送检要求
  - CTEMPLATE_ITEM_CODE string 模板项目编码
  - CTEMPLATE_ITEM_DESC string 模板项目描述
  - CTEMPLATE_ITEM_ID long 模板项目ID
  - CTEMPLATE_ITEM_NAME string 模板项目名称
  - CTEMPLATE_ITEM_TAG string 模板项目标签
  - CTEXTBOX_QTY int 文本框数量
  - CUNIT string 单位
- 关联关系：
  - TBL_QM_PL_LOG_ITEM.CPL_LOG_ID = TBL_QM_PL_LOG.CID

---
六、文件管理

----------------------
118. TBL_ESOP_CONTACT_FORM（联络单信息表）
- 业务含义：联络单信息表，存储内部联络单流程数据。
- 字段列表：
  - CID long 主键ID
  - CAPPLICANT_NO string 申请编号
  - CAPPROVAL_DATE DateTime? 批准日期
  - CAPPROVAL_DESC string 批准意见
  - CAPPROVAL_RESULT int? 批准结果
  - CAPPROVAL_USER string 批准人
  - CBACKGROUND string 背景
  - CCATEGORY string 分类
  - CCOUNTERSIGN int? 会签状态
  - CFILE_PATH string 附件
  - CISSUE_DATE DateTime? 发出日期
  - CISSUE_USER string 发出人
  - CPRESENTATION string 呈送
  - CREVIEW_DATE DateTime? 审核日期
  - CREVIEW_DESC string 审核意见
  - CREVIEW_RESULT int? 审核结果
  - CREVIEW_USER string 审核人
  - CSHADOW_COPY string 影送
  - CSUBJECT string 主题

----------------------
119. TBL_ESOP_COUNTERSIGN（4M文件会签信息表）
- 业务含义：4M文件/联络单会签信息记录。
- 字段列表：
  - CID long 主键ID
  - CDATE DateTime? 会签日期
  - CDEPT_NAME string 会签部门
  - CMAIN_ID long 主表ID
  - CREMARK string 会签备注
  - CTYPE int? 类型
  - CUSER_NAME string 会签人

----------------------
120. TBL_ESOP_FILE（ESOP文件主表）
- 业务含义：ESOP文件管理主表，存储文件元数据。
- 字段列表：
  - CID long 主键ID
  - CAUDIT_MAN string 审核人
  - CAUDIT_TIME DateTime? 审核时间
  - CCOMPANY string 测试公司
  - CEXPIRY_DATE DateTime? 有效期
  - CFILE_CATEGORY long? 文件分类ID
  - CFILE_LEVEL string 文件等级
  - CFILE_NAME string 文件名称
  - CFILE_NO string 文件编号
  - CFILE_PATH string 文件路径
  - CFILE_TYPE long 文件类型ID
  - CFILE_VERSION string 文件版本
  - CIS_AUDIT string 是否审核
  - CMODEL string 型号
  - CREMARK string 备注
  - CREPORT_STATUS int? 测试报告状态
  - CREPORT_TYPE string 报告类型
  - CSCRAP_REMARK string 报废备注
  - CSCRAP_TIME DateTime? 报废时间
  - CSCRAP_USER string 报废人
  - CSTATUS int? 状态
  - CSUPPLIER string 供应商
  - CTEMP_NAME string 模板名称
  - CTEMP_NO string 模板编号
  - CTEST_DATE DateTime? 测试日期
  - CTYPE string 类型
  - CURL string 文件访问地址

----------------------
121. TBL_ESOP_FILE_CATEGORY（ESOP文件分类表）
- 业务含义：ESOP文件分类表，支持树形分类。
- 字段列表：
  - CID long 主键ID
  - CFILE_CATEGORY_NAME string 分类名称
  - CFILE_CATEGORY_NO string 分类编号
  - CFILE_CATEGORY_PATH string 分类层级路径
  - CPARENT_ID long 上级分类ID
  - CSEQ int 排序号
- 关联关系：
  - TBL_ESOP_FILE_CATEGORY.CPARENT_ID = TBL_ESOP_FILE_CATEGORY.CID

----------------------
122. TBL_ESOP_FILE_SIGN（文件手写体信息）
- 业务含义：文件手写体签名信息存储。
- 字段列表：
  - CID long 主键ID
  - CFILE_PATH string 签名文件路径
  - CFILE_TYPE string 签名文件类型
  - CUSER_NAME string 用户姓名
  - CUSER_NO string 用户工号

----------------------
123. TBL_ESOP_FILE_TYPE（ESOP文件类型表）
- 业务含义：ESOP文件类型定义表。
- 字段列表：
  - CID long 主键ID
  - CFILE_EXTENDED string 允许的文件后缀
  - CTYPE_DESC string 类型描述
  - CTYPE_NAME string 类型名称
  - CTYPE_NO string 类型编号

----------------------
124. TBL_ESOP_TEMPLATE（ESOP模板关联表）
- 业务含义：ESOP模板与文件关联表。
- 字段列表：
  - CID long 主键ID
  - CFILE_ID long? 文件ID
  - CTEMP_FACTORY string 工厂
  - CTEMP_ID long? 模板ID
  - CTEMP_MODEL string 型号
  - CTEMP_NO string 模板编号

----------------------
125. TBL_ESOP_TEMPORARY_CHANGE_ORDER（4M临时变更单）
- 业务含义：4M临时变更申请单，记录人机料法变更。
- 字段列表：
  - CID long 主键ID
  - CAFTER_ITEM string 变更后料号
  - CAPPLICANT_DATE DateTime? 申请日期
  - CAPPLICANT_DEPARTMENT string 申请部门
  - CAPPLICANT_NAME string 申请人
  - CAPPLICANT_NO string 申请编号
  - CAPPLY_SOP bool? 申请标准化
  - CAPPLY_VERIFY bool? 申请重新验证
  - CATTACHMENT_AFTER string 上传附件（变更后）
  - CATTACHMENT_BEFORE string 上传附件（变更前）
  - CBEFORE_ITEM string 变更前料号
  - CCHANGE_AFTER string 变更后
  - CCHANGE_BEFORE string 变更前
  - CCHANGE_PERIOD string 变更期限
  - CCONFIRM_DATE DateTime? 品质确认时间
  - CCONFIRM_USER string 品质确认人
  - CCOUNTERSIGN int? 会签状态
  - CCUSTOMER_APPLY bool? 是否向客户提出申请
  - CERP_FILE_NO string ERP文件
  - CEXECUTION_DATE DateTime? 执行变更日期
  - CEXPIRY_DATE DateTime? 有效期
  - CINVOLVED_ITEM_NO string 涉及料号
  - CINVOLVED_MACHINE bool? 涉及机器
  - CINVOLVED_MATERIAL bool? 涉及材料
  - CINVOLVED_METHOD bool? 涉及方法
  - CINVOLVED_PROCESS string 涉及变更工序
  - CINVOLVED_USER bool? 涉及人员
  - CIS_RECOVERY bool? 恢复原状
  - CNEW_4M_NAME string 新4M名称
  - CORDER_NUMBER string 订单号
  - CPREVIOUS_INVENTORY_HANDLING string 变更前在制品、库存品处理方式
  - CREASON_AND_PURPOSE string 变更原因及目的
  - CREVIEW_DATE DateTime? 审核时间
  - CREVIEW_DESC string 审核意见
  - CREVIEW_RESULT int? 审核结果
  - CREVIEW_TODO bool 是否生成代码事项
  - CREVIEW_USER string 审核人

----------------------
126. TBL_FOURM_CHANGE_ITEM_LOG（4M变更料号日志表）
- 业务含义：4M变更涉及的料号变更日志。
- 字段列表：
  - CID long 主键ID
  - CAFTER_ITEM string 变更后料号
  - CBEFOR_ITEM string 变更前料号
  - CFOURM_ID long 表单ID
  - CPART string 部件

---
七、点检保养

----------------------
127. TBL_EAM_PM_TEMP_WC_LINK（模板关联工作中心）
- 业务含义：点检/保养模板与工作中心关联表。
- 字段列表：
  - CID long 主键ID
  - CTEMP_ID long? 模板ID
  - CWC_ID long? 工作中心ID
- 关联关系：
  - TBL_EAM_PM_TEMP_WC_LINK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_PM_TEMP_WC_LINK.CWC_ID = TBL_BD_WC.CID

----------------------
128. TBL_NP_TEMPLATE（模板主表）
- 业务含义：点检/保养模板主表。
- 字段列表：
  - CID long 主键ID
  - CTEMPLATE_CODE string 模板编码
  - CTEMPLATE_NAME string 模板名称
  - CTEMPLATE_TYPE_ID long? 模板类型标识

----------------------
129. TBL_NP_TEMPLATE_CHANGE（模板变更主表）
- 业务含义：模板变更记录主表，记录模板版本变更。
- 字段列表：
  - CID long 主键ID
  - CAPPROVAL_ID long? 审批流标识
  - CAUDIT_REMARK string 审核备注
  - CAUDIT_STATUS int 审核状态
  - CAUDIT_TIME DateTime? 审核时间
  - CAUDIT_USER_ID string 审核人标识
  - CCHANGE_REMARK string 变更备注
  - CCHANGE_TIME DateTime 变更时间
  - CCHANGE_USER_ID string 变更人标识
  - CGROUP_ID long 分组标识
  - CIS_NEW string 是否新增
  - CTEMPLATE_CODE string 模板编码
  - CTEMPLATE_DESC string 模板描述
  - CTEMPLATE_NAME string 模板名称
  - CTEMPLATE_TYPE_ID long 模板类型标识
  - CTEMPLATE_VERSION double 模板版本

----------------------
130. TBL_NP_TEMPLATE_CHANGE_ITEM（模板变更明细表）
- 业务含义：模板变更明细表，记录模板项变更前后值。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal? 报警最大值（原值）
  - CALARM_MAX_VALUE_EDIT decimal? 报警最大值（变更后）
  - CALARM_MIN_VALUE decimal? 报警最小值（原值）
  - CALARM_MIN_VALUE_EDIT decimal? 报警最小值（变更后）
  - CCHECK_CONTENT long 检测内容标识（原值）
  - CCHECK_CONTENT_EDIT long 检测内容标识（变更后）
  - CCHECK_WAY int 检测方式（原值）
  - CCHECK_WAY_EDIT int 检测方式（变更后）
  - CDEFAULT_VALUE string 默认值（原值）
  - CDEFAULT_VALUE_EDIT string 默认值（变更后）
  - CDEFAULT_VALUE_TYPE int 默认值类型（原值）
  - CDEFAULT_VALUE_TYPE_EDIT int 默认值类型（变更后）
  - CDEVIATION_TYPE int 偏差类型（原值）
  - CDEVIATION_TYPE_EDIT int 偏差类型（变更后）
  - CFORMULA string 公式（原值）
  - CFORMULA_EDIT string 公式（变更后）
  - CINPUT_FORMULA string 输入公式（原值）
  - CINPUT_FORMULA_EDIT string 输入公式（变更后）
  - CINPUT_TYPE int 输入类型（原值）
  - CINPUT_TYPE_EDIT int 输入类型（变更后）
  - CIS_CHECK_RESULT string 是否参与结果判定（原值）
  - CIS_CHECK_RESULT_EDIT string 是否参与结果判定（变更后）
  - CIS_CHEMISTAY_LAB string 是否送化学实验室（原值）
  - CIS_CHEMISTAY_LAB_EDIT string 是否送化学实验室（变更后）
  - CIS_KEY_ITEM string 是否关键项（原值）
  - CIS_KEY_ITEM_EDIT string 是否关键项（变更后）
  - CIS_MUST string 是否必填（原值）
  - CIS_MUST_EDIT string 是否必填（变更后）
  - CIS_PHYSICS_LAB string 是否送物理实验室（原值）
  - CIS_PHYSICS_LAB_EDIT string 是否送物理实验室（变更后）
  - CIS_SHOW_STANDARD string 是否显示标准值（原值）
  - CIS_SHOW_STANDARD_EDIT string 是否显示标准值（变更后）
  - CITEM_FREQ_PERIOD_ID long 频次周期标识（原值）
  - CITEM_FREQ_PERIOD_ID_EDIT long 频次周期标识（变更后）
  - CLIST_SOURCE string 列表来源（原值）
  - CLIST_SOURCE_EDIT string 列表来源（变更后）
  - CLIST_SOURCE_TYPE int 列表来源类型（原值）
  - CLIST_SOURCE_TYPE_EDIT int 列表来源类型（变更后）
  - CSEQ int 排序序号（原值）
  - CSEQ_EDIT int 排序序号（变更后）
  - CSTANDARD_MAX_ALLOW string 标准最大允许值（原值）
  - CSTANDARD_MAX_ALLOW_EDIT string 标准最大允许值（变更后）
  - CSTANDARD_MAX_VALUE decimal? 标准最大值（原值）
  - CSTANDARD_MAX_VALUE_EDIT decimal? 标准最大值（变更后）
  - CSTANDARD_MIN_ALLOW string 标准最小允许值（原值）
  - CSTANDARD_MIN_ALLOW_EDIT string 标准最小允许值（变更后）
  - CSTANDARD_MIN_VALUE decimal? 标准最小值（原值）
  - CSTANDARD_MIN_VALUE_EDIT decimal? 标准最小值（变更后）
  - CSTANDARD_VALUE string 标准值（原值）
  - CSTANDARD_VALUE_EDIT string 标准值（变更后）
  - CSTANDARD_VALUE_TYPE int 标准值类型（原值）
  - CSTANDARD_VALUE_TYPE_EDIT int 标准值类型（变更后）
  - CSUM_FIELD string 求和字段（原值）
  - CSUM_FIELD_EDIT string 求和字段（变更后）
  - CTEMPLATE_CHANGE_ID long 变更ID
  - CTEMPLATE_ITEM_CODE string 模板项编码
  - CTEMPLATE_ITEM_DESC string 模板项描述（原值）
  - CTEMPLATE_ITEM_DESC_EDIT string 模板项描述（变更后）
  - CTEMPLATE_ITEM_NAME string 模板项名称（原值）
  - CTEMPLATE_ITEM_NAME_EDIT string 模板项名称（变更后）
  - CTEMPLATE_ITEM_TAG string 模板项标签（原值）
  - CTEMPLATE_ITEM_TAG_EDIT string 模板项标签（变更后）
  - CTOOL_ID long 工具标识（原值）
  - CTOOL_ID_EDIT long 工具标识（变更后）
  - CUNIT string 单位（原值）
  - CUNIT_EDIT string 单位（变更后）
- 关联关系：
  - TBL_NP_TEMPLATE_CHANGE_ITEM.CTEMPLATE_CHANGE_ID = TBL_NP_TEMPLATE_CHANGE.CID

----------------------
131. TBL_NP_TEMPLATE_ITEM（模板项配置表）
- 业务含义：点检/保养模板项配置表。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal 报警最大值
  - CALARM_MIN_VALUE decimal 报警最小值
  - CCHECK_CONTENT long 检测内容标识
  - CCHECK_WAY int 检测方式
  - CDEFAULT_VALUE string 默认值
  - CDEFAULT_VALUE_TYPE int 默认值类型
  - CDEVIATION_TYPE int 偏差类型
  - CINPUT_TYPE int 输入类型
  - CIS_CHECK_RESULT string 是否参与结果判定
  - CIS_CHEMISTAY_LAB string 是否送化学实验室
  - CIS_KEY_ITEM string 是否关键项
  - CIS_MUST string 是否必填
  - CIS_PHYSICS_LAB string 是否送物理实验室
  - CIS_SHOW_STANDARD string 是否显示标准值
  - CITEM_FREQ_PERIOD_ID long 项目频次周期标识
  - CLIST_SOURCE string 列表来源
  - CLIST_SOURCE_TYPE int 列表来源类型
  - CSEQ int 排序序号
  - CSTANDARD_MAX_ALLOW string 标准最大允许值
  - CSTANDARD_MAX_VALUE decimal? 标准最大值
  - CSTANDARD_MIN_ALLOW string 标准最小允许值
  - CSTANDARD_MIN_VALUE decimal? 标准最小值
  - CSTANDARD_VALUE string 标准值
  - CSTANDARD_VALUE_TYPE int 标准值类型
  - CSTANDRAD_SOURCE string 标准来源
  - CSUM_FIELD string 求和字段
  - CTEMPLATE_ID long 模板ID
  - CTEMPLATE_ITEM_CODE string 模板项编码
  - CTEMPLATE_ITEM_DESC string 模板项描述
  - CTEMPLATE_ITEM_NAME string 模板项名称
  - CTEMPLATE_ITEM_TAG string 模板项标签
  - CTOOL_ID long 工具标识
  - CUNIT string 单位
  - LOWER_TOLERANCE decimal? 下公差
  - UPPER_TOLERANCE decimal? 上公差
- 关联关系：
  - TBL_NP_TEMPLATE_ITEM.CTEMPLATE_ID = TBL_NP_TEMPLATE.CID

----------------------
132. TBL_EAM_PM_TEMPLATE_ITEMS（点检模板项目明细表）
- 业务含义：点检模板项目明细表。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX decimal? 报警上限
  - CALARM_MIN decimal? 报警下限
  - CDEFAULT_VALUE string 默认值
  - CINPUT_TYPE string 输入类型
  - CIS_CHECK_RESULT bool 是否参与结果判定
  - CIS_INTERVAL Boolean? 是否区间录入
  - CIS_KEY_ITEM bool 是否关键项
  - CIS_MUST bool 是否必填
  - CIS_MUST_UPLOAD_IMG bool 是否必须上传图片
  - CIS_REGULAR bool 是否正则校验
  - CIS_SERVICE_CHECK bool 是否服务端校验
  - CIS_SHOW_STANDARD bool 是否显示标准值
  - CIS_SHOW_UPLOAD_IMG bool 是否显示上传图片
  - CITEM_DESC string 项目描述
  - CITEM_FREQ string 项目频率
  - CITEM_NAME string 项目名称
  - CITEM_NO string 项目编号
  - CITEM_TAG string 项目标记
  - CLIST_SOURCE string 列表数据源
  - CREGULAR string 正则表达式
  - CREGULAR_TIPS string 正则提示
  - CSEQ int 排序号
  - CSERVICE string 服务配置
  - CSTANDARD_VALUE string 标准值
  - CTEMP_ID long 模板ID
  - CUNIT string 单位
  - CWARM_MAX decimal? 预警上限
  - CWARM_MIN decimal? 预警下限

----------------------
133. TBL_EAM_EQUIPMENT（设备主数据表）
- 业务含义：设备主数据表，存储设备基础信息。
- 字段列表：
  - CID long 主键ID
  - CAPPROACH_DATE DateTime? 进厂日期
  - CASSET_NUMBER string 资产编号
  - CBRAND string 品牌
  - CCAPACITY string 产能
  - CDEPT_ID Int64? 责任部门ID
  - CDUTY_DEPT_NO string 责任部门编号
  - CDUTY_PERSON_NO string 责任人工号
  - CENTER_DATE DateTime? 验收日期
  - CEQUIPMENT_CODE string 设备编码
  - CEQUIPMENT_MODEL string 设备型号
  - CEQUIPMENT_NAME string 设备名称
  - CEQUIPMENT_SUPPLIER string 设备供应商
  - CFACTORY_EQUIPMENT_CODE string 厂内设备编码
  - CIS_CONNECT string 是否联网
  - CLIABLE_PERSON string 责任人
  - CLINK string 联系方式
  - CMANUFACTURING_DATE DateTime? 出厂日期
  - CPURCHASE_WAY string 采购方式
  - CQTY string 数量
  - CREMARK string 备注
  - CSPEC string 规格
  - CSTATUS string 设备状态
  - CSUPPLIER_NO string 供应商编号
  - CTYPE_ID Int64? 设备类型ID
  - CUSE_DEPT_NO string 使用部门编号
  - CWC_ID Int64? 工作中心ID
  - CWORK_CENTER_CID Int64? 工作中心CID
  - CWORK_SHOP_NO string 车间编号
  - CWORKSHOP string 车间
- 关联关系：
  - TBL_EAM_EQUIPMENT.CWC_ID = TBL_BD_WC.CID

----------------------
134. TBL_EAM_EQUIPMENT_TYPE（设备类型信息表）
- 业务含义：设备类型定义表。
- 字段列表：
  - CID long 主键ID
  - CEQUIPMENT_TYPE_CODE string 设备类型编码
  - CEQUIPMENT_TYPE_DESC string 设备类型描述
  - CEQUIPMENT_TYPE_GROUP string 设备类型分组
  - CEQUIPMENT_TYPE_NAME string 设备类型名称

----------------------
135. TBL_EAM_ERROR_CODE（设备故障代码表）
- 业务含义：设备故障代码定义表。
- 字段列表：
  - CID long 主键ID
  - CERROR_CODE string 故障代码
  - CERROR_DESC string 故障描述
  - CERROR_LEVEL string 故障等级
  - CERROR_NAME string 故障名称
  - CERROR_TYPE string 故障类型

----------------------
136. TBL_EAM_FREQUENCY（设备保养频次配置表）
- 业务含义：设备保养频次配置表。
- 字段列表：
  - CID long 主键ID
  - CCOUNT int 频次数值
  - CCOUNT_UNIT string 计数单位
  - CFREQ_DESC string 频次说明
  - CFREQ_NAME string 频次名称
  - CFREQ_UNIT string 频次单位

----------------------
137. TBL_EAM_MAINTAIN_STANDARD_IMG（保养标准图片表）
- 业务含义：保养标准图片存储表。
- 字段列表：
  - CID long 主键ID
  - CIMAGE_PATH string 图片路径
  - CITEM_ID Int64 保养模板项目ID

----------------------
138. TBL_EAM_MAINTAIN_TASK（保养任务主表）
- 业务含义：保养任务主表，记录保养任务执行情况。
- 字段列表：
  - CID long 主键ID
  - CAPPROVAL_ID Int64 审批流ID
  - CAPPROVAL_STATUS Int32 审批状态
  - CBASE_TASK_NO String 基准任务编号
  - CCHECK_REMARK string 点检备注
  - CCHECK_STATUS int 点检状态
  - CEMPOLYEE_NAME String 执行人姓名
  - CEMPOLYEE_NO String 执行人工号
  - CIS_INTERVAL bool 是否按间隔生成任务
  - CMAINTAIN_TIME DateTime? 保养执行时间
  - CREMARK string 备注
  - CRESULT String 保养结果
  - CTASK_CREATED_TIME DateTime? 任务创建时间
  - CTASK_NO String 任务编码
  - CTASK_STAND_TIME_E DateTime? 标准结束时间
  - CTASK_STAND_TIME_S DateTime? 标准开始时间
  - CTASK_STATUS Int32 任务状态
  - CTASK_TAG String 任务标签
  - CTASK_TYPE String 任务类型
  - CTEMP_ID Int64 模板ID
  - CTEMP_NAME String 模板名称
  - CTEMP_NO String 模板编号
  - CWC_ID Int64 工作中心ID
- 关联关系：
  - TBL_EAM_MAINTAIN_TASK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_MAINTAIN_TASK.CWC_ID = TBL_BD_WC.CID

----------------------
139. TBL_EAM_MAINTAIN_TASK_CHANGE_LOG（保养任务时间变更日志表）
- 业务含义：保养任务计划时间变更日志。
- 字段列表：
  - CID long 主键ID
  - CNEW_TIME string 新计划时间
  - COLD_TIME string 原计划时间
  - CREMARK string 备注
  - CTASK_ID long 任务ID
- 关联关系：
  - TBL_EAM_MAINTAIN_TASK_CHANGE_LOG.CTASK_ID = TBL_EAM_MAINTAIN_TASK.CID

----------------------
140. TBL_EAM_MAINTAIN_TASK_ITEM（保养任务明细表）
- 业务含义：保养任务明细表，记录保养项目的执行值和结果。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX Decimal 报警上限
  - CALARM_MIN Decimal 报警下限
  - CDEFAULT_VALUE String 默认值
  - CHID Int64 任务主表ID
  - CINPUT_TYPE String 输入类型
  - CINPUT_VALUE String 输入值
  - CIS_CHECK_RESULT Boolean 是否校验结果
  - CIS_INTERVAL Boolean 是否按间隔生成任务
  - CIS_KEY_ITEM Boolean 是否关键项
  - CIS_MUST Boolean 是否必填
  - CIS_MUST_UPLOAD_IMG bool 是否必须上传图片
  - CIS_REGULAR Boolean 是否正则校验
  - CIS_SERVICE_CHECK Boolean 是否服务校验
  - CIS_SHOW_STANDARD bool 是否显示标准值
  - CIS_SHOW_UPLOAD_IMG bool 是否显示上传图片入口
  - CITEM_DESC String 项目描述
  - CITEM_FREQ String 项目频次
  - CITEM_ID Int64 模板项ID
  - CITEM_NAME String 项目名称
  - CITEM_NO String 项目编号
  - CITEM_TAG String 项目标记
  - CLIST_SOURCE String 下拉数据源
  - CREGULAR String 正则表达式
  - CREGULAR_TIPS String 正则提示
  - CREMARK string 备注
  - CRESULT string 检查结果
  - CSEQ int 排序
  - CSERVICE String 服务地址
  - CSTANDARD_VALUE String 标准值
  - CTEMP_ID Int64 模板ID
  - CUNIT String 单位
  - CWARM_MAX Decimal 预警上限
  - CWARM_MIN Decimal 预警下限
- 关联关系：
  - TBL_EAM_MAINTAIN_TASK_ITEM.CHID = TBL_EAM_MAINTAIN_TASK.CID

----------------------
141. TBL_EAM_MAINTAIN_TASK_ITEM_IMG（保养任务明细图片表）
- 业务含义：保养任务明细图片存储表。
- 字段列表：
  - CID long 主键ID
  - CIMAGE_PATH string 图片路径
  - CITEM_ID Int64 保养任务明细ID
- 关联关系：
  - TBL_EAM_MAINTAIN_TASK_ITEM_IMG.CITEM_ID = TBL_EAM_MAINTAIN_TASK_ITEM.CID

----------------------
142. TBL_EAM_MAINTAIN_TEMP_D（保养模板变更历史明细表）
- 业务含义：保养模板变更历史明细表。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX Decimal 报警上限
  - CALARM_MAX_EDIT Decimal 变更后报警上限
  - CALARM_MIN Decimal 报警下限
  - CALARM_MIN_EDIT Decimal 变更后报警下限
  - CDEFAULT_VALUE String 默认值
  - CDEFAULT_VALUE_EDIT String 变更后默认值
  - CHID Int64 变更主表ID
  - CINPUT_TYPE String 输入类型
  - CINPUT_TYPE_EDIT String 变更后输入类型
  - CIS_CHECK_RESULT Boolean 是否校验结果
  - CIS_CHECK_RESULT_EDIT Boolean 变更后是否校验结果
  - CIS_INTERVAL Boolean 是否按间隔生成任务
  - CIS_INTERVAL_EDIT Boolean 变更后是否按间隔生成任务
  - CIS_KEY_ITEM Boolean 是否关键项
  - CIS_KEY_ITEM_EDIT Boolean 变更后是否关键项
  - CIS_MUST Boolean 是否必填
  - CIS_MUST_EDIT Boolean 变更后是否必填
  - CIS_MUST_UPLOAD_IMG bool 是否必须上传图片
  - CIS_MUST_UPLOAD_IMG_EDIT bool 变更后是否必须上传图片
  - CIS_REGULAR Boolean 是否正则校验
  - CIS_REGULAR_EDIT Boolean 变更后是否正则校验
  - CIS_SERVICE_CHECK Boolean 是否服务校验
  - CIS_SERVICE_CHECK_EDIT Boolean 变更后是否服务校验
  - CIS_SHOW_STANDARD bool 是否显示标准值
  - CIS_SHOW_STANDARD_EDIT bool 变更后是否显示标准值
  - CIS_SHOW_UPLOAD_IMG bool 是否显示上传图片入口
  - CIS_SHOW_UPLOAD_IMG_EDIT bool 变更后是否显示上传图片入口
  - CITEM_DESC String 项目描述
  - CITEM_DESC_EDIT String 变更后项目描述
  - CITEM_FREQ String 项目频次
  - CITEM_FREQ_EDIT String 变更后项目频次
  - CITEM_ID Int64 项目ID
  - CITEM_NAME String 项目名称
  - CITEM_NAME_EDIT String 变更后项目名称
  - CITEM_NO String 项目编号
  - CITEM_TAG String 项目标记
  - CITEM_TAG_EDIT String 变更后项目标签
  - CLIST_SOURCE String 下拉数据源
  - CLIST_SOURCE_EDIT String 变更后下拉数据源
  - CREGULAR String 正则表达式
  - CREGULAR_EDIT String 变更后正则表达式
  - CREGULAR_TIPS String 正则提示
  - CREGULAR_TIPS_EDIT String 变更后正则提示
  - CSEQ int 排序
  - CSEQ_EDIT int 变更后排序
  - CSERVICE String 服务地址
  - CSERVICE_EDIT String 变更后服务地址
  - CSTANDARD_VALUE String 标准值
  - CSTANDARD_VALUE_EDIT String 变更后标准值
  - CTEMP_ID Int64 模板ID
  - CUNIT String 单位
  - CUNIT_EDIT String 变更后单位
  - CWARM_MAX Decimal 预警上限
  - CWARM_MAX_EDIT Decimal 变更后预警上限
  - CWARM_MIN Decimal 预警下限
  - CWARM_MIN_EDIT Decimal 变更后预警下限

----------------------
143. TBL_EAM_MAINTAIN_TEMP_WC_LINK（保养模板与工作中心关联表）
- 业务含义：保养模板与工作中心关联表。
- 字段列表：
  - CID long 主键ID
  - CTEMP_ID Int64 模板ID
  - CWC_ID Int64 工作中心ID
- 关联关系：
  - TBL_EAM_MAINTAIN_TEMP_WC_LINK.CTEMP_ID = TBL_NP_TEMPLATE.CID
  - TBL_EAM_MAINTAIN_TEMP_WC_LINK.CWC_ID = TBL_BD_WC.CID

----------------------
144. TBL_EAM_MAINTAIN_TEMPLATE_ITEMS（保养模板项目表）
- 业务含义：保养模板项目定义表。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX Decimal 报警上限
  - CALARM_MIN Decimal 报警下限
  - CDEFAULT_VALUE String 默认值
  - CINPUT_TYPE String 输入类型
  - CIS_CHECK_RESULT Boolean 是否校验结果
  - CIS_INTERVAL Boolean 是否按间隔生成任务
  - CIS_KEY_ITEM Boolean 是否关键项
  - CIS_MUST Boolean 是否必填
  - CIS_MUST_UPLOAD_IMG bool 是否必须上传图片
  - CIS_REGULAR Boolean 是否正则校验
  - CIS_SERVICE_CHECK Boolean 是否服务校验
  - CIS_SHOW_STANDARD bool 是否显示标准值
  - CIS_SHOW_UPLOAD_IMG bool 是否显示上传图片入口
  - CITEM_DESC String 项目描述
  - CITEM_FREQ String 项目频次
  - CITEM_NAME String 项目名称
  - CITEM_NO String 项目编号
  - CITEM_TAG String 项目标记
  - CLIST_SOURCE String 下拉数据源
  - CREGULAR String 正则表达式
  - CREGULAR_TIPS String 正则提示
  - CSEQ int 排序
  - CSERVICE String 服务地址
  - CSTANDARD_VALUE String 标准值
  - CTEMP_ID Int64 模板ID
  - CUNIT String 单位
  - CWARM_MAX Decimal 预警上限
  - CWARM_MIN Decimal 预警下限

----------------------
145. TBL_EAM_REPAIR（维修工单主表）
- 业务含义：设备维修工单主表，记录报修、维修、关闭全流程。
- 字段列表：
  - CID long 主键ID
  - CAPPLY_DATE DateTime? 报修时间
  - CAPPLY_MAN string 报修人工号
  - CASSIGNMENT_DATE DateTime? 指派时间
  - CASSIGNMENT_MAN string 指派人工号
  - CAUDIT_DEPARTMNT string 审核部门
  - CAUDIT_STATUS string 审核状态
  - CAUDIT_USERNAME string 审核/驳回人
  - CCAUSE string 故障根因
  - CCLOSE_DATE DateTime? 关闭时间
  - CCLOSE_MAN string 关闭人工号
  - CDEMAND_DATE DateTime? 要求完成时间
  - CEND_REPAIR_DATE DateTime? 结束维修时间
  - CERROR_DESC string 故障描述
  - CERROR_ID Int64 故障代码ID
  - CERROR_REASON string 故障原因描述
  - CIS_PRODUCT string 是否停产
  - CIS_URGENT string 是否紧急
  - CODE string 用户工号
  - CPLAN_COMPLETE_DATE DateTime? 计划完成时间
  - CPRIORITY int 优先级
  - CREMARK string 备注
  - CREPAIR_CODE string 维修单编号
  - CREPAIR_DESC string 维修措施说明
  - CREPAIR_MAN string 维修人工号
  - CSCORE int 评分
  - CSTART_REPAIR_DATE DateTime? 开始维修时间
  - CSTATUS string 工单状态
  - CWAIT_MATERIAL_DATE DateTime? 开始待料时间
  - CWC_CHILDREN long? 设备故障子节点
  - CWC_ID Int64 工作中心ID
  - NAME string 用户姓名
- 关联关系：
  - TBL_EAM_REPAIR.CWC_ID = TBL_BD_WC.CID
  - TBL_EAM_REPAIR.CERROR_ID = TBL_EAM_ERROR_CODE.CID

----------------------
146. TBL_EAM_REPAIR_IMG（维修图片记录表）
- 业务含义：维修工单图片记录表。
- 字段列表：
  - CID long 主键ID
  - CIMAGE_PATH string 图片路径
  - CREPAIR_ID Int64 维修单ID
  - CTYPE int 图片类型
- 关联关系：
  - TBL_EAM_REPAIR_IMG.CREPAIR_ID = TBL_EAM_REPAIR.CID

----------------------
147. TBL_EAM_REPAIR_MAN（指派人员列表）
- 业务含义：维修工单指派人员记录。
- 字段列表：
  - CID long 主键ID
  - CREPAIR_CODE string 维修单编号
  - CREPAIR_ID long 维修单ID
  - CREPAIR_MAN_CODE_PRE string 指派人账号
  - CREPAIR_MAN_NAME_PRE string 指派人名称
- 关联关系：
  - TBL_EAM_REPAIR_MAN.CREPAIR_ID = TBL_EAM_REPAIR.CID

----------------------
148. TBL_EAM_REPAIR_MATERIAL（维修耗材记录表）
- 业务含义：维修工单耗材使用记录。
- 字段列表：
  - CID long 主键ID
  - CMATERIAL_NAME string 物料名称
  - CMATERIAL_SPEC string 物料规格
  - CQTY int 数量
  - CREPAIR_ID Int64 维修单ID
- 关联关系：
  - TBL_EAM_REPAIR_MATERIAL.CREPAIR_ID = TBL_EAM_REPAIR.CID

---
八、生产流程

----------------------
149. TBL_SFC_WS_LOG（生产记录表）
- 业务含义：工位报工/检验类生产记录主表（数量、班次、条码、模板等）。
- 字段列表：
  - CID long 主键ID
  - BOARD_TYPE string 板类型
  - CCHECK_REMARK string 审核备注
  - CCHECK_TIME DateTime? 审核时间
  - CCHECK_USER_NAME string 审核人账号
  - CEND_TIME DateTime? 完工时间
  - CEND_USER_NAME string 完工人账号
  - CIS_CHECK string 是否已审核
  - CIS_FINISH string 是否完工
  - CIS_WIP string 是否已过数
  - CITEM_ID long? 物料ID
  - CLEVEL string 等级
  - CMO_LOT string 工单批次
  - CNG_NUMBER decimal? 不良数量
  - CNUMBER_TYPE int? 数量类型
  - CORDER_ID long? 订单ID
  - CPROCESS_ID long 工序ID
  - CREMARK string 备注
  - CSCAN_BARCODE string 扫描条码
  - CSCRAP_NUMBER decimal? 报废数量
  - CSHIFT string 班次
  - CSTART_TIME DateTime? 开工时间
  - CSTART_USER_NAME string 开工人账号
  - CSTATUS int? 状态
  - CTEMPLATE_ID long 模板ID
  - CUNIT string 单位
  - CUSTOMER_CODE string 客户编码
  - CWC_ID long 工作中心ID
  - CWORK_NUMBER decimal 工作数量
  - CWORK_TYPE int 工作类型
- 关联关系：
  - TBL_SFC_WS_LOG.CMO_LOT = TBL_MO.CMO_LOT
  - TBL_SFC_WS_LOG.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_SFC_WS_LOG.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SFC_WS_LOG.CWC_ID = TBL_BD_WC.CID

----------------------
150. TBL_SFC_WS_LOG_ITEM（生产记录项目明细）
- 业务含义：生产记录项目明细表，记录报工时填写的检验项目值。
- 字段列表：
  - CID long 主键ID
  - CALARM_MAX_VALUE decimal? 预警上限
  - CALARM_MIN_VALUE decimal? 预警下限
  - CINPUT_VALUE string 输入值
  - CREMARK string 备注
  - CRESULT int 结果
  - CSEQ int 排序号
  - CSTANDARD_MAX_ALLOW string 标准上限是否允许等于
  - CSTANDARD_MAX_VALUE decimal? 标准上限
  - CSTANDARD_MIN_ALLOW string 标准下限是否允许等于
  - CSTANDARD_MIN_VALUE decimal? 标准下限
  - CSTANDARD_VALUE string 标准值
  - CSTANDARD_VALUE_TYPE int 标准值类型
  - CTEMPLATE_ITEM_CODE string 模板项编码
  - CTEMPLATE_ITEM_DESC string 模板项描述
  - CTEMPLATE_ITEM_NAME string 模板项名称
  - CTEMPLATE_ITEM_TAG string 模板项标签
  - CUNIT string 单位
  - CWS_LOG_ID long 生产记录主表ID
- 关联关系：
  - TBL_SFC_WS_LOG_ITEM.CWS_LOG_ID = TBL_SFC_WS_LOG.CID

----------------------
151. TBL_SFC_WS_TEMPLATE_CONFIG（工位报工模板配置表）
- 业务含义：工位报工模板配置表，控制报工界面行为。
- 字段列表：
  - CID long 主键ID
  - CFIRST_COMMIT_TIMESPAN int? 一次报工自动补全时间差
  - CIS_AUTO_GET_NUMBER string 是否自动获取数量
  - CIS_CONTROL_NUMBER string 是否管控数量
  - CIS_FIRST_COMMIT string 是否一次报工
  - CIS_GET_LAST_DATA string 是否赋值上次记录
  - CIS_IGNORE_ITEM string 赋值上次记录时是否忽略产品
  - CIS_IPQC_FIRST string 是否需要IPQC首件管控
  - CIS_KEYPART_MANAGE string 是否关键物料管控
  - CIS_LOCK_NUMBER string 是否锁定数量
  - CIS_NO_ORDER string 是否允许无工单生产记录
  - CIS_PM string 是否校验设备点检
  - CIS_WIP_TEMPLATE string 是否过数模板
  - CNEXT_TIMESPAN int? 相同lot卡下一次开工最小时间间隔
  - COVERDUE_TIME int? 超期时间
  - CREMARK string 备注
  - CSE_TIMESPAN int? 开工完工最小时间间隔
  - CTEMPLATE_ID long 模板ID
  - CUNIT string 默认单位
  - CWARNING_TIME int? 预警时间

----------------------
152. TBL_SFC_WS_TEMPLATE_LINK（工位模板关联配置表）
- 业务含义：工位模板与工序/工作中心关联表。
- 字段列表：
  - CID long 主键ID
  - CPROCESS_ID long 工序ID
  - CREMARK string 备注
  - CTEMPLATE_ID long 模板ID
  - CWC_ID long 工作中心ID
- 关联关系：
  - TBL_SFC_WS_TEMPLATE_LINK.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SFC_WS_TEMPLATE_LINK.CWC_ID = TBL_BD_WC.CID

----------------------
153. TBL_MO（工单信息表）
- 业务含义：生产工单主表，记录工单计划与执行信息。
- 字段列表：
  - CID long 主键ID
  - CACTULA_END_TIME DateTime? 实际完成时间
  - CACTULA_START_TIME DateTime? 实际生产时间
  - CCOMPLETED_QTY decimal? 完工数量
  - CCUST_ORDER string 客户订单
  - CIS_ACTIVITY string 是否激活
  - CIS_MANUAL string 是否手工创建
  - CITEM_ID long? 物料ID
  - CLEVEL int? 级别
  - CMO_LOT string 工单批次
  - CORDER_DATETIME DateTime? 工单日期
  - CORDER_NO string 工单编号
  - CPARENT_ID string 父级工单编号
  - CPLAN_END_TIME DateTime? 预计完成时间
  - CPLAN_QTY decimal? 计划数量
  - CPLAN_START_TIME DateTime? 预计生产时间
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CROUTE_ID long? 工艺路线ID
  - CSCHEDULE_QTY decimal? 已排产数量
  - CSEQ int? 工单批次中的顺序
  - CSO_DTL_ID string 销售单明细ID
  - CSOURCE_ID string 来源ID
  - CSOURCE_ORDER_NO string 来源工单编号
  - CSTATUS int? 工单状态
  - CTYPE_ID long? 工单类型ID
  - CUST_CODE string 客户代码
  - CWC_ID long? 工作中心ID
- 关联关系：
  - TBL_MO.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_MO.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_MO.CWC_ID = TBL_BD_WC.CID

----------------------
154. TBL_MO_FAKE（虚拟工单表）
- 业务含义：虚拟工单表，用于特殊场景（如无工单生产）。
- 字段列表：
  - CID long 主键ID
  - CACTULA_END_TIME DateTime? 实际完成时间
  - CACTULA_START_TIME DateTime? 实际生产时间
  - CCOMPLETED_QTY decimal? 完工数量
  - CCUST_ORDER string 客户订单
  - CIS_ACTIVITY string 是否激活
  - CIS_MANUAL string 是否手工创建
  - CITEM_ID long? 物料ID
  - CLEVEL int? 级别
  - CMO_LOT string 工单批次
  - CORDER_DATETIME DateTime? 工单日期
  - CORDER_NO string 工单编号
  - CPARENT_ID string 父级工单编号
  - CPLAN_END_TIME DateTime? 预计完成时间
  - CPLAN_QTY decimal? 计划数量
  - CPLAN_START_TIME DateTime? 预计生产时间
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CROUTE_ID long? 工艺路线ID
  - CSCHEDULE_QTY decimal? 已排产数量
  - CSEQ int? 工单批次中的顺序
  - CSO_DTL_ID string 销售单明细ID
  - CSOURCE_ID string 来源ID
  - CSOURCE_ORDER_NO string 来源工单编号
  - CSTATUS int? 工单状态
  - CTYPE_ID long? 工单类型ID
  - CUST_CODE string 客户代码
  - CWC_ID long? 工作中心ID

----------------------
155. TBL_MO_OUTS（外协工单信息表）
- 业务含义：外协工单信息表，记录外协订单关联。
- 字段列表：
  - CID long 主键ID
  - CITEM_NO string 料号
  - CMO_LOT string 工单批次
  - COS_NO string 外协订单号
  - CQTY int 数量
  - CSO_NO string 销售订单号

----------------------
156. TBL_SFC_DBFC_USER（叠板防错用户）
- 业务含义：叠板防错功能授权用户表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_NO string 设备编码
  - CUSER_NAME string 用户账号

----------------------
157. TBL_SFC_PACKAGE（包装信息表）
- 业务含义：成品/半成品包装信息主表。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CBATCH_NUMBER string 批次号
  - CCUSTOMER_CODE string 客户编码
  - CCUSTOMER_ITEM_NAME string 客户品名
  - CCUSTOMER_ITEM_NO string 客户料号
  - CCYCLE string 周期
  - CINVENTORY_STATUS int? 库存状态
  - CIS_REPRINT string 是否补打
  - CITEM_ID long? 物料ID
  - CLEVEL int? 包装层级
  - CLOCATION_ID long? 货位ID
  - CMO_ID string 工单ID
  - CMO_LOT string 工单批次
  - CNET_WEIGHT decimal? 净重
  - CORDER_ID long? 订单ID
  - CORDER_NO string 订单号
  - CPACKING_TIME DateTime? 包装时间
  - CPARAM_VALUE string 参数值
  - CPARENT_ID long? 父级包装ID
  - CQTY decimal? 数量
  - CREMARK string 备注
  - CSALES_ORDER string 销售订单
  - CSET_PCS_QTY int? SET开板数
  - CSET_X_QTY int? SET叉板数
  - CSOURCE_BARCODE string 补打前的箱号
  - CSPLIT_DATETIME DateTime? 拆分时间
  - CSPLIT_ID long? 上级条码ID
  - CSTATUS string 状态
  - CWEIGHT decimal? 毛重
  - CX_QTY string 叉板数
  - EXPAND1 string 扩展字段1
  - ScrapDateTime string 报废时间
  - ScrapUser string 报废人
  - XOUT string 叉板值
- 关联关系：
  - TBL_SFC_PACKAGE.CITEM_ID = TBL_BD_ITEM.CID

----------------------
158. TBL_SFC_PACKAGE_LABEL_LINK（包装模板与物料/客户关联表）
- 业务含义：包装模板与物料/客户的关联配置。
- 字段列表：
  - CID long 主键ID
  - CCUSTOMER_ID long? 客户ID
  - CITEM_ID long? 物料ID
  - CREMARK string 备注
  - CTEMPLATE_ID long 模板ID

----------------------
159. TBL_SFC_PACKAGE_LOG（包装操作日志表）
- 业务含义：包装操作日志记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - COPERATE_TYPE int? 操作类型
  - CREMARK string 备注

----------------------
160. TBL_SFC_PACKAGE_RULE（包装规则主表）
- 业务含义：包装规则配置主表。
- 字段列表：
  - CID long 主键ID
  - CBOX_TYPE string 箱型
  - CBOX_WEIGHT decimal? 箱重
  - CDEVIATION decimal? 重量偏差
  - CFAIL_RULE int? 失败处理规则
  - CHEIGHT decimal? 高度
  - CIS_MULTI_CYCLE string 是否允许多周期混装
  - CIS_MULTI_ITEM string 是否允许多料号混装
  - CIS_MULTI_LOT string 是否允许多批次混装
  - CIS_MULTI_ORDER string 是否允许多工单混装
  - CIS_MULTI_X string 是否允许多叉板值混装
  - CLEN decimal? 长度
  - CMAX_QTY decimal? 最大装箱数量
  - CMIN_QTY decimal? 最小装箱数量
  - CPKG_WEIGHT decimal? 包装重量
  - CREMARK string 备注
  - CRULE_NAME string 规则名称
  - CRULE_TYPE int 规则类型
  - CTOTAL_WEIGHT decimal? 总重量
  - CWIDTH decimal? 宽度

----------------------
161. TBL_SFC_PACKAGE_RULE_EXT（包装规则扩展配置表）
- 业务含义：包装规则扩展属性配置。
- 字段列表：
  - CID long 主键ID
  - CEXTEND_1 string 板间隔纸
  - CEXTEND_10 string 有无工艺边
  - CEXTEND_11 string 有无RoHS
  - CEXTEND_12 string 纸箱要求
  - CEXTEND_13 string 填充方式
  - CEXTEND_14 string 每箱重量
  - CEXTEND_15 string 特别要求
  - CEXTEND_16 string 封箱方式
  - CEXTEND_17 string 打带方式
  - CEXTEND_18 string 外箱标签
  - CEXTEND_19 string 外箱其他标识
  - CEXTEND_2 string 上下垫板
  - CEXTEND_20 string 其他特别要求
  - CEXTEND_21 string 有无卤素
  - CEXTEND_22 string 有无HF
  - CEXTEND_23 string 有无工艺边
  - CEXTEND_24 string 有无RoHS
  - CEXTEND_3 string 干燥剂
  - CEXTEND_4 string 湿度卡
  - CEXTEND_5 string 包装方式
  - CEXTEND_6 string 小包标签
  - CEXTEND_7 string 其他特别要求
  - CEXTEND_8 string 有无卤素
  - CEXTEND_9 string 有无HF
  - CIMAGE_DATA string 图片
  - CPACKAGE_RULE_ID long 主表ID
- 关联关系：
  - TBL_SFC_PACKAGE_RULE_EXT.CPACKAGE_RULE_ID = TBL_SFC_PACKAGE_RULE.CID

----------------------
162. TBL_SFC_PACKAGE_RULE_LINK（包装规则与物料/客户关联表）
- 业务含义：包装规则与物料/客户关联配置。
- 字段列表：
  - CID long 主键ID
  - CCUSTOMER_ID long? 客户ID
  - CITEM_ID long? 物料ID
  - CPACKAGE_RULE_ID long? 包装规则ID
  - CREMARK string 备注

----------------------
163. TBL_SFC_RECIPE_LOT（按工单批次的配方申请主表）
- 业务含义：按工单批次申请的配方记录主表。
- 字段列表：
  - CID long 主键ID
  - CAPPLY_NO string 申请编号
  - CAUDIT_DESC string 审核说明
  - CAUDIT_TIME DateTime? 审核时间
  - CAUDIT_USER string 审核人
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CENTERPRISE_CODE long? 企业代码
  - CINSTANCE_ID string 实例ID
  - CITEM_NAME string 料号名称
  - CMO_LOT string 工单批次
  - CORDER_NO string 订单号
  - CORG_CODE long? 组织代码
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CROWREMARK string 行备注
  - CSTATE string 状态标识
  - CSTATUS int? 审核状态
  - CSU_ID long? 提交用户ID
  - CSU_R_ID long? 申请单关联ID
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
  - CVERSION int? 版本

----------------------
164. TBL_SFC_RECIPE_LOT_LINK（工单批次配方项目明细表）
- 业务含义：工单批次配方的具体项目明细。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CENTERPRISE_CODE long? 企业代码
  - CEXPRESSION string 校验表达式
  - CINSTANCE_ID string 实例ID
  - CMAX_TOLERANCE decimal? 最大公差
  - CMAX_VALUE decimal? 最大值
  - CMIN_TOLERANCE decimal? 最小公差
  - CMIN_VALUE decimal? 最小值
  - CORG_CODE long? 组织代码
  - CR_LOT_ID long 配方批次主表ID
  - CREAL_VALUE string 实际值
  - CREMARK string 备注
  - CRI_DATA_TYPE string 数据类型
  - CRI_DATA_UNIT string 数据单位
  - CRI_DESC string 配方项描述
  - CRI_ID long? 配方项ID
  - CRI_NAME string 配方项名称
  - CRI_NO string 配方项编码
  - CRI_TYPE int? 项目类型
  - CROWREMARK string 行备注
  - CSEQ int? 排序号
  - CSTANDARD_VALUE string 标准值
  - CSTATE string 状态标识
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
  - CVALUE_TYPE int? 值类型
- 关联关系：
  - TBL_SFC_RECIPE_LOT_LINK.CR_LOT_ID = TBL_SFC_RECIPE_LOT.CID

----------------------
165. TBL_SFC_RECIPE_PRODUCT（按产品维度的配方申请主表）
- 业务含义：按产品物料维度申请的配方记录主表。
- 字段列表：
  - CID long 主键ID
  - CAUDIT_DESC string 审核说明
  - CAUDIT_TIME DateTime? 审核时间
  - CAUDIT_USER string 审核人
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CDD_TYPE string 打点类型
  - CENTERPRISE_CODE long? 企业代码
  - CINSTANCE_ID string 实例ID
  - CITEM_ID long 物料ID
  - CORG_CODE long? 组织代码
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CROWREMARK string 行备注
  - CSTATE string 状态标识
  - CSTATUS int? 审核状态
  - CSU_ID long 提交用户ID
  - CSU_R_ID long 申请单关联ID
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
  - CVERSION int? 版本
- 关联关系：
  - TBL_SFC_RECIPE_PRODUCT.CITEM_ID = TBL_BD_ITEM.CID

----------------------
166. TBL_SFC_RECIPE_PRODUCT_LINK（产品配方项目明细表）
- 业务含义：产品配方的具体项目明细。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 创建时间
  - CDATETIME_MODIFIED DateTime? 修改时间
  - CENTERPRISE_CODE long? 企业代码
  - CEXPRESSION string 校验表达式
  - CINSTANCE_ID string 实例ID
  - CMAX_TOLERANCE decimal? 最大公差
  - CMAX_VALUE decimal? 最大值
  - CMIN_TOLERANCE decimal? 最小公差
  - CMIN_VALUE decimal? 最小值
  - CORG_CODE long? 组织代码
  - CR_PRODUCT_ID long 产品配方主表ID
  - CREAL_VALUE string 实际值
  - CREMARK string 备注
  - CRI_DATA_TYPE string 数据类型
  - CRI_DATA_UNIT string 数据单位
  - CRI_DESC string 配方项描述
  - CRI_ID long? 配方项ID
  - CRI_NAME string 配方项名称
  - CRI_NO string 配方项编码
  - CRI_TYPE int? 项目类型
  - CROWREMARK string 行备注
  - CSEQ int? 排序号
  - CSTANDARD_VALUE string 标准值
  - CSTATE string 状态标识
  - CUSER_CREATED string 创建用户
  - CUSER_MODIFIED string 修改用户
  - CVALUE_TYPE int? 值类型
- 关联关系：
  - TBL_SFC_RECIPE_PRODUCT_LINK.CR_PRODUCT_ID = TBL_SFC_RECIPE_PRODUCT.CID

----------------------
167. TBL_OUTSOURCE_SHIFT_EMPLOYEE（外协班次员工配置表）
- 业务含义：外协工厂班次与员工配置表。
- 字段列表：
  - ID int 主键ID
  - CREATED_TIME string 创建时间
  - CWC_ID long 工作中心ID
  - SHIFT_CODE string 班次编码
  - UPDATED_TIME string 更新时间
  - USER_ID long 员工用户ID

---
九、仓储管理

----------------------
168. TBL_WMS_ITEM_BARCODE（物料条码表）
- 业务含义：物料条码主表，存储库存条码及数量信息。
- 字段列表：
  - CID long 主键ID
  - CBALANCE_QTY decimal? 剩余数量
  - CBARCODE string 条码
  - CBARCODE_TYPE string 条码类型
  - CCYCLE string 周期
  - CEFFECTIVE_STATUS int? 是否超期
  - CERP_LOT_NO string ERP批次号
  - CEXPIRATION_TIME DateTime? 有效日期
  - CITEM_ID long? 物料ID
  - CLOCATION_ID long? 货位ID
  - CLOSS_QTY decimal? 调整数量
  - CLOT_NO string 批次号
  - CPACKING_DATETIME DateTime? 包箱时间
  - CPACKING_ID long? 包装条码ID
  - CPI_DTL_ID long? 入库明细ID
  - CPLAIN_CODE string 料盘编码
  - CPRINT_TIMES int? 打印次数
  - CPRODUCTION_DATETIME DateTime? 生产时间
  - CQTY decimal? 条码数量
  - CREMARK string 备注
  - CSCRAP_TIME DateTime? 条码报废时间
  - CSO_NO string 销售订单
  - CSOURCE_ID long? 来源ID
  - CSPLIT_DATETIME DateTime? 拆分时间
  - CSPLIT_ID long 上级条码ID
  - CSRC_ID long? 来源记录ID
  - CSRC_TYPE string 来源类型
  - CSTATUS string 条码状态
  - CSTORAGE_TIME DateTime? 入库日期
  - CSUPPLIER_ID long? 供应商ID
  - CSUPPLIER_LOT_NO string 供应商批号
  - CUNIT string 单位
  - CUSE_QTY decimal? 使用数量
- 关联关系：
  - TBL_WMS_ITEM_BARCODE.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_ITEM_BARCODE.CLOCATION_ID = TBL_WMS_LOCATION.CID

----------------------
169. TBL_WMS_ITEM_PACKING_BARCODE（物料包装条码表）
- 业务含义：物料包装层级条码关联表。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 包装条码
  - CPARENT_ID long 上级包装ID
  - CREMARK string 备注
  - CSOURCE_ID string 来源ID
  - CSTATUS string 状态

----------------------
170. TBL_WMS_LINE_BARCODE_RECORD（线边仓条码出入记录表）
- 业务含义：线边仓条码出入库操作记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE_ID long? 条码ID
  - CIN_TIME DateTime? 入仓时间
  - CIN_USER string 入仓人
  - CLOCATION_SN string 货位条码
  - COUT_QTY int? 已出仓数量
  - COUT_TIME DateTime? 出仓时间
  - COUT_USER string 出仓人
  - CQTY int? 数量
  - CREMARK string 备注
  - CSTATUS int? 状态
  - CWAREHOUSE_ID long? 仓库ID

----------------------
171. TBL_WMS_LINE_RECORD（线别仓操作记录）
- 业务含义：线别仓操作记录表。
- 字段列表：
  - CID long 主键ID
  - CATTRIBUTE string 属性
  - CIN_TIME DateTime? 入仓时间
  - CIN_USER string 入仓人
  - CITEM_NAME string 产品
  - CLOCATION_SN string 货位条码
  - CORDER_NO string 工单
  - COUT_QTY int? 已出仓数量
  - COUT_TIME DateTime? 出仓时间
  - COUT_USER string 出仓人
  - CPROCESS string 工艺
  - CQTY int? 数量
  - CREMARK string 备注
  - CSTATUS int 状态
  - CTG_VALUE string TG值
  - CWAREHOUSE_ID long 中转仓ID

----------------------
172. TBL_WMS_LOCATION（仓库货位）
- 业务含义：仓库货位主数据表。
- 字段列表：
  - CID long 主键ID
  - CAREA_ID long? 库区ID
  - CLOCATION_CODE string 货位编码
  - CLOCATION_NAME string 货位名称
  - CLOCATION_SN string 货位条码
  - CMAX_CAPACITY decimal? 最大容量
  - CMAX_WEIGHT decimal? 最大重量
  - CPACKING_SEQ int? 拣货顺序
  - CREMARK string 备注
  - CSHELVES_CODE string 货架编码
  - CSHELVES_NAME string 货架名称
  - CSOURCE_ID string 来源ID
  - CTYPE string 货位类型
  - CWAREHOUSE_ID long? 仓库ID
- 关联关系：
  - TBL_WMS_LOCATION.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------
173. TBL_WMS_MANTISSA_RECORD（尾数仓操作记录）
- 业务含义：尾数仓操作记录表。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CCYCLE string 周期
  - CIN_TIME DateTime? 入仓时间
  - CIN_USER string 入仓人
  - CITEM_NAME string 产品
  - CLOCATION_SN string 货位条码
  - COUT_QTY int? 已出仓数量
  - COUT_TIME DateTime? 出仓时间
  - COUT_USER string 出仓人
  - CQTY int? 数量
  - CREMARK string 备注
  - CSTATUS int 状态
  - CWAREHOUSE_ID long 尾数仓ID

----------------------
174. TBL_WMS_PACKAGE_IN_RECORDS（入库记录表）
- 业务含义：成品/物料入库记录主表。
- 字段列表：
  - CID long 主键ID
  - CBOX_QTY int? 箱数
  - CDEF_QTY int? 叉板数
  - CIFMIX string 是否叉板混箱
  - CITEM_NO string 料号
  - CITEM_VERSION string 料号版本
  - CLOCATION_CODE string 货位编码
  - CP_IN_CODE string 入库单号
  - CPACK_QTY int? 每箱包装数量
  - CPCS_QTY int? 总数
  - CQUALITY_QTY int? 正品数
  - CWAREHOUSE_CODE string 仓库编码

----------------------
175. TBL_WMS_PACKAGE_IN_RECORDS_BOXES（入库记录外箱详情表）
- 业务含义：入库记录外箱明细表。
- 字段列表：
  - CID long 主键ID
  - CBOX_CODE string 外箱条码
  - CDATE_CODE string 日期码
  - CPCS_QTY int? 箱内PCS数量
  - CRECORD_ID long? 入库记录主表ID
  - CSCRAP_QTY int? 报废数量
  - CTYPE int? 明细类型
  - CX_OUT string 外箱扩展标识
- 关联关系：
  - TBL_WMS_PACKAGE_IN_RECORDS_BOXES.CRECORD_ID = TBL_WMS_PACKAGE_IN_RECORDS.CID

----------------------
176. TBL_WMS_PICKING_LOG（领料记录）
- 业务含义：领料记录主表。
- 字段列表：
  - CID long 主键ID
  - CPICKING_CODE string 领料单号
  - CPICKING_QTY decimal? 领料数量
  - CREMARK string 备注
  - CUSER_NAME string 领料人

----------------------
177. TBL_WMS_PICKING_LOG_DTL（领料记录明细）
- 业务含义：领料记录明细表。
- 字段列表：
  - CID long 主键ID
  - CBARCODE_ID long? 条码ID
  - CPICKING_ID long? 领料主表ID
  - CQTY decimal? 领料数量
  - CREMARK string 备注
- 关联关系：
  - TBL_WMS_PICKING_LOG_DTL.CPICKING_ID = TBL_WMS_PICKING_LOG.CID

----------------------
178. TBL_WMS_WAREHOUSE（仓库主数据表）
- 业务含义：仓库主数据表。
- 字段列表：
  - CID long 主键ID
  - CDEPARTMENT_CODE string 部门编码
  - CIS_BATCH string 是否批号
  - CIS_POSITION string 是否货位
  - CIS_PRINT string 是否打条码
  - CPERSON_ID string 管理员ID
  - CREMARK string 备注
  - CSOURCE_ID string 来源ID
  - CWAREHOUSE_ADDRESS string 地址
  - CWAREHOUSE_CODE string 仓库编码
  - CWAREHOUSE_NAME string 仓库名称
  - CWAREHOUSE_TYPE_ID long 仓库分类ID
- 关联关系：
  - TBL_WMS_WAREHOUSE.CWAREHOUSE_TYPE_ID = TBL_WMS_WAREHOUSE_TYPE.CID

----------------------
179. TBL_WMS_WAREHOUSE_TYPE（仓库类型）
- 业务含义：仓库类型定义表。
- 字段列表：
  - CID long 主键ID
  - CIS_BATCH_CTRL string 是否批号
  - CIS_CHECK string 是否检验
  - CIS_LOCATION_CTRL string 是否货位
  - CIS_PRINT string 是否打条码
  - CREMARK string 备注
  - CSOURCE_ID string 来源ID
  - CWAREHOUSE_TYPE_CODE string 类别代码
  - CWAREHOUSE_TYPE_NAME string 类别名称
  - CWAREHOUSE_TYPE_PROPERTY string 仓库属性

----------------------
180. TBL_WMS_AREA（仓库区域）
- 业务含义：仓库区域定义表。
- 字段列表：
  - CID long 主键ID
  - CAREA_CODE string 区域代码
  - CAREA_DESC string 区域描述
  - CAREA_NAME string 区域名称
  - CPERSON_ID string 区域管理员ID
  - CREMARK string 备注
  - CSOURCE_ID string 来源ID
  - CWAREHOUSE_ID long? 仓库ID
- 关联关系：
  - TBL_WMS_AREA.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------
181. TBL_WMS_BARCODE_SPLIT_RECORD（条码拆分记录表）
- 业务含义：条码拆分操作记录。
- 字段列表：
  - CID long 主键ID
  - CREMARK string 备注
  - CSOURCE_BARCODE_ID long? 来源条码ID
  - CSPLIT_QTY decimal? 拆分数量
  - CSPLIT_TIME DateTime? 拆分时间
  - CSPLIT_USER string 拆分人
  - CTARGET_BARCODE_ID long? 目标条码ID

----------------------
182. TBL_WMS_ITEM_BARCODE_HISTORY（物料条码操作历史表）
- 业务含义：物料条码操作历史记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码编码
  - CBARCODE_STATUS string 条码状态
  - CQTY object 数量
  - CREMARK string 备注

----------------------
183. TBL_WMS_ITEM_LOCATION（物料默认货位）
- 业务含义：物料默认货位配置表。
- 字段列表：
  - CID long 主键ID
  - CITEM_ID long 物料ID
  - CLOCATION_ID long 货位ID
- 关联关系：
  - TBL_WMS_ITEM_LOCATION.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_ITEM_LOCATION.CLOCATION_ID = TBL_WMS_LOCATION.CID

----------------------
184. TBL_WMS_ITEM_TEMPLATE（物料标签绑定表）
- 业务含义：物料与标签模板绑定关系。
- 字段列表：
  - CID long 主键ID
  - CITEM_ID long? 物料ID
  - CITEM_TYPE_ID long? 物料类型ID
  - MINTEMPLATEID long? 最小包装模板ID
  - PACKTEMPLATEID long? 包装箱模板ID

----------------------
185. TBL_WMS_MI（备料单主表）
- 业务含义：备料单主表，记录生产备料需求。
- 字段列表：
  - CID long 主键ID
  - CDEPARTMENT_CODE string 部门编码
  - CDEPARTMENT_ID string 生产部门ID
  - CMI_DATETIME DateTime? 备料单日期
  - CMI_NO string 单号
  - CMI_TYPE string 备料来源单类型
  - CMITEM_USER string 物料员
  - CMO string 生产工单号
  - CMO_ID string 生产工单ID
  - CREMARK string 备注
  - CSOURCE_BILL_ID string 来源ID
  - CSOURCE_BILL_NO string 来源单号
  - CSOURCE_BILL_TYPE string 来源单源类型
  - CSTATUS string 状态
  - CWAREHOUSE_ID long 仓库ID
  - CWC_ID long? 线体Id
- 关联关系：
  - TBL_WMS_MI.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------
186. TBL_WMS_MI_BARCODE（备料条码表）
- 业务含义：备料单关联条码记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CMI_DTL_ID long 备料单明细ID
  - CQTY decimal 条码发料数量

----------------------
187. TBL_WMS_MI_DTL（备料单子表）
- 业务含义：备料单明细表，记录备料物料及数量。
- 字段列表：
  - CID long 主键ID
  - CITEM_ID long 物料ID
  - CLOCATION_ID long 货位ID
  - CLOSS_RATE decimal? 生产损耗率
  - CMI_ID long 主表ID
  - CMO_QTY decimal? 工单标准用量
  - CQTY decimal? 应发数量
  - CREMARK string 备注
  - CRETURN_QTY decimal? 退料数量
  - CSEND_QTY decimal? 累计发料数量
  - CSOURCE_BILL_ID string 来源ID
  - CSOURCE_BILL_NO string 来源单号
  - CSOURCE_BILL_ROW int? 来源单行
  - CSOURCE_BILL_TYPE string 来源单源类型
  - CSTATION_CODE string 工站编码
  - CSTATUS string 状态
  - CUNIT string 单位
  - CWP_CODE string 工序编码
- 关联关系：
  - TBL_WMS_MI_DTL.CMI_ID = TBL_WMS_MI.CID
  - TBL_WMS_MI_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------
188. TBL_WMS_PI（出入库主表）
- 业务含义：出入库单据主表。
- 字段列表：
  - CID long 主键ID
  - CBILL_SOURCE string 单据来源
  - CBILL_TYPE string 单据类型
  - CCUSTOMER_CODE string 客户编码
  - CDEPT_CODE string 部门编码
  - CERP_STATUS int? ERP接口状态
  - COPERATE_TYPE int 操作类型
  - CPI_DATETIME DateTime? 业务日期
  - CPI_NO string 单号
  - CRB_FLAG int? 红蓝标识
  - CREMARK string 备注
  - CSALESMAN_CODE string 业务员编码
  - CSOURCE_ID string 来源ID
  - CSR_FLAG int? 收发标志
  - CSUPPLIER_ID long? 供应商ID
  - CWAREHOUSE_ID long? 仓库ID
  - CWAREHOUSE_USER string 仓管员
- 关联关系：
  - TBL_WMS_PI.CWAREHOUSE_ID = TBL_WMS_WAREHOUSE.CID

----------------------
189. TBL_WMS_PI_BARCODE（出入库条码表）
- 业务含义：出入库单据关联条码记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CPI_DTL_ID long 出入库子表ID
  - CQTY decimal? 条码数量
  - CSTATUS int? 状态
- 关联关系：
  - TBL_WMS_PI_BARCODE.CPI_DTL_ID = TBL_WMS_PI_DTL.CID

----------------------
190. TBL_WMS_PI_DTL（出入库明细表）
- 业务含义：出入库单据明细表。
- 字段列表：
  - CID long 主键ID
  - CBATCH_NO string 批号
  - CCYCLE string 周期
  - CDETAILS string 明细
  - CERP_STATUS int? ERP接口状态
  - CITEM_ID long? 物料ID
  - CLOCATION_ID long? 货位ID
  - CMO string 生产工单号
  - CNUMBER int? 实际出入库件数
  - CPI_ID long 出入库主表ID
  - CPO string 采购订单号
  - CQTY decimal? 实际出入库数量
  - CRB_FLAG int? 红蓝标识
  - CREMARK string 备注
  - CSALE_NO string 销售订单号
  - CSOURCE_BILL_ID long 来源单ID
  - CSOURCE_BILL_NO string 来源单单号
  - CSOURCE_BILL_TYPE string 来源单类型
  - CSOURCE_ID string 来源ID
  - CSTATUS int? 状态
- 关联关系：
  - TBL_WMS_PI_DTL.CPI_ID = TBL_WMS_PI.CID
  - TBL_WMS_PI_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------
191. TBL_WMS_PRINT_LOG（WMS标签打印日志表）
- 业务含义：WMS标签打印日志记录。
- 字段列表：
  - CID long 主键ID
  - lotcode string 批次号
  - materialcode string 物料编码
  - materialname string 物料名称
  - order string 单据号
  - printer string 打印机名称
  - qty int 打印数量

----------------------
192. TBL_WMS_PRODUCT_BARCODE（成品仓条码表）
- 业务含义：成品仓条码库存表。
- 字段列表：
  - CID long 主键ID
  - CBALANCE_QTY decimal? 剩余数量
  - CBARCODE string 条码
  - CBARCODE_TYPE string 条码类型
  - CEXPIRATION_TIME DateTime? 有效日期
  - CITEM_ID long? 物料ID
  - CLOCATION_ID long? 货位ID
  - CLOSS_QTY decimal? 调整数量
  - CLOT_NO string 批次号
  - CPACKING_DATETIME DateTime? 包箱时间
  - CPACKING_ID long? 包装条码ID
  - CPI_DTL_ID long? 入库单明细ID
  - CPRINT_TIMES int? 打印次数
  - CPRODUCTION_DATETIME DateTime? 生产时间
  - CQTY decimal? 条码数量
  - CREMARK string 备注
  - CSCRAP_TIME DateTime? 条码报废时间
  - CSOURCE_ID long? 来源ID
  - CSPLIT_DATETIME DateTime? 拆分时间
  - CSPLIT_ID long? 上级条码ID
  - CSRC_ID long? 来源记录ID
  - CSRC_TYPE string 来源类型
  - CSTATUS string 条码状态
  - CSUPPLIER_ID long? 供应商ID
  - CSUPPLIER_LOT_NO string 供应商批号
  - CUNIT string 单位
  - CUSE_QTY decimal? 使用数量

----------------------
193. TBL_WMS_PS（出货单主表）
- 业务含义：出货单主表，记录销售出库信息。
- 字段列表：
  - CID long 主键ID
  - CCHECK_USER string 检验员编码
  - CCUSTOMER_ID long? 客户ID
  - CDELIVERY_USER string 送货员编码
  - CDEPARTMENT_ID long? 销售部门ID
  - CPS_DATETIME DateTime? 日期
  - CPS_NO string 单号
  - CPS_TYPE string 类型
  - CREMARK string 备注
  - CSALESMAN_CODE string 业务员编码
  - CSOURCE_BILL_ID string 来源ID
  - CSTATUS int? 状态
  - CWAREHOUSE_ID long? 仓库ID
  - CWAREHOUSE_USER string 仓管员编码

----------------------
194. TBL_WMS_PS_BARCODE（出货单条码表）
- 业务含义：出货单关联条码记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CPS_DTL_ID long 出货单子表ID
- 关联关系：
  - TBL_WMS_PS_BARCODE.CPS_DTL_ID = TBL_WMS_PS_DTL.CID

----------------------
195. TBL_WMS_PS_DTL（出货单明细表）
- 业务含义：出货单明细表。
- 字段列表：
  - CID long 主键ID
  - CCUSTOMER_BILL_NO string 客户订单号
  - CCUSTOMER_BILL_ROW string 客户订单行
  - CCUSTOMER_ITEM_CODE string 客户物料编码
  - CITEM_ID long? 物料ID
  - CLOC_ID long? 货位ID
  - CMI_QTY decimal? 备货数量
  - CPS_QTY decimal? 发货数量
  - CPSID long? 主表关联ID
  - CQTY decimal? 订单数量
  - CSALES_BILL_NO string 销售订单号
  - CSALES_BILL_ROW string 销售订单行
  - CSHIPMENTS_QTY decimal? 累计备货数量
  - CSHIPMENTS_SUM_QTY decimal? 累计出货数量
  - CSOURCE_BILL_ID string 来源ID
  - CSTATUS int? 状态
  - CUNIT string 单位
  - REMARK string 备注
- 关联关系：
  - TBL_WMS_PS_DTL.CPSID = TBL_WMS_PS.CID
  - TBL_WMS_PS_DTL.CITEM_ID = TBL_BD_ITEM.CID

----------------------
196. TBL_WMS_SALES_ORDER（销售订单表）
- 业务含义：销售订单主表。
- 字段列表：
  - CID long 主键ID
  - CCUSTOMER_CODE string 客户编码
  - CCUSTOMER_ID string 客户ID
  - CDELIVERY_ADDR string 交货地址
  - CORIG_CUSTOMER string 关联原客户
  - CREMARK string 备注
  - CRESERVE1 DateTime? 预留字段1
  - CRESERVE10 string 预留字段10
  - CRESERVE2 DateTime? 预留字段2
  - CRESERVE3 DateTime? 预留字段3
  - CRESERVE4 string 预留字段4
  - CRESERVE5 string 预留字段5
  - CRESERVE6 string 预留字段6
  - CRESERVE7 string 预留字段7
  - CRESERVE8 string 预留字段8
  - CRESERVE9 string 预留字段9
  - CSALES_DEPT string 销售部门ID
  - CSALES_MAN string 业务员
  - CSO_NO string 订单号
  - CSO_TIME DateTime? 订单日期
  - CSO_TYPE string 订单类型
  - CSOURCE_ID string 来源ID
  - CSTATUS string 状态

----------------------
197. TBL_WMS_STOCK_BARCODE_LINK（ERP库存与打印条码关联表）
- 业务含义：ERP库存记录与打印条码关联。
- 字段列表：
  - CID long 主键ID
  - CBARCODE_ID long 打印条码记录ID
  - CREMARK string 备注
  - CSTOCK_ID long ERP库存记录ID

----------------------
198. TBL_WMS_STOCKTAKING_DTL（盘点单明细表）
- 业务含义：盘点单明细表。
- 字段列表：
  - CID long 主键ID
  - CITEM_ID long 物料ID
  - CLOCATION_ID long 货位ID
  - CLOSS_QTY double 盘亏数量
  - CQTY double 盘点数量
  - CREMARK string 备注
  - CSTOCKTAKING_ID long 主表ID
  - CSURPLUS_QTY double 盘盈数量
  - CWAREHOUSE_ID long 仓库ID
- 关联关系：
  - TBL_WMS_STOCKTAKING_DTL.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_WMS_STOCKTAKING_DTL.CLOCATION_ID = TBL_WMS_LOCATION.CID

---
十、供应链协同

----------------------
199. TBL_SRM_PO（采购单）
- 业务含义：采购订单主表。
- 字段列表：
  - CID long 主键ID
  - CBUSINESS_TYPE string 业务类型
  - CCHANGE_DATETIME DateTime? 变更时间
  - CDEPT_ID string 部门ID
  - CIS_MANUAL string 是否手动录入
  - CPERSON_ID string 采购员ID
  - CPO string 采购单号
  - CPURCHASE_DATE DateTime? 采购日期
  - CPURCHASE_TYPE string 采购方式
  - CREMARK string 备注
  - CREVIEW_DATETIME DateTime? 审核时间
  - CSOURCE_ID string 来源ID
  - CSTATUS string 状态
  - CSUPPLIER_ID Int64? 供应商ID
- 关联关系：
  - TBL_SRM_PO.CSUPPLIER_ID = TBL_BD_SUPPLIER.CID

----------------------
200. TBL_SRM_PO_DELIVERY（采购订单交付表）
- 业务含义：采购订单交付计划表。
- 字段列表：
  - CID long 主键ID
  - CASSIGNED_QTY decimal? 分配数量
  - CBATCH_CODE string 批号
  - CDELIVERED_QTY decimal? 送货数量
  - CGENERATE_BARCODE_QTY decimal? 已打条码数量
  - CIN_STOCK_QTY decimal? 入库数量
  - CITEM_CODE string 物料编码
  - CITEM_ID Int64? 物料ID
  - CITEM_NAME string 物料名称
  - CITEM_SPEC string 物料规格
  - CPO_DETAIL_ID Int64? 采购订单明细ID
  - CQTY decimal? 数量
  - CREMARK string 备注
  - CRETURN_QTY decimal? 退货数量
  - CSOURCE_ID string 来源ID
  - CSTATUS string 状态
  - CSUPPLIER_CONFIRM_DELIVERY_DATE DateTime? 供应商回复交期
  - CSUPPLIER_CONFIRM_REMARK string 供应商备注
  - CUNIT string 单位
- 关联关系：
  - TBL_SRM_PO_DELIVERY.CITEM_ID = TBL_BD_ITEM.CID

----------------------
201. TBL_SRM_PO_DETAIL（采购订单明细）
- 业务含义：采购订单明细表。
- 字段列表：
  - CID long 主键ID
  - CASSIGNED_QTY decimal? 分配数量
  - CBUSINESS_BILL_CODE string 业务单号
  - CCHANGE_DATETIME DateTime? 变更时间
  - CDELIVERED_QTY decimal? 已交货数量
  - CDELIVERY_DATETIME DateTime? 交货日期
  - CGENERATE_BARCODE_QTY decimal? 已打条码数量
  - CIN_STOCK_QTY decimal? 入库数量
  - CITEM_CODE string 物料编码
  - CITEM_ID Int64? 物料ID
  - CITEM_NAME string 物料名称
  - CITEM_SPEC string 物料规格
  - CORIGIN_TYPE string 来源类型
  - CPO_ID Int64? 采购订单ID
  - CQTY decimal? 订单数量
  - CREMARK string 备注
  - CRETURN_QTY decimal? 退货数量
  - CSEQ int? 订单行号
  - CSOURCE_ID string 来源ID
  - CUNIT string 单位
- 关联关系：
  - TBL_SRM_PO_DETAIL.CPO_ID = TBL_SRM_PO.CID
  - TBL_SRM_PO_DETAIL.CITEM_ID = TBL_BD_ITEM.CID

----------------------
202. TBL_SRM_RECEIVING（收货单主表）
- 业务含义：采购收货单主表。
- 字段列表：
  - CID long 主键ID
  - CBATCH_CODE string 批号
  - CBILL_TYPE string 单据类型
  - CBUSINESS_TYPE string 业务类型
  - CPURCHASE_TYPE string 采购类型
  - CRECEIVING_CUSTOMER string 收货客户名称
  - CRECEIVING_DATE DateTime? 收货日期
  - CRECEIVING_DEPT string 收货部门
  - CRECEIVING_NO string 收货单号
  - CRECEIVING_USER string 收货人
  - CREMARK string 备注
  - CSOURCE_ID string 来源ID
  - CSTATUS string 状态
  - CSUPPLIER_ID Int64? 供应商ID
- 关联关系：
  - TBL_SRM_RECEIVING.CSUPPLIER_ID = TBL_BD_SUPPLIER.CID

----------------------
203. TBL_SRM_RECEIVING_BARCODE（收货单条码关联表）
- 业务含义：收货单关联条码记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE string 条码
  - CRECEIVING_DTL_ID Int64? 收货单明细ID
- 关联关系：
  - TBL_SRM_RECEIVING_BARCODE.CRECEIVING_DTL_ID = TBL_SRM_RECEIVING_DTL.CID

----------------------
204. TBL_SRM_RECEIVING_DTL（收货单明细表）
- 业务含义：收货单明细表，记录收货物料及检验结果。
- 字段列表：
  - CID long 主键ID
  - CBATCH_CODE string 批号
  - CDELIVER_QTY decimal? 供应商送货数量
  - CEMERGENCY_LEVEL int? 来料检验紧急程度
  - CGOOD_QTY decimal? 合格数量
  - CINSOTCK_QTY decimal? 入库数量
  - CINSPECT_DATETIME DateTime? 检验时间
  - CINSPECT_RESULT string 检验结果
  - CINSPECT_USER string 检验人
  - CINSTOCK_DATETIME DateTime? 入库时间
  - CITEM_CODE string 物料编码
  - CITEM_ID Int64? 物料ID
  - CITEM_NAME string 物料名称
  - CITEM_SPEC string 物料规格
  - CLOCATION_ID Int64? 货位ID
  - CNG_QTY decimal? 不合格数量
  - CPO string 采购单号
  - CPO_DELIVERY_ID long? 采购单交付ID
  - CPO_DETAIL_ID long? 采购单明细ID
  - CPO_QTY decimal? 采购数量
  - CPO_SEQ int? 采购订单行号
  - CRECEIVING_ID Int64? 收货单ID
  - CRECEIVING_QTY decimal? 收货数量
  - CRETURN_QTY decimal? 退货数量
  - CSEQ int? 收货单行号
  - CSO string 销售单号
  - CSOURCE_ID string 来源ID
  - CSOURCE_NO string 来源单号
  - CSOURCE_TYPE string 来源类型
  - CSTATUS string 状态
  - CUNIT string 单位
  - CWAREHOUSE_ID Int64? 仓库ID
- 关联关系：
  - TBL_SRM_RECEIVING_DTL.CRECEIVING_ID = TBL_SRM_RECEIVING.CID
  - TBL_SRM_RECEIVING_DTL.CITEM_ID = TBL_BD_ITEM.CID

---
十一、物料防错

----------------------
205. TBL_SHEET_LINK_PP（供应商替代关联表）
- 业务含义：供应商替代关系配置表。
- 字段列表：
  - CID long 主键ID
  - CLINK_SUPPLIER_ID long 被关联的供应商ID
  - CREMARK string 备注
  - CSUPPLIER_ID long 供应商ID
  - CSUPPLIER_NAME string 供应商名称

----------------------
206. TBL_ITEM_LINK_SUPPLIER（料号与供应商关联表）
- 业务含义：物料与供应商关联配置表。
- 字段列表：
  - CID long 主键ID
  - CITEM_NO string 被关联的料号
  - CREMARK string 备注
  - CSUPPLIER_ID long 供应商ID
  - CSUPPLIER_NAME string 供应商名称

----------------------
207. TBL_MO_BARCODE_PROD_LINK（工单与条码生产关联表）
- 业务含义：工单与生产条码关联记录。
- 字段列表：
  - CID long 主键ID
  - CBARCODE_ID long? 条码ID
  - CMO_ID long? 工单ID
  - CPROCESS_ID long? 工序ID
  - CREMARK string 备注
  - CSUPPLIER_BARCODE string? 供应商条码

----------------------
208. TBL_PRESTK_RECORD（预叠操作记录表）
- 业务含义：预叠操作记录表。
- 字段列表：
  - CID long 主键ID
  - CLINKED_RECORD_ID long? 关联记录ID
  - CREMARK string 备注
  - CUSER string 操作用户
  - CWO string 工单号

---
十二、SPC

----------------------
209. TBL_SPC_CONTROL_CHARACTERISTIC（SPC管控特性主表）
- 业务含义：SPC统计过程控制特性定义表。
- 字段列表：
  - CID long 主键ID
  - CCALCULATION_METHOD string 计算方法
  - CCHART_TYPE string 控制图类型
  - CCPK double? CPK
  - CCRITIAL_CONTROL string 是否关键控制项
  - CDECIML_PLACES int? 小数位数
  - CMEASURE_INSTRUMENT string 测量仪器
  - CMEASURE_METHOD string 测量方法
  - CMEASURE_REMARK string 测量备注
  - CPROCESS_ID long? 工序ID
  - CREFRENCE_FILE string 参考文件
  - CSAMPLE_COUNT int? 抽样数量
  - CSAMPLING_FREQ int? 抽样频率
  - CSAMPLING_REMARK string 抽样说明
  - CSAMPLING_UNIT string 抽样频率单位
  - CSPECIFICATION_LOW_LIMIT string 规格下限
  - CSPECIFICATION_STANDARD double? 规格中心值
  - CSPECIFICATION_UP_LIMIT string 规格上限
  - CSTATUS int 发布状态
  - CTYPE string 特性类型
  - CUNIT string 单位
  - CVARIABLE_CODE string 特性编码
  - CVARIABLE_NAME string 特性名称
  - CWC_ID long? 工作中心ID
- 关联关系：
  - TBL_SPC_CONTROL_CHARACTERISTIC.CPROCESS_ID = TBL_BD_PROCESS.CID
  - TBL_SPC_CONTROL_CHARACTERISTIC.CWC_ID = TBL_BD_WC.CID

----------------------
210. TBL_SPC_CONTROL_CHARACTERISTIC_ITEM_LINK（SPC管控特性与对象关联表）
- 业务含义：SPC特性与料号/模板关联表。
- 字段列表：
  - CID long 主键ID
  - CDATA_SOURCE string 数据来源
  - CITEM_NO string 料号
  - CTEMP_NO string 模板编号
  - CTYPE string 关联对象类型
  - CVARIABLE_ID long? 管控特性ID
- 关联关系：
  - TBL_SPC_CONTROL_CHARACTERISTIC_ITEM_LINK.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------
211. TBL_SPC_CONTROL_CHARACTERISTIC_LIMIT（SPC管控特性控制限配置表）
- 业务含义：SPC控制图控制限配置表。
- 字段列表：
  - CID long 主键ID
  - CCONTROL_METHOD string 管制方法
  - CLCL_CONTROL_LOW_LIMIT double? 下控制图管制下限
  - CLCL_CONTROL_MIDDLE double? 下控制图管制中线
  - CLCL_CONTROL_UP_LIMIT double? 下控制图管制上限
  - CUCL_CONTROL_LOW_LIMIT double? 上控制图管制下限
  - CUCL_CONTROL_MIDDLE double? 上控制图管制中线
  - CUCL_CONTROL_UP_LIMIT double? 上控制图管制上限
  - CVARIABLE_ID long? 管控特性ID
- 关联关系：
  - TBL_SPC_CONTROL_CHARACTERISTIC_LIMIT.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------
212. TBL_SPC_CONTROL_CHARACTERISTIC_RULE_LINK（SPC管控特性与判异规则关联表）
- 业务含义：SPC特性与判异规则关联表。
- 字段列表：
  - CID long 主键ID
  - CCHART_TYPE int? 图类型
  - CGROUP_ID long? 分组ID
  - CRULE_ID long? 规则ID
  - CVARIABLE_ID long? 管控特性ID
- 关联关系：
  - TBL_SPC_CONTROL_CHARACTERISTIC_RULE_LINK.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------
213. TBL_SPC_DATA_REAL（SPC实时采样数据表）
- 业务含义：SPC实时采样数据记录表。
- 字段列表：
  - CID long 主键ID
  - CCRAFT_AUDIT_MAN string 工艺审核人
  - CCRAFT_AUDIT_STATUS int? 工艺审核状态
  - CCRAFT_AUDIT_TIME DateTime? 工艺审核时间
  - CINPUT_TIME DateTime 录入时间
  - CINPUT_VALUE1 decimal 输入值1
  - CINPUT_VALUE2 decimal 输入值2
  - CINPUT_VALUE3 decimal 输入值3
  - CINPUT_VALUE4 decimal 输入值4
  - CINPUT_VALUE5 decimal 输入值5
  - CINPUT_VALUE6 decimal 输入值6
  - CIPQA_AUDIT_MAN string IPQA审核人
  - CIPQA_AUDIT_STATUS int? IPQA审核状态
  - CIPQA_AUDIT_TIME DateTime? IPQA审核时间
  - CIS_NG string 是否NG
  - CITEM_ID long? 物料ID
  - CITEM_NAME string 物料名称
  - CNG_REASON string NG原因
  - CQA_AUDIT_MAN string 品保审核人
  - CQA_AUDIT_STATUS int? 品保审核状态
  - CQA_AUDIT_TIME DateTime? 品保审核时间
  - CQUALITY_AUDIT_MAN string 品质工程审核人
  - CQUALITY_AUDIT_STATUS int? 品质工程审核状态
  - CQUALITY_AUDIT_TIME DateTime? 品质工程审核时间
  - CREASON_ANALYSIS string 原因分析
  - CREDRESS_MEASURE string 纠正措施
  - CSOURCE long? 数据来源
  - CTEMP_NAME string 模板名称
  - CTYPE int 图类型
  - CVALUE decimal 统计值
  - CVARIABLE_ID long 管控特性ID
- 关联关系：
  - TBL_SPC_DATA_REAL.CVARIABLE_ID = TBL_SPC_CONTROL_CHARACTERISTIC.CID

----------------------
214. TBL_SPC_RULE_OF_DISSENT（SPC判异规则定义表）
- 业务含义：SPC判异规则定义表。
- 字段列表：
  - CID long 主键ID
  - CCOUNT string 判异次数/数量条件
  - CDESC string 规则描述
  - CTYPE int 规则类型

---
十三、出货报告

----------------------
215. TBL_OQC_SHIPMENT_GENERATE（出货报告生成）
- 业务含义：出货报告生成记录主表。
- 字段列表：
  - CID long 主键ID
  - CFILES string 生成文件信息
  - CGENERATE_QTY int 生成次数
  - CGENERATE_REASON string 生成原因
  - CGENERATE_TIME DateTime 生成时间
  - CGENERATE_USER string 生成人
  - CITEM_NO string 型号
  - CLOG_ID long 生成记录ID
  - CPARAMS string 生成参数
  - CPERIOD string 周期
  - CREPORT_CODE string 报告编号
  - CREPORT_ID long 报告ID
  - CREPORT_NAME string 报告名称
  - CSO_NO string 订单号

----------------------
216. TBL_OQC_SHIPMENT_GENERATE_LOG（出货报告生成记录）
- 业务含义：出货报告生成历史版本记录。
- 字段列表：
  - CID long 主键ID
  - CAUDIT_REMARK string 审核备注
  - CAUDIT_STATUS Enum_AuditStatus 审核结果
  - CAUDIT_TIME DateTime? 确认时间
  - CAUDIT_USER string 确认人
  - CFILES string 生成文件信息
  - CFILES_OLD string 旧版本生成文件信息
  - CGENERATE_ID long 报告生成ID
  - CGENERATE_QTY int 生成次数
  - CGENERATE_REASON string 生成原因
  - CGENERATE_TIME DateTime 生成时间
  - CGENERATE_USER string 生成人
  - CIS_NEW bool 是否最新
  - CITEM_NO string 型号
  - CPARAMS string 生成参数
  - CPARAMS_OLD string 旧版本生成参数
  - CPERIOD string 周期
  - CREPORT_CODE string 报告编号
  - CREPORT_ID long 报告ID
  - CREPORT_NAME string 报告名称
  - CSO_NO string 订单号

----------------------
217. TBL_OQC_SHIPMENT_ITEM_LINK（出货报告料号关联表）
- 业务含义：出货报告与料号关联表。
- 字段列表：
  - CID long 主键ID
  - CITEM_ID long? 物料ID
  - CREPORT_ID long 报告ID
  - CSEQ int 排序
- 关联关系：
  - TBL_OQC_SHIPMENT_ITEM_LINK.CITEM_ID = TBL_BD_ITEM.CID

----------------------
218. TBL_OQC_SHIPMENT_REPORT（出货报告表）
- 业务含义：出货报告定义主表。
- 字段列表：
  - CID long 主键ID
  - CCODE string 报告编号
  - CDESC string 描述
  - CNAME string 报告名称
  - CTYPE_ID long? 报告类型ID

----------------------
219. TBL_OQC_SHIPMENT_REPORT_TYPE（出货报告类型表）
- 业务含义：出货报告类型定义表。
- 字段列表：
  - CID long 主键ID
  - CTYPE_CODE string 类型编码
  - CTYPE_DESC string 类型描述
  - CTYPE_NAME string 类型名称

----------------------
220. TBL_OQC_SHIPMENT_TEMPLATE_LINK（出货报告模板关联表）
- 业务含义：出货报告与模板关联表。
- 字段列表：
  - CID long 主键ID
  - CREPORT_ID long 报告ID
  - CSEQ int 排序
  - CTEMPLATE_ID long 模板ID

---
十四、锁机锁卡

----------------------
221. TBL_PM_ITEM_LINK_TAG（点检项目与测点关联表）
- 业务含义：点检项目与设备测点关联配置。
- 字段列表：
  - CID long 主键ID
  - CPM_ITEM_ID long 被关联的点检项目ID
  - CPM_TEMPLATE_WC_LINK_ID long? 点检模板工作中心关联ID
  - CREMARK string 测点服务器地址
  - CTAG_ID long 测点ID
  - CTAG_NAME string 测点名称
  - CTAG_PATH string 测点路径

----------------------
222. TBL_PM_TEMPLATE_LINK_DEVICE（模板与工作中心关联采集设备）
- 业务含义：点检模板与采集设备关联表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID long? 设备ID
  - CDEVICE_NAME string 设备名称
  - CDEVICE_NO string 设备编号
  - CPM_TEMPLATE_ID long? 被关联的点检模板ID
  - CPM_TEMPLATE_WC_LINK_ID long? 模板工作中心关联ID
  - CREMARK string 服务器地址备注

----------------------
223. TBL_SJSKDATA_YYYYMM（锁机锁卡读码记录表）
- 业务含义：锁机锁卡设备读码记录表（按月分表）。
- 字段列表：
  - CID long 主键ID
  - CDATETIME_CREATED DateTime? 读码时间
  - CITEM_ID string 读码料号
  - CLOT_ID string 工单号
  - EQPID string 设备ID
  - PANEL_LOT string 面板批次

----------------------
224. TBL_SJSKEQPINFO（读码设备实时工单信息表）
- 业务含义：读码设备当前/下一工单信息表。
- 字段列表：
  - CID long 主键ID
  - CURRENTITEM string 当前料号
  - CURRENTLOT string 当前工单
  - EQPIP string 设备IP
  - EQPNAME string 设备名称
  - NEXTITEM string 下一料号
  - NEXTLOT string 下一工单
  - UpdateTime DateTime? 更新时间

----------------------
225. TBL_EAP_ALARM_CONTROL_LINK（设备报警项关联配置表）
- 业务含义：设备报警项与测点关联配置。
- 字段列表：
  - CID long 主键ID
  - CALARM_NAME string 报警名称
  - CDEVICE_ID int 设备ID
  - CREMARK string 备注
  - CTAG_ID long? 测点ID
- 关联关系：
  - TBL_EAP_ALARM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
226. TBL_EAP_ITEM_CONTROL_LINK（设备关联料号）
- 业务含义：设备可生产物料关联配置。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID int 设备ID
  - CITEM_ID long? 物料ID
  - CREMARK string 备注
- 关联关系：
  - TBL_EAP_ITEM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID
  - TBL_EAP_ITEM_CONTROL_LINK.CITEM_ID = TBL_BD_ITEM.CID

----------------------
227. TBL_EAP_POTION_ITEM_CONTROL_LINK（设备关联药水化验项目）
- 业务含义：设备与药水化验项目关联配置。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID int 设备ID
  - CNP_ITEM_ID long? 化验模板项ID
  - CREMARK string 备注
- 关联关系：
  - TBL_EAP_POTION_ITEM_CONTROL_LINK.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

----------------------
228. TBL_EAP_PRODUCE_CONTROL_DEVICE（生产管控设备配置表）
- 业务含义：生产管控设备开关配置表。
- 字段列表：
  - CID long 主键ID
  - CDEVICE_ID long 设备ID
  - CDEVICE_NAME string 设备名称
  - CEND_CONTROL TimeSpan 管控结束时间
  - CFIRST_CHECK string 首检校验开关
  - CINSPECTION_CHECK string 检验记录校验开关
  - CIS_SET_SCREEN string 是否启用看板/画面设置
  - CPARENT_DEVICE string 上级设备/父设备标识
  - CPOTION_CHECK string 药水化验校验开关
  - CPRODUCE_LOG_CHECK string 生产日志校验开关
  - CREMARK string 备注
  - CSTART_CONTROL TimeSpan 管控开始时间
  - CTIME_CHECK string 时间段校验开关
- 关联关系：
  - TBL_EAP_PRODUCE_CONTROL_DEVICE.CDEVICE_ID = TBL_EAP_DEVICE.CDEVICE_ID

---
十五、其它信息

----------------------
229. TBL_FA_TXDD_KTHD（图形电镀孔铜厚度测量）
- 业务含义：图形电镀孔铜厚度测量数据表。
- 字段列表：
  - CID long 主键ID
  - CCLKJ string 测量孔径
  - CMAIN_ID long 主表ID
  - CT_DATA1 string 测量值1
  - CT_DATA2 string 测量值2
  - CT_DATA3 string 测量值3
  - CT_DATA4 string 测量值4
  - CT_DATA5 string 测量值5
- 关联关系：
  - TBL_FA_TXDD_KTHD.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
230. TBL_FA_TXDD_MAIN（图像电镀FA信息主表）
- 业务含义：图形电镀FA（首件确认）信息主表。
- 字段列表：
  - CID long 主键ID
  - CAGV_CCOPER string 平均铜厚
  - CAUDIT_DESC string 审核描述
  - CAUDIT_STATUS int? 审核状态
  - CAUDIT_TIME DateTime? 审核时间
  - CAUDIT_USER string 审核人
  - CBD_COPPER_THICKNESS string 板底铜厚
  - CCOPPER_THICKNESS string 铜厚
  - CCREATOR string 制作
  - CCS_CCOPER string C/S铜厚
  - CDATE DateTime? 日期
  - CDRILL_BIT string 钻咀规格
  - CDTCSCS_AREA string 镀铜C/S面参数
  - CDTCSCS_ASF string 镀铜C/S面参数
  - CDTDDSJ string 镀铜电镀时间
  - CDTDLMD string 镀铜电流密度
  - CDTSSCS_AREA string 镀铜S/S面参数
  - CDTSSCS_ASF string 镀铜S/S面参数
  - CDXCSCS_AREA string 镀锡C/S面参数
  - CDXCSCS_ASF string 镀锡C/S面参数
  - CDXDDSJ string 镀锡电镀时间
  - CDXDLMD string 镀锡电流密度
  - CDXSSCS_AREA string 镀锡S/S面参数
  - CDXSSCS_ASF string 镀锡S/S面参数
  - CELEC_SIDE string 电镀挂板夹边
  - CELEC_WINDOW string 电镀窗口
  - CIC_TOLERANCE string IC公差
  - CINSPECT_DDCS string 电镀参数：检测人
  - CINSPECT_GBFS string 挂板方式：检测人
  - CINSPECT_KTHD string 孔铜厚度：检测人
  - CINSPECT_QPBT string 切片表铜：检测人
  - CINSPECT_SKKJ string 蚀刻后孔径测量：检测人
  - CINSPECT_SKXK string 蚀刻后线宽：检测人
  - CINSPECT_ZKCS string 阻抗测试：检测人
  - CITEM_NO string 料号
  - CK_CCOPER string K值铜厚
  - CLEN decimal? 长度
  - CLINE string 线别
  - CM_CCOPER string M值铜厚
  - CMIN_LINE_SPACE string 最小线距
  - CMIN_LINE_WIDE string 最小线宽
  - CPLANK_QTY string 挂板数量
  - CRESULT_KTHD string 孔铜厚度：判定结果
  - CRESULT_QPBT string 切片表铜：判定结果
  - CRESULT_SKKJ string 蚀刻后孔径测量：判定结果
  - CRESULT_SKXK string 蚀刻后线宽：判定结果
  - CRESULT_ZKCS string 阻抗测试：判定结果
  - CSAMPLE_QTY int? 抽样数量
  - CSIZE string 尺寸
  - CSS_CCOPER string S/S铜厚
  - CTHICKNESS string 板厚
  - CTIN_THICKNESS string 锡厚
  - CWIDE decimal? 宽度
  - CXK_TOLERANCE string 线宽管控公差

----------------------
231. TBL_FA_TXDD_QPBT（图形电镀切片表铜）
- 业务含义：图形电镀切片表铜测量数据。
- 字段列表：
  - CID long 主键ID
  - CBMTH1 string 表铜厚度1
  - CBMTH2 string 表铜厚度2
  - CBMTH3 string 表铜厚度3
  - CBMTH4 string 表铜厚度4
  - CDXCL1 string 锡层测量1
  - CDXCL2 string 锡层测量2
  - CINSPECT_USER string 检测人
  - CKCCL1 string 孔铜粗糙度1
  - CKCCL2 string 孔铜粗糙度2
  - CKNTHA string 孔内铜厚A
  - CKNTHB string 孔内铜厚B
  - CKNTHC string 孔内铜厚C
  - CKNTHD string 孔内铜厚D
  - CKNTHE string 孔内铜厚E
  - CKNTHF string 孔内铜厚F
  - CMAIN_ID long 主表ID
  - CRESULT string 判定结果
- 关联关系：
  - TBL_FA_TXDD_QPBT.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
232. TBL_FA_TXDD_SKKJ（图形电镀蚀刻后孔径测量）
- 业务含义：图形电镀蚀刻后孔径测量数据。
- 字段列表：
  - CID long 主键ID
  - CDRILL_BIT string 钻咀规格
  - CMAIN_ID long 主表ID
  - CMEASURED string 实测值
  - CPRODUCT string 产品
  - CREMARK string 备注
  - CRESULT string 判定结果
  - CTOLERANCE string 公差
- 关联关系：
  - TBL_FA_TXDD_SKKJ.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
233. TBL_FA_TXDD_SKXK（图形电镀蚀刻后线宽）
- 业务含义：图形电镀蚀刻后线宽/线隙测量数据。
- 字段列表：
  - CID long 主键ID
  - CBGAJX_SC string BGA间隙实测
  - CBGAJX_YQ string BGA间隙要求
  - CBGAKD_SC string BGA孔大实测
  - CBGAKD_YQ string BGA孔大要求
  - CGBDKD_SC string GBD孔大实测
  - CGBDKD_YQ string GBD孔大要求
  - CICJX_SC string IC间隙实测
  - CICJX_YQ string IC间隙要求
  - CICKD_SC string IC孔大实测
  - CICKD_YQ string IC孔大要求
  - CLAYER string 层别
  - CMAIN_ID long 主表ID
  - CZXXK_SC string 阻焊线宽实测
  - CZXXK_YQ string 阻焊线宽要求
  - CZXXX_SC string 阻焊线隙实测
  - CZXXX_YQ string 阻焊线隙要求
- 关联关系：
  - TBL_FA_TXDD_SKXK.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
234. TBL_FA_TXDD_XHCL（图形电镀锡厚测量）
- 业务含义：图形电镀锡厚测量数据。
- 字段列表：
  - CID long 主键ID
  - CMAIN_ID long 主表ID
  - CX_DATA1 string 锡厚数据1
  - CX_DATA2 string 锡厚数据2
  - CX_DATA3 string 锡厚数据3
  - CX_DATA4 string 锡厚数据4
  - CX_DATA5 string 锡厚数据5
- 关联关系：
  - TBL_FA_TXDD_XHCL.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
235. TBL_FA_TXDD_ZKCS（图形电镀阻抗测试）
- 业务含义：图形电镀阻抗测试数据。
- 字段列表：
  - CID long 主键ID
  - CLEVEL string 层别
  - CMAIN_ID long 主表ID
  - CMEASURED string 实测值
  - CREMARK string 备注
  - CRESULT string 判定结果
  - CSTANDARD string 标准值
  - CTOLERANCE string 公差
- 关联关系：
  - TBL_FA_TXDD_ZKCS.CMAIN_ID = TBL_FA_TXDD_MAIN.CID

----------------------
236. TBL_FA_YHYJ_MAIN（压合压机）
- 业务含义：压合压机FA（首件确认）信息主表。
- 字段列表：
  - CID long 主键ID
  - CAUDIT_DESC string 审核描述
  - CAUDIT_PROCESS string 工艺审核
  - CAUDIT_PRODUCE string 生产审核
  - CAUDIT_QUALITY string 品质审核
  - CAUDIT_STATUS int? 审核状态
  - CAUDIT_TIME DateTime? 审核时间
  - CAUDIT_USER string 审核人
  - CCORE_BOARD_THICKNESS string 芯板厚度
  - CCREATOR1 string 制作人1
  - CCREATOR2 string 制作人2
  - CCREATOR3 string 制作人3
  - CDATE DateTime? 日期
  - CERROR string 异常说明
  - CINNER_COPPER_THICK string 内层铜厚
  - CIPQC_SURE1 string IPQC确认1
  - CIPQC_SURE2 string IPQC确认2
  - CIS_BB string 是否爆板
  - CIS_BDZW string 是否板底皱纹
  - CIS_QPZH string 是否起泡折痕
  - CITEM_NO string 料号
  - CPBKS string 排版块数
  - CPP_SUPPLIER string PP供应商
  - CPRESSED_STACKED string 压合叠板方式
  - CRESIDUAL_COPPER_RATE string 残铜率
  - CRESULT string 判定结果
  - CTB_SPEC string 铜箔规格
  - CX_CSCALE string X向涨缩
  - CX_TARGET string X方向靶值汇总
  - CX_TARGET1 string X靶值1
  - CX_TARGET2 string X靶值2
  - CX_TARGET3 string X靶值3
  - CX_TARGET4 string X靶值4
  - CX_TARGET5 string X靶值5
  - CX_TARGET6 string X靶值6
  - CY_CSCALE string Y向涨缩
  - CY_TARGET string Y方向靶值
  - CY_TARGET1 string Y靶值1
  - CY_TARGET2 string Y靶值2
  - CY_TARGET3 string Y靶值3
  - CY_TARGET4 string Y靶值4
  - CY_TARGET5 string Y靶值5
  - CY_TARGET6 string Y靶值6
  - CYB_PROGRAM string 压板程序

----------------------
237. TBL_FA_YHYJ_MI（压合压机MI实测）
- 业务含义：压合压机MI（制造指示）实测数据。
- 字段列表：
  - CID long 主键ID
  - CJZHD_MI string 机组厚度MI值
  - CJZHD_RESULT string 机组厚度判定
  - CMAIN_ID long 主表ID
  - CNCXBHD_MI string 内层芯板厚度MI值
  - CNCXBHD_RESULT string 内层芯板厚度判定
  - CYBHD_MI string 压板厚度MI值
  - CYBHD_RESULT string 压板厚度判定
- 关联关系：
  - TBL_FA_YHYJ_MI.CMAIN_ID = TBL_FA_YHYJ_MAIN.CID

----------------------
238. TBL_MEP_MATERIAL_PARAM（重点物料参数维护）
- 业务含义：重点物料/ NPI物料参数维护表。
- 字段列表：
  - CID long 主键ID
  - CCONFIRMATION_TIME DateTime? 确认时间
  - CCONFIRMED_USER string 确认人
  - CCONTROL_PLANS string 控制计划
  - CDELIVERY_DATE DateTime? 交货日期
  - CENTER_DATE DateTime? 下单日期
  - CGROUP string 需确认组
  - CITEM_ID long 料号ID
  - CNOTES string 资料难点和注意事项
  - CNPI_STATUS string NPI状态
  - CPROCESS_ID long 工序ID
  - CQUANTITY string 数量
  - CREASON string 跟进原因
  - CSTATUS long 状态
  - CTYPE string 类型
- 关联关系：
  - TBL_MEP_MATERIAL_PARAM.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_MEP_MATERIAL_PARAM.CPROCESS_ID = TBL_BD_PROCESS.CID

