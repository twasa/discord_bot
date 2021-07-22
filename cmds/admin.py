import discord
from discord.ext import commands
from core.cog import CogExtension

from tools.log import logger


class Admin(CogExtension):
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def load(self, ctx, extension_name):
        self.bot.load_extension(f'cmds.{extension_name}')
        await ctx.send(f'loaded {extension_name} done.')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unload(self, ctx, extension_name):
        self.bot.unload_extension(f'cmds.{extension_name}')
        await ctx.send(f'unloaded {extension_name} done.')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def reload(self, ctx, extension_name):
        # if ctx.message.author.guild_permissions.administrator:
        self.bot.reload_extension(f'cmds.{extension_name}')
        await ctx.send(f'reload {extension_name} done.')


def setup(bot):
    bot.add_cog(Admin(bot))
