import  cv2


path = "E:/Opencv/OpenCV-101/images/"

img = cv2.imread(path + "garden.jpg")

resized_img = cv2.resize(img, (500,500))
cv2.imshow("img", resized_img)


img_rgb = cv2.cvtColor(resized_img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(resized_img,cv2.COLOR_BGR2HSV)

cv2.imshow("img_hsv", img_hsv)
cv2.imshow("img_rgb", img_rgb)
cv2.imshow("img_gray", img_gray)
cv2.waitKey(0)