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

# Flipping the image
flipped = cv2.flip(image, 1) # To flip verical (0) to flip both (-1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# Cropping the image
cropped = image[30: 120, 240: 335]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

# Creating 2 matrixs of 1' to add and subtract image
M = np.ones(image.shape, dtype = "uint8") * 100
N = np.ones(image.shape, dtype = "uint8") * 50

# Adding to an image to make it brigher
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

# Subtracting from an image to make it darker
subtracted = cv2.subtract(image, N)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

# Setting up for the bitwise operations section
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# Bitwise operations
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

# Masking operation
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY -75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask applied", masked)
cv2.waitKey(0)

# Splitting and mergining images
# Splitting essentially means getting our image into seperate RGB channels
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# Merging individual GBRs to get a solid color
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("RedM", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.imshow("GreenM", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow("BlueM", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

# GrayScale, HSV, and L.A.B colorsets
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)