import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Kamera Taninmadi")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Kameradan Goruntu Alinamiyor")        
        break

    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Goruntu Sonlandirildi")
        break

cam.release()
cv2.destroyAllWindows()