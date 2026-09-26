# Supervisor Approval Checklist

**Purpose:** every unresolved design question currently scattered across
`docs/experimental_protocol.md`, `docs/event_marker_protocol.md`,
`docs/vocabulary_validation.md`, and `docs/decision_log.md`, collected
into one explicit sign-off list. **Nothing in this checklist should be
treated as decided until it is checked off with a date and Dr. Goyal's
name in the "Approved" column.** This document exists specifically so
data collection does not start on the basis of an implied or assumed
approval.

How to use this: bring this document to the protocol-alignment meeting.
For each row, either (a) it gets checked off with a decision recorded,
(b) it is explicitly deferred with a new target date, or (c) it is
reassigned for further team investigation before it can be brought back
for approval. Update the linked source document (protocol, event-marker
doc, vocabulary validation plan, or decision log) immediately after any
item is resolved here, so this checklist and those documents never
contradict each other.

---

## A. Ethics & Governance

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Ethics/IRB submission timeline | When will the submission actually go in? | `docs/experimental_protocol.md` §3, §5 | |
| ☐ | Consent form content | Final wording, especially the "what EEG can/cannot reveal" section | `docs/ethical_considerations.md` | |
| ☐ | Public-release consent language | Exact wording for the separate, explicit release-consent clause | `docs/ethical_considerations.md` | |
| ☐ | Supervisor email in `CITATION.cff` | Confirm Dr. Goyal is comfortable with her email appearing once the repository is public | `CITATION.cff` (see inline note) | |

## B. Participant Criteria

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Target sample size, Phase 1 | Proposed default: 10–15; not yet approved | `docs/experimental_protocol.md` §3.2 | |
| ☐ | Age range justification | 18–45 proposed as a default; needs an explicit stated reason or revision | `docs/experimental_protocol.md` §3 | |
| ☐ | Handedness policy | Current plan: record but do not exclude left-handed participants | `docs/experimental_protocol.md` §3 | |

## C. Vocabulary

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Core vocabulary (8 items) | Approve as candidate set for pilot use, pending linguistic validation | `vocabulary/vocabulary_core.csv`, `docs/vocabulary_rationale.md` | |
| ☐ | Extended/emotional vocabulary use in first pilot | Current recommendation: **exclude** from first pilot unless Dr. Goyal specifically wants it included | `docs/decision_log.md` | |
| ☐ | रुको ("Stop / Wait") disambiguation | Split into two items, or keep as one with documented ambiguity? | `docs/vocabulary_validation.md` §3 | |
| ☐ | खाना ("Food" / "to eat") ambiguity | Keep, clarify, or replace with a less ambiguous item? | `docs/vocabulary_validation.md` §3 | |
| ☐ | Vocabulary validation method | Existing Hindi norms database vs. internal norming survey vs. corpus lookup — which, and via whom? | `docs/vocabulary_validation.md` §2 | |
| ☐ | Vocabulary validation timeline relative to ethics submission | Can a norming survey run in parallel with IRB submission? | `docs/vocabulary_validation.md` §5 | |
| ☐ | Word → phrase progression | Approve the 3-phase roadmap (single words → short need-phrases → natural communication) as the project's long-term vocabulary direction | `docs/vocabulary_rationale.md`, `docs/decision_log.md` | |

## D. Trial & Task Design

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Overt-speech condition | Include a paired overt condition, or covert-only? | `docs/experimental_protocol.md` §12 | |
| ☐ | Event-marking method | Cue-locked (recommended) vs. self-initiated keypress | `docs/event_marker_protocol.md` §2 | |
| ☐ | Formal marker set | Approve `REST_ON` / `CUE_ON` / `IMAGINE_ON` / `IMAGINE_OFF` / `TRIAL_END` as final, or revise | `docs/event_marker_protocol.md` §3 | |
| ☐ | Cue format | Text (Devanagari), audio, or both | `docs/experimental_protocol.md` §6.3 (referenced) | |
| ☐ | Trial timing (stage durations) | Currently draft proposals; require piloting before lock-in | `docs/experimental_protocol.md` §10 | |
| ☐ | Repetitions per item, session length | Proposed 40–60 reps/item, ~60–75 min sessions | `docs/experimental_protocol.md` §7 | |

## E. Hardware & Signal Acquisition

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | EEG device and channel count | Depends entirely on confirmed lab access | `docs/experimental_protocol.md` §7 | |
| ☐ | Sampling rate | Proposed 250–500 Hz range | `docs/experimental_protocol.md` §7 | |
| ☐ | EMG inclusion | Whether to record EMG at all, and for how many participants | `docs/experimental_protocol.md` §7, `docs/decision_log.md` | |
| ☐ | Marker-to-EEG latency tolerance | Cannot be set until hardware is chosen; must be measured during bench testing | `docs/event_marker_protocol.md` §4 | |

## F. Preprocessing & Analysis

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Filter cutoffs, reference method | Not yet set — depend on hardware and pilot signal quality | `preprocessing/preprocessing_pipeline.md` | |
| ☐ | Epoch window and baseline window | To be finalized jointly by both teams | `preprocessing/preprocessing_pipeline.md` §12–13 | |
| ☐ | Artifact-rejection method | ICA is a candidate, not a default; final method not chosen | `preprocessing/preprocessing_pipeline.md` §10 | |
| ☐ | Evaluation protocol | Approve staged plan: state-detection sanity check → within-subject word-level → cross-subject | `code/analysis/README.md` | |

## G. Pilot

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Pilot scope and labeling | Confirm pilot is explicitly a "protocol/usability pilot," not a decoding-feasibility study, and its results will not be used to claim anything about the main dataset | `docs/experimental_protocol.md` §24, `docs/decision_log.md` | |
| ☐ | Pilot participant count | Proposed: 2–3 team members | `docs/experimental_protocol.md` §24 | |

## H. Narrative / Framing

| ☐ | Item | Detail | Source | Approved (name, date) |
|---|---|---|---|---|
| ☐ | Project narrative emphasis | Recommendation: lead with "assistive communication," with mental-health-related communication explicitly framed as a future application area | `docs/decision_log.md` (top entry) | |

---

## Sign-Off Summary

Once every row above is checked and approved, this section should be
completed:

- **Protocol version approved:** \_\_\_\_\_\_\_\_\_\_
- **Approved by:** \_\_\_\_\_\_\_\_\_\_
- **Date:** \_\_\_\_\_\_\_\_\_\_
- **Effective for:** first pilot / first main-study cohort *(circle one)*

Only after this section is completed should `docs/research_status.md`
mark the experimental protocol as **COMPLETED** rather than **IN
PROGRESS**.
