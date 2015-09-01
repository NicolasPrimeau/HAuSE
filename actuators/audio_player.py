
import pafy, sys
from subprocess import Popen, PIPE
import configurations

SupportedExtensions = ["m4a"]


class AudioPlayer:

  song = None

  def __init__(self, song):
    self.song = song

  def play(self, song=None):
    if song is None:
      self._play_song(self._get_song())
    else:
      self._play_song(self._get_song(song))

  def _play_song(self, obj):
    stream = obj.getbestaudio(preftype="m4a")
    stream.download(filepath=configurations.BUFFERED_TEMP_LOCATION+"."+stream.extension)
    self._play_audio(stream.extension)

  def _play_audio(self, ext):
    if ext not in SupportedExtensions:
      sys.err.write("Extension " + ext + " not in supported extensions\n")

    if ext == "m4a":
      self._play_m4a()

  def _play_m4a(self):
    pipes = dict(stdin=PIPE, stdout=PIPE, stderr=PIPE)
    mplayer = Popen(["mplayer", configurations.BUFFERED_TEMP_LOCATION+".m4a"], **pipes)

    # to control u can use Popen.communicate
    mplayer.communicate(input=b">")
                        
    sys.stdout.flush()

  def _get_song(self, song=None):
    if song is None:
      return pafy.new(self.song.url)
    else:
      return pafy.new(song.url)


