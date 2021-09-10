#text
# from num2word import num2word
from subprocess import call
from jarvish_take_command import command
cmd_beg= 'espeak '
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file
text = command()
print(text)

#Replacing ' ' with '_' to identify words in the text entered
def speak(text):
    text = text.replace(' ', '_')
#Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+cmd_out+text+cmd_end], shell=True)
speak(text)
