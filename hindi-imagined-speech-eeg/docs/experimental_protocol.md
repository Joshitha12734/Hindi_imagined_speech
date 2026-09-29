# Experimental Protocol

**Status:** Current protocol-aligned draft.  
This document reflects the current supervisor/committee protocol supplied for the study. Items explicitly identified as requiring confirmation remain marked as pending.

---

## 1. Objective

To collect a controlled EEG dataset while healthy adult Hindi-speaking participants silently imagine speaking Hindi words. The resulting dataset will support research into Hindi imagined speech / inner-speech BCI and proof-of-concept classification of imagined-word conditions and rest.

## 2. Research Question

Can EEG signals recorded during silent, instructed imagination of Hindi words contain reproducible information about the intended linguistic target?

The study is designed to investigate this question; it does not assume a successful decoding result in advance.

## 3. Participant Criteria

The current committee protocol specifies:

- Healthy adult Hindi-speaking volunteers.
- Target sample: **10 participants**.
- Age range: **18–35 years**.
- Screening is completed before enrollment/recording.
- Written informed consent is obtained before EEG recording.

The supplied protocol should be treated as the source of truth for the final inclusion/exclusion wording. Do not reintroduce the previous 18–45-year proposed range from the earlier draft.

## 4. Screening and Consent

Participants complete the study's approved screening procedure before recording. Written informed consent is obtained before any recording.

Consent and participant-identifying documents are stored separately from coded EEG research data and are not committed to this repository.

## 5. Experimental Setup

Participants are seated comfortably in the recording environment and view the Hindi stimulus on a display. The task is designed as a silent imagined-speech task.

## 6. EEG Acquisition

The current protocol identifies the EEG hardware as requiring confirmation between the proposed systems, including **OpenBCI Cyton+Daisy and Emotiv EPOC+**. Until the final device is confirmed, this repository must not hard-code a device-specific channel count, montage, sampling rate, reference, ground, or file format.

Once the actual hardware is used, the acquisition metadata must record the exact device and configuration.

## 7. Trial Structure

Each experimental trial follows the current protocol timing:

1. **500 ms — fixation**
2. **300 ms — Hindi word display**
3. **3000 ms — imagined speech**
4. **1000 ms — rest/reset**

Visual summary:

```text
FIXATION (500 ms)
        ↓
HINDI WORD (300 ms)
        ↓
IMAGINED SPEECH (3000 ms)
        ↓
REST / RESET (1000 ms)
        ↓
NEXT TRIAL
```

Participants silently imagine saying the displayed Hindi word during the 3000 ms production window. The task does not require overt speech.

## 8. Recording Structure

The current protocol specifies:

| Stage | Trials | Approx. duration |
|---|---:|---:|
| Practice | 55 | ~4 min |
| Main Block 1 | 110 | ~8.8 min |
| Main Block 2 | 110 | ~8.8 min |
| Main Block 3 | 110 | ~8.8 min |
| Main Block 4 | 110 | ~8.8 min |

The final session/break arrangement should follow the approved implementation.

## 9. Stimulus Classes

The current recording protocol specifies **6 Hindi word classes/stimuli**. The final approved stimulus list should be kept synchronized between the stimulus-presentation software, vocabulary documentation, event logs, and trial metadata.

## 10. Covert / Imagined Speech Condition

Participants silently imagine speaking the displayed Hindi word. They should not overtly speak during the imagined-speech window. The recording protocol is intended to capture EEG associated with the instructed covert task rather than actual vocal production.

## 11. Event Markers

The repository uses the following marker vocabulary for synchronizing trial stages with EEG:

| Marker | Meaning |
|---|---|
| `REST_ON` | Rest/reset begins |
| `CUE_ON` | Hindi word is presented |
| `IMAGINE_ON` | Imagined-speech window begins |
| `IMAGINE_OFF` | Imagined-speech window ends |
| `TRIAL_END` | Trial is complete |

The marker-generation mechanism and measured marker-to-EEG latency/jitter must be validated with the final hardware before the main study.

See [`docs/event_marker_protocol.md`](event_marker_protocol.md).

## 12. Data Naming

Use a participant/session structure that keeps raw EEG, event information, and processed data separate. A BIDS-inspired naming convention may be used without claiming full BIDS compliance:

```text
sub-P001/
└── ses-S001/
    ├── eeg/
    │   └── sub-P001_ses-S001_task-imaginedspeech_eeg.<native-format>
    └── events/
        └── sub-P001_ses-S001_task-imaginedspeech_events.tsv
```

The exact native EEG file format depends on the hardware actually used.

## 13. Metadata

### Participant metadata

`metadata/participant_metadata.csv` stores coded participant-level information required by the approved study and for interpreting data quality. Direct identifiers must not be stored here.

### Trial metadata

`metadata/trial_metadata.csv` stores one row per trial, including coded participant/session identifiers, block/trial number, stimulus/class information, event timing, and quality-control fields.

The schema must remain synchronized with the actual event stream.

## 14. Quality Control

Before processing a session, verify:

- Recording duration
- Actual channel count
- Actual sampling rate
- Presence and order of expected event markers
- Marker timing/latency
- Missing or corrupted EEG segments
- Excessive noise or bad channels
- Trial-level quality flags
- Consistency between raw event logs and trial metadata

Any rejected session or trial must be documented rather than silently removed.

## 15. Preprocessing

The preprocessing pipeline should be applied only after the actual EEG hardware and recording configuration are confirmed.

The general workflow is:

1. Inspect raw recording integrity.
2. Verify acquisition metadata.
3. Verify event markers.
4. Identify bad channels/segments.
5. Apply the approved filtering strategy.
6. Re-reference according to the approved acquisition/preprocessing configuration.
7. Handle ocular/cardiac and other artifacts using the approved method.
8. Epoch around the synchronized `IMAGINE_ON` event.
9. Perform trial-level quality checks/rejection.
10. Save processed data and a reproducible preprocessing log.

Final filter cutoffs, epoch windows, baseline treatment, artifact thresholds, and device-specific settings should be finalized from the actual hardware/pilot data and supervisor-approved protocol. They must not be invented in advance.

## 16. Artifact Handling

Eye and muscle artifacts are important quality-control considerations for imagined-speech EEG. The exact artifact-removal/rejection procedure should be selected after hardware confirmation and pilot testing and then documented in the preprocessing log.

## 17. Epoching

The primary task epoch should be anchored to the synchronized `IMAGINE_ON` marker so that the 3000 ms imagined-speech window can be identified consistently across trials.

Any additional baseline or analysis window must be documented explicitly in the preprocessing configuration.

## 18. Trial Rejection

A trial may be flagged for review/rejection when, for example, it has missing or corrupted EEG, invalid/missing markers, excessive artifact, or a documented participant/protocol error.

Every rejection must have a recorded reason in the preprocessing/QC log.

## 19. Data Storage and Privacy

- Raw and processed EEG are kept separate.
- Participant identifiers are coded.
- Names, registration numbers, contact information, consent forms, and other directly identifying records must not be committed to GitHub.
- Consent and identifying documents remain under the appropriate institutional storage process.
- Any future data sharing must follow the approved consent and institutional data-governance requirements.

## 20. Analysis Output

The intended downstream analysis includes proof-of-concept classification distinguishing imagined-word conditions and rest. Model results must be reported only after data quality, preprocessing, and evaluation procedures have been documented.

A classification result must not be interpreted as evidence of mental-health diagnosis or direct access to a participant's private thoughts.

## 21. Pilot / Validation Before Main Recording

Before relying on the pipeline for the main dataset, validate:

1. Stimulus timing.
2. Event-marker count and order.
3. Marker-to-EEG latency/jitter.
4. Trial/block transitions.
5. Recording integrity.
6. Participant understanding of the imagined-speech instruction.
7. Preprocessing and metadata generation on pilot data.

## 22. Protocol-Controlled Items

### Current protocol values

- Target participants: **10**
- Participant age: **18–35 years**
- Hindi word classes/stimuli: **6**
- Fixation: **500 ms**
- Word display: **300 ms**
- Imagined speech: **3000 ms**
- Rest/reset: **1000 ms**
- Practice: **55 trials (~4 min)**
- Main blocks: **4 × 110 trials (~8.8 min each)**

### Items requiring confirmation

- Final EEG hardware
- Exact channel configuration/montage
- Device-specific acquisition parameters
- Exact marker implementation and measured latency/jitter
- Any other item explicitly marked for confirmation in the current supervisor/committee material

Do not silently replace these pending items with assumptions from earlier project drafts or unrelated EEG datasets.
