import pytest
import builtins
phrase = input("Set a phrase: ")

def test_check_phrase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mark")
    assert phrase == "Mark", f"Wrong phrase length"

test_check_phrase(phrase)