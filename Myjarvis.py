import datetime
import pyautogui
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import AppOpener
import random
import pywhatkit
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def talk(com):
    engine.say("Playing " + com)
    engine.runAndWait()

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"Amit: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : Wrap this inside of a try catch block
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
         f.write(text)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n ********************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : Wrap this inside of a try catch block
    # print(response["choice"][0]["text"])
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            # com = r.recognize_google(audio)
            # song = com.replace('play','')

            # talk(song)
            # pywhatkit.playonyt(song)
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__' :
    print('Pycharm')
    speak("Hello I am Jarvis Sir..")

    while True:
        print("Listening...")
        query = takecommand()
        if 'song please'.lower() in query.lower() or 'play some song'.lower() in query.lower() or 'could you play song'.lower() in query.lower():
            speak('Sir what song should i play...')
            song = takecommand()
            # webbrowser.open(f'https://spotify.com/search/{song}')
            # pyautogui.sleep(13)
            # pyautogui.click(x=1055, y=617)
            # speak('Playing' + song)
        # elif 'play'.lower() in query.lower() or 'can you play'.lower() in query.lower() or 'please play'.lower() in query.lower():
        #     speak("OK! here you go!!")
        #     query = query.replace("play", "")
        #     query = query.replace('could you play',"")
        #     query = query.replace("please play", "")
        #     webbrowser.open(f'https://spotify.com/search/{query}')
        #     pyautogui.sleep(19)
        #     pyautogui.click(x=1055,y=617)
        #     speak("Enjoy Sir!")
    # todo : Add more Sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # if "Close it".lower() in query.lower():
        #     from AppOpener import close
        #     close("Spotify")  # Closes Spotify

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strfTime}")

        # todo : Add more Application
        apps = [["Spotify", "Spotify"], ["Visual Studio", "Visual Studio Code"], ["Chrome", "Google Chrome"], ["WhatsApp", "WhatsApp Web"], ["Edge", "Microsoft Edge"], ["Pinterest", "Pinterest"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speak(f"Opening {app[0]} sir...")
                from AppOpener import open
                open(app[1])   # Opening Application
            if f"Close {app[0]}".lower() in query.lower():
                from AppOpener import close
                close(app[1])  # Closing Application

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower()  in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr =""

        else:
            print("Chatting...")
            chat(query)



        # query = takecommand()
        # if 'song please'.lower() in query.lower() or 'play some song'.lower() in query.lower() or 'could you play song'.lower() in query.lower():
        #     speak('Sir what song should i play...')
        #     song = takecommand()
        #     webbrowser.open(f'https://spotify.com/search/{song}')
        #     pyautogui.sleep(13)
        #     pyautogui.click(x=1055, y=617)
        #     speak('Playing' + song)
        # elif 'play'.lower() in query.lower() or 'can you play'.lower() in query.lower() or 'please play'.lower() in query.lower():
        #     speak("OK! here you go!!")
        #     query = query.replace("play", "")
        #     query = query.replace('could you play',"")
        #     query = query.replace("please play", "")
        #     webbrowser.open(f'https://spotify.com/search/{query}')
        #     pyautogui.sleep(19)
        #     pyautogui.click(x=1055,y=617)
        #     speak("Enjoy Sir!")

        # say(query)