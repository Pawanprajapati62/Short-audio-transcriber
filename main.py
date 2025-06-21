import speech_recognition as sr


recognizer = sr.Recognizer()


with sr.AudioFile("sample.wav") as source:
    print("Listening to audio...")
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:\n", text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Request failed, check your internet.")
