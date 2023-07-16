import pyttsx3

def createMP3(string, rate, volume, voiceID):

    engine = pyttsx3.init() # object creation

    """ RATE"""

    engine.setProperty('rate', rate)     # setting up new voice rate
    print(f"Voice Rate: {rate}") #DEBUG

    """VOLUME"""

    engine.setProperty('volume', volume)    # setting up volume level  between 0 and 1
    print(f"Volume: {volume}") #DEBUG

    """VOICE"""

    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[voiceID].id)   #changing index, changes voices. 1 for female



    """ Main: """

    engine.say("Hello World!") # DEBUG
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(string, 'audio/test.mp3')


