import unittest
import numpy as np
import sys
import os
import asyncio

# Ensure local Omega-System takes precedence
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.memory import VectorMemory
from core.kernel import OmegaKernel

class TestOmegaCore(unittest.TestCase):
    def test_memory_mesh(self):
        mesh = VectorMemory(dimension=64)
        v = np.random.rand(64).tolist()
        mesh.add_embedding(v, {"tag": "test"})
        results = mesh.search(v, top_k=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["tag"], "test")

    def test_kernel_registration(self):
        k = OmegaKernel()
        # The Kernel class in kernel.py uses register_agent and schedule_task
        # I'll update the test to match the actual implementation
        asyncio.run(k.register_agent("test-agent", ["memory-read"]))
        self.assertEqual(len(k.registry), 1)
        self.assertIn("test-agent", k.registry)

if __name__ == "__main__":
    import asyncio
    unittest.main()
