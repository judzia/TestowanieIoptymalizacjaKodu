import cv2

# ---- Zadanie 1: Odbicie poziome ----
image = cv2.imread("example.jpg")
if image is None:
    print("Błąd: Nie udało się wczytać obrazu!")
else:
    flipped_horizontally = cv2.flip(image, 1)
    cv2.imshow("Oryginał", image)
    cv2.waitKey(0)
    cv2.imshow("Odbicie poziome", flipped_horizontally)
    cv2.waitKey(0)
    
    # ---- Zadanie 2: Odbicie pionowe ----
    flipped_vertically = cv2.flip(image, 0)
    cv2.imshow("Odbicie pionowe", flipped_vertically)
    cv2.waitKey(0)
    
    # ---- Zadanie 3: Odbicie względem obu osi ----
    flipped_both = cv2.flip(image, -1)
    cv2.imshow("Odbicie względem obu osi", flipped_both)
    cv2.waitKey(0)
    
    # ---- Zadanie 4: Odbicie wybranego obszaru ----
    h, w = image.shape[:2]
    region = image[h//4:3*h//4, w//4:3*w//4]  # Środkowy obszar
    flipped_region = cv2.flip(region, 1)
    image_with_flipped_region = image.copy()
    image_with_flipped_region[h//4:3*h//4, w//4:3*w//4] = flipped_region
    cv2.imshow("Odbicie wybranego obszaru", image_with_flipped_region)
    cv2.waitKey(0)
    
    # ---- Zadanie 5: Odbicie na podstawie wyboru użytkownika ----
    choice = int(input("Wybierz sposób odbicia (0 - pionowe, 1 - poziome, -1 - oba): "))
    if choice in [0, 1, -1]:
        flipped_user_choice = cv2.flip(image, choice)
        cv2.imshow("Odbicie na podstawie wyboru użytkownika", flipped_user_choice)
        cv2.waitKey(0)
    else:
        print("Nieprawidłowy wybór.")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
