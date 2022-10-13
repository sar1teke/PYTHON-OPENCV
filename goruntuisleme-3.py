import cv2

cam = cv2.VideoCapture("sarki.mp4")

while cam.isOpened():

    ret, frame = cam.read()

    if not ret:
        print("Goruntu Okunamiyor")
        break

    cv2.imshow("Goruntu",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Video Kapatildi")
        break

cam.release()
cv2.destroyAllWindows()
