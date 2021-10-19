# This is an extra script you can run to test the video stream from your IP camera.

import cv2
cap = cv2.VideoCapture("rtsp://admin:admin123@192.168.1.150:88/videoMain") # <-- EDIT HERE

ret, frame = cap.read()

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('VideoFeed', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
