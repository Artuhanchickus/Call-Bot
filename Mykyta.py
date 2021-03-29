from pyrogram import Client, filters
import time
api_id = "3774678"
api_hash = "ac882a54f7884879a6f794ff33c1fb2b"
phone_number = "+380500298007"


print("start")
while True:
    mins = time.strftime("%M");
    if int(mins) == 15:
        print('sending...')
        with Client("Shmaltsell", api_id, api_hash, phone_number = phone_number) as app:
            app.send_message(-306597811,"/drochnut")
        time.sleep(120)
        print("have sent")
