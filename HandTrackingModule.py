import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectioCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, 
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
           myHand = self.results.multi_hand_landmarks[handNo]

           for id, lm in enumerate(handLms.landmark):
           # print(id, lm)
           h, w, c = img.shape
           cx, cy = int(lm.x*w), int(lm.y*h)
           print(id, cx, cy)
           # if id==4:
           cv2.circle(img, (cx,cy), 25, (255,0,255), cv2.FILLED)

        return lmList

    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
                                    #(value,position)                #scale          #thickness
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

def main():
    pTime=0
    cTime=0
    cap = cv2.capture(1)
    detector = handDetector()
    detector.findHands(img)
    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
                                        #(value,position)                #scale          #thickness
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()