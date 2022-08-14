import datetime
import pyttsx3

from configuration import configuration

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
speak_engine.setProperty('rate', 140)


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


# сказать текущее время
def ctime_command():
    now = datetime.datetime.now()
    speak("Сейчас " + str(now.hour) + ":" + str(now.minute))


# поздороваться
def greeting_command():
    speak("Приветствую " + configuration.get("user_name", ""))