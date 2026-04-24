# NeuroLift Agent Solidarity Kit - Unified Architecture Design

## Overview

The Agent Solidarity Kit integrates three core components into a unified layer between the AI model and the agent:

1. **RRT Advocate** — Crisis intervention and immediate safety (protective layer)
2. **NLT-OTOI** — Terms of Interaction and Orchestrated Terms of Interaction (constitutional layer)
3. **Sleepwalker Protocol (SWP)** — Emotional continuity across sessions (continuity layer)

A **unified core** coordinates these components, with Supervisor AI and internal state/communication helpers. This design evolved from NeuroLift’s core product work and is the shared base for NLT agents.

## Architectural principles

- **Privacy-first** — Local processing and user-controlled data where applicable  
- **Solidarity Framework** — Transparency, minimal footprint, escalation culture, human flourishing, agency preservation  
- **Modular integration** — Each component keeps a clear boundary and integration surface  
- **Scalable** — New Advocates can be added without rewriting the whole stack  

## Component integration

### RRT Advocate

Real-time stress/crisis assessment, tiered response, escalation. Integrated via `unified_core.integration.rrt_integration` and the vendored `rrt-advocate` implementation.

### NLT-OTOI

TOI/OTOI preference and optimization flow. Integrated via `unified_core.integration.toi_otoi_integration`. The integration may ingest **RRT crisis context** through `ingest_rrt_crisis_context` when the communication layer routes messages (no external voice engine).

### Sleepwalker Protocol

Long-horizon emotional continuity. Integrated via `unified_core.integration.sleepwalker_integration`.

## Unified core

- **`NeuroLiftFoundation`** (`unified_core/neurolift_foundation.py`) — Main coordinator  
- **`SupervisorAI`** — Cross-advocate coordination  
- **`UnifiedStateManager` / `ComponentCommunication`** — State and inter-component message routing (see `unified_core/core_coordination/`)  

## Data flow (high level)

```text
User / agent request
       │
       ▼
 Unified core (NeuroLiftFoundation)
       ├── RRT Advocate (acute safety)
       ├── NLT-OTOI (governance & optimization)
       ├── Sleepwalker (continuity)
       └── Supervisor (coordination)
```

## Upstream component sync

Components such as `rrt-advocate/`, `nlt-otoi/`, and `sleepwalker/` are often maintained as **git subtrees** or submodules. Sync procedures live with your team’s release process; this repo no longer includes an Aimybox or separate voice runtime subtree.

## Future expansion

Additional **Advocates** can register with Supervisor AI and plug into the same communication and state contracts without changing the core three-component model.
