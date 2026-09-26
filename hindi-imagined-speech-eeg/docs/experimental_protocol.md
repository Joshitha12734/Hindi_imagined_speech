# Experimental Protocol

**Status:** Draft — under development / pending supervisor review.
Nothing in this document should be treated as final until it carries an
explicit sign-off note from Dr. Goyal.

---

## 1. Objective

To design and pilot a controlled recording protocol for collecting EEG
(and, where feasible, EMG) data while participants silently imagine
speaking Hindi words and phrases, producing a dataset suitable for
later exploration of imagined-speech decoding.

## 2. Research Question

Can EEG signals recorded during silent, instructed imagination of a
Hindi word or phrase contain reproducible information about the
intended linguistic target? This protocol is designed to generate data
that can be used to investigate this question — it does not assume the
answer.

## 3. Participant Criteria

- Fluent Hindi speakers (native or high-proficiency), 18–45 years old.
  This range is a **proposed default**, not a theoretically required
  one — chosen as a broad, commonly-used healthy-adult range in
  comparable EEG literature to limit developmental- and aging-related
  EEG variability while keeping recruitment feasible for a student
  team. It should be revisited and explicitly justified (or narrowed/
  widened) with Dr. Goyal rather than treated as fixed by convention.
- No self-reported history of neurological or psychiatric disorders,
  and no history of brain surgery.
- Not currently taking medication known to significantly affect central
  nervous system activity (screened via questionnaire).
- Handedness is recorded for every participant. **No exclusion based on
  handedness is currently planned** — left-handed participants are not
  excluded by default. If the team later decides to restrict the
  initial cohort to right-handed participants only, that decision
  should be made explicitly, with a stated reason (e.g. a specific
  laterality-related confound identified during piloting), rather than
  applied automatically as a literature convention.
- Normal or corrected-to-normal hearing and vision (relevant if audio
  or visual cues are used).

Exact target sample size: **to be determined**, in discussion with Dr.
Goyal, based on available recording time and hardware access. See
`docs/vocabulary_rationale.md` and the open-items list at the end of
this document.

## 4. Screening

Before enrollment, each prospective participant completes a short
screening questionnaire covering:

- Age, handedness, native language, other languages spoken, and
  self-rated Hindi/English proficiency and dominance.
- Neurological and psychiatric history (self-report).
- Current medication use.
- Recent caffeine and nicotine use (same-day).
- Hours of sleep the previous night.
- Hearing and vision status.

Screening responses determine eligibility but are **not** used to make
any claim about a participant's mental-health status. See
`docs/ethical_considerations.md`.

## 5. Consent

Written informed consent is obtained before any recording. The consent
form must, at minimum:

- Explain the purpose of the study in plain language.
- Explain what EEG recording involves and any physical sensations
  associated with electrode placement/gel.
- State explicitly what the data can and cannot reveal (i.e. it is not
  a diagnostic or mental-state-reading procedure).
- Describe how data will be anonymized and stored.
- Describe whether/how data may be released publicly in the future, and
  obtain separate, explicit consent for that specific possibility.
- Describe the right to withdraw at any point, including after
  recording, and what withdrawal means for already-collected data.

Consent template: **to be drafted**, reviewed by Dr. Goyal and the
institutional ethics body before use.

## 6. Experimental Setup

Recording will take place in a quiet room with minimal visual and
auditory distraction. Participants will be seated comfortably at a
consistent viewing distance from a display screen (distance and screen
specifications: **to be determined** once hardware is finalized).

## 7. EEG Acquisition

**Hardware has not yet been finalized.** This section will be completed
with exact device model, channel count, and specifications once
determined, in consultation with Dr. Goyal and based on lab access.

Planned parameters, several marked as placeholders:

| Parameter | Value |
|---|---|
| Device | To be determined |
| Channel count | To be determined (target: as many as available hardware supports) |
| Sampling rate | To be determined (comparable published work uses 128–500 Hz) |
| Reference electrode | To be determined |
| Ground electrode | To be determined |
| EMG channels (optional) | Under discussion — see Section 12 |

## 8. Electrode Placement

Planned: an international 10–20 or 10–10 system layout, exact montage
**to be determined** by final channel count and device. If EMG is used,
placement will target the masseter (jaw) and/or laryngeal region,
following precedent in reviewed literature (see
`docs/literature_review.md`).

## 9. Recording Parameters

**Left as placeholders until hardware is finalized.** Do not treat any
value below as final:

- Band-pass filter range: to be determined (typical published range:
  approximately 0.1–70 Hz; final choice depends on hardware and
  research goals).
- Notch filter: to be determined based on local power-line frequency
  (50 Hz is standard for India, unlike the 60 Hz used in some
  North American datasets we reviewed).
- Recording file format: to be determined (e.g. `.edf` is common in
  comparable studies).

## 10. Trial Structure

Each trial follows this general sequence. Exact durations for each
stage are **proposed defaults**, not final values, and must be piloted
before use in real data collection.

1. Inter-trial rest (blank screen / fixation).
2. Stimulus cue presented (format — text, audio, or both — under
   discussion; see Section 12).
3. Brief preparation interval.
4. Production window: participant either speaks aloud (overt condition)
   or silently imagines speaking (covert condition), depending on the
   block.
5. Post-trial rest before the next trial begins.

A visual summary:

```
REST → CUE → PREPARATION → PRODUCTION (overt or covert) → REST → next trial
```

## 11. Rest Periods

- Inter-trial rest: jittered duration (proposed: 1.5–2.5 s) to avoid
  participants anticipating trial onset.
- A longer resting-state baseline (proposed: ~1 minute, eyes open) is
  planned at the start and end of each session, following common
  practice in the literature reviewed, to provide a noise/state
  reference independent of the task.

## 12. Overt Speech Condition — If Approved

Whether an overt-speech condition is included (participants say the
word aloud, in addition to imagining it) is **under discussion, not yet
finalized**. Rationale for including it: several reviewed datasets pair
overt and covert articulation of the same items, which provides a
built-in way to check that the covert condition is doing something
distinct from actual speech production. If approved, the overt
condition would precede the covert condition for each item, matching
common practice in the literature.

## 13. Covert Speech Condition

Participants are instructed to silently imagine saying the target
word/phrase: no vocalization, no lip or tongue movement, no whispering,
no lip-syncing. The instruction wording itself needs to be piloted and
possibly refined — participants may interpret "imagine saying" in
different ways (imagining hearing the word vs. imagining producing it),
and this ambiguity is a known issue in the literature (see
`docs/literature_review.md`).

## 14. Event Markers

**Decision required.** Two general approaches were considered:

- **Self-initiated marker** (e.g. a participant keypress immediately
  before each utterance/imagination): used in some reviewed studies,
  but a keypress-based marker is not compatible with the target
  population this project's long-term motivation refers to (e.g.
  patients with limited motor function).
- **Cue-locked, fixed-duration marker**: timing is predetermined and
  identical across trials, driven by the stimulus presentation system
  rather than a participant action.

**Current recommendation (not yet finalized): cue-locked marking**, to
keep the protocol closer to what would eventually be usable by a
motor-impaired population, at the cost of being less naturalistic than
self-paced production. This must be discussed with Dr. Goyal and
piloted before being locked in.

### 14.1 Formal Event-Marker Table

Whichever marking method is chosen, every trial must emit a
well-defined, unambiguous set of markers. Proposed marker set (names
and exact generating system to be confirmed during pilot testing):

| Marker | Meaning | Generated by |
|---|---|---|
| `REST_ON` | Inter-trial or baseline rest begins | Stimulus presentation system, on a fixed/jittered timer |
| `CUE_ON` | Stimulus (word/phrase) is presented | Stimulus presentation system, at cue display time |
| `IMAGINE_ON` | Production window begins (participant starts speaking or imagining) | Stimulus presentation system (cue-locked design) or participant action (if a self-initiated design is used instead) |
| `IMAGINE_OFF` | Production window ends | Stimulus presentation system, at fixed window end (cue-locked design) |
| `TRIAL_END` | Trial fully completed, ready for next trial | Stimulus presentation system |

This table should be finalized alongside the event-marking method
decision (Section 14, and Open Item #4 below) and is directly relevant
to the Preprocessing Team's epoching step
(`preprocessing/preprocessing_pipeline.md`, Step 12) — epoching cannot
be correctly implemented until this table is locked.

## 15. Data Naming Conventions

Planned: a BIDS-inspired (not fully BIDS-compliant) naming structure:

```
sub-P001/
└── ses-S001/
    ├── eeg/
    │   └── sub-P001_ses-S001_task-imaginedspeech_eeg.edf
    └── events/
        └── sub-P001_ses-S001_task-imaginedspeech_events.tsv
```

This repository does not currently claim full BIDS compliance. Full
BIDS compliance is a possible future goal, not a current property of
this dataset.

## 16. Quality Checks

Planned per-session quality checks (to be implemented as part of
`code/quality_control/`):

- Verify actual channel count and sampling rate match the intended
  configuration.
- Verify all expected event markers are present and correctly ordered.
- Verify recording duration matches the expected session length.
- Flag sessions with excessive noise or missing data for review before
  inclusion in preprocessing.

## 17. Preprocessing

See `preprocessing/preprocessing_pipeline.md` for the full planned
pipeline (filtering, re-referencing, artifact removal, epoching). No
filtering or epoching parameters are finalized in this document.

## 18. Artifact Handling

Planned approach: ICA-based removal of ocular and cardiac artifacts,
following common practice in the reviewed literature. If EMG is
recorded, EMG-based flagging of trials with detectable subvocalization
is planned as an additional quality-control step (rather than assuming
the covert-speech instruction alone guarantees a clean trial).

## 19. Epoching

Planned: epochs time-locked to the production-window onset marker
(Section 14), with an epoch window and baseline period **to be
finalized jointly with the preprocessing pipeline design** — see
`preprocessing/preprocessing_pipeline.md`.

## 20. Trial Rejection

Criteria for excluding a trial (e.g. excessive artifact, missing
marker, participant error) will be defined and logged systematically in
`preprocessing/preprocessing_log.csv` once real data collection begins.
No rejection criteria have been applied to any data yet, since no data
has been collected.

## 21. Data Storage

Raw and processed data will be stored following the structure in
`data/raw/README.md` and `data/processed/README.md`. Identifiable data
(if any exists outside the anonymized coded dataset, e.g. signed
consent forms) will be stored separately from this repository, under
institutional data-security requirements, and will never be committed
to version control.

## 22. Privacy

See `docs/ethical_considerations.md` for the full privacy policy. In
brief: only anonymized, coded participant data is intended to appear in
this repository; no names, registration numbers, phone numbers, email
addresses, or other directly identifying information will be included.

## 23. Reproducibility

Every preprocessing decision applied to real data (filter values,
component rejection counts, epoch windows, trial exclusions) will be
logged per participant in `preprocessing/preprocessing_log.csv`, so
that processing can be audited and reproduced rather than treated as a
black box.

## 24. Pilot Testing

A small internal pilot (proposed: 2–3 team members as participants,
reduced vocabulary) is planned before recruiting external participants,
to catch protocol issues (confusing instructions, timing problems,
excessive fatigue) cheaply. Pilot data will be clearly separated from
main-study data and is not intended for inclusion in any released
dataset.

## 25. Future Improvements

- Finalize hardware and recording parameters (Sections 7–9).
- Resolve the event-marking method decision (Section 14) through
  piloting.
- Resolve the overt-speech-condition question (Section 12).
- Expand vocabulary coverage following pilot results and supervisor
  input.
- Formalize the consent and ethics-submission documents.

---

## Open Items Requiring Team / Supervisor Decision

| # | Open item | Status |
|---|---|---|
| 1 | Target sample size | Not decided |
| 2 | EEG hardware and channel count | Not decided — depends on lab access |
| 3 | Cue format (text / audio / both) | Not decided |
| 4 | Event-marking method (cue-locked vs. self-initiated) | Leaning cue-locked; not finalized |
| 5 | Whether an overt-speech condition is included | Not decided |
| 6 | Whether EMG monitoring is included | Not decided |
| 7 | Exact trial timings | Draft proposed; not piloted |
| 8 | Ethics/IRB submission | Not yet submitted |

This table should be treated as the live agenda for protocol-finalization
discussions with Dr. Goyal.
