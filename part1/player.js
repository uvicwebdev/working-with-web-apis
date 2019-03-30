// Written by Juan Carlos Gallegos (+ see acknowledgements.md in repo)
// Using jQuery -- sorry not sorry

let ENTER_KEY = 13;

// When all the elements in the page are loaded and ready
// see http://api.jquery.com/ready/
$(document).ready(() => {
    // find the <input> element, where the user will enter the desired song name
    let input_box = $("#song-input");

    // when the user hits 'enter'
    input_box.keypress((event) => {
        if (event.which == ENTER_KEY) {
          event.preventDefault();
          let songName = input_box.val().trim();
          searchAndUpdate(songName);
        }
    });
});

function searchAndUpdate(songName) {
    getSpotifyBearerToken((token) => {
        // TODO: make HTTP GET request to Spotify Web API to get the Spotify URI for the given song.
        // TODO: get Spotify URI of first result in response

        console.log(`IMPLEMENT ME!`);
        console.log("Using default 'Call Me Maybe' by Carly Rae Jepsen.");
        updateSpotifyWidget("spotify:track:38DgNqC7TQkZ3Ih5Vz6K0Q");
    });
}

function updateSpotifyWidget(spotifyUri) {
    $('#spotify-widget').remove();
    $('<iframe>', {
        src: `https://embed.spotify.com/?uri=${spotifyUri}`,
        id:  'spotify-widget',
    }).appendTo('#widget-container');
}

function getSpotifyBearerToken(useToken) {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/spotify",
        success: (data) => {
            console.log(`Got Bearer Token: '${data}'`);
            useToken(data);
        },
        error: () => {
            console.log("Failed to get bearer token.");
        }
    })
}