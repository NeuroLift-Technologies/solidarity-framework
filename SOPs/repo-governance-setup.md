<!-- SYNCED FROM .github-private — do not edit directly -->
# SOP-NLT-002 — Repository Governance Bootstrap
> Standard Operating Procedure · ORG-DEV-OTOI-1.0.0
> Applies to: Any agent bootstrapping NLT governance infrastructure in a new repository
> Effective: 2025-04-04 · Owner: Joshua W. Dorsey, Sr.

---

## Purpose

This SOP defines the process for setting up ORG-DEV-OTOI-1.0.0-compliant governance infrastructure in a new NeuroLift Technologies repository. It ensures all repositories have a consistent, complete governance foundation before active agent work begins.

---

## When to Use This SOP

Use this SOP when:
- A new repository is being created in the NeuroLift Technologies GitHub organization
- An existing repository needs governance infrastructure added for the first time
- A repository is being brought into OTOI compliance retroactively

---

## Prerequisites

- You have read and completed SOP-NLT-001 (new agent onboarding) for your session
- Joshua W. Dorsey, Sr. has approved the repository creation or governance bootstrap
- You have write access to the target repository
- You have access to the governance templates in `NeuroLift-Technologies/.github/templates/`

---

## Required Governance Files

Every NLT repository must have the following governance infrastructure:

### Tier 1 — Required (OTOI mandatory)
| File | Purpose |
|------|---------|
| `CLAUDE.md` | OTOI Step 3 — repo-specific agent context |
| `docs/active-threads.md` | OTOI Step 4 — work tracking |
| `docs/agent-log/README.md` | Agent log directory explanation |
| `docs/agent-log/registrations/.gitkeep` | Placeholder for registration records |
| `docs/agent-log/handoffs/.gitkeep` | Placeholder for handoff records |

### Tier 2 — Recommended (strong OTOI alignment)
| File | Purpose |
|------|---------|
| `AGENTS.md` | Local copy of coordination gateway (or symlink reference) |
| `.nltotoi/index/governance-files.md` | Local governance registry |
| `.nltotoi/scripts/validate-governance.sh` | Local validation script |

### Tier 3 — Optional (enhance governance quality)
| File | Purpose |
|------|---------|
| `templates/` | Local copies of all governance templates |
| `SOPs/` | Local copies of relevant SOPs |
| `ISSUE_TEMPLATE/agent-escalation.md` | Agent escalation issue template |
| `ISSUE_TEMPLATE/governance-proposal.md` | Governance proposal issue template |

---

## Step-by-Step Process

### Phase 1 — Preparation

1. **Complete SOP-NLT-001 onboarding** for this session (all 8 steps)
2. **Confirm scope with Joshua** — get explicit approval that this repo needs governance bootstrap
3. **Identify the target repository** and note its purpose, primary language(s), and team
4. **Create a branch** for the governance bootstrap work:
   ```
   git checkout -b chore/governance-bootstrap
   ```

### Phase 2 — Create Directory Structure

```bash
mkdir -p docs/agent-log/registrations
mkdir -p docs/agent-log/handoffs
mkdir -p .nltotoi/index
mkdir -p .nltotoi/scripts
mkdir -p templates
mkdir -p SOPs
```

Create placeholder files for empty directories:
```bash
touch docs/agent-log/registrations/.gitkeep
touch docs/agent-log/handoffs/.gitkeep
```

**Commit:**
```
[AGENT_NAME] chore(governance): initialize OTOI directory structure (ORG-DEV-OTOI-1.0.0)
```

### Phase 3 — Create Repo-Specific CLAUDE.md

Copy the `CLAUDE.md` template from `NeuroLift-Technologies/.github/CLAUDE.md` and customize:
- Update the repository name and description
- Update the purpose section to describe this specific repo
- Update the in-scope/out-of-scope items for this repo's domain
- Update the technology stack section
- Adjust any repo-specific conventions

**Commit:**
```
[AGENT_NAME] chore(governance): add CLAUDE.md for OTOI Step 3 compliance
```

### Phase 4 — Create docs/active-threads.md

Copy from `NeuroLift-Technologies/.github/docs/active-threads.md` and:
- Update the repository name in the header
- Clear any existing threads (start with empty Active Threads section)
- Update the last-updated date

**Commit:**
```
[AGENT_NAME] chore(governance): add active-threads.md for OTOI Step 4 compliance
```

### Phase 5 — Add AGENTS.md (Tier 2)

Either:
- Copy the org-level `AGENTS.md` from `.github` directly, OR
- Create a minimal `AGENTS.md` that references `NeuroLift-Technologies/.github/AGENTS.md` for the canonical version

Add any repo-specific coordination notes at the top.

**Commit:**
```
[AGENT_NAME] chore(governance): add AGENTS.md coordination gateway
```

### Phase 6 — Add Templates (Tier 3, if required)

Copy all templates from `NeuroLift-Technologies/.github/templates/`:
- `agent-registration.json`
- `handoff-record.json`
- `escalation.md`
- `intent-log.md`

**Commit:**
```
[AGENT_NAME] chore(governance): add agent governance templates
```

### Phase 7 — Add Governance Validation

Copy from `NeuroLift-Technologies/.github/.nltotoi/`:
- `.nltotoi/index/governance-files.md` (customize for this repo)
- `.nltotoi/scripts/validate-governance.sh`

Run the validation script to confirm all required files are present:
```bash
bash .nltotoi/scripts/validate-governance.sh
```

Fix any issues before proceeding.

**Commit:**
```
[AGENT_NAME] chore(governance): add OTOI governance index and validation script
```

### Phase 8 — Open Pull Request

Create a PR with:
- **Title:** `chore(governance): bootstrap OTOI governance infrastructure (ORG-DEV-OTOI-1.0.0)`
- **Description:** Reference this SOP, list all files added, confirm validation script passes
- **Reviewer:** Joshua W. Dorsey, Sr.
- **Labels:** `governance`, `chore`

### Phase 9 — Write Handoff Record

Per SOP-NLT-001 Step 8, write your handoff record to `docs/agent-log/handoffs/` before ending the session.

---

## Validation Checklist

Before closing the bootstrap PR, confirm:

- [ ] `CLAUDE.md` exists and is repo-specific (not a generic copy)
- [ ] `docs/active-threads.md` exists with empty active threads
- [ ] `docs/agent-log/README.md` exists
- [ ] `docs/agent-log/registrations/.gitkeep` exists
- [ ] `docs/agent-log/handoffs/.gitkeep` exists
- [ ] `.nltotoi/scripts/validate-governance.sh` runs without errors
- [ ] Your agent registration record is in `docs/agent-log/registrations/`
- [ ] Handoff record is written to `docs/agent-log/handoffs/`
- [ ] All commits use the correct `[AGENT_NAME] type(scope): description` format
- [ ] Joshua W. Dorsey, Sr. has reviewed and approved the PR

---

## Document Control

| Field | Value |
|-------|-------|
| **SOP ID** | SOP-NLT-002 |
| **Version** | 1.0.0 |
| **Effective Date** | 2025-04-04 |
| **Owner** | Joshua W. Dorsey, Sr. |
| **Review Cycle** | Quarterly |
| **Next Review** | 2025-07-04 |
| **OTOI Alignment** | ORG-DEV-OTOI-1.0.0 |

---

*Canonical source: `.github-private/SOPs/repo-governance-setup.md` · Synced to public `.github` repo*
