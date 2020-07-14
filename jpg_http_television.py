import time

import cv2
import numpy as np
from flask import Flask                                                         
from flask import Flask, request, redirect, url_for
import threading

app = Flask(__name__)

@app.route('/uploadjpg',methods=["POST"])
def hello_world():
    global img
    data = request.data
    img = cv2.imdecode(np.frombuffer(data, np.uint8), -1)
    return "Thank you!"


if __name__ == "__main__":
    threading.Thread(target=app.run, ).start()
    img  = None
    
    i = 0
    while True:
        i += 1
        if img is not None:
            cv2.imshow("Recieved image", img)
        else:
            cv2.imshow("Recieved image", np.random.randint(0, 256, (300, 300), dtype='uint8'))
            time.sleep(1)

        key = cv2.waitKey(1)
        if key == 27:
            break
