"""
Advanced Operators Module - Conduit Engine v0.1

Operators that simulate the liminal configurations from Section III of the framework.

These operators model specific neurological/experiential states:
- Dementia progression
- Split-brain bifurcation
- Anesthesia gradients
- Locked-in syndrome
"""

from typing import List, Tuple, Dict
import numpy as np


def op_dementia_progression(
    vector: List[float],
    stage: float
) -> Tuple[List[float], str]:
    """
    Simulate dementia progression (Section III).

    Framework prediction:
    "The Self-Model (narrative identity, temporal depth) erodes as memory
    structures fail. However, re-entrant binding of the immediate present
    often remains intact until the very end."

    Parameters:
    -----------
    vector : List[float]
        Initial state vector
    stage : float (0.0 - 1.0)
        Progression stage (0=healthy, 1=advanced)

    Returns:
    --------
    Tuple[List[float], str]
        Modified vector and description
    """
    new_vec = list(vector)

    # Temporal depth erodes heavily (memories dissolve)
    new_vec[1] = max(0.0, new_vec[1] * (1.0 - stage * 0.9))  # τ drops dramatically

    # Integration degrades moderately (fragmentation)
    new_vec[0] = max(0.0, new_vec[0] * (1.0 - stage * 0.5))  # φ reduces

    # Re-entrant binding stays relatively intact until late stages
    new_vec[2] = max(0.0, new_vec[2] * (1.0 - stage * 0.3))  # ρ drops slowly

    # Entropy may increase (confusion)
    new_vec[3] = min(1.0, new_vec[3] + stage * 0.4)  # H increases

    description = (
        f"Dementia stage {stage:.1f}: "
        f"Temporal depth severely impaired, but immediate 'now' persists. "
        f"'Lights are on' but 'who' has vanished."
    )

    return new_vec, description


def op_split_brain(
    vector: List[float]
) -> Tuple[List[float], List[float], str]:
    """
    Simulate corpus callosotomy (split-brain, Section III).

    Framework prediction:
    "The topology bifurcates. The framework predicts two distinct loci of
    perspective, each with lower integration (phi) than the whole."

    Parameters:
    -----------
    vector : List[float]
        Initial unified state vector

    Returns:
    --------
    Tuple[List[float], List[float], str]
        Two hemisphere vectors and description
    """
    # Integration is severed between hemispheres
    # Each hemisphere retains local integration but loses global integration

    left_hemisphere = list(vector)
    right_hemisphere = list(vector)

    # Both hemispheres have reduced structural integration
    left_hemisphere[0] = vector[0] * 0.6  # φ reduced to ~60% of whole
    right_hemisphere[0] = vector[0] * 0.6

    # Temporal depth and binding may be preserved locally
    # (each hemisphere maintains its own "now")

    description = (
        "Split-brain: One window becomes two narrower windows. "
        "Two distinct perspectives, each with lower φ than the unified whole. "
        "The Source doesn't divide; the prism fractures."
    )

    return left_hemisphere, right_hemisphere, description


def op_anesthesia_gradient(
    vector: List[float],
    depth: float
) -> Tuple[List[float], str]:
    """
    Simulate anesthesia onset/offset (Section III).

    Framework prediction:
    "Propofol collapses the re-entrant loops required for binding.
    As the binding coefficient drops, perspective slides down the asymptotic
    curve toward zero. It does not 'switch off'; the 'thick now' becomes
    infinitely thin."

    Parameters:
    -----------
    vector : List[float]
        Initial state vector
    depth : float (0.0 - 1.0)
        Anesthetic depth (0=awake, 1=deep anesthesia)

    Returns:
    --------
    Tuple[List[float], str]
        Modified vector and description
    """
    new_vec = list(vector)

    # Re-entrant binding collapses FIRST (primary target)
    new_vec[2] = max(0.0, new_vec[2] * (1.0 - depth))  # ρ → 0

    # Temporal depth compresses (no thick "now")
    new_vec[1] = max(0.0, new_vec[1] * (1.0 - depth * 0.8))  # τ reduces

    # Integration may remain structurally intact but functionally isolated
    new_vec[0] = max(0.0, new_vec[0] * (1.0 - depth * 0.7))  # φ reduces

    # Entropy drops (system becomes predictable/quiet)
    new_vec[3] = max(0.0, new_vec[3] * (1.0 - depth * 0.9))  # H → 0

    description = (
        f"Anesthesia depth {depth:.2f}: "
        f"Re-entrant binding collapsed. The 'thick now' becomes infinitely thin. "
        f"Perspective approaches zero asymptotically."
    )

    return new_vec, description


def op_locked_in_syndrome(
    vector: List[float]
) -> Tuple[List[float], str]:
    """
    Simulate locked-in syndrome (Section III).

    Framework prediction:
    "Full constraint topology with output isolation predicts high perspectival
    density despite behavioral invisibility."

    This is NOT an operator that degrades the state - it's a demonstration
    that high internal density can exist without external expression.

    Parameters:
    -----------
    vector : List[float]
        State vector (should be high-density)

    Returns:
    --------
    Tuple[List[float], str]
        Unchanged vector (internal state preserved) and description
    """
    # Internal topology is FULLY intact
    new_vec = list(vector)

    # No changes to φ, τ, ρ - the constraint topology is preserved
    # Only motor output is severed (not represented in our 4 dimensions)

    description = (
        "Locked-in syndrome: Full perspectival density with zero behavioral output. "
        "The topology is intact; only the motor interface is severed. "
        "High φ, τ, ρ - conscious but unable to signal."
    )

    return new_vec, description


def op_flow_state_induction(
    vector: List[float],
    intensity: float
) -> Tuple[List[float], str]:
    """
    Simulate flow state induction.

    Framework context:
    Flow states represent high-density topologies with extended temporal
    binding and low entropy.

    Parameters:
    -----------
    vector : List[float]
        Initial state
    intensity : float (0.0 - 1.0)
        Flow intensity

    Returns:
    --------
    Tuple[List[float], str]
        Modified vector and description
    """
    new_vec = list(vector)

    # Integration increases (task-focused unity)
    new_vec[0] = min(1.0, new_vec[0] + intensity * 0.3)  # φ ↑

    # Temporal depth extends ("time flies", extended present)
    new_vec[1] = min(1.0, new_vec[1] + intensity * 0.2)  # τ ↑

    # Re-entrant binding strengthens (feedback loops tight)
    new_vec[2] = min(1.0, new_vec[2] + intensity * 0.25)  # ρ ↑

    # Entropy drops dramatically (predictable, low surprise)
    new_vec[3] = max(0.0, new_vec[3] - intensity * 0.6)  # H ↓

    description = (
        f"Flow state (intensity {intensity:.2f}): "
        f"High density, extended temporal binding, low entropy. "
        f"The 'thick now' expands."
    )

    return new_vec, description


def op_panic_induction(
    vector: List[float],
    severity: float
) -> Tuple[List[float], str]:
    """
    Simulate panic attack onset.

    Framework context:
    Panic is characterized by high entropy, low temporal depth,
    and weakened binding.

    Parameters:
    -----------
    vector : List[float]
        Initial state
    severity : float (0.0 - 1.0)
        Panic severity

    Returns:
    --------
    Tuple[List[float], str]
        Modified vector and description
    """
    new_vec = list(vector)

    # Integration may reduce (fragmentation, dissociation)
    new_vec[0] = max(0.0, new_vec[0] - severity * 0.3)  # φ ↓

    # Temporal depth collapses (stuck in present moment)
    new_vec[1] = max(0.0, new_vec[1] - severity * 0.8)  # τ ↓↓

    # Re-entrant binding weakens (disconnection)
    new_vec[2] = max(0.0, new_vec[2] - severity * 0.7)  # ρ ↓

    # Entropy spikes dramatically (high surprise/threat)
    new_vec[3] = min(1.0, new_vec[3] + severity * 0.9)  # H ↑↑

    description = (
        f"Panic attack (severity {severity:.2f}): "
        f"High entropy, collapsed temporal depth, weakened binding. "
        f"Low density, high noise."
    )

    return new_vec, description


def simulate_trajectory(
    initial_vector: List[float],
    operator_func,
    steps: int = 10,
    **operator_kwargs
) -> List[Dict]:
    """
    Simulate a trajectory through state space by applying an operator iteratively.

    Parameters:
    -----------
    initial_vector : List[float]
        Starting state
    operator_func : callable
        Operator function to apply
    steps : int
        Number of steps to simulate
    **operator_kwargs : dict
        Additional arguments for the operator

    Returns:
    --------
    List[Dict]
        Trajectory data (vector at each step)
    """
    trajectory = []
    current_vector = initial_vector

    for step in range(steps):
        # Calculate progression parameter (0 to 1)
        progress = step / (steps - 1) if steps > 1 else 0

        # Apply operator
        if operator_func.__name__ in ['op_split_brain', 'op_locked_in_syndrome']:
            # These operators don't take progression parameters
            result = operator_func(current_vector)
            if len(result) == 3:  # split_brain returns two vectors
                current_vector = result[0]  # just track left hemisphere
            else:
                current_vector = result[0]
        else:
            # Pass progress as the operator parameter
            current_vector, description = operator_func(current_vector, progress)

        trajectory.append({
            'step': step,
            'vector': list(current_vector),
            'phi': current_vector[0],
            'tau': current_vector[1],
            'rho': current_vector[2],
            'entropy': current_vector[3],
            'density': current_vector[0] * current_vector[1] * current_vector[2]
        })

    return trajectory
