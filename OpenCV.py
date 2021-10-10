import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)       # Opens the camera
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon= 0.8, maxHands = 2) # DetectionCon dictates how accurate the scan is
colorR = (255,0,255)

cx, cy , w , h = 30 , 30, 120 , 120


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    target = cv2.rectangle(img, (420, 400), (500, 500) , 0000 , cv2.FILLED)

    if hands:     # hands is a dictionary that contains the attributes of the hands
        
        hand1 = hands[0]
        lmList = hand1["lmList"]
        dist , info , img = detector.findDistance(lmList[8], lmList[12], img)
        cursor = lmList[8]

        # Trigger

        if dist < 30: # When distance btw the 2 point is less then 30, the trigger is activated
            if cx-w//2 < cursor[0] < cx+w//2 and \
                    cy-h//2 < cursor[1] < cy+h//2:
                colorR = 0,255,0
                cx,cy = cursor

            else:
                colorR = 255,0,255
        
        # When the Box touches the bounds described below, you win!

        if 420 < cursor[0] < 500 and \
                400 < cursor[1] < 500:
            while True:
                print("Box Touched OWO", )

    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2) , colorR , cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)