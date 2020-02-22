import cv2 
import numpy as np
import time 
from gaze_tracking import GazeTracking 

font = cv2.FONT_HERSHEY_SIMPLEX

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

time_diff = []
left_pupil_list = [(0,0)]
right_pupil_list = [(0,0)]
diff_right = []
diff_left = []


while True:

    _, frame = webcam.read()

    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), font, 0.9, (147, 58, 31), 3)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), font, 0.9, (147, 58, 31), 3)

    left_pupil_list.append(left_pupil)
    right_pupil_list.append(right_pupil)

    diff_left_left = np.abs(left_pupil_list[-1][0] - left_pupil_list[-2][0])
    diff_left_right = np.abs(left_pupil_list[-1][1] - left_pupil_list[-2][1])
    diff_right_left = np.abs(right_pupil_list[-1][0] - right_pupil_list[-2][0])
    diff_right_right = np.abs(right_pupil_list[-1][1] - right_pupil_list[-2][1])

    diff_right.append([diff_right_left,diff_right_right])
    diff_left.append([diff_left_left, diff_left_right])

    cv2.imshow("Demo", frame)

    print(diff_right)

    left_pupil_list = [left_pupil_list[-1]]
    right_pupil_list = [right_pupil_list[-1]]

    if cv2.waitKey(1) == 27:
        break