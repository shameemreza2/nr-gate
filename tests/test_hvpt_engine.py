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
    assert scores["t2t3_pct"] == pytest.approx(66.7, abs=0.05)


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


def test_baseline_exists_header_only_csv(tmp_path):
    p = tmp_path / "sessions.csv"
    with open(p, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "day_number", "mode"])
        writer.writeheader()
    assert engine.baseline_exists(p) is False
