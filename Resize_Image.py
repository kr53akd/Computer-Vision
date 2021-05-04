import cv2 as cv
import imutils as im
img = cv.imread("sample.jpg")
# width and height can be varied in order to increase or decrease blur effect
resizeImg = im.resize(img, width=70)
cv.imwrite("resizedImage.jpg", resizeImg)
