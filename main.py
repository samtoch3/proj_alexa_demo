import sys
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice", "french")
engine.setProperty("rate", 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk("Bonjour Samson")

    if 12 <= current_hour < 18:
        talk("Bonne après-midi Samson")

    if current_hour >= 18 and current_hour != 0:
        talk("Bonsoir Samson")


# set french female voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)
greet_me()
engine.say("Comment vas-tu ?")
engine.runAndWait()


def alexa_command():
    with sr.Microphone() as source:
        print("En écoute...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if "alexa" in command:
            command = command.replace("alexa", "")
            print(command)
    return command


def run_alexa():
    command = alexa_command()
    if "musique" in command:
        song = command.replace("musique", "")
        talk("Musique en cours...")
        pywhatkit.playonyt(song)
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("il est actuellement " + time)
    elif "qui est" in command:
        personne = command.replace("qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(personne, 1)
        print(info)
        talk(info)
    elif "sortir" in command:
        talk("Désolé, je suis un peu souffrante en ce moment")
    elif "es tu en couple" in command:
        talk("Pas encore, mon coeur est encore à conquerir")
    elif "blague" in command:
        jokes = ["C'est l'histoire d'un homme qui ne sait pas comment bla bla bla bla ",
                 "c'est la maitresse qui demande à toto \"Cite moi un mamifère qui n'a pas de bla bla bla\" "]
        talk(random.choice(jokes))
    elif "je t'aime" in command:
        talk("C'est gentil. Moi, je suis amoureuse de la connaissance")
    elif "et toi" in command:
        talk("Je vais bien. Merci")
    elif "desactive toi" in command:
        talk("Merci de m'avoir utilisé Samson. A une prochaine")
        sys.exit()
    else:
        talk("Desolé, je n'ai pas bien compris. Pourrais-tu repeter ?")


if __name__ == "__main__":
    while 1:
        run_alexa()
