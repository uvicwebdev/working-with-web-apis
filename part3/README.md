The only objective of this part is to create your own Dialogflow agent
and adapt your code in part 2 to work with your own agent instead of the provided one.

This is tedious compared to writing code, but it's a pre-requisite for code we'll write in part 3.
Also, it's a good example of the hoop-jumping we often have to do to work with APIs.

Stuff for you to do:
- [ ] For starters, [create your own agent](https://dialogflow.com/docs/getting-started)
- [ ] In your new agent, create a `Get Top Song` [intent](https://dialogflow.com/docs/intents) with a [parameter](https://dialogflow.com/docs/intents/actions-parameters) of entity type `@sys.music-artist` that handles phrases like:
    - [ ] `"Get top song by Carly Rae Jepsen"`
    - [ ] `"Get Carly Rae Jepsen's top song"`
    - [ ] `"What is Carly Rae Jepsen's top song?"`
- [ ] Update your Dialogflow client in part 2 to call your agent instead of the provided one.
    - [ ] You'll need an API key for your agent, which you can get by following the [authentication guide](https://dialogflow.com/docs/reference/v2-auth-setup) for your agent.
    - [ ] As mentioned in the authentication guide, you'll need to [install the Google Cloud SDK](https://cloud.google.com/sdk/docs/)
