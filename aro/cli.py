from .demo import build
import argparse, json

def main():
    p = argparse.ArgumentParser(prog="aro"); p.add_argument("--incident", action="store_true"); p.add_argument("--json", action="store_true"); args = p.parse_args()
    a = build()
    if args.incident: a.simulate_incident()
    while a.execute_next(): pass
    from .core import snapshot
    print(json.dumps(snapshot(a), indent=2) if args.json else f"ARO ver392026: {len(a.tasks)} tasks, {len(a.telemetry.records)} telemetry records")

if __name__ == "__main__": main()
