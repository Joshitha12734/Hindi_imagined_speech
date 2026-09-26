# Changelog

All notable changes to this repository are recorded here. Dates use
YYYY-MM-DD format.

## [Unreleased]

### Added (round 3 — expanded specification docs)
- `docs/event_marker_protocol.md` — standalone event-marker specification,
  expanding `docs/experimental_protocol.md` §14 with a full method
  comparison, timing-precision requirements, a validation plan, and an
  explicit mapping to `trial_metadata.csv` fields.
- `docs/vocabulary_validation.md` — the "how and when" companion to
  `docs/vocabulary_rationale.md`'s "what and why": candidate validation
  methods (existing norms databases, internal norming survey, corpus
  frequency lookup, phonological complexity scoring), open disambiguation
  questions (रुको, खाना), and inclusion/exclusion criteria still to be
  decided.
- `docs/supervisor_approval_checklist.md` — every unresolved design
  decision across the repository consolidated into one formal sign-off
  checklist, organized by Ethics, Participants, Vocabulary, Trial Design,
  Hardware, Preprocessing/Analysis, Pilot, and Narrative/Framing.
- `code_commit` column in `preprocessing/preprocessing_log.csv`, distinct
  from `pipeline_commit` — tracks the downstream analysis code version
  separately from the preprocessing code version, since they are
  independently-versioned codebases (`code/analysis/` vs.
  `code/preprocessing/`).

### Changed (round 3)
- `results/README.md` and `code/analysis/README.md` reporting policy now
  requires every result to cite its `code_commit` and transitively its
  `pipeline_commit`, not just describe what was measured.
- README repository-structure tree and `docs/research_status.md` updated
  to include all three new documents.

### Added (round 2 — post-review revisions)
- `docs/research_status.md` — component-by-component status tracker.
- `docs/decision_log.md` — design-decision record with reasons,
  alternatives considered, and approval status.
- Formal event-marker table (`REST_ON`, `CUE_ON`, `IMAGINE_ON`,
  `IMAGINE_OFF`, `TRIAL_END`) in `docs/experimental_protocol.md`.
- `part_of_speech` and `phonological_complexity` columns in
  `vocabulary/vocabulary_master.csv`.
- `pipeline_commit`, `bad_channel_count`, `artifact_percentage`, and
  `quality_control_status` columns in `preprocessing/preprocessing_log.csv`.

### Changed (round 2 — post-review revisions)
- Placeholder participant/trial IDs now prefixed `EXAMPLE_`, and
  placeholder timestamps changed from a bare `PLACEHOLDER` string to
  the more explicit `NOT_A_REAL_TIMESTAMP`, so example rows cannot be
  mistaken for real data.
- Reframed the artifact-removal step in
  `preprocessing/preprocessing_pipeline.md` so ICA is presented as one
  candidate method, not a mandatory default, with an explicit rule
  that component removal must be evidence-justified.
- Participant inclusion criteria (age range, handedness) in
  `docs/experimental_protocol.md` now state that these are proposed
  defaults requiring explicit justification/revisiting, rather than
  literature-convention defaults; handedness is no longer framed as
  "right-handed preferred" without a stated reason.
- `CITATION.cff` `type` changed from `dataset` to `software`, since no
  dataset yet exists; added an explicit note to confirm with Dr. Goyal
  before publishing the repository whether her email should remain in
  the file.

### Added (round 1 — initial structure)
- Initial repository structure: `docs/`, `metadata/`, `vocabulary/`,
  `preprocessing/`, `data/`, `code/`, `results/`.
- Draft experimental protocol (`docs/experimental_protocol.md`).
- Candidate vocabulary — core (8 items) and extended (4 items) sets —
  with rationale document (`docs/vocabulary_rationale.md`).
- Literature review covering imagined-speech EEG, covert speech,
  Hindi/bilingual speech, vocabulary design, public datasets, and
  related areas (`docs/literature_review.md`).
- Ethical considerations policy (`docs/ethical_considerations.md`).
- Metadata schemas for participants and trials, with placeholder
  example rows (`metadata/`).
- Preprocessing pipeline design document and empty audit-trail log
  schema (`preprocessing/`).
- Data dictionary covering all CSV schemas (`docs/data_dictionary.md`).

### Status at this point
- No ethics/IRB approval yet.
- No participants recruited.
- No EEG data recorded.
- No preprocessing or analysis code implemented.
- No results exist.

This is a documentation-and-design-stage snapshot of the project, not a
release of a working dataset.

---

## Template for Future Entries

```
## [vX.Y.Z] - YYYY-MM-DD
### Added
### Changed
### Fixed
### Removed
```
