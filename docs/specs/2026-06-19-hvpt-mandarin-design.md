# HVPT Trainer — Design Spec

**High-Variability Phonetic Training for Mandarin tone perception.**
Date: 2026-06-19 · Repo: `D:\hsk3~5` · Target: Phase 1 (Day 0 = 15 Jul 2026 → fly day 1 Sep 2026)

---

## 1. Goal & context

`phase1/day-00.md` already lists "load HVPT tone source" as a setup step but never defines it. This spec fills that gap: a local, offline, terminal-based HVPT trainer the user runs daily through the tone-first sprint.

It serves the locked Phase 1 parameters (`phase1/README.md`):

- **Unlock gate** (~Day 21): tone-pair ID ≥ 95% overall **and** T2↔T3 ≥ 92% → opens vocab scaling.
- **Fly-day target**: tone-pair ID ≥ 97% overall **and** T2↔T3 ≥ 95%.
- **Bangla-L1 focus**: T2↔T3 is the documented hardest pair; the trainer must over-weight and diagnose it.

The trainer trains **perception only** (the ear). Production (the voice) is handled manually per the Day 0 card (record + compare against native audio); automated production scoring is explicitly Phase 2 (§10).

---

## 2. Scientific basis

The protocol replicates the validated HVPT paradigm:

- **Wang, Spence, Jongman & Sereno (1999, JASA 106):** non-tonal-L1 adults improved Mandarin tone identification ~69% → ~90% in ~2 weeks of training, retained ~6 months, and the gains **transferred to production** without any production drills. This is why a perception-only trainer is sufficient for Stage A.
- **Core mechanism = high variability:** multiple talkers, multiple tokens, randomly interleaved, with **immediate corrective feedback after every trial**. Variability is the active ingredient — it forces talker-independent tone categories rather than memorising one voice.
- **Forced-choice identification:** hear one syllable → choose Tone 1/2/3/4 → instant feedback. No production, no correction window.

**Design rules that follow directly from the science:**

1. Sample talker **and** syllable independently per trial (maximise variability).
2. Tones **interleaved randomly**, never blocked (no runs of one tone).
3. Feedback is **immediate and corrective** (show the correct tone on every miss).
4. Track a **confusion matrix**, not just accuracy — it is the diagnostic that locates the leak (e.g. "heard T2 → said T3").

---

## 3. Data source & access  ⚠️ critical path

**Source: Tone Perfect** (Michigan State University Libraries — Catherine Ryu et al.), `https://tone.lib.msu.edu/`. The closest public equivalent to the lab stimuli HVPT was validated on.

- **Contents:** 410 monosyllables × 4 tones × 6 speakers (3 female `FV1–FV3`, 3 male `MV1–MV3`, Beijing) = **9,840 MP3 files**, ~300 MB (+ ~14 MB XML metadata).
- **License:** non-commercial use only — fine for personal study.
- **Filename format:** `[syllable][tone]_[speaker]_MP3.mp3` — e.g. `fan3_FV1_MP3.mp3`, `fang1_MV2_MP3.mp3`. **Tone and speaker are both encoded in the filename**, so the corpus needs no reorganisation — the engine globs a flat folder and parses each name.

### 3.1 Access is gated (verified 2026-06-19)

Tone Perfect is **not** an instant download. The flow is: submit a request form → the Tone Perfect team approves → files delivered via MSU **FileDepot**. Lead time is unknown and may take days to weeks.

**Runway:** today is 2026-06-19; Day 0 is 2026-07-15 → **26 days**. The request must go in immediately (pre-Day-0 task, §9.1).

### 3.2 Mirror-now, swap-later workflow (user decision)

To de-risk both the build and the science, audio is handled in two tracks:

| Track | Purpose | Timing |
|---|---|---|
| **Official MSU request** | The real, unmodified corpus used for the actual sprint | Submit now; expected before Day 0 |
| **Build-phase sample** | Just enough real-format files to develop and dry-run every code path | Now, during the build |

**Honest constraint:** a clean public bulk mirror of all 9,840 *real* files does not clearly exist. Public repos are either partial (a handful of demo files) or synthetic "voice-changing" adaptations (files tagged `（fake）` — must be excluded). This is acceptable because the **build phase does not need the full corpus** — a few hundred real-format files exercise load/parse/sample/play/score/log identically to 9,840.

**Swap is free:** because the engine globs a folder and parses filenames, replacing the build sample with the official corpus is a **folder swap with zero code change**. The loader excludes any file whose name contains `fake`.

### 3.3 Decision rule

Submit the official request **today**. **Checkpoint 2026-07-08** (one week before Day 0): if the official corpus has not arrived, escalate (email the team) and proceed Day 0 on the largest legitimate real-format sample available, swapping in the full corpus the moment it lands.

---

## 4. Architecture

Two files in `scripts/` + one config, following the existing `scripts/` convention (`build_decks.py` etc.). **Engine/runner split** so the logic is testable in isolation and extraction-ready for Phase 2.

```
D:\hsk3~5\
├── scripts\
│   ├── hvpt.py            # thin runner: terminal I/O, audio playback, keypress, display
│   ├── hvpt_engine.py     # pure logic: corpus load+parse, trial sampler, scorer, confusion matrix, log formatter
│   └── hvpt_config.json   # stable defaults: paths, trial counts, tone weights, gate thresholds
├── corpus\
│   └── tone_perfect\      # flat dump of *.mp3 (build sample now → official corpus on arrival)
└── logs\
    └── hvpt_sessions.csv  # one row per session (append-only; the Day-0 row is the baseline anchor)
```

**Boundary rule (strict):** `hvpt_engine.py` performs **no I/O** — no `print`, no `input`, no audio, no file writes beyond returning formatted rows. It takes inputs, returns data. `hvpt.py` owns everything the user sees/hears and all disk writes. This keeps the engine unit-testable and the runner thin (~80 lines).

**Dependencies:** Python 3.x (already present), `pygame` (audio playback, one `pip install`, MP3-capable on Windows). Everything else is stdlib (`pathlib`, `csv`, `random`, `argparse`, `collections`, `msvcrt`).

---

## 5. Session protocol

**Phases:** startup → 5 unscored warm-up trials → N scored trials → end report.

**Single scored trial:**

```
① Print trial counter + running accuracy
② Play audio (blocking — next trial cannot begin until the stimulus finishes)
③ Capture one raw keypress via msvcrt — only 1/2/3/4 accepted
   └─ any other key → "→ Press 1 / 2 / 3 / 4", re-prompt the SAME trial (not scored as a miss)
④ Compare response to the tone parsed from the filename
⑤ Immediate feedback (correct tone always shown on a miss), brief pause, next trial
```

**Input:** raw single keypress (`msvcrt.getwch`, Windows) — no Enter. `1/2/3/4` maps directly to Tone 1–4. No undo (correct HVPT protocol).

**In-trial display:**
```
HVPT  Day 03  [focus-T2T3]
Trial 12 / 80  |  Running: 83.3%
  [playing...]
  Press 1 / 2 / 3 / 4 :
```

**Feedback:** `✓ Correct — Tone 2` or `✗ You said 3 | Correct: 2`.

**End report:** overall accuracy, per-tone accuracy, full 4×4 confusion matrix (heard × said), both gate checks with the actual numbers, and the log-write confirmation. (Layout as illustrated in the brainstorm; the engine returns the data, the runner renders it.)

---

## 6. Logging & gates

**`logs/hvpt_sessions.csv`** — append-only, one row per session, readable in Excel:

| Field | Example | Notes |
|---|---|---|
| `date` | 2026-07-15 | |
| `day_number` | 0 | 0–47 |
| `mode` | baseline | |
| `total_trials` | 80 | |
| `accuracy_pct` | 78.8 | |
| `t1_pct`…`t4_pct` | 90.0 … 90.0 | per-tone |
| `t2t3_pct` | 67.5 | the gate metric (T2/T3 accuracy combined) |
| `unlock_gate` | False | ≥95% overall **and** T2↔T3 ≥92% |
| `flyday_gate` | False | ≥97% overall **and** T2↔T3 ≥95% |
| `cm_t1t1`…`cm_t4t4` | 18 … 19 | 16 confusion-matrix cells (heard→said) |

**Baseline anchor:** the Day-0 row (`day_number=0, mode=baseline`) **is** the baseline — the CSV is append-only so it is never overwritten. No separate baseline file. A guard refuses a second `--mode baseline` run if a `day_number=0` baseline row already exists (prevents accidental re-anchoring).

**`tracker.md`** append (one line per session), matching the existing tracker style:
```
| 2026-07-15 | Day 00 | baseline | 78.8% | T1:90 T2:70 T3:65 T4:90 | T2↔T3:67.5% | ✗ |
```

**Gate evaluation** runs in the engine at session end; thresholds live in config (§7) so tuning never touches code.

---

## 7. Config (`scripts/hvpt_config.json`)

```json
{
  "corpus_path": "../corpus/tone_perfect",
  "log_path": "../logs/hvpt_sessions.csv",
  "tracker_path": "../tracker.md",
  "feedback_pause_ms": 500,
  "weights": {
    "default":    {"T1": 0.25, "T2": 0.25, "T3": 0.25, "T4": 0.25},
    "focus-T2T3": {"T1": 0.15, "T2": 0.35, "T3": 0.35, "T4": 0.15},
    "baseline":   {"T1": 0.25, "T2": 0.25, "T3": 0.25, "T4": 0.25},
    "diagnostic": {"T1": 0.25, "T2": 0.25, "T3": 0.25, "T4": 0.25}
  },
  "trial_counts": { "default": 80, "focus-T2T3": 80, "baseline": 80, "diagnostic": 100 },
  "gate": {
    "unlock_overall": 0.95, "unlock_t2t3": 0.92,
    "flyday_overall": 0.97, "flyday_t2t3": 0.95
  }
}
```

**Path resolution:** the relative paths above are resolved against the **script's own location** (`Path(__file__).parent`), not the current working directory — so `python scripts/hvpt.py` works identically whether launched from the repo root or from inside `scripts/`.

**Modes are named config bundles, not separate code paths** — the engine takes `weights`, `trial_count`, and flags as parameters; `--mode` only selects which bundle to load. Default run is `python hvpt.py` (no flag). Four modes:

| Mode | Use |
|---|---|
| *(default)* | Standard daily session |
| `--mode baseline` | Day 0 cold run — equal weights, anchors the CSV |
| `--mode focus-T2T3` | When the confusion matrix shows T2↔T3 leaking |
| `--mode diagnostic` | End-of-week full check — 100 trials, all speakers |

---

## 8. Error handling (plausible cases only)

| Situation | Behaviour |
|---|---|
| `corpus/tone_perfect/` missing or empty | Hard stop **before** any trial; print the exact setup/request instruction |
| A single audio file unreadable | Skip that trial, warn, continue — one bad file never kills the session |
| `pygame` audio init fails | Hard stop; print `pip install pygame` + Windows audio-device hint |
| Second `--mode baseline` after Day 0 | Warn ("baseline already anchored"), refuse to re-anchor, offer a normal run |
| CSV write fails | Print the full results to the terminal **first**, then attempt the write — data is never lost |
| `tracker.md` missing | Warn, skip the tracker append, continue (results already in CSV) |
| Key other than 1/2/3/4 | Inline `→ Press 1 / 2 / 3 / 4`, re-prompt same trial |

---

## 9. Day 0 setup checklist (corrects `day-00.md`)

### 9.1 Pre-Day-0 (do now — the 26-day runway)

```
□ Submit the official Tone Perfect request form at https://tone.lib.msu.edu/ (non-commercial use)
□ Obtain a build-phase real-format sample (enough files across all 4 tones + multiple speakers to dry-run)
□ Build + dry-run hvpt.py / hvpt_engine.py against the sample
□ Checkpoint 2026-07-08: if official corpus not received, escalate; proceed Day 0 on the best legitimate sample
```

### 9.2 Day 0 (15 Jul 2026)

```
□ 1. Place the corpus (official if arrived, else sample) as flat *.mp3 in corpus/tone_perfect/
□ 2. pip install pygame
□ 3. python scripts/hvpt.py --mode baseline   # 5 warm-up + 80 scored; writes the Day-0 anchor row
□ 4. git commit:  day00: hvpt baseline | T1:XX T2:XX T3:XX T4:XX | overall:XX% | T2↔T3:XX%
```

---

## 10. Phase 2 extensibility (flagged extension points)

Per the user's requirement — build so Phase 2 upgrades, not rewrites. Each point is a code comment (`# PHASE2-UPGRADE: …`) at the relevant seam:

- **Package extraction:** `hvpt_engine.py` → `hvpt/engine.py` when adding modes; import path is the only change.
- **Multiple corpora:** `corpus_path` → `corpus_paths: [...]` list (add AISHELL/MagicData as extra speaker pools) — loader already takes a folder, extend to a list.
- **Tone sandhi mode:** add a `sandhi` weights/count bundle + a sandhi trial generator inserted between warm-up and main loop; `run_session()` already takes the trial generator as a parameter.
- **Multi-syllable patterns:** 2–3 syllable tone sequences as a new generator (HSK4+ prosody).
- **Automated production scoring:** new `assess_production(audio, reference)` — record via `sounddevice`, extract F0 via `parselmouth` (Praat), classify + overlay contour. Separate module; perception engine untouched.

---

## 11. Success criteria (verifiable)

1. `hvpt_engine.py` parses `fan3_FV1_MP3.mp3` → `(syllable=fan, tone=3, speaker=FV1)`; excludes `fake` files. *(unit-testable, no audio)*
2. A session of N trials samples talker+syllable independently, interleaves tones randomly, and respects mode weights (verify empirical tone distribution over a large N). *(unit-testable)*
3. Scorer + confusion matrix produce correct counts on a hand-built response set. *(unit-testable)*
4. Gate logic returns the right pass/fail at boundary values (94.9/95.0/97.0; T2↔T3 91.9/92.0/95.0). *(unit-testable)*
5. End-to-end: a real session plays audio, accepts 1/2/3/4, shows immediate feedback, and appends exactly one correct CSV row + one `tracker.md` line. *(manual smoke test)*
6. Re-running `--mode baseline` after a Day-0 row exists is refused. *(testable)*

---

## 12. Out of scope (YAGNI)

GUI/web UI · automated production/pitch scoring (Phase 2) · multi-syllable & sandhi trials (Phase 2) · spaced-repetition scheduling of stimuli (Anki owns SRS) · cloud sync · multi-user · non-Windows input handling (`msvcrt` is Windows; the user is on Windows).

---

## 13. Open items / risks

- **R1 — official corpus timing (highest):** gated delivery may miss Day 0. *Mitigation:* request now + build-sample + 2026-07-08 checkpoint (§3.3).
- **R2 — build-sample sourcing:** no clean full public mirror; must assemble a real-format sample (exclude `fake`). *Mitigation:* a few hundred files suffice for the build; full corpus swaps in free.
- **R3 — `pygame` MP3 playback latency on Windows:** verify during build; if problematic, pre-convert to WAV or use `playsound`/`simpleaudio`. *Engine is format-agnostic (globs `*.mp3`/`*.wav`).*
