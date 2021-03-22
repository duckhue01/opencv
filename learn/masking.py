import numpy as np
import cv2 

img = cv2.imread("./images/shape.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("original", img)

mask = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1]// 2, img.shape[0] // 2)
cv2.rectangle(mask, (0, 0), (cX, cY), 255 ,-1)


cv2.imshow("mask", mask)

masked  =cv2.bitwise_and(img, img)


cv2.imshow("masked", masked)
cv2.waitKey(0)