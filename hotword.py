import speech_recognition as sr
import subprocess
import pyttsx3
import time

engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 207)
  
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def takeCommand1():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio = r.listen(source)
        
       
    try:
        print("Recognising...")
        query= r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        
        
    except Exception as e:
        return "None"
    
    return query.lower()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        r.pause_threshold=0.5
        audio = r.listen(source)
        
       
    try:
        #print("Recognising...")
        query= r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        
        
    except Exception as e:
        return "None"
    
    return query.lower()

def Identify():
    pwd = "abcd"
    speak("Identify yourself")
    auth =takeCommand1()
    time.sleep(2)
    def check():
        speak("Should i proceed to authenticate?")
        ans = takeCommand1() 
        if "go ahead" in ans or "sure" in ans:
            if str(pwd) == str(auth):
                subprocess.run("python GUI.py & python main.py", shell=True)
                    
            else:
                speak("Identification failed. Bugger off!")    
        
        elif "no" in ans or "negative" in ans:
            Identify()
            
        else:
            check()
    check()

while True:
    wake = takeCommand()
    
    if "wake up alex" in wake or "hey alex" in wake:
        Identify()
        
    else: 
        pass