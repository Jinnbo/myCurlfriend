import cv2
import mediapipe as mp
import time
import math
import numpy as np

# Creating Angle finder class
class angleFinder:
    def __init__(self, lmlist, p1, p2, p3, p4, p5, p6, drawPoints):
        self.lmlist = lmlist
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.drawPoints = drawPoints

    # finding angles
    def angle(self):
        if len(self.lmlist) != 0:
            point1 = self.lmlist[self.p1]
            point2 = self.lmlist[self.p2]
            point3 = self.lmlist[self.p3]
            point4 = self.lmlist[self.p4]
            point5 = self.lmlist[self.p5]
            point6 = self.lmlist[self.p6]

            print(f"point1: {point1}")
            print(f"point2: {point2}")
            print(f"point3: {point3}")
            print(f"point4: {point4}")
            print(f"point5: {point5}")
            print(f"point6: {point6}")

            if len(point1) >= 2 and len(point2) >= 2 and len(point3) >= 2 and len(point4) >= 2 and len(point5) >= 2 and len(
                    point6) >= 2:
                x1, y1 = point1[:2]
                x2, y2 = point2[:2]
                x3, y3 = point3[:2]
                x4, y4 = point4[:2]
                x5, y5 = point5[:2]
                x6, y6 = point6[:2]

                # calculating angle for left and right hands
                leftHandAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                rightHandAngle = math.degrees(math.atan2(y6 - y5, x6 - x5) - math.atan2(y4 - y5, x4 - x5))

                leftHandAngle = int(np.interp(leftHandAngle, [-170, 180], [100, 0]))
                rightHandAngle = int(np.interp(rightHandAngle, [-50, 20], [100, 0]))

                # drawing circles and lines on selected points
                if self.drawPoints:
                    cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                    cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                    cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)
                    cv2.circle(img, (x4, y4), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x4, y4), 15, (0, 255, 0), 6)
                    cv2.circle(img, (x5, y5), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x5, y5), 15, (0, 255, 0), 6)
                    cv2.circle(img, (x6, y6), 10, (0, 255, 255), 5)
                    cv2.circle(img, (x6, y6), 15, (0, 255, 0), 6)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)
                    cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 4)
                    cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 4)
                    cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 4)

                return [leftHandAngle, rightHandAngle]