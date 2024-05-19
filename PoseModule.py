import cv2
import mediapipe as mp
import time
import math
from abc import ABC, abstractmethod

# Strategy Interface


class AngleCalculationStrategy(ABC):
    @abstractmethod
    def calculate_angle(self, img, lmList):
        pass

    @property
    @abstractmethod
    def key_landmarks(self):
        pass

    @abstractmethod
    def display_data(self, img, lmList, angle_data):
        pass

# Concrete Strategy for Squats


class SquatAngleStrategy(AngleCalculationStrategy):
    def calculate_angle(self, img, lmList):
        p_hip, p_knee, p_ankle, p_shoulder = 23, 25, 27, 11

        x1, y1 = lmList[p_hip][1], lmList[p_hip][2]
        x2, y2 = lmList[p_knee][1], lmList[p_knee][2]
        x3, y3 = lmList[p_ankle][1], lmList[p_ankle][2]
        leg_angle = math.degrees(math.atan2(
            y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if leg_angle < 0:
            leg_angle += 360

        x4, y4 = lmList[p_shoulder][1], lmList[p_shoulder][2]
        upper_body_angle = math.degrees(math.atan2(
            y2 - y1, x2 - x1) - math.atan2(y4 - y1, x4 - x1))
        if upper_body_angle < 0:
            upper_body_angle += 360

        return leg_angle, upper_body_angle

    @property
    def key_landmarks(self):
        return [11, 23, 25, 27]

    def display_data(self, img, lmList, angle_data):
        leg_angle, upper_body_angle = angle_data

        landmark_dict = {landmark[0]: landmark[1:] for landmark in lmList}

        last_coord = None
        for id in self.key_landmarks:
            if id in landmark_dict:
                cx, cy = landmark_dict[id]
                cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), 2)
                angle = leg_angle if id != 11 else upper_body_angle

                if last_coord:
                    cv2.line(img, last_coord, (cx, cy), (0, 255, 0), 2)
                last_coord = (cx, cy)

        cv2.putText(img, f"Leg Angle: {int(leg_angle)} degrees",
                    (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        cv2.putText(img, f"Upper Body Angle: {int(upper_body_angle)} degrees",
                    (50, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

# Concrete Strategy for Push-ups


class PushUpAngleStrategy(AngleCalculationStrategy):
    def calculate_angle(self, img, lmList):
        p_shoulder, p_elbow, p_wrist, p_hip, p_ankle = 12, 14, 16, 24, 28

        x1, y1 = lmList[p_shoulder][1], lmList[p_shoulder][2]
        x2, y2 = lmList[p_elbow][1], lmList[p_elbow][2]
        x3, y3 = lmList[p_wrist][1], lmList[p_wrist][2]

        arm_angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                 math.atan2(y1 - y2, x1 - x2))
        if arm_angle < 0:
            arm_angle += 360

        x4, y4 = lmList[p_shoulder][1], lmList[p_shoulder][2]
        x5, y5 = lmList[p_hip][1], lmList[p_hip][2]
        x6, y6 = lmList[p_ankle][1], lmList[p_ankle][2]

        body_angle = math.degrees(math.atan2(
            y6 - y5, x6 - x5) - math.atan2(y4 - y5, x4 - x5))

        if body_angle < 0:
            body_angle += 360

        return arm_angle, body_angle

    @property
    def key_landmarks(self):
        return [14, 16, 12, 24, 26, 28, 32]

    def display_data(self, img, lmList, angle_data):
        arm_angle, body_angle = angle_data

        last_coord = None
        for id, cx, cy in lmList:
            if id in self.key_landmarks:
                cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), 2)
                if last_coord:
                    cv2.line(img, last_coord, (cx, cy), (0, 255, 0), 2)
                last_coord = (cx, cy)

        cv2.putText(img, f"Arm Angle: {int(arm_angle)} degrees",
                    (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        cv2.putText(img, f"Body Angle: {int(body_angle)} degrees",
                    (50, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)


class CurlAngleStrategy(AngleCalculationStrategy):
    def calculate_angle(self, img, lmList):

        p1, p2, p3 = 12, 14, 16  # arm landmarks

        # Extract landmark coordinates
        x1, y1 = lmList[p1][1], lmList[p1][2]
        x2, y2 = lmList[p2][1], lmList[p2][2]
        x3, y3 = lmList[p3][1], lmList[p3][2]

        # Calculate the angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        return (angle,angle)

    @property
    def key_landmarks(self):
        return [12, 14, 16]

    def display_data(self, img, lmList, angle_data):
        last_coord = None
        key_landmarks = self.key_landmarks
        for idx, (id, cx, cy) in enumerate(lmList):
            if id in key_landmarks:
                cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), 2)

                if last_coord:
                    cv2.line(img, last_coord, (cx, cy), (0, 255, 0), 2)
                last_coord = (cx, cy)

        cv2.putText(img, f"Arm Angle: {int(angle_data[0])} degrees",
                    (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

class poseDetector():

    def __init__(self, strategy="curl", mode=False, complexity=1, smooth=True, seg=False, smooth_seg=False, detectionCon=0.5, trackCon=0.5):
        self.strategy = strategy
        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.seg = seg
        self.smooth_seg = smooth_seg
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth,
                                     self.seg, self.smooth_seg, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, lmList):
        if self.strategy:
            return self.strategy.calculate_angle(img, lmList)
