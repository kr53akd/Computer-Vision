import cv2
import matplotlib.pyplot as plt
img = cv2.imread("sample.jpg")
halfImg = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
Big_Img = cv2.resize(img, (1050, 1060))
# INTERPOLATION is used to print enlargement of an image and calculate pixel values
Stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_NEAREST)

Titles = ["Original", "half", "Bigger", "stretch_near"]
images = [img, halfImg, Big_Img, Stretch_near]
iterate = 4
for i in range(iterate):
    # subplot(rows,columns,plot number)
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
