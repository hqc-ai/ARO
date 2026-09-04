from .core import *
import argparse, json

def build() -> ARO:
    a = ARO()
    names = [("Laptop Security Monitor","watch","light"),("Wi-Fi Monitor","watch","light"),("Router/Modem Monitor","watch","light"),("Camera Monitor","watch","light"),("IoT Monitor","watch","light"),("Network Monitor","watch","light"),("Backup Monitor","watch","light"),("Website Monitor","watch","light"),("Report Agent","work","normal"),("Web Publishing Agent","work","normal"),("Content Agent","work","normal"),("SEO/AEO Agent","work","normal"),("Reminder Agent","work","light"),("Research Agent","work","normal"),("Document Agent","work","normal")]
    for n, c, w in names: a.agents.register(n, c, w)
    a.resources = [Resource("MacBook Air M1", "local-model", 8, 16, load=.28, network_ms=4), Resource("Data Mac mini", "cpu", 4, 8, load=.18, network_ms=3), Resource("Tool Gateway", "tool", 2, 4, load=.05, network_ms=2), Resource("Optional NVIDIA/Linux", "gpu", 16, 64, True, 24, False, 0, 15), Resource("Cloud Frontier", "cloud", 0, 0, network_ms=180, cost_per_1k=.02)]
    for i in range(8): a.submit(Task(f"health check {i+1}", "Network Monitor", "health-check", priority=20))
    a.submit(Task("weekly report", "Report Agent", "report", priority=40, needs_reasoning=True))
    return a

def main():
    p = argparse.ArgumentParser(); p.add_argument("--scenario", choices=["normal", "incident"], default="normal"); p.add_argument("--json", action="store_true"); x = p.parse_args()
    a = build()
    if x.scenario == "incident": a.simulate_incident()
    while a.execute_next(): pass
    print(json.dumps(snapshot(a), indent=2) if x.json else f"ARO ver392026: {len(a.tasks)} tasks, {len(a.telemetry.records)} telemetry records, incident={a.incident_active}")
if __name__ == "__main__": main()
