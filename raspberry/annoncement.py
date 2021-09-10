import sounddevice as sd
from scipy.io.wavfile import write
import time
from jarvish_speak import speak
fs = 44100  # Sample rate
seconds = 10  # Duration of recording
import os
def make_announcement():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    speak("Prem please Make your Announcement")
    print("Speak......")
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file \from pydub import AudioSegment
    import winsound
    time.sleep(2);
    speak("Hello Everyone There is a announcement for you guys From Prem")
    filename = 'output.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    os.remove("output.wav")
#make_announcement()