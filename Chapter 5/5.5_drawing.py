import numpy as np
import cv2

# Creating a new canvas, making it blank
canvas = np.zeros((300, 300, 3), dtype = "uint8")


for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()

    pt = np.random.randint(0, high = 300, size = (2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

# To "print" the image of canvas to the screen
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)