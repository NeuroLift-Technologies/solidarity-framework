# CLAUDE.md — NeuroLift-Technologies/solidarity-framework
> OTOI Compliance File · ORG-DEV-OTOI-1.0.0 · Step 3 of Agent Onboarding (SOP-NLT-001)

---

## Repository Identity

| Field              | Value                                                     |
|--------------------|-----------------------------------------------------------|
| **Repository**     | `NeuroLift-Technologies/solidarity-framework`              |
| **Visibility**     | Private                                                    |
| **Purpose**        | Solidarity Framework documentation and governance source: framework principles, component documentation, coding-agent operations, and Cloudflare agent development resources |
| **OTOI Version**   | ORG-DEV-OTOI-1.0.0                                        |
| **Governing SOP**  | SOP-NLT-001 (`SOPs/new-agent-onboarding.md`)              |
| **Components**     | RRT Advocate, NLT-OTOI, Sleepwalker Protocol, VibeVoice, Agent Ops Documentation, Cloudflare Dev Resources |

---

## Purpose of This Repository

The **solidarity-framework** repository is the canonical documentation and governance source for the NeuroLift Technologies Solidarity Framework. It is distinct from the **Agent Solidarity Framework Development Kit (ASFDK)** implementation/development-kit repository.

This repo serves three interconnected purposes:

### 1. Framework Component Documentation
Component implementations are **not vendored here** — each pillar lives in its own
repository and ships to npm. This repo documents them; integrate from source:
- **RRT Advocate** — Crisis intervention and immediate safety protocols — [`NeuroLift-Technologies/rrt-advocate`](https://github.com/NeuroLift-Technologies/rrt-advocate) · npm `@neurolift-technologies/rrt-advocate`
- **NLT-OTOI Framework** — Interaction governance and orchestration — [`NeuroLift-Technologies/nlt-otoi`](https://github.com/NeuroLift-Technologies/nlt-otoi) · npm `@neurolift-technologies/otoi` (and `@neurolift-technologies/toi`)
- **Sleepwalker Protocol** — Emotional continuity across sessions — [`NeuroLift-Technologies/sleepwalker`](https://github.com/NeuroLift-Technologies/sleepwalker) · npm `@neurolift-technologies/sleepwalker-protocol`
- **VibeVoice** — Open-source frontier voice AI (ASR + TTS) — see [`NeuroLift-Technologies/VibeVoice`](https://github.com/NeuroLift-Technologies/VibeVoice)
- **Unified Core / reference kit** — Integration layer connecting all pillars — [`NeuroLift-Technologies/asfdk`](https://github.com/NeuroLift-Technologies/asfdk) (Python `unified_core` + npm `@neurolift-technologies/asfdk`)

### 2. Coding-Agent Operations Documentation
- **Agent & Skill Profiles** (`agents/`) — Org-wide custom agent and skill definitions
- **Governance SOPs** (`SOPs/`) — Standard operating procedures for agent onboarding, repo setup, and incident response
- **Templates** (`templates/`) — OTOI-compliant registration and handoff artifacts
- **CI Workflows** (`.github/workflows/`) — Automated governance validation and enforcement

### 3. Cloudflare Agent Development Platform
- **Agent Reference Links** (`links.md`) — Curated Cloudflare Workers, Agents SDK, and MCP resources
- **MCP Server Configuration** (`mcp-config.yaml`) — Ready-to-use GitHub and Cloudflare MCP configs

All agents developed by NeuroLift Technologies **must** follow the governance documented here and use the appropriate implementation repositories for runtime integration.

---

## What Agents May and May Not Do Here

This is a **documentation and governance** repository — it contains no component
source code. Implementation changes belong in the component repos linked above.

### ✅ In Scope (proceed after task confirmation)
- Update framework/component **documentation** (this repo describes the pillars; it does not implement them)
- Update governance tracking files in `docs/active-threads.md`
- Add agent registration and handoff records to `docs/agent-log/`
- Update agent & skill profiles in `agents/`, SOPs in `SOPs/`, templates in `templates/`
- Update Cloudflare dev resources (`links.md`, `mcp-config.yaml`)
- Minor documentation improvements (typos, clarity, formatting)

### 🔴 Out of Scope — Escalate to Joshua W. Dorsey, Sr.
- Modifying the governance framework itself (OTOI, AGENTS.md, SOPs)
- Implementation changes to any pillar — those belong in the component repos (`rrt-advocate`, `nlt-otoi`, `nlt-toi`, `sleepwalker`, `asfdk`), not here
- Introducing new external service integrations or LLM provider dependencies
- Architectural decisions about component interaction patterns
- Documenting crisis intervention logic or thresholds in a way that changes intended behavior (escalate; the source of truth is `NeuroLift-Technologies/rrt-advocate`)
- Production deployment decisions
- Changes to the Solidarity Framework principles

---

## Additional Required Reading (Step 3 checklist)

Before beginning work, confirm you have read:

- [ ] `NLT-DEV-OTOI.md` — repo-local governance contract (read first)
- [ ] `AGENTS.md` — coordination gateway and guardrails
- [ ] `SOPs/new-agent-onboarding.md` — onboarding process SOP-NLT-001
- [ ] `docs/active-threads.md` — current work in progress

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
[CLAUDE] docs(components): repoint pillar references to canonical repos
[COPILOT] docs(sops): clarify onboarding step 3
[CODEX] docs(readme): update architecture diagram
```

### Technology Stack
This is a **documentation/governance** repo — Markdown-first, no application code.
- **Markdown** — Documentation, SOPs, agent/skill profiles, governance
- **YAML / JSON** — `mcp-config.yaml`, governance templates, `.nltotoi/` config
- Component implementations use their own stacks — see each component repo.

### Key Files
- `NLT-DEV-OTOI.md` / `AGENTS.md` — governance contract & coordination gateway
- `agents/` — org-wide agent & skill profiles (incl. the pillar skill docs)
- `SOPs/` — standard operating procedures (onboarding, repo setup, incident response)
- `templates/` — OTOI registration, handoff, escalation, intent-log artifacts
- `docs/active-threads.md` — current work state; `docs/agent-log/` — session audit trail
- `links.md` / `mcp-config.yaml` — Cloudflare agent development resources

---

## Escalation

**Primary escalation contact:** Joshua W. Dorsey, Sr.
**Email:** `info@neuroliftsolutions.com`
**Use the escalation template:** `templates/escalation.md`
**Or file a GitHub Issue:** Use the `agent-escalation` issue template

When in doubt, escalate. It is always better to pause than to guess.

---

*This file is part of the ORG-DEV-OTOI-1.0.0 governance framework for NeuroLift Technologies.*
