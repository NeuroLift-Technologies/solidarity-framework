# Governance Files Registry
> ORG-DEV-OTOI-1.0.4 · `.nltotoi/index/governance-files.md`
> Registry of all governed files in NeuroLift-Technologies/solidarity-framework
> Last updated: 2026-11-22

---

## Purpose

This registry lists every file in this repository that is part of the ORG-DEV-OTOI-1.0.4 governance framework. It is used by:
- The `validate-governance.sh` script to verify governance completeness
- Agents performing governance audits
- [The upstream governance comparison workflow](../../.github/workflows/sync-governance-public.yml) to preview changes to imported files

---

## Governance File Index

### Tier 1 — Required OTOI Files (mandatory for compliance)

| File | Status | Source | OTOI Reference | Last Verified |
|------|--------|--------|----------------|---------------|
| `CLAUDE.md` | ✅ Present | Maintained in `solidarity-framework` | §4.1 Step 3 | 2026-11-22 |
| `AGENTS.md` | ✅ Present | Maintained in `solidarity-framework` | §4.1 Step 2 | 2026-11-22 |
| `docs/active-threads.md` | ✅ Present | Maintained in repo | §4.1 Step 4 | 2026-11-22 |
| `docs/agent-log/README.md` | ✅ Present | Maintained in `solidarity-framework` | §3, §5 | 2026-11-22 |
| `docs/agent-log/registrations/` | ✅ Present | Agent-generated | §3 | 2026-11-22 |
| `docs/agent-log/handoffs/` | ✅ Present | Agent-generated | §5 | 2026-11-22 |

### Tier 2 — Templates (required for agent workflow)

| File | Status | Source | OTOI Reference | Last Verified |
|------|--------|--------|----------------|---------------|
| `templates/agent-registration.json` | ✅ Present | Imported from organization `.github` | §3, Step 5 | 2026-11-22 |
| `templates/handoff-record.json` | ✅ Present | Imported from organization `.github` | §5, Step 8 | 2026-11-22 |
| `templates/escalation.md` | ✅ Present | Maintained in `solidarity-framework` | §4.3 | 2026-11-22 |
| `templates/intent-log.md` | ✅ Present | Maintained in `solidarity-framework` | §4.4 | 2026-11-22 |

### Tier 3 — SOPs (operational procedures)

| File | Status | Source | SOP ID | Last Verified |
|------|--------|--------|--------|---------------|
| `SOPs/new-agent-onboarding.md` | ✅ Present | Maintained in `solidarity-framework` | SOP-NLT-001 | 2026-11-22 |
| `SOPs/repo-governance-setup.md` | ✅ Present | Maintained in `solidarity-framework` | SOP-NLT-002 | 2026-11-22 |
| `SOPs/incident-response.md` | ✅ Present | Maintained in `solidarity-framework` | SOP-NLT-003 | 2026-11-22 |

### Tier 4 — Issue Templates (GitHub workflow)

| File | Status | Source | Purpose | Last Verified |
|------|--------|--------|---------|---------------|
| `ISSUE_TEMPLATE/agent-escalation.md` | ✅ Present | Imported from organization `.github` | OTOI §4.3 escalation | 2026-11-22 |
| `ISSUE_TEMPLATE/governance-proposal.md` | ✅ Present | Imported from organization `.github` | Framework amendment process | 2026-11-22 |

### Tier 5 — Governance Infrastructure

| File | Status | Source | Purpose | Last Verified |
|------|--------|--------|---------|---------------|
| `GOVERNANCE.md` | ✅ Present | Maintained in `solidarity-framework` | Public contract entry point | 2026-11-22 |
| `nltotoi.json` | ✅ Present | Maintained in `solidarity-framework` | Discovery and upstream revision | 2026-11-22 |
| `.nltotoi/README.md` | ✅ Present | Maintained in `solidarity-framework` | Namespace overview | 2026-11-22 |
| `.nltotoi/contracts/README.md` | ✅ Present | Maintained in `solidarity-framework` | Contract discovery | 2026-11-22 |
| `.nltotoi/proposals/validation-roadmap.md` | ✅ Present | Maintained in `solidarity-framework` | Historical validation roadmap | 2026-11-22 |
| `.github/workflows/validate-governance.yml` | ✅ Present | Maintained in `solidarity-framework` | Governance and commit-format checks | 2026-11-22 |
| `.nltotoi/index/governance-files.md` | ✅ Present | Maintained in `solidarity-framework` | This file — governance registry | 2026-11-22 |
| `.nltotoi/scripts/validate-governance.sh` | ✅ Present | Maintained in `solidarity-framework` | Automated compliance validation | 2026-11-22 |

---

## Sync Status

The [public governance contract](../../GOVERNANCE.md) is maintained in the organization `.github` repository. The imported session and issue templates are identified in `nltotoi.json`. Local templates, coordination records and tooling are maintained here.

Files marked as **"Maintained in repo"** (e.g., `docs/active-threads.md`, agent log records) are managed directly in this repository by agents and maintainers.

---

## Validation

Run the governance validation script to verify all required files are present and well-formed:

```bash
bash .nltotoi/scripts/validate-governance.sh
```

The script will:
1. Check required files and discovery paths in `nltotoi.json` exist
2. Verify JSON templates parse without errors
3. Check that `docs/active-threads.md` is not stale (>30 days without update)
4. Report any missing or malformed governance files

---

## Adding a New Governance File

To add a new file to the governance framework:

1. Create a `governance-proposal` GitHub Issue describing the new file
2. Await Joshua W. Dorsey, Sr.'s approval
3. Add the file to `NeuroLift-Technologies/solidarity-framework` (canonical source)
4. Update this registry in `.nltotoi/index/governance-files.md`

---

*This file is part of the ORG-DEV-OTOI-1.0.4 governance framework for NeuroLift Technologies.*
