#!/usr/bin/env python3

import pafy, sys
import speech_recognition as sr
from subprocess import Popen, PIPE

location = "/tmp/audio-temp"

command_map = {
 "play my jam" : "https://www.youtube.com/watch?v=8PLifPUIuic",
 "where is my money" : "https://www.youtube.com/watch?v=4jBDnYE1WjI",
 "what does the fox say" : "https://www.youtube.com/watch?v=jofNR_WkoCE",
}

def main():
  while True:
    command = get_command()
    print(command)
    if command is not None and command in command_map:
      song = get_song(command)
      play_song(get_song(command))

def play_song(obj):
  stream = obj.getbestaudio(preftype="m4a")
  stream.download(filepath=location+"."+stream.extension)
  play_audio(stream.extension)

def play_audio(ext):
  print(ext)
  if ext == "m4a":
    play_m4a()

def play_m4a():
  pipes = dict(stdin=PIPE, stdout=PIPE, stderr=PIPE)
  mplayer = Popen(["mplayer", location+".m4a"], **pipes)

  # to control u can use Popen.communicate
  mplayer.communicate(input=b">")
  
  sys.stdout.flush()

def play_ogg():
  pygame.init()
  pygame.mixer.music.load(location+".ogg")
  pygame.mixer.music.play()

def get_command():
  r = sr.Recognizer()
  m = sr.Microphone()

  with m as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
      return r.recognize(audio)
    except LookupError:
      return None

def get_song(title):
  return pafy.new(command_map[title])


if __name__ == "__main__":
  main()
