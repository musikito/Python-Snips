from pytube import YouTube

# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context


def download_video(video_url, save_to):
    try:
        yt = YouTube(video_url)

        # Get the highest resolution
        video_stream = yt.streams.get_highest_resolution()

        # if you want just the audio
        audio_stream = yt.streams.get_audio_only()

        # Download it
        # video_stream.download(output_path=save_to)
        audio_stream.download(output_path=save_to)
        print("download completed")

    except Exception as e:
        print("Hay un Error: ", str(e))


video_link = "https://www.youtube.com/watch?v=AkNFuVJiehk"  # Insert YT video link here
save_path = "/Users/josemiguelmarte/Downloads/"  # insert path where to save video

# Call you Function
download_video(video_link, save_path)
