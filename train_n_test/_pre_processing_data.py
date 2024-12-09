import pathlib
import cv2
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from train_n_test._classifier_load import classifier

IMAGE_SHAPE = (224,224)

data_dir = r"C:\Users\24adi\OneDrive\Desktop\for yoga\Yoga_Trainer\dataset"
data_dir = pathlib.Path(data_dir)
print(f"The database DIR : {data_dir}")


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


str(yoga_poses_img_dict['tree'][0])
img = cv2.imread(str(yoga_poses_img_dict['tree'][0]))

print(f"Initial Img SHAPE : {img.shape}") #image real shape

print(f"Updated Img SHAPE : {cv2.resize(img,(224,224)).shape}")  #changing the img to correct shape

X = []
y = []

#giving pose_names the pose and corrosponding img
for pose_name, images in yoga_poses_img_dict.items():
    for image in images:
        img = cv2.imread(str(image))
        
        if img is None:
            print(f"Corrupted image skipped: {image}")
            continue  # Skip the label as well by not appending it
        
        try:
            resized_img = cv2.resize(img, IMAGE_SHAPE)
            X.append(resized_img)
            y.append(yoga_poses_lab_dict[pose_name])
        except Exception as e:
            print(f"Error processing image {image}: {e}")
            continue  # Skip the label if there's an error resizing

print(f"after skiping the curropt files : {len(X)}")
print(f"after skiping the curropt files : {len(y)}")
X = np.array(X) #list of images to arrays
y = np.array(y) #list of labels to arrays

#spliting the data into training and test data and yet the range of pixel values remains from 0 - 255
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train_scaled = X_train / 255 #normilization
X_test_scaled = X_test / 255

print(f"shape os img in x list : {X[0].shape}")
print(IMAGE_SHAPE+(3,))

x0_resized = X[0]
x1_resized = X[1]
x2_resized = X[8]

print(f"shape os img in x list resized : {(x0_resized.shape)}")

plt.axis('off')
plt.imshow(X[8])
plt.show()

predicted = classifier.predict(np.array([x2_resized]))
predicted_label_index = np.argmax(predicted, axis=1)
print(f"Predicted index : {predicted_label_index}")



image_labels = []
with open("gitfiles/labs.txt", "r") as f:
    image_labels = f.read().splitlines() 

image_label = image_labels[predicted_label_index[0]]

print(f"Predicted index : {predicted_label_index} and Label : {image_label}")
