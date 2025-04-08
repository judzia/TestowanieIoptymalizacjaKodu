import cv2
import numpy as np

# ---- Zadanie 1a: Trójkąt i operacje bitowe ----
triangle = np.zeros((300, 300), dtype="uint8")
pts = np.array([[150, 25], [275, 275], [25, 275]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Triangle", triangle)
cv2.waitKey(0)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("Triangle AND Circle", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("Triangle OR Circle", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("Triangle XOR Circle", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT Triangle", bitwiseNot)
cv2.waitKey(0)

# ---- Zadanie 1b: Przesunięcie trójkąta ----
triangle_shifted = np.zeros((300, 300), dtype="uint8")
pts_shifted = np.array([[200, 75], [300, 275], [100, 275]], np.int32)
pts_shifted = pts_shifted.reshape((-1, 1, 2))
cv2.fillPoly(triangle_shifted, [pts_shifted], 255)
cv2.imshow("Shifted Triangle", triangle_shifted)
cv2.waitKey(0)

bitwiseAnd_shifted = cv2.bitwise_and(triangle_shifted, circle)
cv2.imshow("Shifted Triangle AND Circle", bitwiseAnd_shifted)
cv2.waitKey(0)

bitwiseOr_shifted = cv2.bitwise_or(triangle_shifted, circle)
cv2.imshow("Shifted Triangle OR Circle", bitwiseOr_shifted)
cv2.waitKey(0)

bitwiseXor_shifted = cv2.bitwise_xor(triangle_shifted, circle)
cv2.imshow("Shifted Triangle XOR Circle", bitwiseXor_shifted)
cv2.waitKey(0)

bitwiseNot_shifted = cv2.bitwise_not(triangle_shifted)
cv2.imshow("NOT Shifted Triangle", bitwiseNot_shifted)
cv2.waitKey(0)

# ---- Zadanie 2: Wykrywanie różnic między obrazami ----
img1 = cv2.imread("obrazek1.jpg")
img2 = cv2.imread("obrazek4.jpg")

if img1 is None or img2 is None:
    print("Błąd: Nie udało się wczytać jednego z obrazów do porównania!")
else:
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img2_gray = cv2.resize(img2_gray, (img1_gray.shape[1], img1_gray.shape[0]))
    
    img1_bin = cv2.threshold(img1_gray, 128, 255, cv2.THRESH_BINARY)[1]
    img2_bin = cv2.threshold(img2_gray, 128, 255, cv2.THRESH_BINARY)[1]

    xor_result = cv2.bitwise_xor(img1_bin, img2_bin)
    cv2.imshow("Różnice (XOR)", xor_result)
    

cv2.waitKey(0)
cv2.destroyAllWindows()
