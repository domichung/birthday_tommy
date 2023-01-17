import requests 
from time import sleep
import time
import discord
import pandas as pd

t = 0

url = ""
data = {
        "username" : "❤偷米生日大師❤"
    }

while(1):
    t+=1

    out = '第 '+ str(t) + ' 次 🎂🎂生日快樂唷🎂🎂'
    #字串合併

    data["embeds"] = [
                {
                    "description" : "<@497760103215398917>",
                    #偷米的dcid
                    "title" : out
                }
            ]
    result = requests.post(url, json = data)
    result.raise_for_status()
    sleep(3)
    #多久一次