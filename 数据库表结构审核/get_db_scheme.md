# 读取数据库表结构（Dify 代码节点）

支持 **PostgreSQL** 与 **SQL Server**。整段复制 `dify_get_db_scheme.py` 到 Dify。

## 依赖（按数据库类型安装）

```bash
# PostgreSQL（用户 postgres、端口 5432/15432）
pip install sqlalchemy psycopg2-binary

# SQL Server（用户 sa、端口 1433）
pip install sqlalchemy pymssql
```

## 输入变量

| 变量 | 说明 |
|------|------|
| `server` `port` `username` `password` `database` | 连接信息 |
| **`audit_table_names`** | 表名，逗号分隔（勿用 `table_names`） |
| `db_type` | 可选 `postgresql` / `mssql`；省略时按用户名、端口自动识别 |
| `schema` | PG 默认 `public`，SQL Server 默认 `dbo` |

## 自动识别示例

| 客户端配置 | 脚本识别 |
|------------|----------|
| 用户 `postgres`，库 `demo`，端口 `15432` | **postgresql** |
| 用户 `sa`，端口 `1433` | **mssql** |

## 常见错误

| 现象 | 原因 |
|------|------|
| `Adaptive Server is unavailable` | 用 SQL Server 驱动连了 **PostgreSQL**，请更新脚本或设 `db_type=postgresql` |
| 本机 DBeaver 能连、Dify 不能 | Dify 沙箱未开网：`CODE_EXECUTION_NETWORK_ENABLED=true` |

## 本地调试

```bash
python3 dify_get_db_scheme.py '{"server":"218.95.67.64","port":15432,"database":"demo","username":"postgres","password":"***","audit_table_names":"TBL_WMS_AREA"}'
```
