import datetime
import wikipedia
import pyjokes
import webbrowser
from os import *
import pywhatkit
import os
from .engine import takeCommand, speak
from .main import PersonalGPT

def wishme():
    speak('Hello Sir,')
    hour = int(datetime.datetime.now().hour)
    
    if hour>=5 and hour<12: speak('Good Morning')
    elif hour>=12 and hour<16: speak('Good Afternoon')
    elif hour>=16 and hour<20: speak('Good Evening')
    else: speak('Good Night')
    
    speak('I am Jarvis. How can I help You now?')


def call(query):
    #This is the main executable function
    while True:
        if 'wishme' in query: wishme()
        
        if 'load documents' or 'load my documents' in query:
            gpt = PersonalGPT()
        if 'search my files now':
            gpt.ask_query()
        if 'wikipedia' in query:
            speak('Searching for wikipedia')
            queryy = query.replace('wikipedia','')
            results = wikipedia.summary(queryy, 2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        
        elif 'search' in query:
            queryy = query.replace('search','')
            link = f"https://www.google.com/search?q={queryy}"
            webbrowser.open(link)

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com/')

        elif 'open gmail' in query:
            webbrowser.open('http://www.gmail.com/')

        elif 'open facebook' in query:
            webbrowser.open('http://www.facebook.com/')

        elif 'open w3schools' in query:
            webbrowser.open('http://www.w3schools.com/')

        elif 'open ookla' in query:
            webbrowser.open('https://www.speedtest.net/')

        elif 'open hoichoi' in query:
            webbrowser.open('http://www.hoichoi.tv/')

        elif 'open flipkart' in query:
            webbrowser.open('http://www.flipkart.com/')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'Sir, the time is {strTime}')
            speak(f'Sir, the time is {strTime}')

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime('%Y-%m-%d')
            print(f'Sir, the date is {strDate}')
            speak(f'Sir, the date is {strDate}')

        elif 'play' in query:
            song = query.replace('play', '')
            print('from which player do you want to playing')
            speak('from which player do you want to playing')
            ans = takeCommand()
            if 'youtube' in ans:
                speak('playing ' + song + ' on youtube')
                pywhatkit.playonyt(song)
            """elif 'default player' in ans:
                speak('playing ' + song + ' on default player')
                muDir = 'D:\SONGS'
                path = os.path.join(muDir, (song + '.mp3'))
                for root, dirs, files in os.walk(muDir):
                    for file in files:
                        if file.endswith('.mp3'):
                            #p = vlc.MediaPlayer(path)
                            #p.play()
                            if('0xdd'=='q'):
                                #p.stop()
                                break
            """
                            
        elif 'send messege' in query:
            print('send messege to whom?')
            speak('send messege to whom?')
            number = input('Enter the number: ')
            print('tell the messege')
            speak('tell the messege')
            messege = takeCommand()
            pywhatkit.sendwhatmsg_instantly(number, messege)

        elif 'text to handwriting' in query:
            print('tell the messege you want to convert')
            speak('tell the messege you want to convert')
            messege = takeCommand()
            pywhatkit.text_to_handwriting(messege,'tth.png')

        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)

        elif 'send mail' in query:
            print('send mail to whom?')
            speak('send mail to whom?')
            name = takeCommand()
            speak('tell the messege')
            print('tell the messege')
            messege = takeCommand()
            pywhatkit.send_mail(name,'',messege)

        elif ('jokes' or 'joke') in query:
            joke = pyjokes.get_joke('en','neutral')
            print(joke)
            speak(joke)
            speak("do you want one more?")
            print("do you want one more?")
            choice = takeCommand()
            if ('yes' or 'yup' or 'yeah' or 'sure' or 'ok' or 'why not') in choice:
                continue
            elif 'no' in choice:
                break
    
            '''
            '''

        elif 'sceenshot' in query:
            print('Taking screenshot')
            speak('Taking screenshot')
            pywhatkit.take_screenshot()

        elif 'open notepad' in query:
            speak('opening notepad')
            print('opening notepad')
            system('Notepad')
            break

        elif 'open browser' in query:
            speak('opening browser')
            print('opening browser')
            startfile('msedge')
            break

        elif 'open twitter' in query:
            speak('opening twitter')
            print('opening twitter')
            webbrowser.open('http://twitter.com/')
            break
        

        elif ('end' or 'quit') in query:
            print('quiting-- program')
            speak('quiting program')
            break

        else:
            print('Cannot Find Anything')
            speak('cannot find anything')

if __name__ == '__main__':
    wishme()

#This whole program takes lot of time to write and frutefully execute.
#I am Swarnodip Nag, a programmer like you.
#This file is to dedicate all of you in the world for their education purpose and research purpose only.
#Thank you. Keep upgrading and have fun ;)