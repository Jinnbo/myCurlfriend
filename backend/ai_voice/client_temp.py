import voice
import text_writer
import audio_player

text = text_writer.textWriter("Example Text")
voice.text_to_speech_file(text)
audio_player.playAudio()

