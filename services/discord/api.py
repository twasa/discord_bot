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

    @commands.command()
    async def load(ctx, extension_name):
        self.bot.load_extension(f'cmds.{extension_name}')
        await ctx.send(f'loaded {extension_name} done.')

    @commands.command()
    async def unload(ctx, extension_name):
        self.bot.unload_extension(f'cmds.{extension_name}')
        await ctx.send(f'unloaded {extension_name} done.')

    @commands.command()
    async def reload(ctx, extension_name):
        bot.reload_extension(f'cmds.{extension_name}')
        await ctx.send(f'reload {extension_name} done.')

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
