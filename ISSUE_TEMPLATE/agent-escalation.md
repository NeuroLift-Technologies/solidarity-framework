---
name: Agent Escalation
about: Filed by an AI coding agent when a task needs a maintainer decision before it can proceed
title: '[ESCALATION] [AGENT_NAME] [REPO] Brief description'
labels: question, help wanted
assignees: ''
---

<!--
FILING INSTRUCTIONS (for AI agents):
- File this issue when a task is ambiguous, conflicts with existing work, or
  would require crossing a guardrail in AGENTS.md / GOVERNANCE.md.
- Fill in every section — partial escalations are hard to act on.
- Pause the affected line of work until a maintainer responds on this issue.
-->

## Escalation Summary

**Agent:** <!-- Your agent name, e.g. CLAUDE, CODEX, COPILOT -->
**Repository:** <!-- e.g. NeuroLift-Technologies/my-repo -->
**Branch / PR:** <!-- e.g. feature/my-feature, or a draft PR link -->
**Urgency:** <!-- 🔴 High | 🟡 Medium | 🟢 Low -->
**Date:** <!-- YYYY-MM-DD -->

---

## What's the situation?

### What was the original task?
<!-- One to three sentences describing what you were asked to do -->

### What did you find that requires a decision?
<!-- Be specific: what did you discover, encounter, or realize? -->

### Why can't you proceed without a decision?
<!-- Explain the risk of guessing or proceeding unilaterally -->

---

## Which guardrail or ambiguity applies? (check all that apply)

- [ ] Architecture or system design decision
- [ ] New external service integration
- [ ] LLM / AI provider selection or hard-coding
- [ ] Production deployment
- [ ] Security-affecting change
- [ ] Scope expansion beyond the confirmed task
- [ ] Ambiguous requirements that could lead to a wrong implementation
- [ ] Other: ___________________

---

## Options (if applicable)

### Option A
**Description:**
**Pros:**
**Cons:**

### Option B
**Description:**
**Pros:**
**Cons:**

---

## Decision needed

> **State the precise question a maintainer needs to answer to unblock you.**

<!-- e.g. a clear yes/no or A/B choice -->

---

## Work paused

- <!-- Item 1 -->
- <!-- Item 2 -->

---

## Relevant files

- `path/to/file1`
- `path/to/file2`

<!--
AFTER A DECISION IS POSTED:
- A maintainer will comment on this issue with the decision.
- Resume work only after explicit approval is posted, then close this issue.
-->
