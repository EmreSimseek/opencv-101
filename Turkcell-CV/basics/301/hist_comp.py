import cv2 as cv

path ="E:/Opencv/OpenCV-101/images/"

src1 = cv.imread(path + "garden.jpg")
src2 = cv.imread(path + "miuul.png")
src3 = cv.imread(path + "zoo.jpg")

# cvtColor
hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist
hist1 = cv.calcHist([hsv1], [0,1], None, [60,64], [0,180,0,255])
hist2 = cv.calcHist([hsv2], [0,1], None, [60,64], [0,180,0,255])
hist3 = cv.calcHist([hsv3], [0,1], None, [60,64], [0,180,0,255])

# normalize
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)