import cv2

cap = cv2.VideoCapture(0)# create a while loop for infinte frame
while True:
    ret,img=cap.read() # returns bool value if frames are reading correctly
    cv2.imshow('webcam',img)
    k = cv2.waitKey(1) #set refresh rate with waitkey
    if k==13: #press enter to exit
        break

cap.release()

cv2.destroyAllWindows()