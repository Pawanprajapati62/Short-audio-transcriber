# 🎙️ Speech-to-Text Transcription Tool

This is a simple Python script that listens to a short audio file (sample.wav) and converts it into text using Google’s free Speech Recognition API.
🚀 How It Works

  - Loads the audio file (sample.wav)

  - Uses the speech_recognition library to process the audio

  - Sends the audio to Google for transcription

  - Prints the result in plain text

## 📁 Files

  - main.py: The main script that runs the speech-to-text process.
  - sample.wav: Your input audio file (make sure it exists in the same folder).

## ▶️ How to Run

  - Install the required library:
```bash
pip install SpeechRecognition
```
  - Make sure you have a file named sample.wav in the same folder.

Run the script:
```bash
    python main.py
```
## 🛠️ Notes

- Works best with clear audio and a good internet connection.

- Handles basic errors like no speech or internet issues.

- You can replace sample.wav with any .wav file of your choice.
