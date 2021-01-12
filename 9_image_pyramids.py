import cv2 as cv


locate = "img/NataliePortman.jpg"

image = cv.imread(locate)

#resmi iki kat büyütecek
twiceBig = cv.pyrUp(image)

#resmi iki kat kücültecek
twiceSmall = cv.pyrDown(image)



print("Orj image shape : ",image.shape)
print("Twice as big image shape : ", twiceBig.shape)
print("Twice as small image shape : ",twiceSmall.shape)

cv.imshow("Orj image",image)
cv.imshow("Twice as big image",twiceBig)
cv.imshow("Twice as small image",twiceSmall)

cv.waitKey(0)
cv.destroyAllWindows()