import datetime
import wikipedia
import pyjokes
import webbrowser
from os import *
import pywhatkit
import sys
from .engine import takeCommand, speak
from .__main__ import PersonalGPT

def wishme():
    speak('Hello Sir,')
    hour = int(datetime.datetime.now().hour)
    
    if hour>=5 and hour<12: speak('Good Morning')
    elif hour>=12 and hour<16: speak('Good Afternoon')
    elif hour>=16 and hour<20: speak('Good Evening')
    else: speak('Good Night')
    
    speak('I am Jarvis. How can I help You now?')

websites=['facebook','instagram', 'linkedin', 'yahoo', 'twitter', 'gmail','google','youtube','amazon']
apps=['browser', 'notepad', 'terminal']
yes=['yes','yup','yeah','sure','ok','why not']

def call(query):
    #This is the main executable function
    while True:
        if 'wishme' in query: wishme()
        elif 'load gpt' in query:
            gpt = PersonalGPT()
        elif 'load documents' or 'load my documents' in query:
            gpt = PersonalGPT()
            gpt.from_my_docs()
        elif 'search my files now' or 'serach in gpt' in query:
            gpt.ask_query()
        
        elif 'wikipedia' in query:
            speak('Searching for wikipedia')
            queryy = query.replace('wikipedia','')
            results = wikipedia.summary(queryy, 2)
            speak(f'According to wikipedia, {results}')
        
        elif 'search' in query:
            queryy = query.replace('search','')
            link = f"https://www.google.com/search?q={queryy}"
            webbrowser.open(link)

        elif 'open' in query:
            queryy = query.replace('open','')
            if websites in queryy:
                webbrowser.open(f'http://www.{queryy}.com/')
            if apps in queryy:
                startfile(f'{queryy}')

        elif 'run speedtest' in query:
            webbrowser.open('https://www.speedtest.net/')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime('%Y-%m-%d')
            speak(f'Sir, the date is {strDate}')

        elif 'play' in query:
            song = query.replace('play', '')
            ans = takeCommand('from which player do you want to playing')
            if 'youtube' in ans:
                speak(f'playing {song} on youtube')
                pywhatkit.playonyt(song)
            else:
                speak("Can't playing sir right now")
                            
        elif 'send messege' in query:
            speak('send messege to whom?')
            number = takeCommand('Tell me the number, Sir ')
            message = takeCommand('Tell me the message, Sir')
            pywhatkit.sendwhatmsg_instantly(number, message)

        elif 'text to handwriting' in query:
            messege = takeCommand('tell the messege you want to convert')
            pywhatkit.text_to_handwriting(messege,'tth.png')

        elif 'send mail' in query:
            name = takeCommand('send mail to whom?')
            messege = takeCommand('tell the messege')
            pywhatkit.send_mail(name,'',messege)

        elif ('jokes' or 'joke') in query:
            joke = pyjokes.get_joke('en','neutral')
            speak(joke)
            choice = takeCommand("do you want one more?")
            if choice in yes:
                query = 'joke'

        elif 'sceenshot' in query:
            speak('Taking screenshot')
            pywhatkit.take_screenshot()

        elif 'open notepad' in query:
            print('opening notepad')
            system('Notepad')
            break

        elif 'open browser' in query:
            print('opening browser')
            startfile('msedge')
            break

        elif 'open twitter' in query:
            speak('opening twitter')
            webbrowser.open('http://twitter.com/')
            break
        

        elif ('end' or 'quit') in query:
            speak('quiting program')
            sys.exit(0)

        else:
            speak('cannot find anything')

if __name__ == '__main__':
    wishme()

#This whole program takes lot of time to write and frutefully execute.
#I am Swarnodip Nag, a programmer like you.
#This file is to dedicate all of you in the world for their education purpose and research purpose only.
#Thank you. Keep upgrading and have fun ;)