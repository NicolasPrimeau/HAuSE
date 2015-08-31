#!/usr/bin/env python3

from common.command_types import CommandTypes
from SubtypeProcessors.audio_processor import AudioCommands
from pymongo import MongoClient
import configurations, sys

client = MongoClient()
cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.MUSIC]
song = dict()
song['title'] = sys.argv[1]
song['url'] = sys.argv[2]
if len(sys.argv) == 4:
  song['artist'] = sys.argv[3]
cursor.insert(song)
client.close()

