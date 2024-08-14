import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

# Drawing a green line where green is the BGR of green
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)

# Drawing a red line where green is the BGR of red
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

