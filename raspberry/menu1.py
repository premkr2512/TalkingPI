from instabot import Bot
bot = Bot()
bot.login(username = "we_r_electronics",password="Prem@18091")
#bot.upload_photo("C:\\Users\\welcome\\IdeaProjects\\game1\\autobot.jpg",caption = " Hey don't worry i am an autobot . i posted it my self by my python code")
#bot.follow("elonrmuskk")
import cv2
import glob
import os
import sys
import time
from io import open
sys.path.append(os.path.join(sys.path[0], "instapost_stuff"))
posted_pic_list = []
try:
    with open("C:\\Users\\welcome\\IdeaProjects\\prem1\\posted_pic.txt", "r", encoding="utf8") as f:
        posted_pic_list = f.read().splitlines()
except Exception:
    posted_pic_list = []
print(posted_pic_list)
timeout = 24 * 60 * 60  # pics will be posted every 24 hours
while True:
    folder_path = "C:\\Users\\welcome\\IdeaProjects\\instapost_stuff"
    #pics = glob.glob(folder_path + "/*.jpg")
    #pics = sorted(pics)
    #print(pics)

    cv_img = []
    for pic in glob.glob(folder_path + "/*.jpg"):
        n= cv2.imread(pic)
        print(pic)
        cv_img.append(n)

    try:
        print("i m in loop")
        for pic in cv_img:
            if pic in posted_pic_list:
                continue

            pic_name = pic[:].split("_")

            print("upload: " + pic_name)

            description_file = folder_path + "\\" + pic_name + ".txt"

            if os.path.isfile(description_file):
                with open(description_file, "r") as file:
                    caption = file.read()
            else:
                caption = pic_name.replace("-", " ")

            #bot.upload_photo(pic, caption=caption)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                # snd msg
                break

            if pic not in posted_pic_list:
                #posted_pic_list.append(pic)
                with open("posted_pic.txt", "a", encoding="utf8") as f:
                    f.write(pic + "\n")

            time.sleep(timeout)

    except Exception as e:
        print(str(e))
    time.sleep(60)