import os
from pathlib import Path
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

os.chdir("C:/Users/Usuario/Downloads")
images_folder = ("C:/Users/Usuario/Downloads/Imagenes")
video_folder = ("C:/Users/Usuario/Downloads/Videos")
audio_folder = ("C:/Users/Usuario/Downloads/Audio")
zips_folder = ("C:/Users/Usuario/Downloads/Zips")
installers_folder = ("C:/Users/Usuario/Downloads/Instaladores - programas")
pdfs_folder = ("C:/Users/Usuario/Downloads/PDFs")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(zips_folder, exist_ok=True)
os.makedirs(installers_folder, exist_ok=True)
os.makedirs(pdfs_folder, exist_ok=True)

downloads_files = os.listdir()
for file in downloads_files:
    name, ext = os.path.splitext(file)
    
    if ext in [".jpg", ".png",".jpeg", ".avif", ".webp"]:
        shutil.move(file, images_folder)
    elif ext in [".mp4", ".movi",".gif"]:
        shutil.move(file, video_folder)
    elif ext == ".pdf":
        shutil.move(file, pdfs_folder)
    elif ext == ".mp3":
        shutil.move(file, audio_folder)
    elif ext in [".zip", ".rar"]:
        shutil.move(file, zips_folder)
    elif ext == ".exe":
        shutil.move(file, installers_folder)