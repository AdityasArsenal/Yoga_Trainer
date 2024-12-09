import PIL.Image as Image
import numpy as np
import tensorflow_hub as hub
from tensorflow import keras

model = keras.models.load_model('Pose_model.h5', custom_objects={'KerasLayer': hub.KerasLayer})

IMAGE_SHAPE = (224,224)

yoga_pose = Image.open("www.jpg").resize(IMAGE_SHAPE)
yoga_pose

yoga_pose = np.array(yoga_pose)/255.0
yoga_pose.shape

yoga_pose[np.newaxis, ...]

result = model.predict(yoga_pose[np.newaxis, ...])
result.shape

labs = ['downdog', 'goddess', 'plank', 'tree', 'warror2']
predicted_label_index = np.argmax(result)
print(f"{predicted_label_index}:{labs[predicted_label_index]}")