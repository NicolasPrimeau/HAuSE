from pymongo import MongoClient
import configurations
# A command is an abstraction to the command present in the database
# DAO like sort of thing

class Command:

  name = None
  command_type = None
  sub_type = None
  is_new = None

  def __init__(self, name, command_type=None, sub_type=None):
    self.name = name
    self.command_type = command_type
    self.sub_type = sub_type
    if command_type is None or sub_type is None: 
      self._fetchCommand()

  # Implement this later, most likely as inherited
  # This would fetch from mongo db
  def _fetchCommand(self):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.COMMANDS]

    commands = list(cursor.find({"name" : self.name}))

    if len(commands) == 0:
      # we have to take action here, command doesn't exist
      # Would have to a systems command path, having to dynamically create new
      # commands.
      pass
    elif len(commands) > 1:
      # Just as evil, more than one command with certain name
      pass
    else:
      result = commands[0]
      self.name = result['name']
      self.command_type = result["command_type"]
      self.sub_type = result["sub_type"]
      self.is_new = False

    client.close()
  
  # create the new command in the db
  def create(self, overwrite=False):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.COMMANDS]
    commands = list(cursor.find({"name" : self.name}))

    if len(commands) == 0:
        req = dict()
        req["name"] = self.name
        req["command_type"] = self.command_type
        req["sub_type"] = self.sub_type
       
        cursor.insert(req)
        self.is_new = True
    else:
      sys.stderr.write("Could not create " + self.name + ", it already exists!")
    client.close()

  def delete(self):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.COMMANDS]
    cursor.remove({"name" : self.name})
    client.close()
