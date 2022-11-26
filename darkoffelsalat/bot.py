import logging
import sys
import time
import twitchio
import twitchio.parse
import re
from pyyoutube import Api


class DarkOffelsalat(twitchio.Client):

    def __init__(self, log_level, twitch_token, youtube_token, channel, words, timeout, message, youtube_playlist):
        self.__logger = logging.getLogger("DarkOffelsalat")
        self.__logger.setLevel(logging.getLevelName(log_level))
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        self.__logger.info("Initializing Dark Offelsalat...")
        self.__words = words
        self.__last_message = 0
        self.__timeout = timeout
        self.__youtube_playlist = youtube_playlist
        self.__youtube = Api(api_key=youtube_token) if youtube_token else None
        self.__message = message
        twitchio.Client.__init__(self, token=twitch_token, initial_channels=[channel])

    async def event_ready(self):
        self.__logger.info("Dark Offelsalat is ready")

    async def event_message(self, message: twitchio.Message):
        if message.author is None:
            self.__logger.debug("Received message from the bot, ignoring it")
            return
        self.__logger.debug("Message: %s from %s" % (message.content, message.author.name))
        if not self.__message_matches(message):
            self.__logger.debug("Received message did not contain any matching word")
            return
        now = time.time()
        if now - self.__last_message < self.__timeout:
            self.__logger.debug("Message already sent recently, waiting")
            return
        self.__last_message = now
        if self.__youtube is None:
            await self.__send_text(message.channel)
        else:
            await self.__send_youtube(message.channel)

    async def event_raw_data(self, data):
        parsed = twitchio.parse.parser(data, self.nick)
        if parsed["action"] == "USERNOTICE" and parsed["badges"]["login"] == "streamelements" and parsed["badges"]["msg-id"] == "announcement":
            groups = re.match(r"^(.*?) lance le dé et tombe sur un\.\.\. (\d+)!$", parsed["message"])
            if groups:
                dice_value = int(groups.group(2))
                user = groups.group(1)
                self.__logger.debug("%s rolled the dice and got a %d" % (user, dice_value))
                channel = self.get_channel(parsed["channel"])
                if dice_value == 1:
                    await channel.send("@%s é-cheh-c critique" % user)
                elif dice_value == 20:
                    await channel.send("@%s noice" % user)
                elif dice_value < 10:
                    await channel.send("@%s cheh" % user)
                return

    def __message_matches(self, message: twitchio.Message):
        content = message.content.lower()
        return any(word.lower() in content for word in self.__words)

    async def __send_youtube(self, channel: twitchio.Channel):
        self.__logger.debug("Sending youtube message")
        response = self.__youtube.get_playlist_items(playlist_id=self.__youtube_playlist)
        video_id = response.items[0].snippet.resourceId.videoId
        url = "https://youtu.be/%s" % video_id
        message = self.__message.replace("{{url}}", url)
        await channel.send(message)

    async def __send_text(self, channel: twitchio.Channel):
        self.__logger.debug("Sending normal message")
        await channel.send(self.__message)

    def run(self):
        self.__logger.info("Starting Dark Offelsalat...")
        twitchio.Client.run(self)
