import numpy as np
import cv2
import PIL.Image as Image
import os
import matplotlib.pylab as plt
from train_n_test._classifier_load import classifier
import pathlib

IMAGE_SHAPE = (224, 224)

yoga_pose = Image.open("imgs/w.jpg").resize(IMAGE_SHAPE)

yoga_pose = np.array(yoga_pose)/255.0
print(f"The dimensions of the image : {yoga_pose.shape}")

yoga_pose[np.newaxis, ...]

result = classifier.predict(yoga_pose[np.newaxis, ...])
print(f"The result shape : {result.shape}")

predicted_label_index = np.argmax(result)

image_labels = []
with open("gitfiles/labs.txt", "r") as f:
    image_labels = f.read().splitlines() 

image_label = image_labels[predicted_label_index]

print(f"Predicted index : {predicted_label_index} and Label : {image_label}")


