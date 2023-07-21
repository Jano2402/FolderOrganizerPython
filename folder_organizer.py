import os
from pathlib import Path
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

directory = input('Ingresa la ruta completa de la carpeta a ordenar: ')

os.chdir(f"{directory}")
images_folder = (f"{directory}/Imagenes")
video_folder = (f"{directory}/Videos")
audio_folder = (f"{directory}/Audio")
zips_folder = (f"{directory}/Zips")
installers_folder = (f"{directory}/Instaladores - programas")
pdfs_folder = (f"{directory}/PDFs")

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