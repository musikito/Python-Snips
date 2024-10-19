import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

# Function to download video
def download_video():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    # Ask for download directory
    download_folder = filedialog.askdirectory()
    if not download_folder:
        messagebox.showerror("Error", "Please choose a download location.")
        return

    # yt-dlp options for downloading video
    ydl_opts = {
        'format': 'best',  # Best quality video
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Output template
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Video downloaded successfully to {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")

# Function to download audio and convert it to MP3 using FFmpeg
def download_audio():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    # Ask for download directory
    download_folder = filedialog.askdirectory()
    if not download_folder:
        messagebox.showerror("Error", "Please choose a download location.")
        return

    # yt-dlp options for downloading audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio format
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Output template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Audio quality
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Audio downloaded and converted to MP3 in {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")

# Initialize Tkinter window
root = tk.Tk()
root.title("YouTube Audio/Video Downloader")
root.geometry("400x200")

# URL input label and entry
label_url = tk.Label(root, text="YouTube URL:")
label_url.pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Buttons for video and audio download
btn_video = tk.Button(root, text="Download Video", command=download_video)
btn_video.pack(pady=10)

btn_audio = tk.Button(root, text="Download Audio (MP3)", command=download_audio)
btn_audio.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
