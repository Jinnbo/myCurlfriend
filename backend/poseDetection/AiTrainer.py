import PoseModule as pm
import time
import numpy as np
import cv2
from flask import Flask, Response, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def generate_frames():
    cap = cv2.VideoCapture(1)
    detector = pm.poseDetector()

    # determine strategy?
    # strategy = pm.CurlAngleStrategy()
    # strategy = pm.SquatAngleStrategy()
    strategy = pm.PushUpAngleStrategy()
    detector = pm.poseDetector(strategy=strategy)

    while True:
        success, img = cap.read()
        if not success:
            break
        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        if len(lmList) != 0:
            angle_data = detector.findAngle(img, lmList)
            detector.strategy.display_data(img, lmList, angle_data)

        ret, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')
