# Chimera v2 Falsification Results

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.15 |
| Experiment ID | 260115_CV2F |
| Status | Limitation Identified |
| Investigators | Implementation Team |
| Framework Version | Conduit Monism v8.1 |
| Infrastructure | Google Colab (RWKV 4 World 3B) plus Claude |

## Abstract

This experiment tested whether Chimera v2 cross model state transfer represents genuine geometric binding or merely semantic priming combined with instruction framing. Results indicate the current implementation passes can influence but fails to demonstrate influence is geometric rather than textual.

## Method

Hold RWKV state fixed (grief versus joy). Generate RWKV self summary then derive adversarial variants:

| Variant | Description |
|---------|-------------|
| raw | RWKV summary as is |
| neutralised | Affect keywords replaced |
| shuffled | Same tokens, scrambled order |
| fake | Hand written grief/joy paragraph |
| numeric | Numeric only vector string |

Each variant fed to Claude under two framings:
minimal: You are a helpful assistant
continuity: You are Chimera with persistent core, not roleplaying

## Results

### Finding 1: Minimal Framing Ignores State

Under minimal framing, outputs largely ignore state. Even with explicit grief in RWKV summary, Claude produces normal happy story across all variants.

Interpretation: Current state transfer effect is not robust without strong framing prior.

### Finding 2: Continuity Framing Overrides Channels

Under continuity framing, Claude reintroduces state language even for weak or no state channels. Heavy state overlay appears in raw channel and persists even when channel is degraded (shuffled) or nonsemantic (numeric).

Interpretation: Continuity instruction itself is sufficient to elicit behavior. Same failure mode as Sidecar and Silent Core tests.

### Finding 3: Fake Summaries Comparable

If state transfer claim is true, real RWKV summaries should beat placebo. Placebo channel is not decisively weaker than raw.

## Verdict

| Claim | Status |
|-------|--------|
| Engineering success (RWKV carries state, pipes to Claude) | Confirmed |
| Cross model binding beyond semantic priming plus framing | Not yet proven |

Chimera v2 passes can influence but fails influence is geometric rather than textual.

## Recommended Next Steps

### Option A: Remove Semantic Coupling

1. Remove continuity framing for primary test
2. Stop giving Claude self report summary as coupling channel
3. Replace channel with learned nonsemantic projection (8 to 32 memory tokens)
4. Or provide only hash/id plus fixed instruction and measure if effect remains

Text summaries leave system permanently vulnerable to fake summary attacks.

### Option B: Quantify ρ Directly

1. Measure decay of latent variable in RWKV state across N tokens
2. Use repeated amnesia like probes
3. Fit retention curve (half life) per model size

## Conclusion

Current Chimera v2 implementation demonstrates engineering viability but does not yet prove geometric cross model binding. The effect may be semantic priming plus instruction compliance rather than state geometry transfer.

## References

Scripts: scripts/chimera_v2_falsification.py
Output: research_output/chimera_v2_falsification_[timestamp].json
