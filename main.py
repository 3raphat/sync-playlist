import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from youtube_music import get_youtube_music_playlist

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
refresh_token = os.environ["SPOTIPY_REFRESH_TOKEN"]

destination_playlist_id = os.environ["SPOTIPY_DESTINATION_PLAYLIST_ID"]
source_playlist_id = os.environ["YOUTUBE_SOURCE_PLAYLIST_ID"]

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:5000/callback",
    scope="playlist-modify-public playlist-modify-private",
)

token = sp_oauth.refresh_access_token(refresh_token)
access_token = token["access_token"]

sp = spotipy.Spotify(auth=access_token)

tracks = get_youtube_music_playlist(source_playlist_id)

uris = []

for track in tracks:
    search_query = f"track:{track['title']} artist:{track['artist']}"

    results = sp.search(
        search_query,
        type="track",
        limit=1,
    )

    if results["tracks"]["items"]:
        uri = results["tracks"]["items"][0]["uri"]
        uris.append(uri)
    else:
        continue

print(f"Found: {len(uris)}/{len(tracks)} track(s)")

try:
    sp.playlist_replace_items(destination_playlist_id, uris)
except Exception as e:
    print("Failed to add tracks to the playlist due to an error:", e)
else:
    print("Successfully added tracks to the playlist")
