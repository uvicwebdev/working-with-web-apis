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
        $.ajax({
            type: "GET",
            url: encodeURI("https://api.spotify.com/v1/search?q=" + songName + "&type=track"),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            headers: {
                "Authorization": "Bearer " + token,
            },
            success: function(data) {
                let hits = data['tracks']['items'];
                if (hits.length > 0) {
                    updateSpotifyWidget(hits[0]["uri"]);

                } else {
                    console.log("Found no matching songs... falling back to Carly!");
                    updateSpotifyWidget("spotify:track:38DgNqC7TQkZ3Ih5Vz6K0Q");
                }
            },
            error: function() {
                console.log("Search request to Spotify Web API failed!");
            }
        });
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