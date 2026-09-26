# Quality Control Code

**Status: not yet implemented.**

This folder will contain scripts implementing the quality checks
described in `docs/experimental_protocol.md`, Section 16, including:

- Verifying recorded channel count and sampling rate against the
  intended configuration.
- Verifying all expected event markers are present and correctly
  ordered for each session.
- Verifying recording duration matches the expected session length.
- Flagging sessions or trials for manual review before they enter
  preprocessing.

Output from these scripts should feed directly into
`preprocessing/preprocessing_log.csv` and the `artifact_flag` /
`valid_trial` fields in `metadata/trial_metadata.csv` — see
`docs/data_dictionary.md`.

No code exists in this folder yet.
