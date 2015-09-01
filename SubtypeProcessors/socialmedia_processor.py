
from actuators import twitter_poster
from SubtypeProcessors.subtype_processor import SubTypeProcessor

class SocialMediaTypes:
  TWITTER = "twitter"

class SocialMediaProcessor(SubTypeProcessor):

  def __init__(self, *args, **kwargs):
    super(SocialMediaProcessor, self).__init__(*args, **kwargs)

  def process(self, command):
    media = super(SocialMediaProcessor, self).get_input("Which Social Media")
    if media.lower() == SocialMediaTypes.TWITTER:
      message = super(SocialMediaProcessor, self).get_input("What's your cool new post")
      while len(message) > 140:
        print("That's a bit too long (" + str(len(message)) + ")")
        message = __input("What's your cool new post?")
      twitter_poster.post(message)
