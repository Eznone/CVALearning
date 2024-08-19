from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)
cv2.waitKey(0)

# Creating Histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitkey(0)

