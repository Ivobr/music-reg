import requests

url = "https://accounts.spotify.com/authorize"

token_header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data={
    "grant_type": "client_credentials",
    "client_id": "5ed9be3db5684562a901d034bfc85361",
    "client_secret": "6e31439ec4c74f39a6001520c82478f6"
}

response = requests.request(method = "GET",url=url, headers=token_header, data=data)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")