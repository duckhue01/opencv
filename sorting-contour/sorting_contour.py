import numpy as np
import argparse
import imutils
import cv2 as cv

def sort_contours(cnts, method='left-to-right'):
    reverse  = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    if method  == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    boundingBoxes = [cv.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes), key=lambda b:b[1][i], reverse=reverse))
    return(cnts, boundingBoxes)



def draw_contour(image, c, i):
    M = cv.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv.putText(image, "#{}".format(i + 1), (cX - 20, cY),cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    return image



img = cv.imread("./shapes.png")
accumEdged = np.zeros(img.shape[:2], dtype="uint8")

for chan in cv.split(img):
    chan = cv.medianBlur(chan, 11)
    edged = cv.Canny(chan, 50, 200)
    accumEdged = cv.bitwise_or(accumEdged ,edged)


cnts = cv.findContours(accumEdged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv.contourArea, reverse=True)
orig = img.copy()

for (i, c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)

cv.imshow("Unshorted", orig)
(cnts, boundingBoxes) = sort_contours(cnts, method="top-to-bottom")

for (i, c) in enumerate(cnts):
    draw_contour(img, c, i)



cv.imshow("sorted", img)
# cv.imshow("acc", accumEdged)
cv.waitKey(0)