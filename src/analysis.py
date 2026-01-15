"""
Analysis Module - Conduit Engine v0.1

Asymptotic analysis and theoretical validation tools.

Tests the core claims of Conduit Monism v7.0:
- Multiplicative vs additive relationships
- Asymptotic thresholds
- Perspectival density gradients
"""

import numpy as np
from typing import List, Tuple, Dict
from .encoder import encode, compute_density


def perspectival_density_multiplicative(phi: float, tau: float, rho: float) -> float:
    """
    Compute perspectival density using MULTIPLICATIVE relationship.

    Per Conduit Monism v7.0:
    "The three conditions are not merely additive; they are multiplicative."

    This means: As any variable → 0, density → 0 asymptotically.
    """
    return phi * tau * rho


def perspectival_density_additive(phi: float, tau: float, rho: float) -> float:
    """
    Compute perspectival density using ADDITIVE relationship (for comparison).

    This is the NULL HYPOTHESIS. If this were true, a system with:
    - φ=0, τ=1, ρ=1 would have density = 2/3 = 0.667

    But the framework predicts it should be ~0 (no integration = no perspective).
    """
    return (phi + tau + rho) / 3


def analyze_asymptotic_behavior(
    resolution: int = 50
) -> Dict[str, np.ndarray]:
    """
    Generate a gradient analysis from high-density to asymptotic zero.

    Tests whether the multiplicative relationship creates the predicted
    asymptotic curve toward zero.

    Returns:
    --------
    Dict containing arrays for visualization and analysis
    """
    # Create a gradient where one variable approaches zero
    phi_range = np.linspace(0.01, 1.0, resolution)
    tau_fixed = 0.9
    rho_fixed = 0.9

    multiplicative = []
    additive = []

    for phi in phi_range:
        mult = perspectival_density_multiplicative(phi, tau_fixed, rho_fixed)
        add = perspectival_density_additive(phi, tau_fixed, rho_fixed)
        multiplicative.append(mult)
        additive.append(add)

    return {
        'phi_range': phi_range,
        'multiplicative': np.array(multiplicative),
        'additive': np.array(additive),
        'tau_fixed': tau_fixed,
        'rho_fixed': rho_fixed
    }


def find_critical_threshold(
    epsilon: float = 0.01,
    fixed_high: float = 0.9
) -> Dict[str, float]:
    """
    Find the critical threshold where perspective becomes "meaningless".

    Per Section VIII Open Questions:
    "Does the asymptotic curve ever truly hit zero? Or is there an effective
    threshold below which the gradient becomes meaningless?"

    Parameters:
    -----------
    epsilon : float
        The threshold for "meaningless" density (e.g., 0.01 = 1%)
    fixed_high : float
        The value held constant for the other two variables

    Returns:
    --------
    Dict with critical thresholds for each variable
    """
    thresholds = {}

    # Find where φ × 0.9 × 0.9 < epsilon
    phi_critical = epsilon / (fixed_high * fixed_high)
    thresholds['phi_critical'] = phi_critical

    # Find where 0.9 × τ × 0.9 < epsilon
    tau_critical = epsilon / (fixed_high * fixed_high)
    thresholds['tau_critical'] = tau_critical

    # Find where 0.9 × 0.9 × ρ < epsilon
    rho_critical = epsilon / (fixed_high * fixed_high)
    thresholds['rho_critical'] = rho_critical

    thresholds['epsilon'] = epsilon
    thresholds['interpretation'] = (
        f"Below φ={phi_critical:.4f} (with τ=ρ={fixed_high}), "
        f"perspectival density < {epsilon} (effectively zero)"
    )

    return thresholds


def test_multiplicative_hypothesis() -> Dict[str, any]:
    """
    Test the multiplicative hypothesis with specific cases from the framework.

    Test cases:
    1. Deep Anesthesia: φ=0.1, τ=0.05, ρ=0.05 → should be near zero
    2. Flow State: φ=0.95, τ=0.9, ρ=0.95 → should be very high
    3. Partial failure: φ=0.0, τ=1.0, ρ=1.0 → should be zero (no integration)

    Returns whether multiplicative model better explains the gradient.
    """
    test_cases = [
        {
            'name': 'Deep Anesthesia',
            'phi': 0.1, 'tau': 0.05, 'rho': 0.05,
            'expected': 'near_zero'
        },
        {
            'name': 'Flow State',
            'phi': 0.95, 'tau': 0.9, 'rho': 0.95,
            'expected': 'very_high'
        },
        {
            'name': 'Zero Integration (No Perspective)',
            'phi': 0.0, 'tau': 1.0, 'rho': 1.0,
            'expected': 'zero'
        },
        {
            'name': 'Zero Binding (No Perspective)',
            'phi': 1.0, 'tau': 1.0, 'rho': 0.0,
            'expected': 'zero'
        },
        {
            'name': 'Partial Integration',
            'phi': 0.5, 'tau': 0.9, 'rho': 0.9,
            'expected': 'moderate'
        }
    ]

    results = []
    for case in test_cases:
        phi, tau, rho = case['phi'], case['tau'], case['rho']
        mult = perspectival_density_multiplicative(phi, tau, rho)
        add = perspectival_density_additive(phi, tau, rho)

        results.append({
            'name': case['name'],
            'phi': phi,
            'tau': tau,
            'rho': rho,
            'multiplicative_density': mult,
            'additive_density': add,
            'expected': case['expected'],
            'multiplicative_matches_theory': (
                (mult < 0.01 and case['expected'] in ['near_zero', 'zero']) or
                (mult > 0.7 and case['expected'] == 'very_high') or
                (0.3 < mult < 0.6 and case['expected'] == 'moderate')
            )
        })

    return {
        'test_cases': results,
        'hypothesis_supported': all(r['multiplicative_matches_theory'] for r in results)
    }


def gradient_comparison(variable: str = 'phi') -> Dict[str, np.ndarray]:
    """
    Compare how different variables affect the gradient to zero.

    Parameters:
    -----------
    variable : str
        Which variable to vary ('phi', 'tau', or 'rho')

    Returns:
    --------
    Dict with comparison data
    """
    resolution = 100
    var_range = np.linspace(0.0, 1.0, resolution)

    densities = []

    for val in var_range:
        if variable == 'phi':
            density = perspectival_density_multiplicative(val, 0.9, 0.9)
        elif variable == 'tau':
            density = perspectival_density_multiplicative(0.9, val, 0.9)
        elif variable == 'rho':
            density = perspectival_density_multiplicative(0.9, 0.9, val)
        else:
            raise ValueError(f"Unknown variable: {variable}")

        densities.append(density)

    return {
        'variable': variable,
        'range': var_range,
        'densities': np.array(densities)
    }


def analyze_liminal_states(db) -> Dict[str, any]:
    """
    Analyze the liminal states from the database to validate framework predictions.

    Parameters:
    -----------
    db : ConduitDB
        The database instance containing seeded states

    Returns:
    --------
    Analysis of liminal state densities and their relationships
    """
    # Query all states by fetching from a mid-point
    neighbors = db.find_neighbors(0.5, 0.5, 0.5, 0.5, n_results=20)

    # Compute density for each
    state_analysis = []
    for neighbor in neighbors:
        meta = neighbor['metadata']
        if 'density' in meta:
            state_analysis.append({
                'name': neighbor['name'],
                'phi': meta.get('phi', 0),
                'tau': meta.get('tau', 0),
                'rho': meta.get('rho', 0),
                'entropy': meta.get('entropy', 0),
                'density': meta['density'],
                'distance_from_midpoint': neighbor['distance']
            })

    # Sort by density
    state_analysis.sort(key=lambda x: x['density'], reverse=True)

    return {
        'states': state_analysis,
        'highest_density': state_analysis[0] if state_analysis else None,
        'lowest_density': state_analysis[-1] if state_analysis else None,
        'density_range': (
            state_analysis[-1]['density'],
            state_analysis[0]['density']
        ) if state_analysis else (0, 0)
    }
