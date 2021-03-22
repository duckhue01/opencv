import cv2 
import numpy 

img = cv.imread('./images/dung.jpg', 0)
kernel = np.ones((5,5), np.uint)
erosion  = cv