# Decision Log

A running record of significant design decisions, why they were made,
what alternatives were considered, and who approved them. The point of
this file is to show — to Dr. Goyal, to future team members, and to our
future selves — that design choices were reasoned through, not made
arbitrarily. Add a new row whenever a non-trivial decision is made or
revisited. Do not delete old rows even if a decision is later reversed;
add a new row noting the reversal and why.

| Date | Decision | Reason | Alternatives Considered | Approved By |
|---|---|---|---|---|
| TBD | Project narrative emphasis: lead with "assistive communication," with mental-health-related communication framed explicitly as a future application area, rather than leading with "mental health" | Reduces risk that the project's EEG-decoding results are misread as mental-state or clinical detection; keeps the core, defensible claim (communication intent decoding) separate from the more speculative future one | Keep original title/framing unchanged; drop mental-health framing entirely | Pending — recommendation only, not yet discussed with Dr. Goyal |
| TBD | Candidate vocabulary uses communication-first categories (basic communication, assistance, physical need, emotional state) rather than phonetically-optimized or randomly selected words | Matches the project's assistive-communication goal; follows the explicit function-first rationale used in Kostulin et al. (2026) | Purely phonetically-distinct word list; randomly selected word list | Pending |
| TBD | Event markers: leaning toward cue-locked (fixed-duration) design over self-initiated keypress marking | A keypress-based marker is incompatible with the project's long-term target population (e.g. motor-impaired patients); cue-locked design keeps the protocol closer to eventual real-world usability | Self-initiated keypress marker (used in Kostulin et al. and similar work) | Pending — not yet piloted or approved |
| TBD | EMG monitoring under consideration, for a subset of participants if feasible | Directly addresses the subvocalization confound documented in prior imagined-speech literature; provides an evidence-based way to flag contaminated "covert" trials rather than trusting instruction alone | EEG-only recording, relying on instruction and post-hoc visual inspection only | Pending — depends on hardware/lab access |
| TBD | Emotional/extended vocabulary items (दवा, खुश, डर, चिंता) will NOT be included in the first pilot unless Dr. Goyal specifically requests it; core communication/need words go first | Keeps the first pilot's purpose unambiguous (testing communication-word decodability) and avoids inviting outside misinterpretation of emotional-word stimuli as an emotion-detection experiment | Include full vocabulary (core + extended) from the first pilot | Pending |
| TBD | रुको ("Stop / Wait") flagged as a potentially ambiguous item bundling two distinct intentions | A single word covering two different communicative intents is a weaker stimulus for a future real communication system; needs either disambiguation or splitting into two items | Leave as-is; split into separate "Stop" and "Wait" items | Pending — flagged in `vocabulary/vocabulary_master.csv`, not yet resolved |
| TBD | Word → phrase progression (single words first, then short need-phrases, then natural communication) adopted as the intended long-term vocabulary roadmap | Avoids prematurely attempting phrase-level decoding before word-level feasibility is established; consistent with decoding-target levels distinguished in the broader imagined-speech literature | Attempt phrase-level stimuli from the start | Pending — documented as a future direction in `docs/vocabulary_rationale.md`, not yet started |
| TBD | Handedness recorded for all participants; no automatic exclusion of left-handed participants | Avoids excluding participants based on unexamined literature convention rather than a stated, project-specific reason | Restrict initial cohort to right-handed participants only, as several reviewed datasets do | Pending |
| TBD | Age range 18–45 adopted as a proposed default, to be explicitly revisited rather than fixed by convention | Same reasoning as above — inclusion criteria should be justified for this project, not copied from other studies by default | Narrower or wider age range | Pending |
| TBD | Evaluation plan will report within-subject and cross-subject (subject-independent) performance separately, not a single blended accuracy number | Cross-subject performance is much closer to the real-world assistive-communication use case and is known to be substantially harder than within-subject performance in this literature; reporting only a favorable split risks overstating generalization | Report only within-subject accuracy | Pending — to be formalized once `code/analysis/` is implemented |
| TBD | Pilot recording (2–3 team members) will be explicitly labeled a "protocol pilot / usability pilot," not a decoding feasibility study, and its results will not be used to make claims about the main dataset | Prevents a small, non-representative internal test from being mistaken for (or presented as) evidence about the real dataset's decodability | Treat pilot results as preliminary decoding evidence | Pending |

---

## How to Use This Log

- Every row should have a clear **Reason**, not just a decision — a
  decision without a stated reason is exactly what this log exists to
  prevent.
- **Alternatives Considered** should be genuine alternatives that were
  actually discussed, not filled in retroactively to look thorough.
- **Approved By** should name the actual person/meeting where the
  decision was confirmed. Until that happens, leave it as "Pending" —
  do not write a name in this column to make an entry look more settled
  than it is.
- When a past decision is revisited or reversed, add a **new** row
  referencing the old one, rather than editing the old row in place.
