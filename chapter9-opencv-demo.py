import cv2

# https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html
capture = cv2.VideoCapture(0)

while True:
    return_val, frame = capture.read()
    cv2.imshow('Face', frame)
    key = cv2.waitKey(5)
    if key == 113:
        break
