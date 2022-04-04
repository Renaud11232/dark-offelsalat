import argparse
import os
from darkoffelsalat import DarkOffelsalat


def main():
    parser = argparse.ArgumentParser(description="Starts the Dark Offelsalat bot")
    parser.add_argument("--log-level",
                        type=str,
                        default=os.environ.get("LOG_LEVEL") or "INFO",
                        help="Log level. If omitted, the value of the `LOG_LEVEL` environment variable will be used. Defaults to `INFO`"
                        )
    parser.add_argument("--twitch-token",
                        type=str,
                        default=os.environ.get("TWITCH_TOKEN"),
                        help="Token used to connect to twitch IRC. If omitted, the value of the `TWITCH_TOKEN` environment variable will be used."
                        )
    parser.add_argument("--youtube-token",
                        type=str,
                        default=os.environ.get("YOUTUBE_TOKEN"),
                        help="Token used to connect to the youtube API to fetch the latest video of a playlist. If omitted, the value of the `YOUTUBE_TOKEN` environment variable will be used."
                        )
    parser.add_argument("--youtube-playlist",
                        type=str,
                        default=os.environ.get("YOUTUBE_PLAYLIST"),
                        help="Playlist ID used from which the latest video will be fetched. If omitted, the value of the `YOUTUBE_PLAYLIST` environment variable will be used."
                        )
    parser.add_argument("--channel",
                        type=str,
                        default=os.environ.get("CHANNEL"),
                        help="The channel the bot will work on. If omitted, the value of the `CHANNEL` environment variable will be used."
                        )
    parser.add_argument("--message",
                        type=str,
                        default=os.environ.get("MESSAGE"),
                        help="The message that will be sent in chat. The placeholder {{url}} can be used to insert the fetched youtube video. If omitted, the value of the `MESSAGE` environment variable will be used."
                        )
    parser.add_argument("--timeout",
                        type=int,
                        default=os.environ.get("TIMEOUT") or 60 * 5,
                        help="Delay between each message of the bot (in seconds). If omitted, the value of the `TIMEOUT` environment variable will be used."
                        )
    parser.add_argument("words",
                        type=str,
                        help="The words that will trigger a bot response",
                        nargs="*"
                        )
    args = parser.parse_args()
    bot = DarkOffelsalat(
        twitch_token=args.twitch_token,
        log_level=args.log_level,
        channel=args.channel,
        words=args.words,
        youtube_token=args.youtube_token,
        timeout=args.timeout,
        message=args.message,
        youtube_playlist=args.youtube_playlist
    )
    bot.run()
