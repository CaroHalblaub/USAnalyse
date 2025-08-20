import cv2
import os
import numpy as np


video_path = r"video path einsetzen"
output_dir = r"path des speicherorts der frames"


os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

# Gesamtanzahl Frames im Video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 20 gleichmäßig verteilte Frames
num_frames_to_extract = 20
frame_indices = np.linspace(0, total_frames-1, num_frames_to_extract, dtype=int)

frame_count = 0
saved_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count in frame_indices:
        frame_name = os.path.join(output_dir, f"p_person1_video0_frame_{saved_count:02d}.png")
        cv2.imwrite(frame_name, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"{saved_count} Frames extrahiert in {output_dir}")



