import speech_recognition as sr
from time import ctime
from gtts import gTTS
import sys
import os

def listen(lang='en-US'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        data = r.listen(source)
    text = r.recognize_google(data, language='en-US')
    print(text)
    return text

def speak(audioString, lang="en"):
    gtts = gTTS(text=audioString, lang=lang)
    gtts.save('output.mp3')
    os.system('afplay output.mp3')
    print(audioString)

def app_open(query):
    app = '\ '.join(query)
    os.system('open /Applications/' + app + '.app')
    return 'Launched ' + app + '.'

def search(query):
    q = '+'.join(query[1:])
    if query[0] == 'Google':
        os.system("open http://www.google.com/?q="+q+"#")
    if query[0] == 'Wolfram':
        os.system("open http://www.wolframalpha.com/input/?i="+q)
    else:
        os.system("open http://www.google.com/?q="+q+"#")
    return 'Displaying results in browser.'

def spotify(query):
    q = query
    base = './shpotify/spotify'
    if q[0] == 'play':
        os.system(base + ' play ' + '"' + ' '.join(q[1:])+ '"')
    if q[0] == 'pause':
        os.system(base + ' pause')
    if q[0] == 'next':
        os.system(base + ' next')
    if q[0] == 'previous':
        os.system(base + ' prev')
    if q[0] == 'volume':
        os.system(base + ' vol ' + q[1])
    if q[0] == 'quit':
        os.system(base + ' quit')
    return ' '.join(q)

def main():
    speak('Hi, I\'m Alexis! How can I help today?')
    query = listen()
    while query != 'exit':
    	if 'Alexis' in query:
            query = ' '.join(query.split()[1:])
            # Conversation silliness
            if query == 'how are you':
                response = "I'm good! How are you?"
            elif query == 'what time is it':
                response = "It is " + str(ctime())
            # Open
            elif query.split()[0] == 'launch':
                response = app_open(query.split()[1:])
            # Search
            elif query.split()[0] == 'search':
                response = search(query.split()[1:])
            # Spotify
            elif query.split()[0] == 'Spotify':
                response = spotify(query.split()[1:])
            else:
                response = 'Sorry I didn\'t quite catch that.'
            speak(response)
            query = listen()
    speak('Bye!')

if __name__ == '__main__':
    main()
