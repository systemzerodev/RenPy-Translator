"""Project-wide dialogue extraction for RenPy Translator."""

from pathlib import Path

from renpy_translator.core.models import DialogueEntry
from renpy_translator.core.parser import RenPyParser
from renpy_translator.core.scanner import ScriptScanner


class ProjectExtractor:
    """Scan a Ren'Py project and extract supported dialogue entries."""

    def __init__(self, project_path: Path) -> None:
        self.project_path = project_path
        self.scanner = ScriptScanner(project_path)
        self.parser = RenPyParser()

    def extract(
        self,
    ) -> tuple[list[Path], list[DialogueEntry]]:
        """Return discovered scripts and extracted dialogue entries."""

        script_files = self.scanner.scan()
        dialogues: list[DialogueEntry] = []

        for script_file in script_files:
            dialogues.extend(
                self.parser.parse_file(script_file)
            )

        return script_files, dialogues