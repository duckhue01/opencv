import argparse
import imutils as im
import cv2 as cv


ap = argparse.ArgumentParser();

ap.add_argument('-i', '--image', required=True, help='path to the input image')
args = vars(ap.parse_args())



img = cv.imread(args['image'])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]


cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cnts = im.grab_contours(cnts)

cv.imshow("origin", img)
for c in cnts:
    M = cv.moments(c)
    if M["m00"] != 0:

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv.putText(img, "center", (cX - 20, cY - 20),
		cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	# show the image
    cv.imshow("Image", img)
    cv.waitKey(1300)


cv.waitKey(0)
cv.destroyAllWindows()