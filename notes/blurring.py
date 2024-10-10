import cv2

# blur(), GaussianBlur(), medianBlur(), bilateralFilter()

path = "E:/Opencv/OpenCV-101/images/"

img = cv2.imread(path + "nacat.jpg")

k_size = 13
blur_image = cv2.blur(img,(k_size, k_size))
img_gaus_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_median_blur = cv2.medianBlur(img,k_size)

cv2.imshow("img", img)
cv2.imshow("blur_image", blur_image)
cv2.imshow("gaus_blur", img_gaus_blur)
cv2.imshow("median_blur", img_median_blur)
cv2.waitKey(0)