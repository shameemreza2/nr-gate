# HSK Plan 01

A gated, evidence-first study plan that takes a zero-Chinese, Bangla-L1 learner to an **HSK 3 written + HSKK 初级 (speaking) credential as fast as honestly possible** — because a telecom internship in Shenzhen is the financial exit, and earlier beats later.

It runs in two phases. Each is an *engine*: a folder of daily checklists, each with **one hard gate**, where a day advances only when its gate passes, and **one git commit per passed day** becomes the executed-hours log — the single metric that predicts whether the plan lands.

---

## Repo map

| Path | What it is |
|---|---|
| `phase1/` | **Pre-departure sprint** (Day 0 = 15 Jul 2026 → fly 1 Sep 2026). Tone-first: tones to ≥97% + full HSK 3 vocabulary (1,000 words) + 655 recognition characters. `README.md` = engine + 48-day map; `day-NN.md` = daily cards. |
| `phase2/` | **In-China exam sprint** (Day 0 ≈ 7 Sep 2026 → exam Sat 7 Nov 2026). HSK 3 (2.0) written + HSKK 初级. `README.md` = engine + 62-day map; `day-NN.md` = daily cards. |
| `tracker.md` | The executed-hours + gate log for both phases. **The one file that must never lie.** |
| `scripts/`, `tests/` | HVPT tone-trainer + HSK deck builder (extracts the official word/character lists from the syllabus PDF). |
| `graphify-out/` | Knowledge graph of the whole plan (`graph.html` to browse) + the verified Phase 2 exam research (`.phase2_research_raw.json`). |
| `hsk5_*.md` | Parent feasibility report + the slower v2 year-plan this accelerated track sits inside. |
| `新版HSK考试大纲1219.pdf` | The official syllabus (pub. 2025-11) — the source of every word/character count. |

Start at `phase1/README.md` or `phase2/README.md`.

---

## The daily check-in (non-negotiable)

These are the standing laws. Do them and **record them** every study day — the log *is* the plan.

1. **One commit per passed day.** When a day's hard gate passes, fill the `tracker.md` row and commit. The message is the log: `dayNN: <gate result> | <hours> | <vocab/mock/hw>`. A day with no commit didn't happen.
2. **SRS floor — never zero.** ≥20 min of spaced review (vocabulary + a tone spot-check) *every single day* — deload days, travel days, exam-eve, ever. This is the load-bearing wall (see flag #1).
3. **Evidence-first — log the measured number, not a feeling.** Tone-pair ID %, mock score (with section split), handwriting count, deck count. A number you didn't measure does not exist.
4. **Gate discipline — master before moving on.** Advance only when the day's gate passes. **Slip rule:** if it misses, the next calendar day *repeats the same gate and adds nothing new* (`dayNN-r1`, `-r2`, …). Plan-day ≠ calendar-day.
5. **Production discipline (anti-fossilisation).** Every new word/HSKK answer/handwritten character is recorded or written and checked against a model at least once.
6. **Weekly audit (Sundays).** Deload + one mock + tone audit (+ handwriting error review in Phase 2). Half load, no new material.
7. **Phase 2 only — register early and confirm the format.** Pre-create the chinesetest.cn account *before flying*; register the moment you've settled; and on **Day 28 (≈5 Oct) confirm 2.0 vs 3.0 at the venue before paying** (see flag #6).

---

## Flags that make the whole plan moot

If any of these trips, **stop and re-plan** — the calendar and gates as written no longer hold. They are listed worst-first.

| # | Flag | Why it breaks the plan | What to do |
|---|---|---|---|
| 1 | **SRS floor breaks** (zero review for a stretch) | The review backlog avalanches and retention collapses. The feasibility report states it outright: *the plan only breaks if the SRS floor breaks.* | Never let it hit zero. If broken >2–3 days, re-baseline vocabulary before adding anything new. |
| 2 | **Tone gate never clears 95%** | Phase 1 gates all vocab scaling on ≥95% tone-pair ID. If tones plateau below that for weeks, the unlock never opens, the 1,000-word delivery fails, and **Phase 2's entire starting-state assumption is false.** | Do not fake the gate. If tones stall, the whole timeline must be recomputed — tones are day-gated, not crammable. |
| 3 | **Phase 1 under-delivers** (arrive without ~1,000 vocab / 655 recognition / tones ≥97%) | Phase 2's "short sprint" premise is that the hard part is already done. If it isn't, Phase 2 becomes a from-scratch build and the Nov 7 target is fiction. | Measure the *real* handoff numbers on arrival; recalibrate Stage A bars or slip the exam. |
| 4 | **Start/fly/arrival dates move** (Day 0 ≠ 15 Jul; departure ≠ ~1 Sep) | Every gate is date-anchored off these. A shifted start cascades through both phases. | Recompute both calendars from the new anchor; the gate ladder stays, the dates move. |
| 5 | **Capacity collapses** (financial emergency, or the part-time job eats below the 2 h/day floor for weeks) | Gates stall, the exam slips indefinitely, and the credential timeline — the whole point — evaporates. | If hours can't hold the floor, cut scope to exam-only (drop telecom/abstracts) or push the sitting. Don't pretend. |
| 6 | **The HSK 3.0 switchover lands at the venue** | Phase 2 is built **2.0-first**. If 深圳大学 administers 3.0 by registration, the 2.0-tuned bars and lighter writing are wrong — 3.0 demands the full 150 书写字 + a different speaking paper. | Confirm the format on **Day 28 before paying**. If 3.0: re-aim **Dec 13** and extend the over-prep stage. This is the single biggest external unknown. |
| 7 | **Registration deadline missed** | No registration = no exam that cycle, regardless of readiness. IBT closes ~10 days before (Nov 7 → deadline 28 Oct). | Pre-create the account before flying; register the moment you're settled; watch the deadline in the Day-51 card. |
| 8 | **The "why" changes** (internship no longer the exit, or funding removes the pressure) | The entire acceleration — earliest-possible sitting, telecom/abstracts in parallel — is justified by the internship being the financial exit. Remove that, and the slower parent v2 year-plan is the better track. | Re-decide priorities. This repo is the **fast** track, not the only one. |
| 9 | **The verified facts go stale** (a new official notice changes HSK 3 structure, dates, or counts) | The plan rests on syllabus counts + 2.0 format facts verified 2026-06-19. An official change invalidates the bars. | Re-verify on chinesetest.cn at registration; the research snapshot is in `graphify-out/.phase2_research_raw.json`. |

---

## How to read a day

1. Open `phaseN/day-NN.md`. There is **one hard gate** and a block plan.
2. Do the work. Hit the gate. Log the measured result in `tracker.md`.
3. **Pass** → commit, move on. **Miss** → repeat the gate tomorrow, add nothing new (`-r1`).
4. Sundays are deload + audit. Keep the SRS floor regardless.

The fly date and the exam date never move on their own — the *gates* decide when you're ready, and the credential never ships under-prepared.
