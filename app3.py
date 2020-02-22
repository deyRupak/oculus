
import cv2
import matplotlib.pyplot as plt
import datetime
from gaze_tracking import GazeTracking
import seaborn as sns

sns.set(style="ticks", context="talk")
plt.style.use("dark_background")

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    if(left_pupil == (0,0) or right_pupil == (0,0)):
        pass
    else:
        plt.plot(left_pupil, right_pupil)
        

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == ord(' '):
        break

plt.savefig(str(datetime.datetime.now()) + '.png')