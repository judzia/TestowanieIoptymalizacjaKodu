import cv2
import imutils

# 1. Obrót o 45 stopni  


image = cv2.imread("kicia.jpg")  
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

cv2.imshow("Original", image)
cv2.waitKey(0)

# Obrót o 45 stopni wokół środka
M1 = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated1 = cv2.warpAffine(image, M1, (w, h))
cv2.imshow("Rotated 45 degrees", rotated1)
cv2.waitKey(0)


# 2. Obrót o -90 stopni        


M2 = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated2 = cv2.warpAffine(image, M2, (w, h))
cv2.imshow("Rotated -90 degrees", rotated2)
cv2.waitKey(0)

# 3. Obrót wokół narożnika (0,0) 


M3 = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated3 = cv2.warpAffine(image, M3, (w, h))
cv2.imshow("Rotated 30 deg around corner", rotated3)
cv2.waitKey(0)


# 4. Obrót o dowolny kąt od użytkownika 


try:
    angle = float(input("Podaj kąt obrotu (dowolny): "))
except ValueError:
    print("Błędny kąt! Ustawiam domyślnie 0.")
    angle = 0.0

M4 = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated4 = cv2.warpAffine(image, M4, (w, h))
cv2.imshow(f"Rotated {angle} degrees", rotated4)
cv2.waitKey(0)


# 5. Obrót o 180 stopni imutils.rotate 


rotated5 = imutils.rotate(image, 180)
cv2.imshow("Rotated 180 degrees (imutils)", rotated5)
cv2.waitKey(0)


# 6. Obrót bez przycinania rotate_bound 

rotated6 = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated -33 deg (no cropping)", rotated6)
cv2.waitKey(0)


# 7. Porównanie warpAffine i imutils.rotate 

M7 = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warpAffine = cv2.warpAffine(image, M7, (w, h))
rotated_imutils = imutils.rotate(image, 60)

cv2.imshow("WarpAffine 60 deg", rotated_warpAffine)
cv2.imshow("Imutils 60 deg", rotated_imutils)
cv2.waitKey(0)


# 8. Sekwencyjne 3x 30 stopni  


rotated_seq = image.copy()
for i in range(3):
    M_seq = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
    rotated_seq = cv2.warpAffine(rotated_seq, M_seq, (w, h))

cv2.imshow("Sequential 3x30 deg", rotated_seq)


# Dla porównania pojedynczy obrót o 90
M90 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated90 = cv2.warpAffine(image, M90, (w, h))
cv2.imshow("Single 90 deg", rotated90)
cv2.waitKey(0)


# 9. Obrót o 75 stopni i zapis  


M9 = cv2.getRotationMatrix2D((cX, cY), 75, 1.0)
rotated9 = cv2.warpAffine(image, M9, (w, h))
cv2.imwrite("rotated_output.jpg", rotated9)
cv2.imshow("Rotated 75 deg and saved", rotated9)
cv2.waitKey(0)

# 10. Obrót w pętli co 15 stopni 


for angle in range(0, 361, 15):
    M_loop = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated_loop = cv2.warpAffine(image, M_loop, (w, h))
    cv2.imshow(f"Rotation {angle} deg", rotated_loop)
    cv2.waitKey(500)  # opóźnienie 500ms
    

cv2.waitKey(0)
cv2.destroyAllWindows()