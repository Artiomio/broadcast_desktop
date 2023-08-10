import time

import cv2
import requests


FILE_NAME = 'a.mkv'

cap = cv2.VideoCapture(FILE_NAME)
NUMBER_OF_FRAMES_TO_SKIP = 0


while True:

    for _ in range(NUMBER_OF_FRAMES_TO_SKIP):
        ret, frame = cap.read()

    ret, img = cap.read()

    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
    result, encimg_jpg = cv2.imencode('.jpg', img, encode_param)
    jpg_bytes = encimg_jpg.tobytes()

    res = requests.post(url='http://192.168.1.248:7893/uploadjpg',
                        data=jpg_bytes,
                        headers={'Content-Type': 'application/octet-stream'})
    



