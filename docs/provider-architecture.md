# Provider architecture

ARO exposes ports in `aro/providers.py`: `ResourceProvider`, `ExecutionBackend`, `ModelProvider`, `ToolProvider`, `TelemetryProvider`, `PolicyPlugin`, and `AgentAdapter`.

An OpenAI-compatible endpoint can be configured as one provider rather than receiving a vendor-specific scheduler branch. Planned adapters include OpenAI, Anthropic, Gemini, Bedrock, Ollama, vLLM, FreeToken-compatible endpoints, MLX, MCP, remote ARO Nodes, filesystem/API connectors, and messaging. FreeToken can be an execution backend selected for a GPU node; ARO does not vendor or copy its implementation.
