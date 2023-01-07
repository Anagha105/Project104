import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
cv2.putText(img, "Mercury", (110, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Venus", (200, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Earth", (300, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Mars", (400, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Jupiter", (550, 90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Saturn", (800, 110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Uranus", (950, 110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Neptune", (1100, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("solar_system_with_names.jpg", img)