import discord
import urllib.parse
import requests
from discord.ext import commands
from core.cog import CogExtension
from tools.html_parser import parse_langrisser_wiki_search_result

base_uri = 'https://wiki.biligame.com/langrisser/index.php'


class LQuery(CogExtension):
    @commands.command()
    async def query(self, ctx):
        message = ctx.message.content
        key_word = message.lstrip('//query ')
        # query_string = urllib.parse.quote(key_word)
        search_result = requests.get(base_uri, params={'search': key_word})
        html_str = search_result.text
        result_uri = parse_langrisser_wiki_search_result(html_str)
        await ctx.send(result_uri)


def setup(bot):
    bot.add_cog(LQuery(bot))
