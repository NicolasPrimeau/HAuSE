from pymongo import MongoClient
from SubtypeProcessors.subtype_processor import SubTypeProcessor
import configurations
from speech.listener import Listener

class Song:
  url = None
  title = None
  artist = None

  def __init__(self, title, url=None, artist=""):
    self.title = title.lower()
    self.url = url
    self.artist = artist.lower()
    if url is None or artist == "":
      self._get_information()

  def create(self):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.MUSIC]

    req = dict()
    req["title"] = self.title
    req["artist"] = self.artist
    req["url"] = self.url
    songs = list(cursor.find(req)) 
    if len(songs) == 0:
      cursor.insert(req) 
     
    self.is_new = True
    client.close()

  def delete(self):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.MUSIC]
    cursor.remove({"title" : self.title, "url" : self.url})
    client.close()

  def _get_information(self):
    client = MongoClient()
    cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.MUSIC]
    poss = list(cursor.find({"title" : self.title}))
    if len(poss) == 0:
      print("Song not found, need to fetch it, implement eventually")
    elif len(poss) == 1:
      self.url = poss[0]['url']
      self.artist = poss[0]['artist'].lower()
    elif len(poss) == 2:
      listener = Listener()
      self.artist = listener.get_input("What artist?").lower()
    client.close()
   
