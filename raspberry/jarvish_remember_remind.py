from jarvish_speak import speak
import jarvish_take_command
def remember_this():
    speak("What   to   remember  sir")
    line_to_remember = jarvish_take_command.take_command()
    with open("reminder.txt",'w') as reminder:
        reminder.write(line_to_remember)
def remind_me():
    with open("reminder.txt","rb") as remind:
        line_to_remind = remind.read()
    speak(line_to_remind)
