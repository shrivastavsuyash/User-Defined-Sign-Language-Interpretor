import speech_recognition as sr
import pyttsx
from os import path
engine = pyttsx.init()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate',150)
engine.setProperty('volume',1)
def convert(AUDIO_FILE):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), AUDIO_FILE)
    r=sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        try:
            data=r.recognize_google(audio)
        except:
            data=''
    return(data)
def listn():#Recognise function
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        audio = r.listen(source)
    data=r.recognize_google(audio)
    return(data)
def store(data):
    f=open("txt1.txt","w+")
    f.write(data)
    f.close
def speak(data):
    print(data)
    engine.say(data)
    engine.runAndWait()
print("\t\t\t\tWELCOME to Audio to text converter\t\t\t")
cont=0
audio=''
def read_from_user():
    data=''
    while(data!="exit"):
        try:
            data=listn()
        except:
            data=input("write")
        print(data)
def audio_extract():
    data=''
    aud=input("Enter the name of the audio file")
    data=convert(aud)
    while(data==''):
        print("Reparsing data")
        data=convert(aud)
    store(data)
    print("stored")
def menu():
    print("PRESS 1 to READ from the USER\nPRESS 2 to Extract from audio")

while(True):
    menu()
    user_ch=int(input("ENTER::"))
    if(user_ch==1):
        read_from_user()
    elif(user_ch==2):
        audio_extract()
    else:
        print("Invalid Input")

    

        
        
