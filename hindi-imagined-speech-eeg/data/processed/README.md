# Processed Data

**Status: empty. No preprocessing has been performed yet, since no raw
data exists.**

This folder is where cleaned, epoched EEG data will be stored once the
preprocessing pipeline (`preprocessing/preprocessing_pipeline.md`) has
been implemented and applied to real recordings.

Planned structure mirrors `data/raw/`:

```
data/processed/
└── sub-P001/
    └── ses-S001/
        └── eeg/
            └── sub-P001_ses-S001_task-imaginedspeech_epochs.<ext>
```

File format (e.g. `.fif`, `.set`) is not yet finalized — see
`preprocessing/preprocessing_pipeline.md`.

## Important

- Every processed file must correspond to a logged entry in
  `preprocessing/preprocessing_log.csv`, recording exactly what
  processing was applied — see `docs/data_dictionary.md`.
- Processed files are excluded from version control via `.gitignore`
  in this phase; whether/how processed data is eventually shared is an
  open item — see `docs/ethical_considerations.md`.

This repository documents the *intended* structure for processed data.
It does not currently contain any actual processed recordings.
