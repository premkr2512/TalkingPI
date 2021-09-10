import speech_recognition as sr
a=sr.Recognizer()
def command():
    with sr.Microphone() as source:
        print("say something")
        audio=a.listen(source)
        data=a.recognize_google(audio)
        return data.lower()
