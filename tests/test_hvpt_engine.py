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
