  
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
lower_range = np.array([20, 150, 150])
upper_range = np.array([190, 255, 255])


while(True):
    
    ret, frame = cap.read()
    frame = cv2.resize(frame,(400,320)) #goruntuyu boyutlandirma

    # gurultuyu azaltmak icin bulaniklastirma
    frameBlur = cv2.medianBlur(frame, 3)

    # lab formuna donusturmek icin goruntu bgr olmali
    frameLab = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2Lab)

    #kirmizi rengi maskeleme
    frameLabRed = cv2.inRange(frameLab,lower_range, upper_range)
    # goruntuyu daha duzgun hale getirmek icin tekrar blurlama islemi
    frameLabRed = cv2.GaussianBlur(frameLabRed, (5, 5), 2, 2)
    frameBit = cv2.bitwise_and(frame,frame,mask = frameLabRed)
    # daireleri tespit etme
    circles = cv2.HoughCircles(frameLabRed, cv2.HOUGH_GRADIENT, 1,\
                                frameLabRed.shape[0] / 8, param1=100, param2=18, minRadius=5, maxRadius=90)

	#tespit edilen dairelerin cizimi
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 255, 0), thickness=2)
        

    # ekrana yazdirma 
    cv2.imshow('Orj frame', frame)
    cv2.imshow("Red Lab",frameLabRed)
    cv2.imshow("red bit",frameBit)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()