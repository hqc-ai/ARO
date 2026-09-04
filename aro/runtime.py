"""Reusable headless runtime boundary for CLI, API, dashboard, and desktop."""
from .core import ARO, snapshot

class Runtime:
    def __init__(self, orchestrator: ARO | None = None): self.orchestrator = orchestrator or ARO()
    def state(self): return snapshot(self.orchestrator)
    def simulate_incident(self):
        self.orchestrator.simulate_incident()
        while self.orchestrator.execute_next(): pass
        return self.state()
