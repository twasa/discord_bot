from discord.ext import commands
from core.cog import CogExtension


class Global(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self, payload):
        pass

    @commands.Cog.listener()
    async def on_message(self, payload):
        if payload.author.bot or payload.content[0] == f'{self.bot.command_prefix}':
            return
        await self.bot.process_commands(payload)
        # channel = payload.channel
        # await channel.send("your message")


def setup(bot):
    bot.add_cog(Global(bot))
