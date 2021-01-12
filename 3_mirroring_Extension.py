import cv2 as cv


locate = "img/adilenasit.jpg"

image = cv.imread(locate)
#Aynalama işlemi, BORDER_REFLECT bu işi yapar
mirror = cv.copyMakeBorder(image,50,75,350,325,cv.BORDER_REFLECT)

#uzatma islemleri
extension = cv.copyMakeBorder(image,120,120,200,200,cv.BORDER_REPLICATE)

#Tekrarlama islemi
repeated = cv.copyMakeBorder(image,120,120,320,320,cv.BORDER_WRAP)

#Sarma islemi , value ile renk ayarları verilebilir. default siyah olur
wrapping = cv.copyMakeBorder(image,120,120,120,120,cv.BORDER_CONSTANT)

cv.imshow("Aynalanan Resim",mirror)
cv.imshow("Uzatilan Resim",extension)
cv.imshow("Tekrarlanan Resim",repeated)
cv.imshow("Sarilan Resim",wrapping)



cv.waitKey(0)
cv.destroyAllWindows()