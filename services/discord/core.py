import discord
from discord.ext import commands

class CogCore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
