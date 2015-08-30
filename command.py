
# A command is an abstraction to the command present in the database
# DAO like sort of thing

class Command:

  command = None
  command_typ = None
  value = None
  is_new = None

  def __init__(self, command, typ=None, value=None):
    self.command = command
    self.typ = typ
    self.value = value
    _fetch_values()

  # Implement this later, most likely as inherited
  # This would fetch from mongo db
  def _fetchValue(self):
    return None

  
  # Update the command in the DB
  def update(self):
    pass

  # create the new command in the db
  def create(self, overwrite=False):
    pass


  def delete(self):
    pass
