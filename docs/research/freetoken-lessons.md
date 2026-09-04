# FreeToken lessons

## What FreeToken taught us

FreeToken is an important inspiration for thinking about heterogeneous resource utilization and adaptive execution. See the official [FreeToken repository](https://github.com/FlashML-org/FreeToken) and [FreeToken paper](https://arxiv.org/abs/2608.16157).

The lesson adopted here is to treat available compute as a pool whose capabilities and contention matter, instead of assuming one fixed accelerator per workload.

## From model-level scheduling to agent-level orchestration

FreeToken and inference systems primarily optimize model execution. ARO operates one layer above: it decides whether an agent task needs a model, chooses a tool/model/node/cloud route, applies privacy and priority policy, manages escalation, and records outcome telemetry. ARO is an independent implementation, not a fork, and contains no copied FreeToken source code.
