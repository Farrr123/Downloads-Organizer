import importlib.util
from pathlib import Path

PROJECT_FILE = Path(__file__).parent.parent / "downloads_organizer_Enhanced.py"

spec = importlib.util.spec_from_file_location("organizer", PROJECT_FILE)
organizer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(organizer)


def test_jpg_is_image():
    assert organizer.get_file_category(".jpg") == "image"


def test_mp4_is_video():
    assert organizer.get_file_category(".mp4") == "video"


def test_pdf_is_document():
    assert organizer.get_file_category(".pdf") == "document"


def test_mp3_is_audio():
    assert organizer.get_file_category(".mp3") == "audio"


def test_zip_is_archive():
    assert organizer.get_file_category(".zip") == "archive"


def test_unknown_extension_is_other():
    assert organizer.get_file_category(".xyz") == "other"


def test_extension_is_case_insensitive():
    assert organizer.get_file_category(".JPG") == "image"


def test_file_without_extension_is_other():
    assert organizer.get_file_category("") == "other"
    
def test_organize_moves_file(tmp_path):
    source_file = tmp_path / "photo.jpg"
    source_file.write_text("test image")

    organizer.organize(tmp_path, move=True)

    destination_file = tmp_path / "image" / "photo.jpg"

    assert destination_file.exists()
    assert not source_file.exists()
    assert destination_file.read_text() == "test image"


def test_organize_does_not_overwrite_existing_file(tmp_path):
    image_folder = tmp_path / "image"
    image_folder.mkdir()

    existing_file = image_folder / "photo.jpg"
    existing_file.write_text("OLD FILE")

    source_file = tmp_path / "photo.jpg"
    source_file.write_text("NEW FILE")

    organizer.organize(tmp_path, move=True)

    assert existing_file.read_text() == "OLD FILE"
    assert (image_folder / "photo (1).jpg").read_text() == "NEW FILE"
    
def test_hidden_files_are_ignored(tmp_path):
    hidden_file = tmp_path / ".secret"
    hidden_file.write_text("hidden data")

    counts = organizer.organize(tmp_path, move=True)

    assert hidden_file.exists()
    assert sum(counts.values()) == 0


def test_dry_run_does_not_move_files(tmp_path):
    source_file = tmp_path / "photo.jpg"
    source_file.write_text("test image")

    organizer.organize(tmp_path, move=False)

    assert source_file.exists()
    assert not (tmp_path / "image").exists()