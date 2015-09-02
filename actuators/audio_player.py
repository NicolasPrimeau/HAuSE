
import pafy, sys
from subprocess import Popen, TimeoutExpired, PIPE
import configurations
from speech.listener import Listener

SupportedExtensions = ["m4a"]


class AudioPlayer:

  song = None

  def __init__(self, song):
    self.song = song

  def play(self, song=None):
    if song is None:
      print("Playing " + self.song.title + " by " + self.song.artist)
      self._play_song(self._get_song())
    else:
      print("Playing " + song.title + " by " + self.song.artist)
      self._play_song(self._get_song(song))

  def _play_song(self, obj):
    stream = obj.getbestaudio()
    stream.download(filepath=configurations.BUFFERED_TEMP_LOCATION+"."+stream.extension)
    self._play_audio(stream.extension)

  def _play_audio(self, ext):
    if ext not in SupportedExtensions:
      sys.err.write("Extension " + ext + " not in supported extensions\n")

    if ext == "m4a":
      self._play_m4a()

  def _play_m4a(self):
    mplayer = Popen(["mplayer", configurations.BUFFERED_TEMP_LOCATION+".m4a"], stdin=PIPE, stderr=PIPE, stdout=PIPE)

    listener = Listener()
    paused = False
    stdin = mplayer.stdin
    while True:
      try:
        mplayer.wait(timeout=0.1)
        break
      except TimeoutExpired:  
        if not paused:
          command = listener.get_input("Pause/Stop")
        else:
          command = listener.get_input("Play/Stop")

        command = command.lower()
        if command is not None:
          if command == "pause" and not paused or command == "play" and paused:
            stdin.write(b" ")
            stdin.flush()
            paused = not paused
          elif command == "stop":
            mplayer.terminate()
            break
          
                    
    sys.stdout.flush()

  def _get_song(self, song=None):
    if song is None:
      return pafy.new(self.song.url)
    else:
      return pafy.new(song.url)


