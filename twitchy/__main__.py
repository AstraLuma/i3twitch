import configparser
import os
from twitchy.bot import TwitchBot

from gi.repository import Notify

Notify.init("i3 Twitch")

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.twitchrc'))

bot = TwitchBot(config['Twitch']['username'], config['Twitch']['oauth'])
bot.start()