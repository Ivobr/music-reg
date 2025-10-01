import requests
api_url = "https://accounts.spotify.com/api/token"

token_header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": "5ed9be3db5684562a901d034bfc85361",
    "client_secret": "6e31439ec4c74f39a6001520c82478f6"
}


response = requests.post(api_url, headers=token_header, data=data)

if response.status_code == 200:
    token_info = response.json()
    access_token = token_info["access_token"]
    print("Access Token:", access_token)
else:
    print(f"Error: {response.status_code} - {response.text}")