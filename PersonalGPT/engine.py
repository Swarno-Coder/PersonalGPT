import pyttsx3 
import speech_recognition as sr 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(say=None):
    #This function takes command and recognize by google
    if say: speak(say)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        '''
        r.pause_threshold = 1
        r.phrase_threshold = 1
        r.operation_timeout = 10
        r.non_speaking_duration = 0
        r.energy_threshold = 400
        '''
        r.adjust_for_ambient_noise(source)
        audios = r.listen(source)
        
    try:
        print('Recognizing')
        queryy = r.recognize_google(audios, language='en-IN')
        return queryy.lower()
    except Exception as e:
        return None
