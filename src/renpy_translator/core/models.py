"""Core data models for RenPy Translator."""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


DialogueType = Literal["dialogue", "narration"]


@dataclass(slots=True)
class DialogueEntry:
    """A translatable dialogue entry extracted from a Ren'Py script."""

    type: DialogueType
    text: str
    filename: Path
    line_number: int
    speaker: str | None = None
    attributes: tuple[str, ...] = ()