import cv2 as cv

path = "E:/Opencv/TCell01/"
img = cv.imread(path + "zoo.jpg")


if img is None:
    print(f"Resim dosyası yüklenemedi: {path}")
else:
    cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)
    cv.imshow('opencv_test', img)
    cv.waitKey(0)  # Sonsuz bekleme, pencereyi kapatmak için bir tuşa basılmalı