#importing Libraries
import cv2
import numpy as np

#Processing Images
image = cv2.imread("banana.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged = cv2.Canny(blurred_image, 50, 150)

#Find Contours and Bounding Rectangle:
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cont = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_cont)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#Showing Processed Image
cv2.imshow('Banana', image)

#Convert Image to HSV and Create Color Masks:
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_brown = np.array([0, 100, 100])
upper_brown = np.array([20, 255, 255])

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)

#Calculating Percentage
yellow_pixels = np.count_nonzero(yellow_mask)
brown_pixels = np.count_nonzero(brown_mask)
total_pixels = w * h

yellow_percentage = (yellow_pixels / total_pixels) * 100
brown_percentage = (brown_pixels / total_pixels) * 100
unripe_percentage = 100 - yellow_percentage - brown_percentage

#Checking ripeness
ripe_limit = 50
rotten_limit = 25

if yellow_percentage >= ripe_limit and brown_percentage <= rotten_limit:
    print("Ripe")
elif yellow_percentage >= ripe_limit and brown_percentage > rotten_limit:
    print("Ripe but partly rotten")
elif yellow_percentage < ripe_limit and brown_percentage > rotten_limit:
    print("Fully Rotten")
elif unripe_percentage >= ripe_limit:
    print("Unripe")
else:
    print("Rotten")

#Printing
print(f"Yellow Percentage: {yellow_percentage:.2f}%")
print(f"Brown Percentage: {brown_percentage:.2f}%")
print(f"Unripe Percentage: {unripe_percentage:.2f}%")

cv2.waitKey(0)
cv2.destroyAllWindows()
