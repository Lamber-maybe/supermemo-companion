# Spaced Repetition Companion — Agent Instructions

This repository's entire functionality lives in one self-contained Agent
Skill directory: **`spaced-repetition-companion/`**.

If you are an AI agent reading this file: open and follow
`spaced-repetition-companion/SKILL.md` **in full**. It is the complete
entry point — core principle, tool scope, routing to the three reference
files, ground rules, and personalization — and everything it points to
(`references/`, `docs/`, `assets/`, `scripts/`) lives alongside it inside
that same directory. Nothing else in this repository is required.

This file exists only as a thin bridge for agents that auto-load
`AGENTS.md`/`CLAUDE.md` at a repository root (Claude Code, Codex CLI,
OpenCode, and similar). If you're setting this skill up in your **own**
project rather than working inside this repository, copy or symlink the
`spaced-repetition-companion/` directory into wherever your agent looks
for Agent Skills, keeping the directory name unchanged, and load
`SKILL.md` from there directly — see `README.md` for details.
