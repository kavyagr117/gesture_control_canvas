
# Gesture-Controlled Canvas

This project allows you to control a drawing canvas using **hand gestures** captured through a webcam. The user can draw, change colors, and clear the canvas by performing specific hand gestures, such as raising fingers or using the index finger.

The project uses **OpenCV** for video capture and **MediaPipe** for hand tracking and gesture recognition. The drawing can be done with various colors, and the canvas can be reset with simple gestures.

---

## Features
- **Gesture-Based Drawing**: Use hand gestures to draw on the canvas.
- **Color Change**: Cycle through a predefined set of colors by raising 3 fingers.
- **Canvas Reset**: Clear the canvas by raising 5 fingers.
- **Real-Time Feedback**: Live video feed with drawn lines and color selection.
  
---

## Requirements

Before running the project, make sure to install the necessary dependencies.

### Python Libraries:
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

To install these dependencies, you can use the following command:

```bash
pip install opencv-python mediapipe numpy
```

---

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/gesture-controlled-canvas.git
   cd gesture-controlled-canvas
   ```

2. Install the required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python gesture_canvas.py
   ```

4. The webcam feed should open, and you can begin using gestures to control the canvas.

---

## Gestures and Controls
- **3 Fingers Raised**: Change the drawing color.
- **5 Fingers Raised**: Clear the canvas.
- **Index Finger Raised**: Draw lines on the canvas (move your finger to draw).

---

## Troubleshooting

- **Could not access the webcam**: Ensure that your webcam is connected and accessible by other applications (e.g., Camera app in Windows).
- **Camera index out of range**: If you have multiple cameras, the script may need to be adjusted to use the correct index for your webcam.
- **Low FPS**: Ensure that your system has sufficient resources and that no other heavy applications are running in the background.

---

## License

This project is open source and available under the MIT License.

---

## Acknowledgments

- [OpenCV](https://opencv.org/) for the computer vision library.
- [MediaPipe](https://mediapipe.dev/) for the hand tracking model.
- [NumPy](https://numpy.org/) for efficient numerical operations.
```

---

### Key Sections:
1. **Project Description**: Clear description of what the project does.
2. **Features**: A bullet point list of what the project can do.
3. **Requirements**: List of dependencies to install.
4. **How to Run**: Clear instructions for running the script.
5. **Gestures and Controls**: Describes the gestures and their actions.
6. **Troubleshooting**: Potential issues and fixes for common problems.
7. **License and Acknowledgments**: Info on licensing and credits for used technologies.

