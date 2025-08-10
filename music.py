import requests 
data = {
    'api_token' : '6c8116f39095bbbcbd3172ffb4f18446',
    'return' : 'apple_music,spotify'
}
files = {
    'file' : open('')
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)