import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Настройка Spotify OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="token",
    client_secret="token",
    redirect_uri=" http://localhost:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

# Убедитесь, что у вас есть активное устройство для воспроизведения
devices = sp.devices()
if devices['devices']:

    track_id = "7Gx2q0ueNwvDp2BOZYGCMO"  # Here you can easily add your favourite track using special id.For that just open open.spotify in browser and later copy.For example,I added Pink Floyd-Money with link: https://open.spotify.com/track/7Gx2q0ueNwvDp2BOZYGCMO



    # Начинаем воспроизведение трека
    sp.start_playback(uris=[f'spotify:track:{track_id}'])

    print("Track is playing!")
else:
    print("You don't have any active devices.")
