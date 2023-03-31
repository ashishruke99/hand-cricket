import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<5:
        speak("It's a Good Morning according to time zone, but I think it's high time you should get sleep.")
    elif 5<hour<12:
        speak("Good Morning sir")
    elif 12<hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    speak("I am Jarvis, How can I help you")

def takeCommand():     #It takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print("User Said: ",query)

    except:
        speak("Sorry, I didn't get what you said. Can you please repeat.")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if "play music" in query:
            speak("How would you like to play music? Online or offline")
            query1=takeCommand().lower()
            if "online" in query1:
                speak("Through which website would you like to play music?")
                query2=takeCommand().lower()
                if "spotify" in query2:
                    speak("Opening spotify")
                    webbrowser.open("https://www.spotify.com/in-en/")
                elif "jio saavn" in query2:
                    speak("Opening jio saavn")
                    webbrowser.open("https://www.jiosaavn.com/")
                elif "gana" in query2:
                    speak("Opening gaana")
                    webbrowser.open("https://gaana.com/")
                else:
                    speak("Sorry, I didn't get what you said. Can you please repeat.")
                    continue

            elif "offline" in query1:
                speak("Playing offline music from your library")
                music_dir="D:\songs\hindi songs"
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("Sorry, I didn't get what you said. Can you please repeat.")
                continue

            speak("Sir, in what other way may I help you")
            continue

        elif "movie" in query:
            speak("On which platform would you like to continue?")
            query3=takeCommand().lower()
            if "hotstar" in query3:
                speak("Opening hotstar")
                webbrowser.open("https://www.hotstar.com/in")
            elif "netflix" in query3:
                speak("Opening netflix")
                webbrowser.open("https://www.netflix.com/in/")
            elif "mx player" in query3:
                speak("Opening mx player")
                webbrowser.open("https://www.mxplayer.in/movies")
            elif "amazon prime" in query3:
                speak("Opening amazon prime video")
                webbrowser.open("https://www.primevideo.com/")
            elif "j5" in query3:
                speak("Opening zee5")
                webbrowser.open("https://www.zee5.com/")
            else:
                speak("Sorry, I didn't get what you said. Can you please repeat.")
            
            speak("Sir, in what other way may I help you")
            continue

        elif "online shopping" in query:
            speak("On which platform would you like to go for shopping")
            query4=takeCommand().lower()
            if "flipkart" in query4:
                speak("Opening flipkart")
                webbrowser.open("https://www.flipkart.com/")
            elif "amazon" in query4:
                speak("Opening amazon")
                webbrowser.open("https://www.amazon.in/")
            elif "myntra" in query4:
                speak("Opening myntra")
                webbrowser.open("https://www.myntra.com/")
            elif "meesho" in query4:
                speak("Opening meesho")
                webbrowser.open("https://meesho.com/")
            elif "ajio" in query4:
                speak("Opening ajio")
                webbrowser.open("https://www.ajio.com/")
            else:
                speak("Sorry, I didn't get what you said. Can you please repeat.")
                continue

            speak("Sir, in what other way may I help you")
            continue

        elif "order food online" in query:
            speak("Through which platform would you like to order food")
            query5=takeCommand().lower()
            if "dominos" in query5:
                speak("Opening dominos website")
                webbrowser.open("https://www.dominos.co.in/")
            elif "mcdonald" in query5:
                speak("Opening mcdonalds webbsite")
                webbrowser.open("https://www.mcdonaldsindia.com/")
            elif "swiggy" in query5:
                speak("Opening swiggy website")
                webbrowser.open("https://www.swiggy.com/restaurants")
            elif "zomato" in query5:
                speak("Opening zomato website")
                webbrowser.open("https://www.zomato.com/")
            elif "burger king" in query5:
                speak("Opening burger king website")
                webbrowser.open("https://www.burgerking.in/")
            elif "pizza hut" in query5:
                speak("Opening pizza hut website")
                webbrowser.open("https://www.pizzahut.co.in/")
            else:
                speak("Sorry, I didn't get what you said. Can you please repeat.")
                continue

            speak("Sir, in what other way may I help you")
            continue

        elif "open map" in query:
            speak("Opening google maps")
            webbrowser.open("https://www.google.co.in/maps")

            speak("Sir, in what other way may I help you")
            continue

        elif "google classroom" in query:
            speak("Opening google classroom")
            webbrowser.open("https://classroom.google.com/u/0/h")

            speak("Sir, in what other way may I help you")
            continue

        elif "zoom meeting" in query:
            speak("Opening zoom meeting platform")
            webbrowser.open("https://zoom.us/")
            
            speak("Sir, in what other way may I help you")
            continue

        elif "web series" in query:
            speak("On which platform would you like to continue?")
            query6=takeCommand().lower()
            if "hotstar" in query6:
                speak("Opening hotstar")
                webbrowser.open("https://www.hotstar.com/in")
            elif "netflix" in query6:
                speak("Opening netflix")
                webbrowser.open("https://www.netflix.com/in/")
            elif "mx player" in query6:
                speak("Opening mx player")
                webbrowser.open("https://www.mxplayer.in/movies")
            elif "amazon prime" in query6:
                speak("Opening amazon prime video")
                webbrowser.open("https://www.primevideo.com/")
            elif "j5" in query6:
                speak("Opening zee5")
                webbrowser.open("https://www.zee5.com/")
            else:
                speak("Sorry, I didn't get what you said. Can you please repeat.")
            
            speak("Sir, in what other way may I help you")
            continue

        elif "wikipedia" in query:
            speak("Searching on wikipedia")
            query=query.replace("wikipedia", " ")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

            speak("Sir, in what other way may I help you")
            continue

        elif "whatsapp web" in query:
            speak("Opening whatsapp web")
            webbrowser.open("https://web.whatsapp.com/")
            speak("Sir, in what other way may I help you")
            continue

        elif "youtube" in query:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")
            speak("Sir, in what other way may I help you")
            continue
        
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, right now the time is {strTime}")
            speak("Sir, in what other way may I help you")
            continue
            
    
        elif "quit" in query:
            speak("Thank you for choosing me sir. Have a nice day ahead.")
            quit()

        else:
            speak("Sorry, I didn't get what you said. Can you please repeat.")
        
        
    

    
        
    
