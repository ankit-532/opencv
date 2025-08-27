import cv2
import numpy as np

img = cv2.imread("image.jpg")

sharpen_kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpen_img = cv2.filter2D(img, -1, sharpen_kernal)

cv2.imshow("original image", img)
cv2.imshow("sharpen image", sharpen_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if sharpen_img is not None :
    cv2.imwrite("flower_sharpening_image.png", sharpen_img)
    
else :
    print("image could not saved")