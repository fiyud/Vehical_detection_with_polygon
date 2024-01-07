import cv2
import numpy as np
import time

# Create blank background image
img = np.zeros((500,500,3),np.uint8)

# Define traffic light colors
green = (0,255,0) 
yellow = (0,255,255)
red = (0,0,255)

# Initial color is green
color = green  

# Set countdown timer
timer = 5  

while True:
    # Draw colored circle for traffic light
    cv2.circle(img,(250,250), 100, color, -1)
    
    # Display countdown text
    cv2.putText(img, str(timer), (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    
    # Display image
    cv2.imshow('Traffic light', img)
    
    # Count down each second 
    if timer > 0:
        timer -= 1
        time.sleep(1)
    
    # Change light color
    # if timer == 8:
    #     color = yellow
    # elif timer == 0:
    #     color = red
    if timer == 0:
        timer = 3
        color = yellow
        
    # Check for ESC key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()