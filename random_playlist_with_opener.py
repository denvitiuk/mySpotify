import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import webbrowser

# Function to read credentials from the file
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

# Set up your Spotify API credentials using the read credentials
CLIENT_ID = credentials['CLIENT_ID']
CLIENT_SECRET = credentials['CLIENT_SECRET']
REDIRECT_URI = credentials['REDIRECT_URI']

SCOPE = 'playlist-modify-public playlist-modify-private'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Create a random playlist
user_id = sp.current_user()['id']
playlist_name = f"My Random Playlist {random.randint(1000, 9999)}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
playlist_id = playlist['id']

# Searching for random tracks and after adding them to playlist
search_queries = ['rock', 'pop', 'hip-hop', 'rap', 'classical']
track_uris = []

for query in search_queries:
    results = sp.search(q=query, type='track', limit=10)
    track = random.choice(results['tracks']['items'])
    track_uris.append(track['uri'])

sp.playlist_add_items(playlist_id, track_uris)

# Open the playlist in the default web browser
playlist_url = playlist['external_urls']['spotify']
webbrowser.open(playlist_url)

print(f"Playlist '{playlist_name}' created and opened successfully!")
