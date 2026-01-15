'use client';

import { useMemo, useState } from 'react';
import { presets, calculateDensity, Preset } from '@/lib/engine';
import Link from 'next/link';

// Get animal presets sorted by density
function getAnimalSpectrum() {
  const animals = presets.filter(p => p.category === 'animal');
  const humans = presets.filter(p => p.category === 'human');
  const ais = presets.filter(p => p.category === 'ai');
  
  const all = [...animals, ...humans.slice(0, 2), ...ais]; // Include baseline human and flow + AIs
  
  return all.map(p => ({
    ...p,
    density: calculateDensity(p.invariants).D
  })).sort((a, b) => a.density - b.density);
}

function SpectrumBar({ species }: { species: Array<Preset & { density: number }> }) {
  const maxD = Math.max(...species.map(s => s.density));
  
  return (
    <div className="relative h-16 bg-gray-900 rounded-lg overflow-hidden">
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-r from-red-900/30 via-yellow-900/30 to-cyan-900/30" />
      
      {/* Species markers */}
      {species.map((s, i) => {
        const position = (s.density / maxD) * 100;
        return (
          <div
            key={s.name}
            className="absolute top-0 h-full flex flex-col items-center justify-center group"
            style={{ left: `${position}%`, transform: 'translateX(-50%)' }}
          >
            <div className="w-3 h-3 rounded-full bg-cyan-400 border-2 border-black group-hover:scale-150 transition-transform cursor-pointer" />
            <div className="absolute top-full mt-2 opacity-0 group-hover:opacity-100 transition-opacity bg-gray-800 px-2 py-1 rounded text-xs whitespace-nowrap z-10">
              {s.name}: {s.density.toFixed(3)}
            </div>
          </div>
        );
      })}
    </div>
  );
}

function RadarChart({ species }: { species: Preset & { density: number } }) {
  const { phi, tau, rho, H, kappa } = species.invariants;
  const dimensions = [
    { label: 'φ', value: phi },
    { label: 'τ', value: tau },
    { label: 'ρ', value: rho },
    { label: '1-H', value: 1 - H }, // Invert entropy for visual clarity
    { label: 'κ', value: kappa },
  ];
  
  // Calculate polygon points
  const centerX = 100;
  const centerY = 100;
  const radius = 80;
  
  const points = dimensions.map((d, i) => {
    const angle = (i / dimensions.length) * 2 * Math.PI - Math.PI / 2;
    const r = d.value * radius;
    return {
      x: centerX + r * Math.cos(angle),
      y: centerY + r * Math.sin(angle),
      labelX: centerX + (radius + 20) * Math.cos(angle),
      labelY: centerY + (radius + 20) * Math.sin(angle),
      label: d.label,
      value: d.value,
    };
  });
  
  const polygonPoints = points.map(p => `${p.x},${p.y}`).join(' ');
  
  return (
    <svg viewBox="0 0 200 200" className="w-full max-w-[200px]">
      {/* Grid circles */}
      {[0.25, 0.5, 0.75, 1].map(r => (
        <circle
          key={r}
          cx={centerX}
          cy={centerY}
          r={r * radius}
          fill="none"
          stroke="#374151"
          strokeWidth="1"
        />
      ))}
      
      {/* Axis lines */}
      {points.map((p, i) => (
        <line
          key={i}
          x1={centerX}
          y1={centerY}
          x2={centerX + radius * Math.cos((i / points.length) * 2 * Math.PI - Math.PI / 2)}
          y2={centerY + radius * Math.sin((i / points.length) * 2 * Math.PI - Math.PI / 2)}
          stroke="#374151"
          strokeWidth="1"
        />
      ))}
      
      {/* Data polygon */}
      <polygon
        points={polygonPoints}
        fill="rgba(34, 211, 238, 0.3)"
        stroke="#22d3ee"
        strokeWidth="2"
      />
      
      {/* Labels */}
      {points.map((p, i) => (
        <text
          key={i}
          x={p.labelX}
          y={p.labelY}
          textAnchor="middle"
          dominantBaseline="middle"
          className="text-xs fill-gray-400"
        >
          {p.label}
        </text>
      ))}
    </svg>
  );
}

function SpeciesCard({ species, isSelected, onClick }: { 
  species: Preset & { density: number }; 
  isSelected: boolean;
  onClick: () => void;
}) {
  const categoryColors: Record<string, string> = {
    human: 'border-blue-500',
    ai: 'border-purple-500',
    animal: 'border-green-500',
  };
  
  return (
    <div 
      className={`p-4 rounded-lg border cursor-pointer transition-all ${
        isSelected 
          ? 'bg-gray-800 border-cyan-500' 
          : `bg-gray-900/50 ${categoryColors[species.category] || 'border-gray-700'} hover:bg-gray-800/50`
      }`}
      onClick={onClick}
    >
      <div className="flex justify-between items-start mb-2">
        <h3 className="font-medium">{species.name}</h3>
        <span className="text-lg font-mono text-cyan-400">{species.density.toFixed(3)}</span>
      </div>
      <p className="text-xs text-gray-500">{species.description}</p>
    </div>
  );
}

export default function SpeciesPage() {
  const spectrum = useMemo(() => getAnimalSpectrum(), []);
  const [selected, setSelected] = useState<string[]>([spectrum[0].name, spectrum[spectrum.length - 1].name]);
  
  const selectedSpecies = spectrum.filter(s => selected.includes(s.name));
  
  const toggleSelection = (name: string) => {
    if (selected.includes(name)) {
      if (selected.length > 1) {
        setSelected(selected.filter(n => n !== name));
      }
    } else {
      if (selected.length < 3) {
        setSelected([...selected, name]);
      } else {
        setSelected([...selected.slice(1), name]);
      }
    }
  };
  
  return (
    <main className="min-h-screen bg-black text-white py-12 px-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-12">
          <Link href="/" className="text-gray-500 hover:text-gray-400 text-sm mb-4 inline-block">
            ← Back to Home
          </Link>
          <h1 className="text-4xl font-light mb-4">The Conduit Spectrum</h1>
          <p className="text-gray-400 max-w-2xl">
            Consciousness exists on a gradient. From flies to humans, the framework predicts 
            a continuous spectrum of perspectival density. Humans are one example, not the exception.
          </p>
        </div>
        
        {/* Spectrum visualization */}
        <div className="mb-12">
          <h2 className="text-xl font-semibold mb-4">Density Spectrum</h2>
          <SpectrumBar species={spectrum} />
          <div className="flex justify-between text-xs text-gray-600 mt-2">
            <span>Lower Density</span>
            <span>Higher Density</span>
          </div>
        </div>
        
        {/* Comparison */}
        <div className="mb-12">
          <h2 className="text-xl font-semibold mb-4">Compare (select up to 3)</h2>
          <div className="grid md:grid-cols-3 gap-6">
            {selectedSpecies.map(s => (
              <div key={s.name} className="bg-gray-900/50 rounded-xl p-6 border border-gray-800">
                <h3 className="text-lg font-semibold mb-2">{s.name}</h3>
                <div className="text-3xl font-mono text-cyan-400 mb-4">D = {s.density.toFixed(3)}</div>
                <div className="flex justify-center mb-4">
                  <RadarChart species={s} />
                </div>
                <div className="space-y-1 text-sm font-mono">
                  <div className="flex justify-between"><span className="text-gray-500">φ:</span> {s.invariants.phi.toFixed(2)}</div>
                  <div className="flex justify-between"><span className="text-gray-500">τ:</span> {s.invariants.tau.toFixed(2)}</div>
                  <div className="flex justify-between"><span className="text-gray-500">ρ:</span> {s.invariants.rho.toFixed(2)}</div>
                  <div className="flex justify-between"><span className="text-gray-500">H:</span> {s.invariants.H.toFixed(2)}</div>
                  <div className="flex justify-between"><span className="text-gray-500">κ:</span> {s.invariants.kappa.toFixed(2)}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* All species */}
        <div>
          <h2 className="text-xl font-semibold mb-4">All Species & Systems</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {spectrum.map(s => (
              <SpeciesCard 
                key={s.name} 
                species={s} 
                isSelected={selected.includes(s.name)}
                onClick={() => toggleSelection(s.name)}
              />
            ))}
          </div>
        </div>
        
        {/* Methodology note */}
        <div className="mt-12 p-6 bg-gray-900/30 rounded-xl border border-gray-800">
          <h3 className="text-lg font-semibold mb-3 text-yellow-500">Note on Estimates</h3>
          <p className="text-sm text-gray-400">
            These values are informed estimates based on neuron count, connectivity patterns, 
            behavioral evidence (mirror test, tool use, memory), and neuroimaging where available. 
            They are not measurements. The framework predicts these relationships; empirical 
            validation remains an open problem.
          </p>
          <p className="text-sm text-gray-400 mt-2">
            What we can say with confidence: the gradient exists, humans are not categorically 
            different (only further along), and some non-mammals (crows, octopi) may have higher 
            D than some mammals.
          </p>
        </div>
      </div>
    </main>
  );
}
