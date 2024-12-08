import numpy as np
import cv2

import PIL.Image as Image
import os

import matplotlib.pylab as plt

import tensorflow as tf
import tensorflow_hub as hub

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

IMAGE_SHAPE = (224, 224)

classifier = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4", input_shape=IMAGE_SHAPE+(3,))
])

yoga_pose = Image.open("yy.jpg").resize(IMAGE_SHAPE)
yoga_pose

yoga_pose = np.array(yoga_pose)/255.0
yoga_pose.shape

yoga_pose[np.newaxis, ...]

result = classifier.predict(yoga_pose[np.newaxis, ...])
result.shape

predicted_label_index = np.argmax(result)
predicted_label_index

!wget https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt


image_labels = []
with open("ImageNetLabels.txt", "r") as f:
    image_labels = f.read().splitlines()
image_labels[:5]

image_labels[predicted_label_index]

%%capture
!sudo apt -qq install git-lfs
!git config --global credential.helper store

#Mount your google drive
from google.colab import drive
drive.mount('/content/drive')

!ls -al "/content/drive/MyDrive/yoga-poses-dataset.zip"

!unzip "/content/drive/MyDrive/yoga-poses-dataset" -d /tmp/yogaimg

data_dir="/tmp/yogaimg/yoga-poses-dataset/DATASET/TRAIN"

import pathlib
data_dir = pathlib.Path(data_dir)
data_dir

list(data_dir.glob('*/*.jpg'))[:5]

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

TT = list(data_dir.glob('tree/*'))
TT[:5]

import PIL
PIL.Image.open(str(TT[1]))

DD = list(data_dir.glob('downdog/*'))
PIL.Image.open(str(DD[0]))

yoga_poses_img_dict = {
    'downdog': list(data_dir.glob('downdog/*')),
    'goddess': list(data_dir.glob('goddess/*')),
    'plank': list(data_dir.glob('plank/*')),
    'tree': list(data_dir.glob('tree/*')),
    'warror2': list(data_dir.glob('warrior2/*')),
}

yoga_poses_lab_dict = {
    'downdog': 0,
    'goddess': 1,
    'plank':   2,
    'tree':    3,
    'warror2': 4,
}

yoga_poses_img_dict['tree'][:5]

str(yoga_poses_img_dict['tree'][0])
img = cv2.imread(str(yoga_poses_img_dict['tree'][0]))
img.shape

cv2.resize(img,(224,224)).shape

X, y = [], []

for pose_name, images in yoga_poses_img_dict.items():
    for image in images:
        img = cv2.imread(str(image))
        resized_img = cv2.resize(img,(224,224))
        X.append(resized_img)
        y.append(yoga_poses_lab_dict[pose_name])

X = np.array(X)
y = np.array(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

X[0].shape

IMAGE_SHAPE+(3,)

x0_resized = cv2.resize(X[0], IMAGE_SHAPE)
x1_resized = cv2.resize(X[1], IMAGE_SHAPE)
x2_resized = cv2.resize(X[2], IMAGE_SHAPE)

plt.axis('off')
plt.imshow(X[4])

predicted = classifier.predict(np.array([x0_resized, x1_resized, x2_resized]))
predicted = np.argmax(predicted, axis=1)
predicted


image_labels[550]

feature_extractor_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

pretrained_model_without_top_layer = hub.KerasLayer(
    feature_extractor_model, input_shape=(224, 224, 3), trainable=False)

num_of_poses = 5

model = tf.keras.Sequential([
  pretrained_model_without_top_layer,
  tf.keras.layers.Dense(num_of_poses)
])

model.summary()

model.compile(
  optimizer="adam",
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['acc'])

model.fit(X_train_scaled, y_train, epochs=5)

model.evaluate(X_test_scaled,y_test)

model.save('yoga_classifier.h5')

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