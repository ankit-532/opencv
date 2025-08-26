import cv2

location = input("enter you image location: ")
image = cv2.imread(location)


if image is not None :
    greay = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_color image", greay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if greay is not None:
        name = input("enter you file name: ")
        success = cv2.imwrite(name, greay)
        print(f"sucessfully saved as {name} ")
    else:
        print("greay could not found")
else :
    print("image not found")