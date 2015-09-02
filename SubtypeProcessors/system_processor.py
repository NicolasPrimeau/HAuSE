

from common.command import Command
from common.command_types import CommandTypes
from SubtypeProcessors.subtype_processor import SubTypeProcessor
from pymongo import MongoClient
import configurations
from speech.listener import Listener

class SystemCommands:
  TIME = 1
  NOTE = 2
  PLAY_NOTE = 3

class SystemProcessor(SubTypeProcessor):
 
  def __init__(self, *args, **kwargs):
    super(SubTypeProcessor, self).__init__(*args, **kwargs)

  def process(self, command):
    if command.sub_type == SystemCommands.TIME:
      self._output_time()
    elif command.sub_type == SystemCommands.NOTE:
      self._take_note() 
    elif command.sub_type == SystemCommands.PLAY_NOTE:
      self._play_note()

  def _output_time(self):
    cur_time = time.gmtime()
    print(str(cur_time.tm_year) + "-" + 
          str(cur_time.tm_mon) + "-" +
          str(cur_time.tm_mday))

  def _take_note(self):
    listener = Listener()
    title = listener.get_input("What's the title of this note")
    note = listener.get_input("What's your note")
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.NOTES]
    note = dict()
    note['title'] = title
    note['note'] = note
    if len(list(cursor.find({"title" : note['title']}))) == 0:
      cursor.insert(note)
    else:
      print("Note with that name already exists")
    client.close()

  def _play_note(self):
    listener = Listener()
    title = listener.get_input("What the title")
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.NOTES]
    notes = list(cursor.find({"title" : title}))
    if len(notes) == 0:
      print("Note not found")
    else:
      print(note['title'])
      print(note['note'])
    client.close()


