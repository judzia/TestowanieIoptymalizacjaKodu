import cv2
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
# Zestawienie wszystkich efektow pozwala latwo porownać rozmycia.
# Najbardziej naturalne efekty przy zachowaniu detali daje rozmycie Gaussa i bilateralne.