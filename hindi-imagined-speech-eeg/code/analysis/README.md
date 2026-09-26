# Analysis / Modeling Code

**Status: not yet implemented — future stage.**

This folder will eventually contain feature-extraction and
classification code, once a clean processed dataset exists. Per the
project's staged validation plan (to be documented in full once
recording begins), the intended order of analysis is:

1. **Sanity-check classification**: distinguish rest vs. overt vs.
   covert speech states, as a baseline check that the recording and
   preprocessing pipeline is producing a usable signal at all — this
   mirrors the approach used in Kostulin et al. (2026); see
   `docs/literature_review.md`.
2. **Within-participant word-level classification**: attempt to
   distinguish individual vocabulary items from each other for a single
   participant's data.
3. **Cross-participant generalization** (stretch goal): evaluate
   whether a model trained on some participants transfers to unseen
   participants — expected to be substantially harder based on the
   current state of the field.

No models have been trained and no accuracy figures exist yet. Any
number appearing in this folder in the future must specify exactly what
is being classified (state detection vs. word-level decoding) to avoid
the exact ambiguity flagged in our review of Kostulin et al. — see
`docs/literature_review.md`.

Every script in this folder should record its own Git commit hash as
`code_commit` in `preprocessing/preprocessing_log.csv` (or an
equivalent results-level log, if one is added) for any run whose output
is reported — see `docs/data_dictionary.md` and the reporting policy in
`results/README.md`. This is distinct from `pipeline_commit`, which
tracks the preprocessing code instead.

No code exists in this folder yet.
