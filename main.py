import os
import logging

from tools.log import logger
from services.discord import api as discord_api

discord_bot = discord_api.BotApp()
token = os.getenv('DISCORD_TOKEN', '')

if __name__ == '__main__':
    if not token:
        logger.error('missing token')
        exit(1)
    logger.info('Discord Bot starting...')
    discord_bot.run(token)
