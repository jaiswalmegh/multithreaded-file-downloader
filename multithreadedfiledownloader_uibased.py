import sys
import os
import threading
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QFileDialog, QLabel, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Downloader(QWidget):
    def __init__(self):
        super().__init__()
        self.download_folder = os.path.expanduser("~")  # better default than cwd
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("⚡ Multi-threaded File Downloader")
        self.setGeometry(200, 200, 700, 500)
        self.setStyleSheet("background-color: #f4f6f9;")

        layout = QVBoxLayout()

        # Title
        title = QLabel("🔽 Multi-threaded File Downloader")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        layout.addWidget(title)

        # Folder Selection
        folder_layout = QHBoxLayout()
        self.folder_label = QLabel(f"Download Folder: {self.download_folder}")
        self.folder_label.setStyleSheet("color: #34495e; font-size: 12px;")
        self.browse_btn = QPushButton("📂 Browse Folder")
        self.browse_btn.setStyleSheet(
            "background-color: #3498db; color: white; padding: 6px 12px; border-radius: 4px;"
        )
        self.browse_btn.clicked.connect(self.browse_folder)
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.browse_btn)
        layout.addLayout(folder_layout)

        # URL Input
        self.url_input = QTextEdit()
        self.url_input.setPlaceholderText("Enter one URL per line...")
        self.url_input.setStyleSheet(
            "background-color: white; padding: 10px; border: 1px solid #bdc3c7; font-family: Consolas;"
        )
        layout.addWidget(self.url_input)

        # Download Button
        self.download_btn = QPushButton("🚀 Start Download")
        self.download_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.download_btn.setStyleSheet(
            "background-color: #27ae60; color: white; padding: 10px; border-radius: 6px;"
        )
        self.download_btn.clicked.connect(self.start_downloads)
        layout.addWidget(self.download_btn)

        # Output Log
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet(
            "background-color: #ecf0f1; padding: 10px; font-family: Consolas; border: 1px solid #95a5a6;"
        )
        layout.addWidget(self.log_output)

        self.setLayout(layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if folder:
            self.download_folder = folder
            self.folder_label.setText(f"Download Folder: {self.download_folder}")

    def start_downloads(self):
        urls = self.url_input.toPlainText().strip().split('\n')
        urls = [url.strip() for url in urls if url.strip()]
        if not urls:
            QMessageBox.warning(self, "Error", "Please enter at least one URL.")
            return

        for url in urls:
            thread = threading.Thread(target=self.download_file, args=(url,))
            thread.start()

    def log(self, message):
        self.log_output.append(message)
        self.log_output.verticalScrollBar().setValue(self.log_output.verticalScrollBar().maximum())

    def download_file(self, url):
        try:
            filename = os.path.join(self.download_folder, url.split('/')[-1])
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = (downloaded / total_size) * 100 if total_size else 0
                        self.log(f"[{filename}] {percent:.2f}% downloaded")

            self.log(f"[{filename}] ✅ Download complete!")
        except Exception as e:
            self.log(f"[{url}] ❌ Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Downloader()
    window.show()
    sys.exit(app.exec_())
