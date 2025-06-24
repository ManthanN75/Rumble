import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import time  #working with json
from gtts import gTTS
import pygame
import os
import google_search

#pip install pocketsphinx(but removed later because it was not as efficient)
r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
r.energy_threshold = 300 #Adjust as needed (Try 300-400)
r.dynamic_energy_threshold = True  # Allow automatic adjustment

google_api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with Google API key
google_cx = "xxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Search Engine ID"
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
    
def speak(text): 
    tts = gTTS(text)
    temp_file ='temp.mp3'
    tts.save(temp_file)
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()
    
   
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove(temp_file)

    
def processCommand(c):
    command = c.lower().strip()
    if command.startswith("open"):
        website = command.replace("open", "").strip()
        if website:
            # Construct the URL (assuming .com if no extension is specified)
            url = f"https://www.{website}.com" if "." not in website else f"https://{website}"
            webbrowser.open(url)
            speak(f"Opening {website}")
        else:
            speak("Please specify a website to open.")
    
    elif "open movie themes on guitar playlist" in command:
        webbrowser.open("https://www.youtube.com/playlist?list=PL-RYb_OMw7GeqRwGUiesAvVd0uP23j3Iy") 
    elif "news" in command or "tell me the news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}", timeout=10)
        if r.status_code == 200:
            data = r.json()
        # Extract and print the headlines
        articles = data.get("articles", [])
        for article in articles:
            speak(article["title"])
    
                
        
    elif command.startswith("play"): 
       try:
            song = command.replace("play", "").strip()
            if song:
                print(f"Attempting to play song: {song}")
                if song in music_library.music:
                    speak(f"Playing {song}")
                    link = music_library.music[song]
                    webbrowser.open(link)
                else:
                    speak(f"Searching for {song} on YouTube...")
                    query = f"{song} song official audio"
                    results = google_search.search_google(query, google_api_key, google_cx)
                    if results and "items" in results:
                        youtube_url = results["items"][0].get("link")
                        if youtube_url and "youtube.com" in youtube_url:
                            speak(f"Opening {song} on YouTube")
                            webbrowser.open(youtube_url)
                        else:
                            speak(f"Sorry, I couldn't find a valid YouTube link for {song}")
                    else:
                        speak(f"Sorry, I couldn't find {song} online")
       except Exception as e:
            print(f"Error playing music: {e}")
            speak("Sorry, I had trouble playing that song")

    else:
        # Let Google Custom Search handle the request
        results = google_search.search_google(command, google_api_key, google_cx)
        if "error" in results:
            speak("Sorry, I couldn't find any results.")
        else:
            speak("Here are some results I found:")
            for item in results.get("items", []):
                speak(item.get("title"))
                speak(item.get("snippet"))



if __name__ == "__main__":
    speak("Initializing Rumble....")
    
    
    with sr.Microphone() as source:
        print("Calibrating microphone... Please wait.")
        r.adjust_for_ambient_noise(source, duration=2)
        while True:
          print("recognizing ...")
          try:
            audio = r.listen(source, timeout=7, phrase_time_limit=4)
            word = r.recognize_google(audio)
            
            if word.lower() == "rumble":
                speak("Yaa!")
                print("Rumble activated... Speak now!")
                
                time.sleep(1)  # Delay to prevent instant re-triggering
                
                try:
                    audio = r.listen(source, timeout=8, phrase_time_limit=6)
                    command = r.recognize_google(audio).lower()
                    print(f"Recognized command: '{command}'")  # Added
                    processCommand(command)
                except sr.UnknownValueError:
                    print("Error: Command was unintelligible - please repeat clearly.")  # Added
                except sr.WaitTimeoutError:
                    print("Error: No command detected - please speak within 8 seconds.")  # Added
                except sr.RequestError as e:
                    print(f"Error: Command recognition failed (internet issue?): {e}")  # Added
                time.sleep(3) # Extra delay to prevent immediate looping

          except sr.WaitTimeoutError:
                print("Error: Listening timed out - no speech detected")
          except sr.RequestError as e:
                print(f"Error: Could not request results; {e}")
          except sr.UnknownValueError:
                print("Error: Speech was unintelligible")
          except Exception as e:
                print(f"Error: {e}")