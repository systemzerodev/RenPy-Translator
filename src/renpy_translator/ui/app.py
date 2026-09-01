"""Main desktop interface for RenPy Translator."""

from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from renpy_translator.core.extractor import ProjectExtractor
from renpy_translator.core.models import DialogueEntry


class RenPyTranslatorApp(ctk.CTk):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.project_path: Path | None = None
        self.dialogues: list[DialogueEntry] = []

        self.title("RenPy Translator")
        self.geometry("1280x760")
        self.minsize(1050, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._configure_window()
        self._create_header()
        self._create_sidebar()
        self._create_editor()
        self._create_statusbar()

    def _configure_window(self) -> None:
        """Configure the main application grid."""

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

    def _create_header(self) -> None:
        """Create the top toolbar."""

        self.header = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=0,
        )
        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew",
        )

        self.header.grid_columnconfigure(
            0,
            weight=1,
        )

        self.app_title = ctk.CTkLabel(
            self.header,
            text="RenPy Translator",
            font=ctk.CTkFont(
                size=22,
                weight="bold",
            ),
        )
        self.app_title.grid(
            row=0,
            column=0,
            padx=24,
            pady=18,
            sticky="w",
        )

        self.toolbar = ctk.CTkFrame(
            self.header,
            fg_color="transparent",
        )
        self.toolbar.grid(
            row=0,
            column=1,
            padx=18,
            pady=12,
            sticky="e",
        )

        self.open_button = ctk.CTkButton(
            self.toolbar,
            text="Open Game",
            width=110,
            command=self._open_game,
        )
        self.open_button.pack(
            side="left",
            padx=5,
        )

        self.scan_button = ctk.CTkButton(
            self.toolbar,
            text="Scan",
            width=90,
            state="disabled",
            command=self._scan_project,
        )
        self.scan_button.pack(
            side="left",
            padx=5,
        )

        self.save_button = ctk.CTkButton(
            self.toolbar,
            text="Save",
            width=90,
            state="disabled",
        )
        self.save_button.pack(
            side="left",
            padx=5,
        )

        self.export_button = ctk.CTkButton(
            self.toolbar,
            text="Export Patch",
            width=120,
            state="disabled",
        )
        self.export_button.pack(
            side="left",
            padx=5,
        )

    def _create_sidebar(self) -> None:
        """Create the project file sidebar."""

        self.sidebar = ctk.CTkFrame(
            self,
            width=260,
            corner_radius=0,
        )
        self.sidebar.grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        self.sidebar.grid_propagate(False)

        self.files_title = ctk.CTkLabel(
            self.sidebar,
            text="Project Files",
            font=ctk.CTkFont(
                size=17,
                weight="bold",
            ),
        )
        self.files_title.pack(
            padx=20,
            pady=(22, 12),
            anchor="w",
        )

        self.search_entry = ctk.CTkEntry(
            self.sidebar,
            placeholder_text="Search files...",
            height=36,
        )
        self.search_entry.pack(
            fill="x",
            padx=16,
            pady=(0, 14),
        )

        self.project_files = ctk.CTkScrollableFrame(
            self.sidebar,
            fg_color="transparent",
        )
        self.project_files.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8),
        )

        self._show_sidebar_message(
            "No project opened"
        )

    def _create_editor(self) -> None:
        """Create the main dialogue editor area."""

        self.editor = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#1E1E1E",
        )
        self.editor.grid(
            row=1,
            column=1,
            sticky="nsew",
        )

        self.editor.grid_columnconfigure(
            0,
            weight=1,
        )

        self.editor.grid_rowconfigure(
            1,
            weight=1,
        )

        self.editor_header = ctk.CTkFrame(
            self.editor,
            fg_color="transparent",
        )
        self.editor_header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=24,
            pady=(22, 12),
        )

        self.editor_header.grid_columnconfigure(
            0,
            weight=1,
        )

        self.editor_title = ctk.CTkLabel(
            self.editor_header,
            text="Dialogue Editor",
            font=ctk.CTkFont(
                size=20,
                weight="bold",
            ),
        )
        self.editor_title.grid(
            row=0,
            column=0,
            sticky="w",
        )

        self.dialogue_count = ctk.CTkLabel(
            self.editor_header,
            text="0 dialogues",
            text_color="gray60",
        )
        self.dialogue_count.grid(
            row=0,
            column=1,
            sticky="e",
        )

        self.editor_content = ctk.CTkFrame(
            self.editor,
            corner_radius=8,
        )
        self.editor_content.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=24,
            pady=(0, 20),
        )

        self.editor_content.grid_columnconfigure(
            0,
            weight=1,
        )

        self.editor_content.grid_rowconfigure(
            0,
            weight=1,
        )

        self._show_welcome_editor(
            title="No Ren'Py project opened",
            message=(
                "Open a Ren'Py game folder to scan its scripts "
                "and begin translating."
            ),
            show_button=True,
        )

    def _create_statusbar(self) -> None:
        """Create the bottom status bar."""

        self.statusbar = ctk.CTkFrame(
            self,
            height=38,
            corner_radius=0,
        )
        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew",
        )

        self.statusbar.grid_columnconfigure(
            1,
            weight=1,
        )

        self.status_label = ctk.CTkLabel(
            self.statusbar,
            text="Ready",
            text_color="gray70",
            font=ctk.CTkFont(size=12),
        )
        self.status_label.grid(
            row=0,
            column=0,
            padx=16,
            pady=8,
            sticky="w",
        )

        self.progress_label = ctk.CTkLabel(
            self.statusbar,
            text="Progress: 0 / 0 translated",
            text_color="gray70",
            font=ctk.CTkFont(size=12),
        )
        self.progress_label.grid(
            row=0,
            column=2,
            padx=16,
            pady=8,
            sticky="e",
        )

    def _clear_project_files(self) -> None:
        """Remove all widgets from the sidebar file list."""

        for widget in self.project_files.winfo_children():
            widget.destroy()

    def _clear_editor_content(self) -> None:
        """Remove all widgets from the editor content area."""

        for widget in self.editor_content.winfo_children():
            widget.destroy()

    def _show_sidebar_message(
        self,
        message: str,
    ) -> None:
        """Display a message inside the project sidebar."""

        self._clear_project_files()

        message_label = ctk.CTkLabel(
            self.project_files,
            text=message,
            text_color="gray60",
            anchor="w",
        )
        message_label.pack(
            fill="x",
            padx=12,
            pady=20,
            anchor="w",
        )

    def _show_welcome_editor(
        self,
        title: str,
        message: str,
        show_button: bool = False,
    ) -> None:
        """Display a centered message inside the editor."""

        self._clear_editor_content()

        welcome_frame = ctk.CTkFrame(
            self.editor_content,
            fg_color="transparent",
        )
        welcome_frame.grid(
            row=0,
            column=0,
        )

        title_label = ctk.CTkLabel(
            welcome_frame,
            text=title,
            font=ctk.CTkFont(
                size=21,
                weight="bold",
            ),
        )
        title_label.pack(
            pady=(0, 8),
        )

        message_label = ctk.CTkLabel(
            welcome_frame,
            text=message,
            text_color="gray60",
            font=ctk.CTkFont(size=14),
            wraplength=650,
        )
        message_label.pack(
            pady=(0, 18),
        )

        if show_button:
            open_button = ctk.CTkButton(
                welcome_frame,
                text="Open Game",
                width=130,
                command=self._open_game,
            )
            open_button.pack()

    def _open_game(self) -> None:
        """Open a folder picker and select a Ren'Py project."""

        selected_folder = filedialog.askdirectory(
            title="Select Ren'Py Game Folder"
        )

        if not selected_folder:
            return

        self.project_path = Path(
            selected_folder
        )

        self.dialogues = []

        self._show_sidebar_message(
            self.project_path.name
        )

        self._show_welcome_editor(
            title="Project ready to scan",
            message=(
                "The project folder has been selected. "
                "Click Scan to find and parse Ren'Py scripts."
            ),
        )

        self.scan_button.configure(
            state="normal"
        )

        self.save_button.configure(
            state="disabled"
        )

        self.export_button.configure(
            state="disabled"
        )

        self.dialogue_count.configure(
            text="0 dialogues"
        )

        self.progress_label.configure(
            text="Progress: 0 / 0 translated"
        )

        self.status_label.configure(
            text=f"Project opened: {self.project_path}"
        )

    def _scan_project(self) -> None:
        """Scan and parse the currently selected project."""

        if self.project_path is None:
            return

        self.status_label.configure(
            text="Scanning Ren'Py project..."
        )

        self.update_idletasks()

        extractor = ProjectExtractor(
            self.project_path
        )

        script_files, dialogues = (
            extractor.extract()
        )

        self.dialogues = dialogues

        self._render_script_files(
            script_files
        )

        if not script_files:
            self._show_welcome_editor(
                title="No Ren'Py scripts found",
                message=(
                    "Make sure you selected a Ren'Py project "
                    "or its game folder."
                ),
                show_button=True,
            )

            self.dialogue_count.configure(
                text="0 dialogues"
            )

            self.status_label.configure(
                text="No Ren'Py script files found."
            )

            return

        if not dialogues:
            self._show_welcome_editor(
                title="No supported dialogue found",
                message=(
                    "Ren'Py scripts were found, but the current "
                    "parser did not detect supported dialogue."
                ),
            )

            self.dialogue_count.configure(
                text="0 dialogues"
            )

            self.status_label.configure(
                text=(
                    f"Found {len(script_files)} scripts, "
                    "but no supported dialogue."
                )
            )

            return

        self._render_dialogues()

        self.dialogue_count.configure(
            text=f"{len(dialogues)} dialogues"
        )

        self.progress_label.configure(
            text=(
                f"Progress: 0 / "
                f"{len(dialogues)} translated"
            )
        )

        self.status_label.configure(
            text=(
                f"Found {len(script_files)} scripts "
                f"and {len(dialogues)} dialogues."
            )
        )

    def _render_script_files(
        self,
        script_files: list[Path],
    ) -> None:
        """Display discovered Ren'Py scripts in the sidebar."""

        self._clear_project_files()

        if not script_files:
            self._show_sidebar_message(
                "No .rpy files found"
            )
            return

        if self.project_path is None:
            return

        extractor = ProjectExtractor(
            self.project_path
        )

        script_root = (
            extractor.scanner.script_root
        )

        for script_file in script_files:
            relative_path = script_file.relative_to(
                script_root
            )

            display_path = str(
                relative_path
            ).replace("\\", "/")

            file_label = ctk.CTkLabel(
                self.project_files,
                text=display_path,
                anchor="w",
            )
            file_label.pack(
                fill="x",
                padx=12,
                pady=4,
                anchor="w",
            )

    def _render_dialogues(self) -> None:
        """Display extracted dialogue inside the editor."""

        self._clear_editor_content()

        table = ctk.CTkScrollableFrame(
            self.editor_content,
            fg_color="transparent",
        )
        table.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=8,
            pady=8,
        )

        table.grid_columnconfigure(
            0,
            weight=0,
            minsize=70,
        )

        table.grid_columnconfigure(
            1,
            weight=0,
            minsize=110,
        )

        table.grid_columnconfigure(
            2,
            weight=1,
            minsize=300,
        )

        table.grid_columnconfigure(
            3,
            weight=1,
            minsize=300,
        )

        headers = (
            "Line",
            "Speaker",
            "Original Text",
            "Translation",
        )

        for column, header in enumerate(
            headers
        ):
            header_label = ctk.CTkLabel(
                table,
                text=header,
                font=ctk.CTkFont(
                    size=13,
                    weight="bold",
                ),
                anchor="w",
            )
            header_label.grid(
                row=0,
                column=column,
                sticky="ew",
                padx=8,
                pady=(6, 12),
            )

        for row_index, dialogue in enumerate(
            self.dialogues,
            start=1,
        ):
            line_label = ctk.CTkLabel(
                table,
                text=str(
                    dialogue.line_number
                ),
                anchor="w",
            )
            line_label.grid(
                row=row_index,
                column=0,
                sticky="ew",
                padx=8,
                pady=6,
            )

            speaker_text = (
                dialogue.speaker
                if dialogue.speaker
                else "Narrator"
            )

            speaker_label = ctk.CTkLabel(
                table,
                text=speaker_text,
                anchor="w",
            )
            speaker_label.grid(
                row=row_index,
                column=1,
                sticky="ew",
                padx=8,
                pady=6,
            )

            original_label = ctk.CTkLabel(
                table,
                text=dialogue.text,
                anchor="w",
                justify="left",
                wraplength=360,
            )
            original_label.grid(
                row=row_index,
                column=2,
                sticky="ew",
                padx=8,
                pady=6,
            )

            translation_entry = ctk.CTkEntry(
                table,
                placeholder_text="Enter translation...",
                height=36,
            )
            translation_entry.grid(
                row=row_index,
                column=3,
                sticky="ew",
                padx=8,
                pady=6,
            )


def run_app() -> None:
    """Start RenPy Translator."""

    app = RenPyTranslatorApp()
    app.mainloop()