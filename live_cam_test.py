import os
import cv2
from keras.models import load_model
from tensorflow_hub import KerasLayer
import PIL.Image as Image
import numpy as np

# Load the pre-trained model
model_path = r'C:\Users\24adi\OneDrive\Desktop\for yoga\Yoga_Trainer\yoga_pose_detector.h5'
if os.path.exists(model_path):
    model = load_model(model_path, custom_objects={'KerasLayer': KerasLayer})
else:
    print("Model file not found!")

# Define the image shape the model expects
img_shape = (224, 224)

# List of yoga pose labels
labs = ['downdog', 'goddess', 'plank', 'tree', 'warror2']

# Open webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Continuously capture frames from the webcam
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to PIL Image and resize to match model input shape
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    resized_frame = frame_pil.resize(img_shape)

    # Preprocess the image (normalize)
    frame_array = np.array(resized_frame) / 255.0
    frame_array = frame_array[np.newaxis, ...]

    # Get prediction from the model
    result = model.predict(frame_array)
    predicted_label_index = np.argmax(result)

    # Display the result on the frame
    label = labs[predicted_label_index]
    confidence = result[0][predicted_label_index]

    # Display the prediction label and confidence on the frame
    cv2.putText(frame, f"Pose: {label} ({confidence*100:.2f}%)", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame with the prediction
    cv2.imshow("Yoga Pose Detection", frame)

    # Press 'q' to quit the live feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
