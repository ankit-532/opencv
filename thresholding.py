import cv2

img = cv2.imread("WIN_2.jpg",cv2.IMREAD_GRAYSCALE)

ret ,thresholded_img =cv2.threshold(img, 115, 255, cv2.THRESH_BINARY)

cv2.imshow("edited image", thresholded_img)
cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()