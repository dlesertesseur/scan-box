import pytesseract
from PIL import Image

custom_oem_psm_config = r'--oem 1 --psm 3'
pytesseract.pytesseract.tesseract_cmd = 'C:/work/instalacion/Tesseract-OCR/tesseract.exe'

img_rgb = Image.open('../img/group1/right.jpg')
data = pytesseract.image_to_string(img_rgb, config=custom_oem_psm_config)
#data = pytesseract.image_to_boxes(img_rgb, config=custom_oem_psm_config)

print(data)

#print(pytesseract.image_to_boxes(img_rgb))

