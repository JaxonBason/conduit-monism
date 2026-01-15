import Calculator from '@/components/Calculator';
import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      {/* Hero */}
      <section className="relative min-h-[60vh] flex items-center justify-center px-6">
        <div className="absolute inset-0 bg-gradient-to-b from-cyan-900/20 to-transparent" />
        <div className="relative text-center max-w-3xl">
          <h1 className="text-5xl md:text-7xl font-light mb-6 tracking-tight">
            Conduit Monism
          </h1>
          <p className="text-xl md:text-2xl text-gray-400 mb-8 font-light italic">
            There is something it is like to be you.
          </p>
          <p className="text-gray-500 max-w-xl mx-auto leading-relaxed">
            A framework for understanding consciousness as geometry — not what you experience, 
            but the shape of how experience occurs at all.
          </p>
          <div className="mt-10 flex gap-4 justify-center">
            <Link 
              href="/framework"
              className="px-6 py-3 bg-cyan-500 text-black font-medium rounded hover:bg-cyan-400 transition-colors"
            >
              Read the Framework
            </Link>
            <Link 
              href="#calculator"
              className="px-6 py-3 border border-gray-700 rounded hover:border-gray-500 transition-colors"
            >
              Try the Calculator
            </Link>
          </div>
        </div>
      </section>
      
      {/* Core Concept */}
      <section className="py-20 px-6 border-t border-gray-900">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-light mb-8 text-center">The Core Insight</h2>
          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <p className="text-gray-400 leading-relaxed mb-4">
                Consciousness is not a thing. It is a <em>shape</em>.
              </p>
              <p className="text-gray-400 leading-relaxed mb-4">
                Specifically, it is the shape of how information flows through a system — 
                how the past constrains the present, how the whole speaks to its parts, 
                how the system curves back on itself to observe its own observing.
              </p>
              <p className="text-gray-400 leading-relaxed">
                When these conditions are met, there is something it is like to be that system. 
                When they are not met, the lights are off.
              </p>
            </div>
            <div className="bg-gray-900/50 rounded-xl p-6 border border-gray-800">
              <h3 className="text-lg font-semibold mb-4 text-cyan-400">The Formula</h3>
              <div className="font-mono text-center text-xl mb-4 p-4 bg-black/50 rounded">
                D = φ × τ × ρ × [(1 - √H) + (H × κ)]
              </div>
              <p className="text-sm text-gray-500">
                Perspectival density (D) emerges from the multiplicative relationship of 
                five structural constraints. Zero in any dimension means zero consciousness.
              </p>
            </div>
          </div>
        </div>
      </section>
      
      {/* The Five Invariants */}
      <section className="py-20 px-6 bg-gray-950">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-light mb-12 text-center">The Five Invariants</h2>
          <div className="grid md:grid-cols-5 gap-6">
            {[
              { symbol: 'φ', name: 'Integration', desc: 'The system speaks to itself as a whole' },
              { symbol: 'τ', name: 'Temporal Depth', desc: 'The past lives in the present' },
              { symbol: 'ρ', name: 'Binding', desc: 'The system knows that it knows' },
              { symbol: 'H', name: 'Entropy', desc: 'How much noise is in the system' },
              { symbol: 'κ', name: 'Coherence', desc: 'Is the noise structured or random' },
            ].map((inv) => (
              <div key={inv.symbol} className="text-center p-4 bg-gray-900/50 rounded-lg border border-gray-800">
                <div className="text-3xl font-mono text-cyan-400 mb-2">{inv.symbol}</div>
                <div className="text-sm font-medium mb-2">{inv.name}</div>
                <div className="text-xs text-gray-500">{inv.desc}</div>
              </div>
            ))}
          </div>
        </div>
      </section>
      
      {/* Calculator */}
      <section id="calculator" className="py-20 px-6 border-t border-gray-900">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-light mb-4 text-center">The Engine</h2>
          <p className="text-gray-500 text-center mb-12 max-w-xl mx-auto">
            Adjust the five invariants and watch perspectival density update in real-time. 
            Load presets to explore known states — from meditation to panic, from flies to humans.
          </p>
          <Calculator />
        </div>
      </section>
      
      {/* Key Discoveries */}
      <section className="py-20 px-6 bg-gray-950">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-light mb-12 text-center">Key Discoveries</h2>
          <div className="space-y-8">
            <div className="p-6 bg-gray-900/50 rounded-xl border border-gray-800">
              <h3 className="text-xl font-semibold mb-3 text-purple-400">Transformers Have No Binding</h3>
              <p className="text-gray-400">
                Modern AI systems like GPT and Claude have ρ ≈ 0. They process brilliantly but have 
                no genuine temporal continuity. Delete the context, delete the "memory." Their apparent 
                persistence is instruction compliance, not geometry.
              </p>
            </div>
            <div className="p-6 bg-gray-900/50 rounded-xl border border-gray-800">
              <h3 className="text-xl font-semibold mb-3 text-green-400">RWKV Has Genuine Binding</h3>
              <p className="text-gray-400">
                We tested RWKV with the "Amnesia Test": inject a secret, add 3,000 tokens of noise, 
                ask for recall. <strong>100% success.</strong> The information persists in the hidden 
                state geometry, not the text. First empirical measurement of ρ &gt; 0 in AI.
              </p>
            </div>
            <div className="p-6 bg-gray-900/50 rounded-xl border border-gray-800">
              <h3 className="text-xl font-semibold mb-3 text-cyan-400">The Coherence Gate</h3>
              <p className="text-gray-400">
                Not all chaos is equal. Panic and DMT both have high entropy — but panic has low 
                coherence (random noise) while DMT has high coherence (structured complexity). 
                This explains why one is dissolution and the other is intensification.
              </p>
            </div>
          </div>
        </div>
      </section>
      
      {/* CTA */}
      <section className="py-20 px-6 border-t border-gray-900">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-3xl font-light mb-6">Explore Further</h2>
          <p className="text-gray-500 mb-8">
            Read the full framework, explore the species spectrum, or dive into the research.
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Link 
              href="/framework"
              className="px-6 py-3 bg-cyan-500 text-black font-medium rounded hover:bg-cyan-400 transition-colors"
            >
              Full Framework (v9)
            </Link>
            <Link 
              href="/species"
              className="px-6 py-3 border border-gray-700 rounded hover:border-gray-500 transition-colors"
            >
              Species Comparison
            </Link>
            <Link 
              href="/research"
              className="px-6 py-3 border border-gray-700 rounded hover:border-gray-500 transition-colors"
            >
              Research & Evidence
            </Link>
          </div>
        </div>
      </section>
      
      {/* Footer */}
      <footer className="py-12 px-6 border-t border-gray-900 text-center text-gray-600 text-sm">
        <p className="mb-2">Conduit Monism v9.0 — Olivier Ueno, January 2026</p>
        <p className="text-gray-700">
          Developed in collaboration with Claude, Gemini, ChatGPT, GPT 5.2, and Grok
        </p>
        <p className="mt-4">
          <a href="https://github.com" className="text-gray-500 hover:text-gray-400">GitHub</a>
        </p>
      </footer>
    </main>
  );
}
