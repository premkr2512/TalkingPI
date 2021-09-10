from jarvish_speak import speak
from jarvish_take_command import take_command
import time
list1=['Deepak Chahar','Virat kohli','Mohammad Sammi','Rishabh panth','K L Rahul']
list2=['Rohit sharma','Virat kohli','Rabindra jadeja','Rishabh panth','K L Rahul','Jasprit bumbrah']
list3=['Chateswar pujara','Mohammad Sammi','Rishabh panth','Jasprit bumbrah','rabindra jadeja']
list4=['Chateswar pujara','Mohammad siraj','Mohammad sammi','Rishabh panth','rabindra jadeja']
result_list=['deepak chahar','Rohit sharma','Virat kohli','mohammad Siraj','jasprit Bumbrah','k l rahul','Chateshwar Pujara','Mohammad sammi','Rabindra jadeja','rishabh panth']
c=0
speak("please tell me your name mister")
name=take_command()
speak("Are you ready"+name)
speak("here is the rule mister"+name+" i will you a list of player and you have to choose only one of them and do not reveal it ")
speak("after that we have four list of player ")
speak("you have to say yes if it is present in the lists each time")

speak("listen to the first list carefully")
for i in list1:
    speak(i)
time.sleep(2)
speak("Am i right sir")
is_it1=take_command()
if "yes" in is_it1:
    c=c+1
speak("listen to the second list carefully")
for i in list1:
    speak(i)
time.sleep(2)
speak("Am i right sir")
is_it2=take_command()
if "yes" in is_it2:
    c=c+1
speak("listen to the second list carefully")
for i in list1:
    speak(i)
time.sleep(2)
speak("Am i right sir")
is_it3=take_command()
if "yes" in is_it3:
    c=c+1
speak("listen to the second list carefully")
for i in list1:
    speak(i)
time.sleep(2)
speak("Am i right sir")
is_it4=take_command()
if "yes" in is_it4:
    c=c+1
speak("i think your player is "+result_list[c])