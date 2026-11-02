#!/usr/bin/env python3
"""Read-only readiness report; never installs tools or contacts a service."""

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import sys


def report(root):
    checks = []

    def add(name, ok, required, detail):
        checks.append(dict(name=name, status="ok" if ok else ("missing" if required else "optional"),
                           required=required, detail=detail))

    add("Python >= 3.10", sys.version_info >= (3, 10), True, sys.version.split()[0])
    for name in ("AGENTS.md", "CLAUDE.md", ".claude/commands/setup.md", ".claude/commands/apply.md"):
        add(name, (root / name).is_file(), True, "framework file")
    for name, purpose in (("git", "version control"), ("codex", "local Codex workflow"),
                          ("bun", "portal search"), ("lualatex", "stock CV PDF"),
                          ("xelatex", "stock cover letter PDF"),
                          ("pdftotext", "optional PDF text fallback")):
        add(name, shutil.which(name) is not None, False, purpose)
    for name, purpose in (("pypdf", "PDF text extraction"), ("yaml", "framework lint (PyYAML)")):
        add(name, importlib.util.find_spec(name) is not None, False, purpose)
    profile = root / "CLAUDE.md"
    populated = profile.is_file() and "[YOUR_NAME]" not in profile.read_text(encoding="utf-8")
    add("profile", populated, False, "Placeholder check only; does not validate facts. Personalize only in a verified private repository or offline local copy.")
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    args = parser.parse_args()
    checks = report(args.root.resolve())
    ready = all(c["status"] == "ok" for c in checks if c["required"])
    if args.json:
        print(json.dumps({"framework_ready": ready, "checks": checks}, ensure_ascii=True, indent=2))
    else:
        for c in checks:
            print("[{status}] {name}: {detail}".format(**c))
        print("This report does not prove portal access, PDF compilation, repository privacy, or end-to-end readiness.")
    return 0 if ready else 1


if __name__ == "__main__":
    sys.exit(main())
