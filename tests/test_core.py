import unittest
from aro.core import *

class CoreTests(unittest.TestCase):
    def setUp(self): self.s=AdaptiveScheduler(); self.tool=Resource('tools','tool'); self.cpu=Resource('cpu','cpu'); self.cloud=Resource('cloud','cloud',network_ms=100,cost_per_1k=.1); self.gpu=Resource('gpu','gpu',gpu=True,vram_gb=16)
    def test_no_llm_routing(self): self.assertEqual(self.s.choose(Task('ping','watch','health-check'),[self.tool])[1],Method.TOOL)
    def test_local_cloud_decision(self): self.assertEqual(self.s.choose(Task('draft','work','writing'),[self.cpu,self.cloud])[1],Method.LOCAL); self.assertEqual(self.s.choose(Task('reason','work','complex',needs_reasoning=True),[self.cloud])[1],Method.CLOUD)
    def test_policy_restriction(self): self.assertRaises(RuntimeError,self.s.choose,Task('private','x','complex',needs_reasoning=True,privacy='private'),[self.cloud])
    def test_shortage_and_unavailable(self): self.assertRaises(RuntimeError,self.s.choose,Task('x','x','complex',needs_reasoning=True),[Resource('gone','cpu',available=False)])
    def test_incident_defers_low_priority(self): a=__import__('aro.demo',fromlist=['build']).build(); a.simulate_incident(); self.assertTrue(any(t.status=='deferred' for t in a.tasks if t.priority<70)); self.assertTrue(a.incident_active)
    def test_telemetry_recording(self): a=__import__('aro.demo',fromlist=['build']).build(); a.execute_next(); self.assertGreater(len(a.telemetry.records),0); self.assertIn('method',asdict(a.telemetry.records[0]))
if __name__ == '__main__': unittest.main()
