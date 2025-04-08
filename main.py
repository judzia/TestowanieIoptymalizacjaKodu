import cv2

import numpy as np

# ZAD 1
# a. Wczytaj obraz
image = cv2.imread("kwiatki.jpg")

# b. Rozdziel kanaly
B, G, R = cv2.split(image)

# c. Wyswietl kanaly
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)

# d. Zapisz jako osobne obrazy
cv2.imwrite("kanal_blue.jpg", B)
cv2.imwrite("kanal_green.jpg", G)
cv2.imwrite("kanal_red.jpg", R)
cv2.destroyAllWindows()

# ZAD 2

image = cv2.imread("kwiot.jpg")
B, G, R = cv2.split(image)

# Wyswietl kanaly
cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ZAD 3

# a. Zamiana kolejnosci kanalow
RGB_swapped = cv2.merge([R, B, G])
cv2.imshow("Swapped RBG", RGB_swapped)

# b. Ustawienie jednego kanalu na zero
zero_channel = B.copy()
zero_channel[:] = 0
merged = cv2.merge([B, G, zero_channel])
cv2.imshow("Zeroed Red", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ZAD 4
# a. Wzmocnij czerwony kanal
R_boosted = cv2.add(R, 50)  # przyciecie do max 255 zapewnia cv2.add
image_boosted = cv2.merge([B, G, R_boosted])
cv2.imshow("Boosted Red", image_boosted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ZAD 5

# a. Wczytaj obraz
image = cv2.imread("AUTKO.jpg")
B, G, R = cv2.split(image)

# Zakladamy, ze czerwony kolor zawiera sie w tym zakresie
lower_red = np.array([0, 0, 100])
upper_red = np.array([80, 80, 255])
mask = cv2.inRange(image, lower_red, upper_red)

R_boosted = R.copy()
R_boosted[mask > 0] = np.clip(R[mask > 0] + 50, 0, 255)

modified = cv2.merge([B, G, R_boosted])
cv2.imshow("Red boosted with mask", modified)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ZAD 6

# a. Wczytaj logo
logo = cv2.imread("lougo.png")
B, G, R = cv2.split(logo)

# b. Zamien kolory – niebieski z czerwonym
swapped_logo = cv2.merge([R, G, B])
cv2.imshow("Red-Blue Swapped", swapped_logo)

# c. usun kanal
zero = G.copy()
zero[:] = 0
no_green_logo = cv2.merge([B, zero, R])
cv2.imshow("No Green", no_green_logo)

cv2.waitKey(0)
cv2.destroyAllWindows()