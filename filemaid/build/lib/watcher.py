from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if event.is_directory:
            return
        self.callback(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return

    def on_any_event(self, event):
        print("EVENT:", event.event_type, event.src_path)


def start_watching(folder, callback):
    observer = Observer()
    observer.schedule(MyHandler(callback), folder, recursive=False)

    observer.start()
    print("Watching:", folder)

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


