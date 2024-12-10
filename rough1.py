import mediapipe as mp
import cv2
import time
from rough import get_label


fixed_label = get_label()
print(f"ok lets guide you for {fixed_label} pose")

if fixed_label != None: 

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.4, min_tracking_confidence=0.4)

    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    capture_interval = 2 #sec
    last_capture_time = time.time()

    if not cap.isOpened():
        print("sorry i didnt see")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        #image processing according to model
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        current_time = time.time()

        if current_time - last_capture_time >= capture_interval:
            last_capture_time = current_time  # Update the last capture time

            # Check if landmarks are found
            if results.pose_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                for idx, landmark in enumerate(results.pose_landmarks.landmark):
                    print("🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")
                    print(f"Landmark {idx}: ({landmark.x}, {landmark.y}, {landmark.z})")

        cv2.imshow("Body Points Tracking", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()