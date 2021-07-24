from discord.ext import commands
from core.cog import CogExtension
from tools.log import logger


class Admin(CogExtension):
    @commands.command(administrator=True)
    async def ping(self, ctx):
        await ctx.send(f'{self.bot.latency * 1000} ms')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def load(self, ctx, extension_name):
        try:
            self.bot.load_extension(f'cmds.{extension_name}')
            await ctx.send(f'loaded {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unload(self, ctx, extension_name):
        try:
            self.bot.unload_extension(f'cmds.{extension_name}')
            await ctx.send(f'unloaded {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def reload(self, ctx, extension_name):
        try:
            # if ctx.message.author.guild_permissions.administrator:
            self.bot.reload_extension(f'cmds.{extension_name}')
            await ctx.send(f'reload {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))


def setup(bot):
    bot.add_cog(Admin(bot))
