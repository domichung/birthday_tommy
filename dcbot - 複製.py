import requests 
from time import sleep
import time
import discord
import pandas as pd

t = 519

url = "https://discord.com/api/webhooks/1064872762654601286/V1owsGeha0N8zlL1ApAiBnmy1NLJ8RUko4YPbHIAkFDDbb69DaDz5cqvKqJJNwTTrOxV"
data = {
        "username" : "❤偷米生日大師❤"
    }

while(1):
    t+=1

    out = '第 '+ str(t) + ' 次 🎂🎂生日快樂唷🎂🎂'

    data["embeds"] = [
                {
                    "description" : "<@497760103215398917>",
                    "title" : out
                }
            ]
    result = requests.post(url, json = data)
    result.raise_for_status()
    sleep(3)