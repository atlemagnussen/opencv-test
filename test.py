import numpy as np
import cv2

#cap = cv2.VideoCapture("http://admin:einherjer57@57.57.57.102/video2.mjpg")

cap = cv2.VideoCapture("video.avi")

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print("isOpened=" + str(cap.isOpened()))
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("isOpened=" + str(cap.isOpened()))
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()