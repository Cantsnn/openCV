import cv2 as cv
import numpy as np

locate = "img/morp.png"

image = cv.imread(locate)

kernel = np.ones((5,5),np.uint8)

#erosion: yok etme,asindirma islemi
#gurultu giderilir ve incelmis olur. o yuzden sonradan dilation islemi yapilir
erosion = cv.erode(image,kernel,iterations = 1)

#dilation: genisleme islemi
dilation = cv.dilate(image,kernel,iterations = 1)

#opening islemi, once erosion sonra dilation islemi yapiyor.
#opening = erosion + dilation
opening = cv.morphologyEx(image,cv.MORPH_OPEN,kernel)

#closing islemi de once dilation sonra erosiyon yapar, kopuklu gorsellerde kullanilir
#closing = dilation + erosion
closing = cv.morphologyEx(image,cv.MORPH_CLOSE,kernel,1)

#gradinet = dilation - erosion
gradient = cv.morphologyEx(image,cv.MORPH_GRADIENT,kernel)

#top hat, gurultulu kismi veriyor diyebiliriz
#top hat = orjinal - opening
tophat = cv.morphologyEx(image,cv.MORPH_TOPHAT,kernel)


#black hat = closing - orjinal
blackhat = cv.morphologyEx(image,cv.MORPH_BLACKHAT,kernel)


cv.imshow("Orj image",image)
cv.imshow("Dilation",dilation)
cv.imshow("Erosion",erosion)
cv.imshow("Opening",opening)
cv.imshow("Closing",closing)
cv.imshow("Gradient",gradient)
cv.imshow("Top hat",tophat)
cv.imshow("Black hat",blackhat)



cv.waitKey(0)
cv.destroyAllWindows()