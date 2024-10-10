import  cv2 as cv
import numpy as np
path = "E:/Opencv/OpenCV-101/images/"
src = cv.imread(path + "zoo.jpg")
src_resized = cv.resize(src, (400, 600))
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src_resized)
cv.waitKey(1)
h, w = src_resized.shape[:2]

dst = cv.bilateralFilter(src_resized, 0, 50, 10)

result = np.zeros([h, w * 2, 3], dtype=src_resized.dtype)
result[0:h, 0:w, :] = src_resized
result[0:h, w:2 * w, :] = dst

cv.imshow("result", result)
cv.waitKey(0)

