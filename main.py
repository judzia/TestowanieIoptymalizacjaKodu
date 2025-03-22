import cv2
import numpy as np

# zadanie 1

canvas = np.zeros((300, 300, 3), dtype="uint8")
blue = (255, 0, 0)
center = (canvas.shape[1] // 2, canvas.shape[0] // 2)
bottom_right = (300, 300)

cv2.line(canvas, center, bottom_right, blue,2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# zadanie 2

canvas2 = np.zeros((400, 400, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)



cv2.rectangle(canvas2, (0,0), (100, 50), green, -1)
cv2.rectangle(canvas2, center, (400,400), red, 3)
cv2.imshow("Canvas2", canvas2)
cv2.waitKey(0)

# zadanie 3

canvas3 = np.zeros((300, 300, 3), dtype="uint8")
cv2.circle(canvas3, (40,40), 40, blue, 2)

cv2.circle(canvas3, center , 60, red, 2)

cv2.imshow("Canvas", canvas3)
cv2.waitKey(0)

pink = (205, 192, 253)
violet = (250, 60, 190)

# zadanie 4

canvas4 = np.zeros((300, 300, 3), dtype="uint8")

cv2.rectangle(canvas4, (100,100) , (200,200), pink , -1)
cv2.circle(canvas4, (150,150), 30, violet, 2)

cv2.imshow("Canvas", canvas4)
cv2.waitKey(0)

# zadanie 5

pretty_green = (133, 205, 5)

canvas5 = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas5.shape[1] // 2, canvas5.shape[0] // 2)

for size in range(20, 220, 20):
    top_left = (centerX - size // 2, centerY - size // 2)
    bottom_right = (centerX + size // 2, centerY + size // 2)

    cv2.rectangle(canvas5, top_left, bottom_right, pretty_green, 1)

cv2.imshow("Canvas", canvas5)
cv2.waitKey(0)

# zadanie 6 

image = cv2.imread("chop1.jpg")
38,26
cv2.circle(image, (285, 137), 12, (0, 0, 255), -1)
cv2.circle(image, (340, 160), 12, (0, 0, 255), -1)
cv2.rectangle(image, (270, 195), (335, 215), (0, 255, 0), -1)
cv2.circle(image, (305, 160), 100, (255, 0, 0), 2)

cv2.imshow("zadanko 6", image)
cv2.imshow
cv2.waitKey(0)