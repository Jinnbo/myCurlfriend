import PoseModule as pm
import time
import numpy as np
import cv2
from flask import Flask, Response, render_template, jsonify, request
from flask_cors import CORS
from backend.poseDetection import data_organizer as da
from backend.ai_voice import audio_player
import threading 
import random

app = Flask(__name__)
CORS(app)

current_strategy = pm.PushUpAngleStrategy()
pathname = "curl_angle_count.txt"

startTime = time.time()

with open(pathname, "w") as f:
    f.write("bugtest,angle,count,time,delta,change,struggling,halfrep\n")

@app.route('/api/adjust-strategy', methods=['POST'])
def adjust_strategy():
    data = request.json
    strategy_name = data.get('field')
    global current_strategy

    if strategy_name == "pushup":
        current_strategy = pm.PushUpAngleStrategy()
    elif strategy_name == "squat":
        current_strategy = pm.SquatAngleStrategy()
    elif strategy_name == "curl":
        current_strategy = pm.CurlAngleStrategy()
    else:
        return jsonify(status="error", message="Invalid strategy name"), 400

    return jsonify(status="success", message=f"Strategy changed to {strategy_name}"), 200


def generate_frames():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()

    # determine strategy?
    # strategy = pm.CurlAngleStrategy()
    # strategy = pm.SquatAngleStrategy()

    # strategy = pm.PushUpAngleStrategy()
    detector = pm.poseDetector(strategy=current_strategy)
    dir = 0
    count = 0
    while True:
        success, img = cap.read()
        if not success:
            break

        detector.strategy = current_strategy
        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        


        if len(lmList) != 0:
            angle_data = detector.findAngle(img, lmList)
            detector.strategy.display_data(img, lmList, angle_data)
            # # Left Arm
            # angle = detector.findAngle(img, 11, 13, 15,False)
            per = np.interp(angle_data[0], (210, 310), (0, 100))
            # print(angle, per)
            # Check for the dumbbell curls
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            changed, struggling, halfrep = da.writeToFile(pathname, angle_data[0], count, startTime,"bicep")
        
            if changed:
                # audio_player.playAudio()
                print("WE ARE TRYING TO START THREAD AND PLAY AUDIO")
                newrepaudio = random.choice(["newrep1","newrep2","newrep3"])

                audio_thread = threading.Thread(target=audio_player.playAudio, args=(newrepaudio,))
                audio_thread.start()
            
            elif struggling:
                print("YOU ARE STRUGGLING RIGHT NOW.")
                audio_thread = threading.Thread(target=audio_player.playAudio, args=("encouragement",))
                audio_thread.start()
            
            elif halfrep:
                halfrepaudio = random.choice(["halfrep"])
                audio_thread = threading.Thread(target=audio_player.playAudio, args=(halfrepaudio,))
                audio_thread.start()

        ret, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')
