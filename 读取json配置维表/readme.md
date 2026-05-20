# 维表映射配置维护说明

本目录用于配置 MES 自然语言查数时的**外键 → 维表 JOIN → 中文列名**规则，供 Dify 工作流注入【维表映射规则】，避免列表里只显示 ID、账号。

---

## 日常只需关心 2 个文件

| 文件 | 是否手改 | 作用 |
|------|----------|------|
| `../中络项目MES 系统数据库表结构V1.1.md` | **要** | 表结构、字段中文名、**关联关系**（权威来源） |
| `mes_dimension_joins.map` | **要** | 维表 JOIN / SELECT 中文别名（表格式，推荐维护入口） |
| `mes_dimension_joins.json` | 不要手改 | 由 `build_dify_bundle.py` 从 `.map` 解析生成 |
| `dify_mes_dimension_node.py` | 不要手改 | 同上，**整段复制到 Dify 代码节点** |

其余为工具脚本，一般不用改：

| 文件 | 作用 |
|------|------|
| `parse_dimension_map.py` | `.map` → JSON 解析器 |
| `mes_dimension_rules.py` | 根据配置生成 Markdown 规则文本 |
| `build_dify_bundle.py` | 同步 JSON + 打包 Dify 单文件节点 |
| `generate_dimension_map_from_schema.py` | 从表结构文档**批量重生成**整个 `.map` |

---

## 加一张新表

### 第 1 步：更新表结构文档

在 `中络项目MES 系统数据库表结构V1.1.md` 中补充新表小节，**关联关系**写全，例如：

```markdown
238. TBL_XXX_NEW（新业务表）
- 业务含义：……
- 字段列表：
  - CITEM_ID long 料号ID
  - CPROCESS_ID long 工序ID
  - CCONFIRMED_USER string 确认人
- 关联关系：
  - TBL_XXX_NEW.CITEM_ID = TBL_BD_ITEM.CID
  - TBL_XXX_NEW.CPROCESS_ID = TBL_BD_PROCESS.CID
```

说明：确认人、创建人等**账号字符串**字段，即使文档未写关联，`generate_dimension_map_from_schema.py` 也会按字段名自动补 `TBL_SYS_USER` 映射。

### 第 2 步：更新映射配置（二选一）

#### 方式 A — 只加一张表（推荐日常）

在 `mes_dimension_joins.map` 末尾**复制**已有类似表（如 `TBL_MEP_MATERIAL_PARAM`），改表名、别名、ON 条件：

```text
[表 TBL_XXX_NEW]
标签=新业务表
关键词=新业务, XXX
别名=x

[映射 item]
字段=CITEM_ID
关联=i | TBL_BD_ITEM | i.CID = x.CITEM_ID
列=i.CITEM_NO | 料号
列=i.CITEM_NAME | 品名

[映射 process]
字段=CPROCESS_ID
关联=p | TBL_BD_PROCESS | p.CID = x.CPROCESS_ID
列=p.CPROCESS_NAME | 工序名称
列=p.CPROCESS_NO | 工序编码

[映射 work_center]
字段=CWC_ID
说明=工作中心两级：父级如开料/钻孔；子级如机台。
关联=wc | TBL_BD_WC | wc.CID = x.CWC_ID
关联=wc_p | TBL_BD_WC | wc_p.CID = wc.CPARENT | 依赖=wc
列=COALESCE(wc_p.CWC_NAME, wc.CWC_NAME) | 工作中心名称
列=wc.CWC_NAME | 机台名称
```

`关键词=` 用于用户问题里出现这些词时，自动选中该事实表。

#### 方式 B — 从文档批量生成（表多或大改文档时）

```bash
cd 读取json配置维表
python3 generate_dimension_map_from_schema.py
```

**注意**：会**覆盖**整个 `mes_dimension_joins.map`，手改内容请先 git 提交或备份。

### 第 3 步：同步到 Dify

```bash
cd 读取json配置维表
python3 build_dify_bundle.py
```

将生成的 `dify_mes_dimension_node.py` **全文复制**到 Dify「代码」节点（入参：`user_question`；出参：`dimension_rules` 等接到【维表映射规则】变量）。

---

## `.map` 写法速查

文件头部有完整注释，核心格式如下：

```text
[全局]
默认别名=l
禁止=……

[表 TBL_表名]
标签=中文表名
关键词=词1, 词2
别名=SQL别名

[映射 英文id]
字段=事实表外键列
类型=账号          # 仅人员账号字段
可选=是            # 非必出映射
说明=备注
关联=别名 | 维表名 | ON条件 [| 依赖=上一别名]
列=SQL表达式 | 中文列名
禁止=错误写法示例
```

---

## 常见字段 → 抄哪段映射

| 事实表字段 | 映射写法 |
|-----------|----------|
| `CWC_ID` | `[映射 work_center]`，`wc` + `wc_p`（`CPARENT` 取父级工作中心名） |
| `CPROCESS_ID` | `[映射 process]` → `TBL_BD_PROCESS` |
| `CITEM_ID` | `[映射 item]` → `TBL_BD_ITEM` |
| `CITEM_TYPE_ID` | `[映射 item_type]` → `TBL_BD_ITEM_TYPE` |
| `CDEVICE_ID` | `[映射 device]` → `TBL_EAP_DEVICE`（**禁止**用于解析 `CWC_ID`） |
| `CLOCATION_ID` | `[映射 location]` → `TBL_WMS_LOCATION` |
| `CSTART_USER_NAME` / `CEND_USER_NAME` | `类型=账号`，别名建议 `u_s` / `u_e` → `TBL_SYS_USER` |
| `CMO_LOT` 关联工单 | 参考 `TBL_SFC_WS_LOG` 的 `[映射 mo_lot]` |

生产记录表 `TBL_SFC_WS_LOG` 有额外硬约束（工作中心/工序不得混用、禁止 `TBL_EAP_DEVICE` 解析 `CWC_ID` 等），见 `.map` 中该表下的 `禁止=` 行。

---

## 维护流程一览

```text
新表 / 新关联上线
  │
  ├─ 写入 中络项目MES 系统数据库表结构V1.1.md
  │
  ├─ 只加 1 张表 ──► 手改 mes_dimension_joins.map
  │
  └─ 表很多 / 文档大改 ──► generate_dimension_map_from_schema.py
  │
  └─► python3 build_dify_bundle.py ──► 复制 dify_mes_dimension_node.py 到 Dify
```

---

## 本地验证（可选）

```bash
# 查看某张表生成的规则文本
python3 mes_dimension_rules.py TBL_SFC_WS_LOG

# 按用户问题推断事实表
python3 mes_dimension_rules.py --question "查最近报工记录"
```

---

## 相关文档

- SQL 生成总规则：`../中络项目MES 最新生成SQL提示词.md`
- 表结构全文：`../中络项目MES 系统数据库表结构V1.1.md`
- 示例规则输出：`规则.txt`（仅供参考，以 `.map` / 代码节点为准）
