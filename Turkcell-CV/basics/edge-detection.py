import cv2 as cv

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"
image = cv.imread(path + "cats 2.jpg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# 5x5 kernel oluşturma
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# Açılma işlemi
opened = cv.morphologyEx(gray_image, cv.MORPH_OPEN, kernel)

# Kapanma işlemi
closed = cv.morphologyEx(opened, cv.MORPH_CLOSE, kernel)

cv.imshow("Noise Removed Image", closed)
cv.waitKey(1)

gradient = cv.morphologyEx(closed, cv.MORPH_GRADIENT, kernel)
cv.imshow("Edge detected Image", gradient)
cv.waitKey(0)
cv.destroyAllWindows()
