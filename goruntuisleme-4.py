from asyncore import write
from platform import release
import cv2

cam = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("ilk_kayit.mp4",fourrc , 30.0,(720,840))

while cam.isOpened():

    ret, frame = cam.read()

    if not ret:
        print("Kayit Yapilamiyor.")
        break

    out.write(frame)

    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Kayit Bitti.")
        break

cam.release()
out.release()

cv2.destroyAllWindows()
