import cv2
import numpy as np

# ---- Zadanie 1: Maskowanie twarzy ----
face_img = cv2.imread("dziad.jpg")
if face_img is not None:
    mask_face = np.zeros(face_img.shape[:2], dtype="uint8")
    cv2.ellipse(mask_face, (face_img.shape[1]//2, face_img.shape[0]//2), (180, 200), 0, 0, 360, 255, -1)
    result_face = cv2.bitwise_and(face_img, face_img, mask=mask_face)
    cv2.imshow("Twarz oryginalna", face_img)
    cv2.imshow("Maska na twarz", mask_face)
    cv2.imshow("Twarz po maskowaniu", result_face)
    cv2.waitKey(0)

# ---- Zadanie 2: Ukrywanie oczu ----
    mask_eyes = np.ones(face_img.shape[:2], dtype="uint8") * 255
    cv2.rectangle(mask_eyes, (220, 350), (face_img.shape[1]-90, 470), 0, -1)
    result_eyes = cv2.bitwise_and(face_img, face_img, mask=mask_eyes)
    cv2.imshow("Maska na oczy", mask_eyes)
    cv2.imshow("Twarz bez oczu", result_eyes)
    cv2.waitKey(0)
else:
    print("Blad: Nie udalo sie wczytac obrazu twarzy!")

# ---- Zadanie 3: Ekstrakcja koloru ----
color_img = cv2.imread("kwiaty.jpg")
if color_img is not None:
    hsv = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 100, 100])
    upper = np.array([10, 255, 255])
    mask_color = cv2.inRange(hsv, lower, upper)
    result_color = cv2.bitwise_and(color_img, color_img, mask=mask_color)
    cv2.imshow("Obraz oryginalny", color_img)
    cv2.imshow("Maska koloru", mask_color)
    cv2.imshow("Wydzielony kolor", result_color)
    cv2.waitKey(0)
else:
    print("Blad: Nie udalo sie wczytac kolorowego obrazu!")

cv2.waitKey(0)
cv2.destroyAllWindows()