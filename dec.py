import numpy as np
import mediapipe as mp
from time import time
import matplotlib.pyplot as plt
import math
import cv2

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(static_image_mode = True, min_detection_confidence = 0.3, model_complexity = 2)

print(type(mp_pose))
