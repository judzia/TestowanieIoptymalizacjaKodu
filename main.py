import cv2
import numpy as np

image = cv2.imread('kooootk.jpg')
image = np.array(image, dtype=np.uint8)

# zad 1

roi = image[:100, :100]
cv2.imshow('ROI', roi)
cv2.waitKey(0)


# zad 2

(h, w, _) = image.shape
bottom_half = image[h//2:, :] # dolna polowa obrazu
cv2.imshow('Bottom Half', bottom_half)
cv2.waitKey(0)

# zad 3
right_half = image[:, w//2:]  # prawa polowa obrazu

cv2.imshow("Prawa połowa", right_half)
cv2.waitKey(0)

# zad 4
startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))
startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))

roi_dynamic = image[startY:endY, startX:endX]  

cv2.imshow("Dynamiczny ROI", roi_dynamic)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 5

face_roi = image[50:400, 200:475]  # Przykładowe współrzędne twarzy

cv2.imshow("Twarz", face_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 6

fragment = image[250:350, 200:400].copy()  # Kopiujemy fragment  
image[200:300, 200:400] = fragment  # Wklejamy go gdzie indziej

cv2.imshow("Po wklejeniu fragmentu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 7

h_step = h // 3
w_step = w // 3

for i in range(3):
    for j in range(3):
        part = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]
        cv2.imshow(f"Czesc ({i}, {j})", part)
        cv2.waitKey(500)  # Pokazujemy każdą część na 500ms

cv2.waitKey(0)
# zad 8

for x in range(0, w-100, 10):  
    roi_moving = image[100:200, x:x+100]  # Przesuwamy ROI w poziomie  
    cv2.imshow("Przesuwanie ROI", roi_moving)
    cv2.waitKey(100)  # Pokazujemy każdą część na 100ms

cv2.waitKey(0)

# zad 9
cropped = image[150:450, 120:420]  
cv2.imwrite("cropped_image.jpg", cropped) 
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()