from watcher import start_watching 
from pathlib import Path
import shutil 
import time 
rules = {
    # images
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",

    # videos
    ".mp4": "videos",
    ".mkv": "videos",

    # audio
    ".mp3": "audio",
    ".wav": "audio",

    # documents
    ".pdf": "documents",
    ".docx": "documents",
    ".txt": "documents",

    # archives
    ".zip": "archives",
    ".rar": "archives",

    # code
    ".py": "code",
    ".js": "code",

    # linux/installers
    ".flatpakref": "apps",
    ".deb": "apps"
}
downloads = Path.home() / "Downloads"

def filter_engine(file_path):
    path = Path(file_path)

    if not path.is_file():
        return

    if path.suffix in [".crdownload", ".part", ".tmp"]:
        return

    
    def wait_until_stable(path, timeout=30):
        old_size = -1
        stable_ticks = 0

        for _ in range(timeout):
            try:
                new_size = path.stat().st_size
            except FileNotFoundError:
                return False

            if new_size == old_size:
                stable_ticks += 1
                if stable_ticks >= 2:
                    return True
            else:
                stable_ticks = 0

            old_size = new_size
            time.sleep(1)

        return False

    if not wait_until_stable(path):
        return

    suffix = "".join(path.suffixes).lower()
    folder_name = rules.get(suffix, "other")
    target_folder = downloads / folder_name
    target_folder.mkdir(parents=True, exist_ok=True)

    dest = target_folder / path.name

    if dest.exists():
        base = path.stem
        ext = path.suffix
        counter = 1

        while dest.exists():
            dest = target_folder / f"{base}_{counter}{ext}"
            counter += 1

    shutil.move(str(path), str(dest))
    print("Moved:", path.name) 
def sort_existing_files():
    for f in downloads.iterdir():

      
        if not f.is_file():
            continue

        
        if f.parent != downloads:
            continue

        folder_name = rules.get(f.suffix, "other")
        target_folder = downloads / folder_name
        target_folder.mkdir(exist_ok=True)

        shutil.move(str(f), str(target_folder))
if __name__ == "__main__":
    sort_existing_files()  # optional cleanup
    start_watching(downloads, filter_engine) 