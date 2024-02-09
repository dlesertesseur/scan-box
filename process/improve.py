import numpy as np
import cv2

def deskew(image):
    co_ords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(co_ords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC,
    borderMode=cv2.BORDER_REPLICATE)
    return rotated

def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]

def main():
    img = cv2.imread(r'../img/group1/right.jpg')
    if img is None:
        print("img is None")
        return(-1)

    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

    #2. Skew Correction
    #img = deskew(img)

    #3. Noise Removal
    img = remove_noise(img)

    #4. Thinning and Skeletonization
    kernel = np.ones((5,5),np.uint8)
    img = cv2.erode(img, kernel, iterations = 1)

    #5. Gray Scale image
    img = get_grayscale(img)

    #6. Thresholding or Binarization
    img = thresholding(img)

    cv2.imwrite('improve.jpg', img) 

    print("improve.jpg -> ")

if __name__ == '__main__':
    main()
