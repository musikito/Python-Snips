from pytube import YouTube
import os

# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context


def download_video(video_url, save_to):
    try:
        yt = YouTube(video_url)

        # Get the highest resolution
        video_stream = yt.streams.get_highest_resolution()

        # if you want just the audio
        audio_stream = yt.streams.get_audio_only()

        # Download video
        # video_stream.download(output_path=save_to)

        # Download audio
        output = audio_stream.download(output_path=save_to)
        # Convert to mp3
        base, ext = os.path.splitext(output)
        renamed = base + ".mp3"
        os.rename(output, renamed)

        print(yt.title + " download completed")

    except Exception as e:
        print("Hay un Error: ", str(e))


video_link = str(input("Enter URL: \n>> "))  # Insert YT video link here
# save_path = "/Users/josemiguelmarte/Downloads/"  # insert path where to save video
print("Enter destination (leave blank for current directory)")
save_path = str(input(">> ")) or "."
# Call you Function
download_video(video_link, save_path)
