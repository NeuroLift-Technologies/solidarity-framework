# Solidarity Framework architecture

The Solidarity Framework connects a person's declared terms to decisions about agent actions and information sharing. Its four pillars can be adopted independently. The responsibilities below reflect the effective ADR-001 v1.5.0 architecture baseline. Check the component's own release documentation before relying on an interface.

## Four pillars

| Pillar | Responsibility | Source |
|---|---|---|
| Terms of Interaction (TOI) | The person declares interaction preferences, boundaries and authority constraints. TOI defines the document format, generator and signing primitives. | [nlt-toi](https://github.com/NeuroLift-Technologies/nlt-toi) |
| Orchestrated Terms of Interaction (OTOI) | Resolves TOI authority during operation, applies mandatory guardrails, scopes delegated grants, and decides retention, purge and what can be shared. It issues governance notifications for direct delivery to the person through supported hosts. | [nlt-otoi](https://github.com/NeuroLift-Technologies/nlt-otoi) |
| RRT AIdvocAIte (RRTA) | Provides protective response and escalation. The RED/BLACK design keeps immediate direct support available within the current interaction, without delegation, external tools or storage. | [rrt-advocate](https://github.com/NeuroLift-Technologies/rrt-advocate) |
| Sleepwalker Protocol | Independently monitors continuity and protective drift against OTOI-resolved retention and purge requirements. | [sleepwalker](https://github.com/NeuroLift-Technologies/sleepwalker) |

## Supporting components

| Component | Responsibility | Source |
|---|---|---|
| State Detection Layer (SDL) | Observes state and emits advisory signals. The receiving component makes the decision. | [nlt-sdl](https://github.com/NeuroLift-Technologies/nlt-sdl) |
| Agent Solidarity Framework Deployment Kit (ASFDK) | Integrates component interfaces for deployment. OTOI owns policy decisions. | [asfdk](https://github.com/NeuroLift-Technologies/asfdk) |
| ASFDK Harness | Applies OTOI decisions at supported runtime boundaries. Enforcement claims need evidence for the adapter, operation and version in use. | [asfdk-harness](https://github.com/NeuroLift-Technologies/asfdk-harness) |

## Authority and disclosure

A signature verifies integrity against a key. Operational authority requires OTOI to verify that the key is trusted and bound to the person who authorized it. A delegated grant stays within the parent's scope and any applicable receiver and policy constraints. A separately authorized action or input contributes no automatic approval to release a combined output. The Harness design checks policy before dispatch and before outbound release where the runtime can intercept those operations.

OTOI directs applicable governance notices to the human through the host. Delivery or dismissal carries no operational authority. SDL signals inform protective response. The design calls for RRTA to send authenticated RED/BLACK escalation events to OTOI for revocation and purge decisions, while RRTA provides immediate direct support independently.

## Continuity and data

The framework's data boundary excludes raw conversations, prompts, responses, transcripts and user-linked crisis profiles from persistence. Minimized user-linked governance records require explicit consent and finite retention controlled by OTOI. Sleepwalker monitors adherence to those requirements. Its local-first runtime continuity store and the voluntary public Continuity submission service have distinct purposes and consent boundaries.

## Deployment evidence

Use the [evidence index](evidence-index.md) to find reviewed revisions, artifacts, acceptance controls and deployment observations. Record the component revision, adapter and operation whenever reporting runtime coverage. A configured control has settings, an activated control is running on the named surface, and an enforced control has evidence that it intercepted the operation before execution or release. A package install or a Learning Center playground session establishes neither a runtime coverage result nor deployment readiness.
