import cv2

# Function to read video and return a list of frames
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return frames  # Return an empty list if the video can't be opened
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame is None:
            print("Warning: Empty frame encountered.")
            continue
        frames.append(frame)  # Store each frame in the list
    cap.release()  # Release the video capture object after reading
    return frames  # Return the list of frames

# Function to save a list of frames to a video file
def save_video(output_video_frames, output_video_path):
    if len(output_video_frames) == 0:
        print("Error: No frames to save.")
        return
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Video codec
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()
    print(f"Video saved successfully at {output_video_path}")