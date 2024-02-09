import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

# Cargar la imagen
imagen_original = cv2.imread(r'./img/b1_add_b2.png')
# cv2.imshow('Original', imagen_original)

# Convertir la imagen a escala de grises (si no lo está)
imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gris', imagen_gris)

# Aplicar filtro de enfoque
imagen_enfocada = cv2.filter2D(imagen_gris, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))

# Aplicar aumento de contraste
alpha = 1.2  # Ajusta el valor según sea necesario
beta = 0
imagen_contrastada = cv2.convertScaleAbs(imagen_enfocada, alpha=alpha, beta=beta)
# cv2.imshow('Contraste', imagen_contrastada)

# Aplicar filtro de desenfoque
imagen_desenfocada = cv2.GaussianBlur(imagen_contrastada, (5, 5), 0)
# cv2.imshow('Desenfoque', imagen_desenfocada)

recognized_text = pytesseract.image_to_string(imagen_desenfocada)
print("recognized_text -> ", recognized_text)

cv2.waitKey(0)
cv2.destroyAllWindows()
