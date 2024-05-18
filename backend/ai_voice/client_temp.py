import voice
import text_writer
import audio_player


while True:
    inputtext = input()
    if inputtext == "stop":
        break
    else:
        #text = text_writer.textWriter(inputtext)
        voice.text_to_speech_file(inputtext)
        audio_player.playAudio()