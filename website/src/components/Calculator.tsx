'use client';

import { useState, useMemo } from 'react';
import { calculateDensity, presets, Invariants, Preset } from '@/lib/engine';

interface SliderProps {
  label: string;
  symbol: string;
  value: number;
  onChange: (value: number) => void;
  description: string;
}

function Slider({ label, symbol, value, onChange, description }: SliderProps) {
  return (
    <div className="mb-6">
      <div className="flex justify-between items-center mb-2">
        <label className="text-sm font-medium text-gray-300">
          <span className="text-cyan-400 font-mono">{symbol}</span> {label}
        </label>
        <span className="text-lg font-mono text-white">{value.toFixed(2)}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer slider"
      />
      <p className="text-xs text-gray-500 mt-1">{description}</p>
    </div>
  );
}

function DensityBar({ value }: { value: number }) {
  const percentage = Math.min(100, Math.max(0, value * 100));
  
  // Color gradient based on density
  const getColor = () => {
    if (value < 0.1) return 'bg-red-600';
    if (value < 0.3) return 'bg-orange-500';
    if (value < 0.5) return 'bg-yellow-500';
    if (value < 0.7) return 'bg-green-500';
    return 'bg-cyan-400';
  };
  
  return (
    <div className="w-full bg-gray-800 rounded-full h-6 overflow-hidden">
      <div
        className={`h-full ${getColor()} transition-all duration-300 ease-out`}
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
}

function PresetButton({ preset, onClick, isActive }: { preset: Preset; onClick: () => void; isActive: boolean }) {
  const categoryColors: Record<string, string> = {
    human: 'border-blue-500 hover:bg-blue-500/20',
    ai: 'border-purple-500 hover:bg-purple-500/20',
    animal: 'border-green-500 hover:bg-green-500/20',
    altered: 'border-yellow-500 hover:bg-yellow-500/20',
    pathological: 'border-red-500 hover:bg-red-500/20',
  };
  
  return (
    <button
      onClick={onClick}
      className={`px-3 py-1.5 text-xs rounded border transition-all ${categoryColors[preset.category]} ${
        isActive ? 'bg-white/10' : ''
      }`}
    >
      {preset.name}
    </button>
  );
}

export default function Calculator() {
  const [invariants, setInvariants] = useState<Invariants>({
    phi: 0.85,
    tau: 0.8,
    rho: 0.7,
    H: 0.35,
    kappa: 0.7,
  });
  
  const [activePreset, setActivePreset] = useState<string | null>("Human (Baseline Awake)");
  const [selectedCategory, setSelectedCategory] = useState<Preset['category'] | 'all'>('all');
  
  const result = useMemo(() => calculateDensity(invariants), [invariants]);
  
  const updateInvariant = (key: keyof Invariants, value: number) => {
    setInvariants(prev => ({ ...prev, [key]: value }));
    setActivePreset(null);
  };
  
  const loadPreset = (preset: Preset) => {
    setInvariants(preset.invariants);
    setActivePreset(preset.name);
  };
  
  const filteredPresets = selectedCategory === 'all' 
    ? presets 
    : presets.filter(p => p.category === selectedCategory);
  
  const categories: Array<{ value: Preset['category'] | 'all'; label: string }> = [
    { value: 'all', label: 'All' },
    { value: 'human', label: 'Human' },
    { value: 'animal', label: 'Animal' },
    { value: 'ai', label: 'AI' },
    { value: 'altered', label: 'Altered' },
    { value: 'pathological', label: 'Pathological' },
  ];
  
  return (
    <div className="max-w-4xl mx-auto">
      <div className="grid md:grid-cols-2 gap-8">
        {/* Sliders */}
        <div className="bg-gray-900/50 rounded-xl p-6 border border-gray-800">
          <h3 className="text-lg font-semibold mb-6 text-gray-200">The Five Invariants</h3>
          
          <Slider
            label="Integration"
            symbol="φ"
            value={invariants.phi}
            onChange={(v) => updateInvariant('phi', v)}
            description="How unified is information across the system?"
          />
          
          <Slider
            label="Temporal Depth"
            symbol="τ"
            value={invariants.tau}
            onChange={(v) => updateInvariant('tau', v)}
            description="How much does the past constrain the present?"
          />
          
          <Slider
            label="Binding"
            symbol="ρ"
            value={invariants.rho}
            onChange={(v) => updateInvariant('rho', v)}
            description="Does the system observe its own states?"
          />
          
          <Slider
            label="Entropy"
            symbol="H"
            value={invariants.H}
            onChange={(v) => updateInvariant('H', v)}
            description="How much noise/chaos in the system?"
          />
          
          <Slider
            label="Coherence"
            symbol="κ"
            value={invariants.kappa}
            onChange={(v) => updateInvariant('kappa', v)}
            description="Is the entropy structured or random?"
          />
        </div>
        
        {/* Results */}
        <div className="bg-gray-900/50 rounded-xl p-6 border border-gray-800">
          <h3 className="text-lg font-semibold mb-6 text-gray-200">Perspectival Density</h3>
          
          {/* Main D value */}
          <div className="text-center mb-6">
            <div className="text-6xl font-mono font-bold text-white mb-2">
              {result.D.toFixed(3)}
            </div>
            <div className="text-sm text-gray-400">D = φ × τ × ρ × [(1 - √H) + (H × κ)]</div>
          </div>
          
          <DensityBar value={result.D} />
          
          {/* Breakdown */}
          <div className="mt-6 space-y-2 text-sm font-mono">
            <div className="flex justify-between text-gray-400">
              <span>Structural Base (φ×τ×ρ):</span>
              <span>{result.structuralBase.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-gray-400">
              <span>Entropy Penalty (1-√H):</span>
              <span>{result.entropyPenalty.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-gray-400">
              <span>Coherence Recovery (H×κ):</span>
              <span>{result.coherenceRecovery.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-gray-400 border-t border-gray-700 pt-2">
              <span>Entropy Modulator:</span>
              <span>{result.entropyModulator.toFixed(4)}</span>
            </div>
          </div>
          
          {/* Interpretation */}
          <div className="mt-6 p-4 bg-gray-800/50 rounded-lg">
            <h4 className="text-sm font-semibold text-gray-300 mb-2">Interpretation</h4>
            <p className="text-sm text-gray-400">{result.interpretation}</p>
          </div>
          
          {/* Warnings */}
          {result.warnings.length > 0 && (
            <div className="mt-4 space-y-2">
              {result.warnings.map((warning, i) => (
                <div key={i} className="p-3 bg-yellow-900/20 border border-yellow-700/50 rounded text-xs text-yellow-200">
                  ⚠️ {warning}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
      
      {/* Presets */}
      <div className="mt-8 bg-gray-900/50 rounded-xl p-6 border border-gray-800">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-gray-200">Presets</h3>
          <div className="flex gap-2">
            {categories.map(cat => (
              <button
                key={cat.value}
                onClick={() => setSelectedCategory(cat.value)}
                className={`px-3 py-1 text-xs rounded transition-all ${
                  selectedCategory === cat.value
                    ? 'bg-cyan-500 text-black'
                    : 'bg-gray-800 text-gray-400 hover:bg-gray-700'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>
        
        <div className="flex flex-wrap gap-2">
          {filteredPresets.map(preset => (
            <PresetButton
              key={preset.name}
              preset={preset}
              onClick={() => loadPreset(preset)}
              isActive={activePreset === preset.name}
            />
          ))}
        </div>
        
        {activePreset && (
          <div className="mt-4 p-4 bg-gray-800/50 rounded-lg">
            <p className="text-sm text-gray-400">
              {presets.find(p => p.name === activePreset)?.description}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
