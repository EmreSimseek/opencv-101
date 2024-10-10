import cv2 as cv


# Resim yolu
path = "E:/Opencv/OpenCV-101/images/"
src = cv.imread(path + "cats 2.jpg")

# Orijinal görüntü gösterme
cv.imshow("Original Image", src)

### 📌 1. Gürültü Azaltma ve Filtreler

# 1.1 Ortalama Filtre
mean_blur = cv.blur(src, (5, 5))
cv.imshow("Mean Blur (Average Filter)", mean_blur)

# 1.2 Medyan Filtre
median_blur = cv.medianBlur(src, 5)
cv.imshow("Median Blur", median_blur)

# 1.3 Gaussian Filtre
gaussian_blur = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("Gaussian Blur", gaussian_blur)

### 📌 2. Kenar Tespiti ve Gradyanlar

# 2.1 Sobel Kenar Tespiti
sobelx = cv.Sobel(src, cv.CV_64F, 1, 0, ksize=3)  # X yönü
sobely = cv.Sobel(src, cv.CV_64F, 0, 1, ksize=3)  # Y yönü
sobel_combined = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel Combined", sobel_combined)

# 2.2 Laplacian Kenar Tespiti
laplacian = cv.Laplacian(src, cv.CV_64F)
cv.imshow("Laplacian", laplacian)

# 2.3 Canny Kenar Tespiti
canny_edges = cv.Canny(src, 100, 300)
cv.imshow("Canny Edge Detection", canny_edges)

# Çıkış için bekleme
cv.waitKey(0)
cv.destroyAllWindows()
