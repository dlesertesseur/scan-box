import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

img = cv2.imread(r'./img/camera/cam2.jpg')

grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(_, blackWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)

blackWhiteImage = cv2.copyMakeBorder(src=blackWhiteImage, top=100, bottom=100, left=50, right=50, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))

data = pytesseract.image_to_data(blackWhiteImage, config="-c tessedit_char_whitelist= ABCDEFGHIJKLMNOabcdefghijklmnopqrstuvwxyz --psm 6")
originalImage = cv2.cvtColor(blackWhiteImage, cv2.COLOR_GRAY2BGR)

text = []
for z, a in enumerate(data.splitlines()):
    if z != 0:
        a = a.split()
        if len(a) == 12:
            x, y = int(a[6]), int(a[7])
            w, h = int(a[8]), int(a[9])
            cv2.rectangle(originalImage, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(originalImage, a[11], (x, y - 2), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            text.append(a[11])

print("Text result: \n", text)
cv2.imshow('Image result', originalImage)
cv2.imwrite(r'./img/camera/ocr.png', originalImage) 
cv2.waitKey(0)