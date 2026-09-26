# Preprocessing Code

**Status: not yet implemented.**

This folder will contain scripts implementing the pipeline described in
`preprocessing/preprocessing_pipeline.md`: data import, filtering,
re-referencing, artifact removal (ICA), event synchronization, and
epoch extraction.

Planned language/tooling: **to be determined** by the Preprocessing
Team, likely Python with an EEG-analysis library (e.g. MNE-Python),
consistent with common practice in the literature reviewed in
`docs/literature_review.md`.

Every script added here should:

- Read its filtering/epoching parameters from a single, clearly
  documented configuration point (not hard-coded in multiple places),
  so that parameter changes are traceable.
- Write a corresponding entry to `preprocessing/preprocessing_log.csv`
  for every participant/trial it processes, per the audit-trail
  requirement in `docs/experimental_protocol.md`, Section 23.

No code exists in this folder yet.
