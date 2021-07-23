import urllib.parse
import requests

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
        message = ctx.message.content
        key_word = message.lstrip('//query ')
        # query_string = urllib.parse.quote(key_word)
        try:
            response_obj = requests.get(search_uri, params={'search': cc.convert(key_word)})
        except Exception as e:
            logger.info(str(e))
        if response_obj.status_code != 200:
            await ctx.send('langrisser wiki error')
        if response_obj.url.startswith(f'{base_uri}/{middle_name}'):
            await ctx.send(f'{urllib.parse.unquote(response_obj.url)}')
            return
        if result_uri := parse_langrisser_wiki_search_result(response_obj.text):
            await ctx.send(f'{base_uri}{urllib.parse.unquote(result_uri)}')
            return
        await ctx.send('找不到')


def setup(bot):
    bot.add_cog(Langrisser(bot))
