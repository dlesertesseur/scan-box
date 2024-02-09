import numpy as np
import cv2 as cv
from datetime import datetime

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    key = cv.waitKey(1)

    if key == ord('q'):
        break
    elif (key == ord('p')):
        now = datetime.now()
        date_time = now.strftime("%Y%m%d_%H%M%S")
        name = './img/' + date_time + '.png'
        cv.imwrite(name, frame)
        cv.imshow(name, frame) 

    cv.imshow('frame', frame)        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()