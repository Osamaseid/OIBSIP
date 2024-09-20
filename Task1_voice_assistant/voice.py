import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import webbrowser
import logging
import tkinter as tk
import threading

logging.basicConfig(level=logging.INFO)

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
tts_lock = threading.Lock()

def speak(text):
    with tts_lock:  
        tts_engine.say(text)
        tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        logging.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=3)
            command = recognizer.recognize_google(audio)
            logging.info(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            logging.warning("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            logging.error("Speech service is down.")
            return ""
        except Exception as e:
            logging.error(f"Listening error: {e}")
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

def handle_command():
    command = listen()
    if command:
        if 'hello' in command:
            speak("Hello Osama!")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            speak(f"Today's date is {date}")
        elif 'search' in command:
            speak("What do you want to search for?")
            search_query = listen()
            if search_query:
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
            speak("Goodbye!")
            root.quit()

def start_listening():
    while True:
        handle_command()

def on_speak_button_click():
    threading.Thread(target=start_listening, daemon=True).start()

root = tk.Tk()
root.title("Voice Assistant")
root.geometry("300x200")

btn = tk.Button(root, text="Speak", command=on_speak_button_click, height=2, width=15, bg="blue", fg="white")
btn.pack(pady=20)

root.mainloop()