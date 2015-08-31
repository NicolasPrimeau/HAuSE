#!/usr/bin/env python3

import pafy, sys
from subprocess import Popen, PIPE
from listener import Listener
from common.command_types import CommandTypes
from common.command import Command
from SubtypeProcessors.system_processor import SystemProcessor, SystemCommands
from SubtypeProcessors.audio_processor import AudioProcessor

def parseArgs():
  args = dict()
  args["quiet"] = False
  for arg in sys.argv:
    if arg == "--quietMode":
      args["quiet"] = True

  return args


def main():
  args = parseArgs()
  listener = Listener()
  while True:
    if not args["quiet"]:
      command = Command(listener.listen())
    else:
      command = Command(input("What's up? "))
    
    if command is not None:
      if command.command_type == CommandTypes.MUSIC:
        # Music procssor here
        audioProcessor = AudioProcessor()
        audioProcessor.process(command)
      elif command.command_type == CommandTypes.SYSTEM:
        #System processor here
        systemProcessor = SystemProcessor(args["quiet"])
        systemProcessor.process(command)
      elif command.name.lower() == "exit":
        print("Exiting")
        sys.exit(0)
      else:
        print("Command not recognized.")
if __name__ == "__main__":
  main()
