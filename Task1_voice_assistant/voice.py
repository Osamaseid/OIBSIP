import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken and saved.")

def search_youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    speak(f"Searching YouTube for {query}")

def search_google(query):
    pywhatkit.search(query)
    speak(f"Searching Google for {query}")

def main():
    speak("Hello osama! How can I assist you today?")
    try:
        while True:
            command = listen()

            if 'hello' in command:
                speak("Hello!")
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f"The current time is {time}")
            elif 'date' in command:
                date = datetime.datetime.now().strftime('%Y-%m-%d')
                speak(f"Today's date is {date}")
            elif 'search' in command:
                speak("What do you want to search for?")
                search_query = listen()
                if 'youtube' in search_query:
                    speak("What do you want to search on YouTube?")
                    query = listen()
                    if query:
                        search_youtube(query)
                else:
                    search_google(search_query)
            elif 'screenshot' in command:
                take_screenshot()
            elif 'exit' in command or 'quit' in command:
                speak("Goodbye osama!")
                break
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        speak("Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred. Please try again.")
    finally:
        print("Exiting program.")

if __name__ == "__main__":
    main()
