import argparse
import shutil
from collections import Counter
from pathlib import Path

EXTENSION_MAP = {
    "image": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"},
    "document": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".xls", ".pptx", ".ppt"},
    "audio": {".mp3", ".wav", ".ogg", ".flac", ".m4a"},
    "archive": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def get_file_category(suffix: str) -> str:
    """Return the category for a file extension, or 'other'."""
    suffix = suffix.lower()
    for category, extensions in EXTENSION_MAP.items():
        if suffix in extensions:
            return category
    return "other"


def unique_destination(dest: Path) -> Path:
    """Avoid overwriting: file.txt -> file (1).txt -> file (2).txt"""
    counter = 1
    candidate = dest
    while candidate.exists():
        candidate = dest.with_name(f"{dest.stem} ({counter}){dest.suffix}")
        counter += 1
    return candidate


def organize(folder: Path, move: bool = False) -> Counter:
    counts = Counter()
    for file_path in sorted(folder.iterdir()):
        if not file_path.is_file() or file_path.name.startswith("."):
            continue
        category = get_file_category(file_path.suffix)
        counts[category] += 1
        print(f"{file_path.name} -> {category}")
        if move:
            dest_dir = folder / category
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), unique_destination(dest_dir / file_path.name))
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Categorize files in a folder by extension.")
    parser.add_argument("folder", nargs="?", type=Path, default=Path.home() / "Downloads")
    parser.add_argument("--move", action="store_true", help="Actually move files (default: dry run)")
    args = parser.parse_args()

    if not args.folder.is_dir():
        raise SystemExit(f"Error: '{args.folder}' is not a valid directory.")

    counts = organize(args.folder, move=args.move)
    print("\n--- Summary ---")
    for category, count in counts.most_common():
        print(f"{category}: {count}")
    print(f"total: {sum(counts.values())}")


if __name__ == "__main__":
    main()