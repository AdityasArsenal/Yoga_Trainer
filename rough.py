mp_pose = mp.solutions.pose

pose = mp_pose.Pose(static_image_mode = True, min_detection_confidence = 0.3, model_complexity = 2)

print(type(mp_pose))

mp_drawing = mp.solutions.drawing_utils

smpl = cv2.imread('download.jpg')
plt.figure(figsize=[10,10])
plt.axis('off')
plt.imshow(smpl[:,:,::-1])
plt.show()