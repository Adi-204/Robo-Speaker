import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by Adi")
    engine = pyttsx3.init()
    while True:
        x = input("What you want me to speak: ")
        if x == "exit":
            engine.say("Bye Bye Friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()



