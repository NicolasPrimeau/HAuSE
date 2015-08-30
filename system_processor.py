

from enum import Enum
import time

class SystemCommands(Enum):
  TIME = 1


class SystemProcessor():
  
  def __init__(self):
    pass

  def process(self, command):
    if command.value == SystemCommands.TIME:
      self._output_time()

  def _output_time(self):
    cur_time = time.gmtime()
    print(str(cur_time.tm_year) + "-" + 
          str(cur_time.tm_mon) + "-" +
          str(cur_time.tm_mday))
