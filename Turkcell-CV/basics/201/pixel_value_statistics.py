import cv2 as cv
import  numpy as np

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

#opencv logo
img = cv.imread(path + "logo.png")
cv.imshow("logo", img)
cv.waitKey(1)


#cvtColor
gray_opencv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite(path + "gray_opencv.png", gray_opencv) #gray_opencv.png gri resim dosyası olarak klasöre eklendi

#gray_opencv oluşturuldu
cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray", gray_opencv)
cv.waitKey(1)

#minMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray_opencv)
print("min value: %.2f, max value: %.2f" %(min_value,max_value))

print(f"min loc:{min_loc}, max loc:", max_loc)

#meanStdDev
means, stddev = cv.meanStdDev(gray_opencv)
print("mean: %.2f, stddev: %.2f" % (means,stddev))

gray_opencv[np.where(gray_opencv < means)] = 0
gray_opencv[np.where(gray_opencv > means)] = 255

cv.imshow("white_and_black", gray_opencv)
cv.waitKey(0)
