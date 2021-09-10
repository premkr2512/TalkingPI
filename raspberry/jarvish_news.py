#from win32com.client import Dispatch
import json
from jarvish_speak import speak
import requests
def BBC_news():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "f6df831eca954073a86b296e60496d02 "
    }
    main_url = " https://newsapi.org/v1/articles"
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    # empty list which will
    # contain all trending news
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
        speak(results[i])
    #to read the news out loud for us
    #speak = Dispatch("SAPI.Spvoice")
    #speak.Speak(results)

#BBC_news()