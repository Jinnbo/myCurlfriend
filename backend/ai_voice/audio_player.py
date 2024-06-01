import time
from pygame import mixer
import os

def playAudio(audiofile):
    mixer.init()
    audio_path = f"ai_voice/audio/{audiofile}.mp3"
    mixer.music.load(audio_path)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    mixer.music.stop()
    mixer.music.unload()

    return