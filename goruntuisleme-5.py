import cv2
from cv2 import waitKey

import numpy as np

img = np.zeros((512,720),np.uint8)

cv2.line(img,(100,250),(250,419),(146,76,247),4,cv2.LINE_AA)

cv2.rectangle(img,(255,255),(511,419),(255,255,255),4)
cv2.rectangle(img,(0,0),(250,250),(255,255,255),-1)

cv2.circle(img,(419,419),90,(255,255,255),3,cv2.LINE_AA)

pts = np.array([[20,30],[100,115],[255,358],[15,419]],np.int32)
pts2 = pts.reshape(-1,1,2)

cv2.polylines(img,[pts],True,(255,255,255),4)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'OpenCV',(240,300),font,4,(241,147,2),cv2.LINE_AA)

cv2.imshow("resim",img)

waitKey(0)
cv2.destroyAllWindows()