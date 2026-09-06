# Evidence-first runtime

ARO distinguishes every stage of an operational workflow:

```text
Observation → Evidence → Finding → Conclusion → Action → Verification
```

An `EvidenceArtifact` records source, timestamp, collector, host/device, collection method, hash, transformation history, incident/case, confidence, and attribution. Observations may inform acquisition, but they are not findings. Findings must reference evidence. Actions require a governance decision and, by default, human approval.

The MVP only demonstrates synthetic/read-only collection. It does not quarantine files, terminate processes, modify hosts, revoke credentials, or perform other destructive security actions.
