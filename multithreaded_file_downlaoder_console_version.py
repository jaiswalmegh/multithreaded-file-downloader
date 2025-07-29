import threading
import requests
import os

# List of URLs to download (replace with actual URLs)
urls = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.pdf",
    "https://example.com/file3.zip"
]

# Create download folder
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# Download logic
def download_file(url):
    local_filename = os.path.join(download_dir, url.split("/")[-1])
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0

        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        percent = (downloaded / total_size) * 100
                        print(f"[{threading.current_thread().name}] Downloading {local_filename}: {percent:.2f}%")

        print(f"[{threading.current_thread().name}] Completed: {local_filename}")

    except Exception as e:
        print(f"[{threading.current_thread().name}] Error downloading {url}: {e}")

# Main function
def main():
    threads = []
    for url in urls:
        t = threading.Thread(target=download_file, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("All downloads completed.")

if __name__ == "__main__":
    main()
