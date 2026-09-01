"""Tests for the Ren'Py dialogue parser."""

from pathlib import Path

from renpy_translator.core.parser import RenPyParser


FIXTURE_PATH = (
    Path(__file__).parent
    / "fixtures"
    / "sample_script.rpy"
)


def test_parser_extracts_supported_dialogue() -> None:
    parser = RenPyParser()

    entries = parser.parse_file(
        FIXTURE_PATH
    )

    assert len(entries) == 5

    assert entries[0].type == "dialogue"
    assert entries[0].speaker == "e"
    assert entries[0].text == "Hello there."

    assert entries[1].type == "narration"
    assert entries[1].speaker is None
    assert entries[1].text == "This is narration."

    assert entries[2].speaker == "e"
    assert entries[2].attributes == ("happy",)
    assert entries[2].text == "Nice to meet you."

    assert entries[3].text == "Hello [player_name]."

    assert entries[4].speaker == "m"
    assert entries[4].text == "{i}Welcome to the game.{/i}"


def test_parser_preserves_source_location() -> None:
    parser = RenPyParser()

    entries = parser.parse_file(
        FIXTURE_PATH
    )

    first_entry = entries[0]

    assert first_entry.filename == FIXTURE_PATH
    assert first_entry.line_number > 0