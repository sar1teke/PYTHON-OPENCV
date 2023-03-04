import cv2

# Değişkenler
# Kameradan nesneye (yüz) ölçülen mesafe
KNOWN_DISTANCE = 76.2  # santimetre
# Gerçek Dünyada veya Nesne Düzleminde yüzün genişliği
KNOWN_WIDTH = 15.3  # santimetre
# Renkler
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
fonts = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)

# Yüz Dedektörü
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# odak uzaklığı bulucu fonksiyon
def focal_length(measured_distance, real_width, width_in_rf_image):
    """
    Bu İşlev Odak Uzaklığını Hesaplar (lens ile CMOS sensör arasındaki mesafe), kullanarak bulabileceğimiz basit bir sabittir.
    MEASURED_DISTACE, REAL_WIDTH(nesnenin gerçek genişliği) ve WIDTH_OF_OBJECT_IN_IMAGE
    :param1 Measure_Distance(int): Referans görüntü alınırken nesneden Kameraya olan mesafeyi temsil eder.
    :param2 Real_Width(int): Nesnenin gerçek dünyadaki gerçek genişliğidir (Benim yüz genişliğim = 14,3 santimetre gibi)
    :param3 Width_In_Image(int): Referans görüntüdeki durumumuzdaki çerçeve /görüntüdeki nesne genişliğidir (Yüz algılayıcı tarafından bulunur)
    :retrun odak_uzunluğu(Float):"""
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value


# mesafe tahmin fonksiyonu
def distance_finder(focal_length, real_face_width, face_width_in_frame):
   
    """Bu İşlev, bağımsız değişkenleri (focal_length, Actual_object_width, Object_width_in_the_image) kullanarak nesne ve kamera arasındaki mesafeyi basitçe tespit eder.
    :param1 odak_uzunluğu(float): odak_uzunluk_Finder işleviyle geri döner
    :param2 Real_Width(int): Nesnenin gerçek dünyadaki gerçek genişliğidir (Benim yüz genişliğim = 5,7 İnç gibi)
    :param3 object_Width_Frame(int): görüntüdeki nesnenin genişliği (bizim durumumuzda, Video beslemesini kullanan çerçeve)
    :dönüş Mesafesi(kayan) : Tahmini mesafe"
    distance = (real_face_width * focal_length) / face_width_in_frame
    return distance"""


# yüz tespit fonksiyonu
def face_data(image):
    
    """
    Bu işlev Yüzü algılama
    :param Görüntüyü bağımsız değişken olarak alır.
    :face_width değerini piksel cinsinden döndürür
    """

    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), WHITE, 1)
        face_width = w

    return face_width


# dizinden referans resim okuma
ref_image = cv2.imread("Ref_image.png")

ref_image_face_width = face_data(ref_image)
focal_length_found = focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_image_face_width)
print(focal_length_found)
cv2.imshow("ref_image", ref_image)

while True:
    _, frame = cap.read()

    # face_data fonksiyonunu çağırma
    face_width_in_frame = face_data(frame)
    # Distance fonksiyonunu çağırarak mesafeyi bulma
    if face_width_in_frame != 0:
        Distance = distance_finder(focal_length_found, KNOWN_WIDTH, face_width_in_frame)
        # Standart Ekrana Yazdırma
        cv2.putText(
            frame, f"Distance = {round(Distance,2)} CM", (50, 50), fonts, 1, (WHITE), 2
        )
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()