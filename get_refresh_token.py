import os
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:5000/callback",
    scope="playlist-modify-public playlist-modify-private",
)

token = sp_oauth.get_access_token()
refresh_token = token["refresh_token"]

print("\nPlease copy your refresh_token to github's secret\n")
print(refresh_token)
