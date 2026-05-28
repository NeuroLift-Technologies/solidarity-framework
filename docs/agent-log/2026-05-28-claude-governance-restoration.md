# Claude Code Agent Log — Governance Restoration (supersedes PR #22)

**Date:** 2026-05-28
**Agent:** Claude Code (claude-opus-4-7)
**Session:** claude/governance-docs-restore-yB5sI
**Repository:** NeuroLift-Technologies/solidarity-framework
**Supersedes:** PR #22 (`governance/otoi-compliance`, Copilot baseline)

## Summary

Restored org-level governance framing that Copilot PR #22 over-trimmed via a
global find/replace that substituted both `.github-private` and `.github` with
`solidarity-framework`. Part of a coordinated 11-repo cleanup tracked in
`nlt-agent-1` PR #4.

Copilot's substitution destroyed the public/private distinction in several
files — notably the `.github` public-mirror references which are canonical and
must remain pointing at `NeuroLift-Technologies/.github`.

## Changes Applied (correct subset of PR #22)

- `README.md` — added `ai_assistant_directive` YAML block under the title
  pointing future agents at `NLT-DEV-OTOI.md` before any work.
- `CLAUDE.md` — added `NLT-DEV-OTOI.md` as the first item in the Step 3
  required-reading checklist.
- `.nltotoi/.nltotoi/scripts/validate-governance.sh` — line 151
  `check_content` repository-name assertion updated to
  `NeuroLift-Technologies/solidarity-framework` (was `.github-private`).
- `nltotoi.json` — bumped `metadata.last_updated` to `2026-05-28`. Repository
  name was already correct. Preserved canonical
  `repository.purpose`, `visibility: private`, and the
  `ethical_framework.public_governance` URL pointing at
  `https://github.com/NeuroLift-Technologies/.github` (public mirror).
- `SOPs/SOPs/repo-governance-setup.md` — upgraded v1.0.0 → v1.1.0 from
  canonical `.github-private` source.
- `docs/agent-log/2026-05-21-codex-repo-specific-governance.md` — kept the
  Copilot/Codex audit log entry.

## Changes Explicitly Rejected from PR #22

- `NLT-DEV-OTOI.md`, `AGENTS.md` — org-wide framing preserved.
- `SOPs/SOPs/repo-governance-setup.md` `.github` public-mirror URL preserved
  (the v1.1.0 upgrade itself, not Copilot's text substitution).
- `ISSUE_TEMPLATE/config.yml` — security URL stays on `.github`.
- `.github/workflows/sync-governance-public.yml` — sync target stays on
  the `.github` public repo. (Copilot's edit here was particularly bad — it
  would have made the workflow sync into this repo itself instead of the
  public mirror.)
- `docs/active-threads.md`, `file-structure.md` — historical/architectural
  references preserved.
- `templates/agent-registration.json`, `templates/handoff-record.json` —
  example values referencing `.github` preserved.
- All `docs/agent-log/handoffs/*.json` and
  `docs/agent-log/registrations/*.json` — historical records, not rewritten.

## Validator Result

See commit message and PR description for `validate-governance.sh` output.

## Escalation

None required. All changes within scope of governance baseline restoration.
