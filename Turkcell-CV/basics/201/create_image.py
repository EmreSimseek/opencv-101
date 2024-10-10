import cv2 as cv
import numpy as np

path="E:/Opencv/OpenCV-101/images/"

img = cv.imread(path +"zoo.jpg")
cv.namedWindow("image_create", cv.WINDOW_AUTOSIZE)
cv.imshow("image_create", img)
cv.waitKey(1)


m1 = np.copy(img)
m2 = img

type(img)

cv.destroyAllWindows()
# Resmin belirli bir bölgesi siyah renk ile değiştirme
img[100:200, 200:300, :] = 0
cv.imshow("m2",m2)
cv.waitKey(1)

m3=np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1)

m4 = np.zeros([512,512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1)

m5 = np.zeros([512,512],np.uint8)
m5[:,:]= 127
cv.imshow("m5", m5)
cv.waitKey(0)


