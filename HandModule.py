import cv2
import mediapipe # used for media processing

cap = cv2.VideoCapture(0)
initHand = mediapipe.solutions.hands  # Initializing mediapipe
mainHand = initHand.Hands(max_num_hands = 1,min_detection_confidence = 0.9,min_tracking_confidence = 0.9)# Object of mediapipe with "arguments for the hands module"

draw = mediapipe.solutions.drawing_utils  # Object to draw the connections between each finger index



while True:
    check, img = cap.read()  # Reads frames from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
    result = mainHand.process(imgRGB)

    if result.multi_hand_landmarks:
        for hands in result.multi_hand_landmarks:
            draw.draw_landmarks(img,hands,initHand.HAND_CONNECTIONS)

    cv2.imshow("Webcam", img)
    k = cv2.waitKey(1)
    if k == 27 or k == 13:
        break

cap.release()
cv2.destroyAllWindows()