"""
Encoder Module - Conduit Engine v0.1

Strictly structural encoding following Conduit Monism v7.0 principles.
Only encodes the four sanctioned invariants: φ, τ, ρ, H

NON-NEGOTIABLE: No semantic primitives (valence, self-model, emotion labels)
These must emerge from the geometry, not be hard-coded.
"""

from typing import List


def encode(phi: float, tau: float, rho: float, entropy: float) -> List[float]:
    """
    Encode a topological state using only v7.0 licensed variables.

    Parameters:
    -----------
    phi : float (0.0 - 1.0)
        Structural Integration - how unified/coherent the system is
    tau : float (0.0 - 1.0)
        Temporal Depth - the reach of temporal binding
    rho : float (0.0 - 1.0)
        Re-entrant Binding - recursive feedback strength
    entropy : float (0.0 - 1.0)
        System Surprise/Noise - unpredictability

    Returns:
    --------
    List[float]
        6-dimensional vector: [φ, τ, ρ, H, latent_1, latent_2]
        Latent dimensions are reserved for future discovery (set to 0.0)

    Notes:
    ------
    Removed from earlier versions (per consensus):
    - valence (must emerge, not be assumed)
    - self_model (must emerge, not be assumed)
    """
    # Validate inputs
    assert 0.0 <= phi <= 1.0, "phi must be in range [0.0, 1.0]"
    assert 0.0 <= tau <= 1.0, "tau must be in range [0.0, 1.0]"
    assert 0.0 <= rho <= 1.0, "rho must be in range [0.0, 1.0]"
    assert 0.0 <= entropy <= 1.0, "entropy must be in range [0.0, 1.0]"

    # Add 2 latent dimensions for future discovery (currently 0.0)
    return [float(phi), float(tau), float(rho), float(entropy), 0.0, 0.0]


def compute_density(phi: float, tau: float, rho: float) -> float:
    """
    Compute the 'density' of a state as the product of φ, τ, ρ.

    This is a derived measure, not a primitive.
    High density = high integration, depth, and binding.
    """
    return phi * tau * rho
