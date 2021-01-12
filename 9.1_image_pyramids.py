import cv2 as cv
import numpy as np


#kendi boş resmimizi olusturuyoruz
image = np.zeros((300,300,3),dtype = "uint8")

print(image)

cv.waitKey(0)
cv.destroyAllWindows()