import mediapipe as mp
import cv2
import time
from auio_conv import audd
from downdog_checks import right_hand_check, left_hand_check, right_leg_check, left_leg_check, right_hip_check , left_hip_check

def instructor_for_downdog_pose(label):

    fixed_label = label

    if fixed_label == "downdog": 

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(min_detection_confidence=0.1, min_tracking_confidence=0.5)

        mp_drawing = mp.solutions.drawing_utils

        cap = cv2.VideoCapture(0)

        capture_interval = 4 #sec
        last_capture_time = time.time()

        if not cap.isOpened():
            print("sorry i didnt see")
            exit()
        
        right_hand_flag =  False
        left_hand_flag = False
        right_leg_flag = False
        left_leg_flag = False
        right_hip_flag = False
        left_hip_flag = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            #image processing according to model
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS) # Draw landmarks

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            current_time = time.time()

            if current_time - last_capture_time >= capture_interval:
                last_capture_time = current_time  # Update the last capture time

                if results.pose_landmarks:

                    # Extract landmarks
                    
                    #right hand
                    lm12 = results.pose_landmarks.landmark[12]
                    lm14 = results.pose_landmarks.landmark[14]
                    lm16 = results.pose_landmarks.landmark[16]
                    
                    #left hand
                    lm11 = results.pose_landmarks.landmark[11]
                    lm13 = results.pose_landmarks.landmark[13]
                    lm15 = results.pose_landmarks.landmark[15]

                    #right leg
                    lm23 = results.pose_landmarks.landmark[23]
                    lm25 = results.pose_landmarks.landmark[25]
                    lm27 = results.pose_landmarks.landmark[27]
                    
                    #left leg
                    lm24 = results.pose_landmarks.landmark[24]
                    lm26 = results.pose_landmarks.landmark[26]
                    lm28 = results.pose_landmarks.landmark[28]
                    

                    if True and not left_hip_flag:
                        statues_of_left_hip = left_hip_check(lm23,lm25,lm27)

                        if statues_of_left_hip and not left_hip_flag :
                                print("🟢🟢🟢🟢🟢🟢")
                                print("left leg is set")
                                left_hip_flag = True
                        else:
                            continue

                    if True and not right_hip_flag:
                        statues_of_right_hip = right_hip_check(lm23,lm25,lm27)

                        if statues_of_right_hip and not right_hip_flag :
                                print("🟢🟢🟢🟢🟢🟢")
                                print("right leg is set")
                                right_hip_flag = True
                        else:
                            continue

                    if right_hip_flag:
                        audd("well done")
                        audd("great work keep up")

                        exit()

            cv2.imshow("Body Points Tracking", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        print("🟡 : yellow is for updates")
        print("🔴 : red is for instructions")
        print("🟢 : green is for correct pose")

