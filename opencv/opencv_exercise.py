#d3xt3r0
"""
	Run using python opencv_exercise.py filename.jpg
"""

import cv2
import sys
import numpy as np

pic = sys.argv[1]

frame = cv2.imread(pic)
frame = cv2.resize(frame,(400,400))
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_boundary = np.array([0, 40, 30], dtype="uint8")
upper_boundary = np.array([43, 255, 254], dtype="uint8")
skin_mask = cv2.inRange(frame, lower_boundary, upper_boundary)

frame_skin = cv2.bitwise_and(frame, frame, mask=skin_mask)
frame = cv2.addWeighted(frame, 1.5, frame_skin, -0.5, 0)
frame_skin = cv2.bitwise_and(frame, frame, mask=skin_mask)

cv2.imshow("Skin",frame_skin)
cv2.waitKey()
