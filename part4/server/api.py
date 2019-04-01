from flask import Flask
from flask_assistant import Assistant, tell
from flask_cors import CORS
from spotify_client import SpotifyClient
import logging


app = Flask(__name__)
assist = Assistant(app, project_id='humanperson-73326')
SPOTIFY_CLIENT = None

logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

# NOTE: using only for purposes of demo.
# In real-life applications, enabling CORS like this
# makes it vulnerable to attacks. Make sure you understand the
# implications when using this.
CORS(app)

# Here is where we accept requests from our Dialogflow agent
# to handle the 'Welcome' intent.
@assist.action('Welcome')
def greet():
    return tell("Hiya! Thanks for hitting my webhook :-)")

# TODO: create a new endpoint for retrieving an artist's top song
#   - [ ] Specify what intent you want to serve (like 'Welcome', like above)
#   - [ ] Accept the artist's name as an argument
#       - The name should match the Parameter name in your Dialogflow agent
#   - [ ] Use the SPOTIFY_CLIENT to find the given artist's top song
#       - You'll need to find the artist's ID first
#   - [ ] Reply with the Spotify URI
#
#   For help, look at the example above and at the Flask Assistant docs.


if __name__ == "__main__":
    spotify_client_id = input("Enter Spotify Client ID: ").strip()
    spotify_secret = input("Enter Spotify Secret: ").strip()
    SPOTIFY_CLIENT = SpotifyClient(spotify_client_id, spotify_secret)

    app.run()   # localhost @ port 5000