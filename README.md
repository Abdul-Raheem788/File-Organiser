# File-Organiser
A lightweight Python script that automatically organizes files in any folder into categorized subfolders.
Great for cleaning messy directories like Downloads, Desktop, and Workspaces.


⭐ Features
🔎 Detects file types automatically
📂 Moves files into categories:
Documents → .pdf, .pptx, .docx, .txt
Images → .png, .jpg, .jpeg
Music → .mp3, .wav
Code → .py, .html, .js, .css
Others → anything else
🗂️ Creates category folders if missing
🧾 Generates a clean Organizer_Log.txt
🚫 Skips hidden files, directories, and the log file itself
⚙️ Uses only standard libraries (os, shutil) — no dependencies


📦 Installation
Clone the repo:
git clone https://github.com/yourusername/folder-organizer.git
cd folder-organizer
No external packages needed.


▶️ How to Run
Run the script:
When prompted, enter the folder you want to organize:
Enter the folder path you want to organize: /Users/YourName/Downloads
That's it — your folder will be neatly organized with a full log of actions.


🧪 Example Output
Before
Downloads/
│ file1.docx
│ image.png
│ music.mp3
│ script.py
│ random.xyz
After

Downloads/
│ Organizer_Log.txt
├── Documents/
│     file1.docx
├── Images/
│     image.png
├── Music/
│     music.mp3
├── Code/
│     script.py
└── Others/
      random.xyz


📝 Log File Example
file1.docx → Documents
image.png → Images
music.mp3 → Music
script.py → Code
random.xyz → Others


⚠️ Notes
The script moves, not copies.
Organizes only the top-level files, not nested directories.
If a file with the same name already exists in the target folder, it may be overwritten.
🤝 Contributing
Feel free to open issues or submit pull requests!
📜 License
This project is licensed under the MIT License.






