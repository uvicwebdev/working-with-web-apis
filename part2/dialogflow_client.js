// Written by Juan Carlos Gallegos (+ see acknowledgements.md in repo)
// Using jQuery -- sorry not sorry

/*
    TODO: set up global vars as needed, like in part 1.
*/

// When all the elements in the page are loaded and ready
// see http://api.jquery.com/ready/
$(document).ready(() => {
    /*
        TODO: after adding an input box to the HTML page,
        add code here for detecting user input and calling
        sendQueryAndUpdate with the input box's contents
        when the user hits 'enter'.

        This section will look almost identical to the one in part1.
    */
});

function sendQueryAndUpdate(naturalLangQuery) {
    if (naturalLangQuery === undefined) {
        // If in doubt, assume user wants to listen to "Call Me Maybe" by Carly Rae
        naturalLangQuery = "What is Carly Rae Jepsen's top song?";
        var result = "spotify:track:38DgNqC7TQkZ3Ih5Vz6K0Q";
    }

    /*
        TODO: like in part1, send an HTTP request, but this time to
        our Dialogflow agent.

        We want to use the Dialogflow agent to understand natural language
        requests, not to hold a conversation.

        We want to replace the Dialogflow agent widget with our own
        custom input box and send whatever the user enters to our Dialogflow
        agent, which will parse the query and match it to an 'intent'
        (see https://dialogflow.com/docs/intents).
    */

    console.log(`IMPLEMENT ME!`);
    console.log(`Using default answer '${result}' to default question ${naturalLangQuery}`);
    updateSpotifyWidget(result);
}

function updateSpotifyWidget(spotifyUri) {
    $('#spotify-widget').remove();
    $('<iframe>', {
        src: `https://embed.spotify.com/?uri=${spotifyUri}`,
        id:  'spotify-widget',
    }).appendTo('#widget-container');
}