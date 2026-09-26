# Raw Data

**Status: empty. No recordings have been collected yet.**

This folder is where raw EEG (and EMG, if used) recordings will be
stored once data collection begins, organized under a BIDS-inspired
(not fully BIDS-compliant) structure:

```
data/raw/
└── sub-P001/
    └── ses-S001/
        ├── eeg/
        │   └── sub-P001_ses-S001_task-imaginedspeech_eeg.edf
        └── events/
            └── sub-P001_ses-S001_task-imaginedspeech_events.tsv
```

## Important

- Raw recording files are excluded from version control via
  `.gitignore` and must never be committed to this repository, since
  they may be large and, depending on export settings, could retain
  more information than the anonymized coded dataset is meant to carry.
- Only anonymized, participant-coded data should ever exist under this
  structure — see `docs/ethical_considerations.md`.
- File-naming conventions here must stay consistent with
  `metadata/trial_metadata.csv` (`participant_id`, `session_id`) so that
  every raw file can be traced back to its metadata row.

This repository documents the *intended* structure for raw data storage.
It does not currently contain any actual recordings.
