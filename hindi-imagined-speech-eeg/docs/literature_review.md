# Literature Review

**Status:** Working document. Entries marked "citation to verify" have
been recorded from project notes / secondary reference and have not
been independently confirmed against the original source by this
repository's maintainers at time of writing. Do not cite these entries
in formal work without first verifying the original publication.

For each paper, we separate **what the paper actually demonstrated**
from **our interpretation of its relevance to this project** — these
are not the same thing, and should not be blurred.

---

## A. Imagined Speech EEG

### Kostulin et al. (2026) — EEG-based BCI dataset for directional word recognition
- **Venue:** Scientific Data, 13, 1195. DOI: 10.1038/s41597-026-07809-9
- **Language:** Russian and Spanish
- **Task:** Paired overt and covert articulation of six/seven directional words
- **Participants:** 22 (12 Russian, 10 Spanish), right-handed, ages 18–34
- **EEG setup:** 38 channels, 500 Hz, 10–10 system; EMG (masseter + laryngeal) on a 6-participant subset
- **Vocabulary:** Direction words (forward, backward, left, right, up, down; "next" for Russian only), chosen for semantic role in a navigation task, not phonetic distinctiveness
- **Preprocessing:** 1–70 Hz band-pass, 48–52 Hz notch, ICA (Infomax) for ocular/cardiac artifact removal, 1.5 s epochs around a self-initiated keypress marker
- **Classification:** Random Forest, SVM, LDA distinguishing **rest vs. overt vs. covert speech states** (not word identity); best result 78 ± 4% (Random Forest), 5-fold cross-validation per participant
- **What the paper actually demonstrated:** that broad speech-state classes are separable from EEG+coherence features at well above chance; it did **not** demonstrate word-level (direction-word) decoding.
- **Key limitation flagged by authors:** mostly fixed stimulus order across participants (possible fatigue/order confound); no EMG-based trial rejection despite EMG showing detectable subvocalization during "covert" trials.
- **Relevance to our project:** Closest recent methodological template — paired overt/covert design, explicit function-first vocabulary rationale, multilingual design. Its self-initiated keypress marker is a concern for our long-term assistive-communication motivation (see `docs/experimental_protocol.md`, Section 14) since it depends on reliable motor function.
- **Dataset / code:** doi.org/10.5281/zenodo.20374418 (dataset)

### Zhang et al. (2024) — Chisco: An EEG-based BCI dataset for decoding of imagined speech
- **Venue:** Scientific Data, 11, 1265. DOI: 10.1038/s41597-024-04114-1
- **Language:** Chinese
- **Task:** Large-scale imagined-speech recording (thousands of sentences)
- **EEG setup:** High-density EEG; full details in original paper (not reproduced here — verify before citing exact channel count)
- **What the paper actually demonstrated:** A large open dataset with a full public preprocessing/decoding pipeline; semantic-level decoding results reported in the original paper (exact accuracy figures not reproduced here — verify against source before citing).
- **Relevance to our project:** Closest full end-to-end template for dataset scale and public pipeline structure, though at a scale (20,000+ sentences) well beyond what our team can realistically collect in this phase.

### Almufareh, Kausar, Humayun, Tehsin & Farooq (2025) — Inner Speech Decoding: A Comprehensive Review
- **Venue:** WIREs Cognitive Science, 16(6). DOI: 10.1002/wcs.70016
- **Type:** Review, not a primary dataset paper
- **What the paper actually demonstrated:** A synthesis of preprocessing approaches, ML/DL methods, existing datasets, and open research gaps in inner-speech decoding; not new experimental results of its own.
- **Relevance to our project:** Best single source for locating where our project sits relative to the field's current gaps and standard practices; used to sanity-check our own design choices against broader consensus.

## B. Covert Speech

### Lopez-Bernal, Balderas, Ponce & Molina (2022) — A State-of-the-Art Review of EEG-Based Imagined Speech Decoding
- **Citation status:** As provided by project notes; **to verify** against original source before formal citation.
- **Type:** Review
- **Relevance to our project:** Referenced for a broad survey of decoding approaches and reported performance ranges across the field; specific claims from this paper should be re-checked against the primary source before being used in our own writing.

### Panachakel & Ramakrishnan (2021) — Decoding Covert Speech From EEG — A Comprehensive Review
- **Citation status:** As provided by project notes; **to verify** against original source before formal citation.
- **Type:** Review
- **Relevance to our project:** Additional review-level source on covert/imagined speech decoding methodology, to be cross-checked against the Almufareh et al. (2025) review for consistency and any updated findings.

### Proix, Delgado Saa et al. (2022) — Imagined speech can be decoded from low- and cross-frequency intracranial EEG features
- **Citation status:** As provided by project notes; **to verify** exact author list and venue against original source before formal citation.
- **Task:** Imagined speech decoding using **intracranial** (invasive) EEG
- **Relevance to our project:** Important as a contrast case, not a method template — intracranial EEG has a fundamentally different signal-to-noise profile from the non-invasive scalp EEG this project uses, so reported accuracy figures from this line of work are not directly comparable to what we should expect.

## C. Hindi / Bilingual Speech

### IEEE EMBC (2017) — Bilingual unspoken speech decoding using Hindi and English
- **Citation status:** As provided by project notes; **full bibliographic details (exact title, authors) to verify** against the IEEE EMBC 2017 proceedings before formal citation. This entry should not be cited further until verified.
- **Relevance to our project:** If verified, this would be directly relevant as prior work specifically involving Hindi in an unspoken/imagined-speech paradigm, and should be prioritized for full reading once confirmed.

## D. Vocabulary Design

### Turk et al. (2025) — Word-specific properties affect classification performance in Brain Computer Interfaces for decoding imagined speech from EEG
- **Citation status:** As provided by project notes; **to verify** exact venue and author list before formal citation.
- **Relevance to our project:** Directly relevant to `docs/vocabulary_rationale.md` — supports the general point that linguistic properties of individual words (not just their category) can affect how well they are classified, reinforcing why we plan to record linguistic properties per vocabulary item in `vocabulary/vocabulary_master.csv` even before they are measured.

## E. EEG Preprocessing

Preprocessing methodology in this project draws primarily on the
approaches described in Kostulin et al. (2026) and Hollenstein et al.
(2020, *ZuCo 2.0* — reading/eye-tracking EEG corpus, not imagined
speech, but a well-documented preprocessing and validation methodology;
see prior team review notes). No preprocessing-specific review paper
has yet been added to this section; to be expanded.

## F. Public Datasets

### Lara, Takacs & Rodríguez (2024) — EEGIS: Electroencephalogram Imagined Speech Dataset
- **Source:** Mendeley Data. DOI: 10.17632/73g4fw884c.1 (published 2 December 2024)
- **Language:** Spanish
- **Task:** Imagined speech, single words + rest state
- **Participants:** 10
- **EEG setup:** Emotiv EPOC+, 14 channels, 128 Hz; data provided as 1-second chunks, also pre-split into five frequency bands (delta, theta, alpha, beta, gamma)
- **Vocabulary:** Sí (yes), No (no), Baño (bathroom), Hambre (hunger), Sed (thirst), Ayuda (help), Dolor (pain), Gracias (thank you) — eight functional words + rest
- **Screening criteria (as reported):** right-handed, no CNS-affecting medication, ages 20–30, non-smoker, no alcohol/drug use, no epileptic history
- **What the paper actually demonstrated:** A released, structured dataset; the description available to us does not include classification results — **no accuracy figures should be attributed to this entry** without checking the primary source directly.
- **Relevance to our project:** The closest vocabulary-design precedent to our own core set — note the direct overlap in category (yes/no, help, pain, hunger/thirst-adjacent needs). Low channel count (14) and consumer-grade hardware (Emotiv EPOC+) is also a relevant precedent if our own hardware access is similarly limited.

### 2020 International BCI Competition — Track 3 (Imagined Speech)
- **Citation status:** As provided by project notes; **to verify** exact organizing body, dataset details, and result reporting before formal citation.
- **Task (as described in project notes):** Five-class imagined speech classification using functional commands/communication words (reported as including: Hello, Help me, Stop, Thank you, Yes)
- **Relevance to our project:** If verified, directly relevant as another precedent for a small, functional, communication-oriented vocabulary design, reinforcing the category choices in `docs/vocabulary_rationale.md`.

## G. Assistive Communication

No dedicated assistive-communication-specific paper has been added to
this section yet beyond the general motivation discussed in the
datasets above (EEGIS, BCI Competition Track 3, Kostulin et al.'s
discussion of BCI applications). To be expanded as the team identifies
and reviews further sources specifically on AAC (augmentative and
alternative communication) system design.

## H. Future Clinical Applications

No clinical-application-specific literature has been reviewed yet. This
section is intentionally left minimal: per `docs/ethical_considerations.md`,
this project does not currently pursue clinical or diagnostic
applications, and literature in this area should only be added once
that scope is deliberately and formally expanded, with appropriate
ethical oversight.

---

## Summary Table

| Ref | Year | Language | Task | N | Vocabulary size | Accuracy reported | Citation status |
|---|---|---|---|---|---|---|---|
| Kostulin et al. | 2026 | Russian & Spanish | Overt+covert directional words | 22 | 6–7 | 78±4% (3-class state, not word-level) | Verified |
| Zhang et al. (Chisco) | 2024 | Chinese | Imagined speech, large-scale | Not reproduced here | Thousands of sentences | See source | Verified (details to re-check) |
| Almufareh et al. | 2025 | Review | — | — | — | — | Verified |
| Lopez-Bernal et al. | 2022 | Review | — | — | — | — | To verify |
| Panachakel & Ramakrishnan | 2021 | Review | — | — | — | — | To verify |
| Proix et al. | 2022 | Intracranial EEG | Imagined speech | — | — | — | To verify |
| IEEE EMBC | 2017 | Hindi/English | Unspoken speech | — | — | — | To verify |
| Turk et al. | 2025 | — | Word-property effects | — | — | — | To verify |
| Lara, Takacs & Rodríguez (EEGIS) | 2024 | Spanish | Imagined speech, single words | 10 | 8 + rest | Not reproduced here | Verified (dataset description) |
| BCI Competition Track 3 | 2020 | Multiple | Imagined speech, 5-class | — | 5 | — | To verify |

**Action item:** entries marked "To verify" should be resolved (full
citation confirmed or entry removed) before this document is used in
any formal report or thesis chapter.
