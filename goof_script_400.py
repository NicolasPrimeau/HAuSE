#!/usr/bin/env python3

import pafy, sys, configurations
from subprocess import Popen, PIPE
from speech.listener import Listener
from common.command_types import CommandTypes
from common.command import Command
from SubtypeProcessors.system_processor import SystemProcessor, SystemCommands
from SubtypeProcessors.audio_processor import AudioProcessor
from SubtypeProcessors.socialmedia_processor import SocialMediaProcessor


def main():
  configurations.parseArgs(sys.argv)
  listener = Listener()
  while True:
    print("What's up?")
    if not configurations.ARGS["quiet"]:
      command = Command(listener.listen())
    else:
      command = Command(input())

    if command is not None and command.name is not None:
      print("Command " + command.name)
      if command.command_type == CommandTypes.AUDIO:
        # Music procssor here
        audioProcessor = AudioProcessor()
        audioProcessor.process(command)
      elif command.command_type == CommandTypes.SYSTEM:
        #System processor here
        systemProcessor = SystemProcessor()
        systemProcessor.process(command)
      elif command.command_type == CommandTypes.SOCIAL:
        mediaProcessor = SocialMediaProcessor()
        mediaProcessor.process(command)
      elif command.name.lower() == "exit":
        print("Exiting")
        sys.exit(0)
      else:
        print("Command not recognized.")
    else:
      print("I'm sorry, I didn't catch that")
if __name__ == "__main__":
  main()
