import cv2
import mediapipe as mp
from PIL import Image
from transformers import MobileNetV2ImageProcessor
import torch
from loadd_model import model  # Ensure this imports your trained model

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize the MobileNetV2 image processor
image_processor = MobileNetV2ImageProcessor.from_pretrained('google/mobilenet_v2_1.0_224')

# Class names for yoga poses
names = ['Downdog', 'Goddess', 'Plank', 'Tree', 'Warrior2']

# Start webcam video capture (0 is typically the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Start live video feed
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame (BGR) to RGB and then to a PIL Image for processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(rgb_frame)

    # Preprocess the image for pose classification
    inputs = image_processor(images=image, return_tensors="pt")

    # Make predictions with the trained model
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():  # Disable gradient calculation
        outputs = model(**inputs)

    # Get the predicted class (max logit)
    predicted_class = torch.argmax(outputs.logits, dim=-1).item()

    # Process the image for pose landmarks with MediaPipe
    results = pose.process(rgb_frame)

    # Draw pose landmarks
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            # Convert normalized landmark to pixel coordinates
            h, w, _ = frame.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Draw green circle at each landmark

    # Display the predicted class on the video frame
    cv2.putText(frame, f"Predicted Pose: {names[predicted_class]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the video frame with pose landmarks
    cv2.imshow('Yoga Pose Detection with Landmarks', frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
