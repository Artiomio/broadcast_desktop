import time
import numpy as np
import cv2
import mss
import requests



SCREEN_GRAB_RANGE = {"top": 0, "left": 0, "width": 1280, "height": 1024}
sct = mss.mss()

def get_screenshot(sct):
    try:
        # Get raw pixels from the screen, save it to a Numpy array
        monitor = SCREEN_GRAB_RANGE
        img = np.array(sct.grab(monitor))
    except:
        print("Error taking screenshot!")
        width = SCREEN_GRAB_RANGE["width"] - SCREEN_GRAB_RANGE["left"]
        height = SCREEN_GRAB_RANGE["height"] - SCREEN_GRAB_RANGE["top"]
        img = np.random.randint(0, 255, size=(100, 100, 3), dtype="uint8")

    return img







while True:


    img = get_screenshot(sct)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]
    result, encimg_jpg = cv2.imencode('.jpg', img, encode_param)
    jpg_bytes = encimg_jpg.tobytes()

    res = requests.post(url='http://188.243.172.35/uploadjpg',
                        data=jpg_bytes,
                        headers={'Content-Type': 'application/octet-stream'})
    




    
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        print("Нажали Esc, выхожу из цикла")
        break

    time.sleep(2)

cv2.destroyAllWindows()

    
