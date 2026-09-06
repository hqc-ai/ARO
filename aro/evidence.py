"""Evidence-first domain objects. Collection is descriptive and non-destructive."""
from __future__ import annotations
from dataclasses import dataclass, field
from time import time
from typing import Any
import hashlib, json, uuid

@dataclass
class EvidenceArtifact:
    source: str; collector: str; host: str; method: str; payload: Any
    incident_id: str | None = None; confidence: float = 1.0
    timestamp: float = field(default_factory=time); artifact_id: str = field(default_factory=lambda: uuid.uuid4().hex[:10])
    sha256: str = ""; transformation_history: list[str] = field(default_factory=list)
    def seal(self) -> "EvidenceArtifact":
        body = json.dumps(self.payload, sort_keys=True, default=str).encode()
        self.sha256 = hashlib.sha256(body).hexdigest(); return self

@dataclass
class Finding:
    title: str; evidence_ids: list[str]; confidence: float; incident_id: str

@dataclass
class Incident:
    incident_id: str; title: str; status: str = "open"; artifacts: list[EvidenceArtifact] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list); approval_required: bool = True

def evidence_chain() -> list[str]:
    return ["observation", "evidence", "finding", "conclusion", "action", "verification"]
