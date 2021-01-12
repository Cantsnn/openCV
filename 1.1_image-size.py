import cv2 as cv
import numpy as np

locate = "logo.png"

image = cv.imread(locate)
imageGray = cv.imread(locate,0)

cv.imshow("Logo",image)

print(image.size) #Resmin boyutunu verir
print(image.dtype) #Resmin veri tipini gösterir
print(image.shape)#Genişlik,yükseklik ve kanal sayısını verir.
print(imageGray.shape) 

cv.waitKey(0)
cv.destroyAllWindows()