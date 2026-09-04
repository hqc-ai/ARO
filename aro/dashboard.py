from http.server import BaseHTTPRequestHandler, HTTPServer
from .runtime import Runtime
from .demo import build
import json
a = build()
HTML = '''<!doctype html><meta name="viewport" content="width=device-width"><title>ARO Dashboard</title><style>body{font:15px system-ui;background:#10151c;color:#e8eef5;max-width:1100px;margin:30px auto;padding:0 20px}h1{color:#6ee7b7}button{background:#f59e0b;border:0;border-radius:8px;padding:12px 18px;font-weight:700}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}.card{background:#1a2430;border:1px solid #2c3b4b;border-radius:12px;padding:16px}.muted{color:#9fb0c0}pre{white-space:pre-wrap;color:#b7f7d6}</style><h1>ARO <small>ver392026</small></h1><p>Adaptive Resource Orchestrator · right resource, right task.</p><button onclick="incident()">Simulate Security Incident</button><div id="app"></div><script>async function draw(){let s=await fetch('/api/state').then(r=>r.json());app.innerHTML=`<div class=grid><div class=card><b>Agents</b><h2>${s.agents.length}</h2>${s.incident_active?'🚨 Incident active':'✅ Normal operation'}</div><div class=card><b>Tasks</b><h2>${s.tasks.length}</h2>${s.tasks.filter(x=>x.status==='deferred').length} deferred</div><div class=card><b>Telemetry</b><h2>${s.telemetry.length}</h2>estimated API cost: $${s.telemetry.reduce((n,x)=>n+x.api_cost,0).toFixed(3)}</div><div class=card><b>Resources</b><h2>${s.resources.filter(x=>x.available).length}/${s.resources.length}</h2>healthy / available</div></div><div class=card><b>Current routing</b><pre>${s.telemetry.slice(-12).map(x=>x.agent+' → '+x.method+' @ '+x.node).join('\\n')||'No executions yet'}</pre></div><div class=card><b>Audit and recommendations</b><pre>${s.audit_log.concat(s.recommendations).join('\\n')||'Waiting for events'}</pre></div>`}async function incident(){await fetch('/api/incident',{method:'POST'});draw()}draw();setInterval(draw,2000)</script>'''
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/state': self.send(200, Runtime(a).state(), 'application/json')
        else: self.send(200, HTML, 'text/html')
    def do_POST(self):
        if self.path == '/api/incident': a.simulate_incident(); [a.execute_next() for _ in range(len(a.tasks)+2)]; self.send(200, {'ok':True}, 'application/json')
    def send(self, code, data, kind):
        raw = data.encode() if isinstance(data,str) else json.dumps(data).encode(); self.send_response(code); self.send_header('Content-Type',kind); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw)
def main(): print('ARO dashboard: http://127.0.0.1:8080'); HTTPServer(('127.0.0.1',8080), Handler).serve_forever()
if __name__ == '__main__': main()
