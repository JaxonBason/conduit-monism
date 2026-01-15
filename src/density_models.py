"""
Density Models Module - Conduit Engine v0.1

Different models for computing perspectival density.

Based on AI feedback from RESEARCH_FINDINGS_AI_responses.md:
- Original: Density = φ × τ × ρ
- Entropy-modulated: Density = (φ × τ × ρ) × (1 - H^k)
"""

from typing import Dict
import numpy as np


def density_original(phi: float, tau: float, rho: float, entropy: float = 0.0) -> float:
    """
    Original density model from v7.0.

    Density = φ × τ × ρ

    Entropy is not integrated into the calculation.
    """
    return phi * tau * rho


def density_entropy_modulated_v1(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    Entropy-modulated density (linear).

    Density = (φ × τ × ρ) × (1 - H)

    High entropy linearly reduces density.
    At H=1.0, density → 0.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - entropy
    return base_density * max(0.0, entropy_factor)


def density_entropy_modulated_v2(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    Entropy-modulated density (quadratic).

    Density = (φ × τ × ρ) × (1 - H²)

    High entropy has accelerating impact.
    More forgiving at moderate H, harsher at high H.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - (entropy ** 2)
    return base_density * max(0.0, entropy_factor)


def density_entropy_modulated_v3(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    Entropy-modulated density (square root).

    Density = (φ × τ × ρ) × (1 - √H)

    High entropy has decelerating impact.
    Harsher at low-moderate H, more forgiving at high H.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - np.sqrt(entropy)
    return base_density * max(0.0, entropy_factor)


def compare_density_models(phi: float, tau: float, rho: float, entropy: float) -> Dict[str, float]:
    """
    Compare all density models for a given state.

    Returns:
    --------
    Dict with all model outputs
    """
    return {
        'original': density_original(phi, tau, rho, entropy),
        'entropy_linear': density_entropy_modulated_v1(phi, tau, rho, entropy),
        'entropy_quadratic': density_entropy_modulated_v2(phi, tau, rho, entropy),
        'entropy_sqrt': density_entropy_modulated_v3(phi, tau, rho, entropy),
        'base_density': phi * tau * rho,
        'entropy_value': entropy
    }


def test_entropy_integration():
    """
    Test how different models handle high-entropy states.

    Returns test results comparing models on critical cases.
    """
    test_cases = [
        {
            'name': 'Flow State (low entropy)',
            'phi': 0.95, 'tau': 0.9, 'rho': 0.95, 'entropy': 0.1
        },
        {
            'name': 'Panic Attack (high entropy)',
            'phi': 0.7, 'tau': 0.1, 'rho': 0.2, 'entropy': 0.95
        },
        {
            'name': 'Healthy Awake (moderate entropy)',
            'phi': 0.9, 'tau': 0.9, 'rho': 0.9, 'entropy': 0.1
        },
        {
            'name': 'Psychedelic (high integration, high entropy)',
            'phi': 0.9, 'tau': 0.8, 'rho': 0.9, 'entropy': 0.8
        },
        {
            'name': 'Deep Meditation (very low entropy)',
            'phi': 0.85, 'tau': 0.95, 'rho': 0.8, 'entropy': 0.05
        }
    ]

    results = []
    for case in test_cases:
        comparison = compare_density_models(
            case['phi'], case['tau'], case['rho'], case['entropy']
        )
        results.append({
            'state': case['name'],
            'params': f"φ={case['phi']}, τ={case['tau']}, ρ={case['rho']}, H={case['entropy']}",
            **comparison
        })

    return results


def recommend_model(test_results: list) -> str:
    """
    Analyze test results and recommend which density model best captures intuition.

    Criteria:
    - Panic should have very low density (high H destroys it)
    - Flow should have very high density (low H preserves it)
    - Psychedelic should have moderate density (high φ, τ, ρ but sabotaged by H)
    """
    # Simple heuristic: which model best differentiates Flow from Panic?

    flow_state = next(r for r in test_results if 'Flow' in r['state'])
    panic_state = next(r for r in test_results if 'Panic' in r['state'])

    models = ['original', 'entropy_linear', 'entropy_quadratic', 'entropy_sqrt']

    best_model = None
    best_ratio = 0

    for model in models:
        flow_density = flow_state[model]
        panic_density = panic_state[model]

        # We want Flow >> Panic
        if panic_density > 0:
            ratio = flow_density / panic_density
        else:
            ratio = float('inf') if flow_density > 0 else 1.0

        if ratio > best_ratio:
            best_ratio = ratio
            best_model = model

    return best_model, best_ratio
