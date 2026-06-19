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
