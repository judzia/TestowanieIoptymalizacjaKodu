import cv2
import numpy as np

# ZAD1
image = cv2.imread('shapes2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)

# dwa rozne elementy stryukturalne
# kwadratowy i eliptyczny
kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# erozja dwoma kernelami
erosion_square = cv2.erode(image, kernel_square, iterations=1)
erosion_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)

# wyniki
cv2.imshow("Erosion - Square Kernel", erosion_square)
cv2.imshow("Erosion - Elliptical Kernel", erosion_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' Erozja z kernelem kwadratowym powoduje bardziej "agresywne" usuwanie krawędzi - obiekty szybciej się zmniejszają i tracą szczegóły.
Kernel eliptyczny lepiej zachowuje zaokrąglone kształty - erozja jest łagodniejsza. WIDAC TO SZCZEGOLNIE NA NAPISACH AKURAT!'''

# ZAD 2

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
results = []

# dylatacja z różną liczbą iteracji
for i in range(1, 6):
    dilated = cv2.dilate(image, kernel, iterations=i)
    cv2.imshow(f"Dilated {i}x", dilated)
    results.append((i, np.count_nonzero(dilated)))  # Liczba białych pikseli

cv2.waitKey(0)
cv2.destroyAllWindows()

# zmiany liczby białych pikseli
for i, count in results:
    print(f"Iteracja {i}: {count} białych pikseli")

'''Dylatacja pogrubia obiekty - z każdą iteracją liczba białych pikseli rośnie. 
W przypadku cienkich linii szybko następuje ich połączenie lub wypełnienie przerw między nimi. 
Tutaj już na trzeciej iteracji napisy jak i kształty są niewidoczne.'''

# ZAD 3

noisy = cv2.imread('szum.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Noisy Image", noisy)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opening = cv2.morphologyEx(noisy, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening - Kernel {size}", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Operacja otwarcia skutecznie usuwa losowe białe/ciemne plamki szumu. 
# Zmiana rozmiaru kernela wpływa na efektywność usuwania szumów - większe kernela lepiej radzą sobie z większymi plamkami.
# Jednak zbyt duży kernel może usunąć szczegóły obrazu.

# ZAD 4

image = cv2.imread('blabla.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# Różne kształty elementów strukturalnych
shapes = {
    "Prostokatny": cv2.MORPH_RECT,
    "Eliptyczny": cv2.MORPH_ELLIPSE
}

# Kernel o średnim rozmiarze (bo tak)
kernel_size = (5, 5)

for name, shape in shapes.items():
    kernel = cv2.getStructuringElement(shape, kernel_size)
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    final = cv2.bitwise_not(closed)
    
    cv2.imshow(f"[{name}] Zamkniecie (polaczone litery)", final)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''Operacja zamknięcia skutecznie wypełnia dziury w obiektach. 
Zastosowanie różnych kształtów elementów strukturalnych wpływa na sposób łączenia liter.
Prostokątny lepiej łączy litery w poziomie, a eliptyczny w pionie.
Zaleca się dobierać rozmiar kernela do rozmiaru dziur w obiektach.'''

# ZAD 5

image = cv2.imread('shapes.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Definicja kształtów elementów strukturalnych
shapes = {
    "Kwadrat": cv2.MORPH_RECT,
    "Krzyz": cv2.MORPH_CROSS,
    "Elipsa": cv2.MORPH_ELLIPSE
}

# Rozmiar kernela
kernel_size = (5, 5)

# Dla każdego kształtu wykonaj wszystkie operacje
for name, shape in shapes.items():
    kernel = cv2.getStructuringElement(shape, kernel_size)
    erosion = cv2.erode(binary, kernel)
    dilation = cv2.dilate(binary, kernel)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    # Wyświetlanie wyników
    cv2.imshow(f"[{name}] Erozja", erosion)
    cv2.imshow(f"[{name}] Dylatacja", dilation)
    cv2.imshow(f"[{name}] Otwarcie", opening)
    cv2.imshow(f"[{name}] Zamkniecie", closing)
    cv2.imshow(f"[{name}] Gradient", gradient)
    cv2.waitKey(0)

cv2.destroyAllWindows()

'''Kwadrat (MORPH_RECT) daje równomierne przekształcenia w każdą stronę.
Krzyż (MORPH_CROSS) działa mocniej na pionowe i poziome struktury, zostawiając więcej detali na skosach.
Elipsa (MORPH_ELLIPSE) lepiej zachowuje kształty zaokrąglone – mniej agresywna od kwadratu.'''

# ZAD 6

# Wczytanie zeskanowanego dokumentu z szumem
image3 = cv2.imread('szumyk.jfif', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image3, 150, 255, cv2.THRESH_BINARY_INV)

kernelik= cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernelik)


closed = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernelik)


final = cv2.bitwise_not(closed)

cv2.imshow("Oryginalny zeskanowany", image3)
cv2.imshow("Po binaryzacji", binary)
cv2.imshow("Po otwarciu", cleaned)
cv2.imshow("Po zamknieciu", final)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''po otwarciu szum zrobil sie czarny z białym tłem, a po zamknięciu biały z czarnym tłem.'''