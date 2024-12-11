import pyttsx3
engine = pyttsx3.init()

def audd(statement):
    engine.say(statement)
    engine.runAndWait()
