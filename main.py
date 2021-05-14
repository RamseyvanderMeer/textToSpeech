import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+50)
    engine.say("Hello World! I am doing well . . . umu. . . . . .  . umu")
    engine.runAndWait()
    engine.stop()