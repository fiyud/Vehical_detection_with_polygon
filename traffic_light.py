import cv2
import numpy as np
import time

# Create blank background image
img = np.zeros((700, 900, 3), np.uint8)

color_title = {
    "red": "red",
    "yellow": "yellow",
    "green": "green"
}

next_color = {
    "red": "green",
    "yellow": "red",
    "green": "yellow"
}

# Define traffic light colors
green = (0, 255, 0) 
yellow = (0, 255, 255)
red = (0, 0, 255)

red_default = (34, 34, 162)
yellow_default = (81, 165, 165)
green_default = (40, 151, 40)

# init
red_value = red_default
yellow_value = yellow_default
green_value = green

# Initial color is green
color = color_title["green"]

# Set countdown timer
x = 5 #thoi gian den xanh
y = 3 #thoi gian den vang
z = x + y #thoi gian den do

cor_x = 233
cor_y = 586

timer = 5

def set_hight_light_color(color):
    if color == "green":
      return [y, red_default, yellow, green_default, 366, next_color[color]]
    elif color == "yellow":
      return [z, red, yellow_default, green_default, 150, next_color[color]]
   
    return [x, red_default, yellow_default, green, 588, next_color[color]]


while True:
    # Draw colored circle for traffic light
    cv2.circle(img,(250, 130), 100, red_value, -1)
    cv2.circle(img,(250, 350), 100, yellow_value, -1)
    cv2.circle(img,(250, 570), 100, green_value, -1)
    
    # Display countdown text
    cv2.putText(img, str(timer), (cor_x, cor_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
    
    # Display image
    cv2.imshow('Traffic light', img)
    
    # Count down each second 
    if timer > 0:
        timer -= 1
        time.sleep(1)
        
    if timer == 0:
      timer, red_value, yellow_value, green_value, cor_y, color = set_hight_light_color(color)
            
    # Check for ESC key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()