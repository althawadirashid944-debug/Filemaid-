from watcher import start_watching
from main import filter_engine
from pathlib import Path

def main():
    downloads = Path.home() / "Downloads"
    start_watching(downloads, filter_engine) 