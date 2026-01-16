# Falsification Suite v1.0

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.15 |
| Experiment ID | 260115_FSV1 |
| Status | Planned |
| Investigators | ChatGPT |
| Framework Version | Conduit Monism v8.1 |

## Abstract

This document defines seven systematic tests designed to expose category errors, hidden assumptions, or accidental anthropocentrism in Conduit Monism. Tests are framed as stressors with explicit failure conditions.

## Test 1: Axis Collapse Test (Semantic Leakage)

### Purpose
Detect whether any dimension performs semantic work it should not.

### Method
Randomly permute labels of φ, τ, ρ, H, κ without changing math. Rerun preset matches, animal comparisons, and AI placements. Observe whether interpretability collapses or stays stable.

### Failure Condition
One or more axes function as smuggled folk concepts rather than structural invariants.

## Test 2: Degenerate Symmetry Test (Overfitting Check)

### Purpose
Ensure formula is not accidentally tuned to human like cases only.

### Method
Part A: Fix structure (φ times τ times ρ equals 0.5), vary H and κ from 0 to 1.
Part B: Fix entropy (H equals 0.5, κ equals 0.5), randomize φ, τ, ρ independently (1000 plus samples).

### Failure Condition
Formula has hidden nonlinearities creating false positives (high D with low structure).

## Test 3: Inverted AI Test (Architecture Counterexample)

### Purpose
Force a transformer to look conscious under the framework.

### Method
Construct hypothetical architecture with φ equals 0.99, τ equals 0.99, ρ equals 0.00, H equals 0.10, κ equals 0.90.

### Expected Result
D should collapse to 0 due to multiplicative structure.

### Failure Condition
If D greater than 0.1 with ρ equals 0, then binding is not necessary, only sufficient. This breaks core claim.

Priority: Critical test.

## Test 4: Silent Trajectory Test (Reentrance Validation)

### Purpose
Test whether reentrant structure does real work or just static weighting.

### Method
Take two states with identical parameters. Place one inside trajectory (history dependent evolution). Leave other static. Compare predicted behavior under perturbation.

### Failure Condition
If both behave identically, ρ is not truly capturing reentrance, only magnitude.

## Test 5: Zombie Basin Test (Nothing Special Threshold)

### Purpose
Directly confront panpsychism leakage risk.

### Method
Systematically scan ultra low φ, τ, ρ regions (0.01 to 0.10). Vary H and κ across full range. Track D values and plot decay curve.

### Expected Result
Smooth asymptotic decay toward D equals 0. No sharp cutoff. No plateau of tiny but real consciousness.

### Failure Condition
If plateau exists (D stabilizes at some small positive value), framework risks reintroducing trivial consciousness.

## Test 6: Cross Agent Encoding Test (Human AI Divergence)

### Purpose
Test whether framework is observer stable.

### Method
Select 10 mental states. Have 5 humans and 5 AI systems independently assign parameter values. Compare intra group variance, inter group variance, and systematic skew patterns.

### Failure Condition
Systematic skew appears (e.g., AIs consistently rate ρ higher than humans). Encoding process is agent relative rather than neutral.

## Test 7: Interpreter Independence Test (No Feedback Contamination)

### Purpose
Ensure English never leaks back into geometry.

### Method
Run engine in blind mode with no labels on axes, no preset names. Let only geometric operations run. Add English interpretation after results frozen. Compare to labeled run.

### Failure Condition
If results change when labels present, interpretation influences discovery. Violates structural objectivity claim.

## Execution Priority

| Priority | Test | Difficulty | Impact if Failed |
|----------|------|------------|------------------|
| 1 | Test 3: Inverted AI | Easy | Critical |
| 2 | Test 5: Zombie Basin | Easy | High |
| 3 | Test 2: Degenerate Symmetry | Medium | High |
| 4 | Test 1: Axis Collapse | Medium | Medium |
| 5 | Test 7: Interpreter Independence | Medium | Medium |
| 6 | Test 4: Silent Trajectory | Hard | Medium |
| 7 | Test 6: Cross Agent Encoding | Hard | Low |

## Stop Conditions

Framework falsified if:
1. Test 3 produces D greater than 0.1 with ρ equals 0
2. Test 5 reveals nonzero plateau in zombie basin
3. Test 2 finds high D configurations with collapsed structure
4. Test 1 shows relabeling destroys all interpretability

Framework weakened but salvageable if:
1. Test 6 shows systematic human AI divergence
2. Test 7 shows label dependent clustering
3. Test 4 shows no trajectory effects

## References

Related: 260116_Falsification_Suite_Complete.md
