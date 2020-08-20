Problem is :- "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."

import pyttsx3
import webbrowser
import datetime
import os
import sys

engine = pyttsx3.init('sapi5')

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
speak('WELCOME TO OS APPLICATION')
print()
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()
speak('Hello Sir')
print()


def myCommand():
    try:
        print()
        speak('How can I help you?')
        query = str(input('Command Here: '))
        return query
    except query.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        sys.exit()
    
        

if __name__ == '__main__':
    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'google' in query or 'chrome' in query:
            speak('okay')
            os.system('chrome')

        elif 'notepad' in query or 'text' in query or 'editor' in query or 'text editor' in query:
            speak('okay')
            os.system('notepad')

        elif 'sound' in query or 'dj' in query or 'music' in query or 'play music' in query:
            speak('okay')
            os.system('wmplayer')
            
        elif 'paint' in query or 'draw' in query or 'drawing' in query or 'sketch' in query:
            speak('okay')
            os.system('mspaint')
            
       
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query or 'shut' in query or 'shutdown' in query or  'quit' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()


 
 

 

 

   
