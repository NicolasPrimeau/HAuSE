#!/usr/bin/env python3

from common.command_types import CommandTypes
from SubtypeProcessors.audio_processor import AudioCommands
from pymongo import MongoClient
import configurations, sys

client = MongoClient()
cursor = client[configurations.DB.NAME][configurations.DB.COLLECTIONS.COMMANDS]
song = dict()
song['name'] = sys.argv[1]
song['command_type'] = int(sys.argv[2])
song['sub_type'] = int(sys.argv[3])
cursor.insert(song)
client.close()

