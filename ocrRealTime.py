import numpy as np
import cv2 as cv
import pytesseract
from PIL import ImageGrab

cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

# Function to capture the screen
def capture_screen(bbox=(300, 300, 1500, 1000)):
    cap_scr = np.array(ImageGrab.grab(bbox))
    cap_scr = cv.cvtColor(cap_scr, cv.COLOR_RGB2BGR)
    return cap_scr

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Perform text detection on the frame using Tesseract OCR
    recognized_text = pytesseract.image_to_string(frame)

    # Perform bounding box detection using Tesseract's built-in capabilities
    d = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 0:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
   
    # # Draw the detected text on the frame
    frame_with_text = frame.copy()
    frame_with_text = cv.putText(frame_with_text, recognized_text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    # Display the frame with detected text
    cv.imshow("Frame", frame_with_text)

    key = cv.waitKey(1)

    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()