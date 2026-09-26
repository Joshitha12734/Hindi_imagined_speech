# Ethical Considerations

This document states the ethical policy this project follows. It is
written to be explicit rather than reassuring — several points below
exist specifically to prevent this project's results from being
overstated or misused, including by our own future selves.

## Institutional Approval

No participant recording will take place before institutional
ethics/IRB approval has been obtained. As of this document's writing,
that approval has **not yet been submitted or granted**. This is a
blocking dependency for the entire data-collection timeline.

## Informed Consent

- Participation is voluntary, and consent is obtained in writing before
  any recording.
- The consent process will explain, in plain language, what EEG
  recording involves, what data will be collected, and how it will be
  used.
- Consent will explicitly state what the data **can and cannot**
  reveal — in particular, that this study does not diagnose or assess
  any mental-health condition (see "No Clinical Diagnosis" below).
- Separate, explicit consent will be obtained for any possible future
  public release of anonymized data. Agreeing to participate in the
  study does not automatically imply agreement to public data release.
- Participants may withdraw at any time. The consent process will state
  clearly what withdrawal means in practice (e.g. whether already-
  collected data up to that point is retained or deleted), once this is
  finalized with the institutional ethics body.

## Anonymization

- Participants are identified only by a coded ID (e.g. `P001`) in all
  data files, metadata, and documentation in this repository.
- No names, registration/roll numbers, phone numbers, email addresses,
  home addresses, or other directly identifying information will be
  stored in this repository, in any released dataset, or in any file
  under version control.
- Any necessarily identifying records (e.g. signed paper/digital
  consent forms) will be stored separately from this repository, under
  institutional data-security requirements, with restricted access.
- Demographic fields retained (age, sex, handedness, language
  background) are kept at a level of granularity intended to support
  research use without enabling re-identification of individuals within
  a small participant pool; this should be reviewed as the participant
  count grows.

## Public Release

- No dataset has been released publicly at the time of writing.
- Any future public release will (a) include only anonymized data
  covered by explicit participant consent for that specific purpose,
  and (b) follow licensing terms decided in coordination with the
  institutional ethics approval and Dr. Goyal — see the licensing note
  in `LICENSE`.

## Withdrawal

Participants retain the right to withdraw consent. The exact mechanics
of withdrawal (how to request it, what happens to already-collected
data) will be defined in the finalized consent form and are **not yet
finalized** in this repository.

## Data Security

- Raw and identifiable data will not be committed to this repository's
  version control (see `.gitignore`).
- Storage and access-control procedures for raw recordings and any
  identifying records will follow institutional data-security
  requirements, to be confirmed alongside ethics approval.

## No Clinical Diagnosis

**This project does not diagnose, assess, or make claims about any
participant's mental-health status, and no component of this dataset
should be used for that purpose.**

Specifically:

- No vocabulary item is a diagnostic instrument. Imagining a word such
  as *चिंता* (worry) or *डर* (fear) on instruction is a linguistic task,
  not a psychological assessment — see the detailed discussion in
  `docs/vocabulary_rationale.md`.
- No claim is made, or will be made, that EEG activity recorded in this
  study reflects a participant's actual emotional state, mental health,
  or psychological condition at the time of recording.
- "Mental health applications" in the project title refers to a
  **possible future application area** — specifically, assistive
  communication for people with severe motor/speech impairment who may
  need to express needs, discomfort, or emotional state — not to a
  diagnostic capability of the current dataset.

## No Inference of Mental State From Individual EEG

Beyond the vocabulary-specific point above: this project does not
attempt, and will not attempt, to infer an individual participant's
mental or emotional state from their EEG signal as a general capability
of the dataset or any model trained on it. Any research question of
that form would require a fundamentally different study design,
validation methodology, and ethical review, and is out of scope for the
current project phase.

## Responsible AI / BCI Development

- Results (once they exist) will be reported honestly, including
  negative or modest results — see the reporting policy implied
  throughout `docs/literature_review.md` and `docs/experimental_protocol.md`.
- Accuracy figures will always specify exactly what is being classified
  (e.g. broad speech-state detection vs. word-identity decoding) — a
  documented source of confusion in this literature (see the Kostulin
  et al. entry in `docs/literature_review.md`) that this project
  commits to avoiding.
- Novelty claims (e.g. "first Hindi imagined-speech EEG dataset") will
  not be made unless and until they have been properly verified against
  the existing literature — see the verification note in
  `docs/literature_review.md` and the corresponding caveat in the main
  `README.md`.

## Special Caution Around Future Clinical Populations

The long-term motivation for this work references potential future
benefit to people with severe motor/speech impairment (e.g. ALS,
locked-in syndrome). This project's current phase:

- Recruits only healthy adult volunteers, not clinical populations.
- Does not claim that results from a healthy-volunteer sample will
  generalize directly to a clinical population — EEG characteristics
  and task performance may differ substantially, and this should be
  treated as an open question, not an assumption (see the corresponding
  entry in the README's Limitations section).
- Explicitly defers any work directly involving clinical populations to
  a future phase requiring separate ethical review, clinical
  collaboration, and appropriate expertise beyond the current student
  team.

## Summary

If any part of this project — a document, a script, a presentation, or
a future publication — describes this dataset as diagnostic, clinically
validated, or capable of reading a participant's emotional state, that
description is inconsistent with this policy and should be corrected.
