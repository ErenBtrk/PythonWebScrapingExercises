'''
13. Write a Python program to get the number of people visiting
a U.S. government website right now. Go to the editor
Source: https://analytics.usa.gov/data/live/realtime.json

'''

import requests
import json

url = "https://analytics.usa.gov/data/live/realtime.json"
response = requests.get(url).json()
print(response)
for key,value in response.items():
    if(key == "data"):
        print(response[key][0]["active_visitors"])