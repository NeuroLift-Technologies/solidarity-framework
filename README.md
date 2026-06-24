# Solidarity Framework Documentation

```yaml
ai_assistant_directive:
  priority: 1
  instruction: "Before performing any development or coding tasks, read NLT-DEV-OTOI.md."
  description: "NLT-DEV-OTOI.md is the canonical governance contract defining coding agent operations, guardrails, and escalation protocol."
  required_file: "NLT-DEV-OTOI.md"
```

**Canonical Documentation & Governance — Solidarity Framework · Agent Operations · Cloudflare Dev Resources**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OTOI Governance](https://img.shields.io/badge/governance-ORG--DEV--OTOI--1.0.0-green.svg)](https://github.com/NeuroLift-Technologies/nlt-otoi)
[![Solidarity Framework](https://img.shields.io/badge/framework-Solidarity-purple.svg)](https://github.com/NeuroLift-Technologies/solidarity-framework)

## Overview

The **solidarity-framework** repository is the canonical documentation and governance source for the NeuroLift Technologies Solidarity Framework. It defines the principles, operating procedures, component documentation, and agent-facing governance that NLT agents use when building or integrating Solidarity Framework systems.

The **Agent Solidarity Framework Development Kit (ASFDK)** is a separate implementation/development-kit repository. This repo may document ASFDK architecture and integration expectations, but it is not the ASFDK source repo.

### Core Agent Framework

The Solidarity Framework defines the layer between the AI model and the agent, including:

- **🚨 RRT Advocate** — Rapid Response Team for crisis intervention and immediate safety protocols
- **📋 NLT-OTOI Framework** — Terms of Interaction and Orchestrated Terms of Interaction for governance and user preferences
- **🌙 Sleepwalker Protocol (SWP)** — Emotional continuity governance for long-term safety across sessions
- **🎙️ VibeVoice** — Open-source frontier voice AI for speech recognition (ASR) and text-to-speech (TTS)

Every NLT agent **must** follow the Solidarity Framework governance model and use the relevant implementation repositories for deployable components.

### Coding-Agent Operations Documentation

This repository also houses documentation and governance infrastructure for NLT coding agents:

- **🤖 Agent & Skill Profiles** (`agents/`) — Custom agent and skill definitions deployed across the org
- **📋 Governance SOPs & Templates** (`SOPs/`, `templates/`) — OTOI-compliant operating procedures and registration artifacts
- **⚙️ CI Workflows** (`.github/workflows/`) — Automated governance validation, commit-format enforcement, and security checks

### Cloudflare Agent Development

- **🔗 Agent Reference Links** (`links.md`) — Curated Cloudflare Workers, Agents SDK, Durable Objects, and MCP resources for NLT agent builds
- **🔌 MCP Server Configuration** (`mcp-config.yaml`) — Ready-to-use MCP server configs for GitHub and Cloudflare tooling

The Solidarity Framework ensures human safety, transparency, minimal footprint, and escalation culture across all of these layers.

> **How the Solidarity Framework is different:**
> MCP connects agents to tools. Agent-to-agent (A2A) connects agents to agents.
> The Solidarity Framework connects agent collaboration back to the user's declared terms.
>
> *— Positioning statement added 2026-05-19, session NLT-HND-2026-008*

## 🏗️ Architecture

### Solidarity Framework Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                  Solidarity Framework                           │
│          "The Layer Between the Model and the Agent"             │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │ RRT Advocate      │  │ NLT-OTOI         │  │ Sleepwalker   │ │
│  │ (Protective)      │◄─┤ (Constitutional) │◄─┤ (Continuity)  │ │
│  │                   │  │                  │  │               │ │
│  │ • Crisis Detection│  │ • TOI Governance │  │ • Emotional   │ │
│  │ • Emergency       │  │ • OTOI Orchestr. │  │   State       │ │
│  │   Response        │  │ • Privacy Guard  │  │   Detection   │ │
│  │ • Tiered Alerts   │  │ • User Prefs     │  │ • Session     │ │
│  │ • Agency Preserv. │  │ • Multi-Agent    │  │   Continuity  │ │
│  └──────────────────┘  └──────────────────┘  └───────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                      VibeVoice (Voice Layer)                     │
│  ┌──────────────────────────┐  ┌──────────────────────────────┐ │
│  │ VibeVoice-ASR-7B          │  │ VibeVoice-Realtime-0.5B      │ │
│  │ (Speech Recognition)      │  │ (Text-to-Speech Streaming)   │ │
│  └──────────────────────────┘  └──────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                        Unified Core                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │ Supervisor AI     │  │ Component Comms  │  │ State Manager │ │
│  └──────────────────┘  └──────────────────┘  └───────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Component Sources

| Component | Repository | Purpose |
|-----------|-----------|---------|
| **RRT Advocate** | [`NeuroLift-Technologies/rrt-advocate`](https://github.com/NeuroLift-Technologies/rrt-advocate) | Crisis intervention & safety |
| **NLT-OTOI** | [`NeuroLift-Technologies/nlt-otoi`](https://github.com/NeuroLift-Technologies/nlt-otoi) | Interaction governance & orchestration |
| **Sleepwalker** | [`NeuroLift-Technologies/sleepwalker`](https://github.com/NeuroLift-Technologies/sleepwalker) | Emotional continuity across sessions |
| **VibeVoice** | [`NeuroLift-Technologies/VibeVoice`](https://github.com/NeuroLift-Technologies/VibeVoice) | Voice AI — ASR (speech recognition) & TTS (speech synthesis) |

## 🚀 Using the Framework

This repository is **documentation and governance only** — it no longer vendors
the component implementations. Each Solidarity Framework pillar ships from its own
repository and is published to npm (see [Component Sources](#component-sources)
above). To build or integrate, install the packages directly.

### Reference implementation kit — ASFDK

The fastest way to wire all four pillars together is the **Agent Solidarity
Framework Development Kit** ([`NeuroLift-Technologies/asfdk`](https://github.com/NeuroLift-Technologies/asfdk)),
which provides both a Python `unified_core` kit and a TypeScript umbrella package
that depends on the four pillars:

```bash
npm install @neurolift-technologies/asfdk
```

```ts
import { createFoundation, FoundationMode } from '@neurolift-technologies/asfdk';

// The orchestrator routes interactions through the active pillars for a mode.
const foundation = await createFoundation('user_001', FoundationMode.UNIFIED);
const status = foundation.getSystemStatus();
```

### Individual pillar packages

| Pillar | npm package |
|---|---|
| TOI | `@neurolift-technologies/toi` |
| OTOI | `@neurolift-technologies/otoi` |
| RRT Advocate (⚠️ prototype) | `@neurolift-technologies/rrt-advocate` |
| Sleepwalker Protocol | `@neurolift-technologies/sleepwalker-protocol` |

For Python usage and the canonical reference foundation, see the
[`asfdk`](https://github.com/NeuroLift-Technologies/asfdk) and per-component
repositories linked in [Component Sources](#component-sources).

## 📁 Repository Structure

```
solidarity-framework/                    # Solidarity Framework docs/governance root
│
│  -- Component implementations are NOT vendored here -------------------------
│     Each pillar lives in its own repo and ships to npm. See "Component
│     Sources" above (RRT Advocate, NLT-OTOI, Sleepwalker, VibeVoice) and the
│     reference kit at NeuroLift-Technologies/asfdk.
│
│  -- Coding-Agent Operations Hub ---------------------------------------------
├── agents/                             # 🤖 Org-wide agent & skill profiles
│   ├── nlt-governance-steward.md      # OTOI compliance & guidance agent
│   ├── rrt-advocate-skill.md          # RRT Advocate skill definition
│   ├── nlt-otoi-skill.md              # NLT-OTOI skill definition
│   ├── sleepwalker-skill.md           # Sleepwalker skill definition
│   ├── solidarity-foundation-skill.md # Unified Foundation skill definition
│   └── swe-agent.md                   # Senior software engineer agent
├── docs/                               # 📚 Governance documentation
│   ├── active-threads.md              # Current work state
│   └── agent-log/                     # Agent session audit trail
├── SOPs/                               # 📋 Standard operating procedures
│   ├── new-agent-onboarding.md        # SOP-NLT-001
│   ├── repo-governance-setup.md       # SOP-NLT-002
│   └── incident-response.md           # SOP-NLT-003
├── templates/                          # 📝 Governance templates
│   ├── agent-registration.json
│   ├── handoff-record.json
│   ├── escalation.md
│   └── intent-log.md
├── ISSUE_TEMPLATE/                     # 🎫 Issue templates
│   ├── agent-escalation.md
│   ├── governance-proposal.md
│   ├── bug_report.md
│   └── feature_request.md
├── .nltotoi/                           # 🔒 Governance infrastructure
│   ├── index/governance-files.md
│   └── scripts/validate-governance.sh
├── .github/                            # ⚙️ GitHub configuration & CI workflows
│   ├── copilot-instructions.md
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
│
│  -- Cloudflare Agent Development --------------------------------------------
├── links.md                            # 🔗 Cloudflare agent development references
├── mcp-config.yaml                     # 🔌 MCP server configurations (GitHub + Cloudflare)
│
│  -- Repository Root ---------------------------------------------------------
├── AGENTS.md                           # Agent coordination protocol
├── CLAUDE.md                           # AI assistant guide (OTOI compliant)
├── NLT-DEV-OTOI.md                    # Org-level coding agent contract
├── CONTRIBUTING.md                     # Contribution guidelines
├── CODE_OF_CONDUCT.md                  # Community standards
├── SECURITY.md                         # Security policy
├── SUPPORT.md                          # Support guide
├── LICENSE                             # Apache 2.0
└── README.md                           # This file
```

## 🔐 Governance (ORG-DEV-OTOI-1.0.0)

This repository is governed by **ORG-DEV-OTOI-1.0.0** — the NeuroLift Technologies Orchestrated Terms of Interaction contract.

### For AI Agents

All coding agents working in this repository **must**:

1. Read `CLAUDE.md` for repo-specific context
2. Read `AGENTS.md` for coordination protocol
3. Read `docs/active-threads.md` to avoid work conflicts
4. Self-register using `templates/agent-registration.json`
5. Follow commit format: `[AGENT_NAME] type(scope): description`
6. Escalate to **Joshua W. Dorsey, Sr.** when required

### Escalation Triggers

Escalate immediately when:
- Task scope is unclear or conflicts with existing work
- An architectural or deployment decision is required
- A blocker cannot be resolved by the agent
- An ethical concern arises
- A production deployment is being considered

**Escalation Authority**: Joshua W. Dorsey, Sr. (`info@neuroliftsolutions.com`)

## 🧪 Testing

This is a documentation/governance repo and carries no component test suites.
Each pillar's tests live in its own repository:

- RRT Advocate — [`NeuroLift-Technologies/rrt-advocate`](https://github.com/NeuroLift-Technologies/rrt-advocate)
- NLT-OTOI — [`NeuroLift-Technologies/nlt-otoi`](https://github.com/NeuroLift-Technologies/nlt-otoi)
- Sleepwalker Protocol — [`NeuroLift-Technologies/sleepwalker`](https://github.com/NeuroLift-Technologies/sleepwalker)
- Reference kit (ASFDK) — [`NeuroLift-Technologies/asfdk`](https://github.com/NeuroLift-Technologies/asfdk)

## 🔐 Privacy & Security

### Privacy-First Design

- **Local Processing**: Core functionality operates locally without external dependencies
- **Encrypted Storage**: All user data encrypted at rest and in transit
- **Minimal Data Collection**: Only essential data collected for functionality
- **User Control**: Complete user control over data sharing and retention

### Solidarity Framework Principles

1. **Transparency** — All agent actions are logged and auditable
2. **Minimal Footprint** — Agents only modify what is necessary
3. **Escalation Culture** — When in doubt, escalate to human authority
4. **Human Flourishing** — Technology serves people, not the other way around
5. **Privacy First** — Local-only processing wherever possible
6. **Agency Preservation** — User autonomy is never overridden

## 📄 License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NeuroLift Technologies** — Core AI-fusion framework and methodology
- **Human & AI ElevAItion Foundation (HAIEF)** — Governance standards
- **ADHD Community** — Feedback and real-world testing
- **Open Source Contributors** — Various libraries and tools

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/NeuroLift-Technologies/solidarity-framework/issues)
- **Security**: See [SECURITY.md](SECURITY.md) for vulnerability reporting
- **Email**: info@neuroliftsolutions.com

---

**Framework Version**: 2.0.0  
**Components**: RRT Advocate, NLT-OTOI Framework, Sleepwalker Protocol, VibeVoice  
**Repository Role**: Documentation · Governance · Coding-Agent Ops Documentation · Cloudflare Agent Development
**Governance**: ORG-DEV-OTOI-1.0.0  
**Status**: 🟢 Active Development

*"Tech That Gets You, Nothing About Us Without Us, ElevAIte Your Mind"*
