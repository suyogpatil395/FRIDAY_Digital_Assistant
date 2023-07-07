import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys


# Suyog Sanjay Patil (B.Tech in Mechanical Engineering)
# GitHub  - https://github.com/suyogpatil395
# LinkedIn - https://www.linkedin.com/in/suyog-patil-0089241b2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am FRIDAY. Please tell me how may i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

# Suyog Sanjay Patil (B.Tech in Mechanical Engineering)
# GitHub  - https://github.com/suyogpatil395
# LinkedIn - https://www.linkedin.com/in/suyog-patil-0089241b2


def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@email.com', 'Paasword')
    server.sendmail('your@mail.co', to, content)
    server.close()
     
if __name__ == "__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia") 
            print(results)
            speak(results)

        elif 'friday stands for what' in query:
            speak('Sir, FIDAY stands for Female Replacement Intelligent Digital Assistant Youth.')
            print("Sir, FIDAY stands for Female Replacement Intelligent Digital Assistant Youth")

        elif 'open my profile' in query:
            speak("Opening your github sir")
            webbrowser.open("https://github.com/suyogpatil395")

        elif 'open my linkedin' in query:
            speak("Opening your linkedin sir")
            webbrowser.open("https://www.linkedin.com/in/suyog-patil-0089241b2")

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
                            
        elif 'open my syllabus' in query:
            webbrowser.open("file:///C:/Users/patil/Downloads/TY%20Syllabus.pdf")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

        elif 'open powerpoint' in query:
            PP = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(PP)


# Suyog Sanjay Patil (B.Tech in Mechanical Engineering)
# GitHub  - https://github.com/suyogpatil395
# LinkedIn - https://www.linkedin.com/in/suyog-patil-0089241b2


        elif 'email to suyog' in query:
            try:
                speak("Sure sir!")
                speak("What shoud i say?")
                content = takeCommand()
                to = "reciever@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able ti send this email")

        elif 'thank you' in query:
            speak('Most welcome sir!')

        elif 'exit' in query:
            sys.exit()


