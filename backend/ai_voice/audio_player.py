import time
from pygame import mixer
import voice
import text_writer


text = text_writer.textWriter("Example Text")
voice.text_to_speech_file(text)

mixer.init()
mixer.music.load("backend/ai_voice/audio/tempVoice.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

print("Finished!")