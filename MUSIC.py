import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import webbrowser
import os
import random
import pygame
pygame.mixer.init()
import time
from threading import Timer

def stop():
    pygame.mixer.music.stop()
    st.warning("music stoped")

# generation of music
import mido
from mido import MidiFile, MidiTrack, Message
from mingus.core import chords

model  = load_model("model.h5")
label = np.load("labels.npy")
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

st.header("Emotion Based Music Generation")

if "run" not in st.session_state:
	st.session_state["run"] = "true"

try:
	emotion = np.load("emotion.npy")[0]
except:
	emotion=""

if not(emotion):
	st.session_state["run"] = "true"
else:
	st.session_state["run"] = "false"

class EmotionProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		##############################
		frm = cv2.flip(frm, 1)

		res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

		lst = []

		if res.face_landmarks:
			for i in res.face_landmarks.landmark:
				lst.append(i.x - res.face_landmarks.landmark[1].x)
				lst.append(i.y - res.face_landmarks.landmark[1].y)

			if res.left_hand_landmarks:
				for i in res.left_hand_landmarks.landmark:
					lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			if res.right_hand_landmarks:
				for i in res.right_hand_landmarks.landmark:
					lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			lst = np.array(lst).reshape(1,-1)

			pred = label[np.argmax(model.predict(lst))]

			print(pred)
			cv2.putText(frm, pred, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)

			np.save("emotion.npy", np.array([pred]))

			
		drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_TESSELATION,
								landmark_drawing_spec=drawing.DrawingSpec(color=(0,0,255), thickness=-1, circle_radius=1),
								connection_drawing_spec=drawing.DrawingSpec(thickness=1))
		drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
		drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)


		##############################
        # landmark detection and emotion prediction

		return av.VideoFrame.from_ndarray(frm, format="bgr24")

lang = st.text_input("Language")
singer = st.text_input("Singer")
timer = st.text_input("How much time you want the music to play")
try:
    timer2 = int(timer)
except ValueError:
    st.warning("Please enter a valid numeric value for the timer.")

if lang and singer and st.session_state["run"] != "false":
	webrtc_streamer(key="key", desired_playing_state=True,
				video_processor_factory=EmotionProcessor)

btn = st.button("Recommend songs from YouTube")
btn2 = st.button("Shuffle songs from Database")
btn3 = st.button("Generate Music ")

if btn:
    if not emotion:
        st.warning("Please let me capture your emotion first")
        st.session_state["run"] = "true"
    else:
        raga = ""
        if emotion == "Shringara ":
            raga = "Yaman"
        elif emotion == "Hasya ":
            raga = "Kafi"
        elif emotion == "Karuna ":
            raga = "Bhairavi"
        elif emotion == "Raudra":
            raga = "Bhairav"
        elif emotion == "Veera":
            raga = "Bihag"
        elif emotion == "Bhayanaka":
            raga = "Malkauns"
        elif emotion == "Bibhatsa":
            raga = "Bhairav"
        elif emotion == "Adbhuta":
            raga = "Marwa"
        elif emotion == "Shanta":
            raga = "Ahir Bhairav"
        
        webbrowser.open(f"https://www.youtube.com/results?search_query={singer}+{lang}+{emotion}+navaras+{raga}+raga+song/music")
        np.save("emotion.npy", np.array([""]))
        st.session_state["run"] = "false"


if btn2:
    
    if not emotion:
        st.warning("Please let me capture your emotion first")
        st.session_state["run"] = "true"
    else:
        music_folder_path = "music_random"

        selected_emotion = emotion.capitalize() 
        subfolder_path = os.path.join(music_folder_path, selected_emotion)

        music_files = os.listdir(subfolder_path)

        if music_files:
            random_music_file = os.path.join(subfolder_path, random.choice(music_files))

            print("Playing:", random_music_file)

            try:
                pygame.mixer.music.load(random_music_file)
                pygame.mixer.music.play()

                st.success(f"Playing random music for {selected_emotion} emotion...")

                st.warning("Press the 'Stop Music' button to stop the song.")
                
                t = Timer(timer2,stop)
                t.start()
            except Exception as e:
                st.warning(f"Error playing the music: {e}")
        else:
            st.warning(f"No music found for {selected_emotion} emotion in the 'music_random' subfolder.")


if btn3:
    if not(emotion):
        st.warning("Please let me capture your emotion first")
        st.session_state["run"] = "true"
    else:
        emotion_notes = {
            "Shringara": [60,62,64,67,61,65,63,59,66,64,65,66,68,60,62,64,67,69,65,63,59,67,64,61,65,63,59],
            "Hasya": [60,62,64,65,67,69,71,72,61,63,65,66,68,70,72,73,74,73,71,69,67,66,64,62,60,61,63,65,66,68,70],
            "Karuna": [49,48,45,50,52,55,50,49,46,51,53,56,57,56,53,51,46,49,50,49,48,45,50,52,55,40,42,43,44,46,47,48,49,59,50,51,52,43,56,48,50,32,35,40,42,43,44,46],
            "Raudra": [70,72,74,75,77,78,79,67,69,71,74,76,69,72,74,76,70,74,75,77,78,79,67,69,71],
            "Veera": [72,74,76,77,79,82,84,86,87,89,91,93,95,108,100,96,74,76,77,79,82,84,89,80],
            "Bhayanaka": [85,87,89,77,72,74,76,78,79,81,83,85,87,88,90,92,94,95,80,71,74,76,69,72,74,76,],
            "Bibhatsa": [45,34,32,50,43,34,30,34,50,25,45,35,24,43,53,43,53,53,53,53,53,52,34,44,49,55,53],
            "Adbhuta": [62,64,65,67,69,71,72,74,76,77,79,81,82,84,64,64,64,67,68,57,58,59,39,49,29,57,47,69,70,71,23,72,77,75,74,71,69],
            "Shanta": [60,62,64,65,67,69,70,65,74,72,73,74,78,75,76,74,63,64,65,67,69,70,65,67,69,70,65,74,72,73,74  ]
}
        print("Captured Emotion:", emotion)

        midi_file = MidiFile()
        track = MidiTrack()
        midi_file.tracks.append(track)

        selected_emotion = emotion

        if selected_emotion in emotion_notes:
            for note in emotion_notes[selected_emotion]:
                track.append(Message('note_on', note=note, velocity=64, time=0))
                track.append(Message('note_off', note=note, velocity=64, time=400))
                
            midi_file.save('generated_music_navarasas.mid')
            st.success("Music generated based on Navarasas successfully!")
            st.write("Playing generated music...")
            
            pygame.mixer.init()
            pygame.mixer.music.load('generated_music_navarasas.mid')
            pygame.mixer.music.play()
            
            st.success(f"Playing music for {selected_emotion} emotion...")
            
            time.sleep(timer2)  

            pygame.mixer.music.stop()

            os.remove('generated_music_navarasas.mid')
        else:
            st.warning("Selected emotion is not recognized for music generation.")