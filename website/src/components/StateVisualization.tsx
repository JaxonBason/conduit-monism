'use client';

import { useMemo } from 'react';
import { Invariants, calculateDensity } from '@/lib/engine';

interface StateVisualizationProps {
  invariants: Invariants;
}

export default function StateVisualization({ invariants }: StateVisualizationProps) {
  const result = useMemo(() => calculateDensity(invariants), [invariants]);
  const { phi, tau, rho, H, kappa } = invariants;
  
  // Calculate visual properties
  const hasStructuralZero = phi === 0 || tau === 0 || rho === 0;
  const density = result.D;
  
  // Brightness based on density
  const brightness = Math.max(0.1, density);
  
  // Stability based on binding (rho)
  // Low rho = flickering, unstable
  const flickerIntensity = rho < 0.2 ? (0.2 - rho) * 5 : 0;
  
  // Size based on integration (phi)
  const size = 40 + (phi * 60);
  
  // Blur based on entropy without coherence
  const effectiveNoise = H * (1 - kappa);
  const blur = effectiveNoise * 20;
  
  // Color based on coherence within entropy
  // High H + High kappa = vibrant (psychedelic)
  // High H + Low kappa = grey (seizure)
  // Low H = white/blue (clarity)
  const hue = H > 0.5 && kappa > 0.5 ? 280 : 200; // Purple for structured chaos, blue for clarity
  const saturation = H > 0.5 ? (kappa * 100) : 20;
  
  // Animation for flicker effect
  const flickerAnimation = flickerIntensity > 0 
    ? `flicker ${0.1 + (1 - flickerIntensity) * 0.4}s infinite`
    : 'none';
  
  return (
    <div className="relative">
      {/* State visualization */}
      <div className="h-48 border border-neutral-800 bg-black flex items-center justify-center overflow-hidden">
        {hasStructuralZero ? (
          // Zero state - collapsed
          <div className="text-center">
            <div 
              className="w-2 h-2 rounded-full bg-neutral-800 mx-auto mb-4"
              style={{ opacity: 0.3 }}
            />
            <div className="text-xs font-mono text-neutral-600">
              {rho === 0 ? 'ρ = 0: No binding' : phi === 0 ? 'φ = 0: No integration' : 'τ = 0: No depth'}
            </div>
            <div className="text-xs font-mono text-neutral-700 mt-1">
              Perspective collapsed
            </div>
          </div>
        ) : (
          // Active state
          <div 
            className="rounded-full transition-all duration-300"
            style={{
              width: `${size}px`,
              height: `${size}px`,
              backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness})`,
              boxShadow: `0 0 ${20 + density * 40}px ${10 + density * 20}px hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.5})`,
              filter: `blur(${blur}px)`,
              animation: flickerAnimation,
            }}
          />
        )}
      </div>
      
      {/* Legend */}
      <div className="mt-4 grid grid-cols-2 gap-2 text-xs font-mono text-neutral-600">
        <div>Size: φ (integration)</div>
        <div>Brightness: D (density)</div>
        <div>Stability: ρ (binding)</div>
        <div>Blur: H×(1-κ) (noise)</div>
      </div>
      
      {/* Interpretation */}
      <div className="mt-4 p-3 border border-neutral-800 bg-neutral-900/50">
        <div className="text-xs font-mono text-neutral-500 mb-1">Visual Interpretation</div>
        <div className="text-sm text-neutral-400">
          {hasStructuralZero ? (
            'The sphere has collapsed. Zero in any structural dimension (φ, τ, ρ) produces zero perspective.'
          ) : density < 0.1 ? (
            'Dim, unstable, barely present. Approaching the threshold of non-experience.'
          ) : density < 0.3 ? (
            'Faint presence. Fragmentary awareness, degraded continuity.'
          ) : density < 0.5 ? (
            'Moderate presence. Functional but not optimal awareness.'
          ) : density < 0.7 ? (
            'Clear, stable presence. Coherent experience with good integration.'
          ) : (
            'Vivid, intensely present. High integration, deep binding, clear signal.'
          )}
        </div>
      </div>
      
      {/* CSS for flicker animation */}
      <style jsx>{`
        @keyframes flicker {
          0%, 100% { opacity: 1; }
          50% { opacity: ${1 - flickerIntensity}; }
        }
      `}</style>
    </div>
  );
}
