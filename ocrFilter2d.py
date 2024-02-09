import numpy as np
import cv2 as cv
import pytesseract

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#edge detection filter
kernel = np.array([[0.0, -1.0, 0.0], 
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])
kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)

    #filter the source image
    img_rst = cv.filter2D(frame,-1, kernel)

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