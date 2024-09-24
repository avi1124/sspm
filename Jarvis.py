import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
from google.cloud import speech_v1p1beta1 as speech
import pyaudio
import subprocess
import datetime
import time


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='EN-IN')
            print(f"You Said : {query}")


        except Exception as Error:
          return "none"

        return query.lower() 
   

def TaskExe():

    Speak("Hello, I am bob.")
    Speak("How Can I Help You ?")

    def Music():
        Speak("Tell Me The Name of the Song!")
        musicName = takecommand()

        pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    # Function to send WhatsApp message
    def send_whatsapp_message(contact, message):
        try:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")

        # Schedule the message using pywhatkit
            pywhatkit.sendwhatmsg(f"+91{contact}", message, now.hour, now.minute + 1)         
            Speak(f"Message sent successfully to {contact}")
            webbrowser.open('https://web.whatsapp.com/')  # Replace with the actual path to whatsapp.exe
            Speak(f"Message scheduled and WhatsApp Desktop opened successfully.")
        except Exception as e:
            Speak(f"Failed to send message to {contact}: {str(e)}")

        if __name__ == "__main__":
    # Get contact number
            Speak("Please say the contact number (without country code):")
            contact = takecommand()


    # Get message
            Speak("Please say the message:")
            message = takecommand()


    # Send WhatsApp message
            send_whatsapp_message(contact, message)

    def screenshot():
            Speak("Ok Boss , What should I Name That File ?")
            path = takecommand()
            path1name = path + ".png"
            path1 = "D:\avi\Jarvis Voice Assistant\Screenshots" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("D:\avi\Jarvis Voice Assistant\Screenshots")
            Speak("Here Is Your Screenshot")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")

        if 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open("https://www.google.co.in/maps/@18.5246165,73.8629674,7z?entry=ttu")

        Speak("Your Command Has Been Completed Sir!")


    def CloseApps():
        Speak("Ok Sir , Wait A Second!") 

        if 'chrome' in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif 'maps' in query:
             os.system("TASKKILL /f /im chrome.exe")

        Speak("Your Command Has Been Successfully Completed !")

    def ChromeAuto():
        Speak (" Chrome Automation started ! ")
   
        command = takecommand()
        
        if 'close this tab' in command :
            keyboard.press_and_release ('ctrl + w')
   
        elif 'open new tab' in command :
            keyboard.press_and_release ('ctrl + t')
    
        elif 'open new window' in command :
            keyboard.press_and_release ('ctrl + n')
    
        elif 'history' in command :
            keyboard.press_and_release ('ctrl + h')

    def YoutubeAuto():
        Speak ("Youtube Automation Started !")
        comm = takecommand()
        
        if 'play' in comm:
            keyboard.press ('space bar')

        elif 'pause' in comm:
            keyboard.press ('space bar')

        elif 'restart' in comm:
            keyboard.press ('0')

        elif 'mute' in comm:
            keyboard.press ('m')

        elif 'skip' in comm:
            keyboard.press ('l')

        elif 'back' in comm:
            keyboard.press ('j')
        
        elif 'full screen' in comm:
            keyboard.press ('f')
                 
        elif 'film mode' in comm:
            keyboard.press ('t')

        Speak ("Done Sir")
    

    while True:
        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I am Jarvis")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("What About You")
        
        elif 'bye' in query:
            Speak("Bye Sir")
            Speak("Have A Nice Day")
            break    
        
        elif 'youtube search' in query:
            Speak("OK Sir , This is what I Found for your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia search' in query:
            Speak("OK Sir , This is what I Found for your Search!")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia search","")
            web = 'https://en.wikipedia.org/w/index.php?search=' + query
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'google search' in query:
            Speak("OK Sir , This is what I Found for your Search!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Tell Me The Name Of The Website!") 
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f'According To Wikipedia :{wiki}')

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()        

        elif 'close chrome' in query:
            CloseApps()

        elif 'close facebook' in query:
            CloseApps()

        elif 'close instagram' in query:
            CloseApps() 

        elif 'close maps' in query:
            CloseApps()    

        if 'close this tab' in query:
            keyboard.press_and_release ('ctrl + w')
   
        elif 'open new tab' in query:
            keyboard.press_and_release ('ctrl + t')
    
        elif 'open new window' in query:
            keyboard.press_and_release ('ctrl + n')
    
        elif 'history' in query:
            keyboard.press_and_release ('ctrl + h')

        elif 'chrome automation' in query:
            ChromeAuto()
    
        elif 'screenshot' in query:
            screenshot()

        if 'play' in query:
            keyboard.press ('space bar')

        elif 'pause' in query:
            keyboard.press ('space bar')

        elif 'restart' in query:
            keyboard.press ('0')

        elif 'mute' in query:
            keyboard.press ('m')

        elif 'skip' in query:
            keyboard.press ('l')

        elif 'back' in query:
            keyboard.press ('j')
        
        elif 'full screen' in query:
            keyboard.press ('f')
                 
        elif 'film mode' in query:
            keyboard.press ('t')

        elif 'youtube automation' in query:
            YoutubeAuto()

        elif 'remember that' in query :
            remeberMsg= query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+ remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query :
            remeber = open('data.txt','r')
            Speak ("You Tell Me That"+remeber.read())

        elif 'repeat my words' in query :
            Speak("Speak Sir !")
            jj = takecommand()
            Speak(f" You Said : {jj}")
   


TaskExe()
