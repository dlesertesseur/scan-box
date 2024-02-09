import cv2

# reading image
img = cv2.imread('../img/a1.png')

# thresholding the image
ret,thresh = cv2.threshold(img, 127, 229, cv2.THRESH_TOZERO)
edged = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

# ADDED BINARY THRESHOLD
ret,thresh = cv2.threshold(edged,100,255,cv2.THRESH_BINARY)


# collectiong contours
contours, h = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.imshow('img', thresh)

# looping through contours
for cnt in contours:

    x, y, w, h = cv2.boundingRect(cnt)
    if w > 50 and h > 50:

        #ADDED SIZE CRITERION TO REMOVE NOISES
        size = cv2.contourArea(cnt)
        if size > 500:

            #CHANGED DRAWING CONTOURS WITH RECTANGLE
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,215,255),2)

cv2.imwrite('boxes.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()