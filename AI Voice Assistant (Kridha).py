import pyttsx3 #text to speak 
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib #used to send mail to any internet machine
engine=pyttsx3.init('sapi5')#sapi5 take voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)#voices[1] for female &voices[0] for male 
def speak(audio):
    engine.say(audio)#say function speak the audio 
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)#give time 0 to 24
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am Kridha mam. Please tell me how may I help you")
def takecommand():
    #it take microphone input from user and return string output
    r=sr.Recognizer()#it recognize the speech
    with sr.Microphone() as source:
        print("Listening...")
        #do with all parameters
        r.pause_threshold=1#when we can speak then if we stop it should not finalize it should stop 1 sec
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
        
        

if __name__ == "__main__":
    #speak("hello i am Kridha")
    wishme()
    #while True:
    if 1:
        query=takecommand().lower()
    #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)#sentences=2 because it take 2 sen from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = "   "# ADD path of your music directory and use \\ because to escape the character
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))#songs[0] for play 1st music
            
    
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            code_path="  "#add file path on which you want open code like VS code
            os.startfile(code_path)

        elif "email" in query:
        #to send many people email make a dictionary in this store key value pair key name and value email address
        #first allow less secure app
            try:
                speak("what should I say?")
                content=takecommand()
                to = ""#add email which you want to send
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry! I am not able to send this email.")





            
            
                
            

    
    
    
