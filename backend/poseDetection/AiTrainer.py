# import PoseModule as pm
# import time
# import numpy as np
# import cv2
# from flask import Flask, Response, render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# def generate_frames():
#     cap = cv2.VideoCapture(1)
#     detector = pm.poseDetector()
#     count = 0
#     dir = 0
#     pTime = 0
#     startTime = time.time()

#     with open("curl_angle_count.txt", "w") as f:
#         f.write("angle,count,time\n")

#     while True:
#         success, img = cap.read()
#         if not success:
#             break
        
#         img = cv2.resize(img, (1280, 720))
#         img = detector.findPose(img, False)
#         lmList = detector.findPosition(img, False)
        
#         if len(lmList) != 0:
#             angle = detector.findAngle(img, 12, 14, 16)
#             per = np.interp(angle, (210, 310), (0, 100))
#             bar = np.interp(angle, (220, 310), (650, 100))
#             color = (255, 0, 255)
#             if per == 100:
#                 color = (0, 255, 0)
#                 if dir == 0:
#                     count += 0.5
#                     dir = 1
#             if per == 0:
#                 color = (0, 255, 0)
#                 if dir == 1:
#                     count += 0.5
#                     dir = 0

#             with open("curl_angle_count.txt", "a") as f:
#                 f.write(f"{angle},{count},{time.time() - startTime}\n")
            
#             cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
#             cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
#             cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)
#             cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)
        
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
        
#         ret, buffer = cv2.imencode('.jpg', img)
#         img = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='5005')

import PoseModule as pm
import time
import numpy as np
import cv2
from flask import Flask, Response, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def generate_frames():
    cap = cv2.VideoCapture(0)
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