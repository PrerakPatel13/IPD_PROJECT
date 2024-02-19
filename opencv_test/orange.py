#importing Libraries
import cv2
import numpy as np

#Processing Images
image = cv2.imread("orange.png")  # Change the file name to your orange image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged = cv2.Canny(blurred_image, 50, 150)

#Find Contours and Bounding Rectangle:
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cont = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_cont)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#Showing Processed Image
cv2.imshow('Orange', image)

#Convert Image to HSV and Create Color Masks:
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_orange = np.array([0, 100, 100])  # Adjust the color thresholds for an orange
upper_orange = np.array([20, 255, 255])

orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)

#Calculating Percentage
orange_pixels = np.count_nonzero(orange_mask)
total_pixels = w * h

orange_percentage = (orange_pixels / total_pixels) * 100

#Checking ripeness
ripe_limit = 50
rotten_limit = 25

if orange_percentage >= ripe_limit:
    print("Ripe")
elif orange_percentage < ripe_limit and orange_percentage >= rotten_limit:
    print("Ripe but partly rotten")
else:
    print("Fully Rotten")

#Printing
print(f"Orange Percentage: {orange_percentage:.2f}%")

cv2.waitKey(0)
cv2.destroyAllWindows()
