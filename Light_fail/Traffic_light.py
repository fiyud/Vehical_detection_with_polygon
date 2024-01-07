import cv2
import numpy as np

# Tạo hình ảnh ban đầu cho các đèn giao thông
image = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.circle(image, (150, 100), 50, (0, 0, 255), -1) # Đèn đỏ
cv2.circle(image, (150, 175), 50, (0,255 ,0), -1) # Đèn xanh lá cây
cv2.circle(image, (150, 200), 50, (0,255 ,255), -1) # Đèn vàng
# Hiển thị hình ảnh ban đầu
cv2.imshow('Traffic light',image)
# đặt thời gian chờ
timer = 10

# Hàm để chuyển trạng thái của các đèn giao thông sau mỗi khoảng thời gian
def change_traffic_light():
    while True:
        image = np.zeros((300,300 ,3), dtype=np.uint8)
        cv2.circle(image,(150 ,100 ),50 ,(0 ,0 ,255 ),-1 ) # Red light
        cv2.putText(image,str(timer),(140, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Hiển thị hình ảnh mới với tín hiệu chỉ có màu đỏ trong khoảng thời gian quyết định.
        cv2.imshow('Traffic light',image)

        # Chờ trong khoảng thời gian quyết định cho tín hiệu đèn đỏ
        cv2.waitKey(3000)

        image = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.circle(image, (150, 175), 50, (0 ,255 ,0 ), -1) # Green light
        cv2.putText(image,str(timer), (140, 185), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Hiển thị hình ảnh mới với tín hiệu chỉ có màu xanh lá cây trong khoảng thời gian quyết định.
        cv2.imshow('Traffic light',image)

        # Chờ trong khoảng thời gian quyết định cho tín hiệu đèn xanh
        cv2.waitKey(2000)


        image = np.zeros((300,300 ,3), dtype=np.uint8)
        cv2.circle(image,(150 ,200 ),50 ,(0 ,255 ,255 ),-1 ) # đèn vàng
        cv2.putText(image,str(timer), (140, 225), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        # Hiển thị hình ảnh mới với tín hiệu chỉ có màu vàng trong khoảng thời gian quyết định.
        cv2.imshow('Traffic light',image)

        # Chờ trong khoảng thời gian quyết định cho tín hiệu đèn vàng
        cv2.waitKey(1000)
# Gọi hàm để chạy mô phỏng các trạng thái của các đèn giao thông
change_traffic_light()
cv2.destroyAllWindows()