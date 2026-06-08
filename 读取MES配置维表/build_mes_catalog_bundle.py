#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从《中络项目MES 系统表名清单V1.2.md》打包 Dify 选表清单代码节点：

  python3 build_mes_catalog_bundle.py

维护：
  1. 改 中络项目MES 系统表名清单V1.2.md
  2. 运行本脚本
  3. 复制 dify_mes_table_catalog.py 到 Dify「输出表名清单」代码节点
"""

from __future__ import annotations

import json
from pathlib import Path

from mes_table_catalog import count_slim_tables, count_tables, load_catalog_text, slim_catalog_text
from mes_table_catalog_rank import rank_catalog_lines

ROOT = Path(__file__).resolve().parent
MD_FILE = ROOT.parent / "中络项目MES 系统表名清单V1.2.md"
OUT = ROOT / "dify_mes_table_catalog.py"
RANK_CORE = (ROOT / "mes_table_catalog_rank.py").read_text(encoding="utf-8")
RANK_CORE = RANK_CORE.split('if __name__', 1)[0].strip()
if RANK_CORE.startswith("#!"):
    RANK_CORE = "\n".join(RANK_CORE.splitlines()[1:]).strip()
RANK_CORE = RANK_CORE.replace("from __future__ import annotations\n\n", "")

HEADER = '''# -*- coding: utf-8 -*-
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

'''

DIFY_ENTRY = '''
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
'''


def main() -> None:
    if not MD_FILE.is_file():
        raise SystemExit(f"未找到：{MD_FILE}")

    catalog = load_catalog_text(MD_FILE)
    slim = slim_catalog_text(catalog)
    n_tables = count_slim_tables(slim)
    n_full = count_tables(catalog)
    if n_tables != n_full:
        print(f"警告：精简表数 {n_tables} 与完整表数 {n_full} 不一致")

    # 抽样验证通用排序
    for q in ("查询近一个月维修工单", "采购收货明细", "IPQC检验记录"):
        ranked, n, mode = rank_catalog_lines(q, slim, top_n=35)
        print(f"  [{mode}] {q!r} → {n} 张候选, {len(ranked)} 字符")

    print(
        f"表名清单：{n_tables} 张表，"
        f"精简 {len(slim)} 字符（完整 {len(catalog)} 字符）"
    )

    main_fn = '''
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
'''.strip()

    body = (
        f"_EMBEDDED_CATALOG_SLIM = {json.dumps(slim, ensure_ascii=False)}\n"
        f'_EMBEDDED_CATALOG_FULL_CHAR_COUNT = "{len(catalog)}"\n'
        f'_EMBEDDED_TABLE_COUNT = "{n_tables}"\n\n'
        + RANK_CORE
        + "\n\n"
        + main_fn
        + "\n"
        + DIFY_ENTRY
    )

    OUT.write_text(HEADER + body, encoding="utf-8")
    print(f"已生成 {OUT.name}（{OUT.stat().st_size} 字节）")


if __name__ == "__main__":
    main()
