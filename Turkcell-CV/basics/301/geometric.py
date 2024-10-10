import cv2 as cv
import  numpy as np

#shifting

path = "E:/Opencv/OpenCV-101/images/"
img = cv.imread(path +"logo.png")

rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1, 0, 200], [0, 1, 90]])

shifted = cv.warpAffine(img, M, (cols, rows)) # kaynak resim belirtilen matrise çevirmek

cv.imshow("original",img)
cv.waitKey(1)

cv.imshow("shifted",shifted)
cv.waitKey(1)

#rotation

M = cv.getRotationMatrix2D((cols/2,rows/2),-90,1)
dst = cv.warpAffine(img , M, (cols, rows))

cv.imshow("rotated_image",dst)
cv.waitKey(1)

#scaling

res = cv.resize(img,None, fx=0.8, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow("scaling", res)
cv.waitKey(0)