import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# setup packages for speech recognition
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#if want the voice change then can vhage voice as a male or female
engine.setProperty('voice',100)
engine.setProperty('voice', voices[1].id)

# giving response
def respone(text):
    engine.say(text)
    engine.runAndWait()
#=========================================================================
#Check Time for greeting
def TimeGreeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        respone("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        respone("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        respone("Hello,Good Evening")
        print("Hello,Good Evening")

#=========================================================================
#command getting and recognizing
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-sl')
            print(f"Kid Said:{statement}\n")

        except Exception as e:
            respone("I Didn't get that, please tell me again")
            return "None"
        return statement

TimeGreeting()

#=========================================================================
# the main method loop
if __name__=='__main__':


    while True:
        print("Hi there... how can I help you?")
        respone("Hi there... how can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            respone('your Kid-Dose_VoiceAssistant is shutting down,Good bye')
            print('your Kid-Dose_VoiceAssistant is shutting down,Good bye')
            break


#loading wikipedia data and searching
        if 'wikipedia' in statement:
            respone('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            respone("According to Wikipedia")
            print(results)
            respone(results)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            respone("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                respone(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                      "\n humidity in percentage is " +
                        str(current_humidiy) +
                      "\n description  " +
                        str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                respone(" City Not Found ")


# getting system time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respone(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            respone('I am  your Kid Dose Voice Assistant.')

        elif 'what is your name' in statement:
            respone('My Name is Kid Dose voice Assistant. what is your name?')
            username = takeCommand()
            respone('nice name') or respone('beautiful')

        elif "who is your owner" in statement:
            respone("I was built by Kid Dose team")
            print("I was built by Kid Dose team")

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","kiddose.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
#load datasets using wolframalpha api datasets and use their algorithms
        elif 'ask' in statement:
            respone('I can Answer All English related and mathematics related questions. what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            respone(answer)

        elif "log off" in statement or "sign out" in statement:
            respone("Ok , your phone will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

#=========================================================================












