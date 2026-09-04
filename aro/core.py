from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from time import time
from typing import Any
import uuid

class Method(str, Enum):
    TOOL = "tool-only"
    LOCAL = "local-llm"
    CLOUD = "cloud"
    BURST = "burst-compute"

@dataclass
class Task:
    name: str; agent: str; task_type: str; priority: int = 50; privacy: str = "internal"
    needs_reasoning: bool = False; latency_ms: int = 5000; context_tokens: int = 1000
    expected_runtime_ms: int = 100; status: str = "queued"
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])

@dataclass
class Resource:
    name: str; kind: str; cpu: int = 4; ram_gb: float = 8; gpu: bool = False; vram_gb: float = 0
    available: bool = True; load: float = 0.1; network_ms: int = 10; cost_per_1k: float = 0

@dataclass
class Telemetry:
    task_id: str; agent: str; node: str; method: str; model_or_tool: str
    cpu: float; ram_gb: float; gpu: float; vram_gb: float; storage_io_mb: float
    network_ms: int; ttft_ms: int | None; tokens_per_sec: float | None
    execution_ms: int; queue_ms: int; api_cost: float; result_status: str
    quality_score: float | None = None; timestamp: float = field(default_factory=time)

class AgentRegistry:
    def __init__(self): self.agents: dict[str, dict[str, Any]] = {}
    def register(self, name: str, category: str, weight: str = "normal"):
        self.agents[name] = {"name": name, "category": category, "weight": weight, "status": "sleeping"}

class EventBus:
    def __init__(self): self.events: list[dict[str, Any]] = []
    def publish(self, event: dict[str, Any]): self.events.append(event)

class ResourceRegistry:
    def __init__(self): self.resources: dict[str, Resource] = {}
    def register(self, resource: Resource): self.resources[resource.name] = resource

class ModelRegistry:
    def __init__(self): self.models: dict[str, dict[str, Any]] = {}
    def register(self, name: str, **metadata): self.models[name] = metadata

class ToolRegistry:
    def __init__(self): self.tools: dict[str, dict[str, Any]] = {}
    def register(self, name: str, **metadata): self.tools[name] = metadata

class AuditLog:
    def __init__(self): self.entries: list[str] = []
    def append(self, message: str): self.entries.append(message)

class PolicyEngine:
    def allowed(self, task: Task, resource: Resource, method: Method) -> bool:
        if task.privacy == "private" and method == Method.CLOUD: return False
        if task.task_type == "security" and method == Method.CLOUD and task.privacy != "approved": return False
        return resource.available

class TaskProfiler:
    def profile(self, task: Task) -> dict[str, Any]:
        return {"tool_suitable": task.task_type in {"health-check", "reminder", "normalization", "backup"} and not task.needs_reasoning,
                "reasoning": task.needs_reasoning, "urgency": task.priority >= 80}

class AdaptiveScheduler:
    def __init__(self, policy: PolicyEngine | None = None): self.policy = policy or PolicyEngine()
    def choose(self, task: Task, resources: list[Resource], profiler: TaskProfiler | None = None):
        profile = (profiler or TaskProfiler()).profile(task)
        usable = [r for r in resources if r.available]
        if not usable: raise RuntimeError("no available resources")
        if profile["tool_suitable"]:
            candidates = [r for r in usable if r.kind in {"tool", "cpu"}]
            if candidates: return min(candidates, key=lambda r: r.load), Method.TOOL, "script/monitoring-tool"
        local = [r for r in usable if r.kind in {"cpu", "local-model"} and r.ram_gb >= 2 and r.load < .95]
        if not task.needs_reasoning and local: return min(local, key=lambda r: (r.load, r.network_ms)), Method.LOCAL, "shared-local-model"
        cloud = [r for r in usable if r.kind == "cloud" and self.policy.allowed(task, r, Method.CLOUD)]
        if cloud: return min(cloud, key=lambda r: (r.cost_per_1k, r.network_ms)), Method.CLOUD, "frontier-api"
        gpu = [r for r in usable if r.gpu and r.vram_gb >= 8 and self.policy.allowed(task, r, Method.BURST)]
        if gpu: return min(gpu, key=lambda r: r.load), Method.BURST, "heavy-local-model"
        raise RuntimeError("resource shortage: no compatible route")

class TelemetryCollector:
    def __init__(self): self.records: list[Telemetry] = []
    def record(self, item: Telemetry): self.records.append(item)

class RecommendationEngine:
    def recommend(self, records: list[Telemetry]) -> list[str]:
        if not records: return []
        tool = sum(r.method == Method.TOOL.value for r in records)
        return [f"Keep tool-first routing: it handled {tool} workload(s) without an LLM."] if tool else ["Collect more baseline telemetry before changing hardware or routing policy."]

class ARO:
    def __init__(self):
        self.agents = AgentRegistry(); self.event_bus = EventBus(); self.resource_registry = ResourceRegistry(); self.model_registry = ModelRegistry(); self.tool_registry = ToolRegistry(); self.audit = AuditLog(); self.resources: list[Resource] = []; self.tasks: list[Task] = []
        self.telemetry = TelemetryCollector(); self.profiler = TaskProfiler(); self.policy = PolicyEngine(); self.scheduler = AdaptiveScheduler(self.policy)
        self.incident_active = False; self.audit_log: list[str] = self.audit.entries
    def submit(self, task: Task) -> Task:
        if self.incident_active and task.priority < 70: task.status = "deferred"
        self.tasks.append(task); return task
    def execute_next(self):
        pending = [t for t in self.tasks if t.status == "queued"]
        if not pending: return None
        task = max(pending, key=lambda t: t.priority)
        try: node, method, capability = self.scheduler.choose(task, self.resources, self.profiler)
        except RuntimeError as e: task.status = "waiting"; self.audit_log.append(str(e)); return {"task": task, "error": str(e)}
        task.status = "running"; task.status = "completed"
        self.telemetry.record(Telemetry(task.id, task.agent, node.name, method.value, capability, node.load*100, node.ram_gb, float(node.gpu), node.vram_gb, 2.0, node.network_ms, 120 if method != Method.TOOL else None, 40.0 if method != Method.TOOL else None, task.expected_runtime_ms, 0, node.cost_per_1k, "success", .95))
        return {"task": task, "node": node, "method": method.value, "capability": capability}
    def simulate_incident(self):
        self.incident_active = True; self.event_bus.publish({"type": "security.anomaly", "severity": "high"}); self.audit_log.append("Security anomaly detected; incident priority escalation activated")
        for task in self.tasks:
            if task.priority < 70 and task.status == "queued": task.status = "deferred"
        for name in ["Incident Manager", "Evidence Collector", "IOC/TTP Analyzer", "Timeline Agent", "Investigator"]:
            self.agents.agents.setdefault(name, {"name": name, "category": "incident", "status": "waiting"})["status"] = "running"
        for name, typ in [("Incident Manager", "security"), ("Evidence Collector", "collection"), ("IOC/TTP Analyzer", "security"), ("Timeline Agent", "normalization"), ("Investigator", "incident-reasoning")]:
            self.submit(Task(name, name, typ, priority=95 if name in {"Incident Manager", "Investigator"} else 85, privacy="private", needs_reasoning=name in {"Investigator", "IOC/TTP Analyzer"}))

def snapshot(aro: ARO) -> dict[str, Any]:
    return {"version": "ver392026", "incident_active": aro.incident_active, "agents": list(aro.agents.agents.values()), "resources": [asdict(r) for r in aro.resources], "tasks": [asdict(t) for t in aro.tasks], "telemetry": [asdict(t) for t in aro.telemetry.records], "audit_log": aro.audit_log, "recommendations": RecommendationEngine().recommend(aro.telemetry.records)}
