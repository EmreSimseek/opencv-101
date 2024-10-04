import cv2 as cv
import numpy as np


path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

img = cv.imread(path + "cats 2.jpg")

h, w = img.shape[:2]
dst = cv.edgePreservingFilter(img, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)

result = np.zeros([h, w*2, 3], dtype=img.dtype)
result[0:h, 0:w, :] = img
result[0:h, w:2*w, :] = dst

cv.imshow("result", result)
cv.waitKey(0)
