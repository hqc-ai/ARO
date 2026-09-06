# App / Workflow Pack model

An ARO App is a named workflow pack that runs on the common Runtime. It declares profiles, agent roles, task types, evidence schemas, policies, and reports. It does not implement a second scheduler.

```text
App manifest → Runtime events/tasks → Core scheduling → Evidence → Governance → Report
```

The first showcase is `mini-soc`, with a macOS profile and a read-only pipeline. Future packs include incident investigation, ISO audit, office operations, and SEO monitoring.
