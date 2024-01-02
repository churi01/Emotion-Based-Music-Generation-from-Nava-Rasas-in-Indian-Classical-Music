# Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music
# (The steps to run this project are explained below.)
The integration of Navarasas in Indian classical music with emotion recognition, facial and hands landmark detection, Streamlit for web application, and the Mido module for music generation creates a comprehensive system that explores the intricate connection between emotions and musical expression.

# Emotion Recognition and Navarasas:
Emotion recognition plays a crucial role in this system as it helps in identifying the emotional nuances expressed through facial expressions and hand gestures. The Navarasas, comprising nine fundamental emotions, provide a rich framework for mapping these emotional cues to musical elements. The system leverages this emotional data to dynamically generate music that resonates with the intended emotional tone.

# Facial and Hands Landmark Detection with Mediapipe:
Mediapipe's facial and hands landmark detection capabilities enhance the system's ability to capture the performer's expressions and gestures accurately. By tracking facial landmarks and hand movements, the system gains a detailed understanding of the artist's emotional expressions, allowing for a more nuanced and personalized musical output.

# Streamlit for Web Application:
Streamlit, being a powerful framework for creating interactive web applications with minimal code, serves as the interface for users to interact with the music generation system. It provides a user-friendly environment where individuals can explore and experience the connection between emotions, facial expressions, and the resulting musical compositions. Users can select different Navarasas and witness real-time music generation based on the detected emotions.

# Mido Module for Music Generation:
The Mido module, a MIDI library for Python, facilitates the creation of musical compositions based on the input received from the emotion recognition system. Each Navarasa corresponds to a set of predefined musical notes, rhythms, and melodies. The Mido module transforms this emotional input into a musical output, allowing for the generation of unique compositions that mirror the performer's emotional expressions.

# User Experience and Exploration:
The web application not only serves as a platform for music generation but also offers an educational and exploratory experience for users interested in the connection between emotions and music. Users can witness the real-time transformation of emotional cues into musical expressions, fostering a deeper appreciation for the intricate relationship between the Navarasas and Indian classical music.

In summary, this integrated system creates a captivating and interactive experience, bridging the gap between traditional Indian classical music, modern technology, and the exploration of human emotions through the expressive medium of music.

# Steps to run this project:
(First, pip install all of the modules listed at the beginning of all three files.)
# Step 1
Run the "data_collection.py" file to detect the facial and handlandmark locations to create the dataset of your own. Give the user input a name (any name from the navarasas for whom you are creating the file).

![Screenshot (2)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/2d883ac2-84c4-4546-ade8-93212375f34b)

# Step 2
Create atleast 9 different facial expressions by running the "data_collection.py" file which will be saved as "XYZ.npy" files. Then run the data_training.py file to do the training on all the .npy files present in the folder. (I have provided the .npy files but i would recommed to create your own so the detection would be accurate).

# Step 3 
Lastly in the "MUSIC.py" file, write "streamlit run MUSIC.py" in the terminal, then it will redirect you to the webpage and the the application on streamlit. It will ask for three inputs from you and then will detect the facial emotions and based on it you can search or use "recommed song from youtube" button to search songs on youtube, "play random songs from the database" based on emotion detected ,which is not provided here but, if you are willing to do this project you can connect me on linkedin and l will provide you the drive link for it and lastly use the "music generation button" to generate music with the help of mido module according to emotion detected. (The notes provided in the third button are piano notes).

![Screenshot (10)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/1a2e0688-040f-41e9-8090-d73b0abbc731)
![Screenshot (9)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/1b280f89-f029-4826-8ceb-1d03b72ba4fe)
![Screenshot (5)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/cc301247-ffd1-474b-8204-b3d4b640f6de)
![Screenshot (7)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/36581f61-e1e4-4e17-ac00-ef4bc3faee71)
![Screenshot (8)](https://github.com/churi01/Emotion-Based-Music-Generation-from-Nava-Rasas-in-Indian-Classical-Music/assets/146198146/18905856-007f-4c7e-a652-1c06ac4fdbec)








