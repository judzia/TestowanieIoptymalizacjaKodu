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

#image[:h//2, :w//2] = (255,0,0)
#cv2.imshow("Po kolorowaniu cwiartki", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


[cX,cY] = [w//2, h//2]
top_left = image[0:cY, 0:cX]
top_right = image[0:cY, cX:w]
bottom_left = image[cY:h, 0:cX]
bottom_right = image[cY:h, cX:w]

image[0:cY, 0:cX] = (255,0,0)

cv2.imshow("Zmieniony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 6

half_size = 50
image[center_y-half_size:center_x+half_size, center_x-half_size:center_x+half_size] = (0,0,255)
cv2.imshow("Po wypelnieniu srodka", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

