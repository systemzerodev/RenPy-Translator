"""Parser for extracting translatable text from Ren'Py source files."""

import ast
import re
from pathlib import Path

from renpy_translator.core.models import DialogueEntry


_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z_]\w*$")

_IGNORED_PREFIXES = {
    "call",
    "default",
    "define",
    "elif",
    "else",
    "for",
    "if",
    "image",
    "init",
    "jump",
    "label",
    "menu",
    "pause",
    "play",
    "python",
    "queue",
    "return",
    "scene",
    "screen",
    "show",
    "stop",
    "style",
    "transform",
    "translate",
    "voice",
    "while",
    "window",
}


class RenPyParser:
    """Extract supported dialogue statements from Ren'Py source files."""

    def parse_file(self, file_path: Path) -> list[DialogueEntry]:
        """Parse a Ren'Py file and return supported dialogue entries."""

        entries: list[DialogueEntry] = []

        with file_path.open(
            "r",
            encoding="utf-8-sig",
        ) as script_file:
            for line_number, source_line in enumerate(
                script_file,
                start=1,
            ):
                entry = self.parse_line(
                    source_line=source_line,
                    file_path=file_path,
                    line_number=line_number,
                )

                if entry is not None:
                    entries.append(entry)

        return entries

    def parse_line(
        self,
        source_line: str,
        file_path: Path,
        line_number: int,
    ) -> DialogueEntry | None:
        """Parse one Ren'Py source line."""

        statement = source_line.strip()

        if not statement:
            return None

        if statement.startswith("#"):
            return None

        quoted_string = self._extract_quoted_string(
            statement
        )

        if quoted_string is None:
            return None

        prefix, string_literal, suffix = quoted_string

        # Stage 1 only accepts a clean say statement or
        # a trailing source-code comment.
        if suffix and not suffix.startswith("#"):
            return None

        try:
            text = ast.literal_eval(string_literal)
        except (SyntaxError, ValueError):
            return None

        if not isinstance(text, str):
            return None

        if not prefix:
            return DialogueEntry(
                type="narration",
                text=text,
                filename=file_path,
                line_number=line_number,
            )

        prefix_parts = prefix.split()

        if not prefix_parts:
            return None

        if prefix_parts[0] in _IGNORED_PREFIXES:
            return None

        if not all(
            _IDENTIFIER_PATTERN.fullmatch(part)
            for part in prefix_parts
        ):
            return None

        speaker = prefix_parts[0]
        attributes = tuple(prefix_parts[1:])

        return DialogueEntry(
            type="dialogue",
            speaker=speaker,
            attributes=attributes,
            text=text,
            filename=file_path,
            line_number=line_number,
        )

    @staticmethod
    def _extract_quoted_string(
        statement: str,
    ) -> tuple[str, str, str] | None:
        """
        Extract the first complete double-quoted string.

        Returns:
            prefix, quoted string literal, suffix
        """

        opening_quote = statement.find('"')

        if opening_quote == -1:
            return None

        escaped = False
        closing_quote: int | None = None

        for index in range(
            opening_quote + 1,
            len(statement),
        ):
            character = statement[index]

            if character == "\\" and not escaped:
                escaped = True
                continue

            if character == '"' and not escaped:
                closing_quote = index
                break

            escaped = False

        if closing_quote is None:
            return None

        prefix = statement[:opening_quote].strip()

        string_literal = statement[
            opening_quote : closing_quote + 1
        ]

        suffix = statement[
            closing_quote + 1 :
        ].strip()

        return prefix, string_literal, suffix