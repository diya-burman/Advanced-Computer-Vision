import cv2 
import mediapipe as mp
import time

cap = cv2.VideoCapture('D:\Advanced Computer Vision\Videos\convoAI.mp4')
pTime=0

mpFaceDetection = mp.solutions.face_detection
mpDrawing = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            print(id, detection)
            print(detection.score)
            print(detection.loaction)data.realtive_bounding_box

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1) 