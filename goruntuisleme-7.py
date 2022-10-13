import cv2
from cv2 import waitKey

import numpy as np

def nothing(x):
    pass

img = np.zeros((512,720,3),np.uint8)

cv2.namedWindow("renk")

cv2.createTrackbar("R","renk",0,255,nothing)
cv2.createTrackbar("G","renk",0,255,nothing)
cv2.createTrackbar("B","renk",0,255,nothing)

cv2.createTrackbar("ON/OFF","renk",0,1,nothing)


while(1):
    cv2.imshow("renk",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    r = cv2.getTrackbarPos("R","renk")
    g = cv2.getTrackbarPos("G","renk")
    b = cv2.getTrackbarPos("B","renk")

    switch = cv2.getTrackbarPos("ON/OFF","renk")

    if switch:
        img[:] = [b,g,r]
    else:
        img[:] = 0

cv2.destroyAllWindows()        