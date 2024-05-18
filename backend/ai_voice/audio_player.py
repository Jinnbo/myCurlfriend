import time
from pygame import mixer

def playAudio():
    mixer.init()
    mixer.music.load("backend/ai_voice/audio/tempVoice.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    mixer.music.stop()
    mixer.music.unload()

    print("Finished!")
    return