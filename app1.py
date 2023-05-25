# import module
import pandas as pd
import streamlit as st
import pickle
import random
from scipy.spatial import distance

def sim_track_find(word, artist):
    a = 0
    b = 0
    song = []
    indexes = []
    for i in music["name"]:
        if word.lower() in i.lower() and artist.lower() in music["artist"][a].lower():
            song.append(music_param[a:a + 1].values)
            indexes.append(a)
            b += 1
        a += 1
    if b == 0:
        return 0

    return song[0][0], indexes[0]

def similar_tracks(music,song = "",artist = "",number = 5):

    if (sim_track_find(song,artist) == 0):
        return 0
    else:
        x=sim_track_find(song,artist)[0]
        index = sim_track_find(song,artist)[1]
    p = []
    count=0
    for i in music_param.values:
        p.append([distance.cosine(x,i),count])
        count+=1

    p.sort()
    song_names = music["name"]
    artist_names = music["artist"]
    id = music["id"]

    recommended_music = []

    for i in range(1,number+1):
        recommended_music.append([id[p[i][1]],song_names[p[i][1]],artist_names[p[i][1]]])

    return recommended_music

def mood(mood, num=5):
    if mood == "calm":
        st.subheader("Mood: Calm")
        return random.choices(music_calm, k=5)

    if mood == "angry":
        st.subheader("Mood: Angry")
        return random.choices(music_energetic, k=5)

    if mood == "happy":
        st.subheader("Mood: Happy")
        return random.choices(music_happy, k=5)

    if mood == "sad":
        st.subheader("Mood: Sad")
        return random.choices(music_sad, k=5)


#reading the dataset
music_dict = pickle.load(open('music_dict.pkl','rb'))
music_dict2 = pickle.load(open('music_dict2.pkl','rb'))
music_dict_calm = pickle.load(open('music_dict_calm.pkl','rb'))
music_dict_energetic = pickle.load(open('music_dict_energetic.pkl','rb'))
music_dict_happy = pickle.load(open('music_dict_happy.pkl','rb'))
music_dict_sad = pickle.load(open('music_dict_sad.pkl','rb'))

music = pd.DataFrame(music_dict)
music_param = pd.DataFrame(music_dict2)
music_calm = pd.DataFrame(music_dict_calm).to_numpy()
music_energetic = pd.DataFrame(music_dict_energetic).to_numpy()
music_happy = pd.DataFrame(music_dict_happy).to_numpy()
music_sad = pd.DataFrame(music_dict_sad).to_numpy()

# Title
st.title("Music Recommendation System")

#Select box
music['name'][0] = "Choose a Song to Recommend"
selected_music = st.selectbox("Select your song: ",music['name'].values)

#Create Button
if(st.button("Recommend")):
    if selected_music == "Choose a Song to Recommend":
        pass

    else:
        recommended_music = similar_tracks(music,selected_music)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("img_1.png")
            st.write("Title Name:",recommended_music[0][1])
            st.write("Artist Name:",recommended_music[0][2])

        with col2:
            st.image("img_2.png")
            st.write("Title Name:",recommended_music[1][1])
            st.write("Artist Name:",recommended_music[1][2])

        with col3:
            st.image("img_3.png")
            st.write("Title Name:",recommended_music[2][1])
            st.write("Artist Name:",recommended_music[2][2])

        with col4:
            st.image("img_4.png")
            st.write("Title Name:",recommended_music[3][1])
            st.write("Artist Name:",recommended_music[3][2])

        with col5:
            st.image("img_5.png")
            st.write("Title Name:",recommended_music[4][1])
            st.write("Artist Name:",recommended_music[4][2])


st.subheader("OR")

selected_mood = st.selectbox("Select your emotion: ",
                             ["Choose a Emotion","Calm","Angry","Happy","Sad"])

#camera button
if(st.button("Suggest")):
    if selected_mood == "Choose a Emotion":
        pass

    else:
        suggested_song = mood(selected_mood.lower())

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("img_3.png")
            st.write("Title Name:", suggested_song[0][0])
            st.write("Artist Name:", suggested_song[0][1])

        with col2:
            st.image("img_2.png")
            st.write("Title Name:", suggested_song[1][0])
            st.write("Artist Name:", suggested_song[1][1])

        with col3:
            st.image("img_4.png")
            st.write("Title Name:", suggested_song[2][0])
            st.write("Artist Name:", suggested_song[2][1])

        with col4:
            st.image("img_1.png")
            st.write("Title Name:", suggested_song[3][0])
            st.write("Artist Name:", suggested_song[3][1])

        with col5:
            st.image("img_5.png")
            st.write("Title Name:", suggested_song[4][0])
            st.write("Artist Name:", suggested_song[4][1])


