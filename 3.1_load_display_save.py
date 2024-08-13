from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path of the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("length: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv2.imshow("Ïmage", image)
cv2.waitKey(0)

cv2.imwrite("./images/newimage.jpg", image)