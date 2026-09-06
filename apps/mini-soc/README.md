# Mini SOC workflow pack

This is ARO's first product showcase: evidence-first, AI-assisted security operations for small teams and local environments. The macOS profile is read-only and uses synthetic data in this repository.

Run it with:

```bash
python3 aroctl run mini-soc --profile macos
```

Pipeline: Observe → Acquire Evidence → Normalize → Baseline/Delta → Correlate → AI-assisted Reasoning → Confidence → Decision → Human Approval → Action → Verification → Evidence Preservation.
