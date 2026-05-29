#!/usr/bin/env python3
"""Replay Write/StrReplace from agent transcript onto project files."""
import json
import re
import shutil
from pathlib import Path

TRANSCRIPT = Path(
    r"C:\Users\nikit\.cursor\projects\c-project-mobile-app-creation-2-main"
    r"\agent-transcripts\e7772ec1-737a-4def-a52f-3f8efa01ef01"
    r"\e7772ec1-737a-4def-a52f-3f8efa01ef01.jsonl"
)
PROJECT = Path(r"c:\project\mobile-app-creation-2-main")
BACKUP = PROJECT / "_backup_before_restore"
RENDER_API = """/** Бэкенд на Render (деплой из GitHub). Для локальной разработки: VITE_API_BASE_URL=http://localhost:5000 */
const API_BASE =
  (import.meta.env.VITE_API_BASE_URL as string | undefined)?.replace(/\\/$/, '') ||
  'https://pool-backend-nmuz.onrender.com';

export const API_URLS = {
  auth: `${API_BASE}/auth`,
  bookings: `${API_BASE}/bookings`,
  purchases: `${API_BASE}/purchases`,
  notifications: `${API_BASE}/notifications`,
};
"""

files: dict[str, str] = {}
stats = {"write": 0, "replace_ok": 0, "replace_miss": 0, "replace_disk": 0}


def norm_path(p: str) -> str | None:
    p = p.replace("/", "\\")
    m = re.search(r"mobile-app-creation-2-main\\(.+)$", p, re.I)
    return m.group(1) if m else None


def get_text(rel: str) -> str | None:
    if rel in files:
        return files[rel]
    disk = PROJECT / rel
    if disk.exists():
        return disk.read_text(encoding="utf-8")
    return None


def set_text(rel: str, text: str) -> None:
    files[rel] = text


for line in TRANSCRIPT.read_text(encoding="utf-8").splitlines():
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        continue
    for block in obj.get("message", {}).get("content", []):
        if block.get("type") != "tool_use":
            continue
        name = block.get("name")
        inp = block.get("input", {})
        rel = norm_path(inp.get("path", ""))
        if not rel:
            continue
        if name == "Write" and "contents" in inp:
            set_text(rel, inp["contents"])
            stats["write"] += 1
        elif name == "StrReplace" and "old_string" in inp and "new_string" in inp:
            old, new = inp["old_string"], inp["new_string"]
            text = get_text(rel)
            if text is None:
                stats["replace_miss"] += 1
                print(f"SKIP (no file): {rel}")
                continue
            if old not in text:
                stats["replace_miss"] += 1
                print(f"MISS: {rel} ({len(old)} chars old)")
                continue
            set_text(rel, text.replace(old, new, 1))
            stats["replace_ok"] += 1

# Backup and write
if BACKUP.exists():
    shutil.rmtree(BACKUP)
BACKUP.mkdir()
for rel, text in sorted(files.items()):
    src = PROJECT / rel
    if src.exists():
        dest = BACKUP / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    out = PROJECT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")

print("Stats:", stats)
print(f"Wrote {len(files)} files. Backup: {BACKUP}")
