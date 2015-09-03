
import pafy, sys, signal
import speech_recognition as sr
from common.command import Command
from common.exceptions import CancelCommand
import configurations

class Listener:

  recognizer = None
  mic = None

  class CommandTimeout(Exception):
    pass

  def __init__(self):
    self.recognizer = sr.Recognizer()
    self.mic = sr.Microphone()

  def listen(self, timeout=configurations.COMMAND_TIMEOUT):
    signal.signal(signal.SIGALRM, self.raise_timeout)
    with self.mic as source:
      self.recognizer.adjust_for_ambient_noise(source)
      try:
        signal.alarm(timeout)
        text = self.recognizer.recognize_google(self.recognizer.listen(source, timeout))
        signal.alarm(0)
        return text
      except LookupError:
        return None
      except sr.UnknownValueError:
        return None
      except Listener.CommandTimeout:
        return None

  
  def get_input(self, prompt, confirm=True, timeout=configurations.COMMAND_TIMEOUT):
    while True:
      print(prompt+"?")
      if not configurations.ARGS['quiet']:
        received = self.listen(timeout=timeout) 
        print(received)
        if received is None and confirm:
          print("I didn't catch that, say again?") 
          continue
      else:
        received = input()
 
      if received is not None and received.lower() == "f*** off":
        print("I'm sorry :(")
        continue
      elif received is not None and received.lower() == "cancel":
        raise CancelCommand()

      if not confirm:
        return received

      print("Is that correct? ")
      if not configurations.ARGS['quiet']:
        response = self.listen(timeout=timeout)
        if response is not None and response == "yes" or response == "yeah":
          break
      else:
        response = input().lower()
        if response == "yes" or response == "y":
          break
      if response.lower() == "cancel":
        raise CancelCommand() 
    return received

  def raise_timeout(self, *args):
    raise Listener.CommandTimeout()

