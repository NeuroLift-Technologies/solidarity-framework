# CLAUDE.md — NeuroLift-Technologies/.github
> OTOI Compliance File · ORG-DEV-OTOI-1.0.0 · Step 3 of Agent Onboarding (SOP-NLT-001)

---

## Repository Identity

| Field              | Value                                               |
|--------------------|-----------------------------------------------------|
| **Repository**     | `NeuroLift-Technologies/.github`                    |
| **Visibility**     | Public                                              |
| **Purpose**        | Organization-wide GitHub configuration hub          |
| **OTOI Version**   | ORG-DEV-OTOI-1.0.0                                  |
| **Governing SOP**  | SOP-NLT-001 (`SOPs/new-agent-onboarding.md`)        |
| **Synced From**    | `.github-private` (canonical governance source)     |

---

## Purpose of This Repository

The `.github` repository is the **central configuration hub** for the NeuroLift Technologies GitHub organization. GitHub treats this repository specially — files here serve as organization-wide defaults for all repositories that do not define their own versions.

**This repository contains:**
- Community health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`)
- Default issue and pull request templates
- GitHub Copilot custom instructions (`.github/copilot-instructions.md`)
- Reusable CI/CD workflows (`.github/workflows/`)
- NLT governance files (synced from `.github-private`)
- Agent coordination infrastructure (`docs/`, `templates/`, `SOPs/`)

---

## What Agents May and May Not Do Here

### ✅ In Scope (proceed after task confirmation)
- Update community health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`)
- Update or add issue/PR templates under `ISSUE_TEMPLATE/`
- Update `.github/copilot-instructions.md`
- Update reusable workflow files in `.github/workflows/`
- Update governance tracking files in `docs/active-threads.md`
- Add agent registration and handoff records to `docs/agent-log/`
- Minor documentation improvements (typos, clarity, formatting)

### 🔴 Out of Scope — Escalate to Joshua W. Dorsey, Sr.
- Modifying the governance framework itself (OTOI, AGENTS.md, SOPs)
- Changes to `sync-governance-public.yml` workflow logic
- Introducing new external service integrations
- Changes that affect how governance files are synced from `.github-private`
- Any architectural decisions about how this repo interacts with other org repos
- Changes to the Solidarity Framework principles

---

## Additional Required Reading (Step 3 checklist)

Before beginning work, confirm you have read:

- [ ] `.github-private/NLT-DEV-OTOI.md` — the constitutional agent contract (ORG-DEV-OTOI-1.0.0)
- [ ] `.github-private/AGENTS.md` — coordination gateway and guardrails
- [ ] `SOPs/new-agent-onboarding.md` (this repo) — onboarding process SOP-NLT-001
- [ ] `docs/active-threads.md` (this repo) — current work in progress

---

## Repo-Specific Conventions

### File Naming
- Governance templates: `templates/{type}.json` or `templates/{type}.md`
- Agent registrations: `docs/agent-log/registrations/{YYYY-MM-DD}-{agent-name}-{session-id}.json`
- Handoff records: `docs/agent-log/handoffs/{YYYY-MM-DD}-{session-id}.json`

### Commit Format (mandatory)
```
[AGENT_NAME] type(scope): description
```
Valid types: `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `ci`

Examples for this repo:
```
[CLAUDE] chore(governance): sync active-threads from private repo
[CLAUDE] docs(contributing): clarify PR checklist items
[CODEX] feat(templates): add governance-proposal issue template
```

### Technology Stack
This is a configuration-only repository. It contains:
- Markdown files (`.md`) — primary format for all docs and templates
- JSON files (`.json`) — structured templates and agent records
- YAML files (`.yml`) — GitHub Actions workflows
- Shell scripts (`.sh`) — governance validation utilities

No application code lives in this repository.

---

## Escalation

**Primary escalation contact:** Joshua W. Dorsey, Sr.
**Email:** `joshua@neurolift.tech`
**Use the escalation template:** `templates/escalation.md`
**Or file a GitHub Issue:** Use the `agent-escalation` issue template

When in doubt, escalate. It is always better to pause than to guess.

---

## Governance Sync Note

Many files in this repository are **synced from `.github-private`** via the `sync-governance-public.yml` workflow. If you need to modify a governance document, the canonical edit should be made in `.github-private` and will propagate here on the next sync. Do not edit synced files in this repo directly unless you are the sync workflow itself.

Synced files are marked with a header comment: `<!-- SYNCED FROM .github-private — do not edit directly -->`

---

*This file is part of the ORG-DEV-OTOI-1.0.0 governance framework for NeuroLift Technologies.*
*Canonical source: `.github-private/CLAUDE.md` (synced to this repo)*
