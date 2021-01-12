import cv2 as cv



locate = "img/opencvLogo.png"

image = cv.imread(locate)
#BGR olarak resmin tonlarını degistirme
"""
image[:,:,0] = 200
image[:,:,1] = 80
image[:,:,2] = 20
"""
#Resmin belirli bir bölümüne efekt ekleme
image[300:320,600:650,1] =255
image[300:320,600:650,0] =150
cv.imshow("image",image)


cv.waitKey(0)
cv.destroyAllWindows()