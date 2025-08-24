import cv2

image = cv2.imread("image.jpg")

if image is not None :
    success = cv2.imwrite("output.png", image)
    if success :
        print("image saved as 'output.png' sucessfully saved")
    else :
        print("failed to save")
else:
    print("file not found")