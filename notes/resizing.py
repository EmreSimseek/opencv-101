import  cv2


path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

img = cv2.imread( path +"cats 2.jpg")

print(img.shape)
cv2.imshow("img", img)
cv2.waitKey(1)

resized_img = cv2.resize(img,(300,200))
cv2.imshow("resize", resized_img)
cv2.waitKey(0)
