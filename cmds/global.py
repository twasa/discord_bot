import logging
import discord
from discord.ext import commands
from core.cog import CogExtension

logger = logging.getLogger(__name__)


class Global(CogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{self.bot.latency * 1000} ms')


def setup(bot):
    bot.add_cog(Global(bot))
