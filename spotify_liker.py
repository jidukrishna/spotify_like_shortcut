import time
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from winotify import Notification
from dotenv import dotenv_values

config=dotenv_values("spotify_data.env")
client_id=config["client_id"]
client_secret=config["client_secret"]
redirect_uri=config["redirect_uri"]
def add_to_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
    scope="user-read-playback-state,playlist-modify-private,user-library-modify,user-library-read"))



    r1=sp.currently_playing(market="ES")
    song_name=(r1["item"]["name"])
    artist_name=(r1["item"]["artists"][0]["name"])
    song_uri=r1["item"]["uri"]
    data=""
    check_inside=sp.current_user_saved_tracks_contains([song_uri])[0]
    if not check_inside:
        sp.current_user_saved_tracks_add([song_uri])
        return  {"status":True,"song":song_name,"artist":artist_name,"data":data}
    else:
        return {"status": False, "song": song_name, "artist": artist_name,"data":data}

value=add_to_playlist()
song = value["song"]
artist = value["artist"]
data=value["data"]
image=os.path.join(os.getcwd(),"newicon.png")
if value["status"]:
    toast=Notification(icon=image,app_id="spotify adder",title=f"Added music "+data,msg=f"Added 🩷 {song}\nby {artist}",duration="short")
    toast.show()
else:
    toast=Notification(icon=image,app_id="spotify adder",title=f"already in playlist "+data,msg=f"song:{song} ✔️already \nin playlist ",duration="short")
    toast.show()
exit()
