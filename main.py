import os
import math
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop

# === Konfigurasi ===
input_path = "input_video.mp4"
output_folder = "shorts_output"
clip_duration = 60
short_width = 720
short_height = 1280

# === Buat folder output ===
os.makedirs(output_folder, exist_ok=True)

# === Buka video utama ===
video = VideoFileClip(input_path)
total_duration = video.duration
total_clips = math.floor(total_duration / clip_duration)

print(f"Total durasi video: {total_duration:.2f}s")
print(f"Jumlah shorts yang dihasilkan: {total_clips}")

# === Loop potong video ===
for i in range(total_clips):
    start_time = i * clip_duration
    end_time = start_time + clip_duration
    print(f"Proses clip ke-{i+1}: {start_time}s - {end_time}s")

    clip = video.subclip(start_time, end_time)
    resized = clip.resize(height=short_height)
    w, h = resized.size
    crop_x = (w - short_width) // 2
    vertical_clip = crop(resized, x1=crop_x, width=short_width, y1=0, height=short_height)

    output_file = os.path.join(output_folder, f"short_{i+1}.mp4")
    vertical_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

print("✅ Semua shorts berhasil dibuat!")
