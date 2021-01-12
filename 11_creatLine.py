import cv2 as cv
import numpy as np

image = np.zeros((300,300,3),dtype = "uint8")

#cizgi olusturma
cv.line(image,(100,100),(200,200),color = [255,150,0],thickness = 3)
cv.imshow("Line ",image)

#daire cizdirme
cv.circle(image,(150,150),50,(0,0,255),2)
cv.imshow("Circle ",image)

#text box olusturma
cv.putText(image,"Merhaba",(150,200),cv.FONT_HERSHEY_COMPLEX, 1 ,(255,255,0),1)
cv.imshow("Text box ",image)

cv.waitKey(0)
cv.destroyAllWindows()