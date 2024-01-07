import cv2
import time

xanh = (0,255,0) 
vang = (0,255,255)
do = (0,0,255)

def show_traffic_light(color):
    img = None
    if color == 'red':
        img = cv2.circle(img, (250,250), 100, do, -1)
    elif color == 'green':
        img = cv2.circle(img, (250,250), 100, xanh, -1)
    elif color == 'yellow':
        img = cv2.circle(img, (250,250), 100, vang, -1)
    
    cv2.imshow('Traffic Light', img)
    cv2.waitKey(1000)  # Hiển thị trong 1 giây
    cv2.destroyAllWindows()

def traffic_light_simulation():
    colors = ['red', 'green', 'yellow']
    while True:
        for color in colors:
            show_traffic_light(color)
            time.sleep(1)  # Dừng 1 giây sau mỗi trạng thái đèn giao thông

traffic_light_simulation()
