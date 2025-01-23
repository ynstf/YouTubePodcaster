import subprocess
from mutagen.id3 import ID3, TIT2, TPE1

def fix_music(path_music):

    # Input and output file paths
    input_file = "podcust/background.mp3"
    output_file = "podcust/background_fixed.mp3"

    # Step 1: Convert the audio file using FFmpeg
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_file,          # Input file
        "-c:a", "libmp3lame",      # Audio codec (MP3)
        "-q:a", "2",               # Audio quality
        output_file                # Output file
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Audio conversion complete. Saved as '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running FFmpeg: {e}")
        exit(1)
    except FileNotFoundError:
        print("FFmpeg is not installed or not found in your system's PATH.")
        exit(1)

    # Step 2: Add metadata using mutagen
    try:
        # Load the output file's ID3 tags (or create new ones if they don't exist)
        audio = ID3(output_file)
    except Exception:
        # If the file has no existing ID3 tags, create a new ID3 object
        audio = ID3()

    # Add title and artist metadata
    audio["TIT2"] = TIT2(encoding=3, text="Generated Music")  # Title
    audio["TPE1"] = TPE1(encoding=3, text="Unknown")          # Artist

    # Save the metadata to the file
    audio.save(output_file)
    print(f"Metadata added to '{output_file}'")

    return output_file