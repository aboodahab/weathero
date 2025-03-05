import sys
import requests
import math
from engine2 import key

def great():
    print("Hi, Welcome In Weathero")


def data():
    arguments = sys.argv
    return arguments, key


def check(code):
    if code == 200:
        return "yes"
    return "no"


def getInformations(data,place):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"]
    print(f"""The temperature in {place} today is {math.trunc(temperature)}
The humidity in {place} today is {math.trunc(humidity)}
The weather  condition is {weather_condition} """)


def request(place, apiKey):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={apiKey}&units=metric")
    if check(response.status_code) == "no":
        print("error:please write a correct place")
        return
    print(response)
    getInformations(response.json(),place)


great()
request(data()[0][1], data()[1])
