# HVPT Trainer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local terminal-based HVPT Mandarin tone trainer — pure-logic engine + thin I/O runner — that plays Tone Perfect audio, captures 1/2/3/4 keypress, gives immediate feedback, logs sessions to CSV, and computes unlock/fly-day gate checks.

**Architecture:** `hvpt_engine.py` (zero I/O — corpus loading, trial sampling, scoring, gate logic, log formatting) + `hvpt.py` (thin runner — argparse, pygame audio, msvcrt keypress, terminal display, disk writes). Config in `hvpt_config.json`. Engine is unit-testable without audio; runner is smoke-tested with synthetic WAVs.

**Tech Stack:** Python 3, `pygame` (MP3/WAV playback), `msvcrt` (Windows raw keypress), `pytest` (unit tests), stdlib only otherwise (`pathlib`, `csv`, `random`, `argparse`, `re`, `collections`, `wave`).

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `scripts/hvpt_engine.py` | Create | Pure logic: parse, load, sample, score, gate, format |
| `scripts/hvpt.py` | Create | Runner: audio, keypress, display, disk writes |
| `scripts/hvpt_config.json` | Create | Stable defaults: paths, weights, trial counts, gate thresholds |
| `scripts/make_test_corpus.py` | Create | One-shot: generate synthetic WAVs for smoke testing |
| `tests/conftest.py` | Create | Add `scripts/` to `sys.path` for imports |
| `tests/test_hvpt_engine.py` | Create | Unit tests (no audio, no disk I/O beyond tmp_path) |
| `corpus/tone_perfect/` | Create (dir) | Flat MP3/WAV dump; real corpus swaps in here |
| `logs/` | Create (dir) | `hvpt_sessions.csv` written here at runtime |

---

## Task 1: Scaffolding — dirs, config, stubs, conftest

**Files:**
- Create: `scripts/hvpt_config.json`
- Create: `scripts/hvpt_engine.py` (stub)
- Create: `tests/conftest.py`
- Create: `tests/test_hvpt_engine.py` (stub)

- [ ] **Step 1: Create the config file**

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
  "trial_counts": {
    "default": 80,
    "focus-T2T3": 80,
    "baseline": 80,
    "diagnostic": 100
  },
  "gate": {
    "unlock_overall": 0.95,
    "unlock_t2t3": 0.92,
    "flyday_overall": 0.97,
    "flyday_t2t3": 0.95
  }
}
```

Save to: `scripts/hvpt_config.json`

- [ ] **Step 2: Create the engine stub**

```python
# scripts/hvpt_engine.py
import csv
import random
import re
from collections import defaultdict
from pathlib import Path
```

Save to: `scripts/hvpt_engine.py`

- [ ] **Step 3: Create conftest.py (adds scripts/ to sys.path)**

```python
# tests/conftest.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
```

Save to: `tests/conftest.py`

- [ ] **Step 4: Create the test stub**

```python
# tests/test_hvpt_engine.py
import csv
import pytest
import hvpt_engine as engine
```

Save to: `tests/test_hvpt_engine.py`

- [ ] **Step 5: Install pytest and pygame**

```
pip install pytest pygame
```

- [ ] **Step 6: Verify pytest finds the test file**

```
pytest tests/test_hvpt_engine.py -v
```

Expected: `no tests ran` (stub has no tests yet — that is correct).

- [ ] **Step 7: Commit**

```
git add scripts/hvpt_config.json scripts/hvpt_engine.py tests/conftest.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): scaffolding — config, engine stub, test stub"
```

---

## Task 2: parse_filename()

Parses `fan3_FV1_MP3.mp3` → `('fan', 3, 'FV1')`. Returns `None` for unparseable or `fake` files.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def test_parse_filename_valid_mp3():
    assert engine.parse_filename("fan3_FV1_MP3.mp3") == ("fan", 3, "FV1")

def test_parse_filename_valid_wav():
    assert engine.parse_filename("fang1_MV2_MP3.wav") == ("fang", 1, "MV2")

def test_parse_filename_tone4():
    assert engine.parse_filename("ma4_MV3_MP3.mp3") == ("ma", 4, "MV3")

def test_parse_filename_rejects_fake():
    assert engine.parse_filename("fan3_FV1_MP3（fake）.mp3") is None

def test_parse_filename_rejects_non_audio():
    assert engine.parse_filename("notes.txt") is None

def test_parse_filename_rejects_malformed():
    assert engine.parse_filename("random_file.mp3") is None
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_parse_filename_valid_mp3 -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'parse_filename'`

- [ ] **Step 3: Implement parse_filename() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def parse_filename(filename: str):
    """Parse 'fan3_FV1_MP3.mp3' → ('fan', 3, 'FV1'). Returns None if unparseable or fake."""
    if "fake" in filename.lower():
        return None
    m = re.match(r"^([a-zA-Z]+)([1-4])_([A-Z0-9]+)_MP3\.(mp3|wav)$", filename, re.IGNORECASE)
    if not m:
        return None
    return m.group(1).lower(), int(m.group(2)), m.group(3).upper()
```

- [ ] **Step 4: Run all parse_filename tests**

```
pytest tests/test_hvpt_engine.py -k "parse_filename" -v
```

Expected: 6 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): parse_filename — parses Tone Perfect filenames, rejects fakes"
```

---

## Task 3: load_corpus()

Globs `*.mp3` and `*.wav` from a folder, parses each filename, returns a list of dicts.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def test_load_corpus_basic(tmp_path):
    (tmp_path / "fan3_FV1_MP3.mp3").touch()
    (tmp_path / "fang1_MV2_MP3.mp3").touch()
    (tmp_path / "ba2_FV2_MP3.wav").touch()
    corpus = engine.load_corpus(tmp_path)
    assert len(corpus) == 3

def test_load_corpus_excludes_fake(tmp_path):
    (tmp_path / "fan3_FV1_MP3.mp3").touch()
    (tmp_path / "fan3_FV1_MP3（fake）.mp3").touch()  # （fake） in filename
    corpus = engine.load_corpus(tmp_path)
    assert len(corpus) == 1

def test_load_corpus_excludes_non_audio(tmp_path):
    (tmp_path / "fan3_FV1_MP3.mp3").touch()
    (tmp_path / "readme.txt").touch()
    (tmp_path / "data.csv").touch()
    corpus = engine.load_corpus(tmp_path)
    assert len(corpus) == 1

def test_load_corpus_item_shape(tmp_path):
    (tmp_path / "ba4_MV1_MP3.mp3").touch()
    corpus = engine.load_corpus(tmp_path)
    item = corpus[0]
    assert item["syllable"] == "ba"
    assert item["tone"] == 4
    assert item["speaker"] == "MV1"
    assert item["path"].name == "ba4_MV1_MP3.mp3"

def test_load_corpus_empty_dir(tmp_path):
    assert engine.load_corpus(tmp_path) == []

def test_load_corpus_missing_dir():
    from pathlib import Path
    assert engine.load_corpus(Path("/nonexistent/path")) == []
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_load_corpus_basic -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'load_corpus'`

- [ ] **Step 3: Implement load_corpus() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def load_corpus(corpus_path):
    """Return list of {path, syllable, tone, speaker} for all valid audio files."""
    # PHASE2-UPGRADE: accept corpus_paths: list[Path] to merge multiple corpora
    # (e.g. AISHELL, MagicData). Caller passes a list; this function folds them.
    p = Path(corpus_path)
    if not p.exists():
        return []
    result = []
    for f in p.iterdir():
        if f.suffix.lower() not in (".mp3", ".wav"):
            continue
        parsed = parse_filename(f.name)
        if parsed is None:
            continue
        syllable, tone, speaker = parsed
        result.append({"path": f, "syllable": syllable, "tone": tone, "speaker": speaker})
    return result
```

- [ ] **Step 4: Run all load_corpus tests**

```
pytest tests/test_hvpt_engine.py -k "load_corpus" -v
```

Expected: 6 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): load_corpus — globs corpus folder, parses filenames"
```

---

## Task 4: build_trial_set()

Samples `n_trials` items from the corpus respecting tone weights. Tones interleaved randomly (never blocked).

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def _make_corpus(tones_and_speakers):
    """Helper: build fake corpus list without real files."""
    corpus = []
    for tone, speaker in tones_and_speakers:
        corpus.append({
            "path": None,
            "syllable": "ba",
            "tone": tone,
            "speaker": speaker,
        })
    return corpus

def test_build_trial_set_count():
    corpus = _make_corpus([(t, "FV1") for t in [1, 2, 3, 4]] * 10)
    trials = engine.build_trial_set(corpus, 40, {"T1": 0.25, "T2": 0.25, "T3": 0.25, "T4": 0.25})
    assert len(trials) == 40

def test_build_trial_set_weight_distribution():
    corpus = _make_corpus([(t, "FV1") for t in [1, 2, 3, 4]] * 50)
    weights = {"T1": 0.15, "T2": 0.35, "T3": 0.35, "T4": 0.15}
    trials = engine.build_trial_set(corpus, 2000, weights)
    counts = {1: 0, 2: 0, 3: 0, 4: 0}
    for t in trials:
        counts[t["tone"]] += 1
    # Allow ±5% absolute deviation from expected
    assert 200 <= counts[1] <= 400   # ~15% of 2000
    assert 600 <= counts[2] <= 800   # ~35% of 2000
    assert 600 <= counts[3] <= 800   # ~35% of 2000
    assert 200 <= counts[4] <= 400   # ~15% of 2000

def test_build_trial_set_item_keys():
    corpus = _make_corpus([(1, "FV1")])
    trials = engine.build_trial_set(corpus, 1, {"T1": 1.0, "T2": 0.0, "T3": 0.0, "T4": 0.0})
    assert set(trials[0].keys()) == {"path", "syllable", "tone", "speaker"}
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_build_trial_set_count -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'build_trial_set'`

- [ ] **Step 3: Implement build_trial_set() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def build_trial_set(corpus, n_trials, weights):
    """Sample n_trials from corpus by tone weight. Syllable+speaker are jointly random."""
    # PHASE2-UPGRADE: accept trial_generator parameter for sandhi/multi-syllable modes.
    # Default generator is this weighted-random-tone sampler; callers swap in their own.
    by_tone = {1: [], 2: [], 3: [], 4: []}
    for item in corpus:
        by_tone[item["tone"]].append(item)

    tones = [1, 2, 3, 4]
    tone_weights = [weights[f"T{t}"] for t in tones]
    chosen_tones = random.choices(tones, weights=tone_weights, k=n_trials)

    trials = []
    for tone in chosen_tones:
        pool = by_tone.get(tone, [])
        if not pool:
            continue
        trials.append(dict(random.choice(pool)))
    return trials
```

- [ ] **Step 4: Run all build_trial_set tests**

```
pytest tests/test_hvpt_engine.py -k "build_trial_set" -v
```

Expected: 3 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): build_trial_set — weighted random tone sampling, interleaved"
```

---

## Task 5: score_session() + confusion matrix

Takes `[(correct_tone, given_response), ...]` pairs and returns accuracy, per-tone %, T2↔T3 %, and a 4×4 confusion matrix.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def test_score_session_accuracy():
    responses = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 2)]  # 4/5 correct
    scores = engine.score_session(responses)
    assert scores["accuracy_pct"] == 80.0

def test_score_session_per_tone():
    responses = [(2, 2), (3, 3), (3, 2)]  # T2: 1/1=100%, T3: 1/2=50%
    scores = engine.score_session(responses)
    assert scores["t2_pct"] == 100.0
    assert scores["t3_pct"] == 50.0

def test_score_session_t2t3():
    # T2: 1/1 correct, T3: 1/2 correct → combined 2/3 = 66.7%
    responses = [(2, 2), (3, 3), (3, 2)]
    scores = engine.score_session(responses)
    assert scores["t2t3_pct"] == 66.7

def test_score_session_confusion_matrix():
    responses = [(3, 2)]  # heard T3, said T2
    scores = engine.score_session(responses)
    assert scores["cm_t3t2"] == 1
    assert scores["cm_t3t3"] == 0

def test_score_session_all_correct():
    responses = [(t, t) for t in [1, 2, 3, 4] * 5]
    scores = engine.score_session(responses)
    assert scores["accuracy_pct"] == 100.0
    assert scores["t2t3_pct"] == 100.0
    for heard in range(1, 5):
        for said in range(1, 5):
            expected = 5 if heard == said else 0
            assert scores[f"cm_t{heard}t{said}"] == expected

def test_score_session_keys():
    responses = [(1, 1)]
    scores = engine.score_session(responses)
    required = {"accuracy_pct", "t1_pct", "t2_pct", "t3_pct", "t4_pct", "t2t3_pct"}
    for heard in range(1, 5):
        for said in range(1, 5):
            required.add(f"cm_t{heard}t{said}")
    assert required.issubset(scores.keys())
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_score_session_accuracy -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'score_session'`

- [ ] **Step 3: Implement score_session() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def score_session(responses):
    """
    responses: list of (correct_tone, given_response) — both 1-indexed int.
    Returns dict with accuracy_pct, t1..t4_pct, t2t3_pct, cm_tXtY for all X,Y in 1..4.
    """
    confusion = defaultdict(int)
    per_correct = {1: 0, 2: 0, 3: 0, 4: 0}
    per_total   = {1: 0, 2: 0, 3: 0, 4: 0}

    for correct, given in responses:
        confusion[(correct, given)] += 1
        per_total[correct] += 1
        if correct == given:
            per_correct[correct] += 1

    total = len(responses)
    total_correct = sum(per_correct.values())

    def pct(num, den):
        return round(100 * num / den, 1) if den else 0.0

    t2t3_correct = per_correct[2] + per_correct[3]
    t2t3_total   = per_total[2]   + per_total[3]

    scores = {
        "accuracy_pct": pct(total_correct, total),
        "t1_pct": pct(per_correct[1], per_total[1]),
        "t2_pct": pct(per_correct[2], per_total[2]),
        "t3_pct": pct(per_correct[3], per_total[3]),
        "t4_pct": pct(per_correct[4], per_total[4]),
        "t2t3_pct": pct(t2t3_correct, t2t3_total),
    }
    for heard in range(1, 5):
        for said in range(1, 5):
            scores[f"cm_t{heard}t{said}"] = confusion.get((heard, said), 0)
    return scores
```

- [ ] **Step 4: Run all score_session tests**

```
pytest tests/test_hvpt_engine.py -k "score_session" -v
```

Expected: 6 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): score_session — accuracy, per-tone %, T2↔T3 %, confusion matrix"
```

---

## Task 6: check_gates()

Returns `{unlock_gate: bool, flyday_gate: bool}`. Verified at boundary values.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
GATE_CFG = {
    "unlock_overall": 0.95, "unlock_t2t3": 0.92,
    "flyday_overall": 0.97, "flyday_t2t3": 0.95,
}

def test_check_gates_below_unlock():
    g = engine.check_gates(94.9, 92.0, GATE_CFG)
    assert g["unlock_gate"] is False
    assert g["flyday_gate"] is False

def test_check_gates_at_unlock_threshold():
    g = engine.check_gates(95.0, 92.0, GATE_CFG)
    assert g["unlock_gate"] is True
    assert g["flyday_gate"] is False

def test_check_gates_t2t3_below_unlock():
    g = engine.check_gates(95.0, 91.9, GATE_CFG)
    assert g["unlock_gate"] is False

def test_check_gates_at_flyday_threshold():
    g = engine.check_gates(97.0, 95.0, GATE_CFG)
    assert g["unlock_gate"] is True
    assert g["flyday_gate"] is True

def test_check_gates_flyday_t2t3_below():
    g = engine.check_gates(97.0, 94.9, GATE_CFG)
    assert g["flyday_gate"] is False
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_check_gates_below_unlock -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'check_gates'`

- [ ] **Step 3: Implement check_gates() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def check_gates(accuracy_pct, t2t3_pct, gate_config):
    """Return {unlock_gate, flyday_gate} booleans. Thresholds in gate_config are fractions (0.95)."""
    unlock = (accuracy_pct >= gate_config["unlock_overall"] * 100 and
              t2t3_pct   >= gate_config["unlock_t2t3"]   * 100)
    flyday = (accuracy_pct >= gate_config["flyday_overall"] * 100 and
              t2t3_pct   >= gate_config["flyday_t2t3"]   * 100)
    return {"unlock_gate": unlock, "flyday_gate": flyday}
```

- [ ] **Step 4: Run all check_gates tests**

```
pytest tests/test_hvpt_engine.py -k "check_gates" -v
```

Expected: 5 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): check_gates — unlock + fly-day gate logic, boundary-tested"
```

---

## Task 7: format_csv_row() + format_tracker_line()

Pure formatters — return data structures for the runner to write; no disk access here.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def _sample_scores():
    return {
        "accuracy_pct": 78.8,
        "t1_pct": 90.0, "t2_pct": 70.0, "t3_pct": 65.0, "t4_pct": 90.0,
        "t2t3_pct": 67.5,
        **{f"cm_t{h}t{s}": (5 if h == s else 0) for h in range(1, 5) for s in range(1, 5)},
    }

def _sample_gates():
    return {"unlock_gate": False, "flyday_gate": False}

def test_format_csv_row_required_fields():
    row = engine.format_csv_row("2026-07-15", 0, "baseline", 80, _sample_scores(), _sample_gates())
    assert row["date"] == "2026-07-15"
    assert row["day_number"] == 0
    assert row["mode"] == "baseline"
    assert row["total_trials"] == 80
    assert row["accuracy_pct"] == 78.8
    assert row["t2t3_pct"] == 67.5
    assert row["unlock_gate"] is False
    assert row["cm_t3t2"] == 0

def test_format_csv_row_has_all_confusion_cells():
    row = engine.format_csv_row("2026-07-15", 0, "baseline", 80, _sample_scores(), _sample_gates())
    for heard in range(1, 5):
        for said in range(1, 5):
            assert f"cm_t{heard}t{said}" in row

def test_format_tracker_line_format():
    line = engine.format_tracker_line("2026-07-15", 0, "baseline", _sample_scores(), _sample_gates())
    assert "| 2026-07-15 |" in line
    assert "Day 00" in line
    assert "baseline" in line
    assert "78.8%" in line
    assert "T2↔T3:67.5%" in line
    assert line.startswith("|")
    assert line.endswith("|")

def test_format_tracker_line_gate_fail_symbol():
    line = engine.format_tracker_line("2026-07-15", 0, "baseline", _sample_scores(), _sample_gates())
    assert "✗" in line

def test_format_tracker_line_gate_pass_symbol():
    gates = {"unlock_gate": True, "flyday_gate": False}
    line = engine.format_tracker_line("2026-07-15", 21, "default", _sample_scores(), gates)
    assert "✓" in line
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_format_csv_row_required_fields -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'format_csv_row'`

- [ ] **Step 3: Implement format_csv_row() and format_tracker_line() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def format_csv_row(date_str, day_number, mode, n_trials, scores, gates):
    """Return a flat dict with all CSV columns. Runner writes this to disk."""
    row = {
        "date": date_str,
        "day_number": day_number,
        "mode": mode,
        "total_trials": n_trials,
        "accuracy_pct": scores["accuracy_pct"],
        "t1_pct": scores["t1_pct"],
        "t2_pct": scores["t2_pct"],
        "t3_pct": scores["t3_pct"],
        "t4_pct": scores["t4_pct"],
        "t2t3_pct": scores["t2t3_pct"],
        "unlock_gate": gates["unlock_gate"],
        "flyday_gate": gates["flyday_gate"],
    }
    for heard in range(1, 5):
        for said in range(1, 5):
            row[f"cm_t{heard}t{said}"] = scores[f"cm_t{heard}t{said}"]
    return row


def format_tracker_line(date_str, day_number, mode, scores, gates):
    """Return the tracker.md pipe-table row string. Runner appends this to tracker.md."""
    gate_sym = "✓" if gates["unlock_gate"] else "✗"
    return (
        f"| {date_str} | Day {day_number:02d} | {mode} | {scores['accuracy_pct']}% | "
        f"T1:{scores['t1_pct']} T2:{scores['t2_pct']} "
        f"T3:{scores['t3_pct']} T4:{scores['t4_pct']} | "
        f"T2↔T3:{scores['t2t3_pct']}% | {gate_sym} |"
    )
```

- [ ] **Step 4: Run all format tests**

```
pytest tests/test_hvpt_engine.py -k "format" -v
```

Expected: 5 tests PASSED.

- [ ] **Step 5: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): format_csv_row + format_tracker_line — pure formatters, no I/O"
```

---

## Task 8: baseline_exists()

Checks the CSV for an existing `day_number=0, mode=baseline` row. Guards against re-anchoring.

**Files:**
- Modify: `tests/test_hvpt_engine.py`
- Modify: `scripts/hvpt_engine.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_hvpt_engine.py`:

```python
def _write_csv(path, rows):
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

def test_baseline_exists_no_csv(tmp_path):
    assert engine.baseline_exists(tmp_path / "missing.csv") is False

def test_baseline_exists_no_baseline_row(tmp_path):
    p = tmp_path / "sessions.csv"
    _write_csv(p, [{"date": "2026-07-20", "day_number": "5", "mode": "default", "accuracy_pct": "85.0"}])
    assert engine.baseline_exists(p) is False

def test_baseline_exists_true(tmp_path):
    p = tmp_path / "sessions.csv"
    _write_csv(p, [{"date": "2026-07-15", "day_number": "0", "mode": "baseline", "accuracy_pct": "78.8"}])
    assert engine.baseline_exists(p) is True

def test_baseline_exists_ignores_day0_non_baseline(tmp_path):
    p = tmp_path / "sessions.csv"
    _write_csv(p, [{"date": "2026-07-15", "day_number": "0", "mode": "diagnostic", "accuracy_pct": "78.8"}])
    assert engine.baseline_exists(p) is False
```

- [ ] **Step 2: Run to verify they fail**

```
pytest tests/test_hvpt_engine.py::test_baseline_exists_no_csv -v
```

Expected: `FAILED` — `AttributeError: module 'hvpt_engine' has no attribute 'baseline_exists'`

- [ ] **Step 3: Implement baseline_exists() in hvpt_engine.py**

Append to `scripts/hvpt_engine.py`:

```python
def baseline_exists(log_path):
    """Return True if the CSV already contains a day_number=0 baseline row."""
    p = Path(log_path)
    if not p.exists():
        return False
    with open(p, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("day_number") == "0" and row.get("mode") == "baseline":
                return True
    return False
```

- [ ] **Step 4: Run all baseline_exists tests**

```
pytest tests/test_hvpt_engine.py -k "baseline_exists" -v
```

Expected: 4 tests PASSED.

- [ ] **Step 5: Run the full test suite to confirm nothing regressed**

```
pytest tests/test_hvpt_engine.py -v
```

Expected: all 35 tests PASSED.

- [ ] **Step 6: Commit**

```
git add scripts/hvpt_engine.py tests/test_hvpt_engine.py
git commit -m "feat(hvpt): baseline_exists — guards against re-anchoring Day-0 baseline"
```

---

## Task 9: Test corpus (synthetic WAVs for smoke testing)

Creates a set of tiny playable WAVs named in Tone Perfect format. Used for the smoke test; replaced by the official corpus on arrival.

**Files:**
- Create: `scripts/make_test_corpus.py`

- [ ] **Step 1: Create make_test_corpus.py**

```python
# scripts/make_test_corpus.py
"""
One-shot script: generate tiny synthetic WAV files named in Tone Perfect format.
Used as the build-phase corpus sample until the official MSU corpus arrives.
Run from the repo root: python scripts/make_test_corpus.py
"""
import math
import struct
import wave
from pathlib import Path

SAMPLE_RATE = 22050
DURATION_MS = 800  # 0.8 s — long enough for pygame to play before keypress

# Cover all 4 tones, 3 syllables, 3 speakers (36 files — enough to exercise every code path)
SYLLABLES = ["ba", "ma", "fan"]
TONES = [1, 2, 3, 4]
SPEAKERS = ["FV1", "FV2", "MV1"]

# Distinct frequencies per tone so they're not all identical (helps manual QA)
TONE_FREQ = {1: 300, 2: 400, 3: 250, 4: 350}


def make_wav(path, frequency):
    n = int(SAMPLE_RATE * DURATION_MS / 1000)
    with wave.open(str(path), "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        for i in range(n):
            v = int(32767 * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE))
            f.writeframes(struct.pack("<h", v))


def main():
    out = Path(__file__).parent.parent / "corpus" / "tone_perfect"
    out.mkdir(parents=True, exist_ok=True)

    created = 0
    for syllable in SYLLABLES:
        for tone in TONES:
            for speaker in SPEAKERS:
                fname = f"{syllable}{tone}_{speaker}_MP3.wav"
                fpath = out / fname
                make_wav(fpath, TONE_FREQ[tone])
                created += 1

    print(f"Created {created} synthetic WAV files in {out}")
    print("These are build-phase placeholders. Swap in the official Tone Perfect MP3s on arrival.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

```
python scripts/make_test_corpus.py
```

Expected output:
```
Created 36 synthetic WAV files in D:\hsk3~5\corpus\tone_perfect
These are build-phase placeholders. Swap in the official Tone Perfect MP3s on arrival.
```

- [ ] **Step 3: Verify the corpus loads correctly**

Open a Python shell from the repo root:

```python
import sys; sys.path.insert(0, "scripts")
import hvpt_engine as e
from pathlib import Path
corpus = e.load_corpus(Path("corpus/tone_perfect"))
print(len(corpus))          # expect 36
print(corpus[0])            # expect dict with path/syllable/tone/speaker
```

- [ ] **Step 4: Commit (corpus files excluded — add to .gitignore)**

Add `corpus/tone_perfect/` to `.gitignore` (audio files don't belong in git):

```
# .gitignore — append:
corpus/tone_perfect/
logs/hvpt_sessions.csv
```

```
git add .gitignore scripts/make_test_corpus.py
git commit -m "feat(hvpt): make_test_corpus — synthetic WAVs for build-phase smoke test"
```

---

## Task 10: hvpt.py runner

The thin runner: argparse, config loading, corpus validation, baseline guard, pygame audio, msvcrt keypress, display, end report, CSV append, tracker append.

**Files:**
- Create: `scripts/hvpt.py`

- [ ] **Step 1: Create hvpt.py**

```python
# scripts/hvpt.py
"""HVPT Mandarin tone trainer — runner. See docs/specs/2026-06-19-hvpt-mandarin-design.md"""
import argparse
import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

import pygame

import hvpt_engine as engine

SCRIPT_DIR = Path(__file__).parent
MODES = ["default", "baseline", "focus-T2T3", "diagnostic"]


def load_config():
    with open(SCRIPT_DIR / "hvpt_config.json", encoding="utf-8") as f:
        return json.load(f)


def resolve(cfg, key):
    """Resolve a config path relative to the script's own directory."""
    return (SCRIPT_DIR / cfg[key]).resolve()


def get_keypress():
    """Block until user presses 1/2/3/4. Re-prompt on any other key."""
    import msvcrt
    while True:
        ch = msvcrt.getwch()
        if ch in ("1", "2", "3", "4"):
            return int(ch)
        print("\r  → Press 1 / 2 / 3 / 4 : ", end="", flush=True)


def play_audio(path):
    """Play a single audio file, blocking until playback finishes."""
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
    except Exception as e:
        print(f"\n  [warn] could not play {path.name}: {e} — skipping")


def run_trials(trials, mode, day_number, feedback_pause_ms, scored=True):
    """Run a block of trials. Returns list of (correct_tone, given) pairs (empty if unscored)."""
    responses = []
    n = len(trials)
    correct_so_far = 0
    total_so_far = 0

    for i, trial in enumerate(trials, 1):
        running = f"{100*correct_so_far/total_so_far:.1f}%" if total_so_far else "–"
        print(f"\n{'─'*45}")
        if scored:
            print(f"HVPT  Day {day_number:02d}  [{mode}]")
            print(f"Trial {i} / {n}  |  Running: {running}")
        else:
            print(f"Warm-up {i} / {n}  (unscored — calibrate your ear)")
        print("─" * 45)
        print("  [playing...]", flush=True)
        play_audio(trial["path"])
        print("  Press 1 / 2 / 3 / 4 : ", end="", flush=True)
        given = get_keypress()
        correct = trial["tone"]
        if given == correct:
            print(f"\r  ✓ Correct — Tone {correct}                    ")
            if scored:
                correct_so_far += 1
        else:
            print(f"\r  ✗ You said {given}  |  Correct: {correct}          ")
        if scored:
            total_so_far += 1
            responses.append((correct, given))
        time.sleep(feedback_pause_ms / 1000)

    return responses


def print_end_report(scores, gates, n_trials, mode, day_number, gate_cfg):
    print(f"\n{'─'*45}")
    print(f"SESSION COMPLETE — {n_trials} trials — Day {day_number:02d}")
    print("─" * 45)
    print(f"Overall accuracy:    {scores['accuracy_pct']}%")
    print("\nPer-tone:")
    print(f"  T1 (─ high-level):  {scores['t1_pct']}%")
    print(f"  T2 (╱ rising):      {scores['t2_pct']}%")
    print(f"  T3 (∨ dipping):     {scores['t3_pct']}%")
    print(f"  T4 (╲ falling):     {scores['t4_pct']}%")
    print("\nConfusion matrix (heard → said):")
    print("           Said →   T1    T2    T3    T4")
    for heard in range(1, 5):
        cells = "  ".join(f"{scores[f'cm_t{heard}t{said}']:4d}" for said in range(1, 5))
        print(f"  Heard T{heard}          {cells}")
    u_sym = "✓" if gates["unlock_gate"] else "✗"
    f_sym = "✓" if gates["flyday_gate"] else "✗"
    u_oa = gate_cfg["unlock_overall"] * 100
    u_t  = gate_cfg["unlock_t2t3"]   * 100
    f_oa = gate_cfg["flyday_overall"] * 100
    f_t  = gate_cfg["flyday_t2t3"]   * 100
    print("\nGate checks:")
    print(f"  Unlock  (≥{u_oa:.0f}% + T2↔T3 ≥{u_t:.0f}%):  {u_sym}  "
          f"[{scores['accuracy_pct']}% / {scores['t2t3_pct']}%]")
    print(f"  Fly-day (≥{f_oa:.0f}% + T2↔T3 ≥{f_t:.0f}%):  {f_sym}  "
          f"[{scores['accuracy_pct']}% / {scores['t2t3_pct']}%]")
    print("─" * 45)


def append_csv(log_path, row):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(row.keys())
    write_header = not log_path.exists()
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def append_tracker(tracker_path, line):
    if not tracker_path.exists():
        print(f"  [warn] tracker.md not found at {tracker_path} — skipping")
        return
    with open(tracker_path, "a", encoding="utf-8") as f:
        f.write("\n" + line)


def main():
    parser = argparse.ArgumentParser(description="HVPT Mandarin tone trainer")
    parser.add_argument("--mode", default="default", choices=MODES)
    parser.add_argument("--day", type=int, required=True,
                        help="Sprint day number (0–47)")
    args = parser.parse_args()

    cfg = load_config()
    mode = args.mode
    day_number = args.day

    corpus_path  = resolve(cfg, "corpus_path")
    log_path     = resolve(cfg, "log_path")
    tracker_path = resolve(cfg, "tracker_path")

    # Corpus check — hard stop before any trial
    corpus = engine.load_corpus(corpus_path)
    if not corpus:
        print(f"ERROR: No audio files found in {corpus_path}")
        print("  Place Tone Perfect MP3/WAV files there (e.g. fan3_FV1_MP3.mp3).")
        print("  Or run: python scripts/make_test_corpus.py")
        print("  Official corpus: https://tone.lib.msu.edu/")
        sys.exit(1)

    # Baseline guard
    if mode == "baseline" and engine.baseline_exists(log_path):
        print("ERROR: baseline already anchored (day_number=0 row exists).")
        print("  Re-anchoring would destroy your Day-0 reference. Use --mode default instead.")
        sys.exit(0)

    # pygame init — hard stop on failure
    try:
        pygame.mixer.init()
    except Exception as e:
        print(f"ERROR: pygame audio init failed: {e}")
        print("  Run: pip install pygame")
        print("  Also verify Windows audio output is enabled.")
        sys.exit(1)

    weights   = cfg["weights"][mode]
    n_trials  = cfg["trial_counts"][mode]
    pause_ms  = cfg["feedback_pause_ms"]
    gate_cfg  = cfg["gate"]

    warmup_trials = engine.build_trial_set(corpus, 5, weights)
    main_trials   = engine.build_trial_set(corpus, n_trials, weights)

    print(f"\nHVPT — Day {day_number:02d} — {mode}")
    print(f"Corpus: {len(corpus)} files  |  {n_trials} scored trials + 5 warm-up")
    print("─" * 45)
    print("\n  [5 warm-up trials — unscored]")

    run_trials(warmup_trials, mode, day_number, pause_ms, scored=False)
    responses = run_trials(main_trials, mode, day_number, pause_ms, scored=True)

    scores = engine.score_session(responses)
    gates  = engine.check_gates(scores["accuracy_pct"], scores["t2t3_pct"], gate_cfg)

    # Print end report BEFORE any disk writes — data is never lost
    print_end_report(scores, gates, len(responses), mode, day_number, gate_cfg)

    today   = date.today().isoformat()
    csv_row = engine.format_csv_row(today, day_number, mode, len(responses), scores, gates)
    t_line  = engine.format_tracker_line(today, day_number, mode, scores, gates)

    try:
        append_csv(log_path, csv_row)
        print(f"  Logged → {log_path}")
    except Exception as e:
        print(f"  [warn] CSV write failed: {e}")

    try:
        append_tracker(tracker_path, t_line)
        print("  tracker.md updated")
    except Exception as e:
        print(f"  [warn] tracker append failed: {e}")

    pygame.mixer.quit()


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```
git add scripts/hvpt.py
git commit -m "feat(hvpt): runner — argparse, pygame audio, msvcrt keypress, CSV + tracker writes"
```

---

## Task 11: End-to-end smoke test

Run a full baseline session with synthetic WAVs. Verify CSV row and tracker.md append.

**Files:** no file changes — this is a manual verification step.

- [ ] **Step 1: Confirm corpus exists**

```
python scripts/make_test_corpus.py
```

Expected: `Created 36 synthetic WAV files...` (or "already exist" — no error either way).

- [ ] **Step 2: Confirm no existing baseline row**

```python
python -c "
import sys; sys.path.insert(0, 'scripts')
import hvpt_engine as e
from pathlib import Path
print(e.baseline_exists(Path('logs/hvpt_sessions.csv')))
"
```

Expected: `False`

- [ ] **Step 3: Run the baseline session**

```
python scripts/hvpt.py --mode baseline --day 0
```

Work through all 5 warm-up + 80 scored trials. Press 1/2/3/4 for each. At the end you should see the full end report with per-tone %, confusion matrix, and gate checks.

- [ ] **Step 4: Verify the CSV row was written**

```python
python -c "
import csv
with open('logs/hvpt_sessions.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
print(f'{len(rows)} row(s) in CSV')
print(rows[-1])
"
```

Expected: 1 row, with `day_number=0`, `mode=baseline`, and all 20 confusion-matrix cell columns present.

- [ ] **Step 5: Verify the baseline guard fires**

```
python scripts/hvpt.py --mode baseline --day 0
```

Expected: `ERROR: baseline already anchored...` then exit. No second row added to the CSV.

- [ ] **Step 6: Verify tracker.md was updated**

```python
python -c "
with open('tracker.md', encoding='utf-8') as f:
    print(f.read()[-300:])
"
```

Expected: the last few lines include a pipe-table row like:
```
| 2026-07-15 | Day 00 | baseline | XX.X% | T1:XX T2:XX T3:XX T4:XX | T2↔T3:XX% | ✗ |
```

- [ ] **Step 7: Run a standard session (non-baseline) to confirm daily workflow**

```
python scripts/hvpt.py --mode default --day 0
```

Complete the session. Confirm a second CSV row is appended with `mode=default`.

- [ ] **Step 8: Commit the green state**

```
git add logs/ -N 2>/dev/null; true  # just ensure logs/ is tracked as dir
git commit -m "test(hvpt): smoke test green — baseline guard, CSV, tracker verified"
```

---

## Self-Review Against Spec

**Spec §11 success criteria — all covered:**

| Criterion | Task |
|---|---|
| `parse_filename` parses correctly, excludes fakes | Task 2 |
| Trial sampling: independent, interleaved, respects weights | Task 4 |
| Scorer + confusion matrix correct on hand-built set | Task 5 |
| Gate logic correct at boundary values | Task 6 |
| End-to-end: audio plays, keypress works, CSV + tracker appended | Task 11 |
| Re-running `--mode baseline` after Day-0 row is refused | Task 11 Step 5 |

**Spec §8 error handling — all in runner (Task 10):**
- Corpus missing → hard stop with setup instruction ✓
- Single bad file → skip + warn (play_audio catches exception) ✓
- pygame init fails → hard stop + fix hint ✓
- Second baseline run → refuse + message ✓
- CSV write fails → report already printed, warn ✓
- tracker.md missing → warn, skip ✓
- Invalid keypress → re-prompt same trial ✓

**Phase 2 seams flagged in-code (spec §10):**
- `load_corpus` → PHASE2-UPGRADE comment for `corpus_paths` list ✓
- `build_trial_set` → PHASE2-UPGRADE comment for `trial_generator` param ✓
- Package extraction path noted in engine stub imports ✓
