
import pafy, sys
import speech_recognition as sr
from command import Command

def get_command():
  r = sr.Recognizer()
  m = sr.Microphone()

  with m as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
      return Command(r.recognize(audio))
    except LookupError:
      return None

