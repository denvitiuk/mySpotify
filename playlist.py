import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Настройка Spotify OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="token",
    client_secret="token",
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-modify-private user-top-read"
))

# Получение самого прослушиваемого трека пользователя за определенный период
top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')
top_track_ids = [track['id'] for track in top_tracks['items']]

# Создание нового плейлиста
user_id = sp.current_user()['id']
playlist_name = "Top Tracks Playlist"
playlist_description = "Most popular song playlist"
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

# Добавление треков в плейлист
sp.playlist_add_items(playlist_id=new_playlist['id'], items=top_track_ids)

print(f"Playlist successfully  '{playlist_name}' created and added to Spotify!")
