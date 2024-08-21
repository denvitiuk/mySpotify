import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Настройка Spotify OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="0eb9bd6e41ff4bbea4d302cfbc6ee3bc",
    client_secret="6a5c61e8a6ec42ef9e1287b2bb25ef4f",
    redirect_uri="http://localhost:8888/callback",
    scope="user-top-read"
))

# Функция для получения топ треков для заданного периода времени
def get_top_tracks(time_range, limit=50):
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    track_data = []
    for track in top_tracks['items']:
        track_data.append({
            'Название трека': track['name'],
            'Артист': track['artists'][0]['name'],
            'Популярность': track['popularity'],
            'Период': time_range
        })
    return track_data

# Getting all popular track during three periods(short_term = 1 month,medium_term = 6 month,long_term = all time)
short_term_tracks = get_top_tracks('short_term')
medium_term_tracks = get_top_tracks('medium_term')
long_term_tracks = get_top_tracks('long_term')

# Merged in one DataFrame
all_tracks = short_term_tracks + medium_term_tracks + long_term_tracks
df = pd.DataFrame(all_tracks)

# Сохранение в CSV файл
df.to_csv('spotify_top_tracks.csv', index=False, encoding='utf-8')

print("Successfully saved 'spotify_top_tracks.csv'")
