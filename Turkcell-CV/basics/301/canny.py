import  cv2 as cv

path ="E:/Opencv/OpenCV-101/Turkcell-CV/images/"

src = cv.imread(path + "cats 2.jpg")
cv.imshow("cat", src)
cv.waitKey(1)

edge = cv.Canny(src, 100, 300)
cv.imshow("edge", edge)
cv.waitKey(0)