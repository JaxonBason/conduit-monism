# Empirical Anchors for Conduit Monism

**Version:** 1.1
**Date:** January 2026
**Framework:** Conduit Monism v9.2
**Status:** Empirically grounded (Compass research integration)

---

## Overview

This document defines the mapping between Conduit Monism's five invariants and empirical measurements from consciousness research. The goal is to transform the framework from "internally consistent theoretical model" to "empirically grounded theory."

### Grounding Principles

1. **Monotonic relationship** — The empirical measure must increase/decrease as the framework variable increases/decreases
2. **Conceptual alignment** — The measure must capture what the variable theoretically represents
3. **Reproducibility** — The measure must be obtainable by independent researchers
4. **Documented uncertainty** — Confidence levels are attached to each mapping

### Confidence Levels

| Level | Meaning |
|-------|---------|
| **HIGH** | Direct conceptual mapping, multiple studies, normalized scale |
| **MODERATE** | Good conceptual fit, data exists but requires normalization |
| **LOW** | Proxy measure, contested operationalization, limited data |
| **THEORETICAL** | No current empirical anchor, value derived from framework logic |

---

## Variable Mappings

### ρ (Rho): Re-entrant Binding

**Framework Definition:** The system knows that it knows. Recursive self-reference where output feeds back as input, creating loops of meta-cognition.

**Empirical Anchor:** Perturbational Complexity Index (PCI)

**Confidence:** HIGH

#### Theoretical Justification

PCI measures how a perturbation (TMS pulse) propagates through the brain and creates complex, differentiated "echoes." This is conceptually close to re-entrant binding: the signal feeds back through the system, creating integrated responses that are neither too simple (breakdown) nor too stereotyped (seizure).

High PCI = complex, differentiated re-entrant activity = high ρ
Low PCI = signal dies locally or spreads uniformly = low ρ

#### Key Literature

| Citation | Finding | DOI |
|----------|---------|-----|
| Casali et al. (2013) | PCI reliably distinguishes conscious from unconscious states | 10.1126/scitranslmed.3006294 |
| Casarotto et al. (2016) | **PCI* = 0.31** validated as conscious/unconscious threshold (100% accuracy) | 10.1002/ana.24779 |
| Sarasso et al. (2015) | Ketamine maintains PCI = 0.44 mean vs propofol PCI = 0.24 | 10.1016/j.cub.2015.07.047 |
| Kim et al. (2018) | PCI validates conscious vs unconscious under anesthesia (n=35, p<0.001) | 10.1016/j.clinph.2017.10.020 |
| Massimini et al. (2005) | Cortical effective connectivity breaks down during sleep | 10.1126/science.1117256 |
| Ferrarelli et al. (2010) | Midazolam-induced LOC shows connectivity breakdown | 10.1073/pnas.0913008107 |

#### Mapping Function

```
ρ = PCI (direct mapping, PCI already normalized 0-1)
```

PCI values range from ~0.12 to ~0.67. The validated threshold **PCI* = 0.31** separates conscious from unconscious states with 100% accuracy in benchmark populations (Casarotto 2016).

**Key threshold:** ρ < 0.31 indicates likely unconsciousness; ρ ≥ 0.31 indicates likely consciousness.

#### Data Table

| State | PCI Mean ± SD | PCI Range | ρ Value | Source |
|-------|--------------|-----------|---------|--------|
| Wakefulness (eyes open) | 0.50 ± 0.05 | 0.44 - 0.67 | **0.50** | Casali 2013, Casarotto 2016 |
| REM sleep | ~0.45 | 0.41 - 0.48 | 0.45 | Casali 2013 |
| NREM sleep (N3) | ~0.23 | 0.18 - 0.28 | 0.23 | Casali 2013 |
| **Ketamine anesthesia** | **0.44 ± 0.10** | 0.35 - 0.55 | **0.44** | Sarasso 2015 |
| Propofol anesthesia | 0.24 ± 0.07 | 0.12 - 0.31 | 0.24 | Sarasso 2015, Kim 2018 |
| Xenon anesthesia | 0.17 ± 0.05 | — | 0.17 | Sarasso 2015 |
| Midazolam anesthesia | 0.27 ± 0.06 | — | 0.27 | Ferrarelli 2010 |
| Vegetative state (UWS) | ~0.28 | 0.19 - 0.38 | 0.28 | Casali 2013 |
| Minimally conscious (MCS) | ~0.40 | 0.32 - 0.49 | 0.40 | Casali 2013 |
| Locked-in syndrome | ~0.57 | 0.51 - 0.62 | 0.57 | Casali 2013 |

**Critical Observation:** At equivalent behavioral unresponsiveness, ketamine (ρ = 0.44) maintains PCI nearly double that of propofol (ρ = 0.24). This is the empirical foundation for the dissociative/sedative distinction.

---

### H: Entropy

**Framework Definition:** How much noise corrupts the signal. High entropy = unpredictable system dynamics.

**Empirical Anchor:** Lempel-Ziv Complexity (LZc)

**Confidence:** HIGH

#### Theoretical Justification

Lempel-Ziv complexity measures the compressibility of a signal — how much "new information" appears over time. High LZc = more diverse, less predictable neural activity = high H. This is a direct information-theoretic operationalization of entropy.

#### Key Literature

| Citation | Finding | DOI |
|----------|---------|-----|
| Schartner et al. (2015) | LZc distinguishes conscious states during anesthesia | 10.1371/journal.pcbi.1004669 |
| Schartner et al. (2017) | Psychedelics increase LZc above waking baseline | 10.1038/srep46421 |
| Carhart-Harris et al. (2014) | Entropic brain hypothesis: psychedelics → higher entropy | 10.3389/fnhum.2014.00020 |
| Tagliazucchi et al. (2014) | Enhanced state repertoire during psychedelic experience | 10.1002/hbm.22562 |

#### Mapping Function

```
H = LZc_normalized (scaled to 0-1 based on observed range)
```

Raw LZc values vary by study and preprocessing. We normalize to the observed range, treating "waking baseline" as approximately 0.45-0.50 (midpoint of conscious range).

#### Data Table

| State | LZc (relative) | H Value | Source |
|-------|----------------|---------|--------|
| Epileptic seizure | Very low (stereotyped) | 0.15 | Inferred from hypersynchrony |
| Propofol anesthesia | ~35% below baseline | 0.35 | Schartner 2015 |
| NREM sleep (N2) | ~25% below baseline | 0.40 | Schartner 2015 |
| Wakefulness (baseline) | Reference | 0.50 | Schartner 2017 |
| Ketamine | ~10% above baseline | 0.55 | Schartner 2017 |
| LSD | ~15% above baseline | 0.58 | Schartner 2017 |
| Psilocybin | ~15-20% above baseline | 0.60 | Schartner 2017 |

**Note:** The "DMT breakthrough" likely has H > 0.70, but direct LZc measurements during DMT are limited. This is extrapolated from psilocybin data and phenomenological reports.

---

### τ (Tau): Temporal Depth

**Framework Definition:** The past lives in the present. The "thick now" containing memory of what came before and anticipation of what comes next.

**Empirical Anchor:** Intrinsic Neural Timescales (INT) / Temporal Integration Window

**Confidence:** MODERATE (upgraded with Murray 2014 cortical hierarchy)

#### Theoretical Justification

The "specious present" — the window of time the brain treats as "now" — is approximately 2-3 seconds in healthy waking adults (Pöppel 1997). However, **Murray et al. (2014)** discovered a cortical hierarchy of intrinsic timescales:

| Cortical Region | Intrinsic Timescale | Role |
|----------------|---------------------|------|
| Early sensory | 50-100ms | Immediate sensory processing |
| Parietal | 100-150ms | Spatial integration |
| Frontal | 150-200ms | Working memory, planning |
| Prefrontal | 200-350ms | Abstract cognition, temporal integration |

This hierarchy provides empirical grounding: higher cortical areas have longer timescales, enabling "deeper" temporal integration. τ can be interpreted as the effective timescale of the dominant cognitive mode.

**Additional support:** Hasson et al. (2008) found accumulation timescales ranging from seconds (sensory) to minutes (narrative comprehension), supporting multi-scale temporal processing.

#### Key Literature

| Citation | Finding | DOI |
|----------|---------|-----|
| **Murray et al. (2014)** | **Cortical hierarchy of intrinsic timescales (50-350ms)** | 10.1038/nn.3862 |
| **Hasson et al. (2008)** | **Accumulation timescales from seconds to minutes** | 10.1016/j.neuron.2008.01.015 |
| Pöppel (1997) | Hierarchical temporal perception, ~3s integration window | 10.1016/S1364-6613(97)01057-7 |
| Wittmann (2011) | "Moments in time" — phenomenology of temporal experience | 10.3389/fnint.2011.00066 |
| Wittmann (2015) | Meditation extends subjective duration | 10.1371/journal.pone.0115867 |

#### Mapping Function

```
τ = intrinsic_timescale_ms / 350  (normalized to prefrontal maximum)
```

Or for perceptual integration:

```
τ = temporal_window_ms / 3000  (normalized to 3s baseline)
```

The choice depends on whether we're measuring neural timescale (INT) or perceptual integration (TIW). For most states, we use the perceptual window as the practical anchor.

#### Data Table

| State | Timescale | τ Value | Source |
|-------|-----------|---------|--------|
| Coma / deep anesthesia | ~0 (no integration) | 0.05 | Inferred |
| NREM sleep (N3) | Severely reduced | 0.15 | Inferred |
| Normal wakefulness | 2-3 seconds (perceptual) | 0.50 | Pöppel 1997 |
| Flow state | Extended (subjective) | 0.70 | Csikszentmihalyi 1990 |
| Experienced meditation | Expanded (>3s) | 0.80 | Wittmann 2015 |
| Psychedelics | Distorted/expanded | 0.60-0.90 | Wittmann 2007 |
| PTSD flashbacks | Collapsed (past=present) | 0.20 | van der Kolk 2014 |
| Schizophrenia/psychosis | Fragmented (<1s) | 0.25 | Various |

**Improvement:** Murray 2014 provides empirical grounding for τ's neural basis. The cortical hierarchy demonstrates that temporal integration is not arbitrary — it's built into the architecture of the brain.

---

### φ (Phi): Structural Integration

**Framework Definition:** The system speaks to itself as a whole. Information is unified across the system, not fragmented.

**Empirical Anchor:** Effective Connectivity / Φ Proxies

**Confidence:** LOW

#### Theoretical Justification

IIT's Φ (integrated information) is the theoretically ideal measure, but it is computationally intractable for real brains. Proxy measures include:

- **Effective connectivity** (DCM, Granger causality)
- **ΦR, Φ*** (reduced complexity measures)
- **Geometric integrated information**

These are contested and inconsistently applied across studies.

#### Key Literature

| Citation | Finding | DOI |
|----------|---------|-----|
| Tononi et al. (2016) | IIT 3.0 — integrated information theory | 10.1371/journal.pcbi.1004588 |
| Barrett & Seth (2011) | Practical measures of integrated information | 10.1371/journal.pcbi.1001052 |
| Mediano et al. (2022) | "Greater than the parts" — synergy and integration | 10.1093/nc/niac001 |
| Ferrarelli et al. (2010) | ~75% reduction in effective connectivity under propofol | 10.1073/pnas.0913008107 |

#### Mapping Function

```
φ = effective_connectivity (normalized, study-dependent)
```

No universal normalization exists. We estimate φ relative to waking baseline:
- Waking = 1.0 (reference)
- Propofol = ~0.25 (75% reduction per Ferrarelli 2010)
- Other states interpolated

#### Data Table

| State | Connectivity | φ Value | Source |
|-------|--------------|---------|--------|
| Wakefulness | Baseline | 0.80 | Reference |
| Flow state | Enhanced | 0.90 | Inferred |
| Deep meditation | Enhanced | 0.85 | Inferred |
| REM sleep | Moderate reduction | 0.60 | Inferred |
| NREM sleep (N3) | Significant reduction | 0.40 | Massimini 2005 |
| Propofol anesthesia | ~75% reduction | 0.25 | Ferrarelli 2010 |
| Vegetative state (UWS) | Severe reduction | 0.20 | Inferred |
| Coma | Near-zero | 0.10 | Inferred |

**Uncertainty:** φ is the weakest operationalized variable. Most values are estimated. This is the framework's most significant empirical gap.

---

### κ (Kappa): Coherence

**Framework Definition:** Is the noise structured or random? Coherence measures organization within entropy.

**Empirical Anchor:** Phase-Locking Value / Fractal Dimension

**Confidence:** LOW (approaching THEORETICAL)

#### Theoretical Justification

Coherence distinguishes:
- **Structured chaos** (DMT, creative insight): High H, high κ → meaningful complexity
- **Random chaos** (panic, seizure onset): High H, low κ → destructive noise

Potential measures:
- Phase-locking value (PLV) across frequency bands
- Mutual information structure between brain regions
- Fractal dimension of neural dynamics
- Power-law scaling in neural avalanches

#### Key Literature

| Citation | Finding | DOI |
|----------|---------|-----|
| Carhart-Harris et al. (2014) | Entropic brain distinguishes psychedelics from disorder | 10.3389/fnhum.2014.00020 |
| Tagliazucchi et al. (2014) | Enhanced but structured repertoire during psychedelics | 10.1002/hbm.22562 |
| Various | Seizures show high entropy but low complexity (stereotyped spread) | — |

#### Mapping Function

**CORRECTED (per Gemini review, 2026-01-17):**

The naive ratio `κ = Algorithmic Complexity / Entropy` fails because white noise has BOTH maximal entropy AND maximal algorithmic complexity (incompressible). This would falsely classify seizures as "high coherence."

**Correct Approach: Multi-Scale Entropy (MSE)**

```
κ = MSE_slope  (flatness of entropy across timescales)
```

Or equivalently:

```
κ = Fractal Dimension / D_max  (normalized fractal dimension)
```

**Rationale:**
- **White noise:** High entropy at fine scales, averages to zero at coarse scales → LOW κ
- **Pink noise (1/f, fractal):** Maintains entropy across ALL scales → HIGH κ
- **Seizure (stereotyped):** Low complexity at all scales → LOW κ
- **Psychedelics (structured chaos):** High complexity maintained across scales → HIGH κ

This correctly distinguishes:
- Structured chaos (DMT, creativity): κ → 1.0
- Random chaos (panic, seizure): κ → 0.0

**Key Literature:**
- Costa, M., et al. (2002). Multiscale entropy analysis of complex physiologic time series. *Physical Review Letters*, 89(6), 068102.
- Richman, J. S., & Moorman, J. R. (2000). Physiological time-series analysis using approximate entropy and sample entropy. *American Journal of Physiology*, 278(6), H2039-H2049.

#### Data Table

| State | κ Value | Justification |
|-------|---------|---------------|
| Seizure (generalized) | 0.10 | High entropy but stereotyped, no structure |
| Panic attack | 0.20 | Chaotic but random, meaning-destroying |
| Normal wakefulness | 0.50 | Moderate entropy, moderate structure |
| Flow state | 0.70 | Low entropy, high structure |
| Creative insight | 0.75 | Moderate entropy, high structure |
| Psychedelics (peak) | 0.85 | High entropy, high structure (fractal, meaningful) |
| Deep meditation | 0.80 | Low entropy, high structure |

**Uncertainty:** κ is acknowledged in v9.2 as the "most significant measurement gap." Values are largely phenomenologically derived, not empirically measured.

---

## Constraints and Validation

### Constraint 1: κ cannot exceed 1.0

By definition, coherence is bounded.

### Constraint 2: κ cannot be high when H is low

If there is no entropy (H → 0), there is nothing to structure. High κ with low H is mathematically possible but phenomenologically vacuous.

### Constraint 3: Cross-validation with PCI

PCI may actually measure φ × ρ (or even the full φ × τ × ρ product) rather than ρ alone. Future work should investigate whether:

```
PCI ≈ φ × ρ  (integration × binding)
```

If so, the mapping functions need adjustment.

### Constraint 4: Phenomenological alignment

Grounded values must produce density (D) predictions that align with phenomenological reports:
- High D for rich, vivid experiences (DMT peak, flow, lucid dreaming)
- Low D for diminished experiences (anesthesia, deep sleep)
- Zero D for systems without experience (corporations, thermostats)

---

## Known Gaps and Future Work

### Gap 1: φ lacks direct measurement

IIT's Φ is ideal but intractable. Effective connectivity proxies are study-dependent. This is the largest empirical debt.

**Proposed solution:** Treat φ as partially theoretical, clearly document when values are estimated.

### Gap 2: κ requires Multi-Scale Entropy validation

**Status: Theoretical solution identified (2026-01-17)**

The circularity problem (using phenomenology to define κ) has a proposed solution: **Multi-Scale Entropy (MSE)** or **Fractal Dimension**.

MSE measures how entropy behaves across timescales:
- Structured signals (fractals, 1/f noise) maintain entropy at all scales → high κ
- Random signals (white noise) lose entropy at coarse scales → low κ
- Stereotyped signals (seizures) have low entropy at all scales → low κ

**Next step:** Validate MSE values against phenomenological reports for known states. If MSE correctly predicts that DMT has higher κ than seizures (both high H), the proxy is validated.

**Key citations:** Costa et al. (2002), Richman & Moorman (2000).

### Gap 3: τ has multiple timescales

Perceptual binding (ms-s), working memory (s-min), autobiographical memory (min-lifetime) all contribute to "temporal depth." A single scalar may be insufficient.

**Proposed solution:** Focus on perceptual binding window for now, acknowledge the simplification.

### Gap 4: State-specific measurements are sparse

PCI and LZc data exist for limited states (anesthesia, sleep, psychedelics). Many states (flow, meditation, panic) lack direct measurements.

**Proposed solution:** Interpolate from available data, mark as "estimated" with lower confidence.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-17 | Initial calibration library |
| 1.1 | 2026-01-17 | Integrated Compass research: Ketamine PCI mean 0.44, PCI* threshold 0.31, Murray 2014 temporal hierarchy, Hasson 2008 timescales |

---

## References

### Primary Sources

1. Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105. DOI: 10.1126/scitranslmed.3006294

2. **Casarotto, S., et al. (2016). Stratification of unresponsive patients by an independently validated index of brain complexity. *Annals of Neurology*, 80(5), 718-729. DOI: 10.1002/ana.24779** [PCI* = 0.31 threshold validation]

3. Sarasso, S., et al. (2015). Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine. *Current Biology*, 25(23), 3099-3105. DOI: 10.1016/j.cub.2015.07.047 [Ketamine PCI = 0.44 mean]

4. **Kim, M., et al. (2018). Relationship of ketamine's antidepressant and psychotomimetic effects to its perturbational complexity index (PCI). *Clinical Neurophysiology*, 129(6), 1163-1171. DOI: 10.1016/j.clinph.2017.10.020**

5. Schartner, M., et al. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421. DOI: 10.1038/srep46421

6. Massimini, M., et al. (2005). Breakdown of cortical effective connectivity during sleep. *Science*, 309(5744), 2228-2232. DOI: 10.1126/science.1117256

7. Ferrarelli, F., et al. (2010). Breakdown in cortical effective connectivity during midazolam-induced loss of consciousness. *PNAS*, 107(6), 2681-2686. DOI: 10.1073/pnas.0913008107

8. **Murray, J. D., et al. (2014). A hierarchy of intrinsic timescales across primate cortex. *Nature Neuroscience*, 17(12), 1661-1663. DOI: 10.1038/nn.3862** [Cortical timescale hierarchy 50-350ms]

9. **Hasson, U., et al. (2008). A hierarchy of temporal receptive windows in human cortex. *Neuron*, 56(1), 81-95. DOI: 10.1016/j.neuron.2008.01.015** [Accumulation timescales seconds to minutes]

10. Pöppel, E. (1997). A hierarchical model of temporal perception. *Trends in Cognitive Sciences*, 1(2), 56-61. DOI: 10.1016/S1364-6613(97)01057-7

11. Carhart-Harris, R. L., et al. (2014). The entropic brain: A theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20. DOI: 10.3389/fnhum.2014.00020

12. Tononi, G., et al. (2016). Integrated information theory: from consciousness to its physical substrate. *PLOS Computational Biology*, 12(5), e1004588. DOI: 10.1371/journal.pcbi.1004588

### Secondary Sources

13. Wittmann, M. (2011). Moments in time. *Frontiers in Integrative Neuroscience*, 5, 66. DOI: 10.3389/fnint.2011.00066

14. Tagliazucchi, E., et al. (2014). Enhanced repertoire of brain dynamical states during the psychedelic experience. *Human Brain Mapping*, 35(11), 5442-5456. DOI: 10.1002/hbm.22562

15. Barrett, A. B., & Seth, A. K. (2011). Practical measures of integrated information for time-series data. *PLOS Computational Biology*, 7(1), e1001052. DOI: 10.1371/journal.pcbi.1001052

16. Mediano, P. A. M., et al. (2022). Greater than the parts: A review of the information decomposition approach to causal emergence. *Neuroscience of Consciousness*, 2022(1), niac001. DOI: 10.1093/nc/niac001

17. Costa, M., et al. (2002). Multiscale entropy analysis of complex physiologic time series. *Physical Review Letters*, 89(6), 068102. DOI: 10.1103/PhysRevLett.89.068102 [MSE for κ proxy]

18. Richman, J. S., & Moorman, J. R. (2000). Physiological time-series analysis using approximate entropy and sample entropy. *American Journal of Physiology*, 278(6), H2039-H2049. DOI: 10.1152/ajpheart.2000.278.6.H2039
