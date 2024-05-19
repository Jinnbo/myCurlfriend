from backend.poseDetection import PoseModule as pm
import time
import numpy as np
import cv2
from backend.poseDetection import data_organizer as da
from backend.ai_voice import audio_player
import threading 


cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
startTime = time.time()
pathname = "curl_angle_count.txt"

with open(pathname, "w") as f:
    f.write("angle,count,time,delta,change\n")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("assets/curl.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)

    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # # Left Arm
        # angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))
        # print(angle, per)
        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        changed = da.writeToFile(pathname, angle, count, startTime,"bicep")
        
        if changed:
            # audio_player.playAudio()
            print("WE ARE TRYING TO START THREAD AND PLAY AUDIO")
            audio_thread = threading.Thread(target=audio_player.playAudio())
            audio_thread.start()


        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN,
                    4, color, 4)
        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN,
                    15, (255, 0, 0), 25)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
