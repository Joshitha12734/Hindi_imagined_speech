# Vocabulary Rationale

**Status:** The vocabulary described here is a **candidate set**. It has
not undergone formal linguistic validation or supervisor sign-off, and
should not be treated as the final stimulus set for data collection.

---

## Why Communication-Oriented Vocabulary?

Rather than selecting words purely to maximize classification ease
(e.g. picking phonetically maximally distinct items), we selected
candidate vocabulary primarily for **plausible usefulness in an
assistive-communication context**. This follows the explicit rationale
used in at least one reviewed dataset (Kostulin et al., 2026), where
stimulus words were chosen for their functional role in a task rather
than for phonetic distinctiveness. If this dataset is ever used to
support real communication for someone who cannot otherwise speak, the
vocabulary needs to already reflect things a person would actually want
or need to say.

## Why These Categories?

**Yes / No.** The most basic binary communication signal. Almost every
comparable functional-vocabulary dataset we reviewed (EEGIS, the 2020
BCI Competition Track 3 set) includes a yes/no pair, since it is the
minimum viable communication channel.

**Assistance words (मदद – help, रुको – stop/wait).** Directly relevant
to an assistive-communication use case: the ability to request help or
signal "stop" is a priority communication need, independent of any
specific physical or emotional context.

**Physical needs (पानी – water, खाना – food).** Represent immediate,
concrete physiological needs — a category present in comparable
datasets (e.g. EEGIS includes *Hambre*/hunger and *Sed*/thirst; the
BCI Competition set includes functional commands of a similar
character).

**Pain (दर्द).** A single, high-priority word representing physical
distress. Included as a core item because of its direct relevance to
patient communication needs, independent of any specific diagnosis.

**Rest (आराम).** Represents a basic comfort-related request, included
in the core set alongside the more urgent items above.

**Extended set — medicine, and emotional/state words (दवा, खुश, डर,
चिंता).** These extend the vocabulary toward slightly more abstract or
emotionally salient content. They are placed in the **extended**, not
core, set deliberately: they are more linguistically and conceptually
complex than the core items, and their inclusion should be revisited
after core-vocabulary results (even preliminary ones) are available.

## Why Word-Level Decoding First, Not Sentences?

Across every dataset and review we examined (see
`docs/literature_review.md`), reliable open-vocabulary or long-sentence
imagined-speech decoding from non-invasive EEG has not been
demonstrated. Essentially all functional, communication-oriented
imagined-speech datasets use small, closed vocabularies of single words
or short phrases. Attempting phrase- or sentence-level decoding before
establishing that word-level decoding is even feasible for our
recording setup and vocabulary would not be a scientifically grounded
starting point. Phrase-level decoding is listed as future work in the
main README, not a current goal.

## Linguistic Balancing — Planned, Not Yet Performed

The final vocabulary should ideally be balanced, as much as practically
possible, across:

- **Word frequency** — how commonly the word occurs in everyday Hindi.
- **Familiarity** — how well-known/recognizable the word is expected to
  be across a general adult Hindi-speaking population.
- **Age of acquisition** — roughly when the word is typically learned.
- **Syllable count** and **word length** (character count).
- **Phonological complexity** — e.g. consonant clusters, retroflex
  sounds, which may affect how consistently a word is internally
  articulated.
- **Concreteness** — concrete, physically-grounded words (पानी) versus
  more abstract ones (चिंता) may behave differently in imagined-speech
  paradigms; this is itself a documented concern in the literature
  (see the Turk et al. 2025 entry in `docs/literature_review.md` on
  word-specific properties affecting classification performance).
- **Semantic category** — spreading items across distinct functional
  categories rather than clustering many near-synonyms together.
- **Emotional salience**, where relevant to the extended/emotional-word
  set specifically.

None of these properties have been formally measured for our candidate
vocabulary yet. The corresponding fields in
`vocabulary/vocabulary_master.csv` are intentionally left blank (`NA`)
rather than filled with invented numbers.

## Important Distinction: Communication Targets vs. Clinical Interpretation

This project treats vocabulary items — including emotional-state words
in the extended set (खुश, डर, चिंता) — strictly as **communication
targets**: fixed linguistic labels a participant is asked to silently
imagine on cue, for the purpose of studying whether the *word identity*
can be decoded from EEG.

**An EEG response recorded while a participant imagines the word
"चिंता" (worry) does not constitute evidence that the participant is
anxious, distressed, or experiencing any mental-health condition.** The
task requires imagining a specific word on instruction, exactly as it
requires imagining "पानी" (water) — it says nothing about the
participant's actual internal emotional state at the time, and no claim
of this kind will be made based on this dataset.

Any future application involving inference about a person's actual
emotional or mental-health state from EEG would require an entirely
different experimental design, validation methodology, and ethical
review process, and is explicitly out of scope for the current phase of
this project. See `docs/ethical_considerations.md` for the full policy
on this point.

## Status Summary

| Vocabulary tier | Item count | Validation status |
|---|---|---|
| Core | 8 | Candidate only — not linguistically validated |
| Extended | 4 | Candidate only — not linguistically validated |

Full item-by-item detail is in `vocabulary/vocabulary_master.csv`,
`vocabulary/vocabulary_core.csv`, and `vocabulary/vocabulary_extended.csv`.
