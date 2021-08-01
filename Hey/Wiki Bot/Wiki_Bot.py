import pyttsx3 as py #Text to speech library
import datetime #Date & Time Library
import speech_recognition as sr #Speech recognition Library
import wikipedia #Wiki Library
import urllib.request #URL Handling Library
import os #Operating system Library
import pyaudio #Audio Library

#------------- Initiallition ------------------
engine = py.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio): # Speaks Out
    engine.say(audio)
    engine.runAndWait()
 
def wishme(): # Greets you with repect to time
    hour =int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!, Durga Sai ")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon, Durga Sai ")
    else:
        speak("Good Evening, Durga Sai")
    speak("Im wiki bot how may i help you today")



def navigate(): #Navigation and Voice input
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me what you want to search on wikipedia ?")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Please Wait sir, Search in progress...")
        result = r.recognize_google(audio,language='en-in')
        print(f"You said:{result}\n")
        speak(result)


    except Exception as e:

        return "None"
    return result
def image(query):
    query = query.replace(" ","_".lower())
    page_image = wikipedia.page(query)
    image_down_link = page_image.images[5]

    urllib.request.urlretrieve(image_down_link , "loc.jpg")
    os.startfile("loc.jpg")

if __name__ == '__main__':
    wishme()
    query = navigate().lower()
    if "wikipedia "  in query:
        speak("searching in wiki hang on...!")
        query = query.replace("wikipedia ","")
        result =wikipedia.summary(query,sentences=2)
        image(query)
        speak("According to wiki..")
        page_image = wikipedia.page(query)
        image_down_link = page_image.images[0]
        urllib.request.urlretrieve(image_down_link , "loc.jpg")
        print(result)
        speak(result)
    elif '' in query:
        try: # Searching

            speak("searching in wiki hang on...!")
            query = query.replace("","")
            result =wikipedia.summary(query,sentences=3)
            speak("According to wiki..")
            print(result)
            image(query) #Image related to our search
            speak(result)
        except Exception as e:
            speak("Im sorry i could not found your query") #No results found or Didn't recognize
    else:
        speak("Im sorry i could not found your query") #No results found or Didn't recognize
