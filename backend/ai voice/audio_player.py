import time
from pygame import mixer


mixer.init()
mixer.music.load("file_example_MP3_1MG.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

print("Finished!")