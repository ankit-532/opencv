import cv2

img = cv2.imread("image.jpg")

edge = cv2.Canny(img, 0, 67)

cv2.imshow("edges img", edge)
cv2.imshow("original img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()