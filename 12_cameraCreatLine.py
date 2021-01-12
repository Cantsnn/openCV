import cv2 as cv


camera = cv.VideoCapture(0)


while True:
    ret,image = camera.read()
    #dikdörtgen ekleme
    cv.rectangle(image,(200,200),(400,400),(255,0,0),3)

    #cizgi ekleme
    cv.line(image,(0,0),(300,300),(0,0,255),3)

    #daire ekleme
    cv.circle(image,(320,240),100,(0,255,0),2)

    #text box ekleme
    cv.putText(image,"hello",(320,240),cv.FONT_HERSHEY_DUPLEX,1,(255,255,255),1)

    cv.imshow("Kamera",image)

    if cv.waitKey(1) & 0xFF ==ord("q"):
        break


camera.release()
cv.destroyAllWindows()