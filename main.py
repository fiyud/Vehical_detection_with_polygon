import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
from tracker import*

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('yolov8counting-trackingvehicles-main/veh2.mp4')

my_file = open("yolov8counting-trackingvehicles-main/coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count = 0

area = [(553, 282), (566, 346), (848, 340), (698, 266)]
area_c = set()
tracker = Tracker()

cy1 = 322
cy2 = 368
offset = 6

car_c = set()
bus_c = set()
motorcycle_c = set()
truck_c = set()

while True:
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500))
   

    results = model.predict(frame)
#   print(results)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
#   print(px)w2
    list = []
             
    for index, row in px.iterrows():
#   print(row)
 
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if c in ['motorcycle', 'car', 'bus', 'truck']:
            list.append([x1, y1, x2, y2])

    bbox_id = tracker.update(list)

    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        cx = int(x3 + x4)//2
        cy = int(y3 + y4)//2
        results = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
        if results >= 0:
            cv2.circle(frame, (cx,cy), 4, (0, 0, 255), -1)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 225), 2)
            cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
            area_c.     add(id)
            if id == 'car':
                car_c.add(id)
            elif id == 'bus':
                bus_c.add(id)
            elif id == 'motorcycle':
                motorcycle_c.add(id)
            elif id == 'truck':
                truck_c.add(id)
            
    cv2.polylines(frame, [np.array(area, np.int32)], True,(250, 0, 0))
    count = len(area_c)
    cv2.putText(frame, "Total:" + str(count), (146, 146), cv2.FONT_HERSHEY_PLAIN, 5, (19, 33, 235))

    car_count = len(car_c)
    bus_count = len(bus_c)
    motorcycle_count = len(motorcycle_c)
    truck_count = len(truck_c)
                      
    cv2.putText(frame, "Car:" + str(car_count), (61, 146), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 0))
    cv2.putText(frame, "Bus:" + str(bus_count), (61, 196), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 0))
    cv2.putText(frame, "Moto:" + str(motorcycle_count), (61, 246), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 0))
    cv2.putText(frame, "Truck:" + str(truck_count), (61, 296), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 0))

        
           
#    cv2.line(frame,(274,cy1),(814,cy1),(255,255,255),1)
#    cv2.line(frame,(177,cy2),(927,cy2),(255,255,255),1)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()


