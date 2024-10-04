import cv2
import numpy as np

path = "E:/Opencv/OpenCV-101/Turkcell-CV/images/"

# İkili görüntü (binary image) oluştur
img = cv2.imread(path + "cats 2.jpg", 0)  #0 Gray #1 BGR #-1 Original
kernel = np.ones((5,5), np.uint8)

cv2.imshow("Input image", img)
cv2.waitKey(1)
# Erozyon uygulama
eroded = cv2.erode(img,kernel,iterations=1)

cv2.imshow("Eroded Image", eroded)
cv2.waitKey(1)


# Genleşme
dilated = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilated Image", eroded)
cv2.waitKey(1)


# Açılma (Opening) İşlemi : (failed) erozyon + genleşme
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening Image", opening)
cv2.waitKey(1)


# Kapanma (Closing)  genleşme + erozyon
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing Image", closing)
cv2.waitKey(1)


# Morfolojik Gradyan işlemi
# görüntünün genleşmesi ve erozyonu arasındaki farktır. Nesnelerin kenarlarını çıkarmak için kullanılır.
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient Image", gradient)
cv2.waitKey(1)


#Top Hat işlemi
#aydınlık bölgeleri çıkarmak için kullanılır.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Top Hat Image', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Black Hat işlemi
# koyu bölgeleri çıkarmak için kullanılır.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('Black Hat Image', blackhat)
cv2.waitKey(1)
