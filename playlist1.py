import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                credentials[key.strip()] = value.strip()
    return credentials

# Read the credentials from the file
credentials = read_credentials('spotify_credentials.txt')


# Spotify OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=credentials['CLIENT_ID'],
    client_secret = credentials['CLIENT_SECRET'],
    redirect_uri= credentials['REDIRECT_URI'],
    scope = "playlist-modify-public playlist-modify-private user-modify-playback-state user-read-playback-state"
))

# Step 1: Create a Random Playlist
user_id = sp.current_user()['id']
playlist_name = f"My Random Playlist {random.randint(1000, 9999)}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
playlist_id = playlist['id']

# Search for random tracks and add them to the playlist
search_queries = ['rock', 'pop', 'hip-hop', 'jazz', 'classical']  # Customize the genres or queries as needed
track_uris = []

for query in search_queries:
    results = sp.search(q=query, type='track', limit=10)
    track = random.choice(results['tracks']['items'])
    track_uris.append(track['uri'])

# Add the tracks to the new playlist
sp.playlist_add_items(playlist_id, track_uris)

# Step 2: Play the Newly Created Playlist on an Active Device
devices = sp.devices()
if devices['devices']:
    # Start playing the playlist
    sp.start_playback(context_uri=f'spotify:playlist:{playlist_id}')

    print(f"Playlist '{playlist_name}' is playing on your active device!")
else:
    print("You don't have any active devices.")
