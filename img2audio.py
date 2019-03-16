from PIL import Image
import pytesseract
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Simple image to string
output = pytesseract.image_to_string(Image.open('screenshot.png'))

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
