import cv2 
import numpy as np


img = cv2.imread('./images/dung.jpg', 1)
kernel = np.ones((11,11), np.uint)
erosion  = cv2.erode(img, kernel, iterations=10)

cv2.imshow('img', img)
cv2.waitKey(0)