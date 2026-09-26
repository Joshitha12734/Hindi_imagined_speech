# Results

**Status: empty. No experiments have been run yet.**

This folder will hold results (figures, tables, model outputs) once
data collection, preprocessing, and analysis have produced something to
report.

## Reporting Policy

When results are added here, each result must:

- State exactly what was classified/measured (e.g. "3-class rest vs.
  overt vs. covert state detection", not just "classification
  accuracy").
- State the participant count, trial count, and evaluation method
  (e.g. within-subject cross-validation vs. cross-subject) used to
  produce it.
- Cite the exact `code_commit` (Git commit hash of `code/analysis/`)
  and, transitively, the `pipeline_commit` of the processed data it was
  computed from (see `preprocessing/preprocessing_log.csv`), so any
  reported number can be traced back to the exact code and data version
  that produced it — a result without a commit reference should be
  treated as provisional, not reportable.
- Be accompanied by an update to the "Current Status" table in the
  main `README.md`.
- Avoid overclaiming — a modest above-chance result is a legitimate,
  reportable outcome at this stage of the field; see
  `docs/literature_review.md` for context on typical reported accuracy
  ranges in comparable work.

No fabricated or placeholder results are included in this folder.
