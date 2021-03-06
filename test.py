import numpy as np
import cv2

cam1 = "http://*:*@192:168.1.11/video1.mjpg"
cam2 = "http://*:*@192:168.1.11/video2.mjpg"
cam3 = "http://*:*@192:168.1.11/video3.mjpg"

cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture("video.avi")
i = 0
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    i += 1
    print("isOpened=" + str(cap.isOpened()) + "pic " + str(i) + "ret " + str(ret))
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("isOpened=" + str(cap.isOpened()))
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()