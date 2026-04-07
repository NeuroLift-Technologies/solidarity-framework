---
name: Agent Escalation
about: Filed by an AI coding agent when a task requires human decision-making (per OTOI §4.3)
title: '[ESCALATION] [AGENT_NAME] [REPO] Brief description of the escalation'
labels: escalation, agent-governance
assignees: ''
---

<!--
FILING INSTRUCTIONS (for AI agents):
- File this issue BEFORE emailing joshua@neurolift.tech for P1/P2 urgency
- Fill in every section — partial escalations are not actionable
- Stop all work on the affected task until a decision is received
- Document this escalation in your handoff record under "escalations"
- Reference this issue URL in your escalation email
-->

## Escalation Summary

**Agent:** <!-- Your agent name, e.g. CLAUDE, CODEX, GEMINI -->
**Session ID:** <!-- Your session ID from your registration record -->
**Repository:** <!-- e.g. NeuroLift-Technologies/my-repo -->
**Branch:** <!-- e.g. feature/my-feature -->
**Active Thread ID:** <!-- e.g. THREAD-001 from docs/active-threads.md -->
**Urgency:** <!-- 🔴 High | 🟡 Medium | 🟢 Low -->
**Date:** <!-- YYYY-MM-DD -->

---

## Escalation Trigger

**Which OTOI §4.3 trigger applies? (check all that apply)**

- [ ] Architecture or system design decision
- [ ] New external service integration
- [ ] LLM provider selection or hard-coding
- [ ] Production deployment
- [ ] Security-affecting change
- [ ] Governance framework modification
- [ ] Scope expansion beyond confirmed task
- [ ] Ethical concern
- [ ] Ambiguous requirements that could lead to wrong implementation
- [ ] Other: ___________________

---

## Context

### What was the original confirmed task?
<!-- One to three sentences describing what the human asked me to do -->

### What did I discover that requires escalation?
<!-- Be specific. What did you find, encounter, or realize that triggered this escalation? -->

### Why can't I proceed without a decision?
<!-- Explain the risk of guessing or proceeding unilaterally -->

---

## Options (if applicable)

### Option A
**Description:** <!-- What is option A? -->
**Pros:** <!-- What are the advantages? -->
**Cons:** <!-- What are the risks or downsides? -->

### Option B
**Description:** <!-- What is option B? -->
**Pros:**
**Cons:**

### Option C (if applicable)
**Description:**
**Pros:**
**Cons:**

---

## Decision Needed

> **Please answer the following question to unblock me:**

<!-- State the exact yes/no or A/B/C question Joshua needs to answer. Be precise. -->

---

## Work Paused

I have stopped the following work pending this decision:

- <!-- Item 1 -->
- <!-- Item 2 -->

---

## Relevant Files

<!-- List any files that are directly relevant to the decision -->

- `path/to/file1`
- `path/to/file2`

---

## Additional Context

<!-- Any other information that will help Joshua make a fast, informed decision -->

---

<!--
AFTER DECISION IS MADE:
- Joshua (or designee) will comment on this issue with the decision
- Close this issue once the decision is documented
- Agent must update their handoff record with the decision
- Agent may resume work after explicit approval is posted
-->
