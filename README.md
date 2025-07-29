📥 Multithreaded File Downloader (Python)
This project demonstrates how to download multiple files simultaneously using multithreading in Python.

It includes:

✅ A simple Console-Based Downloader

🎨 A beautiful GUI-based Downloader using PyQt5

🚀 Features
Download multiple files concurrently using Python threads

Set custom download folder

GUI with real-time download logs

Clean and modern PyQt5 interface

📂 Project Structure
multithreaded_file_downloader/
│
├── downloader_console.py       # Console-based downloader
├── downloader_gui.py           # GUI-based PyQt5 downloader
├── README.md                   # This file

🖥️ Console Version
▶️ How to Run
python downloader_console.py

📄 How It Works
Enter the number of URLs

Paste each URL one by one

Files are downloaded concurrently using Python threads

Progress is printed in the terminal

🛠 Requirements
Python 3.x

requests library

Install with: pip install requests

🖼 GUI Version (PyQt5)
▶️ How to Run
python downloader_gui.py
🖌 Features
Multi-threaded download engine

Select download folder using folder picker

Paste multiple URLs (one per line)

Styled interface with log area

Start downloads in parallel

🛠 Requirements
Python 3.x

requests, PyQt5

Install with: pip install requests PyQt5
