import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text

settings = config.settings
options = settings.get('options')

print(f"{settings.get('assistant_name')} начал свою работу ...")


def va_respond(voice: str):
    if voice.startswith(options.get('alias')):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in options.get('commands').keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for word in options.get('alias'):
        cmd = cmd.replace(word, "").strip()

    for word in options.get('actions'):
        cmd = cmd.replace(word, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, expression in options.get('commands').items():
        for char in expression:
            vrt = fuzz.ratio(cmd, char)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "здороваться ..."
        text += "произносить время ..."
        text += "и нести чушь."
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.va_speak(text)
    elif cmd == 'greeting':
        # current time
        text = "Приветствую создателЯ!"
        tts.va_speak(text)


# начать прослушивание команд
stt.va_listen(va_respond)