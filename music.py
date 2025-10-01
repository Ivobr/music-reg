import requests 
import json
import drivers
from time import sleep

display = drivers.Lcd()
data = {
    'api_token': 'd30173a93f26680235ebfcf4454e370a',
    'return': 'apple_music,spotify'
}
files = {
    'file': open('./02-mamacita.mp3', 'rb')
}
result = requests.post('https://api.audd.io/', data=data, files=files)

response_json = json.loads(result.text)

artist = response_json['result']['artist']
title = response_json['result']['title']

# artist = "Tyler The Creator"
# title = "New Magic Wand and your mom"
print(artist)
print(title)


try:
    def displaying(display, text='', num_line=1, num_cols=16):
        if len(text) > num_cols:
            display.lcd_display_string(text[:num_cols], num_line)
            sleep(1)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                display.lcd_display_string(text_to_print, num_line)
                sleep(0.5)
            sleep(1)
        else:
            display.lcd_display_string(text, num_line)
    
    displaying(display, artist, 1)
    displaying(display, title, 2)

    if len(artist) > 16 and len(title) <= 16:
        while True:
            displaying(display, artist, 1)
    
    if len(artist) > 16 and len(title) > 16:
        while True:
            displaying(display, artist, 1)
            displaying(display, title, 2)

except KeyboardInterrupt:
    display.lcd_clear()


