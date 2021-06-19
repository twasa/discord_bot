import logging
import discord
import os
from discord.ext import commands
from services.discord.manager import Manager

base_dir = os.getcwd()

class BotApp(object):
    def __init__(self):
        self.token = ''
        self.bot = commands.Bot(command_prefix='//')

    def load_extension(self):
        for filename in os.listdir('cmds'):
            if filename.endswith('.py'):
                ext_name = f'cmds.{filename[:-3]}'
                self.bot.load_extension(ext_name)

    def run(self, token):
        self.token = token
        self.bot.add_cog(Manager(self.bot))
        self.load_extension()
        self.bot.run(self.token)
