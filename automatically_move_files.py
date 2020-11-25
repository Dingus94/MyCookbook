from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil



class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            shutil.move(src, new_destination)

    def destination_decider(self):
        for filename in os.listdir(folder_to_track):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                return r"F:\Downloads\Images"
            elif filename.lower().endswith('.exe'):
                return r"F:\Downloads\exe"
            else:
                return r"F:\Downloads"

folder_to_track = r"C:\Users\Thoma\Downloads"
folder_destination = str(MyHandler.destination_decider(1))
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()


