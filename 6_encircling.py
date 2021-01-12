#Resimde Belli Bölgeyi Dikdörtgen İçine Alma
#Almak istediginiz alanin sol alt ve sag ust köselerini bulmak lazim

import cv2 as cv

locate = "img/hababam.jpg"

image = cv.imread(locate)
#alanin x ve y koordinatlarini veriyoruz. thickness kalinligini ayarlar 0-9 arasi
cv.rectangle(image,(200,100),(300,200),color = [0,0,255],thickness = 3)

cv.imshow("Hababam Sinifi",image)




cv.waitKey(0)
cv.destroyAllWindows()