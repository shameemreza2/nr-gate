# Phase 1 Tracker — executed hours + gate log

The one metric that predicts everything: **executed hours per week.** Fill a row when each day's gate passes (or slips). Keep it honest — a slip logged is data; a slip hidden breaks the plan.

**Gate convention (enforced by `hooks/commit-msg`):** a day PASSES only when its row has **hours + the day's metric filled and the Gate? cell set to ✅**. Leave `☐` for not-done; log a miss as a slip (`dayNN-rN`). The commit hook blocks a `dayNN`/`p2-dayNN` PASS commit unless that row is ✅ **and** the previous day is ✅ (no skipping). See repo `README.md`.

## Running totals

| | Target | Actual |
|---|---|---|
| Days passed | 48 | 0 |
| Hours logged | ~250–280 | 0 |
| Vocab (cum) | ~1,075 (full HSK 3 vocab, 1,000) | 0 |
| Recognition chars | ~655 (full HSK 3 set) | 0 |
| Tone-pair ID (latest) | ≥97% by fly | — |
| Unlock cleared? | ~Day 21 | no |
| Adjusted vocab target | 1,075 | 1,075 |

> Auto-shrink rule: each slip lowers the adjusted vocab target by ~35. Update the cell above.
> Level boundaries: 300 = HSK 1 · 500 = HSK 2 · 1,000 = HSK 3 · 2,000 = HSK 4.

## Daily log

**Date = the actual day the gate passed — filled in when it happens, never in advance.** Plan-day ≠ calendar-day (phase1/README §7). The only real calendar constraint in Phase 1: **✈ fly 22 Aug 2026.** Streak lives in git, not here: any day with a `unit:` or `dayNN` commit = streak day (phase1/README §0).

| Day | Date | Hours | Tone-pair ID | T2↔T3 | Vocab cum | Gate? | Notes |
|---|---|---|---|---|---|---|---|
| 0 |  | | — | — | 0 | ☐ | 3 Jul partial: Praat + tone_compare.py + baseline.wav banked |
| 1 |  | | | | 10 | ☐ | |
| 2 |  | | | | 25 | ☐ | |
| 3 |  | | | | 40 | ☐ | |
| 4 |  | | | | 40 | ☐ | deload |
| 5 |  | | | | 55 | ☐ | |
| 6 |  | | | | 75 | ☐ | wk1 gate |
| 7 |  | | | | 95 | ☐ | |
| 8 |  | | | | 115 | ☐ | |
| 9 |  | | | | 135 | ☐ | |
| 10 |  | | | | 155 | ☐ | |
| 11 |  | | | | 155 | ☐ | deload |
| 12 |  | | | | 175 | ☐ | |
| 13 |  | | | | 195 | ☐ | wk2 gate |
| 14 |  | | | | 215 | ☐ | |
| 15 |  | | | | 235 | ☐ | |
| 16 |  | | | | 255 | ☐ | |
| 17 |  | | | | 275 | ☐ | |
| 18 |  | | | | 275 | ☐ | deload |
| 19 |  | | | | 290 | ☐ | |
| 20 |  | | | | 300 | ☐ | wk3 gate; ★ HSK1 done (300) |
| 21 |  | | | | 300 | ☐ | UNLOCK |
| 22 |  | | | | 330 | ☐ | sprint start |
| 23 |  | | | | 360 | ☐ | |
| 24 |  | | | | 390 | ☐ | |
| 25 |  | | | | 390 | ☐ | deload |
| 26 |  | | | | 425 | ☐ | |
| 27 |  | | | | 460 | ☐ | |
| 28 |  | | | | 495 | ☐ | |
| 29 |  | | | | 530 | ☐ | ★ HSK2 done (500) |
| 30 |  | | | | 565 | ☐ | |
| 31 |  | | | | 600 | ☐ | |
| 32 |  | | | | 600 | ☐ | deload |
| 33 |  | | | | 635 | ☐ | |
| 34 |  | | | | 670 | ☐ | |
| 35 |  | | | | 710 | ☐ | |
| 36 |  | | | | 750 | ☐ | |
| 37 |  | | | | 790 | ☐ | self-intro draft |
| 38 |  | | | | 830 | ☐ | |
| 39 |  | | | | 830 | ☐ | deload |
| 40 |  | | | | 870 | ☐ | |
| 41 |  | | | | 910 | ☐ | |
| 42 |  | | | | 945 | ☐ | HSK-3 mock 1 |
| 43 |  | | | | 980 | ☐ | HSK-3 mock 2 |
| 44 |  | | | | 1015 | ☐ | ★ HSK3 vocab done (1,000) |
| 45 |  | | | | 1045 | ☐ | full HSK-3 mock |
| 46 |  | | | | 1045 | ☐ | deload; pack |
| 47 |  | | | | 1075 | ☐ | core-curriculum exit gate |
| 48 |  | | | | 1075 | ☐ | buffer 1: hold gate / make-up day |
| 49 |  | | | | 1075 | ☐ | buffer 2: FLY-READY — ✈ fly 22 Aug |

| 2026-06-19 | Day 00 | baseline | 32.5% | T1:33 T2:25 T3:45 T4:21 | T2↔T3:36.7% | ✗ |

> ↑ **The score to beat.** 32.5% at chance level (25%) with zero training. Every HVPT session prints the new number next to this one — the whole game is watching that number climb to 97.

---

# Phase 2 Tracker — exam readiness + gate log

Same rule: a row filled when the day's primary gate passes (or slips). Evidence-first — mock scores, HSKK self-scores, handwriting + deck counts. **Pass = hours + metric + ✅ in Gate? (enforced by `hooks/commit-msg`).**

## Running totals

| | Target | Actual |
|---|---|---|
| Days passed | 61 | 0 |
| Hours logged | ~150–200 | 0 |
| Written full mock (latest) | ≥250/300 (pass 180) | — |
| HSKK mock (latest) | ≥80/100 (pass 60) | — |
| Handwriting chars (cum) | 150 (official 书写字) | 0 |
| Telecom deck (cum) | 700 (seed 200 → intm 450 → adv 700; stop at exam week) | 0 |
| Format confirmed (2.0/3.0)? | by ~Day 28 (Oct 5) | — |
| Registered? | by Oct 28 (Nov 7 IBT) | no |
| Exam result | HSK3 ≥180 + HSKK ≥60 | — |

> Branch rule: 2.0 at venue → Nov 7. 3.0 at venue → Dec 13 (extend Stage B/C). Pull-forward Oct 17 only if Day-34 gate clears early + cheap reschedule.

## Daily log

| Day | Date | Hours | Written mock | HSKK | HW cum | Deck cum | Gate? | Notes |
|---|---|---|---|---|---|---|---|---|
| 0 | Mon 7 Sep | | baseline | — | 0 | 0 | ☐ | setup + REGISTER + confirm 2.0/3.0 |
| 1 | Tue 8 Sep | | | | | | ☐ | reading technique |
| 2 | Wed 9 Sep | | | | | | ☐ | listening technique |
| 3 | Thu 10 Sep | | | | ~15 | | ☐ | handwriting start |
| 4 | Fri 11 Sep | | | | | | ☐ | HSKK Part 1 |
| 5 | Sat 12 Sep | | | | | | ☐ | reading P3 + writing P1 |
| 6 | Sun 13 Sep | | baseline | | | | ☐ | deload: diagnostic mock |
| 7 | Mon 14 Sep | | | | ~25 | | ☐ | |
| 8 | Tue 15 Sep | | | | | | ☐ | reading full section |
| 9 | Wed 16 Sep | | | | | | ☐ | |
| 10 | Thu 17 Sep | | | | | | ☐ | full 书写 drill |
| 11 | Fri 18 Sep | | | | | | ☐ | HSKK Part 2 |
| 12 | Sat 19 Sep | | | | | | ☐ | |
| 13 | Sun 20 Sep | | ≥200 | | | | ☐ | deload: mock |
| 14 | Mon 21 Sep | | | | ~40 | | ☐ | |
| 15 | Tue 22 Sep | | | | | | ☐ | |
| 16 | Wed 23 Sep | | | | | | ☐ | |
| 17 | Thu 24 Sep | | | | | | ☐ | |
| 18 | Fri 25 Sep | | | | | | ☐ | HSKK Part 3 |
| 19 | Sat 26 Sep | | | | | | ☐ | full timed mock |
| 20 | Sun 27 Sep | | ≥215 | ≥70 | ~55 | | ☐ | deload ★ 2.0 covered |
| 21 | Mon 28 Sep | | | | ~60 | | ☐ | begin 150 over-prep |
| 22 | Tue 29 Sep | | | | | | ☐ | |
| 23 | Wed 30 Sep | | | | | | ☐ | |
| 24 | Thu 1 Oct | | | | | | ☐ | |
| 25 | Fri 2 Oct | | | | | | ☐ | HSKK full run |
| 26 | Sat 3 Oct | | | | | | ☐ | full mock |
| 27 | Sun 4 Oct | | ≥230 | ≥75 | | | ☐ | deload |
| 28 | Mon 5 Oct | | | | ~95 | | ☐ | **FORMAT DECISION + reg** |
| 29 | Tue 6 Oct | | | | | | ☐ | |
| 30 | Wed 7 Oct | | | | | | ☐ | Oct-17 IBT deadline |
| 31 | Thu 8 Oct | | | | | | ☐ | |
| 32 | Fri 9 Oct | | | ≥78 | | | ☐ | |
| 33 | Sat 10 Oct | | | | | | ☐ | full mock |
| 34 | Sun 11 Oct | | ≥240 | ≥80 | ~130 | | ☐ | deload ★ 2.0 SECURED |
| 35 | Mon 12 Oct | | | | | 200 | ☐ | ★ seed deck done |
| 36 | Tue 13 Oct | | | | | | ☐ | pitch draft; start intermediate deck |
| 37 | Wed 14 Oct | | | | | | ☐ | |
| 38 | Thu 15 Oct | | | | | | ☐ | sentence writing |
| 39 | Fri 16 Oct | | | | | | ☐ | |
| 40 | Sat 17 Oct | | | | | | ☐ | (pull-forward exam date) |
| 41 | Sun 18 Oct | | ≥245 | | 150 | | ☐ | deload ★ 150 first-pass |
| 42 | Mon 19 Oct | | | | | | ☐ | 150 consolidation |
| 43 | Tue 20 Oct | | | | | | ☐ | full timed mock |
| 44 | Wed 21 Oct | | | | | | ☐ | weak-item clear |
| 45 | Thu 22 Oct | | | | | | ☐ | |
| 46 | Fri 23 Oct | | | ≥80 | | | ☐ | HSKK timed |
| 47 | Sat 24 Oct | | | | | | ☐ | full mock |
| 48 | Sun 25 Oct | | ≥250 | | | 450 | ☐ | deload; ★ intermediate deck done |
| 49 | Mon 26 Oct | | | | | | ☐ | start advanced deck (if no exam conflict) |
| 50 | Tue 27 Oct | | | | | | ☐ | full timed mock |
| 51 | Wed 28 Oct | | | | | | ☐ | **Nov-7 IBT reg deadline** |
| 52 | Thu 29 Oct | | | | | | ☐ | short-passage (3.0) |
| 53 | Fri 30 Oct | | | ≥80 | | | ☐ | |
| 54 | Sat 31 Oct | | | | | | ☐ | exam-conditions mock |
| 55 | Sun 1 Nov | | ≥250 | ≥80 | | | ☐ | deload; ★ exam week — freeze telecom deck here |
| 56 | Mon 2 Nov | | | | | | ☐ | HSK focus only |
| 57 | Tue 3 Nov | | | | | | ☐ | final calibration mock |
| 58 | Wed 4 Nov | | | | | | ☐ | HSKK final rehearsal |
| 59 | Thu 5 Nov | | | | | | ☐ | error-log sweep |
| 60 | Fri 6 Nov | | | | | | ☐ | rest + 准考证 printed |
| 61 | Sat 7 Nov | | | | | | ☐ | **✎ EXAM DAY** |
| 2026-06-24 | Day 00 | baseline | 31.2% | T1:20 T2:38 T3:32 T4:36 | T2↔T3:34.2% | ✗ |