from pytube import YouTube
import os
import subprocess

# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context


def download_video(video_url, save_to):
    try:
        yt = YouTube(video_url)

        # Get the highest resolution
        # video_stream = yt.streams.get_highest_resolution()

        # if you want just the audio
        audio_stream = yt.streams.get_audio_only()

        # Download video
        # video_stream.download(output_path=save_to)

        # Download audio
        print("Downloading... " + yt.title)
        audio_stream.download(output_path=save_to)
        # Get default name using pytube API
        name = audio_stream.default_filename
        # Use the same name with the mp3 extension
        new_name = yt.title + ".mp3"
        # Uncomment the next line if you want to enter your own name
        # new_filename = input("Enter filename (including extension): "))  # e.g. new_filename.mp3

        # Converting
        print("Converting to mp3...")
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                os.path.join(save_to, name),
                os.path.join(save_to, new_name),
            ]
        )
        # Delete the .mp4 file
        print("Deleting file " + name)
        os.remove(save_to + name)
        # rename to mp3
        # base, ext = os.path.splitext(output)
        # renamed = base + ".mp3"
        # os.rename(output, renamed)

        print(yt.title + " download completed")

    except Exception as e:
        print("Hay un Error: ", str(e))


video_link = str(input("Enter URL: \n>> "))  # Insert YT video link here
# save_path = "/Users/josemiguelmarte/Downloads/"  # insert path where to save video
print("Enter destination (leave blank for current directory)")
save_path = str(input(">> ")) or "."
# Call you Function
download_video(video_link, save_path)
