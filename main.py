import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread("gakster.jpg")

# 1a. Zwiększanie jasności o 50 - NumPy
temp_np = np.ones(image.shape, dtype="uint8") * 50
brighter_numpy = image + temp_np

# 1b. Zwiększanie jasności o 50 - OpenCV
brighter_cv2 = cv2.add(image, temp_np)

cv2.imshow("Brighter NumPy", brighter_numpy)
cv2.imshow("Brighter OpenCV", brighter_cv2)
cv2.waitKey(0)

# 2a. Symulacja "przepalenia" obrazu - NumPy
overexposed_numpy = image + 150
cv2.imshow("Overexposed NumPy", overexposed_numpy)


# 2b. Przepalenie - OpenCV
overexposed_cv2 = cv2.add(image, np.ones(image.shape, dtype="uint8") * 150)
cv2.imshow("Overexposed OpenCV", overexposed_cv2)
cv2.waitKey(0)

# 3a. Przyciemnianie obrazu o 80 - NumPy
darker_numpy = image - 80
cv2.imshow("Darker NumPy", darker_numpy)

# 3b. Przyciemnianie obrazu o 80 - OpenCV
darker_cv2 = cv2.subtract(image, np.ones(image.shape, dtype="uint8") * 80)
cv2.imshow("Darker OpenCV", darker_cv2)
cv2.waitKey(0)

# 4. Filtr Instagram - zmiany kolorow
image_filtered = image.copy()
image_filtered[:, :, 2] = cv2.add(image[:, :, 2], 30)  # Czerwony
image_filtered[:, :, 1] = cv2.subtract(image[:, :, 1], 20)  # Zielony
image_filtered[:, :, 0] = cv2.add(image[:, :, 0], 10)  # Niebieski
cv2.imshow("Instagram Filter", image_filtered)
cv2.waitKey(0)

# 5. Detekcja zmian w obrazie
rows, cols = image_filtered.shape[:2]
M = np.float32([[1, 0, 10], [0, 1, 10]])  # Macierz przesunięcia
image_shifted = cv2.warpAffine(image_filtered, M, (cols, rows))

cv2.imshow("Instagram Filter (Shifted)", image_shifted)
cv2.imwrite("image2.jpg", image_shifted)


image2 = cv2.imread("image2.jpg")

# sprawdzenie czy obrazy maja ten sam rozmiar w ogole
if image.shape != image2.shape:
    print("Obrazy maja rozne rozmiary, dopasowuje")
    image2 = cv2.resize(image2, (image.shape[1], image.shape[0]))

changes = cv2.absdiff(image, image2)

# zeby nie bylo czarnego ekranu jak malo zmian
if np.all(changes == 0):
    print("Obrazy są identyczne! Brak wykrytych różnic.")
else:
    cv2.imshow("Differences", changes)
    cv2.waitKey(0)

cv2.destroyAllWindows()