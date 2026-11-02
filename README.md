
# Downloads Organizer

A Python command-line tool that organizes files into folders based on their extensions.

## Features

- Categorizes images, videos, documents, audio files, archives, and other files.
- Supports dry-run mode by default.
- Moves files only when `--move` is specified.
- Skips hidden files and directories.
- Prevents overwriting existing files by generating unique filenames.
- Displays a summary of processed files.
- Includes automated tests using pytest.

## File Categories

| Category | Examples |
|---|---|
| Image | `.jpg`, `.png`, `.gif`, `.svg` |
| Video | `.mp4`, `.mkv`, `.avi` |
| Document | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| Audio | `.mp3`, `.wav`, `.flac` |
| Archive | `.zip`, `.rar`, `.7z` |
| Other | Unknown extensions or files without extensions |

## Requirements

- Python 3.10 or newer
- pytest (for running tests only)

## Usage

Clone the repository:

```bash
git clone https://github.com/Farrr123/Downloads-Organizer.git
cd Downloads-Organizer
```

Run in dry-run mode:

```bash
python downloads_organizer_Enhanced.py ~/Downloads
```

Move files into category folders:

```bash
python downloads_organizer_Enhanced.py ~/Downloads --move
```

Show available options:

```bash
python downloads_organizer_Enhanced.py --help
```

**Note:** Dry-run mode is enabled by default. Files are not moved unless `--move` is specified.

## Running Tests

Install pytest:

```bash
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -v
```

## Technologies

- Python
- pathlib
- argparse
- shutil
- collections.Counter
- pytest

## Project Structure

```text
Downloads Organizer/
├── downloads_organizer.py
├── downloads_organizer_Enhanced.py
├── tests/
│   └── test_downloads_organizer.py
├── README.md
└── .gitignore
```

## License

Not specified yet.
