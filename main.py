import cv2

# Zaladuj obraz
image = cv2.imread("lilDog.jpg")
cv2.imshow("Oryginalny obraz", image)

# Lista parametrow (rozmiary kernela / inne parametry dla bilateralFilter)
kernel_sizes = [(3, 3), (9, 9), (15, 15)]
median_sizes = [3, 9, 15]
bilateral_params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

# -----------------------------
# 1a i: Rozmycie proste (cv2.blur)
for (kX, kY) in kernel_sizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Rozmycie proste ({kX}, {kY})", blurred)
    # Komentarz:
    # - Metoda dobrze wygladza, ale rozmywa tez szczegoly i krawedzie.
    # - Im wiekszy kernel, tym mocniejsze rozmycie.
cv2.waitKey(0)  

# -----------------------------
# 1a ii: Rozmycie Gaussa (cv2.GaussianBlur)
for (kX, kY) in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Rozmycie Gaussa ({kX}, {kY})", blurred)
    # Komentarz:
    # - Gauss lepiej zachowuje szczegoly niz rozmycie proste.
    # - Wagi maleja wraz z odlegloscia od srodka, wiec efekt jest bardziej "naturalny".
cv2.waitKey(0)

# -----------------------------
# 1a iii: Rozmycie medianowe (cv2.medianBlur)
for k in median_sizes:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Rozmycie medianowe ({k})", blurred)
    # Komentarz:
    # - Medianowe bardzo dobrze usuwa szum (np. "sol i pieprz").
    # - Czasami moze powodowac artefakty przy duzych wartosciach kernela.
cv2.waitKey(0)

# -----------------------------
# 1a iv: Rozmycie dwustronne (cv2.bilateralFilter)
for (d, sigmaColor, sigmaSpace) in bilateral_params:
    blurred = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imshow(f"Rozmycie dwustronne (d={d}, sc={sigmaColor}, ss={sigmaSpace})", blurred)
    # Komentarz:
    # - Bardzo dobra metoda do zachowania krawedzi!
    # - Redukuje szum, ale nie rozmywa konturow jak inne metody.
    # - Najwolniejsza z metod (obliczeniowo ciezka).

cv2.waitKey(0)
cv2.destroyAllWindows()

# podsumowanie:
#cv2.blur – szybka, ale bardzo rozmywa.
#cv2.GaussianBlur – naturalniejsze rozmycie, ale trochę mniej skuteczne na szum niż medianowe.
#cv2.medianBlur – skuteczne na szum, ale może zniekształcić tekstury.
#cv2.bilateralFilter – najdokładniejsza, ale też najwolniejsza.

# zad 2 

# w sumie to troche je zrobilam juz wyzej!
# takze ponowie komentarze:
#i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
#ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?

# odpowiedzi:
# i. Im wiekszy kernel, tym mocniejsze rozmycie. Rozmycie proste i Gaussa sa bardziej widoczne przy wiekszych kernelach.
# Rozmycie medianowe daje najlepsze efekty przy srednich rozmiarach kernela (3-9), a rozmycie dwustronne najlepiej zachowuje szczegoly przy wiekszych wartosciach d (np. 11-21).
# Rozmycie Gaussa i proste sa mniej skuteczne na szum, ale bardziej naturalne.


# Jaki rozmiar kernela jest optymalny?
# - Gaussian: (5,5) lub (9,9) to zloty srodek.
# - Median: 5 lub 9, zaleznie od poziomu szumu.
# - Bilateral: zalezy od parametrow — warto testowac interaktywnie.

# zad 3

image3 = cv2.imread("fnafik.jpg")  
cv2.imshow("Original", image3)

# Parametry do testowania
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image3, diameter, sigmaColor, sigmaSpace)
    title = f"Bilateral d={diameter}, sc={sigmaColor}, ss={sigmaSpace}"
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# KOMENTARZE (odpowiedzi):
# i. Tak, rozmycie dwustronne skutecznie redukuje szum przy zachowaniu krawędzi.
# ii. W porównaniu do blur i GaussianBlur, krawędzie są lepiej zachowane.
# iii. Najlepsze wyniki dawały wartości średnie: (11, 41, 21) – balans między wygładzeniem a ostrością.

# zad 4 

image4 = cv2.imread("gasseten.jpg")  
cv2.imshow("Original", image4)

cv2.waitKey(0)
# Rozne rozmycia
kernel_sizes = [(3, 3), (5, 5), (9, 9)]

# Rozmycie proste
for k in kernel_sizes:
    blurred = cv2.blur(image4, k)
    cv2.imshow(f"Blur {k}", blurred)

cv2.waitKey(0)
# Rozmycie Gaussowskie
for k in kernel_sizes:
    blurred = cv2.GaussianBlur(image4, k, 0)
    cv2.imshow(f"GaussianBlur {k}", blurred)

cv2.waitKey(0)
# Rozmycie medianowe – potrzebuje tylko jednej wartosci
for k in [3, 5, 9]:
    blurred = cv2.medianBlur(image4, k)
    cv2.imshow(f"MedianBlur {k}", blurred)

cv2.waitKey(0)
# Rozmycie dwustronne – tylko 1 zestaw dla porownania
bilateral = cv2.bilateralFilter(image4, 11, 41, 21)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# KOMENTARZE:
# Rozmycie mocno wplywa na czytelnosc tekstu.
# Prosty blur i GaussianBlur szybko rozmywają krawedzie znakow.
# MedianBlur nieco lepiej je zachowuje, ale tez znieksztalca.
# BilateralFilter najlepiej zachowuje ostre kontury liter.
# Wniosek: Jesli zalezy nam na zachowaniu tekstu, najlepszy jest bilateralny filtr.
# PLUS Mam duzy tekst takze nie ma problemu z jego odczytaniem.


# zad 5

image = cv2.imread("lilDog.jpg")  
cv2.imshow("Original", image)

# rozmycie Gaussa
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Wykrywanie krawedzi (Canny) po rozmyciu
edges = cv2.Canny(blurred, 30, 100)
cv2.imshow("Canny after Gaussian Blur", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# KOMENTARZ:
# Rozmycie Gaussa pomaga lepiej wykryc rzeczywiste krawedzie bez falszywych z szumu.


# zad 6


image6 = cv2.imread("perspektywa.jpg")  
cv2.imshow("Original", image6)

# Rozne rozmycia na tym samym obrazie
cv2.imshow("Blur", cv2.blur(image6, (9, 9)))
cv2.imshow("GaussianBlur", cv2.GaussianBlur(image6, (9, 9), 0))
cv2.imshow("MedianBlur", cv2.medianBlur(image6, 9))
cv2.imshow("Bilateral", cv2.bilateralFilter(image6, 11, 41, 21))

cv2.waitKey(0)
cv2.destroyAllWindows()

# KOMENTARZ:
# Zestawienie wszystkich efektow pozwala latwo porownac rozmycia.
# Najbardziej naturalne efekty przy zachowaniu detali daje rozmycie Gaussa i bilateralne.