# Active Threads — NeuroLift-Technologies/.github
> OTOI §4.1 Step 4 · Read before starting any work to avoid conflicts
> Last updated: 2026-04-04

---

## How to Use This File

This file tracks all **current and recently completed** work threads in this repository. Before starting any task, you must:

1. Read this file in its entirety
2. Identify any active threads related to your task
3. Check for potential conflicts with in-progress work
4. Register your new thread in the **Active Threads** section below
5. Move completed threads to **Completed Threads** when done

**Update this file as part of your first commit when starting a thread, and as part of your handoff record when closing one.**

---

## Active Threads

<!-- Add new threads here. One entry per thread. -->

### THREAD-001 — Governance File Bootstrap
| Field | Value |
|-------|-------|
| **Thread ID** | THREAD-001 |
| **Status** | 🟡 In Progress |
| **Started** | 2025-04-04 |
| **Owner** | Pending assignment |
| **Branch** | `copilot/sync-governance-public-files` |
| **Task** | Create and populate all initial governance files for the `.github` public repo as part of the `sync-governance-public.yml` workflow bootstrap |
| **Scope** | `CLAUDE.md`, `AGENTS.md`, `docs/`, `templates/`, `SOPs/`, `ISSUE_TEMPLATE/agent-escalation.md`, `ISSUE_TEMPLATE/governance-proposal.md`, `.nltotoi/` |
| **Blockers** | None |
| **Related PR** | TBD |
| **Notes** | This is the initial governance bootstrap. No prior governance infrastructure exists in this repo. |

---

## Completed Threads

<!-- Move threads here when closed. Retain for 30 days after completion. -->

*No completed threads yet.*

---

## Thread Registry Format

When adding a new thread, copy this template:

```markdown
### THREAD-XXX — [Short Title]
| Field | Value |
|-------|-------|
| **Thread ID** | THREAD-XXX |
| **Status** | 🟡 In Progress / 🔴 Blocked / ✅ Complete |
| **Started** | YYYY-MM-DD |
| **Owner** | [Agent name or human] |
| **Branch** | `branch-name` |
| **Task** | [One-sentence description] |
| **Scope** | [Files or areas affected] |
| **Blockers** | [None, or description] |
| **Related PR** | [PR URL or TBD] |
| **Notes** | [Any relevant context for future agents] |
```

---

## Conflict Avoidance Rules

- **One agent per thread** — if you need to hand off a thread, write a handoff record first
- **Do not modify files owned by another active thread** without explicit coordination
- **If you see a conflict**, stop and escalate via the `agent-escalation` issue template
- **Stale threads** (no update in 7+ days) should be escalated to Joshua W. Dorsey, Sr. for disposition

---

*This file is part of the ORG-DEV-OTOI-1.0.0 governance framework for NeuroLift Technologies.*
