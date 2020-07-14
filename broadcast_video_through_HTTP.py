import time

import cv2
import requests


FILE_NAME = r"/home/art/beautiful_dataset/Матрица.avi"
# FILE_NAME = r"O:\photos\video_mall.mov" - так в Windows не работает

cap = cv2.VideoCapture(FILE_NAME)
NUMBER_OF_FRAMES_TO_SKIP = 3


while True:

    for _ in range(NUMBER_OF_FRAMES_TO_SKIP):
        ret, frame = cap.read()

    ret, img = cap.read()

    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
    result, encimg_jpg = cv2.imencode('.jpg', img, encode_param)
    jpg_bytes = encimg_jpg.tobytes()

    res = requests.post(url='http://127.0.0.1:5000/uploadjpg',
                        data=jpg_bytes,
                        headers={'Content-Type': 'application/octet-stream'})
    




    
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        print("Нажали Esc, выхожу из цикла")
        break

    #time.sleep(0.1)

cv2.destroyAllWindows()

    
