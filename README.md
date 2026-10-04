# Downloads Organizer

A simple Python script that scans files in a folder, identifies their file types, and categorizes them into different groups.

## What It Does

The program checks each file based on its extension and categorizes it into:

- Images
- Videos
- Documents
- Audio
- Others

It also counts how many files belong to each category.

## Example Output

```text
archive.zip → other
book.pdf → document
data.xlsx → document
movie.mkv → video
photo.png → image
song.mp3 → audio

other: 2
document: 3
video: 2
image: 2
audio: 2
total: 11
```
# Technologies
Python 3
pathlib
collections.Counter

# How It Works
1. The program scans the selected folder.
2. It checks each file extension.
3. The file is assigned to a category.
4. The program displays the category for each file.
5. It calculates summary statistics.

# Safety
This version is a dry run.

It only analyzes and categorizes files.
It does not move, delete, or modify any files.

# Project Structure
```text
Downloads Organizer/
├── downloads_organizer.py
├── README.md
├── screenshot.png
└── Test Files/
