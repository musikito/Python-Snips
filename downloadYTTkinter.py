import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os
import subprocess


def download_video():
    video_url = url_entry.get()
    save_to = path_entry.get()

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.get_audio_only()

        status_label.config(text=f"Downloading... {yt.title}")
        audio_stream.download(output_path=save_to)
        name = audio_stream.default_filename
        new_name = f"{yt.title}.mp3"

        status_label.config(text="Converting to mp3...")
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                os.path.join(save_to, name),
                os.path.join(save_to, new_name),
            ]
        )

        status_label.config(text=f"Deleting file {name}")
        os.remove(os.path.join(save_to, name))

        status_label.config(text=f"{yt.title} download completed")
        messagebox.showinfo(
            "Success", f"{yt.title} has been downloaded and converted to MP3."
        )

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def browse_path():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)


# Create the main window
root = tk.Tk()
root.title("YouTube Audio Downloader")

# Create and place widgets
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Save to:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
path_entry = tk.Entry(root, width=50)
path_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_path).grid(
    row=1, column=2, padx=5, pady=5
)

tk.Button(root, text="Download", command=download_video).grid(row=2, column=1, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()
