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


def _validate_local_instance_root(value: Path) -> tuple[Path, Path]:
    """Fail closed for data-path indirection in an explicitly selected instance.

    The engine is shared but instance data cannot be redirected with filesystem
    links/junctions into another library. Does not create or initialize data.
    """
    raw_root = value.expanduser().absolute()
    if not raw_root.is_dir() or raw_root.is_symlink() or bool(getattr(raw_root, "is_junction", lambda: False)()):
        raise ValueError("--instance-root must be an existing plain local directory")
    root = raw_root.resolve()
    for relative in ("01_DB", "01_DB/koa_mediatheque.sqlite", "02_STORAGE", "02_STORAGE/source_files"):
        current = root
        for part in Path(relative).parts:
            current = current / part
            if current.is_symlink() or bool(getattr(current, "is_junction", lambda: False)()):
                raise ValueError("Instance database/storage path contains a link or junction")
        if not current.resolve().is_relative_to(root):
            raise ValueError("Instance database/storage path escapes selected instance")
    db = root / "01_DB" / "koa_mediatheque.sqlite"
    storage = root / "02_STORAGE"
    if not db.is_file() or not storage.is_dir():
        raise ValueError("--instance-root requires initialized DB and existing 02_STORAGE directory")
    return db, storage


def main() -> int:
    p = argparse.ArgumentParser(description="Plan/accept EncyK v2 evidence into Médiathèque source catalog")
    p.add_argument("--handoff", required=True, type=Path, help="Path to producer handoff JSON")
    p.add_argument("--evidence-root", required=True, type=Path, help="Root of EncyK checkout; relative paths resolve here")
    p.add_argument("--db", type=Path, help="Existing Médiathèque sqlite DB (only with --accept)")
    p.add_argument("--storage", type=Path, help="Médiathèque 02_STORAGE directory (only with --accept)")
    p.add_argument("--instance-root", type=Path,
                   help="Existing local Médiathèque instance root; derives its DB and storage paths")
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
            if a.instance_root:
                if a.db or a.storage:
                    raise ValueError("--instance-root cannot be combined with --db or --storage")
                db_path, storage_path = _validate_local_instance_root(a.instance_root)
            else:
                db_path, storage_path = a.db, a.storage
            if not db_path or not storage_path or not db_path.is_file():
                raise ValueError("--accept requires an existing instance DB, or --db existing.sqlite and --storage directory")
            connection = get_db_connection(db_path)
            try:
                payload = import_encyk_handoff(connection, a.handoff, a.evidence_root, storage_path)
            finally:
                connection.close()
        emit(payload)
        return 0
    except Exception as exc:
        emit({"format": "koa.encyk-source-handoff-attempt/1.0.0", "status": "rejected", "error": str(exc)}, failed=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
