from pymongo import MongoClient
from SubtypeProcessors.subtype_processor import SubTypeProcessor
import configurations


class Song:
  url = None
  title = None
  artist = None

  def __init__(self, title, url=None, artist=None):
    self.title = title
    self.url = url
    self.artist = artist
    if url is None or artist is None:
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
    poss = list(cursor.find({"title" : title}))
    if len(poss) == 0:
      print("Song not found, need to fetch it, implement eventually")
    elif len(poss) == 1:
      self.url = poss['url']
      self.artist = poss['artist'] 
    elif len(poss) == 2:
      print("Multiple songs with same title, need to ask for artist, implement later")
    client.close()
   
