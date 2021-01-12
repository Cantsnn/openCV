import cv2 as cv

locate = "img/NataliePortman.jpg"

image = cv.imread(locate)

#Orjinaline ihtiyaç yoksa direk bu sekilde okutabiliriz.
#imageGray = cv.imread(locate,0)

#resmi griye çevirir
imageGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#bu sekilde de atama yapabiliyoruz
height,weight,channelNo = image.shape

print("Size of orj image : ",image.size)
print("Size of gray image : ",imageGray.size)
print("Shape of orj image : ",height, weight, channelNo) #image.shape
print("Shape of gray image : ",imageGray.shape)


cv.imshow("Gri resim",imageGray)

cv.waitKey(0)
cv.destroyAllWindows()