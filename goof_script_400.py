#!/usr/bin/env python3

import pafy, sys
from subprocess import Popen, PIPE
from command_processor import CommandProcessor
from common.command_types import CommandTypes
from common.command import Command
from SubtypeProcessors.system_processor import SystemProcessor, SystemCommands
from SubtypeProcessors.audio_processor import AudioProcessor

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
    if command is not None:
      if command.command_type == CommandTypes.MUSIC:
        # Music procssor here
        audioProcessor = AudioProcessor()
        audioProcessor.process(command)
      elif command.command_type == CommandTypes.SYSTEM:
        #System processor here
        systemProcessor = SystemProcessor()
        systemProcessor.process(command)

if __name__ == "__main__":
  main()
