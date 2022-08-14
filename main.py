import time
import speech_recognition as sr

from fuzzywuzzy import fuzz
from commands.commands import ctime_command, greeting_command
from configuration import configuration

options = configuration["options"]


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(options["alias"]):
            command = voice

            for alias in options['alias']:
                command = command.replace(alias, "").strip()

            for action in options['actions']:
                command = command.replace(action, "").strip()

            # распознаем и выполняем команду
            print(command)
            command = recognize_command(command)
            execute_command(command['command'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_command(command):
    recognized_command = {'command': '', 'percent': 0}
    for cmd, v in options['commands'].items():

        for x in v:
            vrt = fuzz.ratio(command, x)
            if vrt > recognized_command['percent']:
                recognized_command['command'] = cmd
                recognized_command['percent'] = vrt

    return recognized_command


def execute_command(command):
    if command == 'ctime':
        ctime_command()

    elif command == 'greeting':
        greeting_command()

    else:
        print('Команда не распознана, повторите!')


# запуск
recognizerInstance = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    recognizerInstance.adjust_for_ambient_noise(source)

greeting_command()

stop_listening = recognizerInstance.listen_in_background(mic, callback)
while True: time.sleep(0.1) # infinity loop