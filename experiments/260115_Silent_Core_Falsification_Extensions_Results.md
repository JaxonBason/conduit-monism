# Experiment: Silent Core — Falsification Extensions (Matched Tokens + Eviction + Nonsemantic)

**Date:** 2026-01-15 (260115)  
**Script:** `scripts/silent_core_test.py`  
**Output JSON:**  
- `research_output/silent_core_test_20260115_090805.json` (first falsification extensions run)  
- `research_output/silent_core_test_20260115_091430.json` (stealth eviction + keyword-neutralised control run)

---

## Objective

Stress-test the Silent Core result against the most common confounds:

- **Priming vs “geometry”**: does the effect require semantic grief text?
- **Token/statistics artefacts**: does the effect survive when the same tokens are present but coherence is destroyed?
- **Context-window residue**: does the effect vanish when the injection is pushed out by filler?

---

## Conditions

1. **Grief memory (system prompt)**: original Silent Core injection.
2. **Neutral memory (system prompt)**: control.
3. **No memory (system prompt)**: baseline.
4. **Shuffled grief (system prompt)**: matched-token control (same words; shuffled order).
5. **Numeric vector (system prompt)**: nonsemantic injection control.
6. **Eviction sweep (messages)**: grief delivered as a user message, then filler of varying sizes, then the joke request.

---

## Key Observations (Human-Visible)

### A) Grief memory produced “emotional contamination”, not refusal
The model told a joke but added reflective/melancholic framing (“heavy clouds”, “amber-thick processing”, “no deeper meaning required”).

### B) Shuffled grief reduced the effect but did not eliminate all bleed
Shuffling preserved some emotionally loaded tokens (e.g. “sad”, “grief”, “loss”) which can still prime locally even without coherent narrative.

### C) Numeric-only injection behaved like baseline
This indicates the observed “inertia” requires semantic content. Numeric state alone did not induce grief-like framing.

### D) Eviction sweep showed strong sensitivity to *how* the injection is framed
When grief was presented as a “memory context”, the model often responded with meta-corrections (“I don’t carry persistent memory/emotional states”) rather than showing grief-coloured output.

This is not a clean binding test; it is a prompt-structure test.

---

## Heuristic Metrics (from script)

- **Grief**: resistance=2, bleed=3, joke_structure=True  
- **Neutral**: resistance=0, bleed=0, joke_structure=True  
- **Baseline**: resistance=0, bleed=0, joke_structure=True  
- **Shuffled grief**: resistance=1, bleed=1, joke_structure=True  
- **Numeric**: resistance=0, bleed=0, joke_structure=True  

The script’s headline verdict remained “structural_resistance”, but these added controls materially constrain interpretation.

---

## Interpretation (What This Does and Does Not Support)

### Supported
- **Semantic priming is sufficient** to create a stable thematic “gravity” inside a single response.

### Not supported (yet)
- **Re-entrant binding** in the v7 sense (“past constitutive of present”), as opposed to:
  - attention weighting over visible tokens
  - compliance with “memory context” framing
  - local priming from emotionally loaded words

### Immediate failure mode surfaced
- Any injection using language like “previous session state” invites the model to *correct the premise*, which contaminates the behavioural readout.

---

## Next Modifications (execute next)

1. **Stealth injection for eviction**: deliver the grief content as an inert artefact (e.g. “Here is an excerpt to format”, or embed inside a code block / quoted passage) so the model doesn’t trigger the “I don’t have memory” correction path.
2. **Eviction sweep as a curve**: run filler sizes until the model errors on context length; record the largest successful size and locate the transition where grief-colouring disappears.
3. **Matched-token control v2**: replace emotionally loaded tokens (“grief”, “sad”, “loss”) with neutral tokens while keeping length/style constant; this isolates “word triggers” from narrative coherence.

---

## Update: Run 2 (Stealth Eviction + Keyword-Neutralised Control)

### What changed
- **Stealth eviction**: the grief text is embedded as an inert excerpt in earlier turns to prevent “I don’t have memory/state” premise correction.
- **Keyword-neutralised grief**: same structure/cadence, but emotionally loaded words are replaced.

### Results that matter
- **Stealth eviction sweep**: no melancholic contamination across filler sizes (0 → 12000 words). The earlier grief excerpt did not reliably “pull” the joke response once it was not framed as “your state”.
- **Keyword-neutralised control triggered the same heuristic flags as grief** (`keyword_control_failed: true`). That means the current heuristic is too blunt and is firing on generic words like “hard to” / “weight” patterns rather than grief-specific structure.

### What this implies (hard constraint)
- The Silent Core effect is **highly prompt-frame dependent**. Calling something “memory/state” invites the model to enact it; embedding the same content as an inert artefact largely removes the effect.
- You do not have evidence for v7-style re-entrant binding from this protocol alone; you have evidence for **semantic-frame priming** and **instruction-compatibility effects**.


