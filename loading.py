import cv2

load = cv2.imread("image.jpg")
if load is not None :
    print("image is successfully loaded")
else :
    print("image not found")