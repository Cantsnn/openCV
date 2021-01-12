import cv2 as cv

locate = "img/opencvLogo.png" #Resim farklı yerdeyse konumu ile verilmeli

image = cv.imread(locate) #Resmi okuyor.
imageGray = cv.imread(locate,0) #Resmi griye çevirip alıyor. 1 yapılırsa renkli olur


cv.imshow("RGB image",image) # Okuduğumuz resmi ekranda gösteriyoruz.
cv.imshow("Gray image",imageGray) #Ilk parametre pencerede gözükecek olan isim.

cv.imwrite("imageGray.png",imageGray) #Griye cevirdigimiz resmi farklı isimle kaydediyoruz.


cv.waitKey(0)
cv.destroyAllWindows()
