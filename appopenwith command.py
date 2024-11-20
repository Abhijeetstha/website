import speech_recognition as sr
import subprocess
from transformers import pipeline
import pyttsx3
engine = pyttsx3.init()
# Load a transformer model for NLP (use a small model for faster results)
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to interpret command and open the respective application
def open_app(command):
    if "notepad" in command:
        subprocess.Popen("notepad.exe")
    elif "calculator" in command or "calc" in command:
        subprocess.Popen("calc.exe")
    elif "vs code" in command :
        subprocess.Popen("C:/Users/abhijeet/AppData/Local/Programs/Microsoft VS Code/Code.exe")
    elif "powerpoint" in command :
        subprocess.Popen("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")
    elif "facebook" in command:
        subprocess.Popen("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe https://www.facebook.com")
    # elif "Messanger" in command:
    #     subprocess.Popen("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe https://www.messenger.com")
    elif "Messanger" in command:
        subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe https://www.messenger.com")
    elif "Instagram" in command:
        subprocess.Popen("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe www.instagram.com")
    elif "spotify" in command:
        subprocess.Popen("C:/Users/YourUsername/AppData/Roaming/Spotify/Spotify.exe")  # Replace with actual path
    elif "chrome" in command or "browser" in command:
        subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
    elif "youtub" in command:
        subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  https://www.youtube.com/")
    elif "chat" in command:
        subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  https://chatgpt.com/c/6725786a-34ec-8000-b2db-80813a53226b")
    else:
        engine.say("Application not recognized.")
        print("Application not recognized.")
        engine.runAndWait()

# Function to listen for voice input
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Listening for your command...")
        print("Listening for your command...")
        engine.runAndWait()
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio)
        # engine.say(f"You said: {command}")
        engine.say(f"You said: {command}")
        engine.runAndWait()
        print(f"You said: {command}")
        engine.runAndWait()
        return command.lower()
    except sr.UnknownValueError:
        engine.say("Sorry, I could not understand the audio.")
        print("Sorry, I could not understand the audio.")
        engine.runAndWait()
    except sr.RequestError:
        engine.say("Sorry, there was an issue with the speech recognition service.")
        print("Sorry, there was an issue with the speech recognition service.")
        engine.runAndWait()
    return ""

# Function to process the command with NLP and open an app
def process_and_open():
    command = listen_command()
    if command:
        # Analyze the command using NLP (you can expand this with classification or intent matching)
        result = nlp(command)
        # engine.say(f"NLP result: {result}")
        print(f"NLP result: {result}")
        engine.runAndWait()
        open_app(command)

# Run the process
process_and_open()

