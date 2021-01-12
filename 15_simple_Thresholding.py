import cv2 as cv


locate = "img/23nisan.jpeg"

image = cv.imread(locate,0) #gri tonlama uzerinden islem yapilir

 #simple threshold, her piksel icin ayni esik degeri kullanilir
 #esik degerini 127 yaptik altinda kalanlar 0 , uzerinde kalanlar 255 olacak
ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(image,127,255,cv.THRESH_BINARY_INV) #tersini ceviriyor
ret,thresh3 = cv.threshold(image,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(image,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)


cv.imshow("Orjinal",image)
cv.imshow("Simple Thresh1",thresh1)
cv.imshow("Simple Thresh2",thresh2)
cv.imshow("Simple Thresh3",thresh3)
cv.imshow("Simple Thresh4",thresh4)
cv.imshow("Simple Thresh5",thresh5)


cv.waitKey(0)
cv.destroyAllWindows()