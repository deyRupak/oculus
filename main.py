from flask import Flask, render_template
import pickle

import time
import multiprocessing

import cv2
import matplotlib.pyplot as plt
import datetime
import fastai 
from fastai.vision import *
import os
from gaze_tracking import GazeTracking
import seaborn as sns


app = Flask(__name__)


def ValuePredictor(img_to_check):

    path = Path("./model/")
    learn = load_learner(path)
    pred_class,pred_idx,outputs = learn.predict(img_to_check)

    return str(pred_class)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def test():
    return render_template("takeTest.html")


@app.route("/dyslexia")
def dyslexia():
    return render_template("./test/dyslexia.html")


@app.route("/adhd")
def adhd():
    return render_template("./test/adhd.html")

@app.route("/adhdRes")
def adhdRes():

    #app3 code
    # p = multiprocessing.Process(target = ValuePredictor, name="valuePredictor", args=())
    # p.start()
    # time.sleep(10)
    # p.terminate()

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
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        if(left_pupil == (0, 0) or right_pupil == (0, 0)):
            pass
        else:
            plt.plot(left_pupil, right_pupil)

        cv2.imshow("Demo", frame)

        if cv2.waitKey(1) == ord(' '):
            break

    plt.savefig('2.png')

    img = open_image('./2.png')
    result = ValuePredictor(img)
    if result == 'ASD':
        prediction = "ADHD"
    else:
        prediction = "No ADHD"
    return render_template("./test/adhd.html", prediction = prediction)


@app.route("/autism")
def autism():
    return render_template("./test/autism.html")

@app.route("/autismRes")
def autismRes():

    #app3 code
    # p = multiprocessing.Process(target = ValuePredictor, name="valuePredictor", args=())
    # p.start()
    # time.sleep(10)
    # p.terminate()
    
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
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        if(left_pupil == (0, 0) or right_pupil == (0, 0)):
            pass
        else:
            plt.plot(left_pupil, right_pupil)

        cv2.imshow("Demo", frame)

        if cv2.waitKey(1) == ord(' '):
            break

    plt.savefig('1.png')

    img = open_image('./1.png')
    result = ValuePredictor(img)
    if result != 'ASD':
        prediction = "Autistic"
    else:
        prediction = "Not Autistic"
    return render_template("./test/autism.html", prediction = prediction)


    

if __name__ == "__main__":
    app.run(debug=False)
    # We made two new changes
