
from pymongo import MongoClient
import configurations
# A command is an abstraction to the command present in the database
# DAO like sort of thing

class Command:

  name = None
  command_type = None
  sub_type = None
  value = None
  is_new = None

  def __init__(self, name, command_type=None, sub_type=None, value=None):
    self.name = name
    self.command_type = command_type
    self.sub_type = sub_type
    self.value = value
    self._fetchCommand()

  # Implement this later, most likely as inherited
  # This would fetch from mongo db
  def _fetchCommand(self):
    client = MongoClient()
    cursor =
        client[configurations.DB.NAME]
              ['configurations.DB.COLLECTIONS.COMMANDS']

    req = dict()
    req['name'] = self.name
    if cursor.count(req) == 0:
      # we have to take action here, command doesn't exist
      # Would have to a systems command path, having to dynamically create new
      # commands.
      pass
    elif cursor.count(req) > 1:
      # Just as evil, more than one command with certain name
      pass
    else:
      result = cursor.find(req)[0]
      self.command_type = result["command_type"]
      self.sub_type = result["sub_type"]
      self.value = result["value"]
      is_new = False

    client.close()
  
  # Update the command in the DB
  def update(self):
    pass

  # create the new command in the db
  def create(self, overwrite=False):
    pass


  def delete(self):
    pass
