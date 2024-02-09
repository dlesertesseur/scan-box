import numpy as np
import cv2 as cv
import pytesseract

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)

    #filter the source image
    img_rst = cv.Canny(gray,100,200)

    cv.imshow('frame', img_rst)

    key = cv.waitKey(1)

    if key == ord('q'):
        break
    elif (key == ord('s')):
        print("scannig-OCR")
        print(pytesseract.image_to_string(img_rst))
        cv.imshow('TO scann', img_rst) 

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()