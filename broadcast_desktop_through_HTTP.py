import time
import numpy as np
import cv2
import mss
import requests



SCREEN_GRAB_RANGE = {"top": 0, "left": 0, "width": 1366, "height": 768}
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




def send_to_artmonitor(img, secret="wubuku", jpg_quality=30, monitor_url="https://artmonitor.pythonanywhere.com"):
    url=f'{monitor_url}/{secret}/postimage/'
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality]
    result, encimg_jpg = cv2.imencode('.jpg', img, encode_param)
    jpg_bytes = encimg_jpg.tobytes()
    print(f"!!!Broadcasting desktop!!!\nSending POST request: {len(jpg_bytes)} bytes {monitor_url}")
    start = time.time()
    res = requests.post(url,
                        data=jpg_bytes,
                        headers={'Content-Type': 'application/octet-stream'})

    print(f"Response: {res}\nReady: {len(jpg_bytes)} bytes sent in {time.time() - start} sec")




while True:


    img = get_screenshot(sct)
    send_to_artmonitor(img)



    
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        print("Нажали Esc, выхожу из цикла")
        break

    time.sleep(1)

cv2.destroyAllWindows()

    
