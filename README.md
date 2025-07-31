⚡ Multi-threaded File Downloader (Python + PyQt5)
A lightweight, GUI-based file downloader that supports multiple simultaneous downloads using multithreading. Built with Python and PyQt5, this app provides an intuitive interface for downloading large files efficiently.

📸 Preview
Add a screenshot or gif demo here if you have one!

✅ Features
🧠 Multi-threaded downloads – improves speed and performance

📥 Paste multiple URLs – download many files at once

📁 Select download folder – choose where to save files each session

🚀 Real-time logs – track download progress per file

💡 Cleans filenames – removes query strings to avoid OS errors

🎨 Modern PyQt5 GUI – easy to use, no command line needed

⚠️ Important Usage Notes
This downloader supports only direct file URLs — for example, links ending in .jpg, .png, .pdf, etc.

✅ Valid example:  https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg

❌ Invalid example (webpage, not a file): https://www.pexels.com/photo/green-and-blue-peacock-feather-674010/
Make sure you copy the actual file URL, not just the webpage where the file is displayed.

🛠️ Tech Stack
Python 3

PyQt5 – GUI

threading – concurrent downloads

requests – HTTP streaming and file writing

📂 Folder Structure
multithreadedfiledownloader/
├── downloader.py        # Main PyQt5 app
├── README.md            # You're reading it :)
├── requirements.txt     # Python dependencies

🧱 Code Structure
downloader.py
├── class Downloader(QWidget)
│   ├── __init__()                   # Initializes the UI and variables
│   ├── init_ui()                    # Sets up the PyQt5 GUI layout
│   ├── browse_folder()              # Opens folder picker dialog
│   ├── start_downloads()            # Triggers downloads using threading
│   ├── log(message)                 # Appends messages to the output log
│   └── download_file(url)          # Downloads a file in a separate thread
│       ├── Handles HTTP streaming
│       ├── Cleans filename using urlparse
│       └── Updates real-time log with download progress


🧠 How It Works
Paste one or more direct download URLs into the input box.

Click "Start Download".

You'll be prompted to select a folder.

Each file will be downloaded in its own thread.

Progress logs appear in real-time.

💡 Future Improvements (Suggestions welcome!)
Progress bars per file

Cancel/resume support

Download history

Drag-and-drop file support

🤝 Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

📄 License
This project is licensed under the MIT License.

🙌 Author
Megh Jaiswal
GitHub: @jaiswalmegh
LinkedIn: https://www.linkedin.com/in/megh-jaiswal-0762b2339/
