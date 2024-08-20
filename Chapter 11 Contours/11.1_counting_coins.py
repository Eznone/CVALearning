import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
image = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred image", image)

edged = cv2.Canny(image, 30, 150)
cv2.imshow("edged image", edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Detected coins", coins)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(coins, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(coins, "#{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Contours", coins)

cv2.waitKey(0)