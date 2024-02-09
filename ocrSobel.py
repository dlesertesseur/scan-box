import numpy as np
import cv2 as cv
import pytesseract

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Aplicar el filtro de Sobel para resaltar bordes
    sobelx = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=5)

    # Calcular la magnitud del gradiente
    magnitud = np.sqrt(sobelx**2 + sobely**2)

    # # Normalizar la magnitud para convertirla a valores de píxeles de 8 bits
    magnitud = cv.normalize(magnitud, None, 0, 255, cv.NORM_MINMAX)

    # # Convertir la imagen resultante de nuevo a valores de píxeles de 8 bits
    magnitud = np.uint8(magnitud)

    cv.imshow('frame', magnitud)
    
    key = cv.waitKey(1)

    if key == ord('q'):
        break
    elif (key == ord('s')):
        print("scannig-OCR")
        print(pytesseract.image_to_string(magnitud))
        cv.imshow('TO scann', magnitud) 
    elif (key == ord('i')):
        imagen_invertida = 255 - magnitud
        cv.imshow('TO scann', imagen_invertida) 

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()