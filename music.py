import requests 

data = {
    'api_token': 'd30173a93f26680235ebfcf4454e370a',
    'return': 'apple_music,spotify'
}
files = {
    'file': open('./02-mamacita.mp3', 'rb')
}

# Make request
response = requests.post('https://api.audd.io/', data=data, files=files)

# Convert to JSON
json_data = response.json()
print(json_data)
# Extract artwork URL template
artwork_url = json_data["result"]["apple_music"]["artwork"]["url"]

# Replace placeholders with actual size
cover_url = artwork_url.replace("{w}", "1000").replace("{h}", "1000")

# Download the image
img_data = requests.get(cover_url).content
with open("album_cover.jpg", "wb") as handler:
    handler.write(img_data)

print("Album cover saved as album_cover.jpg")
