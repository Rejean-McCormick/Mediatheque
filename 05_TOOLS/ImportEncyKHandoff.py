"""Explicit, local-only EncyK → Médiathèque kOA handoff importer.

PLAN by default. Add --accept to import verified evidence into a local DB.
No network operation, no Kristal semantic construction, no publication.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "06_GUI" / "koa_mediatheque_gui"))

from koa_mediatheque.db import get_db_connection  # noqa: E402
from koa_mediatheque.services.encyk_handoff_service import (  # noqa: E402
    import_encyk_handoff,
    plan_encyk_handoff,
)


def main() -> int:
    p = argparse.ArgumentParser(description="Plan/accept EncyK v2 evidence into Médiathèque source catalog")
    p.add_argument("--handoff", required=True, type=Path, help="Path to producer handoff JSON")
    p.add_argument("--evidence-root", required=True, type=Path, help="Root of EncyK checkout; relative paths resolve here")
    p.add_argument("--db", type=Path, help="Existing Médiathèque sqlite DB (only with --accept)")
    p.add_argument("--storage", type=Path, help="Médiathèque 02_STORAGE directory (only with --accept)")
    p.add_argument("--accept", action="store_true", help="Explicitly import into local private source storage")
    p.add_argument("--receipt-out", type=Path, help="Optional local JSON receipt file (including rejection reasons)")
    a = p.parse_args()
    def emit(payload: dict, *, failed: bool = False):
        text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        if a.receipt_out:
            out = a.receipt_out.expanduser().resolve()
            out.parent.mkdir(parents=True, exist_ok=True)
            temporary = out.with_name(out.name + ".part")
            temporary.write_text(text, encoding="utf-8")
            os.replace(temporary, out)
        print(text, end="", file=sys.stderr if failed else sys.stdout)

    try:
        if not a.accept:
            plan = plan_encyk_handoff(a.handoff, a.evidence_root)
            payload = {"status": "plan_valid", "handoff_id": plan["handoff_id"],
                "contract": plan["contract"], "file_count": len(plan["files"]),
                "total_bytes": plan["total_bytes"], "no_writes": True}
        else:
            if not a.db or not a.storage or not a.db.is_file():
                raise ValueError("--accept requires --db existing.sqlite and --storage directory")
            connection = get_db_connection(a.db)
            try:
                payload = import_encyk_handoff(connection, a.handoff, a.evidence_root, a.storage)
            finally:
                connection.close()
        emit(payload)
        return 0
    except Exception as exc:
        emit({"format": "koa.encyk-source-handoff-attempt/1.0.0", "status": "rejected", "error": str(exc)}, failed=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
