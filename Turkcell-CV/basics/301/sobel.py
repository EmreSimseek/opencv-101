import  cv2 as cv


path ="E:/Opencv/OpenCV-101/Turkcell-CV/images/"

src = cv.imread(path + "cats 2.jpg")

h ,w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad", x_grad)
cv.imshow("y_grad", y_grad)
cv.waitKey(1)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("gradient", dst)
cv.waitKey(0)