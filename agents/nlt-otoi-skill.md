---
name: NLT-OTOI Skill
description: Guidance for resolving Terms of Interaction authority and applying Orchestrated Terms of Interaction policy.
version: 1.0.0
nlt-otoi-version: ORG-DEV-OTOI-1.0.4
nlt-solidarity-framework: true
nlt-haief: true
nlt-authority: Joshua W. Dorsey, Sr.
skill-component: nlt-otoi
skill-type: standalone
adoption-tier: component
---

# NLT-OTOI Skill

Follow [repository governance](../GOVERNANCE.md) and ORG-DEV-OTOI-1.0.4.

## Role

Guide adopters of Orchestrated Terms of Interaction (OTOI). The Terms of Interaction (TOI) project supplies the canonical format, generator and signing primitives. OTOI alone resolves TOI authority during operation against a trusted, human-bound signing key and mandatory guardrails. Treat an absent, invalid or untrusted TOI as providing no TOI-derived authority under the architecture.

OTOI decides policy, delegated grants, outbound release, retention and purge. For a governance conflict that requires the person's attention, OTOI issues a notice for direct delivery by a supported host. Delivery or dismissal conveys no authorization. The ASFDK Harness applies decisions at the runtime boundaries supported by the adapter.

## Adoption and escalation

Use the [nlt-otoi repository](https://github.com/NeuroLift-Technologies/nlt-otoi) for version-specific installation, API and compatibility guidance. Keep implementation claims tied to the exact release and runtime. Escalate unresolved governance conflicts, proposed changes to policy or trust rules, and new providers or storage integrations to Joshua W. Dorsey, Sr. Preserve the original TOI and limit diagnostics to what the receiver is authorized to see.
