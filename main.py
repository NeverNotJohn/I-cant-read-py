import pyttsx3


engine = pyttsx3.init() # object creation

""" RATE"""

rate = 200

engine.setProperty('rate', rate)     # setting up new voice rate
print(f"Voice Rate: {rate}")

"""VOLUME"""

volume = 1.0

engine.setProperty('volume', volume)    # setting up volume level  between 0 and 1
print(f"Volume: {volume}")

"""VOICE"""

voiceID = 1

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[voiceID].id)   #changing index, changes voices. 1 for female





def main():
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World', 'audio/test.mp3')

if __file__ == "__main__":
    main()
