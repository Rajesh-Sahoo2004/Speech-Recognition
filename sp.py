import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import sys
import time
import webbrowser


engine = pyttsx3.init()

# Set voice (optional: 0=male, 1=female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print(" Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(" You said:", command)
            return command
    except sr.WaitTimeoutError:
        print("Timeout: No speech detected.")
        return ""
    except sr.UnknownValueError:
        print(" Could not understand.")
        return ""
    except sr.RequestError:
        print(" Network error.")
        return ""

# Process the command
def run_assistant():
    command = take_command()
    print(" Debug:", command)

    if "open notepad" in command:
        talk("Opening Notepad")
        os.system("notepad.exe")

    elif "open calculator" in command:
        talk("Opening Calculator")
        os.system("calc.exe")
    
    elif "open youtube" in command or "launch youtube" in command or "start youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")


    elif "open paint" in command:
        talk("Opening Paint")
        os.system("mspaint.exe")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {current_time}")

    elif "search" in command:
        search_query = command.replace("search", "")
        talk(f"Searching for {search_query}")
        pywhatkit.search(search_query)

    elif "exit" in command or "bye" in command:
        talk("Goodbye Rajesh! Have a great day.")
        sys.exit()

    elif command != "":
        talk("Sorry, I didn't understand that.")


talk("Jay shri Ram")
while True:
    run_assistant()
    time.sleep(1) 
 