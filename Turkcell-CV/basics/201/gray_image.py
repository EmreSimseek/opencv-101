import cv2 as cv

path = "E:/Opencv/OpenCV-101/images/"

img = cv.imread(path + "zoo.jpg")
#img = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE) direkt olarak gri skala göstermek
if img is None:
    print(f"Resim dosyası yüklenemedi: {path}")
else:
    cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)
    cv.imshow('opencv_test', img)
    cv.waitKey(1500)

#cvtColor
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(100)

#imwrite
cv.imwrite(path + "gray_zoo.png", gray) #gray_opencv.png gri resim dosyası olarak klasöre eklendi
cv.destroyAllWindows()

img = cv.imread(path + "zoo.jpg", cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img)
cv.waitKey(0)