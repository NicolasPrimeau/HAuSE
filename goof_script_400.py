#!/usr/bin/env python3

import pafy, sys
from subprocess import Popen, PIPE
from command_processor import CommandProcessor
from command_types import CommandTypes
from command import Command
from system_processor import SystemProcessor, SystemCommands

location = "/tmp/audio-temp"

command_map = {
 "play my jam" : "https://www.youtube.com/watch?v=8PLifPUIuic",
 "where is my money" : "https://www.youtube.com/watch?v=4jBDnYE1WjI",
 "what does the fox say" : "https://www.youtube.com/watch?v=jofNR_WkoCE",
}

def main():
  processor = CommandProcessor()
  while True:
    command = processor.get_command()
    #command = Command("time", CommandTypes.SYSTEM, SystemCommands.TIME)
    print(command)
    if command.command_type == CommandTypes.MUSIC:
      # Music procssor here
      song = get_song(command)
      play_song(get_song(command))
    elif command.command_type == CommandTypes.SYSTEM:
      #System processor here
      systemProcessor = SystemProcessor()
      systemProcessor.process(command)
    break

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

def get_song(command):
  return pafy.new(command.value)


if __name__ == "__main__":
  main()
