import cv2 as cv


locate = "img/opencvLogo.png"

image = cv.imread(locate)

print(image[(230,80)]) #Resmin o noktadaki piksel degerlerini verir

print("Image size : ",image.size)
print("Attributes of the image : ",image.shape)
print("Data type of the image : ",image.dtype)


cv.waitKey(0)
cv.destroyAllWindows()