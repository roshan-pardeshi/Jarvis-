import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import random
import cv2

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "044602566a45469ca5f5d93e0eb394c4"



def speak2(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak2("opeing google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        speak2("opeing facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c.lower():
        speak2("opeing instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open whatsapp" in c.lower():
        speak("opeing whatsapp")
        webbrowser.open("https://www.whatsapp.com")

    elif c.lower().startswith("play"):
        speak2("playing the song")
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    

    elif "addition" in c.lower():
        speak2("addition is")
        a=int(input("enter 1"))
        b=int(input("enter second"))
        print("addition is ",a+b)
        
    
    
    elif "game" in c.lower():
        computer = random.choice([1,2])
        you=int(input("enter the number under 1,2,3"))
        print(f"computer choice=={computer}")

        if(computer==you):
            print("the match will be deaw")

        else:
            print("computer is a win")

    elif "gpt" in c.lower():
        speak2("opening chatgpt")
        webbrowser.open("https://chat.openai.com/")
        
    elif "task manager" in c.lower():
        speak2("opening task manager")
        webbrowser.open("https://www.processlibrary.com/en/")
        

if __name__ == "__main__":
    speak2("Initializing sonu")

    while True:
        r = sr.Recognizer()
        print("recognizing--")

        try:
            with sr.Microphone() as source:
                print("Listening sonu...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if word.lower() == "monu":                                   # ✅ properly indented
                speak2("yes boss")
                
                with sr.Microphone() as source:
                    
                    print("sonu Active--")
                    audio= r.listen(source)
                    command= r.recognize_google(audio)

                    processCommand(command)
            
            if word.lower()=="stop":
                speak2("your task will end")
                break
    
        except Exception as e:
            speak2("your choice is not understding")
            print(f"error;not work {0}".format(e))
















   # import speech_recognition as sr
# import webbrowser
# import pyttsx3


# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://www.google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://www.facebook.com")
#     elif "open intagram" in c.lower():
#         webbrowser.open("https://www.intagram.com")
#     elif "open whatsapp" in c.lower():
#         webbrowser.open("https://www.whatsapp.com")


# if __name__ == "__main__":
#     speak("Initializing sonu")
#     while True:
#         r = sr.Recognizer()
#         print("recognizing--")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening sonu...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if (word.lower() == "sonu"):   # ✅ properly indented
#                     speak("ya")
#                     with sr.Microphone() as source:
#                         print("sonu Active--")
#                         audio= r.listen(source)
#                         command= r.recognize_google(audio)
         
#                         processCommand(command)
    
#         except Exception as e:
#             print(f"error;not work {0}".format(e))

 
