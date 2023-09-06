import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import requests


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('volume',1.0)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source_voice:
        print('Listening...')
        r.pause_threshold = .7
        r.energy_threshold = 500
        audio = r.listen(source=source_voice)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-in')
            print(f'{query}\n')

        except Exception:
            print('Sorry. Couldn\'t recognize')
            return 'NONE'
    return query
    
def sum():
    speak('Tell me the numbers you want to add by saying and after every number')
    print('Tell me the numbers you want to add by saying and after every number')
    numbers = command()
    lst = []
    for i in numbers.split():
        try:
            number = int(i)
            lst.append(number)
        except ValueError:
            pass
    sum = 0
    for j in lst:
        sum+=j
    speak(f'The sum is {sum}')
    print(f'The sum is {sum}')

def multiply():
    speak('Tell me the numbers you want to multiply by saying and after every number')
    print('Tell me the numbers you want to multiply by saying and after every number')
    numbers = command()
    lst = []
    for i in numbers.split():
        try:
            number = int(i)
            lst.append(number)
        except ValueError:
            pass
    res = 1
    for j in lst:
        res*=j
    speak(f'The resultant is {res}')
    print(f'The resultant is {res}')


def power():
    speak('Tell me two numbers ')
    print('Tell me two numbers ')
    numbers = command()
    lst = []
    for i in numbers.split():
        try:
            number = int(i)
            lst.append(number)
        except ValueError:
            pass
    res = lst[0]**lst[1]
    speak(f'The resultant is {res}')
    print(f'The resultant is {res}')


speak('Hey, I"m your assistant. What is your name')
name = command()

speak(name + 'If you want to skip the introduction, say skip')
query = command()

if 'skip' not in query:
    speak('Hey '+ name +'. What do you want me to do? I can add, subtract, multiply, raise a number to another number. I can also read news and create or read a file')
if __name__=='__main__':

    while(1):

        clear = lambda: os.system('cls')

        clear()
        
        query = command().lower()


        if 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google' in query:
            webbrowser.open('google.com')

        elif 'amazon' in query:
            webbrowser.open('amazon.in')

        elif 'wikipedia' in query:
            print('Searching...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences = 2)
            speak(result)
            print(result)

        elif ('create' or 'note') in query:
            speak('What should it\'s name be?')
            name = command()
            speak('What should I write?')
            text = command()
            
            file = open(f'{name}.txt','a')
            txt = file.write(text)
            file.close()

        elif ('open') in query:
            speak('What is the file name?')
            name = command()
            name = f'{name}.txt'
            if name in os.listdir():
                file = open(name,'r')
                z = file.read()
                speak(z)
                speak('Do you want to print it?')
                while True:
                    printing = str(command().lower())
                    if  'yes' in printing:
                        print(z)
                        speak('OK. Here you go.')
                        file.close()
                        break
                    elif 'no' in printing:
                        speak('OK')
                        file.close()
                        break
                    else:
                        speak('Sorry. I did not understand')
            else:
                speak('Sorry. This file is not in this directory')

        elif 'news' in query:
            url = ('https://newsapi.org/v2/top-headlines?'
            'country=in&'
            'sortBy=popularity&'
            'apiKey=YOUR API KEY FROM NEWSAPI.COM'
            )
            response = requests.get(url)
            x = response.json()
            y = x['articles']
            for i in y:
                speak(i['title'])
                print(i['title'])
                speak('DO YOU WANT DESCRIPTION: ')
                z = command().lower()
                if 'yes' in z:
                    speak(i['description'])
                    print(i['description'])
                elif 'quit' or 'enough' or 'stop' in z:
                    break
                else:
                    speak('OK')
                speak('MOVING ON TO THE NEXT NEWS')

        elif 'add' in query:
            sum()
        elif 'multiply' in query:
            multiply()
        elif 'power' in query:
            power()
        elif 'terminate' in query:
            speak('Bye, Have a great time')
            break


