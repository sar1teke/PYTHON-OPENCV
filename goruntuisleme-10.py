from gettext import translation
import cv2
from cv2 import imread
import numpy as np

img = cv2.imread("togg.png")

print(img.shape)

#Bu kısımda görüntüyü bir matris içine alarak döndürme,kaydırma (vb.) işlemleri yaptık.

rows,cols = img.shape[:2]

#translation_matrix = np.float32([
#   [1 , 0 , 50],
#   [0 , 1 , 50]
#])

#img_translation = cv2.warpAffine(img , translation_matrix ,(cols+50 ,rows+50))

rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)

img_rotation = cv2.warpAffine(img ,rotation_matrix,(cols,rows))

cv2.imshow("togg.png",img)
cv2.imshow("img_translation" , img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()