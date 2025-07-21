import cv2 as cv
import numpy as np

CHARACTERS = "@%#*+=-:. "

cam = cv.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("Impossible de récuperer la frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img_arr = np.array(gray)
    height, width = frame.size
    row = []
    
    for height in height:
        for width in width:
            index = int(gray / 255)
            img_arr[height, width] = CHARACTERS[index]

            row.append(img_arr)

    for i in row:
        print("".join(i))

cam.release()
cv.destroyAllWindows()
