import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube
import os
import subprocess


def download_content():
    video_url = url_entry.get()
    save_to = path_entry.get()
    download_type = download_var.get()

    try:
        yt = YouTube(video_url)

        if download_type == "audio":
            stream = yt.streams.get_audio_only()
            file_extension = "mp3"
        else:
            stream = yt.streams.get_highest_resolution()
            file_extension = "mp4"

        status_label.config(text=f"Downloading... {yt.title}")
        stream.download(output_path=save_to)
        name = stream.default_filename
        new_name = f"{yt.title}.{file_extension}"

        if download_type == "audio":
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
        else:
            os.rename(os.path.join(save_to, name), os.path.join(save_to, new_name))

        status_label.config(text=f"{yt.title} download completed")
        messagebox.showinfo(
            "Success", f"{yt.title} has been downloaded as {file_extension}."
        )

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def browse_path():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)


# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

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

# Add radio buttons for download type
download_var = tk.StringVar(value="audio")
tk.Radiobutton(root, text="Audio", variable=download_var, value="audio").grid(
    row=2, column=0, pady=5
)
tk.Radiobutton(root, text="Video", variable=download_var, value="video").grid(
    row=2, column=1, pady=5
)

tk.Button(root, text="Download", command=download_content).grid(
    row=3, column=1, pady=10
)

status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
