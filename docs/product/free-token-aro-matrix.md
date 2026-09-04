# FreeToken → ARO design matrix

| Principle | FreeToken focus | ARO generalization |
|---|---|---|
| Heterogeneous pooling | CPU, GPU, host memory, interconnect | Any node, tool, model, API, storage, or cloud capability |
| Profiling | Hardware and bandwidth | Task demand plus resource, policy, cost, and history |
| Adaptive scheduling | Runtime model execution | Agent/task route selection and priority |
| Telemetry | Inference/runtime signals | Queue, execution, resource, cost, and quality signals |
| Dynamic allocation | Cache and memory efficiency | Preemption, defer, escalation, and shared model selection |
| Productization | Research → CLI/API/Desktop | Core → Runtime → CLI/API/Dashboard/Desktop |

The question for ARO is not “what can we copy?” but “what resource-awareness principle can we generalize from model-level execution to multi-agent orchestration?” ARO can select a GPU/node and then use FreeToken as the inference backend inside that node; the systems are complementary.
