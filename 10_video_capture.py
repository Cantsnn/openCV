import cv2 as cv


#0 yazarsak kendi kameramizi açar
#1 dersek usbde tanimli kamerayi alir
#2 dersek kayitli videodan alir
camera = cv.VideoCapture(0)

while (camera.isOpened()):
    ret,image = camera.read()

    cv.imshow("Kamera",image)

    if cv.waitKey(30) & 0xFF ==ord("q"):
        break


camera.release()
cv.destroyAllWindows()