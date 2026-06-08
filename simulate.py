import random
import time
import asyncio
import numpy as np
from core.memory import VectorMemory
from core.kernel import OmegaKernel

class SwarmSimulator:
    """
    Simulates autonomous agent swarm activity.
    Generates logs and data for Omega-System.
    """
    def __init__(self, agent_count: int = 10):
        self.kernel = OmegaKernel()
        self.memory = VectorMemory(dimension=128)
        self.agent_count = agent_count

    async def run_simulation(self, steps: int = 1000):
        print(f"--- Starting Live Swarm Kernel ({self.agent_count} agents) ---")
        
        # Register agents
        for i in range(self.agent_count):
            await self.kernel.register_agent(f"Agent-{i}", ["nav", "scan"])

        step = 0
        while step < steps:
            # Register random tasks
            tasks = ["Scan Grid", "Update Local Map", "Sync Knowledge", "Optimize Path"]
            task = random.choice(tasks)
            agent_id = random.randint(0, self.agent_count - 1)
            await self.kernel.schedule_task(f"Agent-{agent_id}: {task}", {"priority": "high"})
            
            # Store simulated findings in memory
            vector = np.random.rand(128).tolist()
            self.memory.add_embedding(vector, {"step": step, "agent": agent_id, "action": task})
            
            await asyncio.sleep(5)
            step += 1
        
        print("\n--- Simulation Loop Handoff to Kernel ---")
        await self.kernel.run()

if __name__ == "__main__":
    sim = SwarmSimulator(agent_count=5)
    asyncio.run(sim.run_simulation())
