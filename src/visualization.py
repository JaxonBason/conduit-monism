"""
Visualization Module - Conduit Engine v0.1

Tools for visualizing the topological space, trajectories, and analysis results.

Note: Uses matplotlib for visualization. Install with: pip install matplotlib
"""

try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("Warning: matplotlib not installed. Visualization features disabled.")
    print("Install with: pip install matplotlib")


def plot_asymptotic_curve(analysis_data: dict, save_path: str = None):
    """
    Plot the asymptotic behavior: multiplicative vs additive.

    Parameters:
    -----------
    analysis_data : dict
        Output from analysis.analyze_asymptotic_behavior()
    save_path : str, optional
        Path to save the figure
    """
    if not VISUALIZATION_AVAILABLE:
        print("Matplotlib not available. Skipping visualization.")
        return

    phi_range = analysis_data['phi_range']
    multiplicative = analysis_data['multiplicative']
    additive = analysis_data['additive']

    plt.figure(figsize=(10, 6))
    plt.plot(phi_range, multiplicative, 'b-', linewidth=2, label='Multiplicative (φ × τ × ρ)')
    plt.plot(phi_range, additive, 'r--', linewidth=2, label='Additive ((φ + τ + ρ) / 3)')

    plt.axhline(y=0.01, color='gray', linestyle=':', alpha=0.5, label='Threshold (ε=0.01)')
    plt.xlabel('φ (Structural Integration)', fontsize=12)
    plt.ylabel('Perspectival Density', fontsize=12)
    plt.title('Asymptotic Behavior: Multiplicative vs Additive\n(τ=0.9, ρ=0.9 fixed)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    else:
        plt.show()

    plt.close()


def plot_gradient_comparison(gradient_data: dict, save_path: str = None):
    """
    Plot how each variable affects the density gradient.

    Parameters:
    -----------
    gradient_data : dict
        Output from analysis.gradient_comparison()
    save_path : str, optional
        Path to save the figure
    """
    if not VISUALIZATION_AVAILABLE:
        return

    var = gradient_data['variable']
    var_range = gradient_data['range']
    densities = gradient_data['densities']

    plt.figure(figsize=(10, 6))
    plt.plot(var_range, densities, 'g-', linewidth=2)
    plt.fill_between(var_range, 0, densities, alpha=0.3, color='green')

    plt.xlabel(f'{var} ({"φ" if var=="phi" else "τ" if var=="tau" else "ρ"})', fontsize=12)
    plt.ylabel('Perspectival Density', fontsize=12)
    plt.title(f'Density Gradient: Varying {var}\n(other variables = 0.9)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(0, max(densities) * 1.1)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    else:
        plt.show()

    plt.close()


def plot_3d_state_space(states: list, save_path: str = None):
    """
    Plot states in 3D space (φ, τ, ρ).

    Parameters:
    -----------
    states : list
        List of dicts with 'phi', 'tau', 'rho', 'name', 'density'
    save_path : str, optional
        Path to save the figure
    """
    if not VISUALIZATION_AVAILABLE:
        return

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Extract coordinates
    phi = [s['phi'] for s in states]
    tau = [s['tau'] for s in states]
    rho = [s['rho'] for s in states]
    densities = [s['density'] for s in states]
    names = [s['name'] for s in states]

    # Color by density
    scatter = ax.scatter(phi, tau, rho, c=densities, cmap='viridis',
                        s=200, alpha=0.6, edgecolors='black', linewidth=1.5)

    # Label each point
    for i, name in enumerate(names):
        ax.text(phi[i], tau[i], rho[i], f'  {name}', fontsize=8)

    ax.set_xlabel('φ (Integration)', fontsize=11)
    ax.set_ylabel('τ (Temporal Depth)', fontsize=11)
    ax.set_zlabel('ρ (Re-entrant Binding)', fontsize=11)
    ax.set_title('Topological State Space\n(Color = Perspectival Density)', fontsize=14)

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
    cbar.set_label('Density (φ × τ × ρ)', fontsize=10)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    else:
        plt.show()

    plt.close()


def plot_trajectory(trajectory: list, title: str = "State Trajectory", save_path: str = None):
    """
    Plot a trajectory through state space over time.

    Parameters:
    -----------
    trajectory : list
        List of dicts with 'step', 'phi', 'tau', 'rho', 'entropy', 'density'
    title : str
        Plot title
    save_path : str, optional
        Path to save the figure
    """
    if not VISUALIZATION_AVAILABLE:
        return

    steps = [t['step'] for t in trajectory]
    phi = [t['phi'] for t in trajectory]
    tau = [t['tau'] for t in trajectory]
    rho = [t['rho'] for t in trajectory]
    entropy = [t['entropy'] for t in trajectory]
    density = [t['density'] for t in trajectory]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(title, fontsize=16)

    # φ trajectory
    axes[0, 0].plot(steps, phi, 'b-', linewidth=2, marker='o')
    axes[0, 0].set_ylabel('φ (Integration)', fontsize=11)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_ylim(-0.05, 1.05)

    # τ trajectory
    axes[0, 1].plot(steps, tau, 'g-', linewidth=2, marker='o')
    axes[0, 1].set_ylabel('τ (Temporal Depth)', fontsize=11)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_ylim(-0.05, 1.05)

    # ρ trajectory
    axes[1, 0].plot(steps, rho, 'r-', linewidth=2, marker='o')
    axes[1, 0].set_ylabel('ρ (Re-entrant Binding)', fontsize=11)
    axes[1, 0].set_xlabel('Step', fontsize=11)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_ylim(-0.05, 1.05)

    # Density trajectory
    axes[1, 1].plot(steps, density, 'purple', linewidth=2, marker='o')
    axes[1, 1].plot(steps, entropy, 'orange', linewidth=2, marker='s', alpha=0.6, label='Entropy')
    axes[1, 1].set_ylabel('Value', fontsize=11)
    axes[1, 1].set_xlabel('Step', fontsize=11)
    axes[1, 1].legend(['Density (φ×τ×ρ)', 'Entropy (H)'], fontsize=9)
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    else:
        plt.show()

    plt.close()


def plot_liminal_states_comparison(states: list, save_path: str = None):
    """
    Create a bar chart comparing liminal states across all dimensions.

    Parameters:
    -----------
    states : list
        List of state dicts with dimensions and density
    save_path : str, optional
        Path to save the figure
    """
    if not VISUALIZATION_AVAILABLE:
        return

    names = [s['name'] for s in states]
    phi = [s['phi'] for s in states]
    tau = [s['tau'] for s in states]
    rho = [s['rho'] for s in states]
    entropy = [s['entropy'] for s in states]
    density = [s['density'] for s in states]

    x = np.arange(len(names))
    width = 0.15

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    fig.suptitle('Liminal States: Dimensional Comparison', fontsize=16)

    # Top: Individual dimensions
    ax1.bar(x - 1.5*width, phi, width, label='φ (Integration)', color='blue', alpha=0.8)
    ax1.bar(x - 0.5*width, tau, width, label='τ (Temporal Depth)', color='green', alpha=0.8)
    ax1.bar(x + 0.5*width, rho, width, label='ρ (Re-entrant Binding)', color='red', alpha=0.8)
    ax1.bar(x + 1.5*width, entropy, width, label='H (Entropy)', color='orange', alpha=0.8)
    ax1.set_ylabel('Value', fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(names, rotation=45, ha='right')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_ylim(0, 1.1)

    # Bottom: Density
    colors = plt.cm.viridis(np.array(density) / max(density))
    ax2.bar(x, density, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Perspectival Density (φ×τ×ρ)', fontsize=11)
    ax2.set_xlabel('State', fontsize=11)
    ax2.set_xticks(x)
    ax2.set_xticklabels(names, rotation=45, ha='right')
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    else:
        plt.show()

    plt.close()


def print_text_visualization(states: list):
    """
    Print a text-based visualization of states (for when matplotlib is unavailable).

    Parameters:
    -----------
    states : list
        List of state dicts
    """
    print("\n" + "="*80)
    print("STATE SPACE VISUALIZATION (Text Mode)")
    print("="*80)

    for state in states:
        name = state['name']
        phi = state['phi']
        tau = state['tau']
        rho = state['rho']
        entropy = state['entropy']
        density = state['density']

        print(f"\n{name}:")
        print(f"  φ (Integration):       {'█' * int(phi * 40)} {phi:.2f}")
        print(f"  τ (Temporal Depth):    {'█' * int(tau * 40)} {tau:.2f}")
        print(f"  ρ (Re-entrant Binding):{'█' * int(rho * 40)} {rho:.2f}")
        print(f"  H (Entropy):           {'█' * int(entropy * 40)} {entropy:.2f}")
        print(f"  Density (φ×τ×ρ):       {'█' * int(density * 40)} {density:.3f}")

    print("\n" + "="*80 + "\n")
