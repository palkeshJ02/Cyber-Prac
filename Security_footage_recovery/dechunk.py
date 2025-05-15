import re

boundary = b"--BoundaryString"
jpeg_start = b"\xff\xd8"
jpeg_end = b"\xff\xd9"

with open("stream.raw", "rb") as f:
    data = f.read()

parts = data.split(boundary)
frame_count = 0

for part in parts:
    if jpeg_start in part and jpeg_end in part:
        start = part.find(jpeg_start)
        end = part.find(jpeg_end)
        jpeg = part[start:end+2]
        with open(f"frame_{frame_count:04d}.jpg", "wb") as out:
            out.write(jpeg)
        frame_count += 1

print(f"Extracted {frame_count} frames.")
