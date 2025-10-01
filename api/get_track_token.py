import requests
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

# Your Spotify app credentials
CLIENT_ID = "5ed9be3db5684562a901d034bfc85361"
CLIENT_SECRET = "6e31439ec4c74f39a6001520c82478f6"
REDIRECT_URI = "https://localhost:8888/callback"
SCOPES = "user-read-currently-playing user-read-playback-state"

# HTTP request handler
class SpotifyAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/callback"):
            params = urllib.parse.parse_qs(self.path.split("?")[1])
            code = params.get("code", [None])[0]

            # Exchange code for tokens
            token_url = "https://accounts.spotify.com/api/token"
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET
            }
            r = requests.post(token_url, data=data)
            tokens = r.json()

            # Send a simple response
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"You can close this window now.")

            print("\n✅ ACCESS TOKEN:\n", tokens.get("access_token"))
            print("\n🔄 REFRESH TOKEN:\n", tokens.get("refresh_token"))
            exit()

# Build Spotify login URL
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPES
}
auth_url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)

# Open browser for login
print("Opening Spotify login...")
webbrowser.open(auth_url)

# Start HTTPS server
server_address = ('localhost', 8888)
httpd = HTTPServer(server_address, SpotifyAuthHandler)

# SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Waiting for Spotify authorization on https://localhost:8888/callback ...")
httpd.handle_request()
