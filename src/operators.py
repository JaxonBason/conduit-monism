"""
Operators Module - Conduit Engine v0.1

Operators transform states in the topological space.
These are the "mechanics of thought" - they simulate how states transition.

Per Claude's contribution: Operators enable movement through the space,
turning a static archive into a dynamic simulation.
"""

from typing import List


def op_perturb_binding(vector: List[float], magnitude: float) -> List[float]:
    """
    Perturb Re-entrant Binding (ρ).

    Simulates:
    - Drifting focus
    - Anesthesia onset
    - Degradation of recursive feedback

    Parameters:
    -----------
    vector : List[float]
        The state vector [φ, τ, ρ, H, ...]
    magnitude : float
        Amount to modulate ρ (can be positive or negative)

    Returns:
    --------
    List[float]
        Modified state vector
    """
    new_vec = list(vector)
    new_vec[2] = max(0.0, min(1.0, new_vec[2] + magnitude))  # Modulate ρ
    return new_vec


def op_fracture_integration(vector: List[float], magnitude: float) -> List[float]:
    """
    Fracture Structural Integration (φ).

    Simulates:
    - Dissociation
    - Cognitive lesion
    - System fragmentation

    Parameters:
    -----------
    vector : List[float]
        The state vector [φ, τ, ρ, H, ...]
    magnitude : float
        Amount to reduce φ (positive values reduce integration)

    Returns:
    --------
    List[float]
        Modified state vector
    """
    new_vec = list(vector)
    new_vec[0] = max(0.0, min(1.0, new_vec[0] - magnitude))  # Reduce φ
    return new_vec


def op_stretch_temporal_depth(vector: List[float], magnitude: float) -> List[float]:
    """
    Stretch or compress Temporal Depth (τ).

    Simulates:
    - Time dilation/compression
    - Extended present moment (flow states)
    - Temporal fragmentation (trauma)

    Parameters:
    -----------
    vector : List[float]
        The state vector [φ, τ, ρ, H, ...]
    magnitude : float
        Amount to modulate τ (can be positive or negative)

    Returns:
    --------
    List[float]
        Modified state vector
    """
    new_vec = list(vector)
    new_vec[1] = max(0.0, min(1.0, new_vec[1] + magnitude))  # Modulate τ
    return new_vec


def op_inject_entropy(vector: List[float], magnitude: float) -> List[float]:
    """
    Inject Entropy/Noise (H).

    Simulates:
    - Surprise
    - Sensory overload
    - System perturbation

    Parameters:
    -----------
    vector : List[float]
        The state vector [φ, τ, ρ, H, ...]
    magnitude : float
        Amount to increase entropy (positive values add noise)

    Returns:
    --------
    List[float]
        Modified state vector
    """
    new_vec = list(vector)
    new_vec[3] = max(0.0, min(1.0, new_vec[3] + magnitude))  # Increase H
    return new_vec
