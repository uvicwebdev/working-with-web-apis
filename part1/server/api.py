from flask import Flask
from flask_cors import CORS
from base64 import b64encode
import requests


app = Flask(__name__)

# NOTE: using only for purposes of demo.
# In real-life applications, enabling CORS like this
# makes it vulnerable to attacks. Make sure you understand the
# implications when using this.
CORS(app)

SPOTIFY_CLIENT_ID, SPOTIFY_SECRET = None, None

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/spotify")
def get_spotify_token():
    if SPOTIFY_CLIENT_ID is None or SPOTIFY_SECRET is None:
        raise Exception("ERROR: need Spotify client ID and secret to proceed")
    return _get_spotify_token(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET)

def _get_spotify_token(client_id, secret):
    encoded_auth_header = b64encode((client_id + ":" + secret).encode("UTF-8")).decode()
    post_headers = dict(Authorization="Basic {}".format(encoded_auth_header))
    post_body = dict(grant_type="client_credentials")
    resp = requests.post(
        "https://accounts.spotify.com/api/token",
        data=post_body,
        headers=post_headers,
    )
    if resp.status_code != 200:
        raise Exception("ERROR: failed to refresh token. HTTP status={}".format(resp.status_code))

    try:
        body = resp.json()
    except Exception as e:
        print("ERROR: Could not parse response body to request for token.")
        raise e

    token = body.get("access_token")
    if token is None:
        raise Exception("ERROR: Token not found in resp body: ", body)
    return token


if __name__ == "__main__":
    SPOTIFY_CLIENT_ID = input("Enter Spotify Client ID: ").strip()
    SPOTIFY_SECRET = input("Enter Spotify Secret: ").strip()

    app.run()   # localhost @ port 5000