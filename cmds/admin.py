import inspect
from discord.ext import commands
from core.cog import CogExtension
from tools.log import logger


class Admin(CogExtension):
    @commands.command()
    async def ping(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            return
        await ctx.send(f'{self.bot.latency * 1000} ms')

    @commands.command()
    async def load(self, ctx, extension_name):
        if not ctx.author.guild_permissions.administrator:
            return
        try:
            self.bot.load_extension(f'cmds.{extension_name}')
            await ctx.send(f'loaded {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))

    @commands.command()
    async def unload(self, ctx, extension_name):
        if not ctx.author.guild_permissions.administrator:
            return
        cmd_file_path = inspect.stack()[0][1]
        self_extension_name = cmd_file_path.split('/')[-1].split('.')[0]
        if extension_name == self_extension_name:
            logger.warning(f'unload {extension_name} not allowed')
            return
        try:
            self.bot.unload_extension(f'cmds.{extension_name}')
            await ctx.send(f'unloaded {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))

    @commands.command()
    async def reload(self, ctx, extension_name):
        if not ctx.author.guild_permissions.administrator:
            return
        try:
            self.bot.reload_extension(f'cmds.{extension_name}')
            await ctx.send(f'reload {extension_name} done.')
        except Exception as e:
            logger.warning(str(e))


def setup(bot):
    bot.add_cog(Admin(bot))
