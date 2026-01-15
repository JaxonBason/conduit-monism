#!/usr/bin/env python3
"""
Conduit Engine v0.1
===================

The executable implementation of Conduit Monism v7.0.

This system:
- Encodes mental states as structural topology (not semantics)
- Stores states in a persistent vector database
- Uses operators to simulate state transitions
- Discovers patterns through geometric proximity

Per the AI deliberation consensus:
- Gemini: Provided the substrate (database structure)
- ChatGPT: Enforced constraints (no premature semantic commitment)
- Claude: Provided the mechanics (operators)

The system is an INSTRUMENT, not a mind.
It discovers structure. Humans interpret meaning.
"""

from src.database import ConduitDB
from src.encoder import encode
from src.operators import (
    op_perturb_binding,
    op_fracture_integration,
    op_stretch_temporal_depth,
    op_inject_entropy
)


def print_banner():
    """Display startup banner."""
    print("=" * 60)
    print("CONDUIT ENGINE v0.1")
    print("Conduit Monism v7.0 - Structural Topology System")
    print("=" * 60)
    print()


def seed_liminal_cases(db: ConduitDB):
    """
    Seed the database with 'liminal cases' - anchor points in the space.

    These are states that define the boundaries and extremes of the topology.
    Per Grok's contribution: these provide the necessary seed data.
    """
    print("Seeding liminal cases (anchor states)...")
    print()

    # Baseline: Healthy, awake, integrated consciousness
    db.seed_state(
        name="Healthy Awake",
        phi=0.9, tau=0.9, rho=0.9, entropy=0.1,
        description="Baseline integrated consciousness"
    )

    # Asymptotic zero: Complete loss of integration
    db.seed_state(
        name="Deep Anesthesia",
        phi=0.1, tau=0.05, rho=0.05, entropy=0.0,
        description="Near-zero consciousness"
    )

    # High entropy, fragmented state
    db.seed_state(
        name="Panic Attack",
        phi=0.7, tau=0.1, rho=0.2, entropy=0.95,
        description="High entropy, low temporal depth, weak binding"
    )

    # High density flow state
    db.seed_state(
        name="Flow State",
        phi=0.95, tau=0.9, rho=0.95, entropy=0.1,
        description="Maximum integration and binding, low noise"
    )

    # Dissociated state
    db.seed_state(
        name="Dissociation",
        phi=0.4, tau=0.6, rho=0.3, entropy=0.5,
        description="Fractured integration, moderate binding"
    )

    # Deep meditation
    db.seed_state(
        name="Deep Meditation",
        phi=0.85, tau=0.95, rho=0.8, entropy=0.05,
        description="High temporal depth, very low entropy"
    )

    print()


def run_simulation_1(db: ConduitDB):
    """
    Simulation 1: Fracturing Integration

    Question: If we take a healthy state and fracture its integration (φ),
    what does it become geometrically?

    This tests whether the system can 'discover' that trauma leads to
    dissociation/panic without being explicitly told.
    """
    print("=" * 60)
    print("SIMULATION 1: Fracturing Integration")
    print("=" * 60)
    print()
    print("Starting with: Healthy Awake state (φ=0.9, τ=0.9, ρ=0.9, H=0.1)")
    print("Applying operator: Fracture φ by -0.4 (simulating trauma/dissociation)")
    print()

    # Create healthy state vector
    healthy_vec = encode(0.9, 0.9, 0.9, 0.1)

    # Apply operator: fracture integration
    fractured_vec = op_fracture_integration(healthy_vec, 0.4)

    # Query database to see what this is geometrically close to
    neighbors = db.query_vector(fractured_vec, n_results=3)

    print("Resulting state is geometrically closest to:")
    for i, neighbor in enumerate(neighbors, 1):
        print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")

    print()
    print("Interpretation: The system discovered this relationship structurally,")
    print("not because we labeled it, but because the geometry maps this way.")
    print()


def run_simulation_2(db: ConduitDB):
    """
    Simulation 2: Entropy Injection

    Question: What happens when we inject high entropy into a flow state?
    """
    print("=" * 60)
    print("SIMULATION 2: Injecting Entropy into Flow")
    print("=" * 60)
    print()
    print("Starting with: Flow State (φ=0.95, τ=0.9, ρ=0.95, H=0.1)")
    print("Applying operator: Inject entropy +0.8")
    print()

    flow_vec = encode(0.95, 0.9, 0.95, 0.1)
    perturbed_vec = op_inject_entropy(flow_vec, 0.8)

    neighbors = db.query_vector(perturbed_vec, n_results=3)

    print("Resulting state is geometrically closest to:")
    for i, neighbor in enumerate(neighbors, 1):
        print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")

    print()


def run_exploration_mode(db: ConduitDB):
    """
    Interactive exploration mode.

    Allows manual queries of the topological space.
    """
    print("=" * 60)
    print("EXPLORATION MODE")
    print("=" * 60)
    print()
    print("Query the topological space by providing φ, τ, ρ, H values.")
    print("Type 'quit' to exit.")
    print()

    while True:
        try:
            cmd = input("Enter state (φ τ ρ H) or 'quit': ").strip()
            if cmd.lower() in ['quit', 'exit', 'q']:
                break

            values = [float(x) for x in cmd.split()]
            if len(values) != 4:
                print("Error: Please provide exactly 4 values (φ τ ρ H)")
                continue

            phi, tau, rho, entropy = values

            neighbors = db.find_neighbors(phi, tau, rho, entropy, n_results=3)

            print(f"\nNearest neighbors to (φ={phi}, τ={tau}, ρ={rho}, H={entropy}):")
            for i, neighbor in enumerate(neighbors, 1):
                print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")
            print()

        except ValueError:
            print("Error: Invalid input. Please enter 4 numbers separated by spaces.")
        except KeyboardInterrupt:
            print("\n")
            break


def main():
    """Main execution function."""
    print_banner()

    # Initialize database
    db = ConduitDB()
    print(f"Database initialized. Current state count: {db.count()}")
    print()

    # Seed if empty
    if db.count() == 0:
        seed_liminal_cases(db)
    else:
        print(f"Database already contains {db.count()} states. Skipping seeding.")
        print()

    # Run simulations
    run_simulation_1(db)
    run_simulation_2(db)

    # Interactive mode
    print("Starting interactive exploration mode...")
    print()
    run_exploration_mode(db)

    print()
    print("=" * 60)
    print("SESSION ENDED")
    print("The Conduit persists. The structure remains.")
    print("=" * 60)


if __name__ == "__main__":
    main()
