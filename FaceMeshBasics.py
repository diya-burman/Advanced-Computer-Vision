import cv2
import mediapipe as mp
import time

# Initialize video capture and timing
cap = cv2.VideoCapture('D:\\Advanced Computer Vision\\Videos\\convoAI.mp4')
pTime = 0

# Initialize Mediapipe components
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=4)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)  # Customize landmark and connection drawing

while True:
    success, img = cap.read()
    if not success:
        print("Video ended or cannot be loaded.")
        break

    # Convert image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    # Draw face landmarks
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                img, 
                faceLms, 
                mpFaceMesh.FACEMESH_CONTOURS,  # Use FACEMESH_CONTOURS for facial connections
                drawSpec, drawSpec
            )

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    # Display the output
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
