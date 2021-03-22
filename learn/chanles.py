import numpy as  np
import cv2


img = cv2.imread('./images/shape.png')
cv2.imshow("img", img)

(B, G, R) =  cv2.split(img)


# cv2.imshow("red", r)
# cv2.imshow("green", g)
# cv2.imshow("blue", b)




# merged = cv2.merge([b, g, r])
# cv2.imshow("merged", merged)
zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


# cv2.waitKey(0)

cv2.destroyAllWindows()