import discord
from discord.ext import commands
from ..core import CogCore

class Admin(CogCore):
    @commands.command()
    async def load(self, ctx, extension):
        
        await ctx.send()

def setup(bot):
    bot.add_cog(Admin(bot))
