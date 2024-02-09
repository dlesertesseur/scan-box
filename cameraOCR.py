import numpy as np
import cv2 as cv
import pytesseract

cap = cv.VideoCapture(1)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    key = cv.waitKey(1)

    if key == ord('q'):
        break
    elif (key == ord('f')):
        print("scannig-OCR")
        img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        print(pytesseract.image_to_string(img_rgb))
        #cv.imshow('TO scann', img_rgb) 

    cv.imshow('frame', frame)        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()