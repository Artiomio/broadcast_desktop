import time

from flask import Flask, request, redirect, url_for
#from gtts import gTTS
import os

def say_message(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("mpg123 temp.mp3")


app = Flask(__name__)

@app.route('/',methods=["POST"])
def hello_world():
    data = request.data
    with open(f"data {time.ctime().replace(':', '-')} .bin", "wb") as f:
        f.write(data)

    print(f"{time.ctime()} : {len(data)} bytes saved")

    
    if len(data) > 10**9:
        size_human = f"{int(round(len(data) / 10**9))} Gigabytes"
    elif len(data) > 10**6:
        size_human = f"{int(round(len(data) / 10**6))} Megabytes"
    elif len(data) > 10**3:
        size_human = f"{int(round(len(data) / 10**3))} Kilobytes"
    else:
        size_human = f"{len(data)} bytes"
    
    #say_message(f"""Wow, something interesting, we have recieved a file, its size is {size_human}...
    #                I saved it in {os.getcwd()} folder. Don't forget about that...""")



    return "Got it!"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7893, debug=True)
