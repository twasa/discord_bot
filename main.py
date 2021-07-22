import os
from dotenv import load_dotenv

from tools.log import logger
from services.discord import api as discord_api

discord_bot = discord_api.BotApp()


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN', '')
    if not token:
        logger.error('missing token')
        exit(1)
    logger.info('Discord Bot starting...')
    discord_bot.run(token)
