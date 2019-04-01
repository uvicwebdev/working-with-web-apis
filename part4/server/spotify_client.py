from base64 import b64encode
import requests

class SpotifyClient():
    def __init__(self, client_id, secret):
        self.client_id = client_id
        self.secret = secret
        self.api_base = "https://api.spotify.com"

    def _get_spotify_token(self):
        "Uses client ID and secret to retrieve bearer token necessary to make basic calls to Spotify Web API."
        encoded_auth_header = b64encode((self.client_id + ":" + self.secret).encode("UTF-8")).decode()
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

    def _set_token_in_auth_header(self, headers):
        """Adds 'Authorization' field to given headers object and returns it.

        Params:
            headers (dict): HTTP headers.

        Returns:
            headers (dict): HTTP headers, with the 'Authorization' header newly set.
        """
        if "Authorization" in headers:
            print("WARN: Overwriting existing 'Authorization' header: {}".format(headers.get("Authorization")))

        try:
            headers["Authorization"] = "Bearer {}".format(self._get_spotify_token())
        except Exception as e:
            print("ERROR: Failed to set header because token could not be retrieved")
            raise e
        return headers

    def get_artist_data(self, artist):
        """Retrieves summary data regarding specified artist.

        Naively resolves artist ambiguity by taking first result.

        Params:
            artist (string): e.g. "Justin Bieber"

        Returns:
            (dict): body of Spotify API's response, containing info about matching artists,
                songs, and albums.
        """
        params = dict(q=artist, type="artist")
        headers = self._set_token_in_auth_header(dict())
        resp = requests.get(
            self.api_base + "/v1/search",
            params=params,
            headers=headers,
        )

        try:
            body = resp.json()
        except Exception as e:
            print("ERROR: Could not parse response body of search request for artist: ", artist)
            raise e

        if resp.status_code != 200:
            print("ERROR: Search request for artist '{}' failed. Received HTTP code:{}".format(artist, resp.status_code))
            print(body)
            return None

        num_hits = len(body["artists"]["items"])
        if num_hits == 0:
            print("Could not find info for artist '{}'".format(artist))
            return None

        return dict(
            id=body["artists"]["items"][0]["id"],
            num_followers=body["artists"]["items"][0]["followers"]["total"],
            genres=body["artists"]["items"][0]["genres"],
        )

    def get_top_songs(self, artist_ID, country_iso_code="CA"):
        """Retrieves metadata of the specified artist's top songs on Spotify.

        Params:
            artist_ID (string).
            country_iso_code (string): e.g. "CA" for Canada.

        Returns:
            top_songs (dict): keys are the song names, val is a dict with various fields. Empty if an error occurs.
                e.g. {
                    "thank u, next": {
                        duration_ms: 207320,
                        id: "3e9HZxeyfWwjeyPAMmWSSQ",
                        popularity: 92,
                        uri: "spotify:track:3e9HZxeyfWwjeyPAMmWSSQ"
                    },
                    ...
                }
        """
        headers = self._set_token_in_auth_header(dict())
        params = dict(country=country_iso_code)
        resp = requests.get(
            self.api_base + "/v1/artists/{}/top-tracks".format(artist_ID),
            headers=headers,
            params=params,
        )
        try:
            body = resp.json()
        except Exception as e:
            print("ERROR: Could not parse response body of top songs request for artist with ID: ", artist_ID)
            return dict()

        if resp.status_code != 200:
            print("ERROR: Request for finding top songs of '{}' failed. Received HTTP code:{}".format(artist_ID, resp.status_code))
            print(body)
            return dict()

        top_songs = dict()
        for track in body["tracks"]:
            top_songs[track["name"]] = dict(
                duration_ms=int(track["duration_ms"]),
                id=track["id"],
                popularity=int(track["popularity"]),
                uri=track["uri"],
            )
        return top_songs
