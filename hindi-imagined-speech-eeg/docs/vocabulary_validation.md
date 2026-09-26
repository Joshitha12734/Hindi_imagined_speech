# Vocabulary Validation Plan

**Status:** Planned — not started. This document exists because
`docs/vocabulary_rationale.md` correctly identifies *what* needs
validating, but does not yet specify *how* or *when*. Every numeric
field currently `NA` in `vocabulary/vocabulary_master.csv` is `NA`
because this plan has not yet been executed, not because the
properties don't matter.

## 1. What Needs Validation, and Why

| Property | Why it matters for this project | Currently |
|---|---|---|
| Word frequency | Turk et al. (2025; citation to verify — see `docs/literature_review.md`) reports word frequency affecting imagined-speech classification performance; an unbalanced set could confound word-identity decoding with frequency effects | `NA` for all 12 items |
| Familiarity | Related to but distinct from frequency; a word can be infrequent in corpora but highly familiar (or vice versa) | `NA` for all 12 items |
| Age of acquisition | Also reported as a relevant factor in the literature; earlier-acquired words may be processed/imagined differently | `NA` for all 12 items |
| Concreteness | पानी (concrete) vs. चिंता (abstract) may plausibly engage different imagery/processing strategies during imagination | `NA` for all 12 items |
| Phonological complexity | Consonant clusters, retroflex sounds etc. may affect how consistently a word is internally articulated | `NA` for all 12 items |
| Syllable / character count | Structural properties, objectively countable | Already filled in for all 12 items |
| Part of speech | Grammatical category, objectively determinable | Already filled in for all 12 items |

## 2. Validation Methods Under Consideration

**Not yet decided which of these will be used — likely some
combination:**

### A. Existing Hindi psycholinguistic norms databases
If a published Hindi word-norms database exists covering frequency,
familiarity, age of acquisition, and/or concreteness for our candidate
items, using it would be far more efficient than collecting new norms.
**Action item: search for and evaluate existing Hindi norms databases
before planning a new norming study** — this has not yet been done and
should happen before Section 2B below is committed to.

### B. A small internal norming survey
If no adequate existing database covers our items, a short survey
(native Hindi speakers rate each candidate word on familiarity,
concreteness, and, where relevant, emotional salience, typically on a
1–7 or 1–5 Likert scale) could be run. This requires:
- A target respondent count (**to be determined**; norming studies
  commonly use several dozen respondents, but the appropriate number
  for 12 items should be decided deliberately, not assumed).
- Its own lightweight ethics consideration (anonymous survey, no EEG
  involved, likely lower-risk than the main study but still requiring
  informed consent for participation).
- A decision on whether this survey is run by our team or draws on an
  existing linguistics resource/collaborator.

### C. Corpus-frequency lookup
Word frequency could potentially be computed directly from an existing
Hindi text corpus (e.g. a large Hindi Wikipedia dump or a published
Hindi frequency list), which is more mechanical than a survey and does
not require new participant recruitment. **Action item: identify a
specific corpus/frequency list to use** — not yet selected.

### D. Phonological complexity scoring
Likely requires either (a) a rule-based scoring scheme we define
ourselves (e.g. counting consonant clusters, retroflex consonants,
vowel-cluster complexity) or (b) an existing Hindi phonological
complexity metric from the linguistics literature, if one exists and is
locatable. **Not yet decided which approach to use.**

## 3. Decisions This Validation Pass Must Resolve

These are flagged directly in `vocabulary/vocabulary_master.csv` and
`docs/vocabulary_rationale.md` and should be explicitly revisited once
validation data exists, not decided on convenience:

- **रुको ("Stop / Wait")** — does validation data (or simply closer
  linguistic/team discussion) support splitting this into two distinct
  items, or is a single item acceptable given the assistive-
  communication context (i.e. context may disambiguate the intended
  meaning in practice)?
- **खाना ("Food" / "to eat")** — is the noun reading reliably the
  default interpretation for a Hindi speaker seeing this word presented
  in isolation, or does it need to be replaced/clarified (e.g. with a
  more unambiguous synonym) to guarantee participants imagine the
  intended target?
- **Balance across categories** — once frequency/familiarity/AoA data
  exists, does the core set remain reasonably balanced, or does it
  skew toward high-frequency/highly-familiar items in a way that would
  make word-identity decoding easier for uninteresting reasons (i.e.
  frequency differences doing the work rather than genuine semantic/
  phonological distinctiveness)?

## 4. Inclusion/Exclusion Criteria — Not Yet Defined

Once validation data exists, the team needs an explicit rule for what
happens to an item that turns out to be, for example, unexpectedly rare
or ambiguous — **not yet decided whether such items are**:
(a) dropped from the core set and moved to extended/rejected,
(b) kept but flagged with a documented caveat, or
(c) replaced with a better-behaved synonym.

This decision should be made and recorded in `docs/decision_log.md`
before validation results are used to finalize the vocabulary, so the
criteria aren't chosen retroactively to justify a preferred outcome.

## 5. Timeline

**Not yet scheduled.** This should happen before the vocabulary is
"frozen" for main-study data collection (see
`docs/supervisor_approval_checklist.md`), but the exact timing relative
to ethics approval and the protocol pilot has not been decided — a
norming survey (Section 2B) does not require EEG and could plausibly
run in parallel with ethics submission, which is worth discussing with
Dr. Goyal as a way to save time rather than sequencing everything
strictly one step at a time.

## 6. Output

Once complete, this validation pass should populate the currently-`NA`
columns in `vocabulary/vocabulary_master.csv` with real measured values
(not estimates), update `selection_status` for each item from
`candidate` to `validated` or `rejected`, and be summarized with a short
results note added to this document.
