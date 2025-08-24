import cv2

image = cv2.imread("image.jpg")

# if image is not None :
#     resize_img = cv2.resize(image , (50,50))
#     cv2.imshow("original image", image)
#     cv2.imshow("resized image", resize_img)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# else:
#     print("image not found")



cropped_img = image[100:200 ,50:150]

cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()