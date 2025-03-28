import cv2
import imutils

image = cv2.imread("kicia.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

# zad 1

resized_half = cv2.resize(image, (int(image.shape[1] / 2), int(image.shape[0] / 2)), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized half", resized_half)
cv2.waitKey(0)

# zad 2
resized_double = cv2.resize(image, (int(image.shape[1] * 2), int(image.shape[0] * 2)), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized 200%", resized_double)
cv2.waitKey(0)


# zad 3

resized_fixed = cv2.resize(image, (200, 300), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized to 200x300", resized_fixed)
cv2.waitKey(0)

# zad 4

methods = {
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_AREA", cv2.INTER_AREA),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
}

for (name, method) in methods:
    resized = cv2.resize(image, (image.shape[1] * 3, image.shape[0] * 3), interpolation=method)
    cv2.imshow(f"Method: {name}", resized)

# zad 5

resized_width = imutils.resize(image, width=500)
cv2.imshow("Width 500px", resized_width)
cv2.waitKey(0)

# zad 6

resized_height = imutils.resize(image, height=400)
cv2.imshow("Resized height", resized_height)
cv2.waitKey(0)

# zad 7
resized_down = cv2.resize(image, (image.shape[1] // 5, image.shape[0] // 5), interpolation=cv2.INTER_AREA)
cv2.imshow("Scaled Down 5x (INTER_AREA)", resized_down)
cv2.waitKey(0)

# zad 8

resized_cubic = cv2.resize(image, (image.shape[1] * 4, image.shape[0] * 4), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(image, (image.shape[1] * 4, image.shape[0] * 4), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Scaled Up 4x (INTER_CUBIC)", resized_cubic)
cv2.imshow("Scaled Up 4x (INTER_LANCZOS4)", resized_lanczos)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad 9

for scale in range(100, 301, 20):
    resized_loop = cv2.resize(image, (image.shape[1] * scale // 100, image.shape[0] * scale // 100), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"Resized {scale}%", resized_loop)
    cv2.waitKey(500)


# zad 10

resized_save = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized_save)
cv2.imshow("Saved Resized Image", resized_save)

cv2.waitKey(0)
cv2.destroyAllWindows()

