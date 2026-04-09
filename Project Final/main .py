import subprocess
from logging import exception
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import random
import threading
from plyer import notification
import pyautogui



x=datetime.datetime.now()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def content():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=7)
                user_input = r.recognize_google(audio, language="en-in")
                print(f"You said: {user_input}")
                return user_input
            except sr.WaitTimeoutError:
                print("Listening timed out, waiting again...")
                speak("I'm listening...")
            except sr.UnknownValueError:
                print("Could not understand audio.")
                speak("Sorry, I didn’t catch that. Could you say it again?")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                speak("Sorry, I'm having trouble connecting to the service.")
            except Exception as e:
                print("An error occurred:", e)
                speak("Sorry, something went wrong.")


def main_process():
    while True:
        request=content().lower()
        print(request) # hal purtu
      
        if "andrew" in request:
            if "favourite" in request:
                if "play"and"music"or"song" in request:
                    webbrowser.open("https://www.youtube.com/watch?v=pNx1eaUqV1A")
                elif "car" in request:
                    speak("Sir your favourite car is mercedes benz clk gtr")

            elif "date" in request:
                speak("Sir todays date is "+x.strftime("%d")+x.strftime("%B")+x.strftime("%Y"))
            elif "which day" in request:
                speak("Todays day is "+x.strftime("%A"))
            elif "time" in request:
                speak(x.strftime("%I")+x.strftime("%M")+x.strftime("%p"))

            elif "open" in request:
                if "whatsapp"in request:
                    webbrowser.open("https://web.whatsapp.com")
                elif "youtube" in request:
                    webbrowser.open("https://www.youtube.com")
                elif "instagram" in request:
                    webbrowser.open("https://www.instagram.com")
                elif "google" in request:
                    webbrowser.open("https://www.google.com/")
                elif "email" in request:
                    webbrowser.open("https://workspace.google.com/intl/en-US/gmail/")
                elif "application" in request:
                    request = request.replace("andrew", "")
                    request = request.replace("open","")
                    request = request.replace("application", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(request)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

            elif "search "and "on web" in request:
                request=request.replace("andrew","")
                request=request.replace("search","")
                request=request.replace("on web","")
                request=request.replace(" ","")
                webbrowser.open("https://www.google.com/search?q="+request)

            elif "search" and "song" in request:
                request = request.replace("andrew", "")
                request = request.replace("search", "")
                request=request.replace("song" ,"")
                request=request.replace(" ","")
                webbrowser.open("https://music.youtube.com/search?q="+request)

            elif "search" and "on wikipedia" in request:
                request = request.replace("andrew", "")
                request = request.replace("search", "")
                request = request.replace("on wikipedia", "")
                request = request.replace(" ", "")
                request=wikipedia.summary(request)
                speak(request)

            if "task" in request:
                if "add" in request:
                    request = request.replace("andrew", "")
                    request = request.replace("add a task", "")
                    request=request.strip()
                    if request!="":
                        with open("todo.txt","a") as file:
                            file.write(request+"\n")
                            speak("adding task successfully")
                elif "read" in request:
                    with open("todo.txt", "r") as file:
                            speak(file.read())
                elif "display" in request:
                    with open("todo.txt", "r") as file:
                        task=file.read()
                        if task!="":
                            notification.notify(
                                title="Today's tasks",
                                message=task
                            )
                        else:
                            notification.notify(
                                title="Today's tasks",
                                message="No tasks for today"
                            )

            elif "take screenshot" in request:
                    request=request.replace("andrew take screenshot as","")
                    im1 = pyautogui.screenshot()
                    im1.save(request+".png")

            elif "write" in request:
                request=request.replace("andrew","")
                pyautogui.write(request)

            elif "joke" in request:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "weather" in request:
                request = request.replace("andrew", "")
                request = request.replace("weather", "")
                request = request.replace("in", "")
                city = request
                if city:
                    url = f"https://www.google.com/search?q=weather+in+{city}"
                    webbrowser.open(url)
                    speak(f"Showing weather for {city}")

            elif "flip a coin" in request:
                speak(random.choice(["Heads", "Tails"]))

            elif "roll a dice" in request or "roll a die" in request:
                speak(f"You got a {random.randint(1, 6)}")

            elif "location" in request:
                request = request.replace("andrew", "")
                request = request.replace("location", "")
                request = request.replace("of", "")
                location = request
                if location:
                    url = f"https://www.google.com/maps/place/{location.replace(' ', '+')}"
                    webbrowser.open(url)
                    speak(f"Here is the location of {location}.")
                else:
                    speak("Sorry, I couldn't catch the location name.")
                    
            elif "run gesture control" in request or "run gesture code" in request:
                t = threading.Thread(target=run_gesture_script)
                t.start()
                speak("Running gesture control in the background.")


            elif "thank you" in request:
                speak("Its my pleasure i am here for helping you ")
            elif"how are you" in request:
                speak("im fine sir ")
            elif "hello" or "hi" in request:
                speak("hello sir i am here for helping you")
            elif "what is your name" in request:
                speak("sir my name is andrew what can i help you")
            elif "good" in request:
                speak("I am appriciate you sir")



            elif"andrew" in request:
                speak("Yes sir! What can I help you")
                


def run_gesture_script():
    try:
        subprocess.run(["python", "C:\Users\hansr\OneDrive\Desktop\Project Final\Gesture_Controller.py"])
    except Exception as e:
        speak("Failed to run gesture control script.")
        print(f"Gesture Script Error: {e}")


main_process()