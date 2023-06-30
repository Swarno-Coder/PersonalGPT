from PersonalGPT import takeCommand
from PersonalGPT import call

while True:
    com = takeCommand(say=None)
    print(com)
    if 'jarvis' or 'hey jarvis' in com:
        com = com.replace('hey jarvis' ,'')
        call(com)
    print('/')