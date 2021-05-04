import cv2 as cv
import imutils as imu
img = cv.imread("sample.jpg")
gaussianBlur = cv.GaussianBlur(img, (11, 11), 0)
cv.imwrite("BlurredImage.jpg", gaussianBlur)


