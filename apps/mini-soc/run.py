from aro.evidence import EvidenceArtifact, Finding, Incident
from aro.governance import Governance

def run(profile="macos"):
    incident = Incident("incident-001", "Synthetic suspicious persistence change")
    artifact = EvidenceArtifact("launch-agent-baseline", "macos-read-only-collector", "synthetic-macbook", "metadata-only", {"delta": "new entry", "path": "~/Library/LaunchAgents/example.plist"}, incident.incident_id, .92).seal()
    incident.artifacts.append(artifact)
    incident.findings.append(Finding("New persistence entry requires review", [artifact.artifact_id], .86, incident.incident_id))
    return {"profile": profile, "incident": incident, "governance": Governance()}

if __name__ == "__main__":
    result = run(); print(result["incident"].incident_id, "read-only evidence collected")
