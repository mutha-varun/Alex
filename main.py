import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import os
import time
import PyPDF2
import pyautogui
from pywikihow import search_wikihow
from gtts import gTTS
import wikipedia as googleScrap
import speedtest
from googletrans import Translator
import pyjokes
from PyDictionary import PyDictionary as dict
from playsound import playsound
from tkinter import Label, Entry, Button, Tk, StringVar
from pytube import YouTube
import wolframalpha 
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 207)
  
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak("Good Morning! How can i help you,good sir?")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon! How can i help you,good sir?")
        
    else:
        speak("Good Evening! How can i help you,good sir?")
        
def Dict():
    speak("What should i search for good sir?")
    topic = takeCommand()

    if "meaning" in topic:
        topic = topic.replace("tell me the meaning of", "")
        result = dict.meaning(topic)
        speak(result)
        
    elif "synonym" in topic:
        topic=topic.replace("tell me the synonym of", "")
        result=dict.synonym(topic)
        speak(result)

    elif "antonym" in topic:
        topic=topic.replace("tell me the antonym of", "")
        result=dict.antonym(topic)
        speak(result)

    speak("Anything else good sir?")
    ans = takeCommand()
    if "yes" in ans:
        Dict()

    elif "no" in ans:
        return None

def Spotify(song1):

    os.system("open /Applications/Spotify.app")
    if song1=='1':
        #for playlist 
        time.sleep(8)
        pyautogui.click(148, 356)
        #for playing
        time.sleep(6)
        pyautogui.click(371, 453) 
        
    elif song1=="2":
        time.sleep(8)
        pyautogui.click(730, 837)
        
    else:
        #search bar
        time.sleep(8)
        pyautogui.click(109, 148)
        time.sleep(2)
        pyautogui.write(song1)
        time.sleep(10)
        pyautogui.click(710, 439)
        
def WhatsApp():
    speak("To whom do you want to send the message?")
    name = takeCommand()

    def op():
        os.system("open /Applications/WhatsApp.app")
        time.sleep(6)
        pyautogui.click(128, 115)
        pyautogui.write(name)
        time.sleep(1)
        pyautogui.press('down') 
        mes()
        
    def mes():
        speak("What do you want to send?")
        message= takeCommand()
        time.sleep(0.5)
        pyautogui.click(704, 775)
        pyautogui.write(message)
        
        speak("should i send?")
        ans= takeCommand().lower()
        
        if ans == "yes":
            pyautogui.press('enter')
            
        elif ans == "no":
            pyautogui.press(['command','delete'])
            mes()
            
        elif ans=="cancel":
            return None

    op()

def Screenshot():
    speak("what should i name the file sir?")        
    name = takeCommand()
    ext = name + ".png"
    path = "/Users/Varun/Documents/Programming/PythonProjects/Alex/Items/ss/"+ext
    ss = pyautogui.screenshot()
    ss.save(path)
    speak("Should open the file?")
    ans = takeCommand()
    if "yes" in ans:
        os.system("open "+path)

    elif "no" in ans:
        return None

def App(ch):

    if ch == '1':
        speak("which app should i open?")
        name = takeCommand().title()
        
        if name == None:
            return  None
        
        else:    
            os.system("open -a "+ name)
        
    elif ch == '2':
        speak("which app should i close?")
        name = takeCommand().title()
        
        if name == None:
            return None
        
        else:
            os.system("pkill "+name)

def Reader():
    os.system("open /Users/Varun/Documents/Programming/PythonProjects/Alex/Items/The last Olympian.pdf")
    book = open("/Users/Varun/Documents/Programming/PythonProjects/Alex/Items/The last Olympian.pdf","rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.getNumPages(book)
    speak(f"There are {pages} pages in this book")
    speak("From which page should i start reading?")
    num = takeCommand()
    page = pdfreader.getPage(num)
    text=page.extractText()
    speak("In which language should i read?")
    lang = takeCommand()

    if "hindi" in lang:
        trans = Translator()
        textHin= trans.translate(text, "hi")
        textm= textHin.text
        speech = gTTS(text = textm)
        try:
            speech.save("book.mp3")
            playsound("book.mp3")
            
        except:
            playsound("book.mp3")
            
            
    else:
        speak(text)

def SpeedTest(test):
    speak("Checking Speed.....")
    speed= speedtest.Speedtest()
    downloading= speed.download()
    corrDown = int(downloading/800000)
    uploading= speed.upload()
    corrUp = int(uploading/800000)

    if '1' in test:
        speak(f"Uploading Speed is {corrUp} mbps")
        
    elif '2' in test:
        speak(f"Downloading Speed is {corrDown} mbps")

    else:
        speak(f"Downloading Speed is {corrDown} mbps and Uploading Speed is {corrUp} mbps")
        
def VideoDownloader():
    root = Tk()
    root.geometry('500x300+480+120')
    root.resizable(0,0)
    root.title('Video Downloader')

    speak("Enter video URL here!")

    Label(root, text = "YouTube video downloader", font = "arial 15 bold" ).pack()

    link = StringVar()
    Label(root, text = "Paste Yt video URL here", font = "arial 15 bold").place(x=160, y=60)

    Entry(root, width=70, textvariable=link).place(x=22, y=90)

    def Download():
        url= YouTube(str(link.get()))
        video = url.streams.first()
        video.download(filename="download.mp4", output_path="/Users/Varun/Documents/Programming/PythonProjects/Alex/Items/download")
        
        Label(root, text= "Downloaded", font="arial 15").place(x= 180, y= 210)
        
    Button(root, text="Download", font="arial 15 bold", bg = "pale violet red", padx=2, command=Download)


    root.mainloop()
    speak("Downloading successful")

def takeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio = r.listen(source)

        
    try:
        print("Recognising...")
        query= r.recognize_google(audio, language='hi')
        print(f"You said: {query}\n")
        
    except Exception as e:
        return "None"

    return query.lower()

def Translate():
    speak("What do you wish to translate?")
    line = takeHindi()
    translate = Translator()
    result = translate.translate(line)
    txt = result.text
    speak(txt)

def SearchWiki(task):
    speak("Searching the web......")
    max_result= 1
    how_to =  search_wikihow(task, max_result)
    assert len(how_to) == 1
    how_to[0].print()
    speak(how_to[0].summary) 

def WolfRam(question):
    api_key = "Q683TP-ULHLJ3WKV2"
    requester = wolframalpha.Client(api_key)
    
    requested = requester.query(question)
    
    try:
        ans = next(requested.result).text
        
        return ans
    except :
        speak("No speakable data found")
        
def Calc():
    speak("Tell the expression to be calculated")
    exp = takeCommand()
    term = str(exp)
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("multiplied by", "*")
    term = term.replace("divided by", "/")
    term = term.replace("into", "*")
    term = term.replace("subtracted from", "-")
    
    Final = str(term)
    
    try:
        result = WolfRam()
        speak(f"{result}")
        
    except:
        speak("No speakable data found")

def Instagram(ch):
    
    os.system("open /Applications/Instagram.app")
    time.sleep(6)
    pyautogui.click(478, 75)
    pyautogui.press('delete')
        
    def mes():
        speak("What do you want to send?")
        while True:
            message = takeCommand()
            if "do not send anymore message" in message:
                break
            else:
                time.sleep(0.5)
                pyautogui.write(message)
                
                speak("should i send?")
                ans= takeCommand().lower()
                if ans == "sure" or ans == "go ahead" or ans =="yes":
                    pyautogui.press('enter')
                    speak("Sent sir")
                    
                elif ans == "no":
                    pyautogui.press(['command','delete'])
                 
                     
    if ch == "1":
        pyautogui.click(478, 75)
        time.sleep(3)
        pyautogui.typewrite("https://www.instagram.com/direct/t/17842806041872938/")
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.click(678 ,759)
        mes()
        
        
    if ch == "2":
        pyautogui.click(478, 75)
        time.sleep(3)
        pyautogui.typewrite("https://www.instagram.com/direct/t/106034957464761/")
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.click(678 ,759)
        mes()
       
       
    if ch == "3":
        pyautogui.click(478, 75)
        time.sleep(3)
        pyautogui.typewrite("https://www.instagram.com/direct/t/17845431953725298/")
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.click(678 ,759)
        mes()
        
    if ch == "4":
        pyautogui.click(478, 75)
        time.sleep(3)
        pyautogui.typewrite("https://www.instagram.com/direct/t/17852113994702526/")
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.click(678 ,759)
        mes()
      
def Temperature():
    speak("Temperature of which city")
    city = takeCommand()
    city = str(city)
    
    if "outside" in city:
        var = "Temperature in Aurangabad"
        
        ans = WolfRam(var)
        
        speak(f"{var} is {ans}")
        
    else:
        var = "Temperature in "+city
        ans = WolfRam(var)
        speak(f"{var} is {ans}")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio = r.listen(source,0, 8)
        

    try:
        print("Recognising...")
        query= r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        time.sleep(1)
        
    except Exception as e:
        return ""

    return query.lower()

wishMe()
webbrowser.get('macosx')

while True:
    query = takeCommand()
    
    if "search youtube" in query:
        speak("What should i search?")
        topic = takeCommand()
        webbrowser.open("https://www.youtube.com/results?search_query="+topic)
        speak("Done Sir!")
    
    elif 'the time' in query or "what time is it" in query:
        time1= datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, time is {time1}")
                
    elif 'date' in query or "today's date" in query:
        date= datetime.datetime.now().strftime("%d%B, %Y")
        speak(f"Sir, date is {date}")           
        
    elif 'what day is it' in query or 'what day is today' in query:
        day=datetime.datetime.now().strftime("%A")
        speak(f"Sir, today is {day}")
    
    elif "today's day" in query:
        day=datetime.datetime.now().strftime("%A")
        speak(f"Sir, today is {day}")
        
    elif 'quit' in query:
        speak("  Always there for you good sir")
        os.system("pkill "+"Python Launcher")
        break
                
    elif 'thank' in query:
        speak("  Always there for you good sir")
        os.system("pkill "+"Python Launcher")
        break
        
    elif 'thanks' in query:
        speak("  Always there for you good sir")
        os.system("pkill "+"Python Launcher")  
        break
    
    elif "message parth" in query or "text parth" in query:
        Instagram("1")
    
    elif "message khushi" in query or "text khushi" in query:
        Instagram("2")
        
    elif "message palak" in query or "text palak" in query:
        Instagram("3")
        
    elif "message veda" in query or "text veda" in query:
        Instagram("4")
         
    elif 'play one' in query:
        Spotify("1")
            
    elif 'play ' in query:
        song = query.replace('play ',"")
        Spotify(song)
            
    elif 'continue playing' in query:
        Spotify("2")
        
    elif "continue song" in query:
        Spotify("2")
    
    elif "uploading speed" in query:
        SpeedTest("1")
    
    elif "downloading speed" in query:
        SpeedTest("2")
        
    elif "internet speed" in query:
        SpeedTest("3")
    
    elif "send whatsapp" in query:
        WhatsApp()
    
    elif "google search about" in query:
        query = query.replace("google search about", "")
        pywhatkit.search(query)
        
        try:
            result = googleScrap.summary(query, 2)
            ("This is what i found on web "+str(result))
            
        except:
            speak("No speakable data found")
    
    elif "temperature" in query:
        Temperature()
    
    elif "screenshot" in query:
        Screenshot()
    
    elif "how to" in query:
        SearchWiki(query)
    
    elif "calculate" in query:
        Calc()
               
    elif "joke" in query:
        get = pyjokes.get_joke()
        speak(get)
      
    elif "translate" in query:
        Translate()
    
    elif "open dictionary" in query:
        Dict()
                
    elif "alarm" in query:
        speak("I should set an alarm for?")
        time = input("Enter the time ")
        
        while True:
            Time_am = datetime.datetime.now()
            now = Time_am.strftime("%H:%M:%S")
            
            if now == time:
                playsound("/Items/alarm.mp3")
                
            elif now > time:
                break
    
    elif "open" in query:
        App("1")
        
    elif "close" in query:
        App("2")
                    
    elif 'wait' in query:
        time.sleep(5)
        speak('What should i do now?')
        takeCommand()      
    
    elif "remember" in query:
        msg = query.replace("remember that", "")
        ("Sir you want me to remind you about"+msg)
        remember= open("data.txt","w")
        remember.write(msg)
        remember.close()
    
    elif "what do you remember" in query:
        remember= open("data.txt","r")
        speak("told me to remind you about"+remember.read())
    
    elif "read book" in query:
        Reader()
        
    elif "download video" in query:
        VideoDownloader()
              
    elif "open website" in query:
        speak("Website's name sir?")
        topic=takeCommand()
        webbrowser.open("https://www."+topic+"com")
        speak("Sir the website is open")
    
    
