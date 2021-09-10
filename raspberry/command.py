from jarvish_take_command import take_command
import os
import random
import smtplib
from wikipedia import summary
from pywikihow import search_wikihow
import pygame
from PyDictionary import PyDictionary as dct
from jarvish_speak import speak
from googletrans import Translator
import googletrans
import requests
import pandas as pd
import nasa2
day = ['Monday','tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
time1 = ['8:30','12:30','5:30','17:02']
rutine = ['breakfast','lanch','supper','dinner']
menu = pd.read_csv("menu_hostel.csv")
directory = 'song_album'
import time
from datetime import date, datetime
import inflect
import wolframalpha
try:
    app = wolframalpha.Client("5L4Q6Y-HJEU3VPA4P")
except Exception:
    print("import Error")
def wolf_app(query):
    try:
        print("I m trying ")
        res = app.query(query)
        print(next(res.results).text)
        # print(type(next(res.results).text))
        speak(next(res.results).text)
        #speak1 = Dispatch("SAPI.Spvoice")
        #speak1.Speak(next(res.results).text)
    except:
        speak("Sorry sir I cannot help you Please contact Prem Sir ")
def say_time():
        p = inflect.engine()
        t_H=datetime.now().hour
        t_M=datetime.now().minute
        speak("now time is"+ "     "+p.number_to_words(t_H)+"   "+"   "+p.number_to_words(t_M)+"    "+"o  Clock")  
        print("now time is"+p.number_to_words(t_H) +"  " + "  "+ p.number_to_words(t_M)+"o  Clock")
def take_time_for_reminder():
    #speak("at  what  time  you  want  to  set  reminder")
    time_set = str(input("write time to set reminder"))
    return time_set
def alarm_ring(query):
    time_set = take_time_for_reminder()
    with open("alarm_time.txt","w") as t:
        t.write(time_set)
    os.startfile("C:\\Users\\welcome\\IdeaProjects\\prem1\\alarm_run.py")
def remember_this():
    speak("What   to   remember  sir")
    line_to_remember = str(input("Enter your thing to remember"))
    with open("reminder.txt",'w') as reminder:
        reminder.write(line_to_remember)
def remind_me():
    with open("reminder.txt","rb") as remind:
        line_to_remind = remind.read()
    speak(line_to_remind)
def happy_bdy_func():
        Hbd = pd.read_csv("C:\\Users\\welcome\\IdeaProjects\\game1\\Birthday_list.csv")
        c = 0
        d=1
        for i in Hbd['Date']:
            str_date = str(datetime.now())
            if str(i)== str_date[5:10]:
                speak("today is  "+Hbd.iat[c,d]+ "   Birthday")
                c=c+1
def menu_func(query):
            c1 = -1
            c2=-1
            Current_day = day[date.today().weekday()]
            for i in menu['day']:
                c1+=1
                if i.lower() == Current_day.lower():
                    for j in range(len(time1)):
                        c2+=1
                        t1 = time1[j]
                       # wish_me()
                        s = menu.iat[c1,j+1]
                        print(s)
                        speak("in" + rutine[j])
                        #time.sleep(0.5)
                        speak(s)
def take_youtube_search():
    speak("sir   what you want to search ")
    search = take_command()
    return search
def wikipedia(query):
    speak("searching wikipedia ")
    query = query.replace("wikipedia"," ")
    result = summary(query,sentences= 2)
    speak("According to wikipedia")
    print(result)
    speak(result)
def news_func():
        query_params = {
                "source": "bbc-news",
                "sortBy": "top",
                "apiKey": "f6df831eca954073a86b296e60496d02 " }
        main_url = " https://newsapi.org/v1/articles"
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]
        results = []
        for ar in article:
            results.append(ar["title"])
        for i in range(len(results)):
                print(i + 1, results[i])
                speak(results[i])
def send_mail(content):
    from_mail = input("Enter your mail id")
    to_mail = input(("Enter mail to which email is to be send"))
    Passward = input("Enter Passward")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(from_mail,Passward)
    server.sendmail(from_mail,to_mail,content,)
    server.close()
def how_to_do(query):
    max_result = 1
    how_to = search_wikihow(query = query,max_results = max_result)
    assert len(how_to)==1
    print(how_to[0].summary)
    speak(how_to[0].summary)
def repeat_me():
    speak("sir   say   something ")
    repeat_line = take_command()
    return repeat_line
def repeat_func():
        repeat_line = repeat_me()
        with open("repeat_me.txt","w") as r:
            r.write(repeat_line)
        with open("repeat_me.txt","r") as line_read:
            line_read=line_read.read()
        speak(line_read)
        with open("repeat_me.txt","r+") as delete:
            delete.truncate(0)
def nasa_func(query):
        speak("Please enter date for which you want to know information")
        year_month_day= str(input("enter Date "))
        year_month_day = year_month_day.replace(" and ","-")
        speak(nasa2.get_nasa_news(year_month_day))
def song_func(query):
        if("song" in query):
                speak("sir  what kind of song you want to listen ")
                print("sir  what kind of song you want to listen")
                song_query=take_command()
                if"hollywood" in song_query:
                        file = os.path.join(directory, song_query)
                        music_dir=os.listdir(file)
                        m0 = -1
                        while m0 <=len(music_dir):
                                m0+=1
                                music = random.choice(music_dir)
                                if music.endswith(".mp3"):
                                        file_path = file +"//" + music
                                        pygame.mixer.music.load(str(file_path))
                                        print(music)
                                        pygame.mixer.music.play()
                                        speak("playing Hollywood song")
                                        print("playing hollywood song")
                                        while pygame.mixer.music.get_busy()==True:
                                                continue
                #print(music_dir)
                #playsound(d)
                elif "ayush" in song_query:
                        file = os.path.join(directory, song_query)
                        music_dir=os.listdir(file)
                        m0 = -1
                        while m0 <=len(music_dir):
                                m0+=1
                                music = random.choice(music_dir)
                                if music.endswith(".mp3"):
                                        file_path = file +"//" + music
                                        pygame.mixer.music.load(str(file_path))
                                        print(music)
                                        pygame.mixer.music.play()
                                        speak("playing ayushman khurana song")
                                        print("playing ayushman khurana song")
                                        while pygame.mixer.music.get_busy()==True:
                                                continue
                elif "honey_singh" in song_query:
                        file = os.path.join(directory, song_query)
                        music_dir=os.listdir(file)
                        m0 = -1
                        while m0 <=len(music_dir):
                                m0+=1
                                music = random.choice(music_dir)
                                if music.endswith(".mp3"):
                                        file_path = file +"//" + music
                                        pygame.mixer.music.load(str(file_path))
                                        print(music)
                                        pygame.mixer.music.play()
                                        speak("playing honey singh song")
                                        print("playing honey singh song")
                                        while pygame.mixer.music.get_busy()==True:
                                                continue
                else:
                        #"jubin_nautyal" in song_query:
                        file = os.path.join(directory, song_query)
                        music_dir=os.listdir(file)
                        m0 = -1
                        while m0 <=len(music_dir):
                                m0+=1
                                music = random.choice(music_dir)
                                if music.endswith(".mp3"):
                                        file_path = file +"//" + music
                                        pygame.mixer.music.load(str(file_path))
                                        print(music)
                                        pygame.mixer.music.play()
                                        speak("playing jubin nautyal song")
                                        print("playing jubin nautyal  song")
                                        while pygame.mixer.music.get_busy()==True:
                                                continue
def word_serch_func():
        dict = dct()
        speak("what to search sir :  Antonyms   Synonyms   Or    Meaning  ")
        kind =take_command()
        if kind == "meaning":
                speak("Enter your word sir")
                word= take_command()
                result= dict.meaning(word)
                speak(result)
                print(result)
        if kind == "antonym":
                speak("Enter your word sir")
                word= take_command()
                result= dict.antonym(word)
                speak(result)
                print(result)
        if kind == "synonym":
                speak("Enter your word sir")
                word= take_command(word)
                result= dict.synonym(word)
                speak(result)
                print(result)
def translate_func(query):
        translator = Translator()
        dict = googletrans.LANGUAGES
        speak("What to convert sir")
        statement = take_command()
        query= query.replace("translate into ","")
        for i,j in dict.items():
                if j == query:
                        x= translator.translate(statement, dest=i)
        x = x.pronunciation
        print(x)
        speak(x)