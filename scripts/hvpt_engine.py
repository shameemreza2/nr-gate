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
