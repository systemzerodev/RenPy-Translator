<p align="center">
  <img src="assets/banner/banner.png" alt="RenPy Translator Banner" width="100%">
</p>

<h1 align="center">RenPy Translator</h1>

<p align="center">
  <strong>A modern, open-source desktop translation tool for Ren'Py visual novels.</strong>
</p>

<p align="center">
  Scan. Extract. Translate. Export.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Early%20Development-orange?style=for-the-badge" alt="Development Status">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CustomTkinter-Desktop%20UI-1F6AA5?style=for-the-badge" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/Platform-Desktop-lightgrey?style=for-the-badge" alt="Desktop">
  <img src="https://img.shields.io/github/license/systemzerodev/RenPy-Translator?style=for-the-badge" alt="License">
</p>

---

## About

**RenPy Translator** is an open-source desktop application designed to make translating Ren'Py visual novels easier, cleaner, and more accessible.

Instead of manually searching through large `.rpy` script files, the goal is to provide translators with a dedicated workspace where they can scan a Ren'Py project, review translatable dialogue, write translations, track progress, and export translation files ready to be used by Ren'Py.

The project is being built **desktop-first**, with simplicity and translator-friendly workflows as its main priorities.

> **Project Status:** RenPy Translator is currently being rebuilt from the ground up.  
> The repository is in its early development stage and is not yet ready for general use.

---

## Vision

The long-term goal is simple:

> Make Ren'Py game translation approachable even for users who are not programmers.

A typical workflow should eventually look like this:

```text
Select Ren'Py Game
        ↓
Scan Project Files
        ↓
Extract Translatable Text
        ↓
Translate in Desktop Editor
        ↓
Review Translation Progress
        ↓
Export Ren'Py Translation Patch
        ↓
Install Patch into Game
```

---

## Planned Features

### Core Translation Workflow

- [ ] Scan Ren'Py project directories
- [ ] Detect `.rpy` script files
- [ ] Parse translatable dialogue
- [ ] Extract speaker and dialogue information
- [ ] Preserve Ren'Py variables and text tags
- [ ] Create translation projects
- [ ] Save and resume translation progress

### Translation Editor

- [ ] Modern desktop interface
- [ ] Project file explorer
- [ ] Original text and translation view
- [ ] Inline translation editing
- [ ] Search dialogue
- [ ] Filter untranslated entries
- [ ] Translation progress tracking
- [ ] Auto-save support

### Export

- [ ] Generate Ren'Py translation files
- [ ] Indonesian translation support for the first release
- [ ] Export ready-to-install translation patches
- [ ] Preserve source file structure
- [ ] Validate translation output before export

### Future

- [ ] Multiple target languages
- [ ] Optional machine translation assistance
- [ ] Translation memory
- [ ] Advanced parser compatibility
- [ ] Additional quality-of-life tools
- [ ] Mobile companion interface

---

## Desktop UI Concept

The desktop application is planned around a translator-focused workspace:

```text
┌─────────────────────────────────────────────────────────────────────┐
│ RenPy Translator                                                   │
│ [ Open Game ] [ Scan ] [ Save ] [ Export Patch ]                  │
├───────────────────┬─────────────────────────────────────────────────┤
│ Project Files     │ Dialogue Editor                                │
│                   │                                                 │
│ script.rpy        │ ID │ Speaker │ Original Text │ Translation     │
│ day1.rpy          │ 01 │ e       │ Hello there.  │ Halo.           │
│ screens.rpy       │ 02 │ m       │ How are you?  │                 │
│ options.rpy       │                                                 │
│                   │                                                 │
├───────────────────┴─────────────────────────────────────────────────┤
│ Translation Progress: 1 / 2                                       │
└─────────────────────────────────────────────────────────────────────┘
```

The final interface may evolve during development.

---

## Technology

RenPy Translator is currently planned around a lightweight Python desktop stack.

| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| Desktop UI | CustomTkinter |
| Ren'Py Processing | Python |
| Project Data | JSON |
| Testing | pytest |
| Linting | Ruff |
| Formatting | Black |
| Import Sorting | isort |
| Git Hooks | pre-commit |
| Version Control | Git + GitHub |

The architecture is intended to keep the **translation engine independent from the UI**, making future interfaces easier to build without rewriting the core logic.

---

## Planned Architecture

```text
RenPy Translator
│
├── Core Engine
│   ├── Project Scanner
│   ├── Ren'Py Parser
│   ├── Translation Models
│   ├── Project Manager
│   └── Patch Generator
│
├── Desktop Interface
│   └── CustomTkinter
│
└── Project Storage
    └── JSON
```

---

## Planned Project Structure

```text
RenPy-Translator/
│
├── assets/
│   ├── banner/
│   ├── icons/
│   └── screenshots/
│
├── core/
│
├── docs/
│
├── tests/
│
├── ui/
│
├── ui_mobile/
│
├── .github/
│
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
│
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

> The structure may change as the architecture is finalized.

---

## Development Roadmap

Development will be approached incrementally.

### Phase 0 — Project Foundation

- [x] Create public repository
- [x] Define project direction
- [x] Select Python + CustomTkinter
- [ ] Complete repository documentation
- [ ] Configure development environment
- [ ] Configure testing and code-quality tools

### Phase 1 — Core Engine

- [ ] Translation data model
- [ ] Ren'Py project scanner
- [ ] `.rpy` parser
- [ ] Translation project manager
- [ ] Automated tests

### Phase 2 — Desktop Application

- [ ] Main window
- [ ] Project explorer
- [ ] Dialogue editor
- [ ] Inline translation editing
- [ ] Search and filtering
- [ ] Progress tracking

### Phase 3 — Translation Export

- [ ] Ren'Py translation generator
- [ ] Output validation
- [ ] Patch export workflow
- [ ] Test generated patches in real Ren'Py projects

### Phase 4 — Beta

- [ ] Real-world testing
- [ ] Parser compatibility improvements
- [ ] Error handling
- [ ] UI polish
- [ ] Documentation
- [ ] First public beta release

For the complete roadmap, see [`ROADMAP.md`](ROADMAP.md).

---

## Installation

RenPy Translator is **not yet available for installation**.

The project is currently under active development. Installation instructions will be added once the first usable development build is available.

If you are interested in development, watch the repository for future updates.

---

## Contributing

RenPy Translator is an open-source project, and contributions will be welcome as development progresses.

Before contributing, please read:

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)

Bug reports, feature ideas, documentation improvements, parser compatibility reports, and code contributions will all be valuable.

---

## Security

Please **do not report security vulnerabilities through public GitHub issues**.

See [`SECURITY.md`](SECURITY.md) for the responsible disclosure process.

---

## Changelog

Development history and notable changes will be documented in:

[`CHANGELOG.md`](CHANGELOG.md)

---

## License

RenPy Translator is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## Disclaimer

RenPy Translator is an independent open-source project.

It is **not affiliated with, endorsed by, or officially associated with Ren'Py or its developers**.

Ren'Py and related names belong to their respective owners.

Users are responsible for ensuring that they have the appropriate rights or permissions to modify or translate the games and content they work with.

---

## Support the Project

If RenPy Translator becomes useful to you, you can support its development by:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting improvements
- 🧪 Testing future releases
- 🤝 Contributing code or documentation

---

<p align="center">
  <strong>Built for translators, visual novel fans, and the Ren'Py community.</strong>
</p>

<p align="center">
  Open source • Desktop first • Community driven
</p>