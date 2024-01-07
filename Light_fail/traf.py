import cv2
import numpy as np
import time

# Create function to display images in Google Colab
def display_image(image):
    cv2.imshow('traffic light',cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Create blank background image
img = np.zeros((500, 500, 3), np.uint8)

# Define traffic light colors
green = (0, 255, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)

# Initial color is green
color = green

# Set countdown timer
timer = 10

while True:
    # Draw colored rectangles for traffic light
    cv2.rectangle(img, (200, 50), (300, 150), red, -1)
    cv2.rectangle(img, (200, 200), (300, 300), yellow, -1)
    cv2.rectangle(img, (200, 350), (300, 450), green, -1)

    # Display countdown text
    cv2.putText(img, str(timer), (225, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    # Display image
    display_image(img)

    # Count down each second
    if timer > 0:
        timer -= 1
        time.sleep(1)

    # Change light color
    if timer == 8:
        color = yellow
    elif timer == 0:
        color = red

    # Clear the image
    img.fill(0)

    # Check for ESC key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
