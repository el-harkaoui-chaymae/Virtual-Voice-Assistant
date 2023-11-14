import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()

# creating and initializing the engine that will speak to me
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate", 120)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_my_speech():

  global my_speech
  try:
    with sr.Microphone() as source:
        
        print("Alexa is lestenning .....")
        voice = listener.listen(source)
        my_speech = listener.recognize_google(voice)
        my_speech = my_speech.lower()
        # alexa wont exchange with me unless i call her
        if "alexa" in my_speech :
          my_speech = my_speech.replace("alexa","")
            

  except :
    pass 

  return my_speech       


# ---------- convert text to speech app

def run_alexa():
    my_speech = take_my_speech()
    print(my_speech)
    
    # play a video on youtube
    
    if "play" in my_speech :
        song = my_speech.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    
    # tell what time is it   
    
    elif "time"  in my_speech :
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("current time is" + time)
    
    # make a search in wikipedia
        
    elif "search" in my_speech :
        
        topic =my_speech.replace("search","")
        info = wikipedia.summary(topic)
        print(info)
        talk(info)
   
    # tell a joke
        
    elif "joke" in my_speech :
           
           joke = pyjokes.get_joke()
           print(joke)
           talk(joke)
    
    else : talk("sorry ! i did not understand you.")        
           

a = True

while a :        
        run_alexa()  
        
        if "thank you" in my_speech :
            a = False
            talk("good bye")      