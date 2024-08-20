import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Average Blurring
blurred = np.hstack([
cv2.blur(image, (3, 3)),
cv2.blur(image, (5, 5)),
cv2.blur(image, (7, 7))])

cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# Weighted Blurring
# Similar to Average but neighboring pixels are weighted more
blurred = np.hstack([
cv2.GaussianBlur(image, (3, 3), 0),
cv2.GaussianBlur(image, (5, 5), 0),
cv2.GaussianBlur(image, (7, 7), 0)])

cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# Median Blurring
# Similar to the other two but removes what looks like motion blur
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])

cv2.imshow("Median", blurred)
cv2.waitKey(0)

# Bilateral blurring
# It reduced noise while maintaing edges using two Gaussian distrubutions

blurred = np.hstack([
    cv2.bilateralFilter(image, 3, 21, 21), 
    cv2.bilateralFilter(image, 5, 31, 31), 
    cv2.bilateralFilter(image, 7, 41, 41)])

cv2.imshow("BiLateral", blurred)
cv2.waitKey(0)