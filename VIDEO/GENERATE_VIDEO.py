from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout
import os




def generate_video(audio_path,image_paths):
    # Paths
    #audio_path = "pudcast/combined_output.mp3"
    #image_folder = "images"
    output_video_path = "podcast/podcast.mp4"

    # Get the list of image paths in order


    # Load the audio and calculate its duration
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration  # Total duration of the audio in seconds

    # Calculate the duration for each image
    num_images = len(image_paths)
    image_duration = audio_duration / num_images  # Equal duration for each image

    # Create a list of image clips with fade transitions
    image_clips = []
    for i, image_path in enumerate(image_paths):
        # Load the image as a clip
        image_clip = ImageSequenceClip([image_path], durations=[image_duration])
        
        # Add fade-in and fade-out transitions (1 second each)
        if i > 0:  # Fade-in for all images except the first
            image_clip = image_clip.fadein(1)
        if i < num_images - 1:  # Fade-out for all images except the last
            image_clip = image_clip.fadeout(1)
        
        image_clips.append(image_clip)

    # Concatenate all image clips into a single video clip
    final_video_clip = concatenate_videoclips(image_clips, method="compose")

    # Set the audio of the video clip to the podcast audio
    final_video_clip = final_video_clip.set_audio(audio_clip)

    # Write the final video to a file
    final_video_clip.write_videofile(output_video_path, fps=24)  # Standard fps for smooth video

    print(f"Video saved to {output_video_path}")

    return output_video_path