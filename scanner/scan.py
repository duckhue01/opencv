from transform import fourPointTransform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils


# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image file")
# ap.add_argument("-c", "--coords",
# 	help = "comma seperated list of source points")
# args = vars(ap.parse_args())

# read image and resize
image = cv2.imread("./image.jpg")    
ratio = image.shape[0] / 500
orig = image.copy()
image = imutils.resize(image,height= 500)



# convert the image to grayscale, blur it and find adges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(gray, 70, 200)


print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()


cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

screenCnt = []
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx =cv2.approxPolyDP(c, 0.02 * peri ,True)
    
    if len(approx) == 4:
        screenCnt = approx   
        
        break


print("STEP 2: Find contours of paper")
print(screenCnt)
print(screenCnt.reshape(4,2) * ratio)
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()    

warped  =fourPointTransform(orig, screenCnt.reshape(4, 2) * ratio)

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)