import cv2 as cv


locate = "img/opencvLogo.png"

image = cv.imread(locate)

image[50,30] = [255,255,255] #Resmin belirli bir noktasını istediğiniz renge çeviriyor.

#Döngü sayesinde noktaları sıralı bir şekilde çizgi gibi çiziyor.
for i in range(1000):
    image[70,i]=[0]  


cv.imshow("resim",image)

print(image[(230,80)]) #Resmin o noktadaki piksel degerlerini verir

print("Image size : ",image.size)
print("Attributes of the image : ",image.shape)
print("Data type of the image : ",image.dtype)


cv.waitKey(0)
cv.destroyAllWindows()