import urllib.parse
import requests
import inspect

from discord.ext import commands
from core.cog import CogExtension
from opencc import OpenCC

from tools.log import logger
from tools.html_parser import parse_langrisser_wiki_search_result

base_uri = 'https://wiki.biligame.com'
middle_name = 'langrisser'
search_uri = f'{base_uri}/{middle_name}/index.php'
cc = OpenCC('t2s')


class Langrisser(CogExtension):
    @commands.command()
    async def q(self, ctx):
        fn_name = inspect.stack()[0][3]
        cmd_prefix = self.bot.command_prefix
        message = ctx.message.content
        query_string = message.removeprefix(f'{cmd_prefix}{fn_name} ')
        try:
            response_obj = requests.get(search_uri, params={'search': cc.convert(query_string)})
        except Exception as e:
            logger.warning(str(e))
            return ctx.send(f'{base_uri} error')
        if response_obj.status_code != 200:
            await ctx.send(f'{base_uri} error')
        if response_obj.url.startswith(f'{base_uri}/{middle_name}'):
            await ctx.send(f'{urllib.parse.unquote(response_obj.url)}')
            return
        if result_uri := parse_langrisser_wiki_search_result(response_obj.text):
            await ctx.send(f'{base_uri}{urllib.parse.unquote(result_uri)}')
            return
        await ctx.send('query without result')


def setup(bot):
    bot.add_cog(Langrisser(bot))
