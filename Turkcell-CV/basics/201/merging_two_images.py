import cv2 as cv
import  numpy as np

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"
img1 = cv.imread(path + "zoo.jpg")
img2 = cv.imread(path + "gray_zoo.png")

cv.imshow("img1",img1) #resim1
cv.waitKey(1)

cv.imshow("img2",img2) #resim2
cv.waitKey(2)

horizontal = np.hstack((img1,img2)) #birleştirilen resim
cv.imshow("merged", horizontal)
cv.waitKey(0)