import datetime
from jarvish_speak import speak
def wish_me():
    time= int(datetime.datetime.now().hour)
    if 0 <= time <12:
        speak("good morning prem")
    elif time >=12 and time<18:
        speak("good afternoon prem")
    else:
        speak("good evning prem")
