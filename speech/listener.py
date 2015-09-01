
import pafy, sys
import speech_recognition as sr
from common.command import Command

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

