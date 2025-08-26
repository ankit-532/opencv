import cv2

camera = cv2.VideoCapture(0)
Frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
Frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("My_Videor.avi", codec ,20 , (Frame_width,Frame_height))

while True:
    success ,image = camera.read()
    if not success:
        break
    recorded.write(image)
    cv2.imshow("RecordingLive", image)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
camera.release()
recorded.release()
cv2.destroyAllWindows()