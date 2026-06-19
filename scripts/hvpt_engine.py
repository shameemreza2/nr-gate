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
