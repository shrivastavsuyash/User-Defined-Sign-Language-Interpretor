#reading instructions
import pyttsx
engine = pyttsx.init()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate',150)
engine.setProperty('volume',1)

def speak(data):
    engine.say(data)
    engine.runAndWait()

f=open("instructions.txt",'r+')
data=f.read()
speak(data)
