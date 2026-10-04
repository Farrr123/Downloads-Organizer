import pathlib
from collections import Counter

TARGET_DIR = pathlib.Path(r"D:\Business\python\My Projects\Downloads Organizer\Test Files")

EXTENSION_MAP = {
    "image": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"},
    "document": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".xls", ".pptx", ".ppt"},
    "audio": {".mp3", ".wav", ".ogg", ".flac", ".m4a"},
    "archive": {".zip", ".rar", ".7z", ".tar", ".gz"}
}

def get_file_category(file_suffix: str) -> str:
    suffix_clean = file_suffix.lower()
    for category, extensions in EXTENSION_MAP.items():
        if suffix_clean in extensions:
            return category
    return "other"

def organize_and_count(folder_path: pathlib.Path, move_files: bool = False):
    
    if not folder_path.exists():
        print(f"Error: The directory '{folder_path}' does not exist.")
        return

    counter = Counter()

    print(f"\n--- Processing Directory: {folder_path} ---")
    for file_path in folder_path.glob("*.*"):
        if file_path.is_file():
            category = get_file_category(file_path.suffix)
            counter[category] += 1
            print(f"[+] {file_path.name} -> {category}")

            if move_files:
                dest_dir = folder_path / category
                dest_dir.mkdir(exist_ok=True)
                file_path.rename(dest_dir / file_path.name)

    print("\n--- Summary Statistics ---")
    for category_name, count in counter.items():
        print(f"  - {category_name.capitalize()}: {count}")
    
    print(f"Total Processed Files: {sum(counter.values())}\n")

if __name__ == "__main__":
    organize_and_count(TARGET_DIR, move_files=False)
