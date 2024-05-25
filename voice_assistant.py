import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

hello_google = pyttsx3.init()
listener = sr.Recognizer()
voices = hello_google.getProperty('voices')
hello_google.setProperty('voice', voices[1].id)


def talk(text):
    hello_google.say(text)
    hello_google.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if 'hello google' in command:
            #     command = command.replace('hello google', '')

    except:
        pass
    return command


def run_hello_google():
    command = take_command()
    if 'to mahi' in command:
        phone_number = "+880 1779-326282"
        command = command.replace('send', '')
        command = command.replace('to mahi', '')
        talk(f'sending {command} to mahi')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to aditya' in command:
        phone_number = "+880 1621-045306"
        command = command.replace('send', '')
        command = command.replace('to aditya', '')
        talk(f'sending {command} to aditya')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to tufail' in command:
        phone_number = "+880 1959-131951"
        command = command.replace('send', '')
        command = command.replace('to tufail', '')
        talk(f'sending {command} to tufail')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to record' in command:
        phone_number = "+880 1750-871239"
        command = command.replace('send', '')
        command = command.replace('to record', '')
        talk(f'sending {command} to saikat')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to kabir' in command:
        phone_number = "+880 1531-777773"
        command = command.replace('send', '')
        command = command.replace('to kabir', '')
        talk(f'sending {command} to kabir')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to sohag' in command:
        phone_number = "+880 1966-043891"
        command = command.replace('send', '')
        command = command.replace('to sohag', '')

        talk(f'sending {command} to sohag')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 15, True, 6)

    elif 'to nadeem' in command:
        phone_number = "+880 1640-637630"
        command = command.replace('send', '')
        command = command.replace('to nadeem', '')
        talk(f'sending {command} to nadeem')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 10, True, 6)

    elif 'to pagal' in command:
        phone_number = "+880 1605-552494"
        command = command.replace('send', '')
        command = command.replace('to pagal', '')
        talk(f'sending {command} to pavel')
        pywhatkit.sendwhatmsg_instantly(phone_number, command, 10, True, 6)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'good morning' in command:
        time = datetime.datetime.now().strftime('%H')

        if 5 < int(time) <= 11:
            talk('Good morning, sir')
        elif 11 < int(time) <= 17:

            talk('Sorry sir. I think you are wrong. It will be good afternoon')
        elif 17 < int(time) <= 22:
            talk('Sorry sir. I think you are wrong. It will be good Evening')
        elif 22 < int(time) <= 24 or 1 < int(time) < 4:
            talk('Sorry sir. I think you are wrong. It will be good night')

    elif 'good afternoon' in command:
        time = datetime.datetime.now().strftime('%H')
        if 5 < int(time) <= 11:
            talk('Sorry sir. I think you are wrong. It will be good morning')
        elif 11 < int(time) <= 17:
            talk('good afternoon, sir')
        elif 17 < int(time) <= 22:
            talk('Sorry sir. I think you are wrong. It will be good Evening')
        elif 22 < int(time) <= 24 or 1 < int(time) < 4:
            talk('Sorry sir. I think you are wrong. It will be good night')

    elif 'good evening' in command:
        time = datetime.datetime.now().strftime('%H')
        if 5 < int(time) <= 11:
            talk('Sorry sir. I think you are wrong. It will be good morning')
        elif 11 < int(time) <= 17:
            talk('Sorry sir. I think you are wrong. It will be good afternoon')
        elif 17 < int(time) <= 22:
            talk('good evening, sir')
        elif 22 < int(time) <= 24 or 1 < int(time) < 4:
            talk('Sorry sir. I think you are wrong. It will be good night')

    elif 'good night' in command:
        time = datetime.datetime.now().strftime('%H')
        if 5 < int(time) <= 11:
            talk('Sorry sir. I think you are wrong. It will be good morning')
        elif 11 < int(time) <= 17:
            talk('Sorry sir. I think you are wrong. It will be good afternoon')
        elif 17 < int(time) <= 22:

            talk('Sorry sir. I think you are wrong. It will be good Evening')
        elif 22 < int(time) <= 24 or 1 < int(time) < 4:
            talk('good night, sir. have a sexy dream')

    elif 'how are you' in command:
        talk('I am fine.')
    elif 'play' in command:
        song = command.replace('play', '')
        talk(f'playing {song}')
        pywhatkit.playonyt(song)

    elif 'fardeen' in command:
        talk('fardin is a bain-chod. he is a playboy.')

    elif "tell about" in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 2)
        talk(info)
    elif 'khan' in command:
        talk('saikat is a boka,chooda, saikat is a loved by his, Shashuri. ')

    elif 'mahi' in command:
        talk('mahi is a playboy. He loves ,Oorin. sometimes he fall in love with any girl. He jerks all the time. He '
             'also jumps all the time.')

    elif 'kabir' in command:
        talk('afif al kabir, is a enterprenour , and he is a gentlemen. also he is a computer engineer')

    elif 'fayaz' in command:
        talk(
            'faiaz sokal is a student of i,u,b. . he is a computer engineer  , he is a handsome boy, and a niqas pussy')

    elif 'tausif' in command:
        talk('Tausif is a student of i,u,b. a good person and a gentle boy')

    elif 'das' in command:
        talk('I have no information, about ramtonu das. I guess he is a good man, and , s,d,e,k')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'date' in command:
        talk('sorry vaiya, i am in another relation')

    elif 'gethu' in command:
        talk('gedu is a human, who invented, sodek- hopefully. ')

    else:
        talk('i did not get you, but i am going to search for you')
        pywhatkit.search(command)


hello_google.say(' Hello sir,I am your voice assistant. How can i help you?')
hello_google.runAndWait()

run_hello_google()
