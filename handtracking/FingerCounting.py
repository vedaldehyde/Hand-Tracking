import cv2
import time
import HandTrackingModule as htm

wCam,hCam=640,480
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


pTime=0
cTime=0

detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    if len(lmList) != 0:
        fingers=[]
        # Thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(0)
        else:
            fingers.append(1)
        # 4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers=fingers.count(1)
        if totalFingers==5:
            cv2.putText(img, f'Five', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        elif totalFingers==4:
            cv2.putText(img, f'Four', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        elif totalFingers==3:
            cv2.putText(img, f'Three', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        elif totalFingers==2:
            cv2.putText(img, f'Two', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        elif totalFingers==1:
            cv2.putText(img, f'One', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        else:
            cv2.putText(img, f'Zero', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

