import  cv2

path = "E:/Opencv/OpenCV-101/images/"

img = cv2.imread(path + "nacat.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,4)
ret, simple_thresh = cv2.threshold(img_gray,150, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("thresh", adaptive_thresh)
cv2.imshow("simple_thresh", simple_thresh)
cv2.waitKey(0)