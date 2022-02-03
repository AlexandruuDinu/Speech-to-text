from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile('Priest_speech.wav') as audio_file:
    audio = recognizer.record(audio_file)

text_returned = recognizer.recognize_google(audio)
print(text_returned)

# ro-RO code for romanian language
