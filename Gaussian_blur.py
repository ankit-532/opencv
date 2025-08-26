import cv2

image = cv2.imread("wallpape.jpg")

blurred_img = cv2.GaussianBlur(image, (5,5) , -1)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()