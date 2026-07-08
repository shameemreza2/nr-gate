# Day 10 — Mon 13 Jul 2026 · Week 2 · Stage A
**Multi-speaker generalisation.** Accuracy on one voice ≠ real perception. Force new speakers so the category generalises (this is what makes the gains durable).

## Hard gate
Tone-pair ID **≥80%** **and** **T2↔T3 ≥68%**, on speakers you have not trained on. Missed → `day10-r1`.

## Blocks (~5.5 h)
- 0:50 — HVPT with **new/unfamiliar speakers** only.
- 0:45 — Production: record, compare to a *different* native model than usual.
- 0:25 — Reading tones.
- 1:15 — SRS: **+20 words** (→155) + reviews.
- 0:45 — Listening (new voice).
- 0:30 — Reading.
- 0:20 — Log + commit.

## Self-test
New-speaker pair test ≥80%; T2↔T3 ≥68%.

## Commit when done
`day10: pair <x>% / T2T3 <y>% (new spkr) | <h>h | vocab 155`
