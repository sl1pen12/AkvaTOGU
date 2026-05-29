from pathlib import Path
PROJECT = Path(r"c:\project\mobile-app-creation-2-main")
REST = PROJECT / "_restored_from_transcript"
files = [
    "src/pages/SchedulePage.tsx",
    "src/config/api.ts",
    "src/lib/purchases.ts",
    "src/pages/HomePage.tsx",
    "src/pages/TariffsPage.tsx",
    "src/App.tsx",
]
for rel in files:
    a, b = PROJECT / rel, REST / rel
    if not b.exists():
        print(f"MISSING restored: {rel}")
        continue
    ta, tb = a.read_text(encoding="utf-8"), b.read_text(encoding="utf-8")
    print(f"{rel}: current={len(ta)} restored={len(tb)} same={ta==tb}")
