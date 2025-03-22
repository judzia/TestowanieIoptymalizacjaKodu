import cv2
import imutils
import numpy as np

# zad 1

image = cv2.imread("piesek.jpeg") 
cv2.imshow("Original", image)
cv2.waitKey(0)

M1 = np.float32([[1, 0, 30], [0, 1, 40]])
shifted1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Right 30px, Down 40px", shifted1)
cv2.waitKey(0)

# zad 2

M2 = np.float32([[1, 0, -20], [0, 1, -50]])
shifted2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Left 20px, Up 50px", shifted2)
cv2.waitKey(0)

# zad 3

tx = int(image.shape[1] / 2) + 50  # szerokość
ty = int(image.shape[0] / 2) + 50  # wysokość
M3 = np.float32([[1, 0, tx], [0, 1, ty]])
shifted3 = cv2.warpAffine(image, M3, (image.shape[1], image.shape[0]))
cv2.imshow(f"Shifted Large ({tx}px, {ty}px)", shifted3)
cv2.waitKey(0)

# zad 4

shifted4 = imutils.translate(image, 100, 50)  # 100px w prawo, 50px w dół
cv2.imshow("Shifted imutils Right 100px, Down 50px", shifted4)
cv2.waitKey(0)

# Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
#Czy zauważyłeś różnice?
# Różnica polega na tym, że funkcja imutils.translate() przesuwa obraz w sposób bardziej "naturalny",
# a funkcja cv2.warpAffine() przesuwa obraz w sposób "sztywny".

# zad 5

try:
    tx_user = int(input("Podaj wartość przesunięcia w poziomie (tx): "))
    ty_user = int(input("Podaj wartość przesunięcia w pionie (ty): "))
except ValueError:
    print("Błędne dane wejściowe! Podaj liczby całkowite.")
    tx_user, ty_user = 0, 0  

M4 = np.float32([[1, 0, tx_user], [0, 1, ty_user]])
shifted5 = cv2.warpAffine(image, M4, (image.shape[1], image.shape[0]))
cv2.imshow(f"Dynamic Shift ({tx_user}px, {ty_user}px)", shifted5)
cv2.waitKey(0)



# Przesunięcie o te same wartości obiema metodami:
M5 = np.float32([[1, 0, 100], [0, 1, 50]])
shifted_warpAffine = cv2.warpAffine(image, M5, (image.shape[1], image.shape[0]))
shifted_imutils = imutils.translate(image, 100, 50)

cv2.imshow("WarpAffine Shifted", shifted_warpAffine)
cv2.imshow("Imutils Shifted", shifted_imutils)

# roznice sa minimalne

cv2.waitKey(0)
cv2.destroyAllWindows()