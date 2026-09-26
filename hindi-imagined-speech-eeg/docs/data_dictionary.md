# Data Dictionary

Defines every field in the four schema files under `metadata/`,
`vocabulary/`, and `preprocessing/`. All example values in this
document and in the CSV files are placeholders — no real participant,
trial, or preprocessing data exists yet.

---

## `metadata/participant_metadata.csv`

| Field | Meaning | Type | Example | Allowed values | Required |
|---|---|---|---|---|---|
| participant_id | Anonymized participant code | string | P001 (real data) / `EXAMPLE_P001` (placeholder rows) | `P` + 3-digit zero-padded number; placeholder rows are prefixed `EXAMPLE_` so they cannot be mistaken for real participants | Yes |
| age | Age in years at time of recording | integer | 23 | 18–45 (per inclusion criteria) | Yes |
| sex | Self-reported sex | string | F | M / F / Other / Prefer not to say | Yes |
| native_language | Self-reported native language | string | Hindi | Free text | Yes |
| other_languages | Other languages spoken | string | English | Free text, comma-separated | No |
| language_proficiency | Self-rated Hindi/English proficiency and dominance | string | Hindi-dominant, fluent English | Free text pending a standardized questionnaire | Yes |
| education_level | Highest education level completed/in progress | string | Undergraduate | Free text | No |
| handedness | Self-reported handedness | string | Right | Right / Left / Ambidextrous | Yes |
| hearing_status | Self-reported hearing status | string | Normal | Normal / Impaired / Corrected | Yes |
| vision_status | Self-reported vision status | string | Corrected | Normal / Impaired / Corrected | Yes |
| neurological_history | Self-reported neurological/psychiatric history | string | None reported | Free text; "None reported" if none | Yes |
| medication_status | Current medication relevant to CNS activity | string | None reported | Free text; "None reported" if none | Yes |
| caffeine_before_session | Caffeine consumption same day before session | string | No | Yes / No / Unknown | Yes |
| nicotine_before_session | Nicotine use same day before session | string | No | Yes / No / Unknown | Yes |
| sleep_hours | Self-reported hours of sleep the prior night | float | 7.5 | Positive number | No |
| session_id | Identifier for the recording session | string | S001 | `S` + 3-digit zero-padded number | Yes |
| recording_date | Date of recording | date (YYYY-MM-DD) | 2026-00-00 | Valid date or placeholder until recording occurs | Yes (placeholder until real recordings exist) |
| consent_public_release | Whether participant separately consented to public data release | string | TBD | Yes / No / TBD | Yes |

**Note:** No directly identifying information (full name, registration
number, phone number, email address) is stored in this file or any
other file in this repository.

## `metadata/trial_metadata.csv`

| Field | Meaning | Type | Example | Allowed values | Required |
|---|---|---|---|---|---|
| participant_id | Links to participant_metadata.csv | string | P001 (real data) / EXAMPLE_P001 (placeholder rows) | Matches an existing participant_id | Yes |
| session_id | Links to the recording session | string | S001 | Matches an existing session_id | Yes |
| trial_id | Unique identifier for this trial | string | P001_S001_T0001 (real) / EXAMPLE_P001_S001_T0001 (placeholder) | `{participant_id}_{session_id}_T` + 4-digit number | Yes |
| trial_number | Sequential trial number within the session | integer | 1 | Positive integer | Yes |
| block_number | Block number within the session | integer | 1 | Positive integer | Yes |
| condition | Experimental condition | string | covert | rest / overt / covert (see Section 12–13 of the protocol — overt condition not yet confirmed) | Yes |
| language | Language of the stimulus | string | Hindi | Hindi (fixed for this project) | Yes |
| stimulus_id | Links to a vocabulary item | string | V001 | Matches an ID in vocabulary_master.csv | Yes (for non-rest trials) |
| stimulus_text | Hindi text shown/spoken for this trial | string | हाँ | Matches vocabulary_master.csv for the given stimulus_id | Yes (for non-rest trials) |
| stimulus_category | Category of the stimulus | string | basic_communication | Matches category field in vocabulary_master.csv | Yes (for non-rest trials) |
| trial_type | High-level trial type | string | main | practice / main / pilot | Yes |
| cue_onset | Timestamp of cue onset, relative to session start | float (seconds) | `NOT_A_REAL_TIMESTAMP` | Non-negative number once real; the literal string `NOT_A_REAL_TIMESTAMP` in placeholder rows, chosen deliberately over a plausible-looking number so it cannot be mistaken for recorded data | Yes (placeholder for now) |
| imagination_onset | Timestamp of production-window onset | float (seconds) | `NOT_A_REAL_TIMESTAMP` | Same convention as cue_onset | Yes (placeholder for now) |
| imagination_offset | Timestamp of production-window offset | float (seconds) | `NOT_A_REAL_TIMESTAMP` | Same convention as cue_onset | Yes (placeholder for now) |
| rest_onset | Timestamp of post-trial rest onset | float (seconds) | `NOT_A_REAL_TIMESTAMP` | Same convention as cue_onset | Yes (placeholder for now) |
| rest_offset | Timestamp of post-trial rest offset | float (seconds) | `NOT_A_REAL_TIMESTAMP` | Same convention as cue_onset | Yes (placeholder for now) |
| response | Any participant response associated with the trial, if applicable | string | NA | Free text or NA | No |
| artifact_flag | Whether this trial was flagged for artifact contamination | boolean | FALSE | TRUE / FALSE | Yes (once QC has run; NA before then) |
| artifact_type | Type of artifact, if flagged | string | NA | e.g. ocular / muscle / movement / NA | No |
| valid_trial | Whether the trial passed quality control | boolean | TRUE | TRUE / FALSE; NA before QC has run | Yes (once QC has run; NA before then) |
| notes | Free-text notes on the trial | string | (blank) | Free text | No |

**Important:** All timestamp fields (`cue_onset` through `rest_offset`)
currently contain the literal placeholder string `NOT_A_REAL_TIMESTAMP` in the example file.
They are not real recorded timestamps and must not be used in any
analysis until actual EEG recordings exist and event markers have been
extracted.

## `vocabulary/vocabulary_master.csv`

| Field | Meaning | Type | Example | Allowed values | Required |
|---|---|---|---|---|---|
| stimulus_id | Unique vocabulary item identifier | string | V001 | `V` + 3-digit zero-padded number | Yes |
| hindi_text | The stimulus in Devanagari script | string | हाँ | Valid Devanagari text | Yes |
| transliteration | Romanized transliteration | string | haan | Free text | Yes |
| english_translation | English gloss | string | Yes | Free text | Yes |
| category | Functional/semantic category | string | basic_communication | basic_communication / assistance / physical_need / emotional_state | Yes |
| candidate_tier | Core or extended candidate set | string | core | core / extended | Yes |
| part_of_speech | Grammatical category of the item | string | noun | noun / verb (imperative) / adjective / interjection/particle / negation particle | Yes — this is objective grammatical fact, not a norming measure, so it is filled in rather than left NA |
| phonological_complexity | Rated phonological complexity (e.g. consonant clusters, retroflex sounds) | float or NA | NA | Not yet measured — requires a defined complexity scale; NA until linguistic validation is performed | No (currently NA) |
| word_frequency | Corpus-based frequency measure | float or NA | NA | Not yet measured — NA until linguistic validation is performed | No (currently NA for all items) |
| familiarity | Rated familiarity | float or NA | NA | Not yet measured — NA until validation | No (currently NA) |
| age_of_acquisition | Estimated age of acquisition | float or NA | NA | Not yet measured — NA until validation | No (currently NA) |
| syllable_count | Number of syllables | integer | 1 | Positive integer | Yes |
| character_count | Number of Devanagari characters | integer | 2 | Positive integer | Yes |
| concreteness | Rated concreteness | float or NA | NA | Not yet measured — NA until validation | No (currently NA) |
| emotional_salience | Rated emotional salience, where relevant | float or NA | NA | Not yet measured — NA until validation; most relevant for extended/emotional-category items | No (currently NA) |
| selection_status | Current status of this item | string | candidate | candidate / validated / rejected | Yes |
| rationale | Short note on why the item was included | string | Basic yes/no communication signal | Free text | Yes |
| source | Where the item/category idea originated | string | Team brainstorm; cf. EEGIS vocabulary | Free text | No |

**Note on blank numeric fields:** `word_frequency`, `familiarity`,
`age_of_acquisition`, `concreteness`, `emotional_salience`, and
`phonological_complexity` are intentionally left as `NA` for every
current item. These properties
require a proper linguistic validation pass (e.g. norming study or
established Hindi psycholinguistic norms database) that has not yet
been performed. Do not fill these with estimated or invented values.

## `preprocessing/preprocessing_log.csv`

This file is an **audit trail**, intended to record exactly what was
done to each participant's/trial's data during preprocessing, for
reproducibility. It is currently empty of real entries because no
preprocessing has been performed (no data exists yet).

| Field | Meaning | Type | Example | Allowed values | Required |
|---|---|---|---|---|---|
| participant_id | Links to participant_metadata.csv | string | P001 (real data) / EXAMPLE_P001 (placeholder rows) | Matches an existing participant_id | Yes |
| session_id | Links to the recording session | string | S001 | Matches an existing session_id | Yes |
| trial_id | Links to trial_metadata.csv | string | P001_S001_T0001 (real) / EXAMPLE_P001_S001_T0001 (placeholder) | Matches an existing trial_id | Yes |
| raw_file | Path/filename of the source raw recording | string | TBD | Valid file path once recordings exist | Yes (once data exists) |
| preprocessing_version | Human-readable version tag of the preprocessing pipeline (e.g. v0.1, v0.2) | string | TBD | Semantic version string | Yes (once pipeline is implemented) |
| pipeline_commit | Exact Git commit hash of the preprocessing code (`code/preprocessing/`) that produced this row | string | TBD | Full or short Git commit hash | Yes (once pipeline is implemented) — added specifically so a processed file can be traced back to the exact code version that produced it, since `preprocessing_version` alone is not precise enough if code changes between version bumps |
| code_commit | Exact Git commit hash of the downstream analysis/modeling code (`code/analysis/`) that later consumed this processed output, if applicable | string | TBD or NA | Full or short Git commit hash, or NA if no analysis has yet used this file | No at preprocessing time; required once any analysis result references this file — kept separate from `pipeline_commit` because preprocessing and analysis are independently-versioned codebases |
| filter_type | Type of filter applied | string | TBD | e.g. Butterworth, FIR | Yes (once finalized) |
| highpass_hz | High-pass filter cutoff | float | TBD | Positive number, Hz | Yes (once finalized) |
| lowpass_hz | Low-pass filter cutoff | float | TBD | Positive number, Hz | Yes (once finalized) |
| notch_filter_hz | Notch filter frequency | float | TBD | Expected 50 (India mains frequency) once finalized | Yes (once finalized) |
| reference_method | Re-referencing method used | string | TBD | e.g. average, linked mastoids | Yes (once finalized) |
| artifact_method | Primary artifact-removal method | string | TBD | e.g. ICA (Infomax) | Yes (once finalized) |
| channels_removed | Channels excluded/interpolated | string | TBD | Comma-separated channel list or "none" | Yes (once data exists) |
| bad_channel_count | Number of channels excluded/interpolated for this recording | integer | TBD | Non-negative integer | Yes (once data exists) |
| ica_applied | Whether ICA was applied | boolean | TBD | TRUE / FALSE | Yes (once pipeline runs) |
| ica_components_removed | Number of ICA components removed | integer | TBD | Non-negative integer | Yes (once pipeline runs) |
| epoch_start_s | Epoch window start, relative to event marker | float | TBD | Number, seconds (can be negative) | Yes (once finalized) |
| epoch_end_s | Epoch window end, relative to event marker | float | TBD | Number, seconds | Yes (once finalized) |
| baseline_correction | Baseline correction method, if applied | string | TBD | Free text or "none" | Yes (once finalized) |
| artifact_flag | Whether this trial was flagged during preprocessing | boolean | TBD | TRUE / FALSE | Yes (once pipeline runs) |
| artifact_type | Type of artifact flagged | string | TBD | Free text or NA | No |
| artifact_percentage | Percentage of the epoch duration flagged as artifact-contaminated | float | TBD | 0–100 | No |
| quality_control_status | Overall QC verdict for this trial, distinct from final inclusion/exclusion | string | TBD | e.g. pass / review_needed / fail | Yes (once QC pipeline runs) |
| trial_status | Final status of the trial after preprocessing | string | TBD | included / excluded | Yes (once pipeline runs) |
| reason_for_rejection | Reason a trial was excluded, if applicable | string | TBD | Free text or NA | No |
| notes | Free-text notes | string | (blank) | Free text | No |

All `TBD` values above will be replaced with real per-participant,
per-trial entries once the preprocessing pipeline (`preprocessing/preprocessing_pipeline.md`)
is finalized and applied to actual recorded data.
