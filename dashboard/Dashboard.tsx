import React, { useState, useEffect } from "react";
import { Activity, Shield, Cpu, Database, LayoutGrid } from "lucide-react";

const FuturisticDashboard = () => {
  const [pulse, setPulse] = useState(0);
  const [nodes, setNodes] = useState([
    { id: "α-1", status: "online", load: 45 },
    { id: "β-2", status: "online", load: 12 },
    { id: "γ-3", status: "warning", load: 88 },
    { id: "δ-4", status: "syncing", load: 30 },
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      setPulse((p) => (p + 1) % 100);
      setNodes((prev) =>
        prev.map((n) => ({
          ...n,
          load: Math.min(100, Math.max(0, n.load + (Math.random() - 0.5) * 10)),
        }))
      );
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-black text-green-500 font-mono p-8 border-4 border-green-900">
      <header className="flex justify-between items-center border-b-2 border-green-900 pb-4 mb-8">
        <div className="flex items-center gap-4">
          <Activity className="w-12 h-12 animate-pulse" />
          <h1 className="text-4xl font-black uppercase tracking-tighter">Omega-System // Command-Center</h1>
        </div>
        <div className="text-right">
          <p className="text-xs">SYSTEM_STATUS: [OPTIMAL]</p>
          <p className="text-xs">Uptime: 2,453.2 hrs</p>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 space-y-8">
          <section className="bg-zinc-950 p-6 border border-green-900/50">
            <h2 className="flex items-center gap-2 text-xl mb-4 border-l-4 border-green-500 pl-4">
              <LayoutGrid className="w-5 h-5" /> Swarm_Network_Topology
            </h2>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              {nodes.map((node) => (
                <div key={node.id} className="p-4 border border-green-900 bg-black hover:border-green-500 transition-colors cursor-crosshair">
                  <p className="text-xs opacity-50 mb-1">{node.id}</p>
                  <p className="text-lg font-bold">{node.status.toUpperCase()}</p>
                  <div className="w-full bg-zinc-900 h-1 mt-2">
                    <div 
                      className={`h-full ${node.load > 80 ? 'bg-red-500' : 'bg-green-500'}`} 
                      style={{ width: `${node.load}%` }} 
                    />
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section className="bg-zinc-950 p-6 border border-green-900/50">
            <h2 className="flex items-center gap-2 text-xl mb-4 border-l-4 border-green-500 pl-4">
              <Database className="w-5 h-5" /> Vector_Memory_Mesh_Flux
            </h2>
            <div className="h-48 flex items-end gap-1 overflow-hidden">
              {[...Array(50)].map((_, i) => (
                <div 
                  key={i} 
                  className="bg-green-500/20 w-full" 
                  style={{ height: `${Math.random() * 100}%` }} 
                />
              ))}
            </div>
          </section>
        </div>

        <div className="space-y-8">
          <section className="bg-zinc-950 p-6 border border-green-900/50">
            <h2 className="flex items-center gap-2 text-xl mb-4 border-l-4 border-green-500 pl-4">
              <Shield className="w-5 h-5" /> Security_Kernel
            </h2>
            <ul className="text-xs space-y-2">
              <li className="flex justify-between"><span>Auth_Handshake:</span> <span className="text-green-400">PASSED</span></li>
              <li className="flex justify-between"><span>Intrusion_Shield:</span> <span className="text-green-400">ACTIVE</span></li>
              <li className="flex justify-between"><span>Data_Entropy:</span> <span className="text-green-400">LOW</span></li>
            </ul>
          </section>

          <section className="bg-zinc-950 p-6 border border-green-900/50">
            <h2 className="flex items-center gap-2 text-xl mb-4 border-l-4 border-green-500 pl-4">
              <Cpu className="w-5 h-5" /> Agentic_Load
            </h2>
            <div className="text-5xl font-black text-center py-4">{pulse}%</div>
            <p className="text-[10px] text-center opacity-50">Global convergance delta approaching zero...</p>
          </section>
        </div>
      </div>

      <footer className="mt-8 pt-4 border-t border-green-900 flex justify-between text-[10px] opacity-30 italic">
        <span>© 2026 Omega-System Dynamics</span>
        <span>Build_v4.1.0-STABLE</span>
      </footer>
    </div>
  );
};

export default FuturisticDashboard;
