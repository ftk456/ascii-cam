import cv2 as cv
import numpy as np

cols = 35
rows = 120
CHAR_LIST = " .:?#$&%@"
num_chars = len(CHAR_LIST)

cam = cv.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("Impossible de récuperer la frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    height, width = frame.size
    cell_height = height / cols
    cell_width = width / rows
    if cols > height or rows > width:
        raise ValueError("Trop de lignes ou de colonnes")
    result = ""
    for i in range(cols):
        for j in range(rows):
            gray = numpy.mean(frame[
                int(cell_height * i):min(int((i + 1) * cell_height), height),
                int(cell_width * j):min(int((j + 1) * cell_width), width)
            ])
            result += CHAR_LIST[min(int(gray * num_chars / 255), num_chars - 1)]
        result += "\n"
    print(result)

cam.release()
cv.destroyAllWindows()
