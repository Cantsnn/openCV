import cv2 as cv

locate = "img/23nisan.jpeg"

image = cv.imread(locate,0) #gri tonlama uzerinden islem yapilir


#simple thresholding
ret1,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)

#otsu, esik degeri belirleme zorunlulugunu kaldirir. kendi otomatik secer
#min ve max degerleri veriyoruz
ret2,thresh2 = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#otsu thresholding after Gaussian filtering
blur = cv.GaussianBlur(image,(5,5),0)
ret3,thresh3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("Orjinal",image)
cv.imshow("Simple Thresh",thresh1)
cv.imshow("Otsu Thresh",thresh2)
cv.imshow("Otsu Thresh Gauss",thresh3)


cv.waitKey(0)
cv.destroyAllWindows()