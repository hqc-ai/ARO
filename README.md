# ARO — Agent Runtime & Operations Platform

**ver392026**

> **Run many AI agents on the hardware you already own.**
>
> *Don't give every agent a GPU. Give every agent the right resource.*

ARO is an evidence-aware runtime and operations platform for multi-agent monitoring, investigation, automation, governance, and operational workflows. It is the entry point for the HQC-AI ecosystem: agents, tools, evidence workflows, and application packs run on a common runtime.

ARO is not a model runtime or inference engine. OpenAI, Anthropic, Gemini, Bedrock, Ollama, vLLM, and FreeToken can be providers/backends. ARO decides what work should happen, where, under which policy, with which evidence and approval trail.

### Why ARO?

Generic agent flow: `Prompt → Agent → Tool → Result`.

ARO flow: `Event → Evidence → Agent → Policy → Decision → Approval → Action → Verification → Audit Trail`.

`Observation ≠ Evidence ≠ Finding ≠ Conclusion ≠ Action`.

### Product architecture

ARO Core is headless and UI-independent. A reusable Runtime exposes the same orchestration services to the CLI, API, Dashboard, and future Desktop application:

```mermaid
flowchart LR
 Core[ARO Core\nprofile · policy · schedule · telemetry] --> Runtime[ARO Runtime]
 Runtime --> CLI[ARO CLI]
 Runtime --> API[ARO API]
 Runtime --> Dash[ARO Dashboard]
 Runtime --> Desktop[ARO Desktop]
```

The dashboard and future desktop shell contain presentation and connection concerns only; scheduling logic remains in Core/Runtime. See [Desktop vision](docs/product/desktop-vision.md).

```mermaid
flowchart LR
 A[Agent / Event] --> B[Task Profiler] --> C{No LLM needed?}
 C -- yes --> D[Tool / Script]
 C -- no --> E[Priority + Policy]
 E --> F[Resource Discovery] --> G[Adaptive Scheduler] --> H[Execution]
 D --> I[Telemetry] 
 H --> I --> J[Evaluation] --> K[Recommendation]
```

## Quick start

Requires Python 3.10+ and no third-party packages.

```bash
python3 aroctl init
python3 aroctl run mini-soc --profile macos
python3 -m aro.dashboard
```

Open <http://127.0.0.1:8080>. Click **Simulate Security Incident** to see watch agents detect an anomaly, incident work escalate, and lower-priority work defer. JSON API: `/api/state`.

Run tests:

```bash
python -m unittest discover -s tests -v
```

The Mini SOC workflow is experimental and read-only: it collects synthetic evidence, builds provenance, and requires human review. It does not quarantine files, terminate processes, modify hosts, or revoke credentials.

## Maturity

**Working now:** headless Runtime boundary, evidence/governance model foundation, provider ports, `aroctl` CLI, Mini SOC macOS read-only workflow, synthetic incident references, dashboard demo, scheduler, and tests.

**Experimental:** agent operations, governance execution, app/workflow-pack model, and the current in-memory runtime state.

**Planned:** Windows/Linux collectors, real provider integrations, automatic resource discovery, durable evidence storage, multi-node ARO, desktop control plane, production approval transport, and production security hardening.

## HQC-AI Ecosystem

If you are new to the HQC-AI ecosystem, start with ARO. ARO provides the runtime/platform layer; `hqc-codex-core-skills` can provide reusable skill packages; `ai-assisted-audit-investigation` provides investigation methodology, evidence reasoning, and reference framework. These projects remain separate and are not mechanically merged.

## What ARO is (and is not)

Inference engines optimize model execution and serving. ARO orchestrates agent workloads: no-LLM decisions, priority, policy, queues, contention, escalation, telemetry, and human-reviewed optimization. ARO is runtime/vendor agnostic and can later connect Ollama, llama.cpp, FreeToken, MLX, OpenAI-compatible APIs, cloud GPUs, and additional nodes without changing the core interfaces.

## Supported by 5SOffice

ARO is developed and tested as part of practical research into AI Agent infrastructure and resource-efficient automation.

**5SOffice** · Website: <https://5soffice.com.vn>

Project initiated by **Nguyễn Đăng Quang** · Supported by **5SOffice**.

## Support ARO

If ARO helps you make better use of your existing hardware, build your AI Agent lab, or reduce unnecessary compute costs, consider supporting continued development. See [SUPPORT.md](SUPPORT.md).

## Public boundary

This repository contains architecture, generic implementation, simulator code, example configuration, and synthetic data only. Never add credentials, private security configuration, real incident evidence, customer data, internal infrastructure details, or private prompts/workflows.

## Documentation

- [Architecture](docs/architecture.md)
- [Home Lab ver392026](docs/home-lab-ver392026.md)
- [FreeToken lessons and attribution](docs/research/freetoken-lessons.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## License and attribution

MIT licensed. See [LICENSE](LICENSE). FreeToken is inspiration for heterogeneous resource utilization and adaptive execution; ARO is an independent agent-level orchestration design and does not copy FreeToken source code. See the dedicated attribution note for official links and scope.
