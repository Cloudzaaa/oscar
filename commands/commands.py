# DEPRECATED VER
import datetime
import pyttsx3

from config import configuration

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
speak_engine.setProperty('rate', 140)
speak_engine.save_to_file("Приветствую " + configuration.get("user_name", "") + ". Скорее бы стать еще лучше.", 'greeting_ver_1.mp3')


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
    text = "Приветствую " + configuration.get("user_name", "") + ". Скорее бы стать еще лучше."
    speak(text)
    speak_engine.save_to_file(text, 'greeting_ver_1.mp3')
    print('saved')


greeting_command()

