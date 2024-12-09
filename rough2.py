import mediapipe as mp
import cv2
import time

fixed_label = "goddess"
print(fixed_label)

if fixed_label == "goddess": 
    
    # Initialize MediaPipe Pose module
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.4, min_tracking_confidence=0.4)

    # Initialize MediaPipe drawing module
    mp_drawing = mp.solutions.drawing_utils

    # Open webcam
    cap = cv2.VideoCapture(0)

    # Set the interval for capturing an image (2 seconds)
    capture_interval = 2 # seconds
    last_capture_time = time.time()

    print(f" your choosen pose {fixed_label}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to get pose landmarks
        results = pose.process(image)

        # Convert the RGB image back to BGR for OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Get the current time
        current_time = time.time()

        # Capture and process an image every 2 seconds
        if current_time - last_capture_time >= capture_interval:
            last_capture_time = current_time  # Update the last capture time

            # Check if landmarks are found
            if results.pose_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # Access and print body landmarks
                for idx, landmark in enumerate(results.pose_landmarks.landmark):
                    print(f"Landmark {idx}: ({landmark.x}, {landmark.y}, {landmark.z})")

        # Display the output
        cv2.imshow("Body Points Tracking", image)

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture object and close windows
    cap.release()
    cv2.destroyAllWindows()
