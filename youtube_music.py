import os
import requests

youtube_api_key = os.environ["YOUTUBE_API_KEY"]


def get_youtube_music_playlist(playlist_id: str):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={youtube_api_key}&maxResults=100"

    response = requests.get(url)
    data = response.json()

    tracks = []

    for item in data["items"]:
        track_title = item["snippet"]["title"]
        tracks_artist = item["snippet"]["videoOwnerChannelTitle"].replace(
            " - Topic", ""
        )
        tracks.append(
            {
                "title": track_title,
                "artist": tracks_artist,
            }
        )

    return tracks
