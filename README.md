# Dark Offelsalat

Dark Offelsalat is a silly project of mine... It all started as a joke during a twitch stream.
After clipping a rather funny moment of the stream, the idea of creating a bot that will present the clip to anyone joining the stream came to me.
The streamer wasn't against it, in fact in challenged me to do it before the end of the stream... Which obviously I did.
I mean... I had to !

I wasn't happy with the 1st version, so I made this one.

The name also comes from a joke... It's supposed to be the **dark side** of Kart Offelsalat.
Kart Offelsalat is one of my prank names that translates to "Potato salad" in german.

On a more serious note, this bot can be useful. It can post predefined messages when a chatter uses a given word.
It can also fetch the most recent video from a YouTube channel and include it in the message. 

The docker images can be used on `amd64` and `arm64` systems.

## Starting the bot

You can run this bot using docker CLI, docker-compose or running it directly on the host machine.

### Parameters

The various arguments the bots takes can be set using a command line flag or using an environment variable :
If the same option is set using both the command flag and the environment variable, the environment variable will be ignored.

| CLI argument         | Environment variable | Description                                                                                                          | Required | Default         |
|----------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| `--log-level`        | `LOG_LEVEL`          | The log level of the bot. The bot will never log the content of the received message or its author                   | No       | `INFO`          |
| `--twitch-token`     | `TWITCH_TOKEN`       | The twitch.tv token used to authenticate                                                                             | Yes      |                 |
| `--youtube-token`    | `YOUTUBE_TOKEN`      | The YouTube API token for fetching the latest video                                                                  | No       |                 |
| `--youtube-playlist` | `YOUTUBE_PLAYLIST`   | The YouTube playlist ID used to fetch the latest video                                                               | No       |                 |
| `--channel`          | `CHANNEL`            | The twitch channel that the bot will be chatting on                                                                  | Yes      |                 |
| `--message`          | `MESSAGE`            | The message that will be sent by the bot. Can include `{{url}}` that will be replaced by the url to the latest video | No       |                 |
| `--timeout`          | `TIMEOUT`            | The delay between each message send by the bot in seconds                                                            | Yes      | 300 (5 minutes) |
| `[args...]`          |                      | The list of words that will trigger a bot response                                                                   | Yes      |                 |


### Docker CLI

```bash
docker run \
  -d \
  --name darkoffelsalat \
  --restart unless-stopped \
  -e LOG_LEVEL=INFO \
  -e TWITCH_TOKEN=yourtwitchtoken \
  -e CHANNEL=twitchchannel \
  -e MESSAGE=The\ message\ to\ send\ including\ a\ {{url}} \
  -e TIMEOUT=300 \
  -e YOUTUBE_TOKEN=youtubetoken \
  -e YOUTUBE_PLAYLIST=yourplaylistid \
  ghcr.io/renaud11232/darkoffelsalat \
  some example words
```

### Docker-compose

`docker-compose.yml`:

```yml
version: "3"
services:
  darkoffelsalat:
    container_name: darkoffelsalat
    image: "ghcr.io/renaud11232/darkoffelsalat"
    environment:
      LOG_LEVEL: INFO
      TWITCH_TOKEN: yourtwitchtoken
      CHANNEL: twitchchannel
      MESSAGE: The message to send including a {{url}}
      TIMEOUT: 300
      YOUTUBE_TOKEN: youtubetoken
      YOUTUBE_PLAYLIST: yourplaylistid
    command:
      - some
      - example
      - words
    restart: unless-stopped
```

```bash
docker-compose up -d
```

### Bare metal

You can install this bot by running the following command (a venv is recommended) :

```bash
pip install "https://github.com/Renaud11232/dark-offelsalat/archive/refs/heads/master.zip"
```

Once it's installed you can start it either by setting the environment variables :
```bash
export LOG_LEVEL=INFO
export TWITCH_TOKEN=yourtwitchtoken
export CHANNEL=twitchchannel
export MESSAGE=The\ message\ to\ send\ including\ a\ {{url}}
export TIMEOUT=300
export YOUTUBE_TOKEN=youtubetoken
export YOUTUBE_PLAYLIST=yourplaylistid
darkoffelsalat some example words
```

Or by providing the correct flags :
```bash
darkoffelsalat \
  --log-level INFO \
  --twitch-token yourtwitchtoken \
  --channel twitchchannel \
  --message "The message to send including a {{url}}" \
  --timeout 300 \
  --youtube-token youtubetoken \
  --youtube-playlist yourplaylistid \
  some example words
```
