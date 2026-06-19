# scripts/hvpt_engine.py
import csv
import random
import re
from collections import defaultdict
from pathlib import Path


def parse_filename(filename: str):
    """Parse 'fan3_FV1_MP3.mp3' → ('fan', 3, 'FV1'). Returns None if unparseable or fake."""
    if "fake" in filename.lower():
        return None
    m = re.match(r"^([a-zA-Z]+)([1-4])_([A-Z0-9]+)_MP3\.(mp3|wav)$", filename, re.IGNORECASE)
    if not m:
        return None
    return m.group(1).lower(), int(m.group(2)), m.group(3).upper()


def load_corpus(corpus_path):
    """Return sorted list of {path, syllable, tone, speaker} for all valid audio files.
    Flat directory only — subdirectories are not searched. Raises OSError if path
    exists but is unreadable."""
    # PHASE2-UPGRADE: accept corpus_paths: list[Path] to merge multiple corpora
    # (e.g. AISHELL, MagicData). Caller passes a list; this function folds them.
    p = Path(corpus_path)
    if not p.exists():
        return []
    result = []
    for f in sorted(p.iterdir()):
        if f.suffix.lower() not in (".mp3", ".wav"):
            continue
        parsed = parse_filename(f.name)
        if parsed is None:
            continue
        syllable, tone, speaker = parsed
        result.append({"path": f, "syllable": syllable, "tone": tone, "speaker": speaker})
    return result


def build_trial_set(corpus, n_trials, weights):
    """Sample n_trials from corpus by tone weight. Syllable+speaker are jointly random.

    Returns fewer than n_trials if a weighted tone has no items in the corpus — the
    runner checks corpus completeness before calling this. Tones are drawn by
    random.choices so short runs of the same tone are possible (acceptable per HVPT).
    """
    # PHASE2-UPGRADE: accept trial_generator parameter for sandhi/multi-syllable modes.
    # Default generator is this weighted-random-tone sampler; callers swap in their own.
    by_tone = {1: [], 2: [], 3: [], 4: []}
    for item in corpus:
        # Silently ignore tones outside 1-4 (e.g. neutral tone 0 in real corpora)
        if item["tone"] in by_tone:
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
            # .get() preferred over direct indexing: defaultdict would insert missing keys on access
            scores[f"cm_t{heard}t{said}"] = confusion.get((heard, said), 0)
    return scores


def check_gates(accuracy_pct, t2t3_pct, gate_config):
    """Return {unlock_gate, flyday_gate} booleans. Thresholds in gate_config are fractions (0.95).
    Config fractions must multiply cleanly to integers (0.95→95.0, 0.92→92.0, 0.97→97.0);
    fractions like 0.83→83.00000000000001 would cause off-by-epsilon errors at exact boundaries.
    """
    unlock = (accuracy_pct >= gate_config["unlock_overall"] * 100 and
              t2t3_pct   >= gate_config["unlock_t2t3"]   * 100)
    # flyday requires unlock first (structurally enforces flyday ⟹ unlock)
    flyday = unlock and (accuracy_pct >= gate_config["flyday_overall"] * 100 and
                         t2t3_pct   >= gate_config["flyday_t2t3"]   * 100)
    return {"unlock_gate": unlock, "flyday_gate": flyday}


def format_csv_row(date_str, day_number, mode, n_trials, scores, gates):
    """Return a flat dict with all CSV columns. Runner writes this to disk.
    Column order matches insertion order; runner must pass fieldnames=list(row.keys())
    to csv.DictWriter to preserve it."""
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
        f"T1:{scores['t1_pct']:.0f} T2:{scores['t2_pct']:.0f} "
        f"T3:{scores['t3_pct']:.0f} T4:{scores['t4_pct']:.0f} | "
        f"T2↔T3:{scores['t2t3_pct']}% | {gate_sym} |"
    )


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
