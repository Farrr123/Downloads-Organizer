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
