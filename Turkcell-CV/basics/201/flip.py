import cv2 as cv

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"
img = cv.imread(path + "logo.png")

# Original
cv.imshow("Original", img)
cv.waitKey(1)
# X flip
dst = cv.flip(img,1)
cv.imshow("X-flip", dst)
cv.waitKey(1)

# Y flip
dst = cv.flip(img,0)
cv.imshow("Y-flip", dst)
cv.waitKey(1)

# X-Y flip
dst = cv.flip(img,-1)
cv.imshow("XY-flip", dst)
cv.waitKey(0)