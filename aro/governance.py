from __future__ import annotations
from enum import Enum

class ExecutionLevel(str, Enum):
    READ_ONLY = "READ_ONLY"
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
    AUTO_ALLOWED = "AUTO_ALLOWED"

class Governance:
    def __init__(self, rules: dict[str, ExecutionLevel] | None = None):
        self.rules = rules or {"process_listing": ExecutionLevel.READ_ONLY, "log_collection": ExecutionLevel.READ_ONLY, "hashing": ExecutionLevel.AUTO_ALLOWED, "report_generation": ExecutionLevel.AUTO_ALLOWED, "quarantine_file": ExecutionLevel.APPROVAL_REQUIRED, "terminate_process": ExecutionLevel.APPROVAL_REQUIRED}
    def level(self, action: str) -> ExecutionLevel: return self.rules.get(action, ExecutionLevel.APPROVAL_REQUIRED)
    def can_execute(self, action: str, approved: bool = False) -> bool:
        level = self.level(action); return level == ExecutionLevel.AUTO_ALLOWED or level == ExecutionLevel.READ_ONLY or approved
