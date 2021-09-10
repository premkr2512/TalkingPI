from wikipedia import summary
from pywikihow import search_wikihow
from jarvish_speak import speak
def my_intro():
    with open("my_Intro.txt") as f:
        line = f.read()
        speak(line)
def how_to_do(query):
    max_result = 1
    how_to = search_wikihow(query = query,max_results = max_result)
    assert len(how_to)==1
    print(how_to[0].summary)
    speak(how_to[0].summary)


