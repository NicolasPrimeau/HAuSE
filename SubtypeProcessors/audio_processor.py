
from actuators.audio_player import AudioPlayer

class AudioCommands:
  PLAY = 1

class AudioProcessor:
  
  def __init__(self):
    pass

  def process(self, command):
    if command is None:
      return
    
    if command.sub_type == AudioCommands.PLAY:
      player = AudioPlayer(command)
      player.play()


