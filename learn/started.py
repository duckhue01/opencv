import cv2 as cv
import sys


img = cv.imread("./images/shape.png")


if img is None:
    sys.exit("Could not read the image.")

cv.imshow("dusplay window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("new.png", img)