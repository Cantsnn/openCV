import cv2 as cv


locate = "23nisan.jpeg"

image = cv.imread(locate)
#Resmin belirli bir alanını alma
kesit = image[160:460,165:465]
kesit[:,:,2]=255

#Aldigimiz alanı resmin belirli bir yerine koyma
image[0:300,0:300] = kesit

#efekt ekleme
image[:,:,0] = 255

cv.imshow("Resim",image)



cv.waitKey(0)
cv.destroyAllWindows()