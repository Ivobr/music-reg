import requests
import time
import json

# Spotify endpoints
live = "https://api.spotify.com/v1/me/player/recently-played"
artist_info = "https://api.spotify.com/v1/artists/2ojqsY1ycYzZOpLDBBwHPU"  # fixed! must use API endpoint, not open.spotify.com
album_info = "https://api.spotify.com/v1/albums/1jzv3jwZbt8lYfEtMjiD1R"
playlist_info = "https://api.spotify.com/v1/playlists/3QEGSNYxAanvaVVV7hSNOQ"
next_track = "https://api.spotify.com/v1/me/player/next"

# Your access token (⚠️ temporary, expires in ~1 hour)
access_token = "BQAUv3AjPOkqFtiKGBSB6oUH7ShLkA_hrLZjuomNkYsFFjWgcUkHdFnxhdLeKTk46-eyC5UGJypLRK_K9lPqT7Awuxm1L7_lVifliRPR4PuXHizKpi6fUbyzAbG3A6AEP-uVw6kcvzk"

headers = {
    "Authorization": f"Bearer {access_token}"
}


def get_track(access_token):
    response = requests.get(artist_info, headers={"Authorization": f"Bearer {access_token}"})
    print("Status:", response.status_code)

    if response.status_code != 200:
        print("Error:", response.text)
        return None

    json_resp = response.json()

    # ✅ Save JSON to file
    with open("api_data.json", "w") as file:
        json.dump(json_resp, file, indent=4)

    print("JSON saved to api_data.json")

    # ✅ Extract album/artist image if available
    if "images" in json_resp and len(json_resp["images"]) > 0:
        album_cover = json_resp["images"][0]["url"]
        img_data = requests.get(album_cover).content
        with open("album_cover.jpg", "wb") as handler:
            handler.write(img_data)
        print("Album cover saved as album_cover.jpg")
    else:
        print("No images found in response")

    return json_resp


def main():
    current_track_id = None
    while True:
        current_track_info = get_track(access_token)
        if current_track_info is None:
            break
        time.sleep(1)
        break


if __name__ == '__main__':
    main()
