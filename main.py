import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="token",
    client_secret="token",
    redirect_uri="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    scope="user-library-read user-top-read"
))

# Check is token valid/working properly
token_info = sp.auth_manager.get_cached_token()
if not token_info:
    print("Didn't get token.")
else:
    print("Token is obtained successfully.")

#  Getting top tracks
try:
    top_tracks = sp.current_user_top_tracks(limit=5)
    top_track_ids = [track['id'] for track in top_tracks['items']]

    # Getting recommendation
    recommendations = sp.recommendations(seed_tracks=top_track_ids, limit=5)

    # Output recommendation
    for track in recommendations['tracks']:
        print(f"Recommended track: {track['name']} - {track['artists'][0]['name']}")

except spotipy.exceptions.SpotifyException as e:
    print(f"Error: {e}")
