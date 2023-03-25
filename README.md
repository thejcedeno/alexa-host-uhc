# alexa-host-uhc
Meme project from twitch.tv/realjcedeno. The idea is to create an API that allows users to deploy game servers with a simple request, then use that API with a smart assistant, ergo the name: `Alexa, please host a UHC`.

## The tech stack
Keeping things lean here, python for everything, and we use terraform from within python to deploy the infraestructure. Once a database is required, pymongo might be a good solution. So in summary:

1. Python w/ Flask for REST Api.
2. Terraform for Infraescture as Code scripts.
3. MongoDB as a NoSQL storage solution
4. (?) A web client to interact with the API, likely to be Typescript+Svelte+TailwindCSS.

## The End Goal
The end goal here is to have an API that takes a request to host a UHC and automatically makes the determination of what infraestructure is needed and where to deploy it. Ideally the instructions provided by the user are the following in JSON:

```json
{
    "request": {
        "game_template": "global-uhc-to2-vanilla",
        "region": "us-east"
    }
}
```

And the logic interprets everything that's needed to be pass down to the current API to get it deployed. The idea is then to use that simple abstraction from a serverless application that hooks to personal assistants -- Siri, Alexa, and Google -- and allows you to ask them with simple  prompts to deploy your infraestructured at a schedulded time.

### The prompts:
Initial ideas. We are probably going to need a GPT-like language model

English:
- "Alexa, host a UHC game in 45 minutes" -- creates a private UHC game and notifies your "friend group" of the match.
- "Hey siri, post a uhc game in 1h." -- creates public match and tweets it for you.
- "Ok Google, schedule a Teams of 2 UHC for next friday at 5pm."

Spanish:
- "Alexa, hosteate un UHC bien cabron." -- creates a public, absorptionless, timebomb, FFA UHC and tweets it.