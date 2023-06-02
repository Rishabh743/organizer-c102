import sys
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
fromdir="C:/Users/amit2/Downloads"
todir="C:/Users/amit2/Downloads"
dir_tree = { 
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
    "Document_Files": ['.ppt','.xls', '.xlsx' '.csv', '.pdf', '.txt'],
      "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            if ext in value:
                filename=os.path.basename(event.src.path)
                print("downloaded")
                path1=fromdir+"/"+filename
                path2=todir+"/"+key
                path3=todir+"/"+key+"/"+filename
                if os.path.exists(path2):
                    print("moving")
                    shutil.move(path1,path3)
                else:
                    print("making")
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep1(1)
event=FileMovementHandler()
observer=Observer()
observer.schedule(event,fromdir,recursive=True)
observer.start()
while True:
    time.sleep(2)
    print("running")
              
                    





