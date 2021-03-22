from transform import fourPointTransform
# from skimage.filters import threshold_local
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
image = cv2.imread("./img2.jpg")    
ratio = image.shape[0] / 500
orig = image.copy()
image = imutils.resize(image,height= 500)



# convert the image to grayscale, blur it and find adges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (1,1), 0)
edged = cv2.Canny(gray, 10, 200)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
cv2.drawContours(image, cnts[:10], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.imshow("blur", blur)
cv2.imshow("edged", edged)

# for c in cnts:
#     peri = cv2.arcLength(c, True)
#     print(peri)

cv2.waitKey(0)
cv2.destroyAllWindows() 





# for c in cnts:
#     peri = cv2.arcLength(c, True)
#     approx =cv2.approxPolyDP(c, 0.02 * peri ,True)
    
#     if len(approx) == 4:
#         screenCnt = approx   

#         print("STEP 2: Find contours of paper")
           
#         break

