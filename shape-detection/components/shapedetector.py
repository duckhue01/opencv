import cv2
import imutils


class ShapeDetector:
    def __init__(self) -> None:
        pass

    def detect(self, c):
        shape = "undefine"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04  * peri, True)

        if len(approx) == 3:
            shape = "triangle"
        
        elif len(approx) == 4:
            (x, y, w ,h) = cv2.boundingRect(approx)
            ar = w / float(h)
            
            shape = "Square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        
        else:
            shape = "circle"

        return shape

        


img = cv2.imread("./shapes.jpg") 

resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
gblurimg = cv2.GaussianBlur(gray,(5,5),0)
ret, threshimg = cv2.threshold(gblurimg, 60, 255, cv2.THRESH_BINARY)

contours = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours  = imutils.grab_contours(contours)
# print(contours)
sd = ShapeDetector()



for c in contours:
    M = cv2.moments(c)
    if( M["m00"] != 0):
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
 
        shape = sd.detect(c)

        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        cv2.drawContours(img, [c], -1 , (0, 255, 0), 2)  
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,shape, (cX, cY),font, 0.5, (0, 0, 0),2)

        cv2.imshow("img",img)
        cv2.waitKey(0)
