"""Ren'Py project script scanner."""

from pathlib import Path


class ScriptScanner:
    """Find Ren'Py script files inside a project."""

    IGNORED_DIRECTORIES = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
    }

    def __init__(self, project_path: Path) -> None:
        self.project_path = project_path

    @property
    def script_root(self) -> Path:
        """
        Return the directory that should contain Ren'Py scripts.

        A normal Ren'Py project usually contains a `game` directory.
        If the user selects the `game` directory directly, use it as-is.
        """

        game_directory = self.project_path / "game"

        if game_directory.is_dir():
            return game_directory

        return self.project_path

    def scan(self) -> list[Path]:
        """Return all source .rpy files in the project."""

        script_files: list[Path] = []

        for path in self.script_root.rglob("*.rpy"):
            if not path.is_file():
                continue

            relative_parts = path.relative_to(self.script_root).parts

            if any(
                part in self.IGNORED_DIRECTORIES
                for part in relative_parts
            ):
                continue

            # Existing Ren'Py translation files are not source scripts.
            if "tl" in relative_parts:
                continue

            script_files.append(path)

        return sorted(
            script_files,
            key=lambda path: str(path).lower(),
        )