import numpy as np 
# import argparse
import imutils
import cv2


image  = cv2.imread("./images/dung.jpg")
cv2.imshow("original", image)


shifted  = imutils.translate(image, 10, 50)

cv2.imshow("shifted", shifted)
cv2.waitKey(0)