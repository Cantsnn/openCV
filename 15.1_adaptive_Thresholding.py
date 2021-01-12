import cv2 as cv

locate = "img/23nisan.jpeg"

image = cv.imread(locate,0) #gri tonlama uzerinden islem yapilir
image = cv.blur(image,(3,3)) #daha net goruntu elde etmek icin blurluyoruz

#simple thresholding
ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)

#adaptive thresholding
thresh2 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
thresh3 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

cv.imshow("Orjinal",image)
cv.imshow("Simple Thresh",thresh1)
cv.imshow("Adaptive Thresh Mean",thresh2)
cv.imshow("Adaptive Thresh Gauss",thresh3)


cv.waitKey(0)
cv.destroyAllWindows()