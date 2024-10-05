import subprocess


def convert_wav_to_mp3(input_file, output_file):
    """Converts a WAV file to MP3."""

    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-vn",
        "-ar",
        "44100",
        "-ac",
        "2",
        output_file,
    ]
    subprocess.call(command)


if __name__ == "__main__":
    input_file = "131660__bertrof__game-sound-correct.wav"
    output_file = "brick_break1.mp3"
    convert_wav_to_mp3(input_file, output_file)
