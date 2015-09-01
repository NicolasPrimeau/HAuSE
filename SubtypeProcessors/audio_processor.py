from actuators.audio_player import AudioPlayer
from pymongo import MongoClient
from speech.listener import Listener
import time, urllib.request, urllib.parse, re, configurations
from common.song import Song
from SubtypeProcessors.subtype_processor import SubTypeProcessor

class AudioCommands:
  PLAY = 1
  ADD = 2
  REMOVE = 3

class AudioProcessor(SubTypeProcessor):
  
  def __init__(self, *args, **kwargs):
    super(AudioProcessor, self).__init__(*args, **kwargs)

  def process(self, command):
    if command is None:
      return
    
    if command.sub_type == AudioCommands.PLAY:
      song = self._fetch_song()
      if song is None:
        print("Song not found")
        return    
      player = AudioPlayer(song)
      print("Playing song " + song.title)
      player.play()
    elif command.sub_type == AudioCommands.ADD:
      self._add_song()
    elif command.sub_type == AudioCommands.REMOVE:
      self._remove_song()


  def _fetch_song(self):
    song_name = super(AudioProcessor, self).get_input("What song")
    artist = super(AudioProcessor, self).get_input("Artist")
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.MUSIC]
    songs = list(cursor.find({"title" : song_name}))

    if len(songs) == 1:
      song = Song(songs[0]['title'], songs[0]['url'])
      return song
    elif len(songs) == 0:
      return self._add_song(song_name, artist)
    else:
      for song in songs:
        if song['artist'] == artist:
          return Song(song['title'], song['url'], songs['artist'])
      return self._add_song(song_name, artist)

  
  def _add_song(self, name=None, artist=None):
    if name is None:
      name = super(AudioProcessor, self).get_input("Song title")
    if artist is None:
      artist = super(AudioProcesor, self).get_inptu("Artist")

    query_string = urllib.parse.urlencode({"search_query" : artist + " " +name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" +
    query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
    html_content.read().decode())

    top_result = "http://www.youtube.com/watch?v=" + search_results[0]

    song = Song(name, top_result, artist=artist)
    song.create()
    print(name +" added")
    return song

  def _remove_song(self):
    name = super(AudioProcessor, self).get_input("Song title")
    sonag = Song(name)
    song.delete()
    print(name + " deleted")
