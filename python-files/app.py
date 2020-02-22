import cv2 
import numpy as np
import time 
from gaze_tracking import GazeTracking 

font = cv2.FONT_HERSHEY_SIMPLEX

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

time_diff = []


while True:

    _, frame = webcam.read()

    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    new_frame = np.zeros((1200,2000,3), np.uint8)
    new_frame[:] = (0, 0, 0)

    
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), font, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), font, 0.9, (147, 58, 31), 1)

    initial_time = time.time()
    if ((left_pupil == None) or (right_pupil == None)):
        initial_left_pupil = (0, 0, 0, 0)
        initial_right_pupil = (0, 0, 0, 0)
    else:
        initial_left_pupil = left_pupil
        initial_right_pupil = right_pupil


    
    while ( (left_pupil != None) or (right_pupil != None)):
        if((np.abs(right_pupil[0] - initial_right_pupil[0]) > 2) or (np.abs(left_pupil[0] - initial_left_pupil[0]) >= 2)):
            diff = time.time - initial_time()
            time_diff.append(diff)
            print(left_pupil, right_pupil, diff)
            cv2.putText(frame, "Time: " + str(diff), (180, 165), font, 0.9, (147, 58, 31), 3)

    


    #print(left_pupil, right_pupil, time_diff[-1])
    print(initial_left_pupil[0], initial_left_pupil[1], initial_left_pupil[3], initial_left_pupil[3])
    
    cv2.imshow("Demo", frame)
    cv2.imshow("Reading Area", new_frame)

    if cv2.waitKey(1) == 27:    
        break