import numpy as np
import cv2

# Creating a new canvas, making it blank
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Making variables for center of circle
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

white = (255, 255, 255)

# A loop that makes a circle that gets a larger radius each time
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

# To "print" the image of canvas to the screen
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)