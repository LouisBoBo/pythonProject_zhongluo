#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地：采集表结构 + 规则审核。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from dify_audit_db_scheme import main as audit_main
from dify_get_db_scheme import main as fetch_main


def main() -> None:
    fetch_args: dict = {}
    if len(sys.argv) > 1:
        try:
            fetch_args.update(json.loads(sys.argv[1]))
        except json.JSONDecodeError:
            fetch_args["table_names"] = sys.argv[1]
    fetched = fetch_main(**fetch_args)
    if fetched.get("result") != "成功":
        print(json.dumps(fetched, ensure_ascii=False, indent=2))
        sys.exit(1)
    result = audit_main(schema_data=fetched["schema_data"])
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
