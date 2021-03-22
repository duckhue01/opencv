import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)


cv.line(img, (0,0), (512,512), (255, 0, 0), 5)
cv.rectangle(img , (10, 10), (100, 150), (0, 255, 0), 3)
cv.circle(img)
cv.imshow("img", img)
cv.waitKey(0