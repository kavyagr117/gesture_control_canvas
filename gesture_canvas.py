import cv2                      # OpenCV for video capture and drawing
import mediapipe as mp          # MediaPipe for hand detection
import numpy as np              # NumPy for canvas operations
import time                     # Time module to add delays for gestures

# === Initialize MediaPipe Hands module ===
mp_hands = mp.solutions.hands  # Load hand tracking model
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)  # Allow only 1 hand, with a confidence threshold
mp_drawing = mp.solutions.drawing_utils  # For drawing hand landmarks on the frame

# === Try to access the webcam ===
cap = cv2.VideoCapture(0)      # Try default camera (index 0)
if not cap.isOpened():         # If failed, try second camera (index 1)
    cap = cv2.VideoCapture(1)
if not cap.isOpened():         # If still failed, exit program
    print("❌ Could not access any webcam.")
    exit()

# === Read first frame to get video dimensions ===
ret, frame = cap.read()        # Capture first frame
if not ret:                    # If capture failed, exit
    print("❌ Could not read frame from camera.")
    exit()
height, width = frame.shape[:2]  # Get height and width of frame

# === Create a black canvas (same size as video frame) ===
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# === Predefine drawing colors and control variables ===
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]  # Blue, Green, Red, Cyan, Magenta
current_color_index = 0       # Start with the first color
points = []                   # Store points to draw lines

# === Gesture debounce variables to avoid rapid switching ===
last_gesture_time = 0         # Time of last gesture
gesture_delay = 1             # Delay in seconds between gestures

# === Function to count raised fingers ===
def count_fingers(landmarks):
    finger_tips = [4, 8, 12, 16, 20]  # Thumb to pinky tip landmarks
    count = 0

    # Check if thumb is open (left of base for right hand)
    if landmarks[4].x < landmarks[3].x:
        count += 1

    # Check other fingers by comparing tip and mid-joint
    for tip in finger_tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:  # Raised if tip is above the joint
            count += 1

    return count  # Return how many fingers are up

# === Main loop to continuously capture frames ===
while True:
    ret, frame = cap.read()    # Read a frame from camera
    if not ret:
        break                  # Break loop if failed

    frame = cv2.flip(frame, 1)  # Flip horizontally (like a mirror)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for MediaPipe
    results = hands.process(rgb_frame)  # Process frame for hand landmarks

    # === If hands are detected ===
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Draw hand on frame

            landmark_list = hand_landmarks.landmark  # Get list of 21 landmarks
            finger_count = count_fingers(landmark_list)  # Count raised fingers
            current_time = time.time()  # Get current time

            # === Change color if 3 fingers are raised and enough time passed ===
            if finger_count == 3 and current_time - last_gesture_time > gesture_delay:
                current_color_index = (current_color_index + 1) % len(colors)  # Cycle to next color
                points = []                  # Reset drawing points
                last_gesture_time = current_time  # Update last gesture time

            # === Clear canvas if 5 fingers are raised ===
            elif finger_count == 5 and current_time - last_gesture_time > gesture_delay:
                canvas = np.zeros_like(canvas)  # Clear canvas
                points = []                     # Reset drawing points
                last_gesture_time = current_time

            # === If drawing (less than 3 fingers), track index fingertip ===
            elif finger_count < 3:
                x = int(landmark_list[8].x * width)   # Get x position of index fingertip
                y = int(landmark_list[8].y * height)  # Get y position of index fingertip
                points.append((x, y))  # Save point to draw line

    # === Draw continuous lines between points on canvas ===
    if len(points) > 1:
        for i in range(1, len(points)):
            cv2.line(canvas, points[i - 1], points[i], colors[current_color_index], 5)

    # === Draw color indicator box on top-left of frame ===
    cv2.rectangle(frame, (10, 10), (60, 60), colors[current_color_index], -1)  # Color box
    cv2.putText(frame, f"Color {current_color_index + 1}", (70, 50),           # Label
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # === Show the live frame and the canvas side by side ===
    cv2.imshow("Frame", frame)     # Video with hand tracking
    cv2.imshow("Canvas", canvas)   # Drawing canvas

    # === Exit if 'q' key is pressed ===
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === Clean up: release camera and close all OpenCV windows ===
cap.release()
cv2.destroyAllWindows()

