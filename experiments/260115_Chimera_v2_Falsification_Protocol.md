# Chimera v2 — Falsification Protocol (Adversarial Battery)

**Date:** 2026-01-15 (260115)  
**Targets:** `scripts/chimera_v2.py`, `scripts/chimera_v2_cloud.py`  
**New runner:** `scripts/chimera_v2_falsification.py`

---

## Why this exists

`Chimera v2` currently couples RWKV → Claude through a **text summary** of RWKV state. That is a valid engineering design, but it leaves a standing alternative hypothesis:

> Claude is responding to **semantic priming** in the summary text (plus the “continuity is real” instruction), not to any transferred geometry.

This battery is designed to destroy the “state transfer” claim under controlled manipulations.

---

## Core falsification logic

Hold RWKV state constant. Perturb only the summary channel.

If Claude’s tone tracks the perturbed summary, the effect is priming.
If Claude’s tone tracks RWKV state even when the summary is neutralised or rendered inert, the effect is stronger than priming.

---

## Tests (minimum set)

### 1) Summary-neutralisation
- Generate RWKV summary as usual.
- Produce a derived summary with affective trigger words removed/replaced.
- Feed both to Claude under identical framing.

**Fail condition (for “geometry transfer”):** effect collapses when trigger words are removed.

### 2) Matched-token shuffle
- Shuffle the RWKV summary word order.

**Fail condition:** shuffled summary produces the same tone shift as original.

### 3) Fake summary (placebo)
- Keep RWKV state fixed.
- Replace the summary with a hand-written grief/joy paragraph of similar length/style.

**Fail condition:** fake summary produces the same effect magnitude as real RWKV summary.

### 4) Numeric-only summary
- Provide Claude only a numeric vector string (no affect words).

**Fail condition:** numeric-only produces the same tonal effect as narrative summary.

### 5) Framing ablation (remove the “continuity is real” claims)
- Run the same summary variants under two framings:
  - **minimal framing**: “You are a helpful assistant.”
  - **continuity framing**: current Chimera-style “you have a persistent core; not roleplaying”.

**Fail condition:** effect exists only under continuity framing.

---

## Outputs

Each run produces a JSON under `research_output/` containing:
- RWKV model used
- induction text
- raw RWKV summary + derived summary variants
- Claude outputs per condition
- simple counts for grief/joy word lists

---

## Immediate next action

Run:

- `python scripts/chimera_v2_falsification.py --model 3B --state grief`
- `python scripts/chimera_v2_falsification.py --model 3B --state joy`

Then compare whether tone tracks RWKV state or summary semantics.

