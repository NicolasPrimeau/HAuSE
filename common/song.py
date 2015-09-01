from pymongo import MongoClient
import configurations


class Song:
  url = None
  title = None
  artist = None

  def __init__(self, title, url, artist=""):
    self.title = title
    self.url = url
    self.artist = artist

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


