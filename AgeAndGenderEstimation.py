from pyagender import PyAgender
import cv2
from gtts import gTTS
import os

agender = PyAgender()

faces = agender.detect_genders_ages(cv2.imread('screenshot.png'))

age_of_person = ''
gender = ''
t = ''
if faces != []:
    for face in faces:
        a = str(int(face['age']))+ ','
        g = int(face['gender'])
        if g >= 0.5:
            t = 'Female'
        else:
            t = 'Male'
        age_of_person += a
        gender += t + ','

n = 'The number of people in the scene is '+str(len(faces))
a = ' The ages are ' + age_of_person
g = ' The genders are ' + gender
output = n + a + g
print(output)

def run():
    with open('test.txt', 'w') as f:
        f.write(output)
        f.close()

    with open("test.txt", 'r') as file:
        file = file.read()

    speak = gTTS(file, lang='en')
    speak.save("audio_new.mp3")

    file = "audio_new.mp3"
    os.system("mpg123 " + file)
    open('test.txt', 'w').close()
