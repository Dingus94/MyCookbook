from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os, sys
import json
import time
import shutil


def getSize(filename):
    if os.path.isfile(filename):
        st = os.stat(filename)
        return st.st_size
    else:
        return -1

def wait_download(file_path):
    current_size = getSize(file_path)
    print("File size")
    time.sleep(1)
    while current_size != getSize(file_path) or getSize(file_path) == 0:
        current_size = getSize(file_path)
        print("current_size:" + str(current_size))
        time.sleep(1)  # wait download
    print("Downloaded")
    time.sleep(1)
    return True

class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            wait_download(filename)
            time.sleep(1)
            if 
            self.on_modified(event)


            # src = folder_to_track + "/" + filename
            # new_destination = folder_destination + "/" + filename
            # if wait_download(src) == True:
            #     shutil.move(src, new_destination)

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


