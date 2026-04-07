# Governance Files Registry
> ORG-DEV-OTOI-1.0.0 · `.nltotoi/index/governance-files.md`
> Registry of all governed files in NeuroLift-Technologies/.github
> Last updated: 2025-04-04

---

## Purpose

This registry lists every file in this repository that is part of the ORG-DEV-OTOI-1.0.0 governance framework. It is used by:
- The `validate-governance.sh` script to verify governance completeness
- Agents performing governance audits
- The `sync-governance-public.yml` workflow to track synced files

---

## Governance File Index

### Tier 1 — Required OTOI Files (mandatory for compliance)

| File | Status | Source | OTOI Reference | Last Verified |
|------|--------|--------|----------------|---------------|
| `CLAUDE.md` | ✅ Present | Synced from `.github-private` | §4.1 Step 3 | 2025-04-04 |
| `AGENTS.md` | ✅ Present | Synced from `.github-private` | §4.1 Step 2 | 2025-04-04 |
| `docs/active-threads.md` | ✅ Present | Maintained in repo | §4.1 Step 4 | 2025-04-04 |
| `docs/agent-log/README.md` | ✅ Present | Synced from `.github-private` | §3, §5 | 2025-04-04 |
| `docs/agent-log/registrations/` | ✅ Present | Agent-generated | §3 | 2025-04-04 |
| `docs/agent-log/handoffs/` | ✅ Present | Agent-generated | §5 | 2025-04-04 |

### Tier 2 — Templates (required for agent workflow)

| File | Status | Source | OTOI Reference | Last Verified |
|------|--------|--------|----------------|---------------|
| `templates/agent-registration.json` | ✅ Present | Synced from `.github-private` | §3, Step 5 | 2025-04-04 |
| `templates/handoff-record.json` | ✅ Present | Synced from `.github-private` | §5, Step 8 | 2025-04-04 |
| `templates/escalation.md` | ✅ Present | Synced from `.github-private` | §4.3 | 2025-04-04 |
| `templates/intent-log.md` | ✅ Present | Synced from `.github-private` | §4.4 | 2025-04-04 |

### Tier 3 — SOPs (operational procedures)

| File | Status | Source | SOP ID | Last Verified |
|------|--------|--------|--------|---------------|
| `SOPs/new-agent-onboarding.md` | ✅ Present | Synced from `.github-private` | SOP-NLT-001 | 2025-04-04 |
| `SOPs/repo-governance-setup.md` | ✅ Present | Synced from `.github-private` | SOP-NLT-002 | 2025-04-04 |
| `SOPs/incident-response.md` | ✅ Present | Synced from `.github-private` | SOP-NLT-003 | 2025-04-04 |

### Tier 4 — Issue Templates (GitHub workflow)

| File | Status | Source | Purpose | Last Verified |
|------|--------|--------|---------|---------------|
| `ISSUE_TEMPLATE/agent-escalation.md` | ✅ Present | Synced from `.github-private` | OTOI §4.3 escalation | 2025-04-04 |
| `ISSUE_TEMPLATE/governance-proposal.md` | ✅ Present | Synced from `.github-private` | Framework amendment process | 2025-04-04 |

### Tier 5 — Governance Infrastructure

| File | Status | Source | Purpose | Last Verified |
|------|--------|--------|---------|---------------|
| `.nltotoi/index/governance-files.md` | ✅ Present | Synced from `.github-private` | This file — governance registry | 2025-04-04 |
| `.nltotoi/scripts/validate-governance.sh` | ✅ Present | Synced from `.github-private` | Automated compliance validation | 2025-04-04 |

---

## Sync Status

Files marked as **"Synced from `.github-private`"** are managed by the `sync-governance-public.yml` workflow. Do not edit these files directly in this repository. Make changes in `.github-private` and allow the sync workflow to propagate them.

Files marked as **"Maintained in repo"** (e.g., `docs/active-threads.md`, agent log records) are managed directly in this repository by agents and maintainers.

---

## Validation

Run the governance validation script to verify all required files are present and well-formed:

```bash
bash .nltotoi/scripts/validate-governance.sh
```

The script will:
1. Check all Tier 1 and Tier 2 files exist
2. Verify JSON templates parse without errors
3. Check that `docs/active-threads.md` is not stale (>30 days without update)
4. Report any missing or malformed governance files

---

## Adding a New Governance File

To add a new file to the governance framework:

1. Create a `governance-proposal` GitHub Issue describing the new file
2. Await Joshua W. Dorsey, Sr.'s approval
3. Add the file to `.github-private` (canonical source)
4. Update this registry in `.github-private/.nltotoi/index/governance-files.md`
5. The sync workflow will propagate changes to this repo

---

*This file is part of the ORG-DEV-OTOI-1.0.0 governance framework for NeuroLift Technologies.*
