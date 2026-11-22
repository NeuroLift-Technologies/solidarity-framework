# Solidarity Framework Documentation

```yaml
ai_assistant_directive:
  priority: 1
  instruction: "Before performing any development or coding tasks, read GOVERNANCE.md and follow its links to the organization contract."
  description: "NeuroLift Technologies maintains the public contributor contract in its .github repository."
  required_file: "GOVERNANCE.md"
```

**Canonical Documentation & Governance — Solidarity Framework · Agent Operations · Cloudflare Dev Resources**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OTOI Governance](https://img.shields.io/badge/governance-ORG--DEV--OTOI--1.0.4-green.svg)](https://github.com/NeuroLift-Technologies/nlt-otoi)
[![Solidarity Framework](https://img.shields.io/badge/framework-Solidarity-purple.svg)](https://github.com/NeuroLift-Technologies/solidarity-framework)

## Overview

The **solidarity-framework** repository is the canonical documentation and governance source for the NeuroLift Technologies Solidarity Framework. It defines the principles, operating procedures, component documentation, and agent-facing governance that NLT agents use when building or integrating Solidarity Framework systems.

The repository hosts the framework documentation, coding-agent governance and the Learning Center in [`app/`](app/).

### Coding-Agent Operations Documentation

This repository also houses documentation and governance infrastructure for NLT coding agents:

- **🤖 Agent & Skill Profiles** (`agents/`) — Custom agent and skill definitions deployed across the org
- **📋 Governance SOPs & Templates** (`SOPs/`, `templates/`) — OTOI-compliant operating procedures and registration artifacts
- **⚙️ CI Workflows** (`.github/workflows/`) — Automated governance validation and commit-format checks

### Cloudflare Agent Development

- **🔗 Agent Reference Links** (`links.md`) — Curated Cloudflare Workers, Agents SDK, Durable Objects, and MCP resources for NLT agent builds
- **🔌 MCP Server Configuration** (`mcp-config.yaml`) — Ready-to-use MCP server configs for GitHub and Cloudflare tooling

Human agency, transparency, a minimal footprint and escalation guide framework design.

> **How the Solidarity Framework is different:**
> MCP connects agents to tools. Agent-to-agent (A2A) connects agents to agents.
> The Solidarity Framework connects agent collaboration back to the user's declared terms.
>
> *— Positioning statement added 2026-05-19, session NLT-HND-2026-008*

## 🏗️ Architecture

The [architecture guide](docs/unified_architecture.md) explains the four pillars, their supporting components and the evidence required for enforcement claims.

| Pillar | Role | Component source |
|---|---|---|
| Terms of Interaction (TOI) | Human-authored preferences and authority constraints, with a canonical format and signing primitives. | [nlt-toi](https://github.com/NeuroLift-Technologies/nlt-toi) |
| Orchestrated Terms of Interaction (OTOI) | Resolves trusted TOI and decides policy, delegated grants, outbound release, retention, purge and direct governance notifications. | [nlt-otoi](https://github.com/NeuroLift-Technologies/nlt-otoi) |
| RRT AIdvocAIte | Protective response and immediate, bounded RED/BLACK direct support in the architecture. | [rrt-advocate](https://github.com/NeuroLift-Technologies/rrt-advocate) |
| Sleepwalker Protocol | Independent continuity assurance and drift monitoring against OTOI requirements. | [sleepwalker](https://github.com/NeuroLift-Technologies/sleepwalker) |

The [State Detection Layer (SDL)](https://github.com/NeuroLift-Technologies/nlt-sdl) supplies advisory observations. The [Agent Solidarity Framework Deployment Kit (ASFDK)](https://github.com/NeuroLift-Technologies/asfdk) integrates component interfaces. The [ASFDK Harness](https://github.com/NeuroLift-Technologies/asfdk-harness) applies OTOI decisions at supported runtime boundaries. These supporting components sit alongside the four pillars.

## Using the framework

Start with the component source above for release-specific installation instructions, APIs and coverage. Use the Learning Center to explore the architecture. Its examples explain component roles.

## 📁 Repository Structure

```
solidarity-framework/                    # Solidarity Framework docs/governance root
│
│  -- Component implementations are NOT vendored here -------------------------
│     Each pillar lives in its own repo and ships to npm. See "Component
│     Sources" above (TOI, OTOI, RRT Advocate, Sleepwalker) and the
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
│   ├── README.md
│   ├── contracts/README.md
│   ├── proposals/validation-roadmap.md
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
├── GOVERNANCE.md                      # Organization contract and local requirements
├── CONTRIBUTING.md                     # Contribution guidelines
├── CODE_OF_CONDUCT.md                  # Community standards
├── SECURITY.md                         # Security policy
├── SUPPORT.md                          # Support guide
├── LICENSE                             # Apache 2.0
└── README.md                           # This file
```

## 🔐 Governance (ORG-DEV-OTOI-1.0.4)

The [NeuroLift Technologies public governance contract](GOVERNANCE.md) applies to contributors to this repository.

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

Run repository governance checks with `bash .nltotoi/scripts/validate-governance.sh --strict`. For the Learning Center, use Node 24 and run:

```bash
cd app
npm ci
npm run lint
npm run build
```

Component test suites live in their respective repositories.

## Privacy & Security

The framework architecture requires data minimization and prohibits persistence of raw conversations, prompts, responses, transcripts and user-linked crisis profiles. OTOI decides eligibility, retention duration and purge requirements. Check the [architecture guide](docs/unified_architecture.md#continuity-and-data) for the continuity boundary and the component release for implementation evidence.

### Solidarity Framework Principles

1. **Transparency** — Record governance evidence with the minimum data needed
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
**Components**: TOI, OTOI, RRT Advocate, Sleepwalker Protocol  
**Repository Role**: Documentation · Governance · Coding-Agent Ops Documentation · Cloudflare Agent Development
**Governance**: ORG-DEV-OTOI-1.0.4
**Status**: 🟢 Active Development

*"Tech That Gets You, Nothing About Us Without Us, ElevAIte Your Mind"*
