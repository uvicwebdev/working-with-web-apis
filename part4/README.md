<img src="../img/part 2 solved.png" height=430px width=800px/>

### Overview
In this section, we start with the web client from part3 (adapted from part2) and a Python server like the one from part1, but with a new endpoint. The new endpoint uses Flask Assisant to serve a webhook request made by the Dialogflow agent to get a greeting. The main goal of this section is to create a similar endpoint for answering a different request from the same Dialogflow agent: to get an artist's top song.

### Prerequisites
* Install [ngrok](ngrok.io) -- this is quick!
    * We'll use run this locally to make our Python server publicly accessible, so that our Dialogflow agent can talk to it.

If you haven't already:
* [Create a Spotify developer account](https://developer.spotify.com/dashboard/):
    * From the Spotify developer dashboard, create an app
    * Find the **client key** and **secret**; have them ready for the next part
* Creat your own Dialogflow agent; see part3.

### Setup
*NOTE:* the commands may be slightly different on your machine. For example, on Windows, `\` is used in file paths instead of `/`.

#### Server
* `cd part4/server`
* (optional) if you like using Python virtual environments, create one. Otherwise, skip this.
* `pip install -r requirements.txt` to install packages
* `python api.py`
    * You'll be prompted for your Spotify credentials; enter them one at a time.
* Now we'll quickly set up ngrok to make our Python server publicly accessible: in a separate terminal tab/window, run `./ngrok http 5000` from the directory where you installed ngrok
    * We specify port `5000` so that it can relay messages to our Python server, which is running on that port (by default)
    * Make note of the HTTPS URL that gets printed (e.g. `https://70208a46.ngrok.io`); you'll need it for the next step

#### Dialogflow Agent
* First, enable fulfillment for both `Welcome` and `Get Top Song` intents in your Dialogflow agent.
* Then, [configure](https://dialogflow.com/docs/fulfillment/configure) your Dialogflow agent to call your Python server to determine how to answer a user request.
    * You'll need the ngrok URL from the previous section (e.g. `https://70208a46.ngrok.io`) -- that's the address your agent will use to talk to your Python server.

#### Web Client
* Copy over the client code you modified in part3 from part2.
* If you don't have one already, add a `console.log` statement that dumps the data resulting from the call to your Dialogflow agent.

### Using it
* Open `index.html` in your browser.
* Like in part 1, you should see a text box and a Spotify player widget with a Bruno Mars song.
* Open the console in the browser Developer Tools.
* If you enter a greeting (e.g. "Hi"), the response should be match what the `greet` function in our Python server returns
    * If it doesn't then, you may have missed a step in setting up the server (e.g. starting the server, starting ngrok on the same port) and/or your agent (e.g. enabling fulfillment for the `Welcome` intent, giving the correct `ngrok` URL)
* You'll notice that if you request an artist's top song (e.g. "Get top song by Carly Rae Jepsen"), it always returns "Call Me Maybe"; that's because the exercise is to implement this part!

### Exercise
* Now it's up to you to finish the code! Create an endpoint in our Python server to fulfill the `Get Top Song` intent
    * Use the provided Spotify Client to get the desired info.
    * See the comments in `server/api.py` for more details
* Look at [Flask Assistant docs](https://flask-assistant.readthedocs.io/en/latest/) and the `greet` endpoint for an example