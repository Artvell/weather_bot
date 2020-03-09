import requests
from config import appid

def get_weather_today(coords):
    url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url,params={"lat":coords[0],"lon":coords[1],"units":'metric','lang':'ru','appid':appid})
    return r.json()

def get_weather_five(coords):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(url,params={"lat":coords[0],"lon":coords[1],"units":'metric','lang':'ru','appid':appid})
    return r.json()

c=[41.300803,69.28]

#print(get_weather_today(c))
