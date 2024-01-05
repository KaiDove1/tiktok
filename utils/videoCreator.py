from moviepy.editor import VideoFileClip
import random

def extract_random_clip(video_path, duration=60, clip_length=60):
    # Load the video
    video = VideoFileClip(video_path)

    # Maximum start time calculation
    max_start = duration - clip_length

    # Random start time
    start_time = random.randint(0, max_start)

    # Extract the clip
    clip = video.subclip(start_time, start_time + clip_length)

    # Save the clip
    clip_filename = f"clip_{start_time}_{start_time + clip_length}.mp4"
    clip.write_videofile(clip_filename, codec="libx264")

    print(f"Clip saved as {clip_filename}")

extract_random_clip('C:\\Users\\KaiDo\\[02]Work\\Projects\\Automate_Social\\local_content\\Minecraft_Parkour.mp4', duration=823, clip_length=60)
