import voice
import text_writer
import audio_player


while True:
    inputtext = input()
    if inputtext == "stop":
        break
    else:
        # text = text_writer.textWriter(inputtext)
        # voice.text_to_speech_file(text,"encouragement")
        # inputtext = input()
        # text = text_writer.textWriter(inputtext)
        # voice.text_to_speech_file(text,"newrep")
        # inputtext = input()
        # text = text_writer.textWriter(inputtext)
        # voice.text_to_speech_file(text,"halfrep")

        text = text_writer.textWriter(inputtext)
        voice.text_to_speech_file(text, "halfrep1")

        

