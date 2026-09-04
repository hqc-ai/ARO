# Technical decisions intentionally deferred

- Durable database and telemetry retention format.
- Authentication, encryption, node identity, and capability attestation.
- Process isolation and sandboxing for third-party tools.
- Exact REST/OpenAPI and streaming event schema.
- Desktop framework and packaging/update channel.
- Provider-specific licensing and model download UX.
- Distributed queue protocol, leases, retries, and exactly-once semantics.
- Benchmark methodology and quality evaluation contracts.
- Production SLA, multi-tenant isolation, and enterprise access control.

These are deferred deliberately so ver392026 can validate orchestration behavior without prematurely coupling the Core to a deployment vendor or UI framework.
