# Day 0 — Setup + the four tones + what pinyin is
**Today builds the machine; tomorrow it runs.** No date on this card: a plan-day is not a calendar-day (README §7). The date goes in `tracker.md` the day the gate passes.

**Banked from 3 Jul — already done, do not redo:** Praat installed ✔ · uv project + `scripts/tone_compare.py` working ✔ · baseline recording `recordings/baseline.wav` ✔. You are ~40 minutes into this card, not at zero.

## Session opener — every session, 90 seconds, before anything else
```
uv run python scripts/tone_compare.py --record ma1
```
One syllable → a verdict + a contour picture. You are playing before you are studying. Then decide: one unit, or many.

## Hard gate (pass before advancing)
1. Setup checklist (README §9) fully ticked, **and**
2. All **4 tones on 5 syllables** (mā má mǎ mà · bā bá bǎ bà …): `tone_compare.py` reads ≥16/20 recordings as the intended tone (where the classifier is unsure, the overlay visibly matching the native model counts).

If missed → repeat as `day00-r1`, add nothing new (README §7).

## Units — each ≤25 min, each ends at a ✔, stopping after ANY of them is a valid day
| # | ~min | Do | ✔ Win |
|---|---|---|---|
| U1 | 20 | Install Pleco (+ add-ons) and Anki | both apps open |
| U2 | 25 | Import official HSK 1–2 deck built from the syllabus PDF (`decks/`) | deck visible in Anki; flip the first 5 cards |
| U3 | 20 | **Game:** `tone_compare.py --record` ma1 · ma2 · ma3 · ma4 | ≥2/4 verdicts = intended tone |
| U4 | 20 | **Game:** bā bá bǎ bà; replay the native model, re-record your worst one | ≥3/4 match |
| U5 | 25 | Pinyin ≠ English letters: c · q · x · zh · r · ü — hear each, say each | record all 6 traps once; spot-check 2 in Praat |
| U6 | 20 | Native four-tone audio: one passive pass, then active | ID the tone of 10 played syllables, ≥7 right |
| U7 | 10 | Fill tracker Day-0 row + PASS commit (line below) | pushed |

**MIN DAY (streak keeper):** any single unit — U3 alone counts. Commit it:
`unit: day00 U3 tone game 3/4 | 20m`

**Hot day:** chain U1→U7, pass the gate, then open `day-01.md` and keep going — its blocks split into units the same way (README §0). Stage A never does two *cards* in one day (tones are day-gated), but finishing tomorrow's SRS block early is fair game.

## Materials
Pleco · Anki · HVPT source · native four-tone audio · official syllabus PDF · **Praat + `scripts/tone_compare.py`** (record → verdict → overlay vs native model).

## Self-test
Play your 5-syllable set back-to-back against the native model. Contours match? Setup boxes all ticked? Tone-pair baseline to beat: **32.5%** (tracker, 19 Jun).

## Commit when done
`day00: setup done + 4 tones produced | <h>h | vocab 0`
