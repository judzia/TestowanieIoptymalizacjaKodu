import cv2

# ZAD 1
image = cv2.imread("kotecek.jpg")  

if image is None:
    print("Blad: nie można wczytac obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Wczytany obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ZAD 2
(h, w, c) = image.shape
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')  # Dla kolorowego zdjęcia powinno być 3 (RGB)

# ZAD 3
image_gray = cv2.imread("wakacjeKotek.png", cv2.IMREAD_GRAYSCALE)
print(f'Gray image shape: {image_gray.shape}')  # Powinien mieć tylko 2 wymiary (wysokość, szerokość)
channels_gray = 1 if len(image_gray.shape) == 2 else image_gray.shape[2]
print(f'Channels (gray): {channels_gray}')  # Dla obrazu w skali szarości powinno być 1

# ZAD 4
cv2.imwrite("wakacjeKotek_gray.png", image_gray)
print("Obraz w skali szarosci zapisano jako wakacjeKotek_gray.png")

# ZAD 5
cv2.imshow("Kolorowy obraz", image)
cv2.imshow("Obraz w skali szarosci", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ZAD 6
cv2.namedWindow("Dostosowane okno", cv2.WINDOW_NORMAL)
cv2.imshow("Dostosowane okno", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
