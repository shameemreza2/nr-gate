# tests/test_hvpt_engine.py
import csv
import pytest
import hvpt_engine as engine


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
