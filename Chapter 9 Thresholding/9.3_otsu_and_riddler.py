import numpy as np
import cv2
import argparse
import mahotas

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's thresholding: {}".format(T))