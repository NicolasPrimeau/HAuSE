
import pafy, sys
import speech_recognition as sr
from common.command import Command
import configurations

class Listener:

  recognizer = None
  mic = None

  def __init__(self):
    self.recognizer = sr.Recognizer()
    self.mic = sr.Microphone()

  def listen(self):
    with self.mic as source:
      self.recognizer.adjust_for_ambient_noise(source)
      audio = self.recognizer.listen(source)
      try:
        return self.recognizer.recognize(audio)
      except LookupError:
        return None

  
  def get_input(self, prompt):
    listener = Listener()
    while True:
      print(prompt+"?")
      if not configurations.ARGS['quiet']:
        received = listener.listen() 
        print(received)
        if received is None:
          print("I didn't catch that, say again?") 
          continue
      else:
        received = input()
      print("Is that correct? ")
      if not configurations.ARGS['quiet']:
        response = listener.listen()
        if response == "yes" or response == "yeah":
          break
      else:
        response = input().lower()
        if response == "yes" or response == "y":
          break
    return received
