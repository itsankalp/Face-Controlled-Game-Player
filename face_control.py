#Run The Code In ipynb
import cv2 #new cell
import mediapipe as mp #new cell
import pyautogui #new cell
import time #new cell
import numpy as np #new cell
# Setup on new cell
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)
cap = cv2.VideoCapture(0)

# Settings
cooldown = 1  # seconds
last_action_time = time.time()
movement_threshold = 25  # Sensitivity

# Movement history for smoothing
x_history = []
y_history = []
buffer_size = 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            nose = landmarks.landmark[1]
            nose_x = int(nose.x * w)
            nose_y = int(nose.y * h)

            x_history.append(nose_x)
            y_history.append(nose_y)

            if len(x_history) > buffer_size:
                x_history.pop(0)
                y_history.pop(0)

            avg_x = int(np.mean(x_history))
            avg_y = int(np.mean(y_history))

            cv2.circle(frame, (avg_x, avg_y), 5, (0, 255, 0), -1)

            # Detect movement direction with cooldown
            now = time.time()
            if now - last_action_time > cooldown:
                dx = nose_x - avg_x
                dy = nose_y - avg_y

                if dx > movement_threshold:
                    print("➡️ Right")
                    pyautogui.press('right')
                    last_action_time = now
                elif dx < -movement_threshold:
                    print("⬅️ Left")
                    pyautogui.press('left')
                    last_action_time = now

                if dy < -movement_threshold:
                    print("⬆️ Up")
                    pyautogui.press('up')
                    last_action_time = now
                elif dy > movement_threshold:
                    print("⬇️ Down")
                    pyautogui.press('down')
                    last_action_time = now

    cv2.imshow("Smooth Face Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
