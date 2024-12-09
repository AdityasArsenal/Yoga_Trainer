import os
from keras.models import load_model 
from tensorflow_hub import KerasLayer
import PIL.Image as Image
import numpy as np

model_path = r'C:\Users\24adi\OneDrive\Desktop\for yoga\Yoga_Trainer\yoga_pose_detector.h5'
if os.path.exists(model_path):
    model = load_model(model_path, custom_objects={'KerasLayer': KerasLayer})
else:
    print("Model file not found!")

img_shape = (224, 224)
yoga_pose = Image.open('imgs/t.jpg').resize(img_shape)

yoga_pose = np.array(yoga_pose)/255.0
yoga_pose.shape

yoga_pose[np.newaxis, ...]

result = model.predict(yoga_pose[np.newaxis, ...])
result.shape

labs = ['downdog', 'goddess', 'plank', 'tree', 'warror2']
predicted_label_index = np.argmax(result)

print("🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")
print(f"The fucking pose is : {predicted_label_index}:{labs[predicted_label_index]}")
print("🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")

