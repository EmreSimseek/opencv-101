import cv2 as cv


path="E:/Opencv/OpenCV-101/TCell01/images/"

img = cv.imread(path +"logo.png")
resized_img = cv.resize(img, (800, 600))
cv.namedWindow("image_create", cv.WINDOW_AUTOSIZE)
cv.imshow("image_create", resized_img)
cv.waitKey(1)

h , w, ch = resized_img.shape
print(f"h:{h}, w:{w}, ch:{ch}")

for row in range(h):
    for col in range(w):
        b, g, r = resized_img[row, col]
        if b == 255 and g == 255 and r == 255: #beyazsa siyah yapma işlemi
            b = 255 - b
            g = 255 - g
            r = 255 - r
            resized_img[row, col] = [b, g, r]
        elif b == 0 and g == 0 and r == 0: #beyaz değilse ve siyahsa beyaz yapma işlemi
            b = 255 + b
            g = 255 + g
            r = 255 + r
            resized_img[row, col] = [b, g, r]

cv.imshow("new",resized_img)
cv.waitKey(0)

