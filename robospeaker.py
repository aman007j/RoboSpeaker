import win32com.client as wincom
import gtts

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("Enter what you want to speak: ")

    if text == "q":
        speak.Speak("Thanks for using robo speaker")
        break

    sound = gtts.gTTS(text, lang="en")
    sound.save("test.mp3")

    speak.Speak(text)
