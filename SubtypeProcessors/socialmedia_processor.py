
from actuators import twitter_poster
from SubtypeProcessors.subtype_processor import SubTypeProcessor
from speech.listener import Listener

class SocialMediaTypes:
  TWITTER = "twitter"

class SocialMediaProcessor(SubTypeProcessor):

  def __init__(self, *args, **kwargs):
    super(SocialMediaProcessor, self).__init__(*args, **kwargs)

  def process(self, command):
    listener = Listener()
    media = listener.get_input("Which Social Media")
    if media.lower() == SocialMediaTypes.TWITTER:
      message = listener.get_input("What's your cool new post", timeout=60)
      while len(message) > 140:
        print("That's a bit too long (" + str(len(message)) + ")")
        message = __input("What's your cool new post?")
      twitter_poster.post(message)
