import cv2 as cv

imgL = cv.imread('C:/work/proyectos/zeetrex/python/scan-box/img/group1/left.jpg', cv.IMREAD_GRAYSCALE)
imgR = cv.imread('C:/work/proyectos/zeetrex/python/scan-box/img/group1/right.jpg', cv.IMREAD_GRAYSCALE)

stereo = cv.StereoBM.create(numDisparities=128, blockSize=15)
disparity = stereo.compute(imgL,imgR)
cv.imwrite("disparity.jpg", disparity)

