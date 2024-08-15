import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# To move an image
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

#To rotate an image
rotated = imutils.rotate(image, 90)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

# To resize an image
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r)) # (Width, Height)
# Interplotation is the algorithim behind the scenes
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# Using imutils to resize the image
resized = imutils.resize(image, height = 50) # width also works
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)