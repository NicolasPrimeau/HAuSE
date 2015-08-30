
# A command is an abstraction to the command present in the database
# DAO like sort of thing

class Command:

  command = None
  command_type = None
  sub_type = None
  value = None
  is_new = None

  def __init__(self, command, command_type=None, sub_type=None, value=None):
    self.command = command
    self.command_type = command_type
    self.sub_type = sub_type
    self.value = value
    self._fetchCommand()

  # Implement this later, most likely as inherited
  # This would fetch from mongo db
  def _fetchCommand(self):
    return None

  
  # Update the command in the DB
  def update(self):
    pass

  # create the new command in the db
  def create(self, overwrite=False):
    pass


  def delete(self):
    pass
