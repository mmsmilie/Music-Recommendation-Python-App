import pickle
import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "f990dd6fd6fe41359bf31e13c4386af9"
CLIENT_SECRET = "0a18a3570dac423982cfaffb8675e2d3"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_song_icon(artist, song):
    searh_query = f"track:{song} artist:{artist}"
    results = sp.search(q=searh_query, type='track')

    if results and results['tracks']['items']:
        track = results['tracks']['items'][0]
        albub_icon = track['album']['images'][0]['url']
        return albub_icon
    else:
        return "nopicture.jpg"

def reccomend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    reccomended_music_names = []
    reccomended_music_icons = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist

        print(artist)
        print(music.iloc[i[0]].song)
        reccomended_music_names.append(music.iloc[i[0]].song)
        reccomended_music_icons.append(get_song_icon(artist, music.iloc[i[0]].song))
    return reccomended_music_names, reccomended_music_icons


st.header('Music Recommender System')
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similer.pkl', 'rb'))

song_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    song_list
)

if st.button('Recommend'):
    names, icons = reccomend(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(icons[0])
    with col2:
        st.text(names[1])
        st.image(icons[1])
    with col3:
        st.text(names[2])
        st.image(icons[2])
    with col4:
        st.text(names[3])
        st.image(icons[3])
    with col5:
        st.text(names[4])
        st.image(icons[4])
