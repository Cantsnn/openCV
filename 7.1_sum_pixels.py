import cv2 as cv

locate = "img/aliAtay.jpg"
locate2 = "img/ismailAbi.jpg"


image = cv.imread(locate)
image2 = cv.imread(locate2)

#Ayni boyuttaki resimleri toplama
sum = cv.add(image,image2)

#resimleri agirlikli olarak toplama, belirli bir oranda
weightedSum = cv.addWeighted(image,0.7,image2,0.3,0)

cv.imshow("Toplanmis resim",sum)
cv.imshow("Agirlikli Toplanmis resim",weightedSum)



cv.waitKey(0)
cv.destroyAllWindows()