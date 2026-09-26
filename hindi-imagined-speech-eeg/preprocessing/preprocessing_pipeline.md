# Preprocessing Pipeline

**Status:** Design stage. No implementation exists yet
(`code/preprocessing/` currently contains only a placeholder README).
**No filtering, referencing, or epoching values below are final** —
they depend on the EEG hardware ultimately used, the recording
environment, pilot-data signal quality, and supervisor approval.

## Pipeline Overview

```
Raw EEG (+ EMG, if used)
        ↓
Data import
        ↓
Channel verification
        ↓
Sampling-rate verification
        ↓
Visual quality inspection
        ↓
Bad-channel identification (+ interpolation, if needed)
        ↓
Filtering (band-pass)
        ↓
Power-line noise handling (notch filter)
        ↓
Re-referencing
        ↓
Artifact identification and removal
        ↓
Event synchronization
        ↓
Epoch extraction
        ↓
Baseline correction (where justified)
        ↓
Trial-level quality control
        ↓
Final processed EEG
```

## Step-by-Step Rationale

### 1. Data import
Load the raw continuous recording (format to be finalized alongside
hardware selection) together with its synchronized event markers.
Without correctly imported event markers, no later step can be aligned
to the task.

### 2. Channel verification
Confirm the actual recorded channel count and labels match the intended
montage before proceeding. Catches hardware/configuration errors early,
before they propagate through the whole pipeline.

### 3. Sampling-rate verification
Confirm the actual sampling rate matches the intended configuration.
Downstream filter design (Step 6) and epoch timing depend on this being
correct.

### 4. Visual quality inspection
A researcher visually reviews the raw trace for gross problems (flat
channels, extreme noise, disconnection artifacts) before any automated
step runs, since automated methods can silently fail on badly corrupted
data.

### 5. Bad-channel identification
Channels that are flat, saturated, or excessively noisy across the
whole session are identified and either excluded or interpolated from
neighboring channels. Exact detection method/thresholds: **to be
determined**, likely following an automated + visual-confirmation
approach similar to that used in ZuCo 2.0 and comparable studies.

### 6. Filtering (band-pass)
Removes frequency content outside the range relevant to EEG activity of
interest, improving signal-to-noise ratio for later steps.
**Cutoff values: to be determined** based on hardware and research
goals; comparable published work uses ranges roughly between 0.1–70 Hz.

### 7. Power-line noise handling (notch filter)
Removes electrical mains interference. **India's mains frequency is 50
Hz** — this is a concrete, hardware-independent parameter we can commit
to now, unlike the band-pass cutoffs above, and differs from the 60 Hz
notch used in some North American datasets referenced in our literature
review.

### 8. Re-referencing
EEG amplitude is inherently relative to a reference point; re-
referencing (e.g. to linked mastoids, average reference, or another
scheme) is a standard step that affects downstream analysis.
**Method: to be determined** based on hardware and standard practice
for the chosen electrode system.

### 9. Artifact identification
Identifies segments/components likely driven by eye movement, blinks,
muscle activity, or cardiac signal rather than brain activity of
interest — necessary because these artifacts are typically much larger
in amplitude than the underlying EEG signal.

### 10. Artifact identification and removal
Some method is used to isolate and remove ocular and cardiac artifact
components. **ICA is not treated as a mandatory default** — it is one
candidate method, used in comparable prior work (ZuCo 2.0's MARA,
Kostulin et al.'s Infomax ICA), but the right choice depends on the
hardware, channel count, and data actually collected. Whatever method is
chosen, **removal of a component must be justified by evidence that it
is genuinely an artifact, not simply because it looks unusual** —
aggressive or unjustified component removal risks discarding real
signal in a domain (imagined speech) that already has a difficult
signal-to-noise problem. Exact method and component-selection criteria:
**to be determined** during pipeline implementation, and logged per
participant via `pipeline_commit` in `preprocessing/preprocessing_log.csv`
so the exact code version behind any removal decision is traceable.

If EMG is recorded (see `docs/experimental_protocol.md`, Section 7),
EMG signal will additionally be used at the trial level (Step 12) to
flag covert-speech trials showing detectable subvocalization — rather
than relying on the EEG artifact-removal step alone to handle this.

### 11. Event synchronization
Confirms that event markers (cue onset, production-window onset/offset,
etc. — see `docs/experimental_protocol.md`, Section 14) are correctly
aligned with the continuous EEG timeline before epoching.

### 12. Epoch extraction
Continuous EEG is cut into per-trial segments ("epochs") time-locked to
a chosen event marker (currently proposed: production-window onset).
**Exact epoch window (start/end relative to the marker): to be
determined**, jointly by the Dataset Preparation and Preprocessing
teams, consistent with the trial timing proposed in
`docs/experimental_protocol.md`, Section 10.

### 13. Baseline correction
Where justified, epoch amplitude is corrected relative to a pre-event
baseline period (e.g. the inter-trial rest period), to control for
slow drifts unrelated to the task. **Baseline window: to be
determined** alongside the epoch window above.

### 14. Trial-level quality control
Each epoch is checked against quality criteria (e.g. amplitude
thresholds, EMG contamination where available, missing-marker trials)
and flagged as included/excluded. All such decisions are logged in
`preprocessing/preprocessing_log.csv` for auditability — see
`docs/data_dictionary.md` for the log schema.

### 15. Final processed EEG
Clean, epoched, quality-controlled data, organized following
`data/processed/README.md`, ready for feature extraction and modeling
(`code/analysis/`).

## What Is Explicitly Not Yet Decided

- Exact band-pass filter cutoffs
- Re-referencing method
- Bad-channel detection thresholds
- ICA algorithm and component-rejection criteria
- Epoch window and baseline window
- Trial-level quality-control thresholds

These will be filled in — and this document updated — once EEG hardware
is finalized and pilot data exists to validate parameter choices
against.
