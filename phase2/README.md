# Phase 2 — In-China Sprint: Pass HSK 3 + HSKK 初级, As Early As Possible

**The phase that converts Phase 1's hidden vocabulary + tone base into two paper credentials, then a supervisor pitch — fast, because the internship is the exit.**
Day 0 = **Mon 7 Sep 2026** (arrive 1 Sep + ~5 settle days) · Primary exam target = **Sat 7 Nov 2026** · **gate-driven** (the calendar bends to mock scores, the credential does not).

This folder is the *engine*, same as Phase 1. Each `day-NN.md` is one execution checklist with **one hard primary gate** plus standing floors. You do not advance the spine until that gate passes. Git history (one commit per passed day) is your executed-hours log.

> Plan files are plain English on purpose — you read them daily.

---

### What Phase 1 hands Phase 2 (the starting state)

By fly day (1 Sep 2026) Phase 1 delivers: **full HSK 3 vocabulary (1,000 words)**, **655 recognition characters**, **tones ≥97% (T2↔T3 ≥95%)**. So Phase 2 starts with **zero new-vocabulary pressure** — the 1,000-word base already exceeds everything HSK 3 written and HSKK 初级 demand. That single fact is why Phase 2 can be short, and why the telecom deck + abstracts can run in parallel instead of fighting for SRS load.

**What Phase 2 must still build:** (a) **exam technique** for the 2.0 written + speaking under the clock, (b) **handwriting production from zero** (Phase 1 was recognition + IME only — she has never hand-written these characters), (c) **spoken delivery fluency** for HSKK 初级, and (d) the internship differentiators — **telecom seed deck + Chinese-abstract skimming**.

---

### Verified exam facts — researched & adversarially checked 2026-06-19  **[R]**

Sources: chinesetest.cn official notices/calendar, hskonline (SuperTest mirror), global-exam, chinaeducenter, mandarinzone, goeastmandarin. Raw research saved at `graphify-out/.phase2_research_raw.json`.

1. **The 2026 exam is the OLD HSK 2.0, not the new 3.0.** chinesetest.cn states plainly: HSK 3.0 ran a one-off global **trial** on 31 Jan 2026; **"2026 regular exam dates still run version 2.0"**; the real 3.0 switchover is **"另行通知" (announced separately — still unconfirmed, possibly 2027)**. The widely repeated "3.0 effective July 2026" is the **syllabus** publication date (考试大纲, pub. 2025-11), **NOT** the exam-administration switchover. **You sit 2.0.**

2. **HSK 3 (2.0) written format:** 80 questions / ~90 min / **300 pts / pass = 180 (60%)**, three sections each scored to 100:
   - **听力 Listening** — 40 questions (4 parts).
   - **阅读 Reading** — 30 questions (3 parts).
   - **书写 Writing** — 10 questions: Part 1 = arrange jumbled words into a sentence (5); Part 2 = **write the correct character from pinyin** (5). Handwriting **is** required, but the 2.0 scope is small, and you only need 180/300 overall — a weak writing section survives on strong listening + reading.

3. **There is no fixed "150 书写字" list in 2.0.** The 150-character handwriting list is a **3.0** feature. In 2.0 the fill-in characters are drawn from the HSK 3 vocabulary you already recognise. *(We still grind the full official 150 — see the hedge below.)*

4. **Speaking = HSKK 初级 (Beginner)** — the operative 2026 speaking test (not "HSK 3 口语", which is a 3.0 construct). 3 parts / 27 items / **~20 min (incl. 7 min prep) / 100 pts / pass = 60**, recorded into a microphone. Lexical floor ≈ **200 words**; you arrive with **1,000**. The binding constraint is **delivery fluency under the clock**, not vocabulary. Parts: 1) 听后重复 listen-and-repeat (15 items / 6 min); 2) 听后回答 listen-and-answer (10 / 4 min); 3) 回答问题 answer printed questions, ≥5 sentences each (2 / 3 min).

5. **Dates & registration (Shenzhen, at 深圳大学 国际交流学院).** HSK 1-6 **and** HSKK 初级 run on the **same days**: **2026-09-13 (Sun), 10-17 (Sat), 11-07 (Sat), 12-13 (Sun).** Internet-based (IBT, at-center) registration closes **~10 days** before; paper-based (PBT) **~27 days** before. Register online at chinesetest.cn. Fees ≈ **350 RMB (HSK 3)** + **~200 RMB (HSKK 初级)** — confirm at checkout.

6. **Earliest realistic sitting** for a 1 Sep arrival: **Oct 17** (IBT deadline Oct 7) is the first *comfortable* date; **Sep 13** (IBT deadline Sep 3) is technically open but needs the account pre-created before flying; **Nov 7** (IBT deadline Oct 28) is the chosen primary; **Dec 13** is the slip fallback.

---

### The format hedge (why we still over-prepare)  **[D]**

The 3.0 switchover date is officially unannounced. There is a small but real chance the **深圳大学** centre is running 3.0 by the time we register (~Oct). 3.0 written demands the **150 书写字 handwriting** and a heavier 书写 section; 3.0 speaking is a different paper. So the plan is built **2.0-first, 3.0-insured**:

- **Cover 2.0 perfectly first** (the floor — guarantees a pass on the format that is actually available now).
- **Then grind the full official 150 书写字 + sentence/short-passage writing** as over-preparation. Building handwriting to 3.0 standard automatically covers the lighter 2.0 demand.
- **At registration (~Day 28, Oct 5), confirm the venue's actual format.** If it is **2.0 → sit Nov 7** (or pull forward to Oct 17 if mocks already clear and a cheap reschedule exists). If it is **3.0 → re-aim Dec 13** and extend the over-prep stage with 3.0-specific drills (the 150 list + 3.0 speaking sample).

The official **HSK 3 150 书写字 list is extractable from the syllabus PDF already in the repo** (`新版HSK考试大纲1219.pdf`, the same file Phase 1 parsed via `scripts/build_decks.py`).

---

## 1. Locked parameters

| Param | Value | Source |
|---|---|---|
| Day 0 | **Mon 7 Sep 2026** (arrive 1 Sep + ~5 settle days) | derived |
| Primary exam target | **Sat 7 Nov 2026** — HSK 3 (2.0) written + HSKK 初级, same day | your call |
| Pull-forward option | **Sat 17 Oct 2026** if mocks clear by ~Oct 5 **and** reschedule is cheap | research |
| Slip fallback | **Sun 13 Dec 2026** (and the mandatory target **if the venue is on 3.0**) | your call |
| Work status | **part-time job + grad classes**, hours **not yet fixed** | your confirm |
| Daily budget | **floor 2 h/day**, flex to ~4 h. Gate-driven, never hour-promised | your call |
| Pass bars (design, set above official) | **written full mock ≥ 240/300** (official 180) · **HSKK mock ≥ 80/100** (official 60) | safety margin |
| Handwriting target | 2.0-light first; then **full official 150 书写字 + sentence writing** (3.0 insurance) | your call |
| Parallel tracks | **telecom seed deck (~200 terms)** + **Chinese-abstract skimming** — ride flex hours, never displace the 2.0 spine | your call |

---

## 2. Standing laws (never broken)

1. **2.0 is the floor; the credential is the goal.** The day's primary gate is hard. Miss it → repeat the gate tomorrow, add nothing new (slip rule, §7), logged `dayNN-r1`.
2. **Maintenance floor never zero.** SRS (vocabulary reviews + a tone spot-check ≥97%) every single day — travel days, deload days, ever. Phase 1's gains decay if unfed.
3. **2.0 perfect before 150-grind.** Do not pour hours into the full 150 书写字 over-prep until the 2.0 written mock clears the design bar. Insurance comes after the floor is solid.
4. **Parallel tracks yield to the spine.** Telecom deck + abstracts run on **flex hours only**. On a floor (2 h) day, the spine (maintenance + 2.0 exam + handwriting) wins; telecom/abstracts wait.
5. **Production discipline.** Every HSKK answer and every new handwritten character is recorded / written-and-checked against a model at least once. Weekly audit on Sundays (tone audit + handwriting error review).
6. **Evidence-first.** Mock scores, HSKK self-scores, handwriting counts, and deck counts are logged in `tracker.md`. A number you did not measure does not exist.
7. **One commit per passed day.** The commit message IS your log (§9).
8. **Confirm the format before you pay.** At registration, verify 2.0 vs 3.0 at the venue and branch the plan (§7).

---

## 3. The four tracks

| # | Track | Priority | Load | Goal |
|---|---|---|---|---|
| 1 | **2.0 exam mastery** (听力 + 阅读 + light 书写 + HSKK 初级) | **Spine** | daily, floor-protected | comfortable pass on the available format |
| 2 | **Handwriting → 150 书写字 + sentence writing** | Over-prep (after 2.0 secured) | daily block, grows in Stage B | 3.0 insurance + HIT coursework value |
| 3 | **Telecom seed deck (~200 terms)** | Parallel | flex hours | supervisor pitch + reading, pitch-ready early |
| 4 | **Chinese-abstract skimming** | Parallel (maintenance) | ~10–15 min, flex | ~80% gist of CNKI/IEEE-CN abstracts |

Plus the **maintenance floor** (SRS vocab + tone spot-check) underneath all four, every day.

---

## 4. Stage structure

| Stage | Days | Window | Spine focus | Hard gate to clear the stage |
|---|---|---|---|---|
| **S — Settle / Register** | 0 | Sep 7 | account, register, **confirm 2.0 vs 3.0**, baseline diagnostic, materials | registered + center/format confirmed + SRS unbroken + baseline mock logged |
| **A — 2.0 Lock** | 1–20 | wk 1–3 | drive 2.0 written + HSKK to comfortable-pass mocks; handwriting 2.0-light; deck build starts | **full 2.0 mock ≥ 240/300 + HSKK ≥ 80/100 sustained** |
| **B — 150 Over-prep + Hold** | 21–41 | wk 4–6 | grind full 150 书写字 + sentence writing; hold 2.0 mocks warm; deck → 200 + pitch | **150 written first-pass + 2.0 mocks held ≥ 245**; format decision made (~Day 28) |
| **C — Peak / Sit** | 42–61 | wk 7–9 | full timed mocks, weak-item clear, HSKK rehearsal, logistics | **mock ≥ 250 held + HSKK ≥ 80 → SIT Nov 7** |
| **D — Post-exam** | 62+ | Nov 8 → | results wait, internship applications, pitch delivery, Phase 3 handoff | results in; pitch delivered |

If the venue is on **3.0**, Stage B/C extend and the target moves to **Dec 13** (§7).

---

## 5. Gate ladder (the rising bars)

Mocks are fresh, timed, full-length, never-reused items. Self-score HSKK against the official 评分说明 rubric.

| End of | Day | Written full mock | HSKK mock | Handwriting (cum.) | Telecom deck (cum.) |
|---|---|---|---|---|---|
| Wk 1 | 6 | **baseline** diagnostic (measure only) | familiarise 3 parts | stroke-order + ~15 chars | setup + ~30 terms |
| Wk 2 | 13 | ≥ 200 | Part-1 repeat clean | ~30 chars | ~70 |
| Wk 3 | 20 | ≥ 215 | **≥ 70** | ~55 chars (2.0 covered) | ~110 |
| Wk 4 | 27 | ≥ 230 | **≥ 75** | ~95 chars | ~160 |
| Wk 5 | 34 | **≥ 240 → "2.0 secured"** | **≥ 80** | ~130 chars | **200 (done)** + pitch draft |
| Wk 6 | 41 | ≥ 245 hold | ≥ 80 hold | **150 (first pass)** + sentences | pitch polish |
| Wk 7 | 48 | ≥ 250 hold | ≥ 80 hold | 150 consolidation + speed | maintenance |
| Wk 8 | 55 | ≥ 250 hold | ≥ 80 hold | short-passage writing (3.0) | maintenance |
| Wk 9 | 61 | **SIT** | **SIT** | hold | — |

---

## 6. Full day map (Day 0 → exam)

S = stage. **Primary gate** is the hard advance condition (tone-of-the-day equivalent). Standing floors (SRS maintenance; production discipline) apply every day and are not repeated. Sun = deload (weekly mock + audit, half load). ★ = milestone. Parallel = telecom/abstracts on flex hours.

| Day | Date | Wk | S | Primary gate | Parallel / notes |
|---|---|---|---|---|---|
| 0 | Mon 7 Sep | 1 | S | setup done: chinesetest.cn account, **register HSK3+HSKK for Nov 7**, confirm 2.0/3.0 at 深圳大学, baseline full 2.0 mock logged | install/import decks; handwriting toolkit; SRS continuity check |
| 1 | Tue 8 Sep | 1 | A | reading Part 1–2 technique; timing baseline | deck sources set up |
| 2 | Wed 9 Sep | 1 | A | listening Part 1–2 technique; timing baseline | deck → 20 |
| 3 | Thu 10 Sep | 1 | A | writing Part 2: handwrite first ~15 high-freq chars from pinyin | — |
| 4 | Fri 11 Sep | 1 | A | HSKK Part 1 听后重复 — repeat clean at speed | deck → 30 |
| 5 | Sat 12 Sep | 1 | A | reading Part 3 + writing Part 1 (word order) | abstracts: 4-slot intro |
| 6 | Sun 13 Sep | 1 | A | **deload: baseline diagnostic mock logged** (measure, no bar) | weekly tone audit |
| 7 | Mon 14 Sep | 2 | A | handwriting → ~25 chars | deck → 50 |
| 8 | Tue 15 Sep | 2 | A | reading speed: full reading section under time | — |
| 9 | Wed 16 Sep | 2 | A | listening Part 3–4 technique | deck → 60 |
| 10 | Thu 17 Sep | 2 | A | writing: full 书写 section drill | — |
| 11 | Fri 18 Sep | 2 | A | HSKK Part 2 听后回答 | deck → 70 |
| 12 | Sat 19 Sep | 2 | A | mixed section mocks | abstracts: 25 frame phrases |
| 13 | Sun 20 Sep | 2 | A | **deload: full mock ≥ 200** | weekly audit |
| 14 | Mon 21 Sep | 3 | A | handwriting → ~40 | deck → 85 |
| 15 | Tue 22 Sep | 3 | A | reading traps + speed | — |
| 16 | Wed 23 Sep | 3 | A | listening at speed | deck → 95 |
| 17 | Thu 24 Sep | 3 | A | writing section clean | — |
| 18 | Fri 25 Sep | 3 | A | HSKK Part 3 回答问题 (≥5 sentences) | deck → 110 |
| 19 | Sat 26 Sep | 3 | A | full timed written mock | abstracts: 1/day skim |
| 20 | Sun 27 Sep | 3 | A | **deload: mock ≥ 215 + HSKK ≥ 70** ★ | weekly audit |
| 21 | Mon 28 Sep | 4 | B | handwriting → ~60 (2.0 fully covered; begin 150 over-prep) | deck → 130 |
| 22 | Tue 29 Sep | 4 | B | reading hold | — |
| 23 | Wed 30 Sep | 4 | B | listening hold | deck → 145 |
| 24 | Thu 1 Oct | 4 | B | writing + new chars | — |
| 25 | Fri 2 Oct | 4 | B | HSKK full run-through | deck → 160 |
| 26 | Sat 3 Oct | 4 | B | full written mock | abstracts skim |
| 27 | Sun 4 Oct | 4 | B | **deload: mock ≥ 230 + HSKK ≥ 75** | weekly audit |
| 28 | Mon 5 Oct | 5 | B | **REGISTRATION/FORMAT DECISION: confirm 2.0 vs 3.0; lock Nov 7 (2.0) or re-aim Dec 13 (3.0)**; handwriting → ~95 | pull-forward-to-Oct-17 check |
| 29 | Tue 6 Oct | 5 | B | reading hold | — |
| 30 | Wed 7 Oct | 5 | B | listening hold *(Oct-17 IBT reg deadline — last call for pull-forward)* | deck → 175 |
| 31 | Thu 8 Oct | 5 | B | writing + chars | — |
| 32 | Fri 9 Oct | 5 | B | HSKK hold ≥ 78 | deck → 190 |
| 33 | Sat 10 Oct | 5 | B | full written mock | abstracts skim |
| 34 | Sun 11 Oct | 5 | B | **deload: mock ≥ 240 "2.0 SECURED" + HSKK ≥ 80** ★ | weekly audit |
| 35 | Mon 12 Oct | 6 | B | handwriting → ~130 | deck → 200 ★ |
| 36 | Tue 13 Oct | 6 | B | reading hold | pitch draft |
| 37 | Wed 14 Oct | 6 | B | listening hold | — |
| 38 | Thu 15 Oct | 6 | B | sentence writing (reorder + dictation) | pitch draft |
| 39 | Fri 16 Oct | 6 | B | HSKK hold | — |
| 40 | Sat 17 Oct | 6 | B | full mock *(= pull-forward EXAM date if chosen)* | abstracts skim |
| 41 | Sun 18 Oct | 6 | B | **deload: 150 first-pass done + mock ≥ 245** ★ | weekly audit |
| 42 | Mon 19 Oct | 7 | C | handwriting 150 consolidation + speed | pitch polish |
| 43 | Tue 20 Oct | 7 | C | full timed written mock | — |
| 44 | Wed 21 Oct | 7 | C | listening + reading weak-item clear | — |
| 45 | Thu 22 Oct | 7 | C | writing speed + accuracy | — |
| 46 | Fri 23 Oct | 7 | C | HSKK timed full run ≥ 80 | — |
| 47 | Sat 24 Oct | 7 | C | full written mock | abstracts maintenance |
| 48 | Sun 25 Oct | 7 | C | **deload: mock ≥ 250 held** | weekly audit |
| 49 | Mon 26 Oct | 8 | C | weak-item drilling | — |
| 50 | Tue 27 Oct | 8 | C | full timed written mock | — |
| 51 | Wed 28 Oct | 8 | C | confirm registration final *(Nov 7 IBT reg deadline)*; listening clear | — |
| 52 | Thu 29 Oct | 8 | C | writing + short-passage (3.0 insurance) | — |
| 53 | Fri 30 Oct | 8 | C | HSKK full run ≥ 80 | — |
| 54 | Sat 31 Oct | 8 | C | full mock under exam conditions | — |
| 55 | Sun 1 Nov | 8 | C | **deload: mock ≥ 250 held + HSKK ≥ 80** | weekly audit |
| 56 | Mon 2 Nov | 9 | C | weak-item clear + timing polish | — |
| 57 | Tue 3 Nov | 9 | C | full timed written mock (final calibration) | — |
| 58 | Wed 4 Nov | 9 | C | HSKK final rehearsal | — |
| 59 | Thu 5 Nov | 9 | C | light review + error log sweep | — |
| 60 | Fri 6 Nov | 9 | C | **rest + logistics**: ticket (准考证) printed, ID, route to venue, materials | low load |
| 61 | **Sat 7 Nov** | 9 | C | **✎ EXAM: HSK 3 (2.0) written + HSKK 初级** | — |
| — | Sun 8 Nov → | — | D | results wait (~2–4 wk); internship applications; pitch delivery; Phase 3 | telecom/abstracts maintenance |

---

## 7. Advance / slip / pull-forward / format-branch mechanics

- **Plan-day ≠ calendar-day.** A day-card advances only when its primary gate passes. SRS floor runs regardless.
- **Pass:** log it, commit, move on. **Slip:** next calendar day repeats the same gate, adds no new material, logged `dayNN-r1`, `-r2`, …
- **Parallel tracks float.** If hours are thin, telecom/abstracts pause (logged) — they never cause a spine slip.
- **Format decision (~Day 28, hard):** confirm 2.0 vs 3.0 at 深圳大学.
  - **2.0 →** hold Nov 7. If the Day-34 "2.0 secured" gate clears early **and** a cheap reschedule exists, optionally pull forward to **Oct 17** (register by Oct 7).
  - **3.0 →** re-aim **Dec 13**; Stage B/C extend with the 150-list to mastery + the official 3.0 speaking sample. The ~5 extra weeks absorb the heavier load.
- **Slip fallback:** if mocks are not at bar by late Stage C, slide the sitting Nov 7 → **Dec 13**. The credential never ships under-prepared.

---

## 8. Daily templates

**Floor day (~2 h — spine only, protect this):**
- 0:25 — SRS maintenance: vocabulary reviews + tone spot-check ≥97% *(never zero)*
- 0:40 — Handwriting: new/under-review characters, written-and-checked
- 0:35 — Primary skill of the day (listening / reading / writing / HSKK, per map)
- 0:15 — Log + git commit
≈ **1:55**

**Flex day (~3.5–4 h — adds the parallel tracks + a mock):**
- everything above, plus
- 0:45 — Second exam skill or a timed section/full mock
- 0:30 — Telecom deck (10–15 new terms, looked up + SRS)
- 0:15 — Abstract skim (1–2 abstracts, 4-slot labelling)
- 0:20 — Production: record HSKK answers / extra handwriting vs model

**Sunday deload (~1.5–2 h):** SRS floor + one weekly mock + weekly audit (tone audit + handwriting error review). No new material.

---

## 9. Git / commit protocol

One commit when a day's primary gate passes:

```
git -C "D:\hsk3~5" add phase2/ tracker.md
git -C "D:\hsk3~5" commit -m "p2-dayNN: <gate result> | <hours> | mock <score> hw <cum>"
# e.g.  p2-day20: mock 218 PASS + HSKK 72 | 2.5h | hw 55
# slip: p2-day20-r1: mock 205 (target 215) | 2.0h | hw 55 HOLD
```

`git -C "D:\hsk3~5" log --oneline` is your executed-hours + gate history.

---

## 10. Registration logistics (do early, de-risk)

- **Pre-create the chinesetest.cn account before flying** if possible — keeps the Sep 13 / Oct 17 early options alive and removes day-1 chaos.
- Centre: **深圳大学 国际交流学院** (Nanshan, 南海大道3688号; ciec@szu.edu.cn / 0755-86937695). Confirm it offers your chosen date **and** which format (2.0/3.0).
- Register **HSK 3** and **HSKK 初级** (same day). Watch deadlines: **IBT ~10 days before, PBT ~27 days before**. Nov 7 IBT deadline = **Oct 28**; Oct 17 IBT deadline = **Oct 7**.
- Steps: account + email verify → upload photo → choose level/format/date/centre → personal details → pay (online/transfer) → print 准考证.

---

## 11. What Phase 3 covers (you instruct later)

After the HSK 3 + HSKK 初级 credentials land: telecom deck → supervisor pitch delivered; abstract-skimming to working speed; the **OFDM project** (separate repo, already outlined); and the longer climb toward **HSK 4 / HSK 4 口语** on the parent v2 plan's employability checkpoint timeline. The accelerated internship track and the slow year-plan converge here.
