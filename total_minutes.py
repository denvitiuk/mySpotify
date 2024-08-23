import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                credentials[key.strip()] = value.strip()
    return credentials

credentials = read_credentials('spotify_credentials.txt')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=credentials['CLIENT_ID'],
    client_secret = credentials['CLIENT_SECRET'],
    redirect_uri= credentials['REDIRECT_URI'],
    scope = "user-read-recently-played"

))
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'


now = datetime.utcnow()
yesterday = now - timedelta(days=1)

# Initialize variables
total_ms = 0
last_timestamp = None

# Loop through recently played tracks, stopping when we go beyond 24 hours
while True:
    # Fetch recently played tracks
    results = sp.current_user_recently_played(limit=50, after=int(yesterday.timestamp() * 1000))

    # If no results are returned, break the loop
    if not results['items']:
        break

    for item in results['items']:
        played_at = datetime.strptime(item['played_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if played_at < yesterday:
            break
        total_ms += item['track']['duration_ms']
        last_timestamp = item['played_at']

    # Break if we've processed all tracks within the last 24 hours
    if played_at < yesterday:
        break

print(f"You've listened to {total_ms / 60000:.2f} minutes of music in the last 24 hours.")
