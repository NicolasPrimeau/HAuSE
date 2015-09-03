# HAuSE

Voice commands inspired by Amazon's Echo. This is an entirely non commercial project. 

--Implemented commands--

Anytime:
- cancel : Return to main execution, ready for new command

System specific:

- time : Display time (will eventually add voice feedback)
- note : Take a note
- play note : Output note

Audio Specific:

- play: Select song name and artist, consult database for youtube url. If not found, search youtube and grab first result, add to database. Then use that video's audio. Usually very precise
  When Playing: 
    - break : Pause. I can't say pause correctly and it gets heard as paws. 
    - play : continue playback of a paused audio track
    - stop : stop audio playback

- add song: Add a youtube url to database
- remove song: Remove a youtube url from database

Social Media Specific:

- post: Specify the social media (Only twitter allowed for now, which can be linked to facebook), then specify the message

