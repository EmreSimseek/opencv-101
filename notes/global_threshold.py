import  cv2

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

img = cv2.imread(path + "nacat.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)