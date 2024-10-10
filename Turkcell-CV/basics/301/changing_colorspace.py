import cv2 as cv

path = "E:/Opencv/OpenCV-101/images/"

# RGB görüntü
img = cv.imread(path +"logo.png")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb",img)
cv.waitKey(1)

# RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(1)

# RGB to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey(0)

cv.destroyAllWindows()

