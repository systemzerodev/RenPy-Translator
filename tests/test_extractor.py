"""Tests for project-wide dialogue extraction."""

from pathlib import Path

from renpy_translator.core.extractor import ProjectExtractor


FIXTURE_DIRECTORY = (
    Path(__file__).parent
    / "fixtures"
)


def test_extractor_scans_and_parses_project() -> None:
    extractor = ProjectExtractor(
        FIXTURE_DIRECTORY
    )

    script_files, dialogues = extractor.extract()

    assert len(script_files) == 1
    assert script_files[0].name == "sample_script.rpy"

    assert len(dialogues) == 5

    assert dialogues[0].speaker == "e"
    assert dialogues[0].text == "Hello there."

    assert dialogues[1].type == "narration"
    assert dialogues[1].text == "This is narration."