import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source: 
     print('Enter Anything')