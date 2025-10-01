import requests
import json
# import drivers
from time import sleep

# dislpa = drivers.Lcd()
data = {
    'api_token' : 'd30173a93f26680235ebfcf4454e370a',
    'return' : 'apple_music, spotify'
}
files = {
    'file' : open('./../02-mamacita.mp3', 'rb')
}
response = requests.post('https://api.audd.io/', data=data, files=files)


json_data = response.json()
print(json_data)

artist = json_data['result']['artist']
title = json_data['result']['title']
artwork_url = json_data['result']['apple_music']['artwork']['url']

print(artwork_url)