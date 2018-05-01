import pyttsx
engine = pyttsx.init()
def speak(data):
    engine.say(data)
    engine.runAndWait()
cont=0
audio=''
while(audio!="exit"):
    audio=input("Type that you want to speak-")
    print(audio)
    data=speak(audio)
