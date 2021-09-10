#Project jarvis
from googletrans import Translator
import googletrans
import inflect
from PyDictionary import PyDictionary as dct
import pywhatkit
from pywikihow import search_wikihow
from win32com.client import Dispatch
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pandas as pd
import holidays
#######################################
#import chat
#from city_loc_JArvish import find_loc
#from alarm_fun import alarm_ring
import annoncement
import nasa2
import jarvish_news
import command
from jarvish_take_command import take_command
import jarvish_some_small_task
import jarvish_remember_remind
from guess_game import money_left
#import chat
import jarvish_dates
#######################################
import wolframalpha
import requests
import time
from datetime import datetime , date
import googlemaps
from playsound import playsound
import pygame
import json
#from Adafruit_IO import Client, Feed, RequestError
#ADAFRUIT_IO_KEY = 'aio_nbJJ32IGEx9gySFQn3DXQozPfd56'
#ADAFRUIT_IO_USERNAME = 'Prem2512'
#aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
pygame.init()
pygame.mixer.init()
directory = 'song_album'
menu = pd.read_csv("menu_hostel.csv")
#print(menu)

try:
    app = wolframalpha.Client("5L4Q6Y-HJEU3VPA4P")
except Exception:
    print("import Error")
#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 100
engine.setProperty('rate',newVoiceRate)
volume = engine.getProperty('volume')
engine.setProperty('volume', 2.0)
from jarvish_speak import speak,speak_2
import jarvish_wish_me
    #speak("i am your assistance sir , how can i help you")
#def take_command():
#   r= sr.Recognizer()
#   with sr.Microphone() as source:
#       print("Listning.....")
#       r.pause_threshold = 1
#       audio = r.listen(source)
#   try:
#       print("Recognising.....")
#       query= r.recognise_google(audio,lnguage='en-in')
#       print(f"User said :{query}\n")
#   except Exception as e:
#       #print(e)
#       print("say it again")
#       return "None"
#   return query
#def take_command():
 #   speak("what  you  want  to  know   prem   ")
  ## return query
from jarvish_wish_me import wish_me
#query =take_command()
#def take_command2():
#    speak("sir    what kind of song you want to listen ")
#    query2 = str(input("sir    what kind of song you want to listen"))
#    return query2
#def take_youtube_search():
#    speak("sir   what you want to search ")
#    search = str(input("write your searching query"))
#    return search
while(1):
        waking_word=take_command()
        if(waking_word=="hello"):
            if __name__ == '__main__':
        
                wish_me()
                speak(" hello   Prem   How   Are   you")
                while True:
                    #digital = aio.feeds('python')
                    query=take_command()
                    query = query.lower()
                    if "quit" in query:
                        speak("Thanks for your time sir  have a good day ")
                        break
                    elif "anything today" in query:
                        jarvish_dates.dates_festival()
                    elif "send_mail" in query:
                        speak("what message to send sir")
                        message =take_command()
                        command.send_mail(message)
                    elif "my intro" in query:
                        with open("my_Intro.txt") as f:
                            line = f.read()
                            speak(line)
                    elif "news" in query:
                            command.news_func()
                    elif "how to " in query:
                        jarvish_some_small_task.how_to_do(query)
                    elif "wikipedia" in query:
                        command.wikipedia(query)
                    #elif "chat" in query:
                        #chat.main_chat()
                    elif "make announcement" in query:
                        annoncement.make_announcement()
                    elif 'open google' in query:
                        webbrowser.open("http://google.com")
                    elif 'open youtube' in query:
                        search= command.take_youtube_search()
                        link = "https://www.youtube.com/results?search_query"+search
                        webbrowser.open(link)
                        speak("This   is   my   Latest  Search   sir")
                        pywhatkit.playonyt(search)
                        speak("This the video sir")
                    #elif "open adafruit" in query:
                    #    webbrowser.open("https://io.adafruit.com/")
                    #elif "gmail" in query:
                    #    speak("what should i say")
                    #    content = take_command()
                    #    send_mail(content)
                    #elif "open code " in query:
                    #    path = "C:\\Users\\welcome\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
                    #    os.startfile(path)
                    #elif "play music" in query:
                    #    music_dir = "C:\\Users\\Public\\Music\\Sample Music"
                    #    song = os.listdir(music_dir)
                    #    os.startfile(os.path.join(music_dir,song[0]))
                    #elif "lets talk" in query:
                    #   speak("why not ")
                    #  chat.main()
                    elif "menu" in query:
                        command.menu_func(query)
                    elif "search a word" in query:
                        command.word_serch_func()
                    elif "song" in query:
                        #with open("song_instruction.txt","w") as so:
                        #    so.write(query)
                        #    os.system("C:\\Users\\welcome\\IdeaProjects\\prem1\\song_.py")
                        command.song_func(query)
                    elif "location" in query:
                        API_KEY = '<AIzaSyB2nXpzoZ30RTILUZI59Ko5FjvYCjOp04c>'
                        location = "delhi technological university"
                        params = {
                        'key': API_KEY,
                        'address': location,
                        'sensor': True
                        }

                        gmaps_key = googlemaps.Client(key="AIzaSyB2nXpzoZ30RTILUZI59Ko5FjvYCjOp04c")
                        geo_result = gmaps_key.geocode(location)
                        #https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,
                        #+Mountain+View,+CA&key=API_KEY

                        #base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
                        #response = requests.get(base_url, params=params).json()
                        #response.keys()
                        #print(response['status'])
                        #result = response['results'][0]
                        #location = result['geometry']['location']
                        #print(location['lat'])
                        #print(location['lng'])
                        #else:
                        #   print("status not found")
                        #result = req.json()['results'][0]
                    # lat = result['geometry']['location']['lat']
                        #lng = result['geometry']['location']['lng']
                        #print(lat,lng)
                    elif "translate" in query:
                        command.translate_func(query)
                    elif "nasa info" in query:
                        command.nasa_func(query)
                    elif "say something" in query:
                        command.repeat_func()
                    elif "say my name" in query:
                        speak("Prem    Kumar")
                    elif "my resume" in query:
                        with open("my_resume.txt","r") as resume:
                            resume_read = resume.read()
                        speak(resume_read)
                    elif "call my device" in query:
                        #aio.send("Python","ON")
                        #data = aio.receive(digital.key)
                        #if str(data.value) == "ON":
                        #    print('received <- ON\n')
                        #elif str(data.value) == "OFF":
                        #    print('received <- OFF\n')
                        #    time.sleep(0.5)
                        pass
                    elif "weather report " in query:
                        api_address='http://api.openweathermap.org/data/2.5/weather?appid=d4143a8bb1dff74d9dda29f45c7b7ded&q='
                        city = input(speak('which City weather you want to know'))
                        url = api_address + city
                        json_data = requests.get(url).json()
                        pressure = json_data['main']['pressure']
                        humidity = json_data['main']['humidity']
                        visibility  = json_data['visibility']
                        wind_speed = json_data['wind']['speed']
                        cloud_report = json_data['weather'][0]['description']
                        print("pressure is :",pressure )
                        print("Humidity is :",humidity )
                        print("Visibiliy is :",visibility)
                        print("Wind speed is :",wind_speed)
                        print("Cloud Report :",cloud_report)
                    elif "hbd" in query:
                        command.happy_bdy_func()
                    elif "festival" in query:
                        holidays_india = holidays.India(years=2021)
                        speak(f"today is : {holidays_india.get(datetime.now().date())}")
                    elif "where am i" in query:
                        #find_loc(query)
                        pass
                    elif "remember this" in query:
                        command.remember_this()
                    elif "remind me something" in query:
                        command.remind_me()
                    elif "set alarm" in query:
                        command.alarm_ring(query)
                    #elif "set alarm" in query:
                    #    time_set = take_time_for_reminder()
                    #    with open("alarm_time.txt","w") as t:
                    #        t.write(time_set)
                    #    os.startfile("C:\\Users\\welcome\\IdeaProjects\\prem1\\alarm_run.py")
                    elif "time now" in query:
                        command.say_time()
                    elif "nasa" in query:
                        api_key_nasa = "pBHPG9z8ChlXrikbMelh4RPY94i1ZK1IImAs54Aa"
                        url = "https://api.nasa.gov/planetary/apod?api_key="+str(api_key_nasa)
                        today = str(datetime.today())
                        today = today[0:10]
                        today = str(today)
                        params_nasa = {'date' :today}
                        r = requests.get(url,params = today)
                        data = r.json()
                        print(data)
                    elif "play game" in query:
                        money_left()
                    else:
                        command.wolf_app(query)
        else:
            continue
