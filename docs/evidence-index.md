# Solidarity Framework evidence index

**Snapshot:** November 22, 2026. [ADR-001 v1.5.0](ADR-001.md) is the effective architecture baseline. Its [evidence boundaries](ADR-001.md#43-evidence-boundaries) distinguish source findings, reproductions, standalone conformance, integrated acceptance and verified deployed state. The index records each item at the level observed.

## Components, reviewed source and release artifacts

The source pins come from the ADR review record. The npm tarballs were listed by the public registry at the time of this snapshot. Package availability and reviewed source are separate evidence. The index establishes no package-to-commit provenance or release conformance.

| Component repository | Reviewed source | Published npm artifact | Scope of evidence |
|---|---|---|---|
| [TOI](https://github.com/NeuroLift-Technologies/nlt-toi) | [`730a16b`](https://github.com/NeuroLift-Technologies/nlt-toi/commit/730a16b39420f58cf3850d83b3fc44d8b93c45a1) | [1.0.3](https://registry.npmjs.org/@neurolift-technologies/toi/-/toi-1.0.3.tgz) | Reviewer reproduced selected behavior and ran standalone TypeScript and Python tests on a branch. |
| [OTOI](https://github.com/NeuroLift-Technologies/nlt-otoi) | [`036c8c0`](https://github.com/NeuroLift-Technologies/nlt-otoi/commit/036c8c0e3bb67f733a4239418a5011b137c589f9) | [1.2.0](https://registry.npmjs.org/@neurolift-technologies/otoi/-/otoi-1.2.0.tgz) | Selected unsigned-input behavior reproduced in both ports. Trusted-key and cross-port gates remain open. |
| [RRT AIdvocAIte](https://github.com/NeuroLift-Technologies/rrt-advocate) | [`da6184a`](https://github.com/NeuroLift-Technologies/rrt-advocate/commit/da6184ad29ff4082c564c5dbab8ff896099a3d42) | [0.1.1](https://registry.npmjs.org/@neurolift-technologies/rrt-advocate/-/rrt-advocate-0.1.1.tgz) | Scoped Python branch review with 110 passing and three failing tests. Worker behavior remains unverified by that review. |
| [Sleepwalker Protocol](https://github.com/NeuroLift-Technologies/sleepwalker) | [`95e9756`](https://github.com/NeuroLift-Technologies/sleepwalker/commit/95e97564db20c18aa4a427f8cb74984033cdc172) | [1.0.2](https://registry.npmjs.org/@neurolift-technologies/sleepwalker-protocol/-/sleepwalker-protocol-1.0.2.tgz) | Scoped Python branch probes and 41 passing tests. TypeScript source review only. |
| [SDL](https://github.com/NeuroLift-Technologies/nlt-sdl) | [`1a0ded8`](https://github.com/NeuroLift-Technologies/nlt-sdl/commit/1a0ded861397ab9cddca18307984499d73405bd7) | [1.0.0](https://registry.npmjs.org/@neurolift-technologies/sdl/-/sdl-1.0.0.tgz) | Supplemental source review. A 40-vector conformance run was reported and has not been independently rerun. |
| [ASFDK](https://github.com/NeuroLift-Technologies/asfdk) | [`24f546c`](https://github.com/NeuroLift-Technologies/asfdk/commit/24f546cf19c3dae3d5c0db02e714030e3d3dc041) | [0.2.4](https://registry.npmjs.org/@neurolift-technologies/asfdk/-/asfdk-0.2.4.tgz) | Reference code and tests cited in the ADR. [ASFDK PR #42](https://github.com/NeuroLift-Technologies/asfdk/pull/42) closed without merge. |
| [ASFDK Harness](https://github.com/NeuroLift-Technologies/asfdk-harness) | [`5384a12`](https://github.com/NeuroLift-Technologies/asfdk-harness/commit/5384a1224d784b4a334100325e6756c0c4117a5a) | Reviewed source [manifest](https://github.com/NeuroLift-Technologies/asfdk-harness/blob/5384a1224d784b4a334100325e6756c0c4117a5a/package.json) declares 0.1.0. No public npm entry was found under the manifest name or its organization-scoped equivalent. | Source review. Dependency resolution blocked test execution at the reviewed revision. |

## Integrated acceptance and deployment evidence

| Evidence | Status | Record |
|---|---|---|
| AT-001 A/B and the integrated acceptance matrix | In-process reference results are recorded. Integrated policy-to-provider acceptance remains unverified. | [Reference evidence](ADR-001.md#43-evidence-boundaries) · [ADR §5 acceptance and controls](ADR-001.md#5-end-to-end-acceptance-test-specification-approval-gate) |
| Adapter enforcement | The Harness source review covers specific adapters at a pinned commit. Per-operation activation and enforcement require runtime evidence. | [Harness review scope](ADR-001.md#41-review-receipts-and-limits) · [AT-RUNTIME-01 in the acceptance matrix](ADR-001.md#51-proposed-integrated-matrix) |
| Cloudflare Governance Worker, OI-10 | A November 22 read-only inspection verified deployed identity, configuration and deployed source for the inspected revision. An authenticated request and end-to-end enforcement were outside that inspection. | [OI-10 disposition and inspection summary](ADR-001.md#641-owner-approved-decision-closure-2026-11-22-owner--no-implementation-authorization) in the ADR. The detailed inspection receipt is internal. |

When adding evidence, record the source and artifact versions, runtime and adapter, operation and tested boundary, date, outcome and receipt. Use **configured** for settings, **activated** for a running control on the named surface and **enforced** only when an observed receipt establishes interception before execution or release. See [ADR §5](ADR-001.md#5-end-to-end-acceptance-test-specification-approval-gate) for positive and negative controls.
