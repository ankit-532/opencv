import cv2
import numpy as np

img = cv2.imread("image.jpg")

blurred = cv2.medianBlur(img, 3)

cv2.imshow("original image", img)
cv2.imshow("blurred image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()