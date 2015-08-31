
ARGS = dict()

class DB():
  NAME = "HAuSE"
  
  class COLLECTIONS():
    COMMANDS = "COMMANDS"
    MUSIC = "MUSIC"
  
COMMAND_CACHE_SIZE = 10

BUFFERED_TEMP_FILE_PATH = "/tmp/"
BUFFERED_TEMP_FILE_PREFIX = "HAuSE-temp"
BUFFERED_TEMP_LOCATION = BUFFERED_TEMP_FILE_PATH + BUFFERED_TEMP_FILE_PREFIX
BUFFERED_TEMP_FILES = 10

def parseArgs(argv):
  global ARGS
  ARGS = dict()
  ARGS["quiet"] = False
  for arg in argv:
    if arg == "--quietMode":
      ARGS["quiet"] = True


