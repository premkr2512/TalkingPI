import requests
api_key = "FuMBMXCzwzYhvIDXQV0YI1hLf3vQjLADTGMpdGND"
def get_nasa_news(date):
    print("Just wat i am extracting data")
    url = "https://api.nasa.gov/planetary/apod?api_key="+str(api_key)
    Params = {'date':str(date)}
    r = requests.get(url,params=Params)
    data = r.json()
    info = data['explanation']
    print(info)
    #title = data['title']
    #image_url = data['url']
    #file_name = str(date) +".jpg"
    #image = requests.get(image_url)

    #with open(file_name,'wb') as f:
     #   f.write(image.content)
    return str(info)
