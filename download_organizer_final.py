import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Definir rutas de carpetas
images_folder = "C:/Users/Usuario/Downloads/Imagenes"
video_folder = "C:/Users/Usuario/Downloads/Videos"
audio_folder = "C:/Users/Usuario/Downloads/Audio"
zips_folder = "C:/Users/Usuario/Downloads/Zips"
installers_folder = "C:/Users/Usuario/Downloads/Instaladores - programas"
pdfs_folder = "C:/Users/Usuario/Downloads/PDFs"

# Crear las carpetas si no existen
os.makedirs(images_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(zips_folder, exist_ok=True)
os.makedirs(installers_folder, exist_ok=True)
os.makedirs(pdfs_folder, exist_ok=True)

def move_file_with_duplicate_handling(src_file, dest_folder):
    base_name, ext = os.path.splitext(os.path.basename(src_file))
    dest_path = os.path.join(dest_folder, f"{base_name}{ext}")
    counter = 1

    while os.path.exists(dest_path):
        dest_path = os.path.join(dest_folder, f"{base_name}_{counter}{ext}")
        counter += 1

    shutil.move(src_file, dest_path)

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file = event.src_path
        name, ext = os.path.splitext(file)
        ext = ext.lower()
    
        if ext in [".jpg", ".png", ".jpeg", ".avif", ".webp"]:
            move_file_with_duplicate_handling(file, images_folder)
        elif ext in [".mp4", ".movi", ".gif"]:
            move_file_with_duplicate_handling(file, video_folder)
        elif ext == ".pdf":
            move_file_with_duplicate_handling(file, pdfs_folder)
        elif ext == ".mp3":
            move_file_with_duplicate_handling(file, audio_folder)
        elif ext in [".zip", ".rar"]:
            move_file_with_duplicate_handling(file, zips_folder)
        elif ext == ".exe":
            move_file_with_duplicate_handling(file, installers_folder)

if __name__ == "__main__":
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path="C:/Users/Usuario/Downloads", recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()