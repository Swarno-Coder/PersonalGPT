from engine import takeCommand
from Jarvis import call

while True:
    some = takeCommand()
    if 'jarvis' or 'hey jarvis' in some:
        some = some.replace('hey jarvis' ,'')
        call(some)