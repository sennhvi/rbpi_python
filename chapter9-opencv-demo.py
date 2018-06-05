import cv2

capture = cv2.VideoCapture(0)

while True:
    return_val, frame = capture.read()
    cv2.imshow('Face', frame)
    key = cv2.waitKey(5)
    if key == 113:
        break
