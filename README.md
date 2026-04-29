# Agent Solidarity Framework Development Kit (ASFDK)

**The Unified Agent Development Platform — The Layer Between the Model and the Agent**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OTOI Governance](https://img.shields.io/badge/governance-ORG--DEV--OTOI--1.0.0-green.svg)](https://github.com/NeuroLift-Technologies/nlt-otoi)
[![Solidarity Framework](https://img.shields.io/badge/framework-Solidarity-purple.svg)](https://github.com/NeuroLift-Technologies/solidarity-framework)

## Overview

The **Agent Solidarity Framework Development Kit (ASFDK)** is the unified agent development platform for NeuroLift Technologies. It serves as both the required governance and integration layer for all NLT agents **and** the operational hub for coding-agent infrastructure, Cloudflare-based agent development, and hosted tooling.

### Core Agent Framework

The ASFDK sits between the AI model and the agent, providing:

- **🚨 RRT Advocate** — Rapid Response Team for crisis intervention and immediate safety protocols
- **📋 NLT-OTOI Framework** — Terms of Interaction and Orchestrated Terms of Interaction for governance and user preferences
- **🌙 Sleepwalker Protocol (SWP)** — Emotional continuity governance for long-term safety across sessions
- **🎙️ VibeVoice** — Open-source frontier voice AI for speech recognition (ASR) and text-to-speech (TTS)

Every NLT agent **must** integrate this kit as its foundational layer.

### Coding-Agent Operations Hub

This repository also houses the org-wide infrastructure for all NLT coding agents:

- **🤖 Agent & Skill Profiles** (`agents/`) — Custom agent and skill definitions deployed across the org
- **📋 Governance SOPs & Templates** (`SOPs/`, `templates/`) — OTOI-compliant operating procedures and registration artifacts
- **⚙️ CI Workflows** (`.github/workflows/`) — Automated governance validation, commit-format enforcement, and security checks

### Cloudflare Agent Development

- **🔗 Agent Reference Links** (`links.md`) — Curated Cloudflare Workers, Agents SDK, Durable Objects, and MCP resources for NLT agent builds
- **🔌 MCP Server Configuration** (`mcp-config.yaml`) — Ready-to-use MCP server configs for GitHub and Cloudflare tooling
- **🌐 Hosting** (`hosting/`) — Web application layer for agent-facing interfaces

The Solidarity Framework ensures human safety, transparency, minimal footprint, and escalation culture across all of these layers.

## 🏗️ Architecture

### Solidarity Framework Layers

```
┌─────────────────────────────────────────────────────────────────┐
│     Agent Solidarity Framework Development Kit (ASFDK)          │
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

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Node.js 18+ (for Sleepwalker TypeScript components)
- Git with configured user credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NeuroLift-Technologies/solidarity-framework.git
   cd solidarity-framework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Agent Solidarity Kit**
   ```python
   from unified_core.neurolift_foundation import create_foundation, FoundationMode
   
   # Create and start the foundation
   foundation = await create_foundation(
       user_id="your_user_id",
       mode=FoundationMode.UNIFIED
   )
   ```

### Basic Usage

```python
import asyncio
from unified_core.neurolift_foundation import create_foundation

async def main():
    # Initialize the Agent Solidarity Kit
    foundation = await create_foundation("user_001")
    
    # Assess emotional state via Sleepwalker Protocol
    assessment = await foundation.assess_emotional_state(
        "I'm feeling overwhelmed today",
        context={"mood": "anxious", "energy": "low"}
    )
    print(f"Assessment: {assessment}")
    
    # Crisis support (if needed) via RRT Advocate
    crisis_response = await foundation.crisis_alert({
        "stress_level": "high",
        "indicators": ["overwhelmed", "panic"],
        "context": "work deadline pressure"
    })
    
    # Update preferences via NLT-OTOI
    await foundation.update_preferences({
        "toi_updates": {
            "crisis_response": {"privacy_level": "high"}
        }
    })
    
    # Get system status
    status = await foundation.get_system_status()
    print(f"System Status: {status}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 📁 Repository Structure

```
solidarity-framework/                    # Agent Solidarity Kit root
│
│  ── Core ASFDK Components ──────────────────────────────────────────────
├── rrt-advocate/                        # 🚨 Crisis intervention component
│   ├── src/rrt_advocate.py             # Core crisis intervention engine
│   ├── config/crisis_thresholds.yaml   # Crisis detection configuration
│   ├── docs/                           # RRT documentation
│   └── tests/                          # RRT test suite
├── nlt-otoi/                           # 📋 Interaction governance framework
│   ├── src/fusion/                     # TOI parser, OTOI orchestrator, privacy guardian
│   ├── schemas/                        # JSON schemas for TOI/OTOI
│   ├── templates/                      # TOI/charter templates
│   ├── docs/                           # OTOI documentation
│   └── examples/                       # Integration examples
├── sleepwalker/                        # 🌙 Emotional continuity protocol
│   ├── sleepwalker_protocol/           # Python implementation
│   ├── src/                            # TypeScript implementation
│   ├── examples/                       # Usage examples
│   └── tests/                          # SWP test suite
├── unified-core/                       # 🔧 Integration layer
│   ├── neurolift_foundation.py         # Main foundation class
│   ├── integration/                    # Component integrations
│   │   ├── rrt_integration.py
│   │   ├── toi_otoi_integration.py
│   │   └── sleepwalker_integration.py
│   ├── supervisor/                     # Supervisor AI coordination
│   └── coordination/                   # Cross-component coordination
│
│  ── Coding-Agent Operations Hub ────────────────────────────────────────
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
│  ── Cloudflare Agent Development ───────────────────────────────────────
├── links.md                            # 🔗 Cloudflare agent development references
├── mcp-config.yaml                     # 🔌 MCP server configurations (GitHub + Cloudflare)
├── hosting/                            # 🌐 Web application layer (Next.js)
│
│  ── Repository Root ────────────────────────────────────────────────────
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

```bash
# Run RRT Advocate tests
cd rrt-advocate && pytest tests/ -v

# Run Sleepwalker Protocol tests (Python)
cd sleepwalker && pytest tests/ -v

# Run Sleepwalker Protocol tests (TypeScript)
cd sleepwalker && npm test
```

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
**Platform**: ASFDK Core · Coding-Agent Ops Hub · Cloudflare Agent Development  
**Governance**: ORG-DEV-OTOI-1.0.0  
**Status**: 🟢 Active Development

*"Tech That Gets You, Nothing About Us Without Us, ElevAIte Your Mind"*
