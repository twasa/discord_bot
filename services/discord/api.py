import discord
import os
from discord.ext import commands
from tools.log import logger


class BotApp(object):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.messages = True
        intents.typing = False
        intents.presences = False
        self.bot = commands.Bot(command_prefix='/', intents=intents)

    def load_extension(self):
        for filename in os.listdir('cmds'):
            if filename.endswith('.py'):
                ext_name = f'cmds.{filename[:-3]}'
                self.bot.load_extension(ext_name)

    def run(self, token):
        self.load_extension()
        self.bot.run(token)
