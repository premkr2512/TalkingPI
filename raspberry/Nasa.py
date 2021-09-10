import requests
import json
api_key = "FuMBMXCzwzYhvIDXQV0YI1hLf3vQjLADTGMpdGND"
def space_news(body):
    print("Just wat i am extracting data")
    name = str(body)
    url = "https://hubblesite.org//api//v3//glossary" +  str(name)
    #Params = {'date':str(date)}
    r = requests.get(url)
    data = r.json.JSONDcoder
    #final =data['definition']
    print(data)
    print("'''''")
space_news('earth')