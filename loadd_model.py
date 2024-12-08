import tensorflow_hub as hub
from tensorflow import keras

model = keras.models.load_model('Pose_model.h5', custom_objects={'KerasLayer': hub.KerasLayer})
