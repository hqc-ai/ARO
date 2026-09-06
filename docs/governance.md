# Governance and human approval

Execution policy has three configurable levels:

| Level | Examples |
|---|---|
| `READ_ONLY` | process listing, socket inspection, metadata, logs, baseline comparison |
| `APPROVAL_REQUIRED` | quarantine, terminate, hosts changes, disable persistence, credential/session revocation |
| `AUTO_ALLOWED` | logging, hashing, evidence indexing, reports, policy-approved notifications |

Agents must not convert an observation into an action without a policy result. Material self-optimization follows **Observe → Evaluate → Propose → Benchmark/Test → Human Approve → Promote**.
