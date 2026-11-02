---
framework_version: 1.0.1
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [CLAUDE.md](CLAUDE.md) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Codex and Antigravity discover these automatically; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.

## Codex onboarding and personal-data boundary

For Turkish-language setup, read [CODEX_KURULUM_TR.md](CODEX_KURULUM_TR.md). It is an environment guide, not a replacement for the canonical workflows above. `python tools/career_check.py` provides a read-only diagnostic report.

Before personalizing tracked profile files or uploading career documents, verify that the destination repository is private. This fork may be public. If privacy is unverified, prepare generic templates only and keep personal data in an unshared local copy until a private destination is established. Never put personal data in public commits, issues, or pull requests. Local Git state and a connector-selected repository can refer to different copies; verify the actual destination for every push.

Claude-specific slash command registration, tool names, agent definitions and `.claude/settings.json` permissions do not automatically configure Codex. Read the canonical workflow, map its operations to available capabilities and the current runtime's permission rules, and report unsupported steps explicitly. Do not claim that source preparation means local installation or end-to-end validation has finished.
