from PersonalGPT.engine import takeCommand
from PersonalGPT.Jarvis import call

while True:
    some = takeCommand(say=None)
    if 'jarvis' or 'hey jarvis' in some:
        some = some.replace('hey jarvis' ,'')
        call(some)
    print('/')