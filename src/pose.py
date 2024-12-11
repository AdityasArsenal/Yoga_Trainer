from keras.models import load_model
from tensorflow_hub import KerasLayer
import cv2
import numpy as np
import time

def get_pose() : 
    model_path = r"mod\yoga_pose_detector.h5"
    model = load_model(model_path, custom_objects={'KerasLayer': KerasLayer})

    img_shape = (224, 224)
    labs = ['downdog', 'goddess', 'plank', 'tree', 'warrior2']

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("please give access to camera")
        exit()

    static_label = None
    static_start_time = None
    threshold_time = 5  # seconds

    while True:
        ret, frame = cap.read()

        if not ret:
            print("sorry i didn't see")
            continue

        # Pre-processing
        resized_frame = cv2.resize(frame, img_shape)
        initial_frame_array = np.array(resized_frame)
        normalized_frame_array = initial_frame_array / 255.0
        frame_array = normalized_frame_array[np.newaxis, ...]

        result = model.predict(frame_array, verbose=0)
        predicted_idx = np.argmax(result)

        label = labs[predicted_idx]

        # Check if the label is static
        if label == static_label:
            if static_start_time is None:
                static_start_time = time.time()
            elif time.time() - static_start_time > threshold_time:
                print(f"ok i will now instruct you to perform '{label}'  LES'S GOOOOOOOO")
                return label
                break
        else:
            static_label = label
            static_start_time = None

        cv2.putText(
            frame, f"Pose detected by model: {label}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
            cv2.LINE_AA
        )

        cv2.imshow("Pose detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


