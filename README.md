# Face-Controlled-Game-Player
A real-time face movement tracking system that allows users to control computer games using facial gestures. Built using Python, OpenCV, MediaPipe, and PyAutoGUI, the project maps nose movement to arrow key presses, enabling hands-free interaction with games like Subway Surfers.
# 🎮 Face Movement Game Controller

This project allows users to control computer games using facial movements, using real-time computer vision techniques. Specifically tested with **Subway Surfers**, this controller maps your nose movement to arrow key presses using your webcam — creating a hands-free game control experience.

---

## 📹 How It Works

The system uses:

- **MediaPipe** – To detect facial landmarks (especially nose tip).
- **OpenCV** – To capture and process webcam input.
- **NumPy** – To calculate average movement using a smoothing buffer.
- **PyAutoGUI** – To simulate keyboard arrow key presses.

---

## 🧠 Features

- Real-time nose tracking for directional control.
- Smoothing algorithm to reduce jittery input.
- Adjustable movement sensitivity and cooldown.
- Simple to run with minimal dependencies.

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

---

## 🚀 Installation

pip install opencv-python mediapipe pyautogui numpy
python face_control.py
