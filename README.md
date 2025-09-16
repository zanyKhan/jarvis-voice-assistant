# Voice Assistant - Jarvis

A Python-based voice assistant that can perform tasks like opening websites, playing music, reading news, and searching Wikipedia.

---

## Features

- Wake word detection (default: "jarvis")
- Open popular websites like Google, YouTube, Facebook, Instagram, LinkedIn
- Play songs from a predefined music library
- Fetch top news headlines
- Search Wikipedia for information
- Text-to-speech responses

---

## Installation

1. Clone the repository:
    ```bash
      git clone https://github.com/zanyKhan/jarvis-voice-assistant.git
      cd jarvis-voice-assistant

2. Create a virtual environment and activate it:
   ```bash
      python -m venv venv
      # Windows
      venv\Scripts\activate
      # macOS/Linux
      source venv/bin/activate
3. Install required packages:
    ```bash
    pip install -r requirements.txt
4. Make sure you have PyAudio installed for microphone support:
   ```bash
   pip install pyaudio
5. Run the program:
   ```bash
   python assistant.py

## Usage

Say the wake word (default: `jarvis`) to activate the assistant.

Give a command like:

- `"Open Google"`
- `"Play [song name]"`
- `"Show me news"`
- Any query to search Wikipedia

---

## Dependencies

- `SpeechRecognition`
- `pyttsx3`
- `requests`
- `wikipedia`
- `PyAudio` for microphone input

---

## Notes

- Ensure your microphone is working properly.
- You need an active internet connection for Wikipedia searches and news.
- Add your songs in `musicLibrary.py` with their links for playback.




