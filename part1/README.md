### Prerequisites
[Create a Spotify developer account](https://developer.spotify.com/dashboard/) (this is easy):
* From the Spotify developer dashboard, create an app
* Find the **client key** and **secret**; have them ready for the next part

### Setup
*NOTE:* the commands may be slightly different on your machine. For example, on Windows, `\` is used in file paths instead of `/`.

* `cd part1/server`
* (optional) if you like using Python virtual environments, create one. Otherwise, skip this.
* `pip install -r requirements.txt` to install packages
* `python api.py`
    * You'll be prompted for your Spotify credentials; enter them one at a time.
* Verify that the server is up by navigating to [`http://localhost:5000`](http://localhost:5000) in your browser.
    * You should see "Hello World".

### Using it
* Open `player.html` in your browser.
* You should see a text box and a Spotify player widget with a Bruno Mars song.
* Enter anything into the text box and hit enter; you should see the widget update to Call Me Maybe by Carly Rae Jepsen.

### Exercise
* Now it's up to you to finish the code! Make an HTTP request to the Spotify API to search for whatever song the user enters into the text box.