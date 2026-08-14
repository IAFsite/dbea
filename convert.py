import subprocess

input_file = "C:/Users/Furru/Downloads/2026-08-15 02-32-11 - Trim.mp4"
output_file = "C:/Users/Furru/Downloads/penjelasankpk.webm"

subprocess.run([
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libvpx-vp9",
    "-crf", "32",
    "-b:v", "0",
    "-c:a", "libopus",
    "-b:a", "96k",
    output_file
])

print("Selesai:", output_file)