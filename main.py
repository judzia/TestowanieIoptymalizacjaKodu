import cv2

# Zad 1 
image = cv2.imread("kiciaNaWakacjach.jpg")

pixel_00 = image[0,0]
print(f"1. Wartosc pikselu w punkcie(0,0): R={pixel_00[2]}, G = {pixel_00[1]}, B = {pixel_00[0]}")

# Zad 2
cv2.imshow("Kicia na wakacjach", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image[-1, -1] = (0,0,255)
cv2.imshow("Po zmianie piksela", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zad 3

h, w, _ = image.shape
center_x, center_y = w//2, h//2
center_pixel = image[center_y, center_x]
print(f"3.Srodek obrazka: ({center_x}, {center_y}), kolor: R = {center_pixel[2]}, G = {center_pixel[2]}, B = {center_pixel[0]}")
#print(f"3. Wymiary obrazka: {w}x{h}, srodek obrazka: ({center_x}, {center_y})")

# Zad 4 

x = int(input("Podaj wspolrzedna x: "))
y = int(input("Podaj wspolrzedna y: "))

if 0 <= x < w and 0 <= y <h:
    image[y, x] = (0,0,0)
    cv2.imshow("Po zmianie piksela na czarny", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bledne wspolrzedne! Wprowadz wartosci w zakresie obrazu.")

# zad 5

top_left = image[0:center_y, 0:center_x]
top_right = image[0:center_y, center_x:w]
bottom_left = image[center_y:h, 0:center_x]
bottom_right = image[center_y:h, center_x:w]
    
# Wyświetlenie każdej ćwiartki osobno
cv2.imshow("Top Left", top_left)
cv2.imshow("Top Right", top_right)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Bottom Right", bottom_right)

# Pokolorowanie górnej lewej ćwiartki na niebiesko
top_left[:] = (255, 0, 0)
    
# Ponowne wyświetlenie podzielonych obrazów po zmianie
cv2.imshow("Top Left (Blue)", top_left)
cv2.imshow("Top Right", top_right)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Bottom Right", bottom_right)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 6

start_x, start_y = center_x - 50, center_y - 50
end_x, end_y = center_x + 50, center_y + 50
image[start_y:end_y, start_x:end_x] = (0, 0, 255)
cv2.imshow("Po zmianie pikseli w kwadracie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 7

crop = image[center_y - h//6:center_y + h//6, center_x - w//6:center_x + w//6]
cv2.imshow("Cropped Center", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


# zad 8
cv2.imshow("Przed zmiana pikseli w wierszu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

if h > 100:
    image[100, :] = (0, 255, 0)

cv2.imshow("Po zmianie pikseli w wierszu 100", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 # zad 9
image[50:100, 50:100] = (255, 255, 255)
    
# zad 10
b1, g1, r1 = image[50, 50]
b2, g2, r2 = image[200, 200]
print(f'Roznice: R={abs(r1 - r2)}, G={abs(g1 - g2)}, B={abs(b1 - b2)}')
    
# zad 11
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
print(f'Najjasniejszy piksel: {maxLoc}, Wartosc: {maxVal}')
    
# Wyświetlenie końcowego obrazu
cv2.imshow("Final Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
