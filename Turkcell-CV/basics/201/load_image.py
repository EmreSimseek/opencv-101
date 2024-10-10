import cv2 as cv

path = "E:/Opencv/OpenCV-101/images/"
img = cv.imread(path + "zoo.jpg")   #1 Resim dosya adresi verildi

print(type(img))
if img is None:
    print(f"Resim dosyası yüklenemedi: {path}")
else:
    cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE) #Pencere oluşturuldu
    cv.imshow('opencv_test', img) #Gösterildi ve bir alt satırda süresi belirlendi
    cv.waitKey(0)  # Sonsuz bekleme, pencereyi kapatmak için bir tuşa basılmalı

cv.destroyAllWindows()