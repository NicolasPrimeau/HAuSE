
import pafy, sys, signal
import speech_recognition as sr
from common.command import Command
import configurations

class Listener:

  recognizer = None
  mic = None

  class CommandTimeout(Exception):
    pass

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

  
  def get_input(self, prompt, confirm=True, timeout=configurations.COMMAND_TIMEOUT):
    listener = Listener()
    signal.signal(signal.SIGALRM, self.raise_timeout)
    while True:
      print(prompt+"?")
      if not configurations.ARGS['quiet']:
        try:
          signal.alarm(timeout)
          received = listener.listen() 
          print(received)
        except CommandTimeout:
          received = None
        signal.alarm(0)
        if received is None:
          print("I didn't catch that, say again?") 
          continue
      else:
        received = input()
 
      if received.lower is "f*** off":
        print("I'm sorry :(")
        continue

      if not confirm:
        return received

      print("Is that correct? ")
      if not configurations.ARGS['quiet']:
        try:
          signal.alarm(timeout)
          response = listener.listen()
        except CommandTimeout:
          response = ""
        signal.alarm(0)
        if response == "yes" or response == "yeah":
          break
      else:
        response = input().lower()
        if response == "yes" or response == "y":
          break
    return received

  def raise_timeout(self, *args):
    raise Listener.CommandTimeout()

