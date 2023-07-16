# Import the required module for text 
# to speech conversion
from gtts import gTTS
import pydub as dub
from pydub.playback import play
import vlc
import time

# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Hello world!'
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("audio/f.mp3")
  
# Playing the converted file

file = dub.AudioSegment.from_mp3("audio/f.mp3")
play(file)