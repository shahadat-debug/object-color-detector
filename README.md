# Object and Color Detector 🔍🎨

A beginner-friendly computer vision project built with Python, OpenCV, and NumPy. This project uses a webcam to detect colored regions, estimate their colors, and display bounding boxes in real time.

## ✨ Features

- Real-time webcam video processing
- Detection of colored regions
- Approximate color classification
- Green bounding boxes around detected regions
- Color labels displayed on the video
- Noise reduction using morphological operations
- Press `Q` to exit the application

## 🛠️ Technologies

- Python
- OpenCV
- NumPy

## 📦 Installation

Install Python, then run:

```bash
python -m pip install opencv-python numpy
```

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder in VS Code.
3. Install the required libraries.
4. Run:

```bash
python object_color_detector.py
```

5. Allow webcam access and hold a colored object in front of the camera.
6. Press `Q` to close the application.

## 🎯 Learning Objectives

- Understand webcam capture with OpenCV
- Learn BGR and HSV color spaces
- Apply color thresholding and masks
- Detect contours and bounding rectangles
- Estimate colors from image pixels

## ⚠️ Limitations

This version detects colored regions rather than identifying real-world object names such as bottle, phone, or apple. Color estimates can vary with lighting, shadows, and background.

## 👨‍💻 Author

**Shahadat Ali**

Software Engineering Student | Python & Computer Vision Learner
