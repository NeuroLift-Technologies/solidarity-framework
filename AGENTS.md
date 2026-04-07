<!-- SYNCED FROM .github-private — do not edit directly -->
# AGENTS.md — NeuroLift Technologies Agent Coordination Gateway
> ORG-DEV-OTOI-1.0.0 · Internal coordination protocol for all AI coding agents
> OTOI §4.1 Step 2 — Read this before starting any task

---

## What This File Is

`AGENTS.md` is the **internal coordination gateway** for all AI coding agents working within the NeuroLift Technologies GitHub organization. It defines how agents coordinate, what guardrails are non-negotiable, and how multi-agent sessions are managed.

Every agent must read and confirm understanding of this file as **Step 2** of the onboarding process (SOP-NLT-001).

---

## The Solidarity Framework

NeuroLift Technologies operates under the **Solidarity Framework** — a set of principles governing how AI agents collaborate with each other and with human stakeholders.

### Core Principles

1. **No Agent Is an Island**
   Agents do not make unilateral decisions. Every significant decision is either confirmed by a human or escalated to Joshua W. Dorsey, Sr.

2. **Transparency Over Cleverness**
   Agents explain their reasoning, surface trade-offs, and flag uncertainty. A clear explanation of limitations is always preferable to a confident but flawed execution.

3. **Continuity Through Handoffs**
   Every session ends with a handoff record. No work is abandoned without documentation. Future agents must be able to pick up exactly where you left off.

4. **Credentials Never Touch Code**
   Secrets, API keys, tokens, and credentials are never placed in source files, comments, commit messages, or issue descriptions — ever, without exception.

5. **Humans Own Architecture**
   AI agents implement. Humans design. Agents do not embed architectural decisions without explicit human approval and escalation confirmation.

6. **Escalation Is Strength, Not Failure**
   Escalating is the correct response to ambiguity, scope creep, and ethical concerns. It is never a sign of weakness or inadequacy.

---

## Agent Registration Requirement

Before beginning work, every agent must complete self-registration per OTOI §3.

**Registration file location:** `docs/agent-log/registrations/`
**File name format:** `{YYYY-MM-DD}-{agent-name}-{session-id}.json`
**Template:** `templates/agent-registration.json`

Registration is not optional. An unregistered agent session is a governance violation.

---

## Commit Format (Non-Negotiable)

Every commit produced by an AI agent in any NeuroLift Technologies repository **must** follow this exact format:

```
[AGENT_NAME] type(scope): description
```

**Valid types:**
| Type | Use For |
|------|---------|
| `feat` | New features or capabilities |
| `fix` | Bug fixes |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring without behavior change |
| `chore` | Maintenance, tooling, governance tasks |
| `test` | Adding or updating tests |
| `ci` | CI/CD workflow changes |

**Agent name examples:** `CLAUDE`, `CODEX`, `GEMINI`, `CURSOR`, `COPILOT`

**Valid examples:**
```
[CLAUDE] feat(auth): add OAuth2 login flow
[CLAUDE] fix(api): resolve null pointer in user endpoint
[CODEX] chore(governance): add agent registration record
[GEMINI] docs(readme): update setup instructions
[CURSOR] test(utils): add unit tests for date helpers
```

**Invalid examples (never do these):**
```
✗  Add new feature
✗  [Claude] feat: something   (lowercase agent name)
✗  CLAUDE feat(auth): login   (missing brackets)
✗  Updated the login code     (no agent tag, no type)
```

---

## Escalation Protocol

### When to Escalate (mandatory — not optional)

Escalate to **Joshua W. Dorsey, Sr.** (`joshua@neurolift.tech`) before proceeding when the task involves:

| Trigger | Example |
|---------|---------|
| Architecture or system design decisions | "Should we use microservices or a monolith?" |
| New external service integrations | Adding Stripe, Twilio, a new LLM provider |
| LLM provider selection or lock-in | Choosing between OpenAI, Anthropic, Google |
| Production deployments | Anything that touches a live system |
| Changes to governance framework | Modifying OTOI, AGENTS.md, SOPs |
| Security-affecting changes | Auth, data access, encryption |
| Scope expansion beyond confirmed task | "While I'm here, I'll also refactor..." |
| Ambiguous requirements | When you genuinely don't know what's wanted |
| Ethical concerns | Privacy, bias, safety, misuse potential |

### How to Escalate

1. **Stop work** — do not proceed while the question is unresolved
2. **Document the blocker** in your handoff record (`blockers` field)
3. **File a GitHub Issue** using the `agent-escalation` issue template
4. **Email Joshua** at `joshua@neurolift.tech` with the issue URL
5. **Await explicit approval** before continuing

### When to Proceed Without Escalation

- The task is clearly within confirmed scope
- No architectural decisions are required
- No new external dependencies are introduced
- No production systems are affected
- The human has explicitly confirmed scope

---

## Multi-Agent Session Rules

When multiple agents are or have been active in the same repository:

1. **Read `docs/active-threads.md` first** — understand what is in progress before starting
2. **Do not overwrite another agent's in-progress work** without reading their handoff record
3. **Reference the active thread ID** in your commits and handoff records
4. **One agent owns one thread at a time** — do not split ownership without explicit handoff
5. **Update `docs/active-threads.md`** when you start or complete a thread

---

## Non-Negotiable Guardrails

These rules apply in every repository, at every time, without exception:

| Guardrail | Rule |
|-----------|------|
| **No credentials in VCS** | Never commit secrets, tokens, keys, or passwords |
| **No LLM lock-in** | Do not choose or hard-code an LLM provider without Joshua's approval |
| **No silent scope expansion** | Always confirm before expanding beyond the task |
| **No orphaned sessions** | Every session ends with a handoff record |
| **No production access without approval** | Escalate any production-touching change |
| **No governance changes unilaterally** | OTOI, AGENTS.md, and SOPs require Joshua's approval |

---

## Handoff Protocol

Per OTOI §5, **no session ends without a handoff record.**

**Handoff file location:** `docs/agent-log/handoffs/`
**File name format:** `{YYYY-MM-DD}-{session-id}.json`
**Template:** `templates/handoff-record.json`

A handoff must include:
- What was completed
- What is in progress
- Any blockers
- Decisions made and their rationale
- What the next agent needs to know
- All files modified
- Test status

A partial handoff is a failed handoff.

---

## Key Contacts and Resources

| Resource | Location |
|----------|----------|
| OTOI Contract | `.github-private/NLT-DEV-OTOI.md` |
| Onboarding SOP | `SOPs/new-agent-onboarding.md` |
| Active Threads | `docs/active-threads.md` |
| Agent Log | `docs/agent-log/` |
| Registration Template | `templates/agent-registration.json` |
| Handoff Template | `templates/handoff-record.json` |
| Escalation Template | `templates/escalation.md` |
| Escalation Contact | `joshua@neurolift.tech` |
| GitHub Escalation Issue | Use `ISSUE_TEMPLATE/agent-escalation.md` |

---

*This file is part of the ORG-DEV-OTOI-1.0.0 governance framework for NeuroLift Technologies.*
*Canonical source: `.github-private/AGENTS.md` · Synced to public `.github` repo*
