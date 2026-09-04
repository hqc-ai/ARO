# ARO Desktop vision

ARO Desktop is a future cross-platform shell for Windows, Linux, and macOS. It is deliberately not part of ver392026; the reusable Core/Runtime is the product foundation.

## Target experience

Download ARO → install → discover local resources and runtimes → add nodes/providers → register agents → scheduling begins → dashboard explains execution and efficiency.

Basic users should not need to understand Kubernetes, CUDA scheduling, or distributed systems. Advanced users can inspect policies, adapters, telemetry, and approval history.

## Discovery and adapters

Desktop will discover CPU, RAM, GPU/VRAM, Apple Silicon, storage, network, local AI runtimes, models, tools, and connected nodes. Planned adapters include Ollama, llama.cpp, MLX, FreeToken, OpenAI-compatible and Anthropic-compatible APIs, MCP, remote ARO Nodes, and cloud GPU providers. These remain providers behind interfaces, never hard-coded into Core.

## ARO Node protocol (proposal)

Nodes advertise a signed, expiring capability snapshot:

```json
{"node_id":"mac-mini-01","resources":{"cpu":4,"ram_gb":8,"gpu":false,"vram_gb":0,"storage_free_gb":400},"models":[],"tools":["log-store"],"workloads":["collection","normalization"],"health":"healthy","utilization":{"cpu":0.18}}
```

Control Plane actions are discover, register, heartbeat, lease, execute, report telemetry, and revoke. Authentication, transport, schema versioning, and attestation are deferred design work; the example is synthetic and not a security protocol.
