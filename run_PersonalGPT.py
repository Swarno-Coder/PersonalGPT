from PersonalGPT import takeCommand, call

while True:
    com = takeCommand(say=None)
    if 'hey jarvis' in com:
        com = com.replace('hey jarvis' ,'')
        call(com)