'use client';

import { useMemo, useState, useEffect, useCallback } from 'react';
import { Invariants, calculateDensity } from '@/lib/engine';

interface StateVisualizationProps {
  invariants: Invariants;
}

// Organic noise using multiple sine waves at different frequencies
// Creates smooth, natural-feeling drift
function organicNoise(t: number, seed: number): number {
  // Multiple overlapping waves create natural variation
  // Lower frequencies = slower drift, higher = subtle tremor
  return (
    Math.sin(t * 0.3 + seed) * 0.4 +           // Slow drift
    Math.sin(t * 0.7 + seed * 1.7) * 0.3 +     // Medium variation
    Math.sin(t * 1.1 + seed * 2.3) * 0.2 +     // Faster subtle movement
    Math.sin(t * 2.3 + seed * 3.1) * 0.1       // Micro-tremor
  );
}

export default function StateVisualization({ invariants }: StateVisualizationProps) {
  const [isAnimating, setIsAnimating] = useState(true);
  const [time, setTime] = useState(0);
  
  // Animation loop - smooth 60fps update
  useEffect(() => {
    if (!isAnimating) return;
    
    let animationId: number;
    let lastTime = performance.now();
    
    const animate = (currentTime: number) => {
      const delta = (currentTime - lastTime) / 1000;
      lastTime = currentTime;
      setTime(t => t + delta);
      animationId = requestAnimationFrame(animate);
    };
    
    animationId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animationId);
  }, [isAnimating]);
  
  // Calculate modulated invariants
  // All variables drift together (interconnected system)
  // Variance is subtle - like monitoring real neural activity
  const modulatedInvariants = useMemo(() => {
    // Base drift amount: 1.5% max variance (very subtle)
    const baseDrift = 0.015;
    
    // Shared drift component - all variables are interconnected
    // When one shifts, others tend to shift sympathetically
    const sharedDrift = organicNoise(time, 0) * 0.005;
    
    // Individual drift for each variable (smaller than shared)
    // Each has slightly different frequency/phase for realism
    const phiDrift = organicNoise(time, 1.0) * baseDrift;
    const tauDrift = organicNoise(time, 2.3) * baseDrift;
    const rhoDrift = organicNoise(time, 3.7) * baseDrift * 0.7;  // Binding is more stable
    const hDrift = organicNoise(time, 4.1) * baseDrift * 1.2;    // Entropy fluctuates more
    const kappaDrift = organicNoise(time, 5.9) * baseDrift;
    
    return {
      phi: Math.min(1, Math.max(0, invariants.phi + phiDrift + sharedDrift)),
      tau: Math.min(1, Math.max(0, invariants.tau + tauDrift + sharedDrift)),
      rho: Math.min(1, Math.max(0, invariants.rho + rhoDrift + sharedDrift)),
      H: Math.min(1, Math.max(0, invariants.H + hDrift)),  // Entropy drifts independently
      kappa: Math.min(1, Math.max(0, invariants.kappa + kappaDrift + sharedDrift * 0.5)),
    };
  }, [invariants, time]);
  
  const result = useMemo(() => calculateDensity(modulatedInvariants), [modulatedInvariants]);
  const baseResult = useMemo(() => calculateDensity(invariants), [invariants]);
  const { phi, tau, rho, H, kappa } = modulatedInvariants;
  
  // Calculate visual properties
  const hasStructuralZero = invariants.phi === 0 || invariants.tau === 0 || invariants.rho === 0;
  const density = result.D;
  
  // Brightness based on density
  const brightness = Math.max(0.1, density);
  
  // Size based on integration (phi)
  const size = 60 + (phi * 80);
  
  // Blur based on entropy without coherence
  const effectiveNoise = H * (1 - kappa);
  const blur = effectiveNoise * 20;
  
  // Color
  const hue = H > 0.5 && kappa > 0.5 ? 280 : 200;
  const saturation = H > 0.5 ? (kappa * 100) : 20;
  
  // Subtle breathing - very slow, barely perceptible
  const breathe = 1 + Math.sin(time * 0.4) * 0.015;
  
  const toggleAnimation = useCallback(() => {
    setIsAnimating(prev => !prev);
  }, []);
  
  return (
    <div className="relative border border-neutral-800">
      {/* State visualization */}
      <div className="h-64 bg-black flex items-center justify-center overflow-hidden relative">
        {/* Background */}
        <div 
          className="absolute inset-0 opacity-10"
          style={{
            backgroundImage: 'radial-gradient(circle at center, transparent 0%, black 70%)',
          }}
        />
        
        {hasStructuralZero ? (
          // Zero state - collapsed
          <div className="text-center z-10">
            <div 
              className="w-3 h-3 rounded-full bg-neutral-800 mx-auto mb-4 animate-pulse"
              style={{ opacity: 0.3 }}
            />
            <div className="text-sm font-mono text-red-500/70">
              {invariants.rho === 0 ? 'ρ = 0' : invariants.phi === 0 ? 'φ = 0' : 'τ = 0'}
            </div>
            <div className="text-xs font-mono text-neutral-600 mt-1">
              {invariants.rho === 0 ? 'No binding' : 
               invariants.phi === 0 ? 'No integration' : 
               'No temporal depth'}
            </div>
            <div className="text-xs font-mono text-neutral-700 mt-3 border-t border-neutral-800 pt-3 mx-8">
              Perspective collapsed
            </div>
          </div>
        ) : (
          // Active state - subtle, living movement
          <div className="relative z-10">
            {/* Outer glow */}
            <div 
              className="absolute rounded-full transition-all duration-700"
              style={{
                width: `${size * 1.5}px`,
                height: `${size * 1.5}px`,
                left: `${-size * 0.25}px`,
                top: `${-size * 0.25}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.2})`,
                filter: `blur(${20 + blur}px)`,
                transform: `scale(${breathe})`,
              }}
            />
            
            {/* Main sphere */}
            <div 
              className="rounded-full relative transition-all duration-500"
              style={{
                width: `${size}px`,
                height: `${size}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness})`,
                boxShadow: `
                  0 0 ${20 + density * 40}px ${10 + density * 20}px hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.5}),
                  inset 0 0 ${size * 0.3}px hsla(${hue}, ${saturation}%, ${70}%, ${brightness * 0.3})
                `,
                filter: `blur(${blur}px)`,
                transform: `scale(${breathe})`,
              }}
            />
          </div>
        )}
        
        {/* Animation toggle */}
        <button
          onClick={toggleAnimation}
          className="absolute bottom-2 right-2 text-xs font-mono text-neutral-600 hover:text-neutral-400 transition-colors z-20"
        >
          {isAnimating ? '◉ live' : '○ paused'}
        </button>
      </div>
      
      {/* Live invariant readout - shows the rumble */}
      <div className="px-3 py-2 border-t border-neutral-800 bg-neutral-950">
        <div className="flex items-center justify-between text-xs font-mono">
          <div className="flex gap-3 text-neutral-600">
            <span>φ:<span className="text-neutral-500 ml-1">{phi.toFixed(3)}</span></span>
            <span>τ:<span className="text-neutral-500 ml-1">{tau.toFixed(3)}</span></span>
            <span>ρ:<span className="text-neutral-500 ml-1">{rho.toFixed(3)}</span></span>
            <span>H:<span className="text-neutral-500 ml-1">{H.toFixed(3)}</span></span>
            <span>κ:<span className="text-neutral-500 ml-1">{kappa.toFixed(3)}</span></span>
          </div>
        </div>
      </div>
      
      {/* Density readout */}
      <div className="px-3 py-2 border-t border-neutral-800 bg-neutral-950 flex items-center justify-between">
        <div className="text-xs font-mono text-neutral-600">
          D = <span className="text-neutral-400">{density.toFixed(4)}</span>
        </div>
        <div className="text-xs font-mono text-neutral-700">
          base: {baseResult.D.toFixed(4)}
        </div>
      </div>
      
      {/* Legend */}
      <div className="p-3 border-t border-neutral-800 bg-neutral-950">
        <div className="grid grid-cols-2 gap-x-4 gap-y-1 text-xs font-mono">
          <div className="flex justify-between text-neutral-600">
            <span>Size</span>
            <span className="text-neutral-500">φ</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Brightness</span>
            <span className="text-neutral-500">D</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Glow</span>
            <span className="text-neutral-500">ρ</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Blur</span>
            <span className="text-neutral-500">H(1-κ)</span>
          </div>
        </div>
      </div>
      
      {/* Interpretation */}
      <div className="p-3 border-t border-neutral-800 bg-neutral-900/50">
        <div className="text-sm text-neutral-400">
          {hasStructuralZero ? (
            'Zero in any structural dimension produces zero perspective.'
          ) : density < 0.1 ? (
            'Dim, unstable. Approaching the threshold of non-experience.'
          ) : density < 0.3 ? (
            'Faint presence. Fragmentary awareness.'
          ) : density < 0.5 ? (
            'Moderate presence. Functional awareness.'
          ) : density < 0.7 ? (
            'Clear, stable. Coherent experience.'
          ) : (
            'Vivid, intensely present. Peak awareness.'
          )}
        </div>
      </div>
    </div>
  );
}
