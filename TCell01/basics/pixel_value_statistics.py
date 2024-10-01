import cv2 as cv
import  numpy as np

path = "E:/Opencv/OpenCV-101/TCell01/images/"

img = cv.imread(path + "logo.png")
cv.imshow("logo", img)
cv.waitKey(1)


#cvtColor
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", img)
cv.waitKey(0)

cv.imwrite(path + "gray_opencv.png", gray) #gray_opencv.png gri resim dosyası olarak klasöre eklendi


cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray", gray_opencv.png)
cv.waitKey(0)