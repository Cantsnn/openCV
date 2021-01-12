import cv2 as cv

locate = "img/imageNoise.jpg"

image = cv.imread(locate)

#mean filteri uyguluyoruz
#piksel sayisini arttirdikca goruntu yumusar
#alakasiz bir piksel butun resmi etkiledigi icin resmi genel olarak bozar
meanFilter = cv.blur(image,(3,3))
meanFilter2 = cv.blur(image,(5,5))
meanFilter3 = cv.blur(image,(7,7))

cv.imshow("Orj image",image)
cv.imshow("Mean Filter3x3 image",meanFilter)
cv.imshow("Mean Filter5x5 image",meanFilter2)
cv.imshow("Mean Filter7x7 image",meanFilter3)

#median filtreleme
#mean mediana göre daha cok yumusatir goruntuyu bozar
medianFilter = cv.medianBlur(image,3)
medianFilter2 = cv.medianBlur(image,5)
medianFilter3 = cv.medianBlur(image,7)
cv.imshow("Median Filter 3x3 image",medianFilter)
cv.imshow("Median Filter 5x5  image",medianFilter2)
cv.imshow("Median Filter 7x7  image",medianFilter3)

#gauss filtreleme, bulanıklastirarak duzeltmeye yarar. mediana benzer
#her pikselin agirlikli ortalamasini cikardigi icin daha verimli bir filtre
gauss = cv.GaussianBlur(image,(3,3),0)
gauss2 = cv.GaussianBlur(image,(5,5),0)
gauss3 = cv.GaussianBlur(image,(7,7),0)

cv.imshow("Gauss filter 3x3 image",gauss)
cv.imshow("Gauss filter 5x5 image",gauss2)
cv.imshow("Gauss filter 7x7 image",gauss3)
print(gauss.shape)




cv.waitKey(0)
cv.destroyAllWindows()