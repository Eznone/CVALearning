import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

black = (0, 0 ,0)
red = (0, 0, 255)

colorList = [black, red]

for y in range(30):
    for x in range(30):
        cv2.rectangle(canvas, (x*10, y*10), ((x*10)+10, (y*10)+10), colorList[(x + y) % 2], -1)

cv2.circle(canvas, (150, 150), 50, (0, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)