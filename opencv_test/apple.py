# Importing Libraries
import cv2
import numpy as np

# Processing Images
image = cv2.imread("rottenapple.jpg")  # Change the file name to your apple image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged = cv2.Canny(blurred_image, 50, 150)

# Find Contours and Bounding Rectangle:
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cont = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_cont)

# Draw a green rectangle around the focused area
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Showing Processed Image
cv2.imshow('Apple', image)

# Convert Image to HSV and Create Color Masks:
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])  # Adjust the color thresholds for an apple
upper_red = np.array([10, 255, 255])

lower_green = np.array([35, 100, 100])  # Adjust the color thresholds for an apple
upper_green = np.array([85, 255, 255])

red_mask = cv2.inRange(hsv, lower_red, upper_red)
green_mask = cv2.inRange(hsv, lower_green, upper_green)

# Calculating Percentage
red_pixels = np.count_nonzero(red_mask)
green_pixels = np.count_nonzero(green_mask)
total_pixels = w * h

red_percentage = (red_pixels / total_pixels) * 100
green_percentage = (green_pixels / total_pixels) * 100
unripe_percentage = 100 - red_percentage - green_percentage

# Checking ripeness
ripe_limit = 50
rotten_limit = 25

if red_percentage >= ripe_limit and green_percentage <= rotten_limit:
    print("Ripe")
elif red_percentage >= ripe_limit and green_percentage > rotten_limit:
    print("Ripe but partly rotten")
elif red_percentage < ripe_limit and green_percentage > rotten_limit:
    print("Fully Rotten")
elif unripe_percentage >= ripe_limit:
    print("Unripe")
else:
    print("Rotten")

# Printing
print(f"Red Percentage: {red_percentage:.2f}%")
print(f"Green Percentage: {green_percentage:.2f}%")
print(f"Unripe Percentage: {unripe_percentage:.2f}%")

cv2.waitKey(0)
cv2.destroyAllWindows()
