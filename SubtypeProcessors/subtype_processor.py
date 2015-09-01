
from speech.listener import Listener
import configurations

class SubTypeProcessor:
  def get_input(self, prompt):
    listener = Listener()
    while True:
      print(prompt+"?")
      if not configurations.ARGS['quiet']:
        received = listener.listen() 
        print(received)
        if received is None:
          print("I didn't catch that, say again?") 
          continue
      else:
        received = input()
      print("Is that correct? ")
      if not configurations.ARGS['quiet']:
        response = listener.listen()
        if response == "yes" or response == "yeah":
          break
      else:
        response = input().lower()
        if response == "yes" or response == "y":
          break
    return received
