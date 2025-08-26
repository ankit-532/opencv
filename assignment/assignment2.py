import cv2

location = input("give me location of picture want to perform operation: ")
image = cv2.imread(location)

if image is not None:
    print("image loaded successfully")
    choise = input(f"press 1 for 'draw line' \n press 2 for 'draw rectangle' \n press 3 for 'circle' \n press 4 for 'Text' ")
    pt1 =(500,420)
    pt2 =(550,525)
    color = (25,43,12)
    thickness = 4
    
    match choise:
        case "1":
            pic = cv2.line(image,pt1,pt2,color,thickness)
            cv2.imshow("picture with line", pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


        case "2":
            pic = cv2.rectangle(image,pt1,pt2,color,thickness)
            cv2.imshow("picture with rectangle", pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


        case "3":
            center = (200,50)
            radius = 50
            pic = cv2.circle(image,center,radius,color,thickness)
            cv2.imshow("picture with circle", pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        case "4":
            text = " welcome to my practise domain"
            org = (110,50)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontscale = 1
            pic =cv2.putText(image,text,org,font,fontscale,color,thickness)
            cv2.imshow("picture with Text", pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        case _:
            print("Invalid Input!!")

else :
    print("image not found")
