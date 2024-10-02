import cv2 as cv

path ="E:/Opencv/OpenCV-101/Turkcell-CV/images/"
src = cv.imread(path + "logo.png")

h, w = src.shape[:2]

img = src.copy()

roi = img[90:150, 20:200, :]

print(roi.shape[:2])
cv.imshow("roi", roi)
cv.waitKey(1)

img[0:60, 0:180, :] = roi
cv.imshow("img",img)
cv.waitKey(1)

res = cv.resize(roi, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(1)

img[0:18, 0:54, :] = res
cv.imshow("img", img)
cv.waitKey(0)