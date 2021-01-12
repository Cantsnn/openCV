import cv2 as cv

locate = "img/turkanSoray.jpg"
locate2 = "img/emelSayin.jpg"


image = cv.imread(locate)
image2 = cv.imread(locate2)
 

#Pikseller toplandiginda en fazla 255 olmasi gerekiyor.
#255ten fazla olanlar mod255 e göre cikti verir.
print("1. resmin pikseli :",image[200,100])
print("2. resmin pikseli : ",image2[100,200])

print("Piksellerin toplami : ",image[200,100]+image2[100,200])

cv.imshow("image",image)
cv.imshow("imagee",image2)


cv.waitKey(0)
cv.destroyAllWindows()