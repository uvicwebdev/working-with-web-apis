### Context
**NOTE:** we don't have our Python server in this section. Instead,
we're focusing on the Dialogflow and Spotify APIs.

Simply, open `player.html` in your browser and start a conversation
with the Turing-test-passing Web Doge (*spoiler:* it's actually a Dialogflow agent).

### Exercise
Notice what happens when you ask the Dialogflow agent something like:
"What is Carly Rae Jepsen's top song?". It gives back the Spotify URI!
Notice two things:
* The Spotify player widget is not updated based on our question and the agent's answer.
    * This is what we'll implement in this section!
    * We'll replace the Dialogflow widget with our plain text box (like the one we used in part 1) and make the API call to Dialogflow ourselves so we can process the response and update the Spotify widget.
    * See comments inline for more info (in the JS script linked in the HTML page).
* Unfortunately, it gives back the same Spotify URI regardless of what artist we ask it about :(
    * We'll fix this in parts 3 and 4.
