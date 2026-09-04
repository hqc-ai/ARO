# ARO architecture

ARO keeps registries and decision interfaces separate from execution adapters. An adapter may expose a local model, API, tool, MCP service, database, vector store, or compute node as a `Resource` without changing scheduling logic.

```mermaid
flowchart TB
 R[Agent Registry] --> Q[Task Queue]
 E[Event Bus] --> P[Task Profiler]
 Q --> P --> Policy[Policy Engine]
 Policy --> S[Adaptive Scheduler]
 RP[Resource Profiler / Registry] --> S
 S --> X[Execution Router]
 M[Model Registry] --> X
 T[Tool Registry] --> X
 X --> Tel[Telemetry Collector]
 Tel --> H[Performance History]
 H --> Rec[Recommendation Engine]
 Rec --> Gate[Human Approval Gate]
 Gate --> Policy
```

The production-safe optimization loop is **Observe → Evaluate → Propose → Benchmark/Test → Human Approve → Promote**. ARO never silently changes production policy.

## Lifecycles

```mermaid
stateDiagram-v2
 [*] --> queued
 queued --> running: scheduler selects
 queued --> deferred: incident / policy
 queued --> waiting: no compatible resource
 running --> completed: execution succeeds
 running --> failed: execution error
 deferred --> queued: incident cleared
```

```mermaid
sequenceDiagram
 participant W as Watch Agent
 participant B as Event Bus
 participant I as Incident Manager
 participant S as Scheduler
 W->>B: anomaly event
 B->>I: create incident
 I->>S: raise priority
 S->>S: defer low-value work
 S-->>I: route evidence / IOC / timeline / investigation
 S->>B: telemetry
```

## Scheduling signals

Task type, priority, privacy, latency, reasoning, context size, expected runtime, current CPU/RAM/GPU/VRAM/I/O/network, availability, model/tool availability, history, API cost, and cloud availability are intended inputs. The demo implements a small deterministic subset and is designed for extension.
