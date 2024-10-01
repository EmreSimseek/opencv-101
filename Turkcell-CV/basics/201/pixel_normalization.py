import cv2 as cv
import  numpy as np


path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

img = cv.imread(path + "logo.png")
cv.imshow("logo", img)
cv.waitKey(1)


gray_opencv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray_opencv)
cv.waitKey(1)
print(gray_opencv.shape)
print(gray_opencv)

gray_opencv = np.float32(gray_opencv)
print(gray_opencv)

# NORM_MINMAX

dst = np.zeros(gray_opencv.shape, dtype=np.float32)
cv.normalize(gray_opencv, dst=dst, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
print(dst)

print(np.uint8(dst*255))
means, stddev = cv.meanStdDev(np.uint8(dst*255))
print("mean: %.2f , stddev: %.2f" % (means, stddev))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min value: %.2f, max value: %.2f" %(min_value,max_value))

# NORM_INF

dst = np.zeros(gray_opencv.shape, dtype=np.float32)
cv.normalize(gray_opencv, dst=dst, alpha=1, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(1)

# NORM_L1

dst = np.zeros(gray_opencv.shape, dtype=np.float32)
cv.normalize(gray_opencv, dst=dst, alpha=1, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(0)

