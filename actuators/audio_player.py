
import pafy, sys
from subprocess import Popen, PIPE

SupportedExtensions = ["m4a"]


class AudioPlayer:

  command = None

  def __init__(self, command):
    self.command = command

  def play():
    self._play_song(self._get_song())

  def _play_song(self, obj):
    stream = obj.getbestaudio(preftype="m4a")
    stream.download(filepath=location+"."+stream.extension)
    self._play_audio(stream.extension)

  def _play_audio(self, ext):
    if ext not in SupportedExtensions:
      sys.err.write("Extension " + ext + " not in supported extensions\n")

    if ext == "m4a":
      self._play_m4a()

  def _play_m4a(self):
    pipes = dict(stdin=PIPE, stdout=PIPE, stderr=PIPE)
    mplayer = Popen(["mplayer", location+".m4a"], **pipes)

    # to control u can use Popen.communicate
    mplayer.communicate(input=b">")
                        
    sys.stdout.flush()

  def _get_song(self):
    return pafy.new(self.command.value)


