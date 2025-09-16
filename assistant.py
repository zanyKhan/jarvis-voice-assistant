import speech_recognition as sr
import webbrowser
import pyttsx3   #text to speech
import musicLibrary
import requests
import wikipedia

class VoiceAssistant:

    def __init__(self, wake_word="jarvis"):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init(driverName='sapi5')
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.wake_word = wake_word.lower()
        self.news_api_key = "08e15bdbeb0a4174a88b609dfabac7eb"

    def speak(self, text):
        self.engine.say(text + " .")
        self.engine.runAndWait()

    def process_command(self, command):
        command  = command.lower().strip()

        if "open google" in command:
            self.speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open facebook" in command:
            self.speak("Opening Google")
            webbrowser.open("https://www.facebook.com/")

        elif "open youtube" in command:
            self.speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "open instagram" in command:
            self.speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com/")

        elif "open linkedin" in command:
            self.speak("Opening Linkedin")
            webbrowser.open("https://in.linkedin.com/")

        elif command.startswith("play"):
            song = command.split(" ")[1]
            link = musicLibrary.music[song]
            self.speak(f"playing {song} song")
            webbrowser.open(link)

        elif "news" in command:
            r = requests.get("https://gnews.io/api/v4/top-headlines?token=2db256f387a28cfbb32eb4b132a76108&lang=en&country=in")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                # Print the headlines
                if not articles:
                    self.speak("No news found.")
                else:
                    self.speak("Here are the top headlines:")
                    for i, article in enumerate(articles[:5]):  # Speak only top 5
                        title = article.get('title', 'No title')
                        print(f"Headline {i+1}: {title}")
                        self.speak(title)
        else:
            output = self.search_wikipedia(command)
            self.speak(output)

    def search_wikipedia(self, command):
        try:
            result = wikipedia.summary(command, sentences=2)
            return result
        except Exception as e:
            print("Error:", e)

    def listen_for_wake_word(self):
        with sr.Microphone() as source:
            print("Listening for wake word...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=3)
                command = self.recognizer.recognize_google(audio).lower()
                if self.wake_word in command:
                    self.speak("Yes, tell me what happens?")
                    return self.listen_for_command()
            except sr.WaitTimeoutError:
                print("⏳ Timeout: No speech detected.")
            except sr.UnknownValueError:
                print("🤷 Could not understand audio.")
            except Exception as e:
                print(f"❌ Error: {e}")
            return None

    def listen_for_command(self):
        with sr.Microphone() as source:
            print("Listening for command...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command =  self.recognizer.recognize_google(audio)
            self.process_command(command)
            
    def run(self):
        self.speak("Initializing jarvis...")
        while True:
            self.listen_for_wake_word()


if __name__ == "__main__":
    assistant = VoiceAssistant(wake_word="alexa")
    assistant.run()