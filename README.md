# ARO — Adaptive Resource Orchestrator

**ver392026**

> **Run many AI agents on the hardware you already own.**
>
> *Don't give every agent a GPU. Give every agent the right resource.*

ARO is a lightweight reference implementation for adaptive, policy-aware orchestration of heterogeneous resources across many AI agents. It operates at the **agent/task layer**, deciding whether a task needs an LLM at all, then routing it to the right tool, local model, node, or cloud capability.

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
python -m aro.demo --scenario normal
python -m aro.demo --scenario incident
python -m aro.dashboard
```

Open <http://127.0.0.1:8080>. Click **Simulate Security Incident** to see watch agents detect an anomaly, incident work escalate, and lower-priority work defer. JSON API: `/api/state`.

Run tests:

```bash
python -m unittest discover -s tests -v
```

## What ARO is (and is not)

Inference engines optimize model execution and serving. ARO orchestrates agent workloads: no-LLM decisions, priority, policy, queues, contention, escalation, telemetry, and human-reviewed optimization. ARO is runtime/vendor agnostic and can later connect Ollama, llama.cpp, FreeToken, MLX, OpenAI-compatible APIs, cloud GPUs, and additional nodes without changing the core interfaces.

## Supported by 5SOffice

ARO is developed and tested as part of practical research into AI Agent infrastructure and resource-efficient automation.

**5SOffice** · Website: <https://5soffice.com.vn>

Project initiated by **Nguyễn Đăng Quang** · Supported by **5SOffice**.

## Support ARO

If ARO helps you make better use of your existing hardware, build your AI Agent lab, or reduce unnecessary compute costs, consider supporting continued development. See [SUPPORT.md](SUPPORT.md).

❤️ Support ARO

Bank transfer — Vietnam & International
Bank: Shinhan Bank Vietnam
Account holder: NGUYEN DANG QUANG
Account number: 0944659937
SWIFT/BIC: SHBKVNVX
Transfer reference: DONATE HQC AIMS
HQC AIMS Community bank transfer QR code
<img width="750" height="1085" alt="image" src="https://github.com/user-attachments/assets/1037042b-8ceb-4068-92f0-24cf75280902" />

USDT — TRON (TRC20)
Asset: Tether — USDT
Network: TRON — TRC20
Receiving address: TPNDgQnemyVjjhAuwSPSJz37BCaQrUkaj9
HQC AIMS Community USDT TRC20 donation QR code
<img width="750" height="1286" alt="image" src="https://github.com/user-attachments/assets/394373c2-eca7-4536-bf93-719d912214b2" />

Verify the receiving address and blockchain network carefully before transferring. Cryptocurrency transactions are generally irreversible.

Your contribution helps maintain the Community Edition, improve documentation, develop practical examples, and continue sharing useful AI governance resources.

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
