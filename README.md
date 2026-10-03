# 📂 File Categorizer & Downloads Organizer
  A smart, efficient Python automation tool designed to categorize and inspect files in any directory (such as Downloads) based on their file extensions.


✨ Key Features
📂 Automatic Categorization: Group files into Images, Videos, Documents, Audio, and Archives.

  📊 Real-time Statistics: Calculates summary counts using collections.Counter.

  🛠️ Cross-Platform: Uses standard pathlib for flexible file path management.

  ⚡ Clean Architecture: Follows best practices and clear function separation.


📊 Sample Output

--- Processing Directory: D:\Downloads ---
[+] book.pdf -> document
[+] data.xlsx -> document
[+] movie.mkv -> video
[+] photo.png -> image
[+] song.mp3 -> audio

--- Summary Statistics ---
  - Document: 2
  - Image: 1
  - Video: 1
  - Audio: 1

Total Processed Files: 5


🚀 Quick Start
# Clone the repository
  git clone [https://github.com/Farrr123/Downloads-Organizer.git](https://github.com/Farrr123/Downloads-Organizer.git)

# Navigate to project directory
  cd Downloads-Organizer

# Run the script
  python main.py


💻 Tech Stack

Language: Python 3.x

Core Modules: pathlib, collections
