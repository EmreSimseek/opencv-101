import  cv2

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

img = cv2.imread(path + "cats 2.jpg")
print(img.shape)

cropped_img = img[150:350, 250:500]
cv2.imshow("img", img)
cv2.imshow("crop", cropped_img)
cv2.waitKey(0)