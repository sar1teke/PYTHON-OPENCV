import cv2
import numpy as np
img = cv2.imread("images/portakal.png")
imgGri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Portakal", img)
cv2.imshow("Portakal GRI", imgGri)

size_x = img.shape[0]
size_y = img.shape[1]
#kanal = imgGri = imgGri.shape[2]

print("Yukseklik:",size_y,"Genislik:",size_x)
print(img[(100,100)])
print(imgGri[(100,100)])

cv2.waitKey(0)
cv2.destroyAllWindows()
