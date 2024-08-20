import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred image", image)

canny = cv2.Canny(image, 50, 150)
cv2.imshow("Canny edges", canny)
cv2.waitKey(0)