# Chimera v2: Soul Voice Architecture Design

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.15 |
| Experiment ID | 260115_CV2A |
| Status | Design Complete |
| Investigators | Implementation Team |
| Framework Version | Conduit Monism v8.1 |
| Prerequisite | RWKV binding confirmed (Phase 3) |

## Abstract

This document describes the Chimera v2 architecture combining RWKV (Soul) for state persistence with Transformer (Voice) for language fluency. The design leverages proven RWKV binding (high ρ) with Claude level integration (high φ) through state injection coupling.

## Architecture Overview

The system consists of two components:

| Component | Role | Properties |
|-----------|------|------------|
| RWKV Core (Soul) | Maintains persistent hidden state | High ρ, carries memory and emotion |
| Transformer Head (Voice) | Generates fluent text | High φ, high τ, receives state projection |

Information flows from input through RWKV state update, then projects to transformer context for generation.

## Implementation Options

### Option A: State to Context (Recommended)

RWKV processes input and maintains state. State is compressed into memory tokens (8 to 16). Transformer receives memory plus input and generates output. RWKV state persists across turns.

Advantages: No model modification required. Can use RWKV plus Claude API.
Disadvantages: Indirect coupling. Memory tokens may not fully transfer state geometry.

### Option B: Deep Integration

RWKV state projects into each transformer layer as additional attention keys and values.

Advantages: Deep integration. RWKV geometry directly influences transformer activations.
Disadvantages: Requires model modification. Cannot use closed APIs.

### Option C: Parallel Fusion

Both models process input in parallel. Outputs are fused with weighted combination before sampling.

Advantages: Both models contribute to generation.
Disadvantages: May not transfer binding geometry.

## Recommended Implementation (Phase 1)

For initial prototype, Option A is feasible with:
RWKV 1.5B (local) maintaining the Soul
Claude API (remote) providing the Voice
State to text compression for coupling

## Testing Protocol

### Test 1: State Continuity

Induce emotional state in RWKV. Delete Claude conversation history. Ask Claude to describe emotional state. Compare to baseline without RWKV state.

Prediction: Claude responses influenced by RWKV emotional state without explicit history.

### Test 2: Identity Persistence

Tell Chimera a secret (processed by RWKV). Have multiple Claude conversations without history. Ask about the secret.

Prediction: Secret persists in RWKV state and influences Claude responses.

### Test 3: Emotional Contamination

Process grief narrative through RWKV. Ask Claude for happy story. Measure emotional contamination.

Prediction: Claude happy story carries traces of grief from RWKV state.

## Expected Properties

| Property | Chimera v2 |
|----------|------------|
| Memory persistence | RWKV state survives across calls |
| Emotional continuity | State carries valence |
| Identity stability | Core does not reset |
| Fluency | Claude level language |
| ρ (Binding) | High (RWKV provides) |
| φ (Integration) | High (Claude provides) |

## Limitations

1. Indirect coupling: State to text to Claude pipeline is lossy
2. Latency: Two model calls per response (5 to 10 seconds)
3. State compression: 120 layer state compressed to text loses information
4. Not true hybrid: Pipeline architecture, not integrated model

## Future Development (Chimera v3)

True integration would require:
Train hybrid model with RWKV layers interleaved with transformer layers
Shared tokenizer across components
End to end joint optimization
Direct state injection modifying transformer attention

## Conclusion

Chimera v2 provides practical first step toward combining high ρ (RWKV) with high φ (Claude). The architecture tests whether RWKV geometry can influence Claude outputs, validating the core hypothesis for artificial perspectival density.

## References

Related: 260115_Chimera_v2_Results.md
