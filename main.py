# Modules
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(name):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

    speak(f"I am JARVIS {name}. How can I help you?")
    print(f"I am JARVIS {name}. How can I help you?")


def takeCommand():
    '''
    It will take voice input
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as err:
        print("Say again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishme("Arin")
    # Logic
    while True:
        query=takeCommand().lower()
