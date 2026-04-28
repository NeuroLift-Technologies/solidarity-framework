# Active Threads — NeuroLift-Technologies/solidarity-framework
> OTOI §4.1 Step 4 · Read before starting any work to avoid conflicts
> Last updated: 2026-04-28

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

### THREAD-002 — Governance File Repository Scoping
| Field | Value |
|-------|-------|
| **Thread ID** | THREAD-002 |
| **Status** | ✅ Complete |
| **Started** | 2026-04-28 |
| **Owner** | GitHub Copilot (@copilot) |
| **Branch** | `copilot/update-deployment-instructions` |
| **Task** | Update all governance files pulled in from .github-private to replace generic/template references with solidarity-framework–specific values (repo name, paths, URLs) |
| **Scope** | `AGENTS.md`, `NLT-DEV-OTOI.md`, `SOPs/new-agent-onboarding.md`, `SOPs/repo-governance-setup.md`, `SOPs/incident-response.md`, `SOPs/SOPs/new-agent-onboarding.md`, `SOPs/SOPs/repo-governance-setup.md`, `SOPs/SOPs/incident-response.md`, `agents/nlt-governance-steward.md`, `.nltotoi/index/governance-files.md`, `.nltotoi/.nltotoi/README.md`, `.nltotoi/.nltotoi/index/governance-files.md`, `.nltotoi/.nltotoi/proposals/validation-roadmap.md`, `nltotoi.json`, `docs/agent-log/README.md`, `docs/escalations/README.md`, `ISSUE_TEMPLATE/governance-proposal.md`, `rrt-advocate/CLAUDE.md`, `file-structure.md`, `agents/swe-agent.md` (new) |
| **Blockers** | None |
| **Related PR** | Branch `copilot/update-deployment-instructions` |
| **Notes** | Governance session artifacts (registration, this thread entry, handoff record) were filed retroactively per §2.1 transparency requirement. Work commits: `8b594e6`, `92618ca`. No architectural decisions were made; all changes were scoping/naming corrections only. |

### THREAD-004 — Solidarity Framework Skills
| Field | Value |
|-------|-------|
| **Thread ID** | THREAD-004 |
| **Status** | 🟡 In Progress |
| **Started** | 2026-04-28 |
| **Owner** | GitHub Copilot (@copilot) |
| **Branch** | `copilot/create-skills-for-solidarity-framework` |
| **Task** | Create standalone skill files for each Solidarity Framework component (RRT Advocate, NLT-OTOI, Sleepwalker Protocol, Unified Foundation) to enable modular adoption |
| **Scope** | `agents/rrt-advocate-skill.md`, `agents/nlt-otoi-skill.md`, `agents/sleepwalker-skill.md`, `agents/solidarity-foundation-skill.md`, `docs/active-threads.md`, `docs/agent-log/registrations/`, `docs/agent-log/handoffs/` |
| **Blockers** | None |
| **Related PR** | Branch `copilot/create-skills-for-solidarity-framework` |
| **Notes** | No architectural changes. Pure documentation/skill-file authoring. Skills are additive — no existing files deleted or modified. |

### THREAD-003 — Governance Enforcement for Remote Agents
| Field | Value |
|-------|-------|
| **Thread ID** | THREAD-003 |
| **Status** | 🟡 In Progress |
| **Started** | 2026-04-28 |
| **Owner** | GitHub Copilot (@copilot) |
| **Branch** | `copilot/update-deployment-instructions` |
| **Task** | Investigate root cause of VS Code Copilot Agents - Insiders not following governance; implement fixes to enforce OTOI §4.1 session start protocol for all remote agents |
| **Scope** | `.github/copilot-instructions.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/workflows/validate-governance.yml`, `docs/active-threads.md` |
| **Blockers** | None |
| **Related PR** | Branch `copilot/update-deployment-instructions` |
| **Notes** | Root cause: `.github/copilot-instructions.md` contained no OTOI governance protocol — only generic coding standards. VS Code Copilot reads this file at session start; without governance instructions there, it had no awareness of SOP-NLT-001. Three fixes: (1) copilot-instructions.md updated with full OTOI session start protocol, commit format, guardrails, escalation triggers, and handoff requirement; (2) PULL_REQUEST_TEMPLATE.md updated with governance checklist; (3) validate-governance.yml updated with agent-commit-format CI job. |

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
