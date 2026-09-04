# Plugin architecture

Community adapters should implement stable ports without editing ARO Core:

| Interface | Responsibility |
|---|---|
| `ResourceProvider` | discover resources, health, utilization, and capabilities |
| `ExecutionBackend` | execute a routed task and return a normalized result |
| `ModelProvider` | list models and model capabilities |
| `ToolProvider` | list and invoke tools/MCP services |
| `TelemetryProvider` | persist or export telemetry |
| `PolicyPlugin` | contribute auditable allow/deny constraints |
| `AgentAdapter` | translate external agent events into ARO tasks |

The current `Resource`, `Task`, `Telemetry`, `PolicyEngine`, and `AdaptiveScheduler` objects are intentionally small ports. Future packages can wrap Ollama, llama.cpp, MLX, FreeToken, API providers, MCP, remote nodes, databases, vector stores, and cloud compute.
