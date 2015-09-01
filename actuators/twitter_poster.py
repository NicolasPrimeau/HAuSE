
from twython import Twython
import configurations

twitter = Twython(configurations.TWITTER_APP_KEY, configurations.TWITTER_APP_SECRET,
                  configurations.TWITTER_OAUTH_KEY, configurations.TWITTER_OAUTH_SECRET)


def post(message):
  twitter.update_status(status=message) 
