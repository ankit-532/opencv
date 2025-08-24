import cv2

image = cv2.imread("image.jpg")

if image is not None:
    h ,w ,c = image.shape
    print(f"image loaded:\n Height:{h} \n width :{w}\n channels:{c}")

else:
    print("image not found")